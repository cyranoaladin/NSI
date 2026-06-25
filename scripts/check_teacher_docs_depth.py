#!/usr/bin/env python3
"""Check that teacher-side complementary documents are substantive."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEQUENCES = [
    ROOT / "premiere/sequences/s01_representation_donnees",
    ROOT / "terminale/sequences/s01_structures_donnees_interfaces_implementations",
]
FILES = ["corrige_professeur.md", "evaluation_corrigee.md", "grille_competences.md", "version_amenagee.md", "bareme.md", "sources.md"]
REQUIRED_TERMS = {
    "corrige_professeur.md": ["Réponse attendue", "Justification", "Barème", "Variante acceptable", "Erreurs fréquentes", "Remédiation", "Critère de réussite", "Capacité officielle"],
    "evaluation_corrigee.md": ["Durée", "Matériel", "Compétences", "Correction", "Barème", "Version aménagée", "Grille"],
    "grille_competences.md": ["Compétence", "Critères observables", "Niveau fragile", "Niveau attendu", "Niveau avancé", "Erreurs typiques", "Remédiation", "Lien évaluation"],
    "version_amenagee.md": ["Durée aménagée", "Consigne réécrite", "Aide intégrée", "Barème adapté", "Objectifs conservés"],
    "bareme.md": ["Total", "Barème détaillé", "Capacité visée", "Ajustements"],
    "sources.md": ["Sources institutionnelles", "Sources techniques", "Traçabilité", "Ressources Drive", "non publiable"],
}


def useful_line_count(text: str) -> int:
    return len([line for line in text.splitlines() if line.strip() and not line.strip().startswith("---")])


def main() -> int:
    errors: list[str] = []
    for seq in SEQUENCES:
        for name in FILES:
            path = seq / name
            if not path.exists():
                errors.append(f"missing {path.relative_to(ROOT)}")
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            if "status: needs_review" not in text and "status: \"needs_review\"" not in text:
                errors.append(f"{path.relative_to(ROOT)}: status needs_review missing")
            if useful_line_count(text) < 35:
                errors.append(f"{path.relative_to(ROOT)}: document too short")
            for term in REQUIRED_TERMS[name]:
                if term not in text:
                    errors.append(f"{path.relative_to(ROOT)}: missing term {term}")
    if errors:
        print("check_teacher_docs_depth: KO")
        for error in errors:
            print(f"- {error}")
        return 1
    print("check_teacher_docs_depth: PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())
