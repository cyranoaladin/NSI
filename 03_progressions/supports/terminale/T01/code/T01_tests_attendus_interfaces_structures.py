"""Asset Python TP. Statut pédagogique: needs_review."""

from __future__ import annotations

import importlib
import os

MODULE = importlib.import_module(os.environ.get("TP_MODULE", "T01_starter_interfaces_structures"))
scenario_structure = MODULE.scenario_structure

def test_nominal() -> None:
    result = scenario_structure([("ajouter", 4), ("ajouter", 7), ("retirer", None)])
    assert result == [7]

def test_limite() -> None:
    result = scenario_structure([("ajouter", 1), ("retirer", None)])
    assert result == [1]

def test_invalide() -> None:
    try:
        scenario_structure([("retirer", None)])
    except (ValueError, TypeError, IndexError):
        return
    raise AssertionError("exception attendue")

if __name__ == "__main__":
    test_nominal()
    test_limite()
    test_invalide()
    print("tests attendus OK")
