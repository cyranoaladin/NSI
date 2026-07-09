#!/usr/bin/env python3
"""Generateur du dossier de revue lead v3.

Lit les verdicts de substance echantillonnes et produit
docs/promotion/dossier_revue_lead_v3.md a partir des fichiers sources.

Usage :
    python -m scripts.generate_dossier_revue_lead_v3
"""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REVIEWS_DIR = ROOT / "substance_reviews" / "campaign"
OUTPUT = ROOT / "docs" / "promotion" / "dossier_revue_lead_v3.md"

# Echantillon fixe : 7 corriges + 6 frais (seed 91)
SAMPLE_CORRIGES = [
    "P-ALGO-03",
    "P-ALGO-04",
    "P-ALGO-05",
    "T-BDD-02",
    "T-BDD-01B",
    "P-IHM-03B",
    "T-LANG-04A",
]
SAMPLE_FRAIS = [
    "P-ARCH-03B",
    "T-LANG-05",
    "P-DATA-CONSTR-03A",
    "T-STRUCT-05C",
    "T-STRUCT-05B",
    "P-DATA-CONSTR-02B",
]

EXTRACT_MAX_LINES = 8


def github_slug(title: str) -> str:
    s = unicodedata.normalize("NFC", title).strip().lower().replace("`", "")
    kept = [ch for ch in s if ch.isalnum() or ch in (" ", "-", "_")]
    return "".join(kept).replace(" ", "-")


HEADER_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FRONTMATTER_RE = re.compile(r"^---\s*$")


def extract_section(md_text: str, anchor: str) -> str | None:
    slug_target = anchor.lstrip("#")
    lines = md_text.splitlines()
    # skip frontmatter
    start = 0
    if lines and FRONTMATTER_RE.match(lines[0]):
        for i in range(1, len(lines)):
            if FRONTMATTER_RE.match(lines[i]):
                start = i + 1
                break

    slug_counts: dict[str, int] = {}
    in_code = False
    section_start: int | None = None
    section_level: int = 0

    for idx in range(start, len(lines)):
        line = lines[idx]
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = HEADER_RE.match(line)
        if m:
            level = len(m.group(1))
            title = m.group(2)
            slug = github_slug(title)
            count = slug_counts.get(slug, 0)
            slug_counts[slug] = count + 1
            actual = slug if count == 0 else f"{slug}-{count}"
            if section_start is not None and level <= section_level:
                return "\n".join(lines[section_start:idx]).strip()
            if actual == slug_target:
                section_start = idx
                section_level = level
    if section_start is not None:
        return "\n".join(lines[section_start:]).strip()
    return None


def truncate_extract(text: str) -> str:
    lines = text.splitlines()
    if len(lines) > EXTRACT_MAX_LINES:
        lines = lines[:EXTRACT_MAX_LINES]
        lines[-1] = lines[-1][:80]
    else:
        for i, line in enumerate(lines):
            if len(line) > 100:
                lines[i] = line[:100]
    return "\n".join(lines)


def load_verdict(cap_id: str) -> dict[str, Any] | None:
    path = REVIEWS_DIR / f"{cap_id}_substance_review.json"
    if not path.exists():
        return None
    data: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    for cap in data.get("capacities", []):
        if cap["capacity_id"] == cap_id:
            result: dict[str, Any] = cap
            return result
    return None


def render_slot(slot_name: str, proof: dict[str, Any]) -> list[str]:
    lines: list[str] = []
    if not proof.get("present"):
        lines.append(f"### {slot_name} : absent")
        return lines
    lines.append(f"### {slot_name}")
    lines.append(f"- **Fichier** : `{proof['file']}`")
    lines.append(f"- **Ancre** : `{proof['anchor']}`")
    quote_preview = proof.get("quote", "")[:120]
    if len(proof.get("quote", "")) > 120:
        quote_preview += "..."
    lines.append(f"- **Citation** : {quote_preview}")

    # Extract from source file
    src = ROOT / proof["file"]
    if src.exists():
        md = src.read_text(encoding="utf-8", errors="replace")
        section = extract_section(md, proof["anchor"])
        if section:
            lines.append("")
            lines.append("**Extrait** :")
            lines.append("```")
            lines.append(truncate_extract(section))
            lines.append("```")
    return lines


def render_entry(idx: int, cap_id: str, tag: str) -> list[str]:
    cap = load_verdict(cap_id)
    if cap is None:
        return [f"## {idx}. {cap_id} ({tag}) — verdict introuvable", "---"]

    proofs_present = sum(
        1
        for k in ("proof_course", "proof_practice", "proof_correction")
        if cap.get(k, {}).get("present")
    )

    lines = [
        f"## {idx}. {cap_id} ({tag}) — {cap['official_label']}",
        f"- **Proofs** : {proofs_present}/3",
        "",
    ]
    for slot, key in [
        ("course", "proof_course"),
        ("practice", "proof_practice"),
        ("correction", "proof_correction"),
    ]:
        proof = cap.get(key, {})
        lines.extend(render_slot(slot, proof))
        lines.append("")

    lines.extend([
        "### Grille",
        "- [ ] Q1 Ancre correcte",
        "- [ ] Q2 Enseigne au niveau du libelle",
        "- [ ] Q3 Meme verdict",
        "- Observation : ___",
        "---",
    ])
    return lines


def count_verdicts() -> tuple[int, int, int]:
    full = 0
    partial = 0
    absent = 0
    for p in sorted(REVIEWS_DIR.glob("*_substance_review.json")):
        if p.name.startswith("_"):
            continue
        data = json.loads(p.read_text(encoding="utf-8"))
        for cap in data.get("capacities", []):
            n = sum(
                1
                for k in ("proof_course", "proof_practice", "proof_correction")
                if cap.get(k, {}).get("present")
            )
            if n == 3:
                full += 1
            elif n > 0:
                partial += 1
            else:
                absent += 1
    return full, partial, absent


def main() -> None:
    full, partial, absent = count_verdicts()
    n_corriges = len(SAMPLE_CORRIGES)
    n_frais = len(SAMPLE_FRAIS)
    total = n_corriges + n_frais

    out: list[str] = [
        "# Dossier de revue lead v3 — Post-REM3 (regenere)",
        "",
        "## Resume executif",
        "",
        f"- **Coverage** : {full}/{partial}/{absent} (source unique : verdicts au moment de la generation)",
        "- **Partial** : T-LANG-04A (1/3)",
        f"- **Echantillon** : {total} verdicts ({n_corriges} corriges + {n_frais} frais seed 91)",
        "",
        "---",
        "",
    ]

    idx = 1
    for cap_id in SAMPLE_CORRIGES:
        out.extend(render_entry(idx, cap_id, "CORRIGE"))
        out.append("")
        idx += 1
    for cap_id in SAMPLE_FRAIS:
        out.extend(render_entry(idx, cap_id, "FRAIS"))
        out.append("")
        idx += 1

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(out), encoding="utf-8")
    print(f"OK  dossier_revue_lead_v3.md regenere ({total} entrees)")


if __name__ == "__main__":
    main()
