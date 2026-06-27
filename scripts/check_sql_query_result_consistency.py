#!/usr/bin/env python3
"""Check SQL examples against their announced results."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re

from _qa_common import ROOT


TARGET_ROOTS = [
    ROOT / "03_progressions" / "supports" / "terminale" / "T10",
    ROOT / "03_progressions" / "fiches_cours" / "terminale" / "T10",
]

EXPECTED_LINE_RE = re.compile(r"(?:réponse|résultat|sortie|après|question)\s+(?:attendue?|finale?|secondaire|principale)?", re.I)
NOTE_FILTER_RE = re.compile(r"note\s*>=\s*(\d+)", re.I)
NAME_NOTE_RE = re.compile(r"\b([A-ZÉÈÀÂÊÎÔÛÇ][A-Za-zÉÈÀÂÊÎÔÛÇéèàâêîôûç-]+)\s+(\d{1,2})\b")
NON_PERSON_RESULT_WORDS = {"Question", "Réponse", "Reponse", "Exercice", "Point"}
UPDATE_RE = re.compile(r"\bUPDATE\s+\w+\s+SET\b", re.I)
DELETE_RE = re.compile(r"\bDELETE\s+FROM\s+\w+\b", re.I)


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


def sql_block_errors(text: str) -> list[str]:
    errors: list[str] = []
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
