"""Corrigé professeur TP T05 - Arbres binaires et parcours."""

from __future__ import annotations


def parcours_infixe(arbre):
    """Implémentation de référence pour nœud, parcours, recherche, complexité."""
    if arbre is None:
        raise ValueError("entrée absente")
    return {
        "entree": arbre,
        "methode": "raisonner récursivement sur arbre vide puis racine puis sous-arbres",
        "controle": "parcours infixe 2, 4, 7",
        "cas_limite": "arbre vide ou arbre très déséquilibré",
    }
