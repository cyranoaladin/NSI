from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_course_sheets_alignment as alignment
import check_course_sheets_coverage as coverage
import check_course_sheets_quality as quality


VALID_SHEET = """---
title: "P01 - Fiche cours conversions"
level: "premiere"
sequence_id: "P01"
document_type: "fiche_cours"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Représentation des entiers"
notion: "conversions"
official_program:
  capacities:
    - "P-DATA-BASE-01"
private_data: false
---

# P01 - Fiche cours conversions

## À savoir
Une base donne la valeur d'un chiffre par sa position.

## Méthodes
1. Diviser par la base.
2. Lire les restes dans le bon ordre.

## Exemples corrigés
### Exemple corrigé 1
13 vaut 1101 en base deux.
### Exemple corrigé 2
101101₂ vaut 45 en base dix.

## Erreurs fréquentes
- Lire les restes dans l'ordre de calcul ; correction : inverser la lecture.
- Oublier les poids ; correction : annoter chaque puissance.
- Accepter un chiffre interdit ; correction : vérifier l'alphabet.

## Cas limites
0 se code 0 et un chiffre 2 est interdit en base deux.

## Mini-exercices
### Exercice 1
Convertir 7 en binaire.
### Exercice 2
Convertir 1010₂ en décimal.
### Exercice 3
Dire pourquoi 102₂ est invalide.

## Réponses rapides
1. 111₂.
2. 10.
3. Le symbole 2 est interdit.

## À retenir
- Une base fixe les symboles autorisés.
- La position donne le poids.
- Les conversions se contrôlent.
- Le cas 0 est particulier.
- Une réponse doit citer la méthode.

## Lien avec la progression
- Séances : P01-S1.
- TD lié : P01_TD_conversions_exercices_1_3.md.

## Auto-évaluation
- Je sais convertir un entier positif.
- Je sais vérifier une écriture binaire.
- Je sais expliquer ma méthode.
"""


class CourseSheetsTest(unittest.TestCase):
    def test_missing_sequence_sheet_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "03_progressions").mkdir()
            (root / "03_progressions" / "progression_premiere.md").write_text(
                "| P00 | Septembre | 4 h | 1 h | P-HIST-01 | Diagnostic |\n"
                "| P01 | Septembre | 8 h | 1 h | P-DATA-BASE-01 | Quiz |\n",
                encoding="utf-8",
            )
            (root / "03_progressions" / "progression_terminale.md").write_text("", encoding="utf-8")

            result = coverage.analyze_course_sheet_coverage(root, program_ids={"P-HIST-01", "P-DATA-BASE-01"})

            self.assertTrue(any("P01: aucune fiche" in error for error in result.errors))

    def test_low_quality_sheet_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            sheet = root / "03_progressions" / "fiches_cours" / "premiere" / "P01" / "P01_fiche_cours_bases.md"
            sheet.parent.mkdir(parents=True)
            sheet.write_text("---\ndocument_type: fiche_cours\nstatus: needs_review\n---\n# Fiche\n", encoding="utf-8")

            result = quality.analyze_course_sheets_quality(root, program_ids={"P-DATA-BASE-01"})

            self.assertTrue(any("frontmatter incomplet" in error for error in result.errors))
            self.assertTrue(any("section manquante" in error for error in result.errors))

    def test_unknown_capacity_is_rejected_by_alignment(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            sheet = root / "03_progressions" / "fiches_cours" / "premiere" / "P01" / "P01_fiche_cours_bases.md"
            sheet.parent.mkdir(parents=True)
            sheet.write_text(VALID_SHEET.replace("P-DATA-BASE-01", "P-UNKNOWN-99"), encoding="utf-8")

            result = alignment.analyze_course_sheets_alignment(root, program_ids={"P-DATA-BASE-01"})

            self.assertTrue(any("capacité absente du YAML" in error for error in result.errors))

    def test_cross_sheet_repetition_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            repeated = "- Ce paragraphe long répété dans trop de fiches signale un gabarit artificiel sans ajout disciplinaire."
            files: list[Path] = []
            for index in range(6):
                sheet = root / f"P{index:02d}_fiche_cours_test.md"
                sheet.write_text(f"---\nstatus: needs_review\n---\n# Fiche\n{repeated}\n", encoding="utf-8")
                files.append(sheet)

            errors = quality.cross_sheet_repetition_errors(files)

            self.assertTrue(any("répétition transversale excessive" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
