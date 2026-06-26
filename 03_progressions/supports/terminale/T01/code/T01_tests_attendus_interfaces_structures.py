"""Tests attendus TP T01."""

from __future__ import annotations

from T01_starter_interfaces_structures import scenario_structure


def test_nominal() -> None:
    sortie = scenario_structure([("ajouter", 4), ("retirer", None)])
    assert sortie["controle"] == "interface séparée de la représentation interne"
    assert sortie["cas_limite"] == "confondre interface et liste Python concrète"


def test_entree_absente() -> None:
    try:
        scenario_structure(None)
    except ValueError:
        return
    raise AssertionError("ValueError attendue pour entrée absente")


if __name__ == "__main__":
    test_nominal()
    test_entree_absente()
    print("tests attendus OK")
