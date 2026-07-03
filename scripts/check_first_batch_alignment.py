#!/usr/bin/env python3
"""Check alignment across ready batch supports and student-facing sessions."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re

from scripts._qa_common import ROOT, load_program_entries
from scripts.check_first_batch_document_quality import FIRST_BATCH_PREFIXES, find_kind_file

SESSION_FILES = [ROOT / "03_progressions/seances_premiere.md", ROOT / "03_progressions/seances_terminale.md"]
CAPACITY_RE = re.compile(r"\b[PT]-[A-Z]+(?:-[A-Z]+)*-\d{2}[A-Z]?\b")
OBJECTIVE_RE = re.compile(r"Objectif\s+(O\d+)\b")
ERROR_RE = re.compile(r"Erreur fréquente\s+(EF\d+)\b")


@dataclass
class AlignmentResult:
    errors: list[str] = field(default_factory=list)


def read(path: Path | None) -> str:
    if not path or not path.exists():
        return ""
    text = path.read_text(encoding="utf-8", errors="replace")
    # Strip YAML frontmatter so capacity IDs in metadata are not mistaken for content
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4:]
    return text


def numbers(pattern: str, text: str) -> set[int]:
    return {int(item) for item in re.findall(pattern, text, flags=re.M)}


def ids(regex: re.Pattern[str], text: str) -> set[str]:
    return set(regex.findall(text))


def sequence_errors(root: Path, prefix: str, program_ids: set[str]) -> list[str]:
    errors: list[str] = []
    paths = {kind: find_kind_file(root, prefix, kind) for kind in ["cours", "trace", "td", "tp", "corrige", "evaluation", "bareme", "remediation"]}
    missing = [kind for kind, path in paths.items() if path is None]
    if missing:
        return [f"{prefix}: documents manquants pour alignement -> {', '.join(missing)}"]

    texts = {kind: read(path) for kind, path in paths.items()}
    course_objectives = ids(OBJECTIVE_RE, texts["cours"])
    worked_text = "\n".join(texts[kind] for kind in ["td", "tp", "evaluation"])
    for objective in sorted(course_objectives):
        if objective not in worked_text:
            errors.append(f"{prefix}: objectif {objective} absent du TD/TP/évaluation")

    td_exercises = numbers(r"^###\s+Exercice\s+(\d+)\b", texts["td"])
    corrected = numbers(r"^###\s+Corrigé exercice\s+(\d+)\b", texts["corrige"])
    for exercise in sorted(td_exercises - corrected):
        errors.append(f"{prefix}: Exercice {exercise} sans corrigé")

    questions = numbers(r"^###\s+Question\s+(\d+)\b", texts["evaluation"])
    scored = numbers(r"^###\s+Barème question\s+(\d+)\b", texts["bareme"])
    for question in sorted(questions - scored):
        errors.append(f"{prefix}: Question {question} sans barème")

    for error_id in sorted(ids(ERROR_RE, texts["cours"] + "\n" + texts["td"] + "\n" + texts["evaluation"])):
        if f"Activité corrective {error_id}" not in texts["remediation"]:
            errors.append(f"{prefix}: {error_id} sans remédiation")

    course_capacities = set(CAPACITY_RE.findall(texts["cours"]))
    for capacity in sorted(course_capacities):
        if capacity not in program_ids:
            errors.append(f"{prefix}: capacité inconnue -> {capacity}")
        if capacity not in worked_text:
            errors.append(f"{prefix}: capacité {capacity} non travaillée")
        if capacity not in texts["evaluation"]:
            errors.append(f"{prefix}: capacité {capacity} non évaluée")
    return errors


def student_session_errors(root: Path, prefixes: list[str]) -> list[str]:
    errors: list[str] = []
    forbidden = re.compile(r"\b[PT]\d{2}_(?:corrige|bareme)_[A-Za-z0-9_]+\.md\b")
    prefix_re = re.compile(r"^### Séance ((?:%s)-S\d+)" % "|".join(prefixes), re.M)
    any_session_re = re.compile(r"^### Séance [PT]\d{2}-S\d+", re.M)
    for session_file in SESSION_FILES:
        if not session_file.exists() or not session_file.is_relative_to(root):
            continue
        text = session_file.read_text(encoding="utf-8", errors="replace")
        starts = [(match.group(1), match.start()) for match in prefix_re.finditer(text)]
        for index, (session_id, start) in enumerate(starts):
            next_any = any_session_re.search(text, start + 1)
            end = next_any.start() if next_any else len(text)
            block = text[start:end]
            for line in block.splitlines():
                if line.startswith("- Document utilisé :") and forbidden.search(line):
                    errors.append(f"{session_id}: document professeur cité comme document élève")
    return errors


def analyze_alignment(root: Path = ROOT, prefixes: list[str] | None = None, program_ids: set[str] | None = None) -> AlignmentResult:
    prefixes = prefixes or FIRST_BATCH_PREFIXES
    program_ids = program_ids or set(load_program_entries())
    result = AlignmentResult()
    for prefix in prefixes:
        result.errors.extend(sequence_errors(root, prefix, program_ids))
    result.errors.extend(student_session_errors(root, prefixes))
    return result


def main() -> int:
    result = analyze_alignment()
    if result.errors:
        print("check_first_batch_alignment: KO")
        for error in result.errors[:120]:
            print(f"- {error}")
        return 1
    print("check_first_batch_alignment: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
