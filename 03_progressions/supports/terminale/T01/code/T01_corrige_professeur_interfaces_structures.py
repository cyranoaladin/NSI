"""Corrigé professeur TP T01 - Interfaces de structures abstraites."""

from __future__ import annotations


def scenario_structure(operations):
    """Implémentation de référence pour interface, opération, coût."""
    if operations is None:
        raise ValueError("entrée absente")
    return {
        "entree": operations,
        "methode": "nommer les opérations, les préconditions et les effets sans dépendre du stockage",
        "controle": "interface séparée de la représentation interne",
        "cas_limite": "confondre interface et liste Python concrète",
    }
