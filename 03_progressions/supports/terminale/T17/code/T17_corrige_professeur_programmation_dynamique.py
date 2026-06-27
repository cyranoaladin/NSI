"""Corrigé professeur TP T17 programmation dynamique. Statut pédagogique: needs_review."""
from __future__ import annotations


def fibonacci_dp(n: int) -> list[int]:
    if n < 0:
        raise ValueError("n invalide")
    if n == 0:
        return [0]
    table = [0, 1]
    for i in range(2, n + 1):
        table.append(table[i - 1] + table[i - 2])
    return table


def rendu_monnaie_dp(montant: int, pieces: list[int]) -> int:
    if montant < 0 or not pieces:
        raise ValueError("données invalides")
    inf = montant + 1
    dp = [0] + [inf] * montant
    for valeur in range(1, montant + 1):
        dp[valeur] = min((dp[valeur - p] + 1 for p in pieces if p <= valeur), default=inf)
    return dp[montant]


def chemin_table(table: list[int]) -> int:
    if not table:
        raise ValueError("table absente")
    return table[-1]
