#!/usr/bin/env python3
"""Deterministic, idempotent RAG ingestion pipeline.

Walks the content tree, chunks Markdown by section, attaches canonical
metadata, and upserts into a ChromaDB collection.  Reuses the privacy
and sensitive-drive guards to refuse PII/Drive content.

Usage:
    python -m scripts.rag_ingest --db /tmp/chroma_ephemeral
    python -m scripts.rag_ingest --db /tmp/chroma_ephemeral --dry-run
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent

# Canonical source directories (only these feed nsi_corpus).
SOURCE_DIRS = [
    ROOT / "03_progressions" / "supports",
    ROOT / "03_progressions" / "fiches_cours",
]

EXCLUSIONS = {".git", ".venv", "__pycache__", "dist", "AUDIT", "Documents_DRIVE"}
EXCLUDED_FILES = {"NotesEleves.csv", "Fichier_Eleves.csv"}


# ---------------------------------------------------------------------------
# Privacy guard: reuse the existing check (import at call time to avoid
# circular issues during collection)
# ---------------------------------------------------------------------------

def _file_has_pii(path: Path, text: str) -> bool:
    """Return True if the file triggers a hard privacy alert."""
    from scripts.check_no_private_data import (
        EMAIL_RE, FR_PHONE_RE, TN_PHONE_RE, ADDRESS_RE,
        ISO_DATE_RE, YEAR_RANGE_RE,
        is_hex_hash_context, is_population_context,
        load_allowlist, allowed,
    )
    allowlist = load_allowlist()
    for regex in [EMAIL_RE, FR_PHONE_RE, TN_PHONE_RE, ADDRESS_RE]:
        for match in regex.finditer(text):
            value = match.group(0)
            if regex in (FR_PHONE_RE, TN_PHONE_RE):
                if ISO_DATE_RE.fullmatch(value) or YEAR_RANGE_RE.fullmatch(value):
                    continue
                if is_population_context(text, match.start(), match.end()):
                    continue
                if is_hex_hash_context(text, match.start(), match.end()):
                    continue
            if not allowed(value, allowlist) and not allowed(
                str(path.relative_to(ROOT)), allowlist
            ):
                return True
    return False


# ---------------------------------------------------------------------------
# Frontmatter & chunking (deterministic, stable boundaries)
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    import yaml
    try:
        meta = yaml.safe_load(text[3:end]) or {}
    except Exception:
        meta = {}
    return (meta if isinstance(meta, dict) else {}), text[end + 4:].strip()


def split_sections(body: str) -> list[tuple[str, str]]:
    """Split body into (section_anchor, text) tuples at ## / ### boundaries."""
    sections: list[tuple[str, str]] = []
    anchor = ""
    lines: list[str] = []
    for line in body.split("\n"):
        m = re.match(r"^(#{1,4})\s+(.+)", line)
        if m:
            if lines:
                txt = "\n".join(lines).strip()
                if txt:
                    sections.append((anchor, txt))
            anchor = re.sub(r"[^a-z0-9àâäéèêëïîôùûüÿçæœ]+", "-",
                            m.group(2).strip().lower()).strip("-")
            lines = [line]
        else:
            lines.append(line)
    if lines:
        txt = "\n".join(lines).strip()
        if txt:
            sections.append((anchor, txt))
    return sections


