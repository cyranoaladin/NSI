from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_corrected_answers_are_concrete as concrete_answers
import check_no_generic_scaffold_overuse as scaffold
import check_sequence_pack_consistency as pack_consistency


def write_support(path: Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"""---
title: "{path.stem}"
level: "premiere"
sequence_id: "P05"
document_type: "td"
status: "needs_review"
---
{body}
""",
        encoding="utf-8",
    )


class SequencePackAndScaffoldControlsTest(unittest.TestCase):
    def test_sequence_pack_rejects_contradictory_csv_scenarios(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            base = root / "03_progressions" / "supports" / "premiere" / "P05"
            write_support(
                base / "P05_td_tables_csv.md",
                "# TD\nLe fichier `pays_monde.csv` contient `PAYS,CAPITALE,CONTINENT,POPULATION`.\n",
            )
            write_support(
                base / "P05_trace_tables_csv.md",
                "# Trace\nOn part de `ville,temp` puis `Tunis,24` pour calculer une moyenne.\n",
            )

            result = pack_consistency.analyze_sequence_pack_consistency(root, prefixes=["P05"])

            self.assertTrue(any("ville,temp" in error and "pays_monde" in error for error in result.errors))

    def test_sequence_pack_accepts_pays_monde_thread_across_pack(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            base = root / "03_progressions" / "supports" / "premiere" / "P05"
            for kind in ["cours", "trace", "td", "tp", "corrige", "bareme", "evaluation", "remediation", "version_amenagee"]:
                write_support(
                    base / f"P05_{kind}_tables_csv.md",
                    "# Support\n"
                    "Fil conducteur : `pays_monde.csv` avec champs `PAYS`, `CAPITALE`, `CONTINENT`, `POPULATION`.\n"
                    "On utilise `csv.reader`, `csv.DictReader`, un filtrage par `CONTINENT`, "
                    "la conversion de `POPULATION` en `int`, un tri numérique et une ligne invalide.\n",
                )

            result = pack_consistency.analyze_sequence_pack_consistency(root, prefixes=["P05"])

            self.assertEqual([], result.errors)

    def test_generic_scaffold_rejects_massive_phrase_without_concrete_result(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            base = root / "03_progressions" / "supports" / "terminale" / "T17"
            for index in range(6):
                write_support(
                    base / f"T17_TD_demo_{index}.md",
                    "# TD\n"
                    "### Exercice 1\n"
                    "- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.\n"
                    "- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.\n",
                )

            result = scaffold.analyze_no_generic_scaffold_overuse(root)

            self.assertTrue(any("apparaît 6 fois" in error for error in result.errors))

    def test_generic_scaffold_allows_phrase_with_local_disciplinary_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            base = root / "03_progressions" / "supports" / "terminale" / "T17"
            for index in range(6):
                write_support(
                    base / f"T17_TD_demo_{index}.md",
                    "# TD\n"
                    "### Exercice 1\n"
                    "- Données : valeurs [2, 5, 9], capacité 7.\n"
                    "- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.\n"
                    "- Résultat concret : état `dp[7] = 12`, trace `[0, 2, 5, 7, 10, 12]`, complexité `O(n*C)`.\n",
                )

            result = scaffold.analyze_no_generic_scaffold_overuse(root)

            self.assertEqual([], result.errors)

    def test_corrected_answers_rejects_correction_without_concrete_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            support = root / "03_progressions" / "supports" / "premiere" / "P10" / "P10_corrige_demo.md"
            write_support(
                support,
                "# Corrigé\n"
                "### Corrigé exercice 1\n"
                "La réponse est correcte si la démarche est claire et complète.\n",
            )

            result = concrete_answers.analyze_corrected_answers(root, files=[support])

            self.assertTrue(any("sans résultat disciplinaire concret" in error for error in result.errors))

    def test_corrected_answers_accepts_trace_and_result(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            support = root / "03_progressions" / "supports" / "terminale" / "T18" / "T18_corrige_demo.md"
            write_support(
                support,
                "# Corrigé\n"
                "### Corrigé exercice 1\n"
                "Motif `ABA`, texte `CABAABABA`. Table mauvais caractère : A -> 2, B -> 1. "
                "Trace : alignement 0, mismatch B, décalage 1 ; alignement 1, occurrence trouvée. "
                "Résultat attendu : indice 1.\n",
            )

            result = concrete_answers.analyze_corrected_answers(root, files=[support])

            self.assertEqual([], result.errors)


if __name__ == "__main__":
    unittest.main()
