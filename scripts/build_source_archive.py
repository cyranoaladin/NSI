#!/usr/bin/env python3
"""Build portable delivery modes without publishing pedagogy."""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
SOURCE = DIST / "source_clean"
BUNDLE = DIST / "git_bundle"
EXCLUDED_NAMES = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".venv", "dist", "build", "01_build_reports"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo", ".aux", ".log", ".toc", ".out", ".fls"}
EXCLUDED_EXACT = {".DS_Store"}


def excluded(path: Path) -> bool:
    if any(part in EXCLUDED_NAMES for part in path.parts):
        return True
    if path.name in EXCLUDED_EXACT:
        return True
    if path.suffix in EXCLUDED_SUFFIXES:
        return True
    if path.name.endswith(".synctex.gz") or path.name.endswith(".fdb_latexmk"):
        return True
    return False


def copy_source() -> None:
    if SOURCE.exists():
        shutil.rmtree(SOURCE)
    target_root = SOURCE / "nsi-enseignement"
    target_root.mkdir(parents=True)
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)
        if excluded(rel):
            continue
        target = target_root / rel
        if path.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        elif path.is_file():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)


def build_bundle() -> None:
    BUNDLE.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(["git", "bundle", "create", str(BUNDLE / "nsi-enseignement.bundle"), "--all"], cwd=ROOT)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def main() -> int:
    copy_source()
    build_bundle()
    print("build_source_archive: generated dist/source_clean and dist/git_bundle")
    return 0

if __name__ == "__main__":
    sys.exit(main())
