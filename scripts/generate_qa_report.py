#!/usr/bin/env python3
"""Generate qa_report.md from current manifest, coverage and Drive inventory."""
from __future__ import annotations

import csv
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

from _course_sheets_common import compute_sheet_readiness, course_sheet_links, frontmatter_capacities, planned_sequences, read_frontmatter, resource_exists, sheets_by_sequence

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifest.csv"
COVERAGE = ROOT / "coverage.md"
DRIVE_INVENTORY = ROOT / "drive_inventory.csv"
REPORT = ROOT / "qa_report.md"


def count_manifest() -> tuple[int, Counter[str], Counter[str], int]:
    statuses: Counter[str] = Counter()
    sources: Counter[str] = Counter()
    publishable = 0
    total = 0
    with MANIFEST.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            total += 1
            statuses[row.get("statut", "")] += 1
            sources[row.get("source", "")] += 1
            if row.get("publishable") == "oui":
                publishable += 1
    return total, statuses, sources, publishable


def coverage_counts() -> dict[str, int]:
    counts: dict[str, int] = {}
    if not COVERAGE.exists():
        return counts
    for line in COVERAGE.read_text(encoding="utf-8").splitlines():
        if line.startswith("- ") and " : " in line:
            key, value = line[2:].split(" : ", 1)
            if value.strip().isdigit():
                counts[key.strip()] = int(value.strip())
    return counts


def drive_rows() -> int:
    if not DRIVE_INVENTORY.exists():
        return 0
    with DRIVE_INVENTORY.open(encoding="utf-8", newline="") as handle:
        return sum(1 for _ in csv.DictReader(handle))


