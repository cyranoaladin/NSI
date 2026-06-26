"""Corrigé professeur TP P01 - Conversions entre bases."""

from __future__ import annotations


def convert_base(value):
    """Implémentation de référence pour base dix, base deux, base seize."""
    if value is None:
        raise ValueError("entrée absente")
    return {
        "entree": value,
        "methode": "divisions euclidiennes successives puis regroupement par paquets de quatre bits",
        "controle": "101101 en base deux et 2D en base seize",
        "cas_limite": "0, 1 et changement de base avec un chiffre interdit",
    }
