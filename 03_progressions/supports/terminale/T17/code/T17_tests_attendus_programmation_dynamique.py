"""Tests attendus TP T17. Statut pédagogique: needs_review."""
from __future__ import annotations
import importlib, os
MODULE = importlib.import_module(os.environ.get("TP_MODULE", "T17_starter_programmation_dynamique"))


def test_nominal_fibonacci_rendu() -> None:
    assert MODULE.fibonacci_dp(6) == [0, 1, 1, 2, 3, 5, 8]
    assert MODULE.rendu_monnaie_dp(6, [1, 3, 4]) == 2


def test_limite_zero_table() -> None:
    assert MODULE.fibonacci_dp(0) == [0]
    assert MODULE.chemin_table([0, 1, 1, 2, 3]) == 3


def test_invalide_n_negatif() -> None:
    try:
        MODULE.fibonacci_dp(-1)
    except ValueError:
        return
    raise AssertionError("ValueError attendue")

if __name__ == "__main__":
    test_nominal_fibonacci_rendu(); test_limite_zero_table(); test_invalide_n_negatif(); print("tests attendus OK")
