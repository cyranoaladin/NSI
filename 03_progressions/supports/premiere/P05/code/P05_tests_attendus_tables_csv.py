"""Tests attendus TP P05."""

from __future__ import annotations

from P05_starter_tables_csv import filtrer_table


def test_nominal() -> None:
    sortie = filtrer_table([{"nom":"Ada", "age":"17"}])
    assert sortie["controle"] == "liste de dictionnaires filtrée puis moyenne calculée"
    assert sortie["cas_limite"] == "champ vide, séparateur inattendu ou nombre invalide"


def test_entree_absente() -> None:
    try:
        filtrer_table(None)
    except ValueError:
        return
    raise AssertionError("ValueError attendue pour entrée absente")


if __name__ == "__main__":
    test_nominal()
    test_entree_absente()
    print("tests attendus OK")
