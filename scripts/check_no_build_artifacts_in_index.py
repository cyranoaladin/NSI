#!/usr/bin/env python3
"""Reject uncontrolled build artifacts while allowing required delivery archives."""

from __future__ import annotations

import sys
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_DIST = {
    Path('dist/source_clean.tar.gz'),
    Path('dist/git_bundle.bundle'),
}
FORBIDDEN_DIRS = {
    '__pycache__',
    '.pytest_cache',
    '.mypy_cache',
    '.ruff_cache',
    '.venv',
    'build',
}
FORBIDDEN_SUFFIXES = {
    '.pyc',
    '.pyo',
    '.aux',
    '.log',
    '.toc',
    '.out',
    '.fls',
}
FORBIDDEN_NAMES = {'.DS_Store'}


def cleanup_python_bytecode() -> None:
    for path in ROOT.rglob('__pycache__'):
        if path.is_dir():
            shutil.rmtree(path)
    for path in ROOT.rglob('*.py[co]'):
        if '.git' not in path.relative_to(ROOT).parts and path.is_file():
            path.unlink()


def is_forbidden(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    if rel in ALLOWED_DIST:
        return False
    if rel == Path('dist'):
        return False
    if rel.parts and rel.parts[0] == 'dist':
        return True
    if any(part in FORBIDDEN_DIRS for part in rel.parts):
        return True
    if path.name in FORBIDDEN_NAMES:
        return True
    if path.suffix in FORBIDDEN_SUFFIXES:
        return True
    if path.name.endswith('.synctex.gz') or path.name.endswith('.fdb_latexmk'):
        return True
    return False


def main() -> int:
    cleanup_python_bytecode()
    errors: list[str] = []
    for path in ROOT.rglob('*'):
        if path == ROOT / '.git':
            continue
        if '.git' in path.relative_to(ROOT).parts:
            continue
        if path.exists() and is_forbidden(path):
            errors.append(f"{path.relative_to(ROOT)}: artefact interdit")
    missing = [str(item) for item in ALLOWED_DIST if not (ROOT / item).exists()]
    if missing:
        errors.append('archives de livraison absentes: ' + ', '.join(sorted(missing)))
    if errors:
        print('check_no_build_artifacts_in_index: KO')
        for error in errors:
            print(f'- {error}')
        return 1
    print('check_no_build_artifacts_in_index: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
