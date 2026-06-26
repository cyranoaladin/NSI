"""Tests attendus TP P02."""

from __future__ import annotations

from P02_starter_complement_booleens import twos_complement_value


def test_nominal() -> None:
    sortie = twos_complement_value("11101001")
    assert sortie["controle"] == "11101001 et simplification en a"
    assert sortie["cas_limite"] == "140 impossible sur 8 bits signés"


def test_entree_absente() -> None:
    try:
        twos_complement_value(None)
    except ValueError:
        return
    raise AssertionError("ValueError attendue pour entrée absente")


if __name__ == "__main__":
    test_nominal()
    test_entree_absente()
    print("tests attendus OK")
