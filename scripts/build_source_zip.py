#!/usr/bin/env python3
"""Build an exploitable ZIP archive of the repository without VCS artifacts."""

from __future__ import annotations

from pathlib import Path
import sys
import zipfile

from build_source_archive import ROOT, DIST, excluded

ZIP_PATH = DIST / "nsi-enseignement_source_clean.zip"


def build_zip(root: Path = ROOT, target: Path = ZIP_PATH) -> Path:
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        target.unlink()
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(root.rglob("*")):
            rel = path.relative_to(root)
            if excluded(rel):
                continue
            if path == target:
                continue
            arcname = Path("nsi-enseignement") / rel
            if path.is_file():
                archive.write(path, arcname.as_posix())
    return target


def main() -> int:
    target = build_zip()
    print(f"build_source_zip: wrote {target.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
