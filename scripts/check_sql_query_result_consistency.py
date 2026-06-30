#!/usr/bin/env python3
"""Check SQL examples against their announced results."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
import re
import sqlite3

from scripts._qa_common import ROOT


TARGET_ROOTS = [
    ROOT / "03_progressions" / "supports" / "terminale" / "T10",
    ROOT / "03_progressions" / "fiches_cours" / "terminale" / "T10",
]

EXPECTED_LINE_RE = re.compile(r"(?:réponse|résultat|sortie|après|question)\s+(?:attendue?|finale?|secondaire|principale)?", re.I)
NOTE_FILTER_RE = re.compile(r"note\s*>=\s*(\d+)", re.I)
NAME_NOTE_RE = re.compile(r"\b([A-ZÉÈÀÂÊÎÔÛÇ][A-Za-zÉÈÀÂÊÎÔÛÇéèàâêîôûç-]+)\s+(\d{1,2})\b")
NAME_NOTE_TABLE_RE = re.compile(r"\|\s*([A-ZÉÈÀÂÊÎÔÛÇ][A-Za-zÉÈÀÂÊÎÔÛÇéèàâêîôûç-]+)\s*\|\s*(\d{1,2})\s*\|")
NON_PERSON_RESULT_WORDS = {"Question", "Réponse", "Reponse", "Exercice", "Point"}
UPDATE_RE = re.compile(r"\bUPDATE\s+\w+\s+SET\b", re.I)
DELETE_RE = re.compile(r"\bDELETE\s+FROM\s+\w+\b", re.I)
SQL_IN_BACKTICKS_RE = re.compile(r"`\s*((?:SELECT|UPDATE|DELETE)\b[^`]+?)\s*`", re.I | re.S)
SQL_LINE_RE = re.compile(r"\b((?:SELECT|UPDATE|DELETE)\b[^;\n]*(?:;|$))", re.I)


@dataclass
class SqlConsistencyResult:
    errors: list[str] = field(default_factory=list)
    files_checked: int = 0


def expected_lines(text: str) -> list[str]:
    lines = text.splitlines()
    result: list[str] = []
    for line in lines:
        if EXPECTED_LINE_RE.search(line) or "JOIN ->" in line or "->" in line:
            result.append(line)
    return result


def line_is_warning(line: str) -> bool:
    return bool(re.search(r"sans\s+where|erreur|risque|trop large|modifie toutes|supprime toutes|interdit", line, re.I))


def create_demo_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE Eleve(id_eleve INTEGER PRIMARY KEY, nom TEXT, classe TEXT)")
    conn.execute("CREATE TABLE Note(id_note INTEGER PRIMARY KEY, id_eleve INTEGER, matiere TEXT, note INTEGER)")
    conn.executemany("INSERT INTO Eleve VALUES (?, ?, ?)", [(1, "Ada", "T1"), (2, "Linus", "T2")])
    conn.executemany("INSERT INTO Note VALUES (?, ?, ?, ?)", [(10, 1, "NSI", 17), (11, 2, "NSI", 13)])
    return conn


def normalize_query(query: str) -> str:
    query = re.sub(r"\s+", " ", query.strip().rstrip(";"))
    query = query.split("->", 1)[0].strip()
    return query


def execute_sql_query(query: str) -> list[tuple[Any, ...]]:
    query = normalize_query(query)
    if not query.upper().startswith("SELECT"):
        raise ValueError("not a SELECT query")
    with create_demo_connection() as conn:
        cursor = conn.execute(query)
        return [tuple(row) for row in cursor.fetchall()]


def execute_sql_update_summary(query: str) -> dict[str, int]:
    query = normalize_query(query)
    if not query.upper().startswith("UPDATE"):
        raise ValueError("not an UPDATE query")
    with create_demo_connection() as conn:
        conn.execute(query)
        rows = conn.execute(
            "SELECT Eleve.nom, Note.note FROM Eleve JOIN Note ON Eleve.id_eleve = Note.id_eleve ORDER BY Eleve.nom"
        ).fetchall()
        return {str(name): int(note) for name, note in rows}


def execute_sql_delete_summary(query: str) -> dict[str, int]:
    query = normalize_query(query)
    if not query.upper().startswith("DELETE"):
        raise ValueError("not a DELETE query")
    with create_demo_connection() as conn:
        conn.execute(query)
        rows = conn.execute(
            "SELECT Eleve.nom, Note.note FROM Eleve JOIN Note ON Eleve.id_eleve = Note.id_eleve ORDER BY Eleve.nom"
        ).fetchall()
        return {str(name): int(note) for name, note in rows}


def extract_sql_statements(text: str) -> list[str]:
    result: list[str] = []
    for regex in (SQL_IN_BACKTICKS_RE, SQL_LINE_RE):
        for match in regex.finditer(text):
            query = normalize_query(match.group(1))
            upper = query.upper()
            if upper.startswith("SELECT") and " FROM " not in f" {upper} ":
                continue
            if upper.startswith("DELETE") and " FROM " not in f" {upper} ":
                continue
            if upper.startswith("UPDATE") and " SET " not in f" {upper} ":
                continue
            if query and query not in result:
                result.append(query)
    return result


def query_targets_demo_schema(query: str) -> bool:
    lowered = query.lower()
    return "eleve" in lowered or "note" in lowered


def announced_person_note_pairs(text: str) -> list[tuple[str, int]]:
    pairs: list[tuple[str, int]] = []
    for line in expected_lines(text):
        for name, raw_note in NAME_NOTE_RE.findall(line):
            if name not in NON_PERSON_RESULT_WORDS:
                pairs.append((name, int(raw_note)))
    for name, raw_note in NAME_NOTE_TABLE_RE.findall(text):
        if name not in NON_PERSON_RESULT_WORDS and name.lower() not in {"nom", "note"}:
            pairs.append((name, int(raw_note)))
    return pairs


def sql_block_errors(text: str) -> list[str]:
    errors: list[str] = []
    statements = extract_sql_statements(text)
    filters = [int(value) for value in NOTE_FILTER_RE.findall(text)]
    for threshold in filters:
        for line in expected_lines(text):
            for name, raw_note in NAME_NOTE_RE.findall(line):
                if name in NON_PERSON_RESULT_WORDS:
                    continue
                note = int(raw_note)
                if note < threshold:
                    errors.append(
                        f"condition note >= {threshold} contredite par le résultat {name} {note}"
                    )

    for line in text.splitlines():
        if UPDATE_RE.search(line) and "WHERE" not in line.upper() and not line_is_warning(line):
            errors.append("UPDATE sans WHERE présenté comme requête opérationnelle")
        if DELETE_RE.search(line) and "WHERE" not in line.upper() and not line_is_warning(line):
            errors.append("DELETE sans WHERE présenté comme requête opérationnelle")
        is_join_query = bool(re.search(r"(?:^|`|\s)SELECT\s+.+?\s+FROM\s+.+?\s+JOIN\b", line, re.I))
        if is_join_query and " ON " not in f" {line.upper()} ":
            if not re.search(r"sans\s+on|cartésien|non maîtrisée|erreur|cas limite", line, re.I):
                errors.append("JOIN sans condition non signalée comme produit cartésien ou erreur")

    for query in statements:
        upper = query.upper()
        if " JOIN " in upper and " ON " not in f" {upper} ":
            if not re.search(r"sans\s+on|cartésien|produit cartésien|erreur|interdit", text, re.I):
                errors.append("JOIN sans ON non traité explicitement comme produit cartésien")
        if not query_targets_demo_schema(query):
            continue
        try:
            if upper.startswith("SELECT"):
                actual = execute_sql_query(query)
                expected_pairs = announced_person_note_pairs(text)
                has_note_result_table = bool(re.search(r"\|\s*nom\s*\|\s*note\s*\|", text, re.I))
                if expected_pairs and has_note_result_table and actual and len(actual[0]) >= 2:
                    actual_pairs = {(str(row[0]), int(row[1])) for row in actual if len(row) >= 2 and isinstance(row[1], int)}
                    expected_set = set(expected_pairs)
                    if expected_set != actual_pairs:
                        errors.append(
                            f"résultat SQL annoncé {sorted(expected_set)} différent du résultat SQLite {sorted(actual_pairs)}"
                        )
            elif upper.startswith("UPDATE") and "WHERE" in upper:
                summary = execute_sql_update_summary(query)
                if re.search(r"Ada\s+18", text) and summary.get("Ada") != 18:
                    errors.append("UPDATE annoncé Ada 18 mais SQLite ne produit pas Ada 18")
                if re.search(r"Linus\s+18", text) and summary.get("Linus") != 18:
                    errors.append("UPDATE annoncé Linus 18 mais la requête ciblée ne le modifie pas")
            elif upper.startswith("DELETE") and "WHERE" in upper:
                summary = execute_sql_delete_summary(query)
                if re.search(r"Linus\s+(?:retiré|retire|supprimé|supprime|absent)", text, re.I) and "Linus" in summary:
                    errors.append("DELETE annoncé Linus retiré mais SQLite le conserve")
                if re.search(r"Ada\s+(?:retirée|retiree|supprimée|supprimee|absent)", text, re.I) and "Ada" in summary:
                    errors.append("DELETE annoncé Ada retirée mais SQLite la conserve")
        except sqlite3.Error as exc:
            if not re.search(r"erreur|interdit|corriger|à éviter|a éviter", text, re.I):
                errors.append(f"requête SQL non exécutable sur le schéma de référence: {query} ({exc})")

    if re.search(r"UPDATE\s+Note\s+SET\s+note\s*=\s*18\s+WHERE\s+id_note\s*=\s*10", text, re.I):
        if re.search(r"Linus\s+18", text):
            errors.append("UPDATE id_note=10 modifie Linus alors que seule la note d'Ada est ciblée")
    if re.search(r"DELETE\s+FROM\s+Note\s+WHERE\s+id_note\s*=\s*11", text, re.I):
        if re.search(r"Ada\s+(?:retirée|supprimée|effacée)", text, re.I):
            errors.append("DELETE id_note=11 retire Ada alors que seule la note de Linus est ciblée")
    return errors


def sql_block_is_consistent(text: str) -> bool:
    return not sql_block_errors(text)


def candidate_files(root: Path = ROOT) -> list[Path]:
    files: list[Path] = []
    for base in TARGET_ROOTS:
        if not base.exists():
            continue
        files.extend(sorted(base.glob("*.md")))
    return files


def analyze_sql_query_result_consistency(root: Path = ROOT) -> SqlConsistencyResult:
    result = SqlConsistencyResult()
    for path in candidate_files(root):
        result.files_checked += 1
        text = path.read_text(encoding="utf-8", errors="replace")
        for error in sql_block_errors(text):
            result.errors.append(f"{path.relative_to(root).as_posix()}: {error}")
    return result


def main() -> int:
    result = analyze_sql_query_result_consistency()
    if result.errors:
        print("check_sql_query_result_consistency: KO")
        for error in result.errors[:200]:
            print(f"- {error}")
        return 1
    print(f"check_sql_query_result_consistency: PASS ({result.files_checked} fichiers T10)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
