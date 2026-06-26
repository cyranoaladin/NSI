"""Tests attendus TP P04."""

from __future__ import annotations

from P04_starter_types_construits import resume_mesures


def test_nominal() -> None:
    sortie = resume_mesures([12, 14, 13])
    assert sortie["controle"] == "tuple non modifié, liste mise à jour, dictionnaire consulté par clé"
    assert sortie["cas_limite"] == "copie de liste et clé absente"


def test_entree_absente() -> None:
    try:
        resume_mesures(None)
    except ValueError:
        return
    raise AssertionError("ValueError attendue pour entrée absente")


if __name__ == "__main__":
    test_nominal()
    test_entree_absente()
    print("tests attendus OK")
