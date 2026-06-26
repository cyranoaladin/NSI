"""Tests attendus TP P01."""

from __future__ import annotations

from P01_starter_conversions_bases import convert_base


def test_nominal() -> None:
    sortie = convert_base(45)
    assert sortie["controle"] == "101101 en base deux et 2D en base seize"
    assert sortie["cas_limite"] == "0, 1 et changement de base avec un chiffre interdit"


def test_entree_absente() -> None:
    try:
        convert_base(None)
    except ValueError:
        return
    raise AssertionError("ValueError attendue pour entrée absente")


if __name__ == "__main__":
    test_nominal()
    test_entree_absente()
    print("tests attendus OK")
