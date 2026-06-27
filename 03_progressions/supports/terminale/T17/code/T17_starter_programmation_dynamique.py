"""Starter TP T17 programmation dynamique. Statut pédagogique: needs_review."""
from __future__ import annotations


def fibonacci_dp(n: int) -> list[int]:
    if n < 0:
        raise ValueError("n invalide")
    valeurs: list[int] = []
    indice = 0
    while indice <= n:
        valeurs.append(indice)
        indice += 1
    return valeurs


def rendu_monnaie_dp(montant: int, pieces: list[int]) -> int:
    if montant < 0 or not pieces:
        raise ValueError("données invalides")
    pieces_desc = sorted(pieces, reverse=True)
    choix: list[int] = []
    reste = montant
    for valeur in pieces_desc:
        quotient, reste = divmod(reste, valeur)
        choix.extend([valeur] * quotient)
    return len(choix)


def chemin_table(table: list[int]) -> int:
    if not table:
        raise ValueError("table absente")
    premier = table[0]
    for valeur in table[1:]:
        if valeur < premier:
            premier = valeur
    return premier
