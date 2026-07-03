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


    def test_known_failure_is_warning_not_error(self) -> None:
        """Known-failure listed in yml → WARNING, gate PASS (not KO)."""
        import scripts.check_first_batch_alignment as mod
        original = mod.KNOWN_FAILURES_PATH
        try:
            with tempfile.TemporaryDirectory() as raw:
                root = Path(raw)
                kf = root / "known.yml"
                kf.write_text(
                    "known_failures:\n  - id: P-FAKE-99\n    prefix: P00\n    reason: test\n    resolution: PR B\n",
                    encoding="utf-8",
                )
                mod.KNOWN_FAILURES_PATH = kf  # type: ignore[assignment]
                # Same fixture as frontmatter-only test
                directory = root / "P00"
                directory.mkdir()
                (directory / "P00_cours_test.md").write_text(
                    "---\ntitle: t\nofficial_program:\n  capacities:\n    - P-FAKE-99\n---\nObjectif O1\nP-LANG-01\nErreur fréquente EF1\n",
                    encoding="utf-8",
                )
                for kind, content in [
                    ("trace", "Objectif O1\nP-LANG-01\n"),
                    ("td", "### Exercice 1\nP-LANG-01\n"),
                    ("tp", "Objectif O1\nP-LANG-01\n"),
                    ("corrige", "### Corrigé exercice 1\n"),
                    ("evaluation", "### Question 1\nP-LANG-01\n"),
                    ("bareme", "### Barème question 1\n"),
                    ("remediation", "Activité corrective EF1\n"),
                ]:
                    (directory / f"P00_{kind}_test.md").write_text(content, encoding="utf-8")

                result = mod.analyze_alignment(root, prefixes=["P00"], program_ids={"P-LANG-01", "P-FAKE-99"})
                # Errors exist but main() should return 0 (all are known)
                self.assertTrue(len(result.errors) >= 1)
                # Simulate main() logic
                known = mod._load_known_failures()
                hard = [e for e in result.errors if not any(
                    e.startswith(f"{p}:") and cid in e for p, cid in known)]
                self.assertEqual(hard, [], f"Expected 0 hard errors, got: {hard}")
        finally:
            mod.KNOWN_FAILURES_PATH = original  # type: ignore[assignment]

    def test_unknown_failure_still_hard_error(self) -> None:
        """Failure NOT in known list → remains KO."""
        import scripts.check_first_batch_alignment as mod
        original = mod.KNOWN_FAILURES_PATH
        try:
            with tempfile.TemporaryDirectory() as raw:
                root = Path(raw)
                kf = root / "known.yml"
                # Known list is EMPTY
                kf.write_text("known_failures: []\n", encoding="utf-8")
                mod.KNOWN_FAILURES_PATH = kf  # type: ignore[assignment]
                directory = root / "P00"
                directory.mkdir()
                (directory / "P00_cours_test.md").write_text(
                    "---\ntitle: t\nofficial_program:\n  capacities:\n    - P-FAKE-99\n---\nObjectif O1\nP-LANG-01\nErreur fréquente EF1\n",
                    encoding="utf-8",
                )
                for kind, content in [
                    ("trace", "Objectif O1\nP-LANG-01\n"),
                    ("td", "### Exercice 1\nP-LANG-01\n"),
                    ("tp", "Objectif O1\nP-LANG-01\n"),
                    ("corrige", "### Corrigé exercice 1\n"),
                    ("evaluation", "### Question 1\nP-LANG-01\n"),
                    ("bareme", "### Barème question 1\n"),
                    ("remediation", "Activité corrective EF1\n"),
                ]:
                    (directory / f"P00_{kind}_test.md").write_text(content, encoding="utf-8")

                result = mod.analyze_alignment(root, prefixes=["P00"], program_ids={"P-LANG-01", "P-FAKE-99"})
                known = mod._load_known_failures()
                hard = [e for e in result.errors if not any(
                    e.startswith(f"{p}:") and cid in e for p, cid in known)]
                self.assertTrue(len(hard) >= 1, f"Expected hard errors for P-FAKE-99, got none")
        finally:
            mod.KNOWN_FAILURES_PATH = original  # type: ignore[assignment]


if __name__ == "__main__":
    unittest.main()
