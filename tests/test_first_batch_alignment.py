from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

import scripts.check_first_batch_alignment as alignment


class FirstBatchAlignmentTest(unittest.TestCase):
    def test_missing_td_correction_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            directory = root / "P00"
            directory.mkdir()
            (directory / "P00_cours_test.md").write_text(
                "Objectif O1 - diagnostiquer une trace\nCapacité : P-LANG-01\nErreur fréquente EF1 - confondre affectation et égalité\n",
                encoding="utf-8",
            )
            (directory / "P00_trace_test.md").write_text("Objectif O1\nCapacité : P-LANG-01\n", encoding="utf-8")
            (directory / "P00_td_test.md").write_text("### Exercice 1 - O1\nCapacité : P-LANG-01\n", encoding="utf-8")
            (directory / "P00_tp_test.md").write_text("Objectif O1\nCapacité : P-LANG-01\n", encoding="utf-8")
            (directory / "P00_corrige_test.md").write_text("### Corrigé exercice 2\n", encoding="utf-8")
            (directory / "P00_evaluation_test.md").write_text("### Question 1 - O1\nCapacité : P-LANG-01\n", encoding="utf-8")
            (directory / "P00_bareme_test.md").write_text("### Barème question 1\n", encoding="utf-8")
            (directory / "P00_remediation_test.md").write_text("Activité corrective EF1\n", encoding="utf-8")

            result = alignment.analyze_alignment(root, prefixes=["P00"], program_ids={"P-LANG-01"})

            self.assertTrue(any("Exercice 1" in error and "corrigé" in error for error in result.errors))

    def test_complete_alignment_passes(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            directory = root / "P00"
            directory.mkdir()
            (directory / "P00_cours_test.md").write_text(
                "Objectif O1 - diagnostiquer une trace\nCapacité : P-LANG-01\nErreur fréquente EF1 - confondre affectation et égalité\n",
                encoding="utf-8",
            )
            (directory / "P00_trace_test.md").write_text("Objectif O1\nCapacité : P-LANG-01\n", encoding="utf-8")
            (directory / "P00_td_test.md").write_text("### Exercice 1 - O1\nCapacité : P-LANG-01\n", encoding="utf-8")
            (directory / "P00_tp_test.md").write_text("Objectif O1\nCapacité : P-LANG-01\nLivrable vérifiable\n", encoding="utf-8")
            (directory / "P00_corrige_test.md").write_text("### Corrigé exercice 1\n", encoding="utf-8")
            (directory / "P00_evaluation_test.md").write_text("### Question 1 - O1\nCapacité : P-LANG-01\n", encoding="utf-8")
            (directory / "P00_bareme_test.md").write_text("### Barème question 1\n", encoding="utf-8")
            (directory / "P00_remediation_test.md").write_text("Activité corrective EF1\n", encoding="utf-8")

            result = alignment.analyze_alignment(root, prefixes=["P00"], program_ids={"P-LANG-01"})

            self.assertEqual(result.errors, [])


    def test_frontmatter_only_capacity_flagged(self) -> None:
        """Adverse: capacity declared in frontmatter but absent from TD/TP/eval → ROUGE."""
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            directory = root / "P00"
            directory.mkdir()
            # Course declares P-FAKE-99 in frontmatter only — NOT in body
            (directory / "P00_cours_test.md").write_text(
                "---\ntitle: test\nofficial_program:\n  capacities:\n    - P-FAKE-99\n---\n"
                "Objectif O1\nCapacité : P-LANG-01\nErreur fréquente EF1\n",
                encoding="utf-8",
            )
            (directory / "P00_trace_test.md").write_text("Objectif O1\nP-LANG-01\n", encoding="utf-8")
            (directory / "P00_td_test.md").write_text("### Exercice 1\nP-LANG-01\n", encoding="utf-8")
            (directory / "P00_tp_test.md").write_text("Objectif O1\nP-LANG-01\n", encoding="utf-8")
            (directory / "P00_corrige_test.md").write_text("### Corrigé exercice 1\n", encoding="utf-8")
            (directory / "P00_evaluation_test.md").write_text("### Question 1\nP-LANG-01\n", encoding="utf-8")
            (directory / "P00_bareme_test.md").write_text("### Barème question 1\n", encoding="utf-8")
            (directory / "P00_remediation_test.md").write_text("Activité corrective EF1\n", encoding="utf-8")

            result = alignment.analyze_alignment(root, prefixes=["P00"], program_ids={"P-LANG-01", "P-FAKE-99"})

            frontmatter_errors = [e for e in result.errors if "P-FAKE-99" in e]
            self.assertTrue(len(frontmatter_errors) >= 1, f"Expected P-FAKE-99 flagged, got: {result.errors}")
            self.assertTrue(any("non travaillée" in e or "non évaluée" in e for e in frontmatter_errors))

    def test_frontmatter_capacity_exercised_passes(self) -> None:
        """Capacity declared in frontmatter AND exercised in TD/eval → VERT."""
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            directory = root / "P00"
            directory.mkdir()
            (directory / "P00_cours_test.md").write_text(
                "---\ntitle: test\nofficial_program:\n  capacities:\n    - P-LANG-01\n---\n"
                "Objectif O1\nP-LANG-01\nErreur fréquente EF1\n",
                encoding="utf-8",
            )
            (directory / "P00_trace_test.md").write_text("Objectif O1\nP-LANG-01\n", encoding="utf-8")
            (directory / "P00_td_test.md").write_text("### Exercice 1\nP-LANG-01\n", encoding="utf-8")
            (directory / "P00_tp_test.md").write_text("Objectif O1\nP-LANG-01\n", encoding="utf-8")
            (directory / "P00_corrige_test.md").write_text("### Corrigé exercice 1\n", encoding="utf-8")
            (directory / "P00_evaluation_test.md").write_text("### Question 1\nP-LANG-01\n", encoding="utf-8")
            (directory / "P00_bareme_test.md").write_text("### Barème question 1\n", encoding="utf-8")
            (directory / "P00_remediation_test.md").write_text("Activité corrective EF1\n", encoding="utf-8")

            result = alignment.analyze_alignment(root, prefixes=["P00"], program_ids={"P-LANG-01"})

            self.assertEqual(result.errors, [])


if __name__ == "__main__":
    unittest.main()
