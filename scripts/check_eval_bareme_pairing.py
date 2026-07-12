#!/usr/bin/env python3
"""Gate: each evaluation file must have a matching barème file (same slug/variant).

Scans 03_progressions/supports/ for evaluation_*.md files and verifies
that a corresponding bareme_*.md file exists with the same suffix.

Exit 0 if all pairs exist, exit 1 with details of unpaired evaluations.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUPPORTS = ROOT / "03_progressions" / "supports"


def main() -> int:
    evals = sorted(SUPPORTS.rglob("*_evaluation_*.md")) + sorted(SUPPORTS.rglob("*_evaluation_*.md"))
    # Deduplicate
    seen: set[Path] = set()
    unique_evals: list[Path] = []
    for e in evals:
        if e not in seen:
            seen.add(e)
            unique_evals.append(e)

    unpaired: list[str] = []
    for eval_path in unique_evals:
        name = eval_path.name
        # Extract: Pxx_evaluation_slug.md or Txx_evaluation_slug.md
        m = re.match(r"(\w+)_evaluation_(.+)\.md", name, re.I)
        if not m:
            continue
        prefix, slug = m.group(1), m.group(2)
        bareme_name = f"{prefix}_bareme_{slug}.md"
        bareme_path = eval_path.parent / bareme_name
        if not bareme_path.exists():
            # Also try case variants
            bareme_alt = eval_path.parent / f"{prefix}_Bareme_{slug}.md"
            if not bareme_alt.exists():
                rel = eval_path.relative_to(ROOT)
                unpaired.append(f"  {rel} → barème manquant: {bareme_name}")

    if unpaired:
        print(f"check_eval_bareme_pairing: FAIL ({len(unpaired)} évaluation(s) sans barème)")
        for u in unpaired:
            print(u)
        return 1

    print(f"check_eval_bareme_pairing: PASS ({len(unique_evals)} paire(s) vérifiées)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
