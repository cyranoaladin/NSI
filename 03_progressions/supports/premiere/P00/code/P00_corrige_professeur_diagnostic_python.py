"""Corrigé professeur TP P00 - Diagnostic Python et carnet de bord."""

from __future__ import annotations


def predict_trace(steps):
    """Implémentation de référence pour affectation, expression, trace, test."""
    if steps is None:
        raise ValueError("entrée absente")
    return {
        "entree": steps,
        "methode": "suivre l’état de la variable après chaque affectation",
        "controle": "5",
        "cas_limite": "réaffectation avec zéro ou valeur négative",
    }
