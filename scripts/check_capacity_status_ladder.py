#!/usr/bin/env python3
"""Separate documented/practiced/assessed from human-reviewed and covered."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import csv
import re

from _qa_common import ROOT
from check_official_program_capacity_coverage_matrix import load_official_capacities


CAPACITY_RE = re.compile(r"\b[PT](?:-[A-Z]+)+-\d{2}[A-Z]?\b")
VALIDATED_RE = re.compile(r"validated_|published|covered", re.I)


@dataclass
class CapacityLadderResult:
    rows: dict[str, dict[str, str]] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)


def docs(root: Path) -> list[Path]:
    return sorted((root / "03_progressions").rglob("*.md"))


def contains_capacity(paths: list[Path], capacity_id: str) -> list[Path]:
    return [path for path in paths if capacity_id in path.read_text(encoding="utf-8", errors="replace")]


def manifest_status_errors(root: Path) -> list[str]:
    manifest = root / "manifest.csv"
    if not manifest.exists():
        return []
    errors: list[str] = []
    with manifest.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            status = " ".join(str(row.get(key, "")) for key in ("statut", "status", "coverage", "publication"))
            if VALIDATED_RE.search(status):
                errors.append(f"statut interdit dans manifest.csv: {row.get('path') or row.get('fichier') or row}")
    return errors


def analyze_capacity_status_ladder(root: Path = ROOT) -> CapacityLadderResult:
    result = CapacityLadderResult()
    all_docs = docs(root)
    sheet_or_course = [path for path in all_docs if "_fiche_cours_" in path.name or "_cours_" in path.name]
    practice = [path for path in all_docs if re.search(r"_(?:TD|td|TP|tp)_", path.name)]
    assessments = [path for path in all_docs if "evaluation" in path.name.lower()]

    for entry in load_official_capacities(root):
        capacity_id = entry["id"]
        documented = bool(contains_capacity(sheet_or_course, capacity_id))
        practiced = bool(contains_capacity(practice, capacity_id))
        assessed = bool(contains_capacity(assessments, capacity_id))
        row = {
            "niveau": entry["niveau"],
            "thème officiel": entry["theme"],
            "documented": "oui" if documented else "non",
            "practiced": "oui" if practiced else "non",
            "assessed": "oui" if assessed else "non",
            "reviewed_pedagogy": "non",
            "reviewed_science": "non",
            "covered": "non",
        }
        result.rows[capacity_id] = row
        if not documented:
            result.errors.append(f"{capacity_id}: documented=non")

    result.errors.extend(manifest_status_errors(root))
    return result


def main() -> int:
    result = analyze_capacity_status_ladder()
    print("| capacité | documented | practiced | assessed | reviewed_pedagogy | reviewed_science | covered |")
    print("|---|---|---|---|---|---|---|")
    for capacity_id, row in sorted(result.rows.items()):
        print(
            "| "
            + " | ".join(
                [
                    capacity_id,
                    row["documented"],
                    row["practiced"],
                    row["assessed"],
                    row["reviewed_pedagogy"],
                    row["reviewed_science"],
                    row["covered"],
                ]
            )
            + " |"
        )
    if result.errors:
        print("check_capacity_status_ladder: KO")
        for error in result.errors[:240]:
            print(f"- {error}")
        return 1
    print(f"check_capacity_status_ladder: PASS ({len(result.rows)} capacités, covered=non)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
