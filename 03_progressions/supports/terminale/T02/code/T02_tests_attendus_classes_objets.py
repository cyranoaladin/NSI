"""Tests attendus TP T02."""

from __future__ import annotations

from T02_starter_classes_objets import creer_compte


def test_nominal() -> None:
    sortie = creer_compte(20)
    assert sortie["controle"] == "solde 13 si l’invariant reste vérifié"
    assert sortie["cas_limite"] == "montant négatif ou accès direct à l’attribut"


def test_entree_absente() -> None:
    try:
        creer_compte(None)
    except ValueError:
        return
    raise AssertionError("ValueError attendue pour entrée absente")


if __name__ == "__main__":
    test_nominal()
    test_entree_absente()
    print("tests attendus OK")