def sha256_str(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


# ---------------------------------------------------------------------------
# Chunk model
# ---------------------------------------------------------------------------

@dataclass
class Chunk:
    id: str
    text: str
    metadata: dict[str, Any]


# ---------------------------------------------------------------------------
# Retrieval contract adapter: CSV -> list for API consumers
# ---------------------------------------------------------------------------

def adapt_metadata(raw: dict[str, Any]) -> dict[str, Any]:
    """Convert stored scalar metadata back to canonical types.

    Chroma stores capacity_ids as CSV string; the adapter returns a list.
    """
    out = dict(raw)
    csv_val = out.get("capacity_ids", "")
    if isinstance(csv_val, str):
        out["capacity_ids"] = [c for c in csv_val.split(",") if c] if csv_val else []
    return out


# ---------------------------------------------------------------------------
# Ingestion report
# ---------------------------------------------------------------------------

@dataclass
class IngestReport:
    files_seen: int = 0
    files_ingested: int = 0
    files_skipped_pii: int = 0
    files_skipped_unchanged: int = 0
    chunks_upserted: int = 0
    errors: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------

def iter_source_files() -> list[Path]:
    files: list[Path] = []
    for d in SOURCE_DIRS:
        if d.exists():
            for p in sorted(d.rglob("*")):
                if p.is_file() and p.suffix in {".md", ".py"}:
                    if not any(part in EXCLUSIONS for part in p.parts):
                        if p.name not in EXCLUDED_FILES:
                            files.append(p)
    return files


def build_chunks(path: Path) -> list[Chunk]:
    text = path.read_text(encoding="utf-8", errors="replace")

    # PII guard
    if _file_has_pii(path, text):
        return []

    meta, body = parse_frontmatter(text)
    if meta.get("private_data") is True:
        return []

    rel = path.relative_to(ROOT).as_posix()
    file_hash = sha256_file(path)

    # Read level/theme/notion/sequence_id from frontmatter (not from path regex)
    level = str(meta.get("level", ""))
    theme = str(meta.get("theme", ""))
    notion = str(meta.get("notion", ""))
    sequence_id = str(meta.get("sequence_id", ""))

    # capacity_ids: canonical location is official_program.capacities
    official = meta.get("official_program")
    if isinstance(official, dict):
        raw_caps = official.get("capacities", [])
    else:
        raw_caps = meta.get("capacity_ids") or meta.get("capacities") or []
    if isinstance(raw_caps, str):
        capacity_ids = [c.strip() for c in raw_caps.split(",") if c.strip()]
    elif isinstance(raw_caps, list):
        capacity_ids = [str(c) for c in raw_caps]
    else:
        capacity_ids = []

    sections = split_sections(body)
    if not sections:
        sections = [("", body)]

    chunks: list[Chunk] = []
    for idx, (anchor, section_text) in enumerate(sections):
        chunk_id = f"{rel}#{anchor or 'chunk'}-{idx}"
        # Chroma only accepts scalar metadata values — serialize lists to CSV.
        capacity_ids_csv = ",".join(capacity_ids)
        chunks.append(Chunk(
            id=chunk_id,
            text=section_text,
            metadata={
                "path": rel,
                "section_anchor": anchor,
                "capacity_ids": capacity_ids_csv,  # CSV string for Chroma
                "document_type": str(meta.get("document_type", path.suffix.lstrip("."))),
                "status": str(meta.get("status") or meta.get("statut") or "needs_review"),
                "level": level,
                "theme": theme,
                "notion": notion,
                "sequence_id": sequence_id,
                "sha256": file_hash,
                "collection": "nsi_corpus",
                "source_type": "nsi_corpus",
                "private_data": False,
            },
        ))
    return chunks


def ingest(
    db_path: Path,
    *,
    collection_name: str = "nsi_corpus",
    dry_run: bool = False,
    embedding_fn: Any = None,
) -> IngestReport:
    report = IngestReport()

    if not dry_run:
        try:
            import chromadb
        except ImportError:
            print("ERREUR: pip install chromadb", file=sys.stderr)
            sys.exit(1)
        client = chromadb.PersistentClient(path=str(db_path))
        col_kwargs: dict[str, Any] = {"name": collection_name}
        if embedding_fn is not None:
            col_kwargs["embedding_function"] = embedding_fn
        collection = client.get_or_create_collection(**col_kwargs)
        existing_ids = set(collection.get()["ids"])
    else:
        existing_ids = set()

    all_chunks: list[Chunk] = []
    for path in iter_source_files():
        report.files_seen += 1
        chunks = build_chunks(path)
        if not chunks:
            report.files_skipped_pii += 1
            continue
        report.files_ingested += 1
        all_chunks.extend(chunks)

    new_ids = {c.id for c in all_chunks}
    to_upsert = [c for c in all_chunks if c.id not in existing_ids or True]  # always upsert for idempotence

    if not dry_run and to_upsert:
        # Batch upsert
        batch_size = 100
        for i in range(0, len(to_upsert), batch_size):
            batch = to_upsert[i:i + batch_size]
            collection.upsert(
                ids=[c.id for c in batch],
                documents=[c.text for c in batch],
                metadatas=[c.metadata for c in batch],
            )

        # Remove stale IDs
        stale = existing_ids - new_ids
        if stale:
            collection.delete(ids=list(stale))

    report.chunks_upserted = len(to_upsert)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest NSI corpus into ChromaDB.")
    parser.add_argument("--db", type=Path, default=Path("/tmp/chroma_nsi_ephemeral"))
    parser.add_argument("--collection", default="nsi_corpus")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    report = ingest(args.db, collection_name=args.collection, dry_run=args.dry_run)
    print(json.dumps({
        "files_seen": report.files_seen,
        "files_ingested": report.files_ingested,
        "files_skipped_pii": report.files_skipped_pii,
        "chunks_upserted": report.chunks_upserted,
        "errors": report.errors,
        "dry_run": args.dry_run,
    }, indent=2))
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
