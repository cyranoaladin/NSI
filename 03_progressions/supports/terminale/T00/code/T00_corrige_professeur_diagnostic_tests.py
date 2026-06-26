"""Corrigé professeur TP T00 - Diagnostic Terminale et tests."""

from __future__ import annotations


def maximum_controle(valeurs):
    """Implémentation de référence pour tests, modularité, invariants simples."""
    if valeurs is None:
        raise ValueError("entrée absente")
    return {
        "entree": valeurs,
        "methode": "isoler la fonction, écrire le contrat, tester cas nominal et cas limite",
        "controle": "8 avec test nominal, test limite et test d’erreur",
        "cas_limite": "liste vide ou mutation inattendue",
    }