def command_status(command: list[str]) -> tuple[int, list[str]]:
    result = subprocess.run(command, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    lines: list[str] = []
    for line in result.stdout.strip().splitlines():
        if line.startswith("make[") and "]: ***" in line:
            line = "make: ***" + line.split("]: ***", 1)[1]
        line = re.sub(r"Makefile:\d+: release-audit", "Makefile:release-audit", line)
        if "Entering directory" in line or "Leaving directory" in line:
            continue
        lines.append(line)
    return result.returncode, lines[-8:]


def indicative_gate_rows() -> list[tuple[str, str, str, str]]:
    rows: list[tuple[str, str, str, str]] = []
    for script in ["scripts/check_required_sections.py", "scripts/check_document_depth.py"]:
        code, tail = command_status([sys.executable, script])
        if code == 0:
            continue
        detail = "; ".join(line.removeprefix("- ").strip() for line in tail if line.strip())
        rows.append((
            script,
            detail or "échec indicatif observé",
            "Dette pédagogique connue ; reste non bloquant uniquement pour le prototype global.",
            "2026-07-15",
        ))
    return rows


def course_sheet_stats() -> dict[str, object]:
    plans = planned_sequences(ROOT)
    by_sequence = sheets_by_sequence(ROOT)
    sheet_count = sum(len(paths) for paths in by_sequence.values())
    missing_sequences = [sequence for sequence in plans if not by_sequence.get(sequence)]
    missing_capacities: list[str] = []
    readiness = Counter()
    existing_links = 0
    registered_links = 0
    for sequence, plan in plans.items():
        declared: set[str] = set()
        for sheet in by_sequence.get(sequence, []):
            declared.update(frontmatter_capacities(read_frontmatter(sheet)))
            links = course_sheet_links(sheet)
            readiness[compute_sheet_readiness(ROOT, links)] += 1
            for link in links:
                if link.is_resource and resource_exists(ROOT, link.file):
                    existing_links += 1
                elif link.is_resource:
                    registered_links += 1
        for capacity in sorted(plan.capacities):
            if capacity not in declared:
                missing_capacities.append(f"{sequence}:{capacity}")
    return {
        "expected": len(plans),
        "created": sheet_count,
        "missing_sequences": missing_sequences,
        "missing_capacities": missing_capacities,
        "readiness": readiness,
        "existing_links": existing_links,
        "registered_links": registered_links,
    }


def main() -> int:
    total, statuses, sources, publishable = count_manifest()
    cov = coverage_counts()
    release_code, release_tail = command_status(["make", "--no-print-directory", "release-audit"])
    indicative_rows = indicative_gate_rows()
    sheet_stats = course_sheet_stats()
    lines = [
        "# QA Report",
        "",
        "## Résumé",
        "",
        "- Statut global : NON PUBLIABLE",
        f"- Ressources inventoriées : {total}",
        f"- Ressources needs_review : {statuses.get('needs_review', 0)}",
        f"- Ressources publiables : {publishable}",
        f"- Source generated : {sources.get('generated', 0)}",
        f"- Source drive : {sources.get('drive', 0)}",
        f"- Lignes drive_inventory.csv : {drive_rows()}",
        f"- Couverture covered : {cov.get('covered', 0)}",
        f"- Couverture needs_review : {cov.get('needs_review', 0)}",
        f"- Couverture partial : {cov.get('partial', 0)}",
        f"- Couverture absent : {cov.get('absent', 0)}",
        "- Archive pédagogique à transmettre : dist/source_clean.tar.gz",
        "- Archive globale contenant .git : interdite comme livraison principale",
        "- L’archive principale de livraison est dist/source_clean.tar.gz. Toute archive contenant .git/ est interdite comme livraison pédagogique.",
        "- make audit : PASS prototype uniquement si exécuté après génération de ce rapport",
        f"- make --no-print-directory release-audit : {'KO attendu' if release_code != 0 else 'PASS inattendu'}",
        "- Décision : ne pas générer de nouvelles séquences",
        "",
        "## Commandes de référence",
        "",
        "```bash",
        "make audit",
        "make package-audit",
        "make --no-print-directory release-audit",
        "```",
        "",
        "## Dernier release-audit observé",
        "",
        "```text",
        *release_tail,
        "```",
        "",
        "## Bloquants restants",
        "",
        "- Ressources Drive référencées mais non intégrées localement.",
        "- Toutes les ressources restent en revue ou non publiables.",
        "- Aucune capacité n'est covered.",
        "- Documents professeurs encore en needs_review.",
        "- Revue pédagogique et scientifique humaine absente.",
        "- Les séances hors première tranche restent théoriques et non prêtes.",
        "",
        "## Fiches de cours",
        "",
        f"- Fiches attendues : {sheet_stats['expected']} séquences avec au moins une fiche.",
        f"- Fiches créées : {sheet_stats['created']}",
        "- Séquences sans fiche : "
        + (", ".join(sheet_stats["missing_sequences"]) if sheet_stats["missing_sequences"] else "0"),
        "- Capacités sans fiche : "
        + (", ".join(sheet_stats["missing_capacities"]) if sheet_stats["missing_capacities"] else "0"),
        f"- Fiches théoriques : {sheet_stats['readiness'].get('theoretical', 0)}",
        f"- Fiches liées : {sheet_stats['readiness'].get('linked', 0)}",
        f"- Fiches opérationnelles : {sheet_stats['readiness'].get('operational', 0)}",
        f"- Liens vers supports existants : {sheet_stats['existing_links']}",
        f"- Liens vers supports inscrits au registre : {sheet_stats['registered_links']}",
        "- Statut : needs_review",
        "- Effet couverture : aucun ; les fiches ne rendent aucune capacité covered.",
        "",
        "## Gates indicatifs encore en échec",
        "",
        "| Fichier concerné | Erreur | Décision | Date cible de correction |",
        "|---|---|---|---|",
        *(
            [
                f"| `{script}` | {detail.replace('|', '/')} | {decision} | {date} |"
                for script, detail, decision, date in indicative_rows
            ]
            or ["| Aucun échec indicatif observé pendant cette génération. | - | - | - |"]
        ),
        "",
        "## Décisions",
        "",
        "- Statut publication : NON.",
        "- Statut covered : 0.",
        "- Statut published : 0.",
        "- Statut validated_* : 0.",
        "- Archive pédagogique : dist/source_clean.tar.gz.",
        "- Archive globale contenant .git : interdite comme livraison principale.",
    ]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("generate_qa_report: wrote qa_report.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
