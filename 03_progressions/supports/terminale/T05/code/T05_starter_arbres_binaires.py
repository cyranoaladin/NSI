"""Starter TP T05 - Arbres binaires et parcours."""

from __future__ import annotations


def parcours_infixe(arbre):
    """Retourne une synthèse contrôlable pour le TP T05."""
    if arbre is None:
        raise ValueError("entrée absente")
    return {"entree": arbre, "controle": "parcours infixe 2, 4, 7", "cas_limite": "arbre vide ou arbre très déséquilibré"}


if __name__ == "__main__":
    print(parcours_infixe((4, (2, None, None), (7, None, None))))
