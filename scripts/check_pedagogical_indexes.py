#!/usr/bin/env python3
"""Validate generated pedagogical indexes."""

from __future__ import annotations

from _qa_common import ROOT, print_result


INDEX_FILES = [
    "INDEX_BY_LEVEL.md",
    "INDEX_BY_THEME.md",
    "INDEX_BY_DOMAIN.md",
    "INDEX_BY_CHAPTER.md",
    "INDEX_BY_SEQUENCE.md",
    "INDEX_BY_SESSION.md",
    "INDEX_BY_DOCUMENT_TYPE.md",
    "INDEX_BY_CAPACITY.md",
    "INDEX_BY_AUDIENCE.md",
    "INDEX_BY_RAG_COLLECTION.md",
]
FORBIDDEN_MARKERS = (
    "AUDIT/",
    "dist/",
    ".git/",
    "Documents_DRIVE/",
    "rendus_eleves/",
    "NotesEleves.csv",
    "Fichier_Eleves.csv",
)


def main() -> None:
    errors: list[str] = []
    for name in INDEX_FILES:
        path = ROOT / name
        if not path.exists():
            errors.append(f"{name} absent")
            continue
        text = path.read_text(encoding="utf-8")
        if "Généré par `scripts/generate_pedagogical_indexes.py`" not in text:
            errors.append(f"{name}: marqueur de génération absent")
        if "03_progressions/supports/" not in text and "Aucune ressource" not in text:
            errors.append(f"{name}: aucune ressource canonique visible")
        for marker in FORBIDDEN_MARKERS:
            if marker in text:
                errors.append(f"{name}: marqueur interdit {marker}")
    print_result("check_pedagogical_indexes", errors)


if __name__ == "__main__":
    main()
