"""Asset Python TP. Statut pédagogique: needs_review."""

from __future__ import annotations

import importlib
import os

MODULE = importlib.import_module(os.environ.get("TP_MODULE", "P05_starter_tables_csv"))
filtrer_table = MODULE.filtrer_table

def test_nominal() -> None:
    result = filtrer_table([{"nom":"Ada","age":"17"},{"nom":"Tim","age":"14"}])
    assert len(result["valides"]) == 1 and result["valides"][0]["nom"] == "Ada"

def test_limite() -> None:
    result = filtrer_table([{"nom":"Lin","age":"x"}])
    assert len(result["erreurs"]) == 1

def test_invalide() -> None:
    try:
        filtrer_table(None)
    except (ValueError, TypeError, IndexError):
        return
    raise AssertionError("exception attendue")

if __name__ == "__main__":
    test_nominal()
    test_limite()
    test_invalide()
    print("tests attendus OK")
