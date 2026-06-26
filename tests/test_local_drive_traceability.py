from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_local_drive_traceability as drive_trace


class LocalDriveTraceabilityTest(unittest.TestCase):
    def test_candidate_source_without_trace_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            support = root / "P01_cours_test.md"
            support.write_text(
                "---\nsource: \"BO 2019 ; ressource locale candidate : Documents_DRIVE/missing.pdf\"\n---\n",
                encoding="utf-8",
            )

            result = drive_trace.analyze_drive_traceability(root, trace_path=root / "support_source_trace.yml")

            self.assertTrue(any("ressource locale candidate" in error for error in result.errors))

    def test_generated_from_program_is_accepted_without_drive_source(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            support = root / "P01_cours_test.md"
            support.write_text(
                "---\nsource: \"BO 2019\"\nsource_creation: \"generated_from_program\"\n---\n",
                encoding="utf-8",
            )
            (root / "support_source_trace.yml").write_text(
                "supports:\n"
                "  - support: P01_cours_test.md\n"
                "    source_officielle: BO 2019\n"
                "    source_locale_drive: ''\n"
                "    type_reprise: création originale\n"
                "    hash_source: ''\n"
                "    statut_rgpd: non concerné\n"
                "    statut_relecture: needs_review\n",
                encoding="utf-8",
            )

            result = drive_trace.analyze_drive_traceability(root, trace_path=root / "support_source_trace.yml")

            self.assertEqual(result.errors, [])


if __name__ == "__main__":
    unittest.main()
