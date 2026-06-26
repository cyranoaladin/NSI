from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_linked_evaluation_quality as evaluation_quality
import check_linked_td_quality as td_quality
import check_operational_supports_no_indicative_debt as operational_debt


class LinkedSupportQualityTest(unittest.TestCase):
    def test_td_requires_eight_exercises_and_required_exercise_types(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            td = root / "P10_TD_reseaux_protocoles_paquets.md"
            td.write_text(
                """---
title: P10 TD
sequence_id: P10
document_type: td
status: needs_review
official_program:
  capacities:
    - P-ARCH-02A
---
# TD

## Exercices
### Exercice 1
Lecture d'un paquet.

## Corrigé
### Corrigé exercice 1
Réponse.
""",
                encoding="utf-8",
            )

            result = td_quality.analyze_linked_td_quality(root, [td])

            self.assertTrue(any("8 exercices" in error for error in result.errors))
            self.assertTrue(any("lecture/analyse" in error for error in result.errors))

    def test_td_check_rejects_missing_target_td_link(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            sheet = root / "03_progressions" / "fiches_cours" / "premiere" / "P10" / "P10_fiche_cours_reseaux_protocoles_paquets.md"
            sheet.parent.mkdir(parents=True)
            sheet.write_text(
                """---
title: P10
sequence_id: P10
readiness: operational
---
# P10

## Lien avec la progression
| Élément | Fichier | Statut | Remarque |
|---|---|---|---|
| Séance | P10-S1 | prête | séance réelle |
| TD | P10_TD_reseaux_protocoles_paquets.md | existant | support réel |
""",
                encoding="utf-8",
            )

            result = td_quality.analyze_linked_td_quality(root)

            self.assertTrue(any("support TD absent" in error for error in result.errors))

    def test_td_check_discovers_every_operational_sheet_not_only_recent_prefixes(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            sheet = root / "03_progressions" / "fiches_cours" / "premiere" / "P01" / "P01_fiche_cours_conversions.md"
            sheet.parent.mkdir(parents=True)
            sheet.write_text(
                """---
title: P01
sequence_id: P01
readiness: operational
---
# P01

## Lien avec la progression
| Élément | Fichier | Statut | Remarque |
|---|---|---|---|
| Séance | P01-S1 | prête | séance réelle |
| TD | P01_TD_conversions.md | existant | support réel |
""",
                encoding="utf-8",
            )

            result = td_quality.analyze_linked_td_quality(root)

            self.assertTrue(any("P01_TD_conversions.md: support TD absent" in error for error in result.errors))

    def test_evaluation_requires_bareme_and_accommodations(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            evaluation = root / "T10_evaluation_sql_select_where_join.md"
            evaluation.write_text(
                """---
title: T10 evaluation
sequence_id: T10
document_type: evaluation
status: needs_review
official_program:
  capacities:
    - T-BDD-03A
---
# Evaluation

## Questions
### Question 1
SELECT simple.
""",
                encoding="utf-8",
            )

            result = evaluation_quality.analyze_linked_evaluation_quality(root, [evaluation])

            self.assertTrue(any("barème question par question" in error.lower() for error in result.errors))
            self.assertTrue(any("aménagement" in error.lower() for error in result.errors))

    def test_evaluation_check_rejects_missing_target_evaluation_link(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            sheet = root / "03_progressions" / "fiches_cours" / "terminale" / "T10" / "T10_fiche_cours_sql_select_where_join.md"
            sheet.parent.mkdir(parents=True)
            sheet.write_text(
                """---
title: T10
sequence_id: T10
readiness: operational
---
# T10

## Lien avec la progression
| Élément | Fichier | Statut | Remarque |
|---|---|---|---|
| Séance | T10-S1 | prête | séance réelle |
| Évaluation | T10_evaluation_sql_select_where_join.md | existant | support réel |
""",
                encoding="utf-8",
            )

            result = evaluation_quality.analyze_linked_evaluation_quality(root)

            self.assertTrue(any("support évaluation absent" in error for error in result.errors))

    def test_evaluation_check_discovers_every_operational_sheet_not_only_recent_prefixes(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            sheet = root / "03_progressions" / "fiches_cours" / "premiere" / "P01" / "P01_fiche_cours_conversions.md"
            sheet.parent.mkdir(parents=True)
            sheet.write_text(
                """---
title: P01
sequence_id: P01
readiness: operational
---
# P01

## Lien avec la progression
| Élément | Fichier | Statut | Remarque |
|---|---|---|---|
| Séance | P01-S1 | prête | séance réelle |
| Évaluation | P01_evaluation_conversions.md | existant | support réel |
""",
                encoding="utf-8",
            )

            result = evaluation_quality.analyze_linked_evaluation_quality(root)

            self.assertTrue(any("P01_evaluation_conversions.md: support évaluation absent" in error for error in result.errors))

    def test_operational_support_debt_rejects_too_short_linked_resource(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "03_progressions" / "seances_premiere.md").parent.mkdir(parents=True)
            (root / "03_progressions" / "seances_premiere.md").write_text("### Séance P10-S1\n", encoding="utf-8")
            support = root / "03_progressions" / "supports" / "premiere" / "P10" / "P10_TD_reseaux_protocoles_paquets.md"
            support.parent.mkdir(parents=True)
            support.write_text(
                """---
title: P10 TD
sequence_id: P10
document_type: td
status: needs_review
---
# P10 TD
## Exercices
### Exercice 1
Un paquet.
## Corrigé
### Corrigé exercice 1
Réponse.
""",
                encoding="utf-8",
            )
            sheet = root / "03_progressions" / "fiches_cours" / "premiere" / "P10" / "P10_fiche_cours_reseaux_protocoles_paquets.md"
            sheet.parent.mkdir(parents=True)
            sheet.write_text(
                """---
title: P10
sequence_id: P10
readiness: operational
---
# P10

## Lien avec la progression
| Élément | Fichier | Statut | Remarque |
|---|---|---|---|
| Séance | P10-S1 | prête | séance réelle |
| TD | P10_TD_reseaux_protocoles_paquets.md | existant | support réel |
""",
                encoding="utf-8",
            )

            result = operational_debt.analyze_operational_supports_no_indicative_debt(root)

            self.assertTrue(any("profondeur insuffisante" in error for error in result.errors))

    def test_operational_support_debt_checks_all_operational_prefixes(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "03_progressions").mkdir()
            (root / "03_progressions" / "seances_premiere.md").write_text("### Séance P01-S1\n", encoding="utf-8")
            support = root / "03_progressions" / "supports" / "premiere" / "P01" / "P01_TD_conversions.md"
            support.parent.mkdir(parents=True)
            support.write_text(
                """---
title: P01 TD
sequence_id: P01
document_type: td
status: needs_review
---
# P01 TD
## Exercices
### Exercice 1
Convertir 5.
## Corrigé
### Corrigé exercice 1
5 vaut 101 en binaire.
""",
                encoding="utf-8",
            )
            sheet = root / "03_progressions" / "fiches_cours" / "premiere" / "P01" / "P01_fiche_cours_conversions.md"
            sheet.parent.mkdir(parents=True)
            sheet.write_text(
                """---
title: P01
sequence_id: P01
readiness: operational
---
# P01

## Lien avec la progression
| Élément | Fichier | Statut | Remarque |
|---|---|---|---|
| Séance | P01-S1 | prête | séance réelle |
| TD | P01_TD_conversions.md | existant | support réel |
""",
                encoding="utf-8",
            )

            result = operational_debt.analyze_operational_supports_no_indicative_debt(root)

            self.assertTrue(any("profondeur insuffisante" in error for error in result.errors))


if __name__ == "__main__":
    unittest.main()
