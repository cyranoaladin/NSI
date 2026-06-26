from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_operational_supports_no_indicative_debt as operational_debt


class ConsolidationStrictTest(unittest.TestCase):
    def test_operational_tp_depth_threshold_is_not_relaxed(self) -> None:
        self.assertGreaterEqual(operational_debt.MIN_LINES["tp"], 80)

    def test_drive_resolution_uses_repo_context_not_absolute_home_path(self) -> None:
        import _drive_paths

        with tempfile.TemporaryDirectory() as raw:
            workspace = Path(raw)
            repo = workspace / "nsi-enseignement"
            repo.mkdir()
            drive = workspace / "Documents_DRIVE"
            drive.mkdir()
            candidate = drive / "source.md"
            candidate.write_text("source locale", encoding="utf-8")

            resolved = _drive_paths.resolve_drive_reference("Documents_DRIVE/source.md", repo)

            self.assertEqual(resolved, candidate)

    def test_drive_scripts_do_not_embed_local_absolute_home_path(self) -> None:
        for relative in [
            "scripts/check_local_drive_traceability.py",
            "scripts/check_drive_integration_plan.py",
        ]:
            text = (ROOT / relative).read_text(encoding="utf-8")
            self.assertNotIn("/home/alaeddine", text)


if __name__ == "__main__":
    unittest.main()
