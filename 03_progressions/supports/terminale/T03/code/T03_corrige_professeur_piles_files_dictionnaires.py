"""Corrigé professeur TP T03 - Piles, files et dictionnaires."""

from __future__ import annotations


def jouer_operations(operations):
    """Implémentation de référence pour LIFO, FIFO, dictionnaire d’index."""
    if operations is None:
        raise ValueError("entrée absente")
    return {
        "entree": operations,
        "methode": "choisir LIFO ou FIFO selon l’ordre de sortie attendu",
        "controle": "B sort avant A pour une pile ; A sort avant B pour une file",
        "cas_limite": "dépiler ou défiler une structure vide",
    }
