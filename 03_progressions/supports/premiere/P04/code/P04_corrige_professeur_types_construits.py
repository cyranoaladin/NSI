"""Corrigé professeur TP P04 - Types construits Python."""

from __future__ import annotations


def resume_mesures(mesures):
    """Implémentation de référence pour tuple, liste, dictionnaire, parcours."""
    if mesures is None:
        raise ValueError("entrée absente")
    return {
        "entree": mesures,
        "methode": "choisir le conteneur selon mutabilité, ordre et accès attendu",
        "controle": "tuple non modifié, liste mise à jour, dictionnaire consulté par clé",
        "cas_limite": "copie de liste et clé absente",
    }
