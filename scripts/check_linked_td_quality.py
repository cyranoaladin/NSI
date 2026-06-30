#!/usr/bin/env python3
"""Check quality of TD supports linked to operational course sheets."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re

from scripts._qa_common import ROOT, read_frontmatter, strip_frontmatter
from scripts._operational_links import ReferenceResolution, operational_resource_links, resolve_reference

REQUIRED_FRONTMATTER = ["title", "level", "sequence_id", "document_type", "status", "official_program"]


@dataclass
class LinkedTDQualityResult:
    errors: list[str] = field(default_factory=list)
    checked_files: int = 0


def target_td_files(root: Path = ROOT) -> list[Path]:
    return sorted(resolution.path for resolution in expected_td_files(root).values() if resolution.path is not None)


def expected_td_files(root: Path = ROOT) -> dict[str, ReferenceResolution]:
    expected: dict[str, ReferenceResolution] = {}
    for resource in operational_resource_links(root, {"td"}):
        expected[resource.link.file] = resolve_reference(root, resource.link.file)
    return expected


def count_headings(text: str, prefix: str) -> int:
    return len(re.findall(rf"^###\s+{re.escape(prefix)}\s+\d+\b", text, flags=re.M | re.I))


def analyze_one_td(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    body = strip_frontmatter(text)
    metadata = read_frontmatter(path)
    rel = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
    missing_fm = [key for key in REQUIRED_FRONTMATTER if key not in metadata]
    if missing_fm:
        errors.append(f"{rel}: frontmatter incomplet -> {', '.join(missing_fm)}")
    if metadata.get("document_type") != "td":
        errors.append(f"{rel}: document_type attendu td")
    if metadata.get("status") != "needs_review":
        errors.append(f"{rel}: status attendu needs_review")
    official = metadata.get("official_program")
    capacities = official.get("capacities") if isinstance(official, dict) else None
    if not isinstance(capacities, list) or not capacities:
        errors.append(f"{rel}: capacités officielles absentes")

    exercises = count_headings(body, "Exercice")
    corrections = count_headings(body, "Corrigé exercice")
    if exercises < 8:
        errors.append(f"{rel}: minimum 8 exercices requis, trouvé {exercises}")
    if corrections < exercises:
        errors.append(f"{rel}: corrigé manquant pour au moins un exercice ({corrections}/{exercises})")

    lower = body.lower()
    lecture_count = len(
        re.findall(
            r"type\s*:\s*lecture/analyse|lecture|analyse|analyser|identifier|rechercher|trier|comparer|reperer|repérer",
            lower,
        )
    )
    production_count = len(re.findall(r"type\s*:\s*production/(?:é|e)criture|production attendue|ecrire|écrire|produire", lower))
    checks = [
        ("lecture/analyse", lecture_count >= 2),
        ("production/écriture", production_count >= 2),
        ("cas limite", "cas limite" in lower),
        ("justification", "justification" in lower or "justifier" in lower),
        ("progression socle", "socle" in lower),
        ("progression standard", "standard" in lower),
        ("progression approfondissement", "approfondissement" in lower or "expert" in lower),
        ("erreurs fréquentes", "erreurs fréquentes" in lower),
        ("différenciation", "différenciation" in lower or "differenciation" in lower),
    ]
    for label, ok in checks:
        if not ok:
            errors.append(f"{rel}: exigence TD manquante -> {label}")
    return errors


def analyze_linked_td_quality(root: Path = ROOT, files: list[Path] | None = None) -> LinkedTDQualityResult:
    result = LinkedTDQualityResult()
    if files is not None:
        paths = {path.as_posix(): path for path in files}
    else:
        expected = expected_td_files(root)
        paths = {reference: resolution.path for reference, resolution in expected.items() if resolution.path is not None}
        for reference, resolution in expected.items():
            if resolution.ambiguous:
                candidates = ", ".join(path.as_posix() for path in resolution.candidates)
                result.errors.append(f"{reference}: support TD ambigu -> {candidates}")
            elif resolution.absent:
                result.errors.append(f"{reference}: support TD absent")
    for path in paths.values():
        result.checked_files += 1
        result.errors.extend(analyze_one_td(path))
    return result


def main() -> int:
    result = analyze_linked_td_quality()
    if result.errors:
        print("check_linked_td_quality: KO")
        for error in result.errors[:180]:
            print(f"- {error}")
        return 1
    print(f"check_linked_td_quality: PASS ({result.checked_files} TD)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
