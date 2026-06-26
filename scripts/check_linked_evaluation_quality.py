#!/usr/bin/env python3
"""Check quality of evaluation supports linked to course sheets."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re

from _qa_common import ROOT, read_frontmatter, strip_frontmatter
from _course_sheets_common import course_sheet_links, sheet_files

REQUIRED_FRONTMATTER = ["title", "level", "sequence_id", "document_type", "status", "official_program"]
TARGET_PREFIXES = {f"P{index:02d}" for index in range(10, 15)} | {f"T{index:02d}" for index in range(10, 20)}


@dataclass
class LinkedEvaluationQualityResult:
    errors: list[str] = field(default_factory=list)
    checked_files: int = 0


def target_evaluation_files(root: Path = ROOT) -> list[Path]:
    return sorted(path for path in expected_evaluation_files(root).values() if path is not None)


def resolve_reference(root: Path, reference: str) -> Path | None:
    candidate = root / reference
    if candidate.exists():
        return candidate
    if "/" in reference:
        return None
    matches = sorted(root.rglob(reference))
    return matches[0] if matches else None


def expected_evaluation_files(root: Path = ROOT) -> dict[str, Path | None]:
    expected: dict[str, Path | None] = {}
    for sheet in sheet_files(root):
        if sheet.name[:3] not in TARGET_PREFIXES:
            continue
        for link in course_sheet_links(sheet):
            element = link.element.lower().strip()
            if element.startswith("évaluation") or element.startswith("evaluation"):
                expected[link.file] = resolve_reference(root, link.file)
    return expected


def count_question_headings(text: str) -> int:
    return len(re.findall(r"^###\s+Question\s+\d+\b", text, flags=re.M | re.I))


def analyze_one_evaluation(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    body = strip_frontmatter(text)
    metadata = read_frontmatter(path)
    rel = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
    missing_fm = [key for key in REQUIRED_FRONTMATTER if key not in metadata]
    if missing_fm:
        errors.append(f"{rel}: frontmatter incomplet -> {', '.join(missing_fm)}")
    if metadata.get("document_type") != "evaluation":
        errors.append(f"{rel}: document_type attendu evaluation")
    if metadata.get("status") != "needs_review":
        errors.append(f"{rel}: status attendu needs_review")
    official = metadata.get("official_program")
    capacities = official.get("capacities") if isinstance(official, dict) else None
    if not isinstance(capacities, list) or not capacities:
        errors.append(f"{rel}: capacités officielles absentes")

    questions = count_question_headings(body)
    if questions < 4 or questions > 6:
        errors.append(f"{rel}: 4 à 6 questions attendues, trouvé {questions}")
    lower = body.lower()
    if "durée" not in lower and "duree" not in lower:
        errors.append(f"{rel}: durée absente")
    if "matériel autorisé" not in lower and "materiel autorise" not in lower:
        errors.append(f"{rel}: matériel autorisé absent")
    if "capacités évaluées" not in lower and "capacites evaluees" not in lower:
        errors.append(f"{rel}: capacités évaluées absentes")
    bareme_lines = re.findall(r"question\s+\d+\s*:", lower)
    if len(bareme_lines) < questions:
        errors.append(f"{rel}: barème question par question incomplet")
    for marker in [
        "critères de réussite",
        "corrigé",
        "erreurs fréquentes",
        "remédiation",
        "fiche liée",
    ]:
        if marker not in lower:
            errors.append(f"{rel}: exigence évaluation manquante -> {marker}")
    if "aménagement" not in lower and "amenagement" not in lower and "version aménagée" not in lower:
        errors.append(f"{rel}: aménagement ou version aménagée absent")
    return errors


def analyze_linked_evaluation_quality(root: Path = ROOT, files: list[Path] | None = None) -> LinkedEvaluationQualityResult:
    result = LinkedEvaluationQualityResult()
    if files is not None:
        paths = {path.as_posix(): path for path in files}
    else:
        expected = expected_evaluation_files(root)
        paths = {reference: path for reference, path in expected.items() if path is not None}
        for reference, path in expected.items():
            if path is None:
                result.errors.append(f"{reference}: support évaluation absent")
    for path in paths.values():
        result.checked_files += 1
        result.errors.extend(analyze_one_evaluation(path))
    return result


def main() -> int:
    result = analyze_linked_evaluation_quality()
    if result.errors:
        print("check_linked_evaluation_quality: KO")
        for error in result.errors[:180]:
            print(f"- {error}")
        return 1
    print(f"check_linked_evaluation_quality: PASS ({result.checked_files} évaluations)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
