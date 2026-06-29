#!/usr/bin/env python3
"""Run audit-extracted-source from the source_clean archive in Git checkouts."""

from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def _assert_inside(path: Path, root: Path, message: str) -> None:
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError as exc:
        raise ValueError(message) from exc


def safe_extract_tar(archive: tarfile.TarFile, destination: Path) -> None:
    """Extract a tar archive after validating every member path and link."""
    destination.mkdir(parents=True, exist_ok=True)
    resolved_destination = destination.resolve()
    members = archive.getmembers()
    for member in members:
        member_name = member.name
        if Path(member_name).is_absolute():
            raise ValueError(f"chemin absolu interdit dans l'archive: {member_name}")
        target = destination / member_name
        _assert_inside(target, resolved_destination, f"chemin sortant interdit dans l'archive: {member_name}")
        if member.isdev():
            raise ValueError(f"fichier spécial interdit dans l'archive: {member_name}")
        if member.mode & 0o7000:
            raise ValueError(f"permissions dangereuses interdites dans l'archive: {member_name}")
        if member.issym() or member.islnk():
            link = Path(member.linkname)
            if link.is_absolute():
                raise ValueError(f"lien absolu interdit dans l'archive: {member_name}")
            link_target = target.parent / link
            _assert_inside(
                link_target,
                resolved_destination,
                f"lien sortant interdit dans l'archive: {member_name}",
            )
    archive.extractall(destination, members=members, filter="data")


def extracted_root(temp_path: Path) -> Path:
    expected = temp_path / "nsi-enseignement"
    if expected.exists():
        return expected
    candidates = [path for path in temp_path.iterdir() if path.is_dir()]
    if len(candidates) == 1:
        return candidates[0]
    raise FileNotFoundError("racine nsi-enseignement absente de source_clean.tar.gz")


def run_audit_extracted_source(root: Path = ROOT) -> int:
    archive = root / "dist" / "source_clean.tar.gz"
    if not archive.exists():
        print("run_audit_extracted_source: KO - dist/source_clean.tar.gz absent")
        return 1
    with tempfile.TemporaryDirectory() as raw:
        temp_path = Path(raw)
        with tarfile.open(archive, "r:gz") as handle:
            safe_extract_tar(handle, temp_path)
        audit_root = extracted_root(temp_path)
        env = os.environ.copy()
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        env.pop("NSI_DOCUMENTS_DRIVE_ROOT", None)
        completed = subprocess.run(["make", "audit-extracted-source"], cwd=audit_root, env=env)
        return completed.returncode


def main() -> int:
    return run_audit_extracted_source()


if __name__ == "__main__":
    sys.exit(main())
