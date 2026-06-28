from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class AuditExtractedSourceNoHangTest(unittest.TestCase):
    def test_makefile_uses_bounded_tp_runtime_gate(self) -> None:
        makefile = (ROOT / "Makefile").read_text(encoding="utf-8")

        self.assertIn("timeout 90 python -u scripts/check_tp_pedagogical_assets_runtime.py", makefile)
        self.assertNotIn("\n\tpython scripts/check_tp_pedagogical_assets.py", makefile)

    def test_source_clean_audit_extracted_source_finishes_without_drive_mirror(self) -> None:
        completed_build = subprocess.run(
            [sys.executable, "scripts/build_source_archive.py"],
            cwd=ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=60,
        )
        self.assertEqual(completed_build.returncode, 0, completed_build.stdout)

        archive = ROOT / "dist" / "source_clean.tar.gz"
        self.assertTrue(archive.exists(), "dist/source_clean.tar.gz doit être généré par ce test")
        with tempfile.TemporaryDirectory() as raw:
            completed_extract = subprocess.run(
                ["tar", "-xzf", str(archive), "-C", raw],
                cwd=ROOT,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                timeout=30,
            )
            self.assertEqual(completed_extract.returncode, 0, completed_extract.stdout)

            extracted = Path(raw) / "nsi-enseignement"
            env = os.environ.copy()
            env.pop("NSI_DOCUMENTS_DRIVE_ROOT", None)
            env["PYTHONDONTWRITEBYTECODE"] = "1"
            completed_audit = subprocess.run(
                ["timeout", "180", "make", "audit-extracted-source"],
                cwd=extracted,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                timeout=190,
            )
            self.assertEqual(completed_audit.returncode, 0, completed_audit.stdout)
            residue = list(extracted.rglob("__pycache__")) + list(extracted.rglob("*.pyc"))
            if residue:
                for path in residue:
                    if path.is_dir():
                        shutil.rmtree(path)
                    else:
                        path.unlink()
            self.assertEqual([], residue)


if __name__ == "__main__":
    unittest.main()
