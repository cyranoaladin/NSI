#!/usr/bin/env python3
"""Check Drive inventory artifacts and explicit blocker when Drive is unavailable."""

from __future__ import annotations

from typing import List
import csv

import yaml

from _qa_common import ROOT, print_result


def main() -> None:
    errors: List[str] = []
    sources = ROOT / "drive_sources.yml"
    inventory = ROOT / "drive_inventory.csv"
    mapping = ROOT / "drive_mapping.md"

    for path in [sources, inventory, mapping]:
        if not path.exists():
            errors.append(f"{path.name} absent")

    if sources.exists():
        data = yaml.safe_load(sources.read_text(encoding="utf-8")) or {}
        if data.get("status") == "blocked":
            blocker = str(data.get("blocker") or "")
            action = str(data.get("action_necessaire") or "")
            if "BLOCKER: accès Drive impossible" not in blocker:
                errors.append("drive_sources.yml: blocker Drive explicite absent")
            if "export zip/tar" not in action and "monter le Drive" not in action:
                errors.append("drive_sources.yml: action nécessaire imprécise")
        elif not data.get("ressources"):
            errors.append("drive_sources.yml: aucune ressource Drive et aucun blocker")

    if inventory.exists():
        with inventory.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        if not rows:
            errors.append("drive_inventory.csv: inventaire vide sans blocker")
        elif rows[0].get("drive_url") == "BLOCKER":
            if "accès Drive impossible" not in rows[0].get("raison", ""):
                errors.append("drive_inventory.csv: ligne blocker insuffisante")

    if mapping.exists():
        text = mapping.read_text(encoding="utf-8", errors="replace")
        if "BLOCKER: accès Drive impossible" not in text:
            errors.append("drive_mapping.md: blocker explicite absent")

    print_result("check_drive_mapping", errors)


if __name__ == "__main__":
    main()
