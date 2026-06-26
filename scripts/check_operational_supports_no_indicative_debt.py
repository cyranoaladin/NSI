#!/usr/bin/env python3
"""Block indicative debt on supports linked to operational course sheets."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from _qa_common import ROOT, read_frontmatter, strip_frontmatter
from _course_sheets_common import course_sheet_links, resource_exists, sheet_files

MIN_LINES = {
    "td": 80,
    "evaluation": 55,
    "tp": 80,
    "cours": 100,
    "trace": 45,
}

REQUIRED_MARKERS = {
    "td": ["Objectifs", "Exercices", "Corrigé", "Erreurs fréquentes", "Différenciation"],
    "evaluation": ["Durée", "Matériel autorisé", "Questions", "Barème", "Corrigé", "Critères de réussite"],
    "tp": ["Objectif", "Consignes", "Tests", "Livrable", "Critères de réussite"],
}
TARGET_PREFIXES = {f"P{index:02d}" for index in range(10, 15)} | {f"T{index:02d}" for index in range(10, 20)}


@dataclass
class OperationalDebtResult:
    errors: list[str] = field(default_factory=list)
    checked_files: int = 0


def resolve_resource(root: Path, reference: str) -> Path | None:
    candidate = root / reference
    if candidate.exists():
        return candidate
    if "/" in reference:
        return None
    matches = sorted(root.rglob(reference))
    return matches[0] if matches else None


def linked_operational_supports(root: Path = ROOT) -> list[Path]:
    supports: dict[str, Path] = {}
    for sheet in sheet_files(root):
        metadata = read_frontmatter(sheet)
        if str(metadata.get("readiness") or "").strip() != "operational":
            continue
        for link in course_sheet_links(sheet):
            if link.is_session or not link.is_resource:
                continue
            if not resource_exists(root, link.file):
                continue
            path = resolve_resource(root, link.file)
            if path and path.suffix == ".md":
                if path.name[:3] not in TARGET_PREFIXES:
                    continue
                supports[path.as_posix()] = path
    return [supports[key] for key in sorted(supports)]


def infer_kind(path: Path, metadata: dict[str, object]) -> str:
    kind = str(metadata.get("document_type") or "").strip().lower()
    if kind:
        return kind
    name = path.name.lower()
    if "_td_" in name:
        return "td"
    if "_evaluation_" in name:
        return "evaluation"
    if "_tp_" in name:
        return "tp"
    return "support"


def analyze_operational_supports_no_indicative_debt(root: Path = ROOT) -> OperationalDebtResult:
    result = OperationalDebtResult()
    for path in linked_operational_supports(root):
        result.checked_files += 1
        text = path.read_text(encoding="utf-8", errors="replace")
        body = strip_frontmatter(text)
        metadata = read_frontmatter(path)
        kind = infer_kind(path, metadata)
        rel = path.relative_to(root) if path.is_relative_to(root) else path
        useful = [line for line in body.splitlines() if line.strip()]
        minimum = MIN_LINES.get(kind, 50)
        if len(useful) < minimum:
            result.errors.append(f"{rel}: profondeur insuffisante ({len(useful)} lignes utiles, minimum {minimum})")
        if not text.lstrip().startswith("---"):
            result.errors.append(f"{rel}: frontmatter absent")
        if "\n# " not in "\n" + text:
            result.errors.append(f"{rel}: titre niveau 1 absent")
        if "\n## " not in text:
            result.errors.append(f"{rel}: sections niveau 2 absentes")
        lower = body.lower()
        for marker in REQUIRED_MARKERS.get(kind, []):
            if marker.lower() not in lower:
                result.errors.append(f"{rel}: section ou marqueur manquant -> {marker}")
    return result


def main() -> int:
    result = analyze_operational_supports_no_indicative_debt()
    if result.errors:
        print("check_operational_supports_no_indicative_debt: KO")
        for error in result.errors[:180]:
            print(f"- {error}")
        return 1
    print(f"check_operational_supports_no_indicative_debt: PASS ({result.checked_files} supports)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
