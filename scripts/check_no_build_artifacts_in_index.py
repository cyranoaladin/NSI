#!/usr/bin/env python3
"""Check index and repository tree for build/cache artifacts."""

from __future__ import annotations

from typing import List

from _qa_common import ROOT, print_result

INDEX = ROOT / "INDEX.md"
FORBIDDEN_DIRS = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".venv", "build", "dist"}
FORBIDDEN_NAMES = {".DS_Store"}
FORBIDDEN_SUFFIXES = {
    ".pyc",
    ".pyo",
    ".aux",
    ".log",
    ".toc",
    ".out",
    ".synctex.gz",
    ".fdb_latexmk",
    ".fls",
}


def forbidden_path(path_text: str) -> bool:
    parts = set(path_text.split("/"))
    if parts.intersection(FORBIDDEN_DIRS):
        return True
    if any(path_text.endswith(suffix) for suffix in FORBIDDEN_SUFFIXES):
        return True
    return any(name in path_text for name in FORBIDDEN_NAMES)


def main() -> None:
    errors: List[str] = []
    if INDEX.exists():
        for line in INDEX.read_text(encoding="utf-8", errors="replace").splitlines():
            if "`" in line:
                candidate = line.strip().strip("- ").strip("`")
                if forbidden_path(candidate):
                    errors.append(f"INDEX.md: artefact référencé -> {candidate}")

    for path in sorted(ROOT.rglob("*")):
        rel = path.relative_to(ROOT).as_posix()
        if ".git" in path.parts:
            continue
        if path.is_dir() and path.name in FORBIDDEN_DIRS:
            errors.append(f"{rel}/: répertoire artefact présent")
        if path.is_file() and (path.name in FORBIDDEN_NAMES or any(path.name.endswith(s) for s in FORBIDDEN_SUFFIXES)):
            errors.append(f"{rel}: fichier artefact présent")

    print_result("check_no_build_artifacts_in_index", errors)


if __name__ == "__main__":
    main()
