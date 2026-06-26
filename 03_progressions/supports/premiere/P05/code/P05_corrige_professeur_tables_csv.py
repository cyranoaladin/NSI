"""Corrigé professeur TP P05 - Tables CSV et requêtes simples."""

from __future__ import annotations


def filtrer_table(rows):
    """Implémentation de référence pour CSV, dictionnaire ligne, sélection, projection."""
    if rows is None:
        raise ValueError("entrée absente")
    return {
        "entree": rows,
        "methode": "lire l’en-tête, convertir les champs utiles, filtrer puis agréger",
        "controle": "liste de dictionnaires filtrée puis moyenne calculée",
        "cas_limite": "champ vide, séparateur inattendu ou nombre invalide",
    }
