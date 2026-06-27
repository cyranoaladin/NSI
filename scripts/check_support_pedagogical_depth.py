#!/usr/bin/env python3
"""Reject supports that have structure but not enough pedagogical substance."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re

from _qa_common import ROOT, read_frontmatter, strip_frontmatter


TARGET_DOC_TYPES = {"cours", "td", "tp", "tp_papier", "evaluation"}
CONCRETE_MARKERS = [
    "`",
    "|",
    "=>",
    "->",
    " = ",
    "[",
    "{",
    "SELECT",
    "def ",
    "class ",
]


@dataclass
class PedagogicalDepthResult:
    errors: list[str] = field(default_factory=list)
    files_checked: int = 0


def candidate_supports(root: Path = ROOT) -> list[Path]:
    base = root / "03_progressions" / "supports"
    result: list[Path] = []
    for path in sorted(base.rglob("*.md")):
        metadata = read_frontmatter(path)
        document_type = str(metadata.get("document_type", "")).strip().lower()
        name = path.name.lower()
        name_type = bool(re.search(r"_(cours|td|tp|evaluation)_", name, flags=re.I))
        name_type = name_type or bool(re.search(r"_(TD|TP)_", path.name))
        if document_type in TARGET_DOC_TYPES or name_type:
            if "corrige" not in name and "bareme" not in name:
                result.append(path)
    return result


def section_item_count(body: str, heading_pattern: str) -> int:
    match = re.search(rf"^##\s+[^\n]*(?:{heading_pattern})[^\n]*\n(.*?)(?=^##\s+|\Z)", body, flags=re.I | re.M | re.S)
    if not match:
        return 0
    block = match.group(1)
    return len(re.findall(r"^\s*(?:[-*]|\d+\.)\s+", block, flags=re.M))


def count_case_insensitive(text: str, pattern: str) -> int:
    return len(re.findall(pattern, text, flags=re.I))


def concrete_marker_count(text: str) -> int:
    count = 0
    for marker in CONCRETE_MARKERS:
        count += text.count(marker)
    count += len(re.findall(r"\b\d+(?:\.\d+)?\b", text))
    count += len(re.findall(r"[PT]-[A-Z]+-\d{2}[A-Z]?", text))
    return count


def analyze_support_file(path: Path, root: Path) -> list[str]:
    errors: list[str] = []
    rel = path.relative_to(root).as_posix()
    metadata = read_frontmatter(path)
    body = strip_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
    lower_name = path.name.lower()
    document_type = str(metadata.get("document_type", "")).strip().lower()
    capacities = re.findall(r"[PT](?:-[A-Z]+)+-\d{2}[A-Z]?", path.read_text(encoding="utf-8", errors="replace"))

    example_count = count_case_insensitive(body, r"exemple corrigé|exercice\s+\d+|question\s+\d+|cas\s+\d+")
    example_count += section_item_count(body, r"exercices intégrés|exercices")
    limit_count = count_case_insensitive(body, r"cas limite|vide|absent|invalide|doublon|exception|interblocage")
    correction_count = count_case_insensitive(body, r"corrigé|réponse attendue|résultat attendu|solution")
    frequent_error_count = count_case_insensitive(body, r"erreur fréquente|EF\d")
    frequent_error_count += section_item_count(body, r"erreurs fréquentes")
    criteria_count = count_case_insensitive(body, r"critère de réussite|critère de validation|barème|observable|contrôle")
    criteria_count += section_item_count(body, r"critères")
    marker_count = concrete_marker_count(body)

    if not capacities:
        errors.append(f"{rel}: aucune capacité officielle liée")
    if example_count < 2:
        errors.append(f"{rel}: exemples concrets insuffisants ({example_count}<2)")
    if limit_count < 2:
        errors.append(f"{rel}: cas limites insuffisants ({limit_count}<2)")
    if frequent_error_count < 2:
        errors.append(f"{rel}: erreurs fréquentes propres à la notion insuffisantes ({frequent_error_count}<2)")
    if criteria_count < 2:
        errors.append(f"{rel}: critères de réussite observables insuffisants ({criteria_count}<2)")
    if marker_count < 8:
        errors.append(f"{rel}: données, code, tables ou traces vérifiables insuffisants ({marker_count}<8)")

    if document_type in {"td", "tp", "tp_papier", "evaluation"} or any(token in lower_name for token in ["td", "tp", "evaluation"]):
        if correction_count < 2:
            errors.append(f"{rel}: corrigé vérifiable insuffisant ({correction_count}<2)")
    return errors


def analyze_support_pedagogical_depth(
    root: Path = ROOT,
    files: list[Path] | None = None,
) -> PedagogicalDepthResult:
    result = PedagogicalDepthResult()
    for path in files or candidate_supports(root):
        result.files_checked += 1
        result.errors.extend(analyze_support_file(path, root))
    return result


def main() -> int:
    result = analyze_support_pedagogical_depth()
    if result.errors:
        print("check_support_pedagogical_depth: KO")
        for error in result.errors[:220]:
            print(f"- {error}")
        return 1
    print(f"check_support_pedagogical_depth: PASS ({result.files_checked} supports)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
