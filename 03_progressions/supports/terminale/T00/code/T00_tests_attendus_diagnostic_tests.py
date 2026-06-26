"""Tests attendus TP T00."""

from __future__ import annotations

from T00_starter_diagnostic_tests import maximum_controle


def test_nominal() -> None:
    sortie = maximum_controle([3, 8, 2])
    assert sortie["controle"] == "8 avec test nominal, test limite et test d’erreur"
    assert sortie["cas_limite"] == "liste vide ou mutation inattendue"


def test_entree_absente() -> None:
    try:
        maximum_controle(None)
    except ValueError:
        return
    raise AssertionError("ValueError attendue pour entrée absente")


if __name__ == "__main__":
    test_nominal()
    test_entree_absente()
    print("tests attendus OK")
