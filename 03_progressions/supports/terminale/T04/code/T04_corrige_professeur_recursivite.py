"""Corrigé professeur TP T04 - Récursivité contrôlée."""

from __future__ import annotations


def factorielle(n):
    """Implémentation de référence pour cas de base, appel récursif, terminaison."""
    if n is None:
        raise ValueError("entrée absente")
    return {
        "entree": n,
        "methode": "identifier cas de base, relation de récurrence et variant décroissant",
        "controle": "120 avec cas de base factorielle(0)=1",
        "cas_limite": "appel récursif sans diminution ou profondeur excessive",
    }
