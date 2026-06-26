"""Corrigé professeur TP T02 - Classes, objets et invariants."""

from __future__ import annotations


def creer_compte(solde):
    """Implémentation de référence pour classe, attribut, méthode, invariant."""
    if solde is None:
        raise ValueError("entrée absente")
    return {
        "entree": solde,
        "methode": "définir constructeur, attributs, méthodes et invariant vérifié après mutation",
        "controle": "solde 13 si l’invariant reste vérifié",
        "cas_limite": "montant négatif ou accès direct à l’attribut",
    }
