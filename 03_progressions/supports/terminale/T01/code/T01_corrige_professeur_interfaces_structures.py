"""Asset Python TP. Statut pédagogique: needs_review."""

from __future__ import annotations

def scenario_structure(operations):
    if operations is None:
        raise ValueError("operations absentes")
    pile = []
    sorties = []
    for op, value in operations:
        if op == "ajouter":
            pile.append(value)
        elif op == "retirer":
            if not pile:
                raise ValueError("structure vide")
            sorties.append(pile.pop())
        else:
            raise ValueError("operation inconnue")
    return sorties
