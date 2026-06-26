"""Tests attendus TP T05."""

from __future__ import annotations

from T05_starter_arbres_binaires import parcours_infixe


def test_nominal() -> None:
    sortie = parcours_infixe((4, (2, None, None), (7, None, None)))
    assert sortie["controle"] == "parcours infixe 2, 4, 7"
    assert sortie["cas_limite"] == "arbre vide ou arbre très déséquilibré"


def test_entree_absente() -> None:
    try:
        parcours_infixe(None)
    except ValueError:
        return
    raise AssertionError("ValueError attendue pour entrée absente")


if __name__ == "__main__":
    test_nominal()
    test_entree_absente()
    print("tests attendus OK")
