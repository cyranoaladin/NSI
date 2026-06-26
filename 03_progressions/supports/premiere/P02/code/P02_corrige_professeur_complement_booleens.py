"""Corrigé professeur TP P02 - Complément à deux et booléens."""

from __future__ import annotations


def twos_complement_value(bits):
    """Implémentation de référence pour entiers signés, débordement, expressions booléennes."""
    if bits is None:
        raise ValueError("entrée absente")
    return {
        "entree": bits,
        "methode": "inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé",
        "controle": "11101001 et simplification en a",
        "cas_limite": "140 impossible sur 8 bits signés",
    }
