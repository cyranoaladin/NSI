"""Starter TP T03 - Piles, files et dictionnaires."""

from __future__ import annotations


def jouer_operations(operations):
    """Retourne une synthèse contrôlable pour le TP T03."""
    if operations is None:
        raise ValueError("entrée absente")
    return {"entree": operations, "controle": "B sort avant A pour une pile ; A sort avant B pour une file", "cas_limite": "dépiler ou défiler une structure vide"}


if __name__ == "__main__":
    print(jouer_operations([("push", "A"), ("push", "B"), ("pop", None)]))
