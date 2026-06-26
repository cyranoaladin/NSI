#!/usr/bin/env python3
"""Blocking quality gate for the first usable batch P00-P02 and T00-T02."""

from __future__ import annotations

from dataclasses import dataclass, field
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIRST_BATCH_PREFIXES = ["P00", "P01", "P02", "T00", "T01", "T02"]
REQUIRED_KINDS = [
    "cours",
    "trace",
    "td",
    "tp",
    "corrige",
    "evaluation",
    "bareme",
    "remediation",
    "version_amenagee",
]
REQUIRED_MARKERS = [
    "Objectifs",
    "Capacités officielles",
    "Exemple",
    "Exercices",
    "Corrigé",
    "Erreurs fréquentes",
    "Remédiation",
    "Différenciation",
]
CAPACITY_RE = re.compile(r"\b[PT]-[A-Z]+(?:-[A-Z]+)*-\d{2}[A-Z]?\b")


@dataclass
class FirstBatchResult:
    errors: list[str] = field(default_factory=list)
    checked_files: int = 0


def find_kind_file(root: Path, prefix: str, kind: str) -> Path | None:
    pattern = f"{prefix}_{kind}_*.md"
    matches = sorted(root.rglob(pattern))
    return matches[0] if matches else None


def useful_lines(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.strip()]


def analyze_file(path: Path, prefix: str) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = useful_lines(text)
    if len(lines) < 25:
        errors.append(f"{path}: profondeur insuffisante ({len(lines)} lignes utiles, minimum 25)")
    if "status: \"needs_review\"" not in text and "status: needs_review" not in text:
        errors.append(f"{path}: statut attendu needs_review")
    for marker in REQUIRED_MARKERS:
        if marker.lower() not in text.lower():
            errors.append(f"{path}: marqueur manquant -> {marker}")
    if not CAPACITY_RE.search(text):
        errors.append(f"{path}: aucune capacité officielle atomique")
    if prefix not in path.name:
        errors.append(f"{path}: préfixe de tranche absent du nom")
    return errors


def analyze_first_batch(root: Path = ROOT) -> FirstBatchResult:
    result = FirstBatchResult()
    for prefix in FIRST_BATCH_PREFIXES:
        for kind in REQUIRED_KINDS:
            path = find_kind_file(root, prefix, kind)
            if path is None:
                result.errors.append(f"{prefix}: support {kind} absent")
                continue
            result.checked_files += 1
            result.errors.extend(analyze_file(path, prefix))
    return result


def main() -> int:
    result = analyze_first_batch()
    if result.errors:
        print("check_first_batch_document_quality: KO")
        for error in result.errors[:120]:
            print(f"- {error}")
        return 1
    print(f"check_first_batch_document_quality: PASS ({result.checked_files} fichiers)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
