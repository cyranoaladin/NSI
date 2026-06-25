#!/usr/bin/env python3
"""Release Drive check: fails unless Drive resources are locally integrated."""

from __future__ import annotations

from typing import List
import csv

from _qa_common import ROOT, print_result


def main() -> None:
    errors: List[str] = []
    inventory = ROOT / "drive_inventory.csv"
    if not inventory.exists():
        errors.append("drive_inventory.csv absent")
        print_result("check_drive_mapping_release", errors)
        return

    with inventory.open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row.get("drive_url") != "BLOCKER"]

    if not rows:
        errors.append("drive = 0: aucune ressource Drive référencée")

    not_integrated = [
        row.get("file_name", "NA")
        for row in rows
        if row.get("local_copy") in {"", "NA", "NA_REMOTE_NOT_DOWNLOADED"}
    ]
    if not_integrated:
        errors.append(
            "ressources Drive référencées mais non intégrées localement: "
            + ", ".join(not_integrated[:20])
        )

    print_result("check_drive_mapping_release", errors)


if __name__ == "__main__":
    main()
