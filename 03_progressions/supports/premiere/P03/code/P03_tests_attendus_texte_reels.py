"""Tests attendus TP P03."""

from __future__ import annotations

from P03_starter_texte_reels import inspect_text


def test_nominal() -> None:
    sortie = inspect_text("Aé")
    assert sortie["controle"] == "2 caractères, 3 octets, somme flottante non exactement égale à 0.3"
    assert sortie["cas_limite"] == "caractère hors ASCII ou comparaison directe de flottants"


def test_entree_absente() -> None:
    try:
        inspect_text(None)
    except ValueError:
        return
    raise AssertionError("ValueError attendue pour entrée absente")


if __name__ == "__main__":
    test_nominal()
    test_entree_absente()
    print("tests attendus OK")
