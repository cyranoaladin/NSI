"""Tests attendus TP P00."""

from __future__ import annotations

from P00_starter_diagnostic_python import predict_trace


def test_nominal() -> None:
    sortie = predict_trace([("x", 3), ("x", 5)])
    assert sortie["controle"] == "5"
    assert sortie["cas_limite"] == "réaffectation avec zéro ou valeur négative"


def test_entree_absente() -> None:
    try:
        predict_trace(None)
    except ValueError:
        return
    raise AssertionError("ValueError attendue pour entrée absente")


if __name__ == "__main__":
    test_nominal()
    test_entree_absente()
    print("tests attendus OK")
