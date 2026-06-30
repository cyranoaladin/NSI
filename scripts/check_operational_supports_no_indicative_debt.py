#!/usr/bin/env python3
"""Block indicative debt on supports linked to operational course sheets."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from scripts._qa_common import ROOT, read_frontmatter, strip_frontmatter
from scripts._operational_links import operational_resource_links, resolve_reference

MIN_LINES = {
    "td": 80,
    "evaluation": 55,
    "tp": 80,
    "cours": 100,
    "trace": 45,
}

REQUIRED_MARKERS = {
    "td": [
        ["objectifs"],
        ["exercices"],
        ["corrigé", "corrige"],
        ["erreurs fréquentes", "erreurs frequentes"],
        ["différenciation", "differenciation"],
    ],
    "evaluation": [
        ["questions"],
        ["barème", "bareme"],
        ["corrigé", "corrige"],
        ["critères de réussite", "criteres de reussite"],
    ],
    "tp": [
        ["objectif"],
        ["consigne", "consignes"],
        ["tests"],
        ["livrable"],
        ["critères de réussite", "criteres de reussite"],
    ],
}


@dataclass
class OperationalDebtResult:
    errors: list[str] = field(default_factory=list)
    checked_files: int = 0


def resolve_resource(root: Path, reference: str) -> Path | None:
    return resolve_reference(root, reference).path


def linked_operational_supports(root: Path = ROOT) -> tuple[list[Path], list[str]]:
    supports: dict[str, Path] = {}
    errors: list[str] = []
    for resource in operational_resource_links(root):
        if resource.resolution.ambiguous:
            candidates = ", ".join(path.as_posix() for path in resource.resolution.candidates)
            errors.append(f"{resource.link.file}: support opérationnel ambigu -> {candidates}")
            continue
        path = resource.path
        if path and path.suffix == ".md":
            supports[path.as_posix()] = path
    return [supports[key] for key in sorted(supports)], errors


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
    supports, link_errors = linked_operational_supports(root)
    result.errors.extend(link_errors)
    for path in supports:
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
        for alternatives in REQUIRED_MARKERS.get(kind, []):
            if not any(marker.lower() in lower for marker in alternatives):
                result.errors.append(f"{rel}: section ou marqueur manquant -> {alternatives[0]}")
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
