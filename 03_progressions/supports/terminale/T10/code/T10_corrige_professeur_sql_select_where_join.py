"""Corrigé professeur TP T10 SQL. Statut pédagogique: needs_review."""
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
    cur = conn.execute("""
        SELECT Eleve.nom, Note.note
        FROM Eleve JOIN Note ON Eleve.id_eleve = Note.id_eleve
        WHERE Note.note >= ?
        ORDER BY Note.note DESC
    """, (seuil,))
    return list(cur.fetchall())


def modifier_note(conn: sqlite3.Connection, id_note: int, valeur: int) -> list[tuple[str, int]]:
    if conn is None:
        raise ValueError("base absente")
    conn.execute("UPDATE Note SET note = ? WHERE id_note = ?", (valeur, id_note))
    return notes_minimum(conn, 0)


def supprimer_note(conn: sqlite3.Connection, id_note: int) -> list[tuple[str, int]]:
    if conn is None:
        raise ValueError("base absente")
    conn.execute("DELETE FROM Note WHERE id_note = ?", (id_note,))
    return notes_minimum(conn, 0)
