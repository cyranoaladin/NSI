#!/usr/bin/env python3
"""Gate: detect known closed error classes across the entire corpus.

Each error class is a grep pattern that should NOT appear in the corpus once fixed.
The gate runs BEFORE correction to prove detection, then must be EMPTY after fixes.

Error classes:
- TCO_NON_TERMINAL: TCO/tail-call invoked for non-terminal recursive call
- LOCALSTORAGE_DOMAIN: "même domaine" used for localStorage (should be "même origine")
- GREEDY_MONTANT_3: montant=3 as greedy counter-example (too small, trivial)
- ROTATION_CONSIGNE_REPONSE: response content in wrong exercise (mots-clés)

Exit codes:
    0: no closed error class detected (clean)
    1: at least one error class detected
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUPPORTS_DIR = ROOT / "03_progressions" / "supports"


def _scan_files() -> list[Path]:
    """Return all markdown files in supports."""
    return sorted(SUPPORTS_DIR.rglob("*.md"))


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


# ─── Error class detectors ───────────────────────────────────────────────────

def check_tco_non_terminal(files: list[Path]) -> list[str]:
    """RVW-016: TCO mentioned near non-terminal recursion (addition on stack)."""
    hits: list[str] = []
    # Group files by sequence directory to detect cross-file TCO+non-terminal
    seq_dirs: dict[Path, list[Path]] = {}
    for f in files:
        seq_dirs.setdefault(f.parent, []).append(f)

    for seq_dir, seq_files in seq_dirs.items():
        combined_text = "\n".join(_read(f) for f in seq_files)
        has_tco = re.search(r"(?i)tail.?call|TCO|optimisation.*terminal", combined_text)
        has_non_terminal = re.search(r"lst\[0\]\s*\+\s*\w+\(lst\[1:\]\)", combined_text)
        if has_tco and has_non_terminal:
            # Report on the file containing the TCO mention
            for f in seq_files:
                text = _read(f)
                lines = text.splitlines()
                for i, line in enumerate(lines, 1):
                    if re.search(r"(?i)tail.?call|TCO|optimisation.*terminal", line):
                        hits.append(f"{f.relative_to(ROOT)}:{i}: TCO invoqué pour appel non terminal")
    return hits


def check_localstorage_domain(files: list[Path]) -> list[str]:
    """RVW-017: 'même domaine' instead of 'même origine' for localStorage."""
    hits: list[str] = []
    pattern = re.compile(r"(?i)local\s*storage.*même\s+domaine|même\s+domaine.*local\s*storage", re.IGNORECASE)
    for f in files:
        text = _read(f)
        if "localStorage" not in text and "localstorage" not in text.lower():
            continue
        lines = text.splitlines()
        for i, line in enumerate(lines, 1):
            if pattern.search(line):
                hits.append(f"{f.relative_to(ROOT)}:{i}: localStorage 'même domaine' au lieu de 'même origine'")
    return hits


def check_greedy_montant_3(files: list[Path]) -> list[str]:
    """Greedy counter-example with montant=3 (trivial, should be larger)."""
    hits: list[str] = []
    pattern = re.compile(r"montant\s*=\s*3\b")
    for f in files:
        text = _read(f)
        if "glouton" not in text.lower() and "greedy" not in text.lower():
            continue
        lines = text.splitlines()
        for i, line in enumerate(lines, 1):
            if pattern.search(line):
                hits.append(f"{f.relative_to(ROOT)}:{i}: contre-exemple glouton avec montant=3 (trop trivial)")
    return hits


def check_rotation_consigne_reponse(files: list[Path]) -> list[str]:
    """Detect answer-in-wrong-slot rotations by keyword patterns."""
    hits: list[str] = []
    # T09: Q1 asks schema/instance but answer says "clé primaire"
    for f in files:
        if "T09" not in f.name or "evaluation" not in f.name:
            continue
        text = _read(f)
        # Check if a Question asking about schéma/instance has answer about
        # clé primaire WITHOUT also mentioning schéma or instance in the answer.
        # The rotation pattern is: Q asks schéma/instance but A talks ONLY about
        # clé primaire, never actually answering the schéma/instance question.
        blocks = re.split(r"^#{2,3}\s+Question\s+\d+", text, flags=re.M)
        for block in blocks[1:]:  # skip pre-question text
            if not re.search(r"schéma|instance", block[:200], re.I):
                continue
            answer_match = re.search(r"Réponse attendue\s*:\s*(.+?)(?:\n-|\Z)", block, re.I | re.S)
            if not answer_match:
                continue
            answer_text = answer_match.group(1)
            has_cle_primaire = bool(re.search(r"clé primaire", answer_text, re.I))
            has_schema_instance = bool(re.search(r"schéma|instance", answer_text, re.I))
            if has_cle_primaire and not has_schema_instance:
                rel = f.relative_to(ROOT)
                hits.append(f"{rel}: rotation Q/R détectée (schéma/instance → clé primaire)")
                break
    return hits


def main() -> None:
    files = _scan_files()
    all_hits: list[str] = []

    checkers = [
        ("TCO_NON_TERMINAL", check_tco_non_terminal),
        ("LOCALSTORAGE_DOMAIN", check_localstorage_domain),
        ("GREEDY_MONTANT_3", check_greedy_montant_3),
        ("ROTATION_CONSIGNE_REPONSE", check_rotation_consigne_reponse),
    ]

    for name, checker in checkers:
        hits = checker(files)
        if hits:
            print(f"\n[{name}] {len(hits)} occurrence(s):")
            for h in hits:
                print(f"  {h}")
            all_hits.extend(hits)

    if all_hits:
        print(f"\ncheck_closed_error_classes: FAIL ({len(all_hits)} hit(s))")
        sys.exit(1)
    else:
        print("check_closed_error_classes: PASS (0 hits)")


if __name__ == "__main__":
    main()
