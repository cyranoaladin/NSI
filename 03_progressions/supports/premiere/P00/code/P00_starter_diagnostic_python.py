"""Starter TP P00 - Diagnostic Python et carnet de bord."""

from __future__ import annotations


def predict_trace(steps):
    """Retourne une synthèse contrôlable pour le TP P00."""
    if steps is None:
        raise ValueError("entrée absente")
    return {"entree": steps, "controle": "5", "cas_limite": "réaffectation avec zéro ou valeur négative"}


if __name__ == "__main__":
    print(predict_trace([("x", 3), ("x", 5)]))
