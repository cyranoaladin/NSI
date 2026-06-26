#!/usr/bin/env python3
"""Check course sheets are aligned with progression and do not validate coverage."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re

from _qa_common import ROOT, read_frontmatter
from _course_sheets_common import (
    frontmatter_capacities,
    planned_sequences,
    program_ids as load_program_ids,
    section_text,
    sheet_files,
)

FORBIDDEN_COVERAGE_CLAIMS = [
    "capacité couverte",
    "capacite couverte",
    "covered",
    "published",
    "validated_pedagogy",
    "validated_science",
    "validated_technical",
    "remplace le cours",
    "remplace le td",
    "remplace le corrigé",
    "remplace le corrige",
]


@dataclass
class CourseSheetAlignmentResult:
    errors: list[str] = field(default_factory=list)
    checked_files: int = 0


def link_block_errors(path: Path, text: str, sequence_id: str) -> list[str]:
    errors: list[str] = []
    block = section_text(text, "Lien avec la progression")
    lowered = block.lower()
    if not block:
        return [f"{path}: lien avec la progression absent"]
    if not re.search(rf"\b{sequence_id}-S\d+\b", block):
        errors.append(f"{path}: aucune séance liée")
    if not any(marker in lowered for marker in ["td", "tp", "évaluation", "evaluation", "projet"]):
        errors.append(f"{path}: aucun TD, TP, évaluation ou projet lié")
    return errors


def analyze_sheet_alignment(path: Path, program_ids: set[str], planned_ids: set[str]) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    lowered = text.lower()
    metadata = read_frontmatter(path)
    sequence_id = str(metadata.get("sequence_id") or path.name[:3])
    if sequence_id not in planned_ids:
        errors.append(f"{path}: sequence_id absent de la progression -> {sequence_id}")
    errors.extend(link_block_errors(path, text, sequence_id))

    capacities = frontmatter_capacities(metadata)
    body = text.split("---", 2)[-1] if text.startswith("---") else text
    for capacity in sorted(capacities):
        if capacity not in program_ids:
            errors.append(f"{path}: capacité absente du YAML officiel -> {capacity}")
        if body.count(capacity) == 0:
            errors.append(f"{path}: capacité déclarée non réellement traitée -> {capacity}")

    for phrase in FORBIDDEN_COVERAGE_CLAIMS:
        if phrase in lowered:
            errors.append(f"{path}: prétention de couverture ou remplacement interdite -> {phrase}")
    return errors


def analyze_course_sheets_alignment(root: Path = ROOT, program_ids: set[str] | None = None) -> CourseSheetAlignmentResult:
    result = CourseSheetAlignmentResult()
    ids = program_ids or load_program_ids()
    planned_ids = set(planned_sequences(root))
    files = sheet_files(root)
    if not files:
        result.errors.append("aucune fiche de cours")
        return result
    for path in files:
        result.checked_files += 1
        result.errors.extend(analyze_sheet_alignment(path, ids, planned_ids))
    return result


def main() -> int:
    result = analyze_course_sheets_alignment()
    if result.errors:
        print("check_course_sheets_alignment: KO")
        for error in result.errors[:180]:
            print(f"- {error}")
        return 1
    print(f"check_course_sheets_alignment: PASS ({result.checked_files} fiches)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
