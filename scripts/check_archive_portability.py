#!/usr/bin/env python3
"""Check source_clean archive portability if the archive has been built."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "dist/source_clean"
FORBIDDEN_PARTS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".venv"}
FORBIDDEN_SUFFIXES = {".pyc", ".pyo", ".aux", ".log", ".toc", ".out", ".fls"}
FORBIDDEN_NAMES = {".DS_Store"}


def main() -> int:
    errors: list[str] = []
    if SOURCE.exists():
        for path in SOURCE.rglob("*"):
            rel = path.relative_to(SOURCE)
            if any(part in FORBIDDEN_PARTS for part in rel.parts):
                errors.append(f"forbidden path in archive: {rel}")
            if path.name in FORBIDDEN_NAMES or path.suffix in FORBIDDEN_SUFFIXES or path.name.endswith(".synctex.gz") or path.name.endswith(".fdb_latexmk"):
                errors.append(f"forbidden artifact in archive: {rel}")
    if errors:
        print("check_archive_portability: KO")
        for error in errors:
            print(f"- {error}")
        return 1
    if SOURCE.exists():
        print("check_archive_portability: PASS")
    else:
        print("check_archive_portability: PASS - source_clean not built in prototype audit")
    return 0

if __name__ == "__main__":
    sys.exit(main())
