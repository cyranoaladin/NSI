#!/usr/bin/env python3
"""Check monthly NSI load against Tunisia 2026-2027 estimates."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "premiere": ROOT / "03_progressions/seances_premiere.md",
    "terminale": ROOT / "03_progressions/seances_terminale.md",
}
ESTIMATES = {
    "premiere": {"septembre":16.2,"octobre":9.0,"novembre":17.1,"décembre":10.4,"janvier":16.2,"février":8.1,"mars":18.5,"avril":13.6,"mai":13.0,"juin":17.8},
    "terminale": {"septembre":24.3,"octobre":13.4,"novembre":25.6,"décembre":15.7,"janvier":24.3,"février":12.2,"mars":27.8,"avril":20.5,"mai":19.5,"juin":26.7},
}


def parse_load(path: Path) -> dict[str, float]:
    data: dict[str, float] = {}
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.startswith("| ") or "---" in line or "Mois" in line:
            continue
        cells = [cell.strip().lower() for cell in line.strip("|").split("|")]
        if len(cells) < 3:
            continue
        planned = re.search(r"([0-9]+(?:[.,][0-9]+)?)\s*h", cells[2])
        if planned:
            data[cells[0]] = float(planned.group(1).replace(",", "."))
    return data


def main() -> int:
    errors: list[str] = []
    for level, path in FILES.items():
        if not path.exists():
            errors.append(f"{level}: session planning missing")
            continue
        loads = parse_load(path)
        for month, estimate in ESTIMATES[level].items():
            if month not in loads:
                errors.append(f"{level}: monthly load missing for {month}")
                continue
            if loads[month] > estimate + 0.05:
                errors.append(f"{level}: {month} overload {loads[month]:g}h > {estimate:g}h")
        if level == "premiere":
            if loads.get("février", 99) > 7.2:
                errors.append("premiere: February not lightened enough for Ramadan")
            if loads.get("mars", 99) > 17.5:
                errors.append("premiere: March not lightened enough around Ramadan/Aid")
        if level == "terminale":
            if loads.get("février", 99) > 10.5:
                errors.append("terminale: February load too high during Ramadan")
            if loads.get("mars", 99) > 25.5:
                errors.append("terminale: March load too high around Ramadan/Aid")
            if loads.get("juin", 99) > 22.0:
                errors.append("terminale: June end-of-year load excessive")
    term_text = FILES["terminale"].read_text(encoding="utf-8", errors="replace") if FILES["terminale"].exists() else ""
    if "T18 - Boyer-Moore | juin" in term_text:
        errors.append("terminale: Boyer-Moore still launched in June")
    if "sans nouveau chapitre lourd" not in term_text:
        errors.append("terminal/premiere: June no-new-heavy-chapter marker missing")
    if errors:
        print("check_monthly_load_balance: KO")
        for error in errors:
            print(f"- {error}")
        return 1
    print("check_monthly_load_balance: PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())
