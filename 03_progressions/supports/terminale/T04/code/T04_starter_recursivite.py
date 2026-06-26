"""Starter TP T04 - Récursivité contrôlée."""

from __future__ import annotations


def factorielle(n):
    """Retourne une synthèse contrôlable pour le TP T04."""
    if n is None:
        raise ValueError("entrée absente")
    return {"entree": n, "controle": "120 avec cas de base factorielle(0)=1", "cas_limite": "appel récursif sans diminution ou profondeur excessive"}


if __name__ == "__main__":
    print(factorielle(5))
