from __future__ import annotations

import csv
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_audit_extracted_runtime_budget as runtime_budget
import check_capacity_status_ladder as capacity_ladder
import check_course_explanatory_quality as course_quality
import check_human_review_register as human_review
import check_tp_executable_opportunity as tp_opportunity


def write(path: Path, content: str = "x") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


class FinalQualityHardeningTest(unittest.TestCase):
    def test_capacity_ladder_rejects_documented_without_practice_or_assessment(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            write(
                root / "00_programmes_officiels/programme_nsi_2019.yaml",
                "programmes:\n"
                "  premiere:\n"
                "    - id: P-TEST-01\n"
                "      theme: Test\n"
                "      capacite: tester une capacité\n",
            )
            write(root / "03_progressions/fiches_cours/premiere/P00/P00_fiche_cours_test.md", "P-TEST-01\n")

            result = capacity_ladder.analyze_capacity_status_ladder(root)

            self.assertEqual(result.rows["P-TEST-01"]["documented"], "oui")
            self.assertEqual(result.rows["P-TEST-01"]["practiced"], "non")
            self.assertEqual(result.rows["P-TEST-01"]["assessed"], "non")
            self.assertTrue(any("practiced=non" in error for error in result.errors))
            self.assertTrue(any("assessed=non" in error for error in result.errors))

    def test_capacity_ladder_reports_session_link_without_covering(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            write(
                root / "00_programmes_officiels/programme_nsi_2019.yaml",
                "programmes:\n"
                "  premiere:\n"
                "    - id: P-TEST-01\n"
                "      theme: Test\n"
                "      capacite: tester une capacité\n",
            )
            write(root / "03_progressions/fiches_cours/premiere/P00/P00_fiche_cours_test.md", "P-TEST-01\n")
            write(root / "03_progressions/supports/premiere/P00/P00_TD_test.md", "P-TEST-01\n")
            write(root / "03_progressions/supports/premiere/P00/P00_evaluation_test.md", "P-TEST-01\n")
            write(
                root / "03_progressions/seances_premiere.md",
                "### Séance P00-S1\n"
                "- Capacité officielle : P-TEST-01\n"
                "- Document utilisé : P00_TD_test.md, P00_evaluation_test.md\n",
            )

            result = capacity_ladder.analyze_capacity_status_ladder(root)

            self.assertEqual(result.rows["P-TEST-01"]["linked_to_session"], "oui")
            self.assertEqual(result.rows["P-TEST-01"]["covered"], "non")
            self.assertFalse(result.errors)

    def test_course_quality_rejects_course_with_only_two_examples(self) -> None:
        text = (
            "---\ndocument_type: cours\nstatus: needs_review\n---\n"
            "# Cours\n"
            "## Situation-problème\n"
            "Une explication conceptuelle substantielle relie la notion à P-TEST-01 avec vocabulaire disciplinaire.\n"
            "## À savoir\nDéfinition précise et rôle.\n"
            "## Méthodes\nSavoir-faire et méthode distingués.\n"
            "### Exemple corrigé 1\nDonnée 1, méthode, résultat 1.\n"
            "### Exemple corrigé 2\nDonnée 2, méthode, résultat 2.\n"
            "## Erreurs fréquentes\n- On confond A et B.\n- On oublie le cas vide.\n"
            "## Cas limites\n- cas vide.\n- cas invalide.\n"
            "## À retenir\nSynthèse finale.\n"
        )

        errors = course_quality.course_quality_errors(text, "cours_test.md")

        self.assertTrue(any("trois exemples" in error for error in errors))

    def test_tp_opportunity_flags_executable_paper_tp_without_assets(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            tp = root / "03_progressions/supports/terminale/T10/T10_tp_sql_select_where_join.md"
            write(
                tp,
                "---\ndocument_type: tp_papier\nstatus: needs_review\n---\n"
                "# TP SQL papier\n"
                "Ce TP papier porte sur SQL, SELECT, JOIN et tables.\n"
                "Aucune ressource Python ou SQLite n'est fournie.\n",
            )

            result = tp_opportunity.analyze_tp_executable_opportunity(root)

            self.assertTrue(result.opportunities)
            self.assertIn("T10", result.opportunities[0])

    def test_human_review_register_requires_one_pending_row_per_major_resource(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            write(
                root / "manifest.csv",
                "path,statut,source\n"
                "03_progressions/supports/premiere/P00/P00_cours_test.md,needs_review,generated\n",
            )
            write(root / "03_progressions/supports/premiere/P00/P00_cours_test.md", "---\nstatus: needs_review\n---\n")

            result = human_review.analyze_human_review_register(root)

            self.assertTrue(any("human_review_register.csv absent" in error for error in result.errors))

    def test_human_review_register_rejects_validation_without_reviewer_date(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            resource = "03_progressions/supports/premiere/P00/P00_cours_test.md"
            write(root / resource, "---\nstatus: needs_review\n---\n")
            write(root / "manifest.csv", f"path,statut,source\n{resource},needs_review,generated\n")
            register = root / "human_review_register.csv"
            register.write_text(
                "ressource,niveau,sequence,notion,reviewer,date,science_status,pedagogy_status,"
                "accessibility_status,technical_status,decision,blockers\n"
                f"{resource},premiere,P00,test,,,validated,validated,pending,pending,needs_review,\n",
                encoding="utf-8",
            )

            result = human_review.analyze_human_review_register(root)

            self.assertTrue(any("sans reviewer/date" in error for error in result.errors))

    def test_runtime_budget_requires_source_archive_extraction(self) -> None:
        self.assertTrue(runtime_budget.uses_source_archive_extraction(runtime_budget.analyze_audit_extracted_runtime_budget))


if __name__ == "__main__":
    unittest.main()
