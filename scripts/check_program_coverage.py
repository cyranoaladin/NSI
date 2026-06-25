#!/usr/bin/env python3
"""Generate explicit evidence-based NSI programme coverage."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Dict, List

from _qa_common import (
    ROOT,
    REQUIRED_EVIDENCE,
    VALIDATED_STATUSES,
    Evidence,
    iter_declared_evidence,
    load_program_entries,
)

COVERAGE = ROOT / "coverage.md"
MATRIX_PREMIERE = ROOT / "programme_matrix_premiere.md"
MATRIX_TERMINALE = ROOT / "programme_matrix_terminale.md"
MISSING = ROOT / "missing_capabilities.md"

FORCED_STATUS = {
    "T-ALGO-02A": ("partial", "parcours en largeur présent seulement comme application, pas comme séquence évaluée complète"),
}


def evidence_label(items: List[Evidence], accepted: set[str]) -> str:
    selected = [item for item in items if item.evidence_type in accepted]
    if not selected:
        return "-"
    return ", ".join(sorted({f"{item.file}{item.anchor}" for item in selected}))


def status_and_blocker(capacity_id: str, items: List[Evidence]) -> tuple[str, str]:
    if capacity_id in FORCED_STATUS:
        return FORCED_STATUS[capacity_id]

    if not items:
        return "absent", "aucune ressource associée"

    types = {item.evidence_type for item in items}
    required_missing = []
    for expected in REQUIRED_EVIDENCE:
        if expected == "td":
            if not {"td", "exercise"}.intersection(types):
                required_missing.append("td ou exercices")
        elif expected == "tp":
            if not {"tp", "activité", "activite"}.intersection(types):
                required_missing.append("tp ou activité pratique")
        elif expected not in types:
            required_missing.append(expected)

    if required_missing:
        return "partial", "preuves manquantes: " + ", ".join(required_missing)

    if any(item.status not in VALIDATED_STATUSES for item in items):
        return "needs_review", "ressources présentes mais statuts non validants"

    return "covered", "-"


def build_rows() -> List[Dict[str, str]]:
    program = load_program_entries()
    by_capacity: Dict[str, List[Evidence]] = defaultdict(list)
    for item in iter_declared_evidence():
        by_capacity[item.capacity_id].append(item)

    rows: List[Dict[str, str]] = []
    for cap_id, entry in program.items():
        items = by_capacity.get(cap_id, [])
        status, blocker = status_and_blocker(cap_id, items)
        rows.append(
            {
                "niveau": str(entry.get("level") or entry.get("niveau")),
                "rubrique": str(entry.get("rubrique")),
                "contenu": str(entry.get("contenu")),
                "capacite": cap_id + " - " + " / ".join(entry.get("capacite_attendue") or []),
                "preuve_cours": evidence_label(items, {"cours", "trace"}),
                "preuve_td_tp": evidence_label(items, {"td", "exercise", "tp", "activité", "activite"}),
                "preuve_evaluation": evidence_label(items, {"evaluation", "qcm"}),
                "preuve_corrige": evidence_label(items, {"corrige"}),
                "statut": status,
                "blocker": blocker,
            }
        )
    return rows


def write_table(path: Path, rows: List[Dict[str, str]]) -> None:
    counts: Dict[str, int] = defaultdict(int)
    for row in rows:
        counts[row["statut"]] += 1
    lines = [
        "# Couverture du programme NSI" if path == COVERAGE else f"# {path.stem}",
        "",
        "## Résumé",
        "",
        f"- Total capacités : {len(rows)}",
        f"- covered : {counts.get('covered', 0)}",
        f"- needs_review : {counts.get('needs_review', 0)}",
        f"- partial : {counts.get('partial', 0)}",
        f"- absent : {counts.get('absent', 0)}",
        "",
        "| niveau | rubrique officielle | contenu officiel | capacité officielle | preuve cours | preuve TD/TP | preuve évaluation | preuve corrigé | statut | blocker |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            "| {niveau} | {rubrique} | {contenu} | {capacite} | {preuve_cours} | {preuve_td_tp} | {preuve_evaluation} | {preuve_corrige} | {statut} | {blocker} |".format(
                **row
            )
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_missing(rows: List[Dict[str, str]]) -> None:
    lines = ["# Capacités manquantes ou à revoir", ""]
    for row in rows:
        if row["statut"] != "covered":
            lines.append(f"- {row['niveau']} | {row['capacite']} | {row['statut']} | {row['blocker']}")
    if len(lines) == 2:
        lines.append("- Aucun item.")
    MISSING.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    rows = build_rows()
    write_table(COVERAGE, rows)
    write_table(MATRIX_PREMIERE, [row for row in rows if row["niveau"] == "premiere"])
    write_table(MATRIX_TERMINALE, [row for row in rows if row["niveau"] == "terminale"])
    write_missing(rows)
    print("check_program_coverage: generated coverage.md and programme matrices")


if __name__ == "__main__":
    main()
