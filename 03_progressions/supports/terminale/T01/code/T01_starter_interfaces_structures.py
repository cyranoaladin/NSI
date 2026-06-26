"""Starter TP T01 - Interfaces de structures abstraites."""

from __future__ import annotations


def scenario_structure(operations):
    """Retourne une synthèse contrôlable pour le TP T01."""
    if operations is None:
        raise ValueError("entrée absente")
    return {"entree": operations, "controle": "interface séparée de la représentation interne", "cas_limite": "confondre interface et liste Python concrète"}


if __name__ == "__main__":
    print(scenario_structure([("ajouter", 4), ("retirer", None)]))
