#!/usr/bin/env python3
"""Génère la couverture programme NSI à partir de PREUVES réelles.

Version étendue : indexe désormais DEUX sources de preuves
  1. les séquences pilotes (preuves ancrées, `iter_declared_evidence`) ;
  2. l'arbre `03_progressions/supports/` (preuves au niveau fichier,
     `iter_support_evidence`), jusqu'ici invisible de la couverture.

L'indexation des supports est réversible (`--no-supports`) et n'invente aucune
validation : un document support `needs_review` fait remonter sa capacité en
`needs_review`, jamais en `covered`. Elle rend visible l'existant, c'est tout.

Sorties :
  - coverage.md, programme_matrix_premiere.md, programme_matrix_terminale.md
    (schéma de colonnes inchangé, pour ne rien casser en aval) ;
  - missing_capabilities.md ;
  - coverage_sources.md (NOUVEAU) : provenance par capacité (pilote / unités
    supports), pour la traçabilité et le pilotage des trous réels.
"""

from __future__ import annotations

import argparse
import re
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
from _supports_evidence import iter_support_evidence

COVERAGE = ROOT / "coverage.md"
MATRIX_PREMIERE = ROOT / "programme_matrix_premiere.md"
MATRIX_TERMINALE = ROOT / "programme_matrix_terminale.md"
MISSING = ROOT / "missing_capabilities.md"
SOURCES = ROOT / "coverage_sources.md"

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


def _unit_of(ev: Evidence) -> str:
    """Étiquette de provenance : préfixe d'unité support (P05, T18) ou 'pilote'."""
    m = re.search(r"/supports/(?:premiere|terminale)/([PT]\d{2})/", ev.file)
    if m:
        return m.group(1)
    if "/sequences/" in ev.file:
        return "pilote"
    return "autre"


def build_rows(use_supports: bool):
    program = load_program_entries()
    by_capacity: Dict[str, List[Evidence]] = defaultdict(list)

    sources = list(iter_declared_evidence())
    if use_supports:
        sources += list(iter_support_evidence())
    for item in sources:
        by_capacity[item.capacity_id].append(item)

    provenance: Dict[str, set] = defaultdict(set)
    rows: List[Dict[str, str]] = []
    for cap_id, entry in program.items():
        items = by_capacity.get(cap_id, [])
        for it in items:
            provenance[cap_id].add(_unit_of(it))
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
    return rows, provenance


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
            "| {niveau} | {rubrique} | {contenu} | {capacite} | {preuve_cours} | {preuve_td_tp} | {preuve_evaluation} | {preuve_corrige} | {statut} | {blocker} |".format(**row)
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


def write_sources(rows: List[Dict[str, str]], provenance: Dict[str, set]) -> None:
    lines = [
        "# Provenance des preuves de couverture",
        "",
        "Origine des preuves par capacité : `pilote` (séquences pilotes) ou",
        "préfixe d'unité support (P00–P14, T00–T19). Capacité sans source = absente.",
        "",
        "| niveau | capacité | statut | sources |",
        "| --- | --- | --- | --- |",
    ]
    for row in rows:
        cap_id = row["capacite"].split(" - ", 1)[0]
        srcs = ", ".join(sorted(provenance.get(cap_id, set()))) or "-"
        lines.append(f"| {row['niveau']} | {cap_id} | {row['statut']} | {srcs} |")
    SOURCES.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--no-supports", action="store_true",
                    help="désactiver l'indexation de 03_progressions/supports/ (comportement historique)")
    ap.add_argument("--print-summary", action="store_true",
                    help="afficher le résumé chiffré sur stdout")
    args = ap.parse_args()

    use_supports = not args.no_supports
    rows, provenance = build_rows(use_supports)
    write_table(COVERAGE, rows)
    write_table(MATRIX_PREMIERE, [r for r in rows if r["niveau"] == "premiere"])
    write_table(MATRIX_TERMINALE, [r for r in rows if r["niveau"] == "terminale"])
    write_missing(rows)
    write_sources(rows, provenance)

    counts: Dict[str, int] = defaultdict(int)
    for r in rows:
        counts[r["statut"]] += 1
    suffix = "avec supports" if use_supports else "pilotes seuls"
    print(f"check_program_coverage ({suffix}) : coverage.md + matrices + coverage_sources.md")
    if args.print_summary:
        print(f"  total={len(rows)} covered={counts['covered']} "
              f"needs_review={counts['needs_review']} partial={counts['partial']} "
              f"absent={counts['absent']}")


if __name__ == "__main__":
    main()
