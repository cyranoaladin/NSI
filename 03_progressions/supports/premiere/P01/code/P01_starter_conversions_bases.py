"""Starter TP P01 - Conversions entre bases."""

from __future__ import annotations


def convert_base(value):
    """Retourne une synthèse contrôlable pour le TP P01."""
    if value is None:
        raise ValueError("entrée absente")
    return {"entree": value, "controle": "101101 en base deux et 2D en base seize", "cas_limite": "0, 1 et changement de base avec un chiffre interdit"}


if __name__ == "__main__":
    print(convert_base(45))
