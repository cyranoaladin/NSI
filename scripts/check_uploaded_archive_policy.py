#!/usr/bin/env python3
"""Check delivery policy: no global archive containing .git, only clean source and bundle."""
from __future__ import annotations

import sys
import tarfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "delivery_policy.md"
ALLOWED = {ROOT / "dist/source_clean.tar.gz", ROOT / "dist/git_bundle.bundle"}
FORBIDDEN_NAMES = {"NSI.tar", "NSI.tar.gz", "nsi.tar", "nsi.tar.gz", "archive.tar", "archive.tar.gz"}


def archive_contains_git(path: Path) -> bool:
    try:
        if path.suffix == ".zip":
            with zipfile.ZipFile(path) as archive:
                return any("/.git/" in name or name.startswith(".git/") for name in archive.namelist())
        if path.name.endswith(".tar") or path.name.endswith(".tar.gz") or path.name.endswith(".tgz"):
            with tarfile.open(path) as archive:
                return any("/.git/" in member.name or member.name.startswith(".git/") for member in archive.getmembers())
    except Exception:
        return True
    return False


def main() -> int:
    errors: list[str] = []
    if not POLICY.exists():
        errors.append("delivery_policy.md absent")
    for required in ALLOWED:
        if not required.exists():
            errors.append(f"required delivery artifact absent: {required.relative_to(ROOT)}")
    for path in ROOT.iterdir():
        if path.name in FORBIDDEN_NAMES:
            errors.append(f"forbidden global archive present: {path.name}")
        if path.is_file() and path not in ALLOWED and (path.name.endswith(".tar") or path.name.endswith(".tar.gz") or path.name.endswith(".tgz") or path.suffix == ".zip"):
            if archive_contains_git(path):
                errors.append(f"archive contains or may contain .git: {path.name}")
    if errors:
        print("check_uploaded_archive_policy: KO")
        for error in errors:
            print(f"- {error}")
        return 1
    print("check_uploaded_archive_policy: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
