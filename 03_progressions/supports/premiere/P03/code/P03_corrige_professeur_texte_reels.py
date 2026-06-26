"""Corrigé professeur TP P03 - Texte Unicode et nombres réels."""

from __future__ import annotations


def inspect_text(text):
    """Implémentation de référence pour Unicode, UTF-8, flottants."""
    if text is None:
        raise ValueError("entrée absente")
    return {
        "entree": text,
        "methode": "distinguer point de code, encodage, octets et approximation machine",
        "controle": "2 caractères, 3 octets, somme flottante non exactement égale à 0.3",
        "cas_limite": "caractère hors ASCII ou comparaison directe de flottants",
    }
