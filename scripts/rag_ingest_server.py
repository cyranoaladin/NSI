#!/usr/bin/env python3
"""Server-side RAG ingestion via Chroma REST API + ollama embeddings.

Uses HTTP only (no pip chromadb required). Embedding via ollama ensures
dimension parity with prod retrieval (nomic-embed-text, 768d).

NEVER uses the Chroma default embedder (all-MiniLM-L6-v2, 384d).

Environment variables:
    CHROMA_URL      Chroma REST base URL  (default: http://127.0.0.1:8000)
    OLLAMA_URL      Ollama API base URL   (default: http://127.0.0.1:11434)
    EMBED_MODEL     Ollama embed model    (default: nomic-embed-text)
    TARGET_COLLECTION  Collection name    (default: nsi_corpus_v2)
    NSI_ROOT        Path to NSI repo root (default: cwd)

Usage (on server):
    NSI_ROOT=/tmp/nsi_ingest TARGET_COLLECTION=nsi_corpus_v2 python3 rag_ingest_server.py
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Configuration from environment (never hardcoded, token never logged)
# ---------------------------------------------------------------------------

CHROMA_URL = os.environ.get("CHROMA_URL", "http://127.0.0.1:8000")
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://127.0.0.1:11434")
EMBED_MODEL = os.environ.get("EMBED_MODEL", "nomic-embed-text")
TARGET_COLLECTION = os.environ.get("TARGET_COLLECTION", "nsi_corpus_v2")
NSI_ROOT = Path(os.environ.get("NSI_ROOT", "."))
EXPECTED_DIM = 768  # nomic-embed-text dimension; assert at runtime

TENANT = "default_tenant"
DB = "default_database"
BATCH_SIZE = 20

SOURCE_DIRS = [
    NSI_ROOT / "03_progressions" / "supports",
    NSI_ROOT / "03_progressions" / "fiches_cours",
]

# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------


def _http(method: str, url: str, data: dict[str, Any] | None = None) -> Any:
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(
        url, data=body, method=method,
        headers={"Content-Type": "application/json"} if body else {},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            raw = r.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        err = e.read().decode()[:300]
        if e.code == 409:
            return None  # collection already exists
        raise RuntimeError(f"HTTP {method} {url}: {e.code} {err}")


def embed(texts: list[str]) -> list[list[float]]:
    """Embed texts via ollama. Returns list of vectors (dim=EXPECTED_DIM)."""
    result = _http("POST", f"{OLLAMA_URL}/api/embed", {
        "model": EMBED_MODEL, "input": texts,
    })
    embeddings: list[list[float]] = result["embeddings"]
    if embeddings and len(embeddings[0]) != EXPECTED_DIM:
        raise RuntimeError(
            f"Embedding dimension {len(embeddings[0])} != expected {EXPECTED_DIM}. "
            f"Model {EMBED_MODEL} may have changed. STOP."
        )
    return embeddings


# ---------------------------------------------------------------------------
# Chroma REST v2
# ---------------------------------------------------------------------------

_BASE = f"{CHROMA_URL}/api/v2/tenants/{TENANT}/databases/{DB}"


def get_or_create_collection(name: str) -> str:
    """Return collection ID, creating if needed."""
    _http("POST", f"{_BASE}/collections", {
        "name": name, "metadata": {"hnsw:space": "cosine"},
    })
    cols: list[dict[str, Any]] = _http("GET", f"{_BASE}/collections")
    for c in cols:
        if c["name"] == name:
            return str(c["id"])
    raise RuntimeError(f"Collection {name} not found after creation")


def collection_count(col_id: str) -> int:
    url = f"{_BASE}/collections/{col_id}/count"
    with urllib.request.urlopen(url, timeout=30) as r:
        return int(r.read().decode())


def upsert(col_id: str, ids: list[str], docs: list[str],
           embs: list[list[float]], metas: list[dict[str, Any]]) -> None:
    _http("POST", f"{_BASE}/collections/{col_id}/upsert", {
        "ids": ids, "documents": docs, "embeddings": embs, "metadatas": metas,
    })


def delete_collection(name: str) -> None:
    cols: list[dict[str, Any]] = _http("GET", f"{_BASE}/collections")
    for c in cols:
        if c["name"] == name:
            _http("DELETE", f"{_BASE}/collections/{c['id']}")
            return


# ---------------------------------------------------------------------------
# Corpus parsing (mirrors rag_ingest.py logic)
# ---------------------------------------------------------------------------

def _parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    try:
        import yaml
        meta = yaml.safe_load(text[3:end]) or {}
    except Exception:
        meta = {}
    return (meta if isinstance(meta, dict) else {}), text[end + 4:].strip()


def _split_sections(body: str) -> list[tuple[str, str]]:
    sections: list[tuple[str, str]] = []
    anchor, lines = "", []  # type: ignore[var-annotated]
    for line in body.split("\n"):
        m = re.match(r"^(#{1,4})\s+(.+)", line)
        if m:
            if lines:
                t = "\n".join(lines).strip()
                if t:
                    sections.append((anchor, t))
            anchor = re.sub(r"[^a-z0-9]+", "-", m.group(2).strip().lower()).strip("-")
            lines = [line]
        else:
            lines.append(line)
    if lines:
        t = "\n".join(lines).strip()
        if t:
            sections.append((anchor, t))
    return sections


def build_chunks(path: Path) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8", errors="replace")
    meta, body = _parse_frontmatter(text)
    if meta.get("private_data") is True:
        return []

    rel = path.relative_to(NSI_ROOT).as_posix()
    fhash = hashlib.sha256(path.read_bytes()).hexdigest()

    level = str(meta.get("level", ""))
    if not level:
        level = "premiere" if "premiere" in rel else ("terminale" if "terminale" in rel else "")
    theme = str(meta.get("theme", ""))
    notion = str(meta.get("notion", ""))
    seq_id = str(meta.get("sequence_id", ""))
    if not seq_id:
        sm = re.search(r"[PT]\d{2}", rel)
        if sm:
            seq_id = sm.group(0)

    official = meta.get("official_program")
    raw_caps: Any = (
        official.get("capacities", []) if isinstance(official, dict)
        else meta.get("capacity_ids") or meta.get("capacities") or []
    )
    if isinstance(raw_caps, str):
        caps = [c.strip() for c in raw_caps.split(",") if c.strip()]
    elif isinstance(raw_caps, list):
        caps = [str(c) for c in raw_caps]
    else:
        caps = []
    caps_csv = ",".join(caps)

    sections = _split_sections(body) or [("", body)]
    chunks: list[dict[str, Any]] = []
    for idx, (anch, txt) in enumerate(sections):
        chunks.append({
            "id": f"{rel}#{anch or 'chunk'}-{idx}",
            "text": txt,
            "metadata": {
                "path": rel, "section_anchor": anch, "capacity_ids": caps_csv,
                "document_type": str(meta.get("document_type", path.suffix.lstrip("."))),
                "status": str(meta.get("status") or "needs_review"),
                "level": level, "theme": theme, "notion": notion,
                "sequence_id": seq_id, "sha256": fhash,
                "collection": TARGET_COLLECTION, "source_type": "nsi_corpus",
                "private_data": "false",
            },
        })
    return chunks


def iter_source_files() -> list[Path]:
    files: list[Path] = []
    for d in SOURCE_DIRS:
        if d.exists():
            for p in sorted(d.rglob("*")):
                if p.is_file() and p.suffix in {".md", ".py"} and "__pycache__" not in str(p):
                    files.append(p)
    return files


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    print(f"CHROMA_URL={CHROMA_URL}")
    print(f"OLLAMA_URL={OLLAMA_URL}")
    print(f"EMBED_MODEL={EMBED_MODEL} (expected dim={EXPECTED_DIM})")
    print(f"TARGET_COLLECTION={TARGET_COLLECTION}")
    print(f"NSI_ROOT={NSI_ROOT}")

    col_id = get_or_create_collection(TARGET_COLLECTION)
    print(f"Collection ID: {col_id}")

    files = iter_source_files()
    print(f"Files found: {len(files)}")

    all_chunks: list[dict[str, Any]] = []
    for p in files:
        all_chunks.extend(build_chunks(p))
    print(f"Chunks built: {len(all_chunks)}")

    ingested = 0
    for i in range(0, len(all_chunks), BATCH_SIZE):
        batch = all_chunks[i:i + BATCH_SIZE]
        texts = [c["text"] for c in batch]
        embs = embed(texts)
        upsert(
            col_id,
            ids=[c["id"] for c in batch],
            docs=texts,
            embs=embs,
            metas=[c["metadata"] for c in batch],
        )
        ingested += len(batch)
        if ingested % 200 == 0:
            print(f"  ingested {ingested}/{len(all_chunks)}")

    count = collection_count(col_id)
    print(f"DONE: {ingested} chunks ingested into {TARGET_COLLECTION}")
    print(f"Collection count: {count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
