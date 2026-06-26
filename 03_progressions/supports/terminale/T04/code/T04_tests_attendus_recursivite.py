"""Tests attendus TP T04."""

from __future__ import annotations

from T04_starter_recursivite import factorielle


def test_nominal() -> None:
    sortie = factorielle(5)
    assert sortie["controle"] == "120 avec cas de base factorielle(0)=1"
    assert sortie["cas_limite"] == "appel récursif sans diminution ou profondeur excessive"


def test_entree_absente() -> None:
    try:
        factorielle(None)
    except ValueError:
        return
    raise AssertionError("ValueError attendue pour entrée absente")


if __name__ == "__main__":
    test_nominal()
    test_entree_absente()
    print("tests attendus OK")
