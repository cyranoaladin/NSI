#!/usr/bin/env python3
"""Generate qa_report.md from current manifest, coverage and Drive inventory."""
from __future__ import annotations

import csv
import subprocess
import sys
from collections import Counter
from pathlib import Path

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


def command_status(command: list[str]) -> tuple[int, str]:
    result = subprocess.run(command, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return result.returncode, result.stdout.strip().splitlines()[-8:]


def main() -> int:
    total, statuses, sources, publishable = count_manifest()
    cov = coverage_counts()
    release_code, release_tail = command_status(["make", "--no-print-directory", "release-audit"])
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
        "",
        "## Décisions",
        "",
        "- Statut publication : NON.",
        "- Statut covered : 0.",
        "- Statut published : 0.",
        "- Statut validated_* : 0.",
    ]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("generate_qa_report: wrote qa_report.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
