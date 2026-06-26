"""Asset Python TP. Statut pédagogique: needs_review."""

from __future__ import annotations

import importlib
import os

MODULE = importlib.import_module(os.environ.get("TP_MODULE", "P04_starter_types_construits"))
resume_mesures = MODULE.resume_mesures

def test_nominal() -> None:
    result = resume_mesures([12, 14, 13])
    assert result["moyenne"] == 13 and result["maximum"] == 14

def test_limite() -> None:
    result = resume_mesures([])
    assert result["moyenne"] is None

def test_invalide() -> None:
    try:
        resume_mesures(None)
    except (ValueError, TypeError, IndexError):
        return
    raise AssertionError("exception attendue")

if __name__ == "__main__":
    test_nominal()
    test_limite()
    test_invalide()
    print("tests attendus OK")
