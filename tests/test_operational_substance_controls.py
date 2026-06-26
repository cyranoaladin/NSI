from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_drive_integration_plan as drive_plan
import check_linked_evaluation_substance as evaluation_substance
import check_linked_td_substance as td_substance
import check_no_operational_scope_hardcoding as scope_hardcoding
import check_operational_readiness_quality_coupling as readiness_coupling
import check_register_no_hidden_operational_debt as hidden_debt


def operational_sheet(root: Path, sequence: str, td: str = "", evaluation: str = "") -> Path:
    level = "premiere" if sequence.startswith("P") else "terminale"
    sheet = root / "03_progressions" / "fiches_cours" / level / sequence / f"{sequence}_fiche_cours_demo.md"
    sheet.parent.mkdir(parents=True)
    links = [
        f"| Séance | {sequence}-S1 | prête | séance réelle |",
    ]
    if td:
        links.append(f"| TD | {td} | existant | support réel |")
    if evaluation:
        links.append(f"| Évaluation | {evaluation} | existant | support réel |")
    sheet.write_text(
        f"""---
title: {sequence}
sequence_id: {sequence}
readiness: operational
---
# {sequence}

## Lien avec la progression
| Élément | Fichier | Statut | Remarque |
|---|---|---|---|
{chr(10).join(links)}
""",
        encoding="utf-8",
    )
    progression = root / "03_progressions" / ("seances_premiere.md" if sequence.startswith("P") else "seances_terminale.md")
    progression.parent.mkdir(parents=True, exist_ok=True)
    progression.write_text(f"### Séance {sequence}-S1\n", encoding="utf-8")
    return sheet


class OperationalSubstanceControlsTest(unittest.TestCase):
    def test_td_substance_rejects_generic_correction_without_real_result(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            td = root / "P10_TD_reseaux_protocoles_paquets.md"
            td.write_text(
                """---
title: P10 TD
level: premiere
sequence_id: P10
document_type: td
status: needs_review
official_program:
  capacities:
    - P-ARCH-02A
---
# TD réseaux

## Exercices
### Exercice 1
- Données : paquet de test.
- Consigne : analyser la situation.
- Production attendue : conclusion.

## Corrigé
### Corrigé exercice 1
Résultat indicatif : l'élève doit obtenir une conclusion explicite.
Démarche : partir de la donnée fournie, isoler les grandeurs utiles.
""",
                encoding="utf-8",
            )

            result = td_substance.analyze_linked_td_substance(root, [td])

            self.assertTrue(any("corrigé générique" in error.lower() for error in result.errors))

    def test_evaluation_substance_rejects_vague_answer_and_repeated_bareme(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            evaluation = root / "T10_evaluation_sql_select_where_join.md"
            evaluation.write_text(
                """---
title: T10 évaluation
level: terminale
sequence_id: T10
document_type: evaluation
status: needs_review
official_program:
  capacities:
    - T-BDD-03A
---
# Évaluation SQL

## Questions
### Question 1
Écrire une requête SQL adaptée.
### Question 2
Écrire une autre requête SQL adaptée.
### Question 3
Expliquer l'erreur.
### Question 4
Corriger la requête.

## Barème
- Question 1 : 1 point méthode, 1 point résultat.
- Question 2 : 1 point méthode, 1 point résultat.
- Question 3 : 1 point méthode, 1 point résultat.
- Question 4 : 1 point méthode, 1 point résultat.

## Corrigé professeur
### Question 1
Solution explicite attendue.
### Question 2
Solution explicite attendue.
""",
                encoding="utf-8",
            )

            result = evaluation_substance.analyze_linked_evaluation_substance(root, [evaluation])

            self.assertTrue(any("réponse attendue vague" in error.lower() for error in result.errors))
            self.assertTrue(any("barème trop répétitif" in error.lower() for error in result.errors))

    def test_scope_hardcoding_rejects_fixed_target_prefix_set(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            script = root / "check_demo.py"
            script.write_text("TARGET_PREFIXES = {'P10', 'P11', 'T10'}\n", encoding="utf-8")

            result = scope_hardcoding.analyze_no_operational_scope_hardcoding(root, [script])

            self.assertTrue(any("TARGET_PREFIXES" in error for error in result.errors))

    def test_readiness_quality_coupling_rejects_operational_sheet_with_formal_td(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            td = root / "P10_TD_reseaux_protocoles_paquets.md"
            td.write_text(
                """---
title: P10 TD
level: premiere
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
Lire un paquet.
## Corrigé
### Corrigé exercice 1
Réponse explicite attendue.
""",
                encoding="utf-8",
            )
            operational_sheet(root, "P10", td=td.name)

            result = readiness_coupling.analyze_operational_readiness_quality_coupling(root)

            self.assertTrue(any("P10_TD_reseaux_protocoles_paquets.md" in error for error in result.errors))

    def test_register_hidden_debt_rejects_operational_sheet_in_general_debt(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            operational_sheet(root, "P10", td="P10_TD_reseaux_protocoles_paquets.md")
            (root / "missing_documents_register_v2.md").write_text(
                """# Registre

## Dettes pédagogiques générales non liées à une fiche opérationnelle
| Fichier | Niveau | Séquence | Séance(s) | Type | Priorité | Statut | Responsable | Date cible | Source possible | Lien Drive éventuel | Dépendance | Décision | Blocage si absent | Fiche(s) concernée(s) | Impact pédagogique |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P10_TD_reseaux_protocoles_paquets.md | premiere | P10 | P10-S1 | TD | haute | absent | equipe NSI | 2027-06-30 | Documents_DRIVE | NA | fiche P10 | créer | oui | P10_fiche_cours_demo.md | TD absent |
""",
                encoding="utf-8",
            )

            result = hidden_debt.analyze_register_no_hidden_operational_debt(root)

            self.assertTrue(any("fiche opérationnelle" in error.lower() for error in result.errors))

    def test_drive_plan_requires_inventory_and_quarantine_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            result = drive_plan.analyze_drive_integration_plan(root)

            self.assertTrue(any("drive_inventory.csv absent" in error for error in result.errors))
            self.assertTrue(any("drive_quarantine_manifest.csv absent" in error for error in result.errors))


if __name__ == "__main__":
    unittest.main()
