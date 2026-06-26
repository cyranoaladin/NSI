from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_no_build_artifacts_in_index as artifacts


class BuildArtifactCheckTest(unittest.TestCase):
    def test_source_clean_zip_is_allowed_delivery_side_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            dist = root / "dist"
            dist.mkdir()
            (dist / "source_clean.tar.gz").write_bytes(b"tar")
            (dist / "git_bundle.bundle").write_bytes(b"bundle")
            (dist / "nsi-enseignement_source_clean.zip").write_bytes(b"zip")

            found = artifacts.find_artifacts(root, require_archives=True)

            self.assertEqual(found, [])

    def test_source_clean_zip_is_not_required_for_audit(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            dist = root / "dist"
            dist.mkdir()
            (dist / "source_clean.tar.gz").write_bytes(b"tar")
            (dist / "git_bundle.bundle").write_bytes(b"bundle")

            found = artifacts.find_artifacts(root, require_archives=True)

            self.assertEqual(found, [])

    def test_check_reports_python_cache_without_deleting_it(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            cache = root / "scripts" / "__pycache__"
            cache.mkdir(parents=True)
            pyc = cache / "module.cpython-312.pyc"
            pyc.write_bytes(b"bytecode")

            found = artifacts.find_artifacts(root, require_archives=False)

            self.assertIn(cache, found)
            self.assertIn(pyc, found)
            self.assertTrue(cache.exists())
            self.assertTrue(pyc.exists())


if __name__ == "__main__":
    unittest.main()
