from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_course_sheet_exercise_answer_count as answer_count
import check_csv_numeric_fields_are_parseable as csv_numeric
import check_no_duplicate_capacity_lines as duplicate_capacity
import check_p04_key_consistency as p04_keys
import check_p05_expected_outputs_are_explicit as p05_outputs
import check_p05_pipeline_consistency as p05_pipeline
import check_t18_trace_table_quality as t18_trace


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


class P05P04ControlsTest(unittest.TestCase):
    def test_csv_numeric_rejects_unescaped_population_with_commas(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            support = root / "03_progressions/supports/premiere/P05/P05_td_tables_csv.md"
            write(
                support,
                "PAYS,CAPITALE,CONTINENT,POPULATION\n"
                "Espagne,Madrid,Europe,46,754,778\n"
                '`int(row["POPULATION"])` donne `46,754,778`.\n',
            )

            result = csv_numeric.analyze_csv_numeric_fields_are_parseable(root)

            self.assertTrue(any("trop de colonnes" in error for error in result.errors))
            self.assertTrue(any("non convertible" in error for error in result.errors))

    def test_p05_pipeline_requires_conversion_before_filtering_and_exact_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            support = root / "03_progressions/supports/premiere/P05/P05_td_tables_csv.md"
            write(
                support,
                "Filtrer l'Europe puis convertir la population. "
                "Résultat : deux lignes européennes sélectionnées.\n",
            )

            result = p05_pipeline.analyze_p05_pipeline_consistency(root)

            self.assertTrue(any("ordre logique" in error for error in result.errors))
            self.assertTrue(any('["Allemagne", "Albanie"]' in error for error in result.errors))

    def test_p05_expected_outputs_rejects_vague_phrases(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            support = root / "03_progressions/supports/premiere/P05/P05_corrige_tables_csv.md"
            write(
                support,
                "Réponse attendue : deux lignes européennes sélectionnées, "
                "ligne invalide isolée avant conversion, méthode visible, résultat correct.\n",
            )

            result = p05_outputs.analyze_p05_expected_outputs_are_explicit(root)

            self.assertGreaterEqual(len(result.errors), 3)

    def test_course_sheet_answer_count_rejects_missing_answer(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            sheet = root / "03_progressions/fiches_cours/premiere/P05/P05_fiche_cours_tables_csv_import_coherence.md"
            write(
                sheet,
                "# Fiche\n"
                "## Mini-exercices\n"
                "1. Exercice A\n"
                "2. Exercice B\n"
                "## Réponses rapides\n"
                "1. Réponse A\n",
            )

            result = answer_count.analyze_course_sheet_exercise_answer_count(root, files=[sheet])

            self.assertTrue(any("2 mini-exercices" in error and "1 réponses" in error for error in result.errors))

    def test_duplicate_capacity_lines_rejects_p05_duplicate_and_missing_ptable02(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            evaluation = root / "03_progressions/supports/premiere/P05/P05_evaluation_tables_csv.md"
            write(
                evaluation,
                "## Capacités évaluées\n"
                "- P-TABLE-01\n"
                "- P-TABLE-01\n",
            )

            result = duplicate_capacity.analyze_no_duplicate_capacity_lines(root)

            self.assertTrue(any("P-TABLE-01" in error and "dupliquée" in error for error in result.errors))
            self.assertTrue(any("P-TABLE-02" in error for error in result.errors))

    def test_p04_key_consistency_rejects_temp_key_when_temperature_is_required(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            support = root / "03_progressions/supports/premiere/P04/P04_td_types_construits.md"
            write(support, 'stations = [{"nom": "A", "temp": 21}]\n')

            result = p04_keys.analyze_p04_key_consistency(root)

            self.assertTrue(any('"temp"' in error for error in result.errors))

    def test_t18_trace_requires_paper_tp_declaration_and_trace_quality(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            trace = root / "03_progressions/supports/terminale/T18/T18_trace_boyer_moore.md"
            write(trace, "# Trace\n| Alignement | Fenêtre |\n|---|---|\n")

            result = t18_trace.analyze_t18_trace_table_quality(root)

            self.assertTrue(any("TP papier" in error for error in result.errors))
            self.assertTrue(any("barème" in error.lower() for error in result.errors))


if __name__ == "__main__":
    unittest.main()
