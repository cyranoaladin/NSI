#!/usr/bin/env python3
"""Check quality of TD supports linked to operational course sheets."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re

import yaml

from scripts._qa_common import ROOT, read_frontmatter, strip_frontmatter
from scripts._operational_links import ReferenceResolution, operational_resource_links, resolve_reference

REQUIRED_FRONTMATTER = ["title", "level", "sequence_id", "document_type", "status", "official_program"]
TASK_FAMILIES = {
    "lecture/analyse": r"lecture|lire|annot(?:er|ation)|rep(?:e|é)r|identifier|analy(?:se|ser)|choisir",
    "trace/table": r"trace|table|tableau|contr(?:o|ô)le|(?:avant|apr(?:e|è)s)",
    "production/écriture": r"(?:é|e)crire|production|requ(?:e|ê)te|algorithme|code|produire",
    "justification": r"justifier|justification|expliquer|prouver|pourquoi",
    "débogage": r"d(?:e|é)bog|debug|corriger|erreur|dangereux",
    "transfert": r"transfert|variante|nouveau cas|g(?:e|é)n(?:e|é)ralisation",
}
BOUNDARY_OR_TRAP = re.compile(
    r"cas limite|r(?:e|é)sultat vide|aucun r(?:e|é)sultat|impossible|absent|inexistant|pi(?:e|è)ge|danger|sans where|sans on",
    re.I,
)
DIFFERENTIATION_OR_AIDS = re.compile(r"diff(?:e|é)renciation|aides? gradu(?:e|é)es?|aide", re.I)
EXERCISE_HEADER = re.compile(r"^###\s+Exercice\s+\d+\b.*$", re.M | re.I)


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


def exercise_blocks(body: str) -> list[str]:
    matches = list(EXERCISE_HEADER.finditer(body))
    blocks: list[str] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else body.find("## Corrigé", match.end())
        blocks.append(body[match.start() : end if end >= 0 else len(body)].lower())
    return blocks


def contract_data(root: Path, sequence_id: str) -> dict[str, object] | None:
    path = root / "03_progressions" / "supports" / "contracts" / f"{sequence_id}_contract.yml"
    if not path.is_file():
        return None
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError:
        return None
    return data if isinstance(data, dict) else None


def contract_requires_eight_exercises(data: dict[str, object]) -> bool:
    excluded_sections = {"must_not", "interdits_pedagogiques", "erreurs_frequentes"}
    for section, value in data.items():
        if section in excluded_sections:
            continue
        if section in {"nombre_exercices", "minimum_exercices", "exercices_minimum"}:
            numeric_requirement: int | None
            try:
                numeric_requirement = int(value) if isinstance(value, (int, float, str)) else None
            except (TypeError, ValueError):
                numeric_requirement = None
            if numeric_requirement is not None and numeric_requirement >= 8:
                return True
        text = "\n".join(str(item) for item in value) if isinstance(value, list) else str(value)
        if re.search(r"\b(?:au moins|minimum(?: de)?|au minimum)\s+(?:8|huit)\s+exercices?\b", text, re.I):
            return True
    return False


def has_distinct_task_families(blocks: list[str]) -> bool:
    candidates = {
        family: [index for index, block in enumerate(blocks) if re.search(pattern, block, re.I)]
        for family, pattern in TASK_FAMILIES.items()
    }
    if any(not positions for positions in candidates.values()):
        return False

    families = sorted(candidates, key=lambda family: len(candidates[family]))

    def assign(index: int, used: set[int]) -> bool:
        if index == len(families):
            return True
        return any(
            position not in used and assign(index + 1, used | {position})
            for position in candidates[families[index]]
        )

    return assign(0, set())


def has_six_task_contract_compliant_td(
    root: Path,
    sequence_id: str,
    body: str,
    exercises: int,
    corrections: int,
) -> bool:
    """Autorise 6-7 tâches seulement avec contrat, rôles et garanties complets."""
    contract = contract_data(root, sequence_id)
    if contract is None or contract_requires_eight_exercises(contract):
        return False
    if exercises not in {6, 7} or corrections < exercises:
        return False
    blocks = exercise_blocks(body)
    if len(blocks) != exercises or not has_distinct_task_families(blocks):
        return False
    lower = body.lower()
    return (
        all(marker in lower for marker in ("socle", "standard"))
        and ("approfondissement" in lower or "transfert" in lower)
        and BOUNDARY_OR_TRAP.search(body) is not None
        and DIFFERENTIATION_OR_AIDS.search(body) is not None
        and "erreurs fréquentes" in lower
    )


def analyze_one_td(path: Path, root: Path = ROOT) -> list[str]:
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
    sequence_value = metadata.get("sequence_id")
    sequence_id = sequence_value if isinstance(sequence_value, str) else ""
    compact_compliant = has_six_task_contract_compliant_td(root, sequence_id, body, exercises, corrections)
    if exercises < 8 and not compact_compliant:
        if exercises in {6, 7} and contract_data(root, sequence_id) is not None and contract_requires_eight_exercises(contract_data(root, sequence_id) or {}):
            errors.append(f"{rel}: contrat exige 8 exercices, trouvé {exercises}")
        elif exercises in {6, 7}:
            errors.append(f"{rel}: TD de {exercises} tâches non conforme au contrat ou aux garanties qualitatives")
        else:
            errors.append(f"{rel}: minimum 8 exercices requis, trouvé {exercises}")
    if corrections < exercises:
        errors.append(f"{rel}: corrigé manquant pour au moins un exercice ({corrections}/{exercises})")

    lower = body.lower()
    lecture_count = len(
        re.findall(
            r"type\s*:\s*lecture/analyse|lecture|lire|annot(?:er|ation)|analyse|analyser|identifier|rechercher|trier|comparer|reperer|repérer|choisir",
            lower,
        )
    )
    production_count = len(re.findall(r"type\s*:\s*production/(?:é|e)criture|production attendue|ecrire|écrire|produire", lower))
    checks = [
        ("lecture/analyse", lecture_count >= 2),
        ("production/écriture", production_count >= 2),
        ("cas limite", BOUNDARY_OR_TRAP.search(body) is not None),
        ("justification", "justification" in lower or "justifier" in lower),
        ("progression socle", "socle" in lower),
        ("progression standard", "standard" in lower),
        ("progression approfondissement", "approfondissement" in lower or "expert" in lower),
        ("erreurs fréquentes", "erreurs fréquentes" in lower),
        ("différenciation", DIFFERENTIATION_OR_AIDS.search(body) is not None),
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
        result.errors.extend(analyze_one_td(path, root))
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
