"""Tests attendus TP T10. Statut pédagogique: needs_review."""
from __future__ import annotations
import importlib, os
MODULE = importlib.import_module(os.environ.get("TP_MODULE", "T10_starter_sql_select_where_join"))


def test_nominal_select_join_where() -> None:
    conn = MODULE.creer_base()
    assert MODULE.notes_minimum(conn, 15) == [("Ada", 17)]
    assert MODULE.notes_minimum(conn, 10) == [("Ada", 17), ("Linus", 13)]


def test_limite_update_delete_cibles() -> None:
    conn = MODULE.creer_base()
    assert MODULE.modifier_note(conn, 10, 18) == [("Ada", 18), ("Linus", 13)]
    assert MODULE.supprimer_note(conn, 11) == [("Ada", 18)]


def test_invalide_base_absente() -> None:
    try:
        MODULE.notes_minimum(None, 15)
    except ValueError:
        return
    raise AssertionError("ValueError attendue")

if __name__ == "__main__":
    test_nominal_select_join_where(); test_limite_update_delete_cibles(); test_invalide_base_absente(); print("tests attendus OK")
