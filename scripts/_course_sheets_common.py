#!/usr/bin/env python3
"""Shared helpers for course sheet QA checks."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Any

from _qa_common import ROOT, load_program_entries, read_frontmatter, strip_frontmatter

SHEETS_ROOT = ROOT / "03_progressions" / "fiches_cours"
PROGRESSION_FILES = {
    "premiere": ROOT / "03_progressions" / "progression_premiere.md",
    "terminale": ROOT / "03_progressions" / "progression_terminale.md",
}
CAPACITY_RE = re.compile(r"\b[PT]-[A-Z]+(?:-[A-Z]+)*-\d{2}[A-Z]?\b")
SEQUENCE_RE = re.compile(r"\b([PT]\d{2})\b")
SHEET_NAME_RE = re.compile(r"^([PT]\d{2})_fiche_cours_[a-z0-9_]+\.md$")

REQUIRED_SECTIONS = [
    "À savoir",
    "Méthodes",
    "Exemples corrigés",
    "Erreurs fréquentes",
    "Cas limites",
    "Mini-exercices",
    "Réponses rapides",
    "À retenir",
    "Lien avec la progression",
    "Auto-évaluation",
]

REQUIRED_FRONTMATTER = [
    "title",
    "level",
    "sequence_id",
    "document_type",
    "status",
    "version",
    "source",
    "source_creation",
    "theme",
    "notion",
    "official_program",
    "private_data",
]

DENSE_MIN_SHEETS = {
    "P01": 2,
    "P02": 2,
    "P03": 2,
    "P04": 3,
    "P08": 2,
    "T03": 3,
    "T10": 2,
}


@dataclass
class SequencePlan:
    sequence_id: str
    level: str
    capacities: set[str]


def normalize(text: str) -> str:
    text = re.sub(r"`[^`]+`", "`code`", text.lower())
    text = re.sub(r"\b\d+\b", "n", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def useful_lines(text: str) -> list[str]:
    body = strip_frontmatter(text)
    return [line.strip() for line in body.splitlines() if line.strip()]


def extract_capacities(text: str) -> set[str]:
    return set(CAPACITY_RE.findall(text))


def frontmatter_capacities(metadata: dict[str, Any]) -> set[str]:
    official = metadata.get("official_program")
    if not isinstance(official, dict):
        return set()
    raw = official.get("capacities")
    if not isinstance(raw, list):
        return set()
    capacities: set[str] = set()
    for item in raw:
        if isinstance(item, str):
            capacities.add(item)
        elif isinstance(item, dict) and item.get("id"):
            capacities.add(str(item["id"]))
    return capacities


def level_for_sequence(sequence_id: str) -> str:
    return "premiere" if sequence_id.startswith("P") else "terminale"


def parse_progression_table(path: Path, level: str) -> dict[str, SequencePlan]:
    plans: dict[str, SequencePlan] = {}
    if not path.exists():
        return plans
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 5:
            continue
        seq_match = SEQUENCE_RE.search(cells[0])
        if not seq_match:
            continue
        sequence_id = seq_match.group(1)
        capacities = extract_capacities(cells[4])
        if sequence_id not in plans:
            plans[sequence_id] = SequencePlan(sequence_id, level, set())
        plans[sequence_id].capacities.update(capacities)
    return plans


def planned_sequences(root: Path = ROOT) -> dict[str, SequencePlan]:
    progressions = {
        "premiere": root / "03_progressions" / "progression_premiere.md",
        "terminale": root / "03_progressions" / "progression_terminale.md",
    }
    plans: dict[str, SequencePlan] = {}
    for level, path in progressions.items():
        plans.update(parse_progression_table(path, level))
    return dict(sorted(plans.items()))


def sheet_files(root: Path = ROOT) -> list[Path]:
    base = root / "03_progressions" / "fiches_cours"
    if not base.exists():
        return []
    return sorted(path for path in base.rglob("*.md") if path.is_file())


def sheets_by_sequence(root: Path = ROOT) -> dict[str, list[Path]]:
    by_sequence: dict[str, list[Path]] = {}
    for path in sheet_files(root):
        match = SHEET_NAME_RE.match(path.name)
        if not match:
            continue
        by_sequence.setdefault(match.group(1), []).append(path)
    return {key: sorted(value) for key, value in sorted(by_sequence.items())}


def section_text(text: str, section: str) -> str:
    pattern = re.compile(
        rf"^##\s+{re.escape(section)}\s*$\n(.*?)(?=^##\s+|\Z)",
        flags=re.M | re.S,
    )
    match = pattern.search(text)
    return match.group(1).strip() if match else ""


def program_ids() -> set[str]:
    return set(load_program_entries())
