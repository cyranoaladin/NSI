#!/usr/bin/env python3
"""Check that annual progressions have operational session-level planning."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = {
    "premiere": (ROOT / "03_progressions/seances_premiere.md", "P", 15),
    "terminale": (ROOT / "03_progressions/seances_terminale.md", "T", 20),
}
REQUIRED = ["Séance", "Durée", "Période", "Objectif", "Activité d’entrée", "Cours / trace", "TD ou TP", "Différenciation", "Document utilisé", "Livrable", "Devoir maison ou préparation", "Évaluation ou non", "Remédiation prévue"]


def main() -> int:
    errors: list[str] = []
    for level, (path, prefix, count) in CONFIG.items():
        if not path.exists():
            errors.append(f"{level}: missing {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for seq in [f"{prefix}{index:02d}" for index in range(count)]:
            if f"### {seq}" not in text:
                errors.append(f"{level}: missing session block for {seq}")
        for marker in REQUIRED:
            if marker not in text:
                errors.append(f"{level}: missing required session field {marker}")
        if text.count("#### Séance") < count * 2:
            errors.append(f"{level}: not enough session entries")
    if errors:
        print("check_session_level_planning: KO")
        for error in errors:
            print(f"- {error}")
        return 1
    print("check_session_level_planning: PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())
