#!/usr/bin/env python3
"""Ensure every absent programme capacity has an actionable remediation row."""

from __future__ import annotations

from pathlib import Path

from _qa_common import ROOT, print_result


PLAN = ROOT / "coverage_gap_action_plan.md"
REQUIRED_COLUMNS = [
    "capacity_id",
    "niveau",
    "rubrique",
    "contenu officiel",
    "capacité officielle",
    "statut actuel",
    "diagnostic",
    "séquence cible",
    "ressources existantes possibles",
    "ressources à créer ou corriger",
    "contrat à enrichir",
    "priorité",
    "action suivante",
]


def absent_from_coverage(path: Path) -> set[str]:
    ids: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        if "| absent |" not in line:
            continue
        cols = [col.strip() for col in line.strip().strip("|").split("|")]
        if len(cols) >= 4:
            ids.add(cols[3].split(" - ", 1)[0].strip())
    return ids


def parse_plan(path: Path) -> tuple[list[str], dict[str, dict[str, str]]]:
    header: list[str] = []
    rows: dict[str, dict[str, str]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| "):
            continue
        cols = [col.strip() for col in line.strip().strip("|").split("|")]
        if cols == REQUIRED_COLUMNS:
            header = cols
            continue
        if not header or cols[0] == "---" or set(cols) == {"---"}:
            continue
        if len(cols) != len(header):
            continue
        row = dict(zip(header, cols))
        rows[row["capacity_id"]] = row
    return header, rows


def main() -> None:
    errors: list[str] = []
    if not PLAN.exists():
        print_result("check_coverage_gap_action_plan", ["coverage_gap_action_plan.md absent"])
    header, rows = parse_plan(PLAN)
    if header != REQUIRED_COLUMNS:
        errors.append("colonnes du plan absentes ou non conformes")
    for capacity_id in sorted(absent_from_coverage(ROOT / "coverage.md")):
        row = rows.get(capacity_id)
        if row is None:
            errors.append(f"{capacity_id}: aucune ligne d'action")
            continue
        for key in REQUIRED_COLUMNS:
            if not row.get(key) or row[key] == "-":
                errors.append(f"{capacity_id}: colonne vide -> {key}")
        if row.get("statut actuel") != "absent":
            errors.append(f"{capacity_id}: statut actuel doit rester absent")
        if row.get("action suivante", "").lower() in {"à définir", "todo", "tbd"}:
            errors.append(f"{capacity_id}: action suivante non actionnable")
    print_result("check_coverage_gap_action_plan", errors)


if __name__ == "__main__":
    main()
