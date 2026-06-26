"""Tests attendus TP T03."""

from __future__ import annotations

from T03_starter_piles_files_dictionnaires import jouer_operations


def test_nominal() -> None:
    sortie = jouer_operations([("push", "A"), ("push", "B"), ("pop", None)])
    assert sortie["controle"] == "B sort avant A pour une pile ; A sort avant B pour une file"
    assert sortie["cas_limite"] == "dépiler ou défiler une structure vide"


def test_entree_absente() -> None:
    try:
        jouer_operations(None)
    except ValueError:
        return
    raise AssertionError("ValueError attendue pour entrée absente")


if __name__ == "__main__":
    test_nominal()
    test_entree_absente()
    print("tests attendus OK")
