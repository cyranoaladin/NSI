#!/usr/bin/env python3
"""Build portable delivery artifacts without embedding .git in source archive."""
from __future__ import annotations

import os
import shutil
import subprocess
import tarfile
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
SOURCE_TAR = DIST / 'source_clean.tar.gz'
BUNDLE = DIST / 'git_bundle.bundle'
EXCLUDED_PARTS = {'.git', '__pycache__', '.pytest_cache', '.mypy_cache', '.ruff_cache', '.venv', 'dist', 'build', '01_build_reports'}
EXCLUDED_SUFFIXES = {'.pyc', '.pyo', '.aux', '.log', '.toc', '.out', '.fls'}
EXCLUDED_NAMES = {'.DS_Store'}

def excluded(rel: Path) -> bool:
    if any(part in EXCLUDED_PARTS for part in rel.parts):
        return True
    if rel.name in EXCLUDED_NAMES or rel.suffix in EXCLUDED_SUFFIXES:
        return True
    if rel.name.endswith('.synctex.gz') or rel.name.endswith('.fdb_latexmk'):
        return True
    return False

def copy_tree(target: Path) -> None:
    root_target = target / 'nsi-enseignement'
    root_target.mkdir(parents=True)
    for path in ROOT.rglob('*'):
        rel = path.relative_to(ROOT)
        if excluded(rel):
            continue
        dest = root_target / rel
        if path.is_dir():
            dest.mkdir(parents=True, exist_ok=True)
        elif path.is_file():
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, dest)

def main() -> int:
    DIST.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        copy_tree(tmp_path)
        if SOURCE_TAR.exists():
            SOURCE_TAR.unlink()
        with tarfile.open(SOURCE_TAR, 'w:gz') as tar:
            tar.add(tmp_path / 'nsi-enseignement', arcname='nsi-enseignement')
    result = subprocess.run(['git', 'bundle', 'create', str(BUNDLE), '--all'], cwd=ROOT)
    if result.returncode != 0:
        return result.returncode
    print(f'build_source_archive: wrote {SOURCE_TAR.relative_to(ROOT)}')
    print(f'build_source_archive: wrote {BUNDLE.relative_to(ROOT)}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
