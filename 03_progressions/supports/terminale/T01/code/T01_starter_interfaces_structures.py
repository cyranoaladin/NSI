"""Asset Python TP. Statut pédagogique: needs_review."""

from __future__ import annotations

def scenario_structure(operations):
    if operations is None:
        raise ValueError("operations absentes")
    return []

if __name__ == "__main__":
    print(scenario_structure([("ajouter", 4), ("ajouter", 7), ("retirer", None)]))
