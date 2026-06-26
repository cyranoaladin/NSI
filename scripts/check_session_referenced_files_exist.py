#!/usr/bin/env python3
"""Check that session planning does not rely on mostly missing documents."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SESSION_FILES = [
    ROOT / "03_progressions/seances_premiere.md",
    ROOT / "03_progressions/seances_terminale.md",
]
REGISTER = ROOT / "missing_documents_register.md"

# Pattern to capture filenames like P00_cours.md, T01_starter_3.py, carnet_de_bord.md
FILE_REF_RE = re.compile(r"\b([A-Za-z][A-Za-z0-9_]*\.[a-z]{2,4})\b")

# Fields that may contain file references
REF_FIELDS = {
    "Document utilisé",
    "Livrable",
    "Trace écrite",
    "Devoir ou préparation",
    "Remédiation",
    "Livrable projet",
}

# Files that are shared/global and not expected per-sequence
GLOBAL_ALLOWLIST = {"carnet_de_bord.md"}
REGISTER_COLUMNS = [
    "Fichier",
    "Séquence",
    "Type",
    "Priorité",
    "Statut",
    "Responsable",
    "Date cible",
    "Source possible",
    "Lien Drive éventuel",
    "Dépendance",
    "Décision",
]
CRITICAL_TYPES = {"cours", "td", "tp", "évaluation", "evaluation", "corrigé", "corrige", "trace", "trace écrite"}
DECISIONS = {"créer", "importer", "abandonner"}


def parse_register(path: Path) -> tuple[dict[str, dict[str, str]], list[str]]:
    """Parse missing_documents_register.md and validate row-level metadata."""
    if not path.exists():
        return {}, ["missing_documents_register.md absent"]
    rows: dict[str, dict[str, str]] = {}
    errors: list[str] = []
    header: list[str] | None = None
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.startswith("| ") or "---" in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if cells and cells[0] == "Fichier":
            header = cells
            if header != REGISTER_COLUMNS:
                errors.append("missing_documents_register.md: colonnes invalides")
            continue
        if not cells or header is None:
            continue
        if len(cells) != len(REGISTER_COLUMNS):
            errors.append(f"missing_documents_register.md: ligne mal formée -> {line[:120]}")
            continue
        row = dict(zip(REGISTER_COLUMNS, cells))
        filename = row["Fichier"].strip("`")
        rows[filename] = row
        if not filename:
            errors.append("missing_documents_register.md: fichier vide")
        for key in REGISTER_COLUMNS[1:]:
            if not row[key]:
                errors.append(f"{filename}: champ registre vide -> {key}")
        if row["Date cible"].lower() == "à définir":
            errors.append(f"{filename}: Date cible à définir interdite")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", row["Date cible"]):
            errors.append(f"{filename}: Date cible non ISO -> {row['Date cible']}")
        if row["Décision"].lower() not in DECISIONS:
            errors.append(f"{filename}: Décision invalide -> {row['Décision']}")
    return rows, errors


def extract_file_refs(session_path: Path) -> list[tuple[str, str, str]]:
    """Return list of (session_id, field, filename) for all file references."""
    refs: list[tuple[str, str, str]] = []
    text = session_path.read_text(encoding="utf-8", errors="replace")
    blocks = re.split(r"(?=^### Séance )", text, flags=re.M)
    for block in blocks:
        if not block.startswith("### Séance "):
            continue
        header = block.splitlines()[0].strip()
        session_id = header.replace("### Séance ", "").strip()
        for line in block.splitlines()[1:]:
            if not line.startswith("- ") or " : " not in line:
                continue
            key, value = line[2:].split(" : ", 1)
            key = key.strip()
            if key not in REF_FIELDS:
                continue
            for match in FILE_REF_RE.finditer(value):
                filename = match.group(1)
                # Skip purely numeric or very short non-file tokens
                if len(filename) < 4:
                    continue
                refs.append((session_id, key, filename))
    return refs


def file_exists_anywhere(filename: str) -> bool:
    """Check if a file exists anywhere in the project tree."""
    for p in ROOT.rglob(filename):
        if p.is_file():
            return True
    return False


def main() -> None:
    register_rows, register_errors = parse_register(REGISTER)
    errors: list[str] = []
    seen: set[str] = set()
    unique_refs = 0
    missing: list[tuple[str, str, str]] = []

    for session_path in SESSION_FILES:
        if not session_path.exists():
            errors.append(f"session file missing: {session_path.name}")
            continue
        refs = extract_file_refs(session_path)
        for session_id, field, filename in refs:
            if filename in GLOBAL_ALLOWLIST:
                continue
            if filename in seen:
                continue
            seen.add(filename)
            unique_refs += 1
            if not file_exists_anywhere(filename):
                missing.append((session_id, field, filename))

    errors.extend(register_errors)

    missing_ratio = (len(missing) / unique_refs) if unique_refs else 0.0
    if missing_ratio > 0.20:
        errors.append(f"taux de fichiers cités absents trop élevé: {len(missing)}/{unique_refs} = {missing_ratio:.1%}")

    high_priority_missing = 0
    for session_id, field, filename in missing:
        row = register_rows.get(filename)
        if row is None:
            errors.append(f"{session_id} ({field}): {filename} absent et non inscrit au registre")
            continue
        priority = row["Priorité"].lower()
        doc_type = row["Type"].lower()
        if priority == "haute":
            high_priority_missing += 1
        if priority == "haute" or doc_type in CRITICAL_TYPES:
            if row["Date cible"].lower() == "à définir" or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", row["Date cible"]):
                errors.append(f"{filename}: absence critique sans date cible précise")

    if high_priority_missing > 30:
        errors.append(f"trop de fichiers haute priorité absents: {high_priority_missing} > 30")

    if errors:
        print("check_session_referenced_files_exist: KO")
        for e in errors:
            print(f"- {e}")
        sys.exit(1)
    print("check_session_referenced_files_exist: PASS")


if __name__ == "__main__":
    main()
