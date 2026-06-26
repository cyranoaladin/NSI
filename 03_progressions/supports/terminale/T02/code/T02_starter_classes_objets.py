"""Starter TP T02 - Classes, objets et invariants."""

from __future__ import annotations


def creer_compte(solde):
    """Retourne une synthèse contrôlable pour le TP T02."""
    if solde is None:
        raise ValueError("entrée absente")
    return {"entree": solde, "controle": "solde 13 si l’invariant reste vérifié", "cas_limite": "montant négatif ou accès direct à l’attribut"}


if __name__ == "__main__":
    print(creer_compte(20))
