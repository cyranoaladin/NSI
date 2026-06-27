"""Starter TP T10 SQL. Statut pédagogique: needs_review."""
from __future__ import annotations
import sqlite3


def creer_base() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE Eleve(id_eleve INTEGER PRIMARY KEY, nom TEXT, classe TEXT)")
    conn.execute("CREATE TABLE Note(id_note INTEGER PRIMARY KEY, id_eleve INTEGER, matiere TEXT, note INTEGER)")
    conn.executemany("INSERT INTO Eleve VALUES (?,?,?)", [(1,"Ada","T1"),(2,"Linus","T2")])
    conn.executemany("INSERT INTO Note VALUES (?,?,?,?)", [(10,1,"NSI",17),(11,2,"NSI",13)])
    return conn


def notes_minimum(conn: sqlite3.Connection, seuil: int) -> list[tuple[str, int]]:
    if conn is None:
        raise ValueError("base absente")
    return []


def modifier_note(conn: sqlite3.Connection, id_note: int, valeur: int) -> list[tuple[str, int]]:
    if conn is None:
        raise ValueError("base absente")
    return []


def supprimer_note(conn: sqlite3.Connection, id_note: int) -> list[tuple[str, int]]:
    if conn is None:
        raise ValueError("base absente")
    return []
