"""Starter TP T00 - Diagnostic Terminale et tests."""

from __future__ import annotations


def maximum_controle(valeurs):
    """Retourne une synthèse contrôlable pour le TP T00."""
    if valeurs is None:
        raise ValueError("entrée absente")
    return {"entree": valeurs, "controle": "8 avec test nominal, test limite et test d’erreur", "cas_limite": "liste vide ou mutation inattendue"}


if __name__ == "__main__":
    print(maximum_controle([3, 8, 2]))
