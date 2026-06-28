#!/usr/bin/env python3
"""Orchestrateur du juge de substance : assemble le message utilisateur à partir
d'une unité du dépôt, appelle le modèle juge, écrit le verdict JSON, puis laisse
check_substance_anchors.py faire le veto mécanique.

Ce fichier est un squelette opérationnel : la fonction `call_judge` est isolée
pour brancher l'API Anthropic (ou un autre fournisseur) sans toucher au reste.
La construction du prompt (table des ancres + texte intégral) est complète et ne
dépend d'aucune API : elle est testable hors-ligne avec --dry-run.

Usage :
    # prépare le prompt seulement (aucun appel modèle) :
    python run_substance_judge.py --unit s01_representation_donnees \
        --level premiere --repo-root /chemin/depot --dry-run

    # boucle complète (nécessite ANTHROPIC_API_KEY) :
    python run_substance_judge.py --unit P05 --level premiere \
        --repo-root /chemin/depot --out P05/_substance_review.json
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from check_substance_anchors import parse_sections, load_official_labels

# Documents soumis au juge, par ordre de pertinence pédagogique.
# Pour le modèle « séquences » et le modèle « supports », on tente plusieurs noms.
CANDIDATE_DOCS = [
    "cours_eleve.md", "cours.md", "trace_ecrite.md", "trace.md",
    "td.md", "tp.md", "corrige.md",
]


def find_unit_dir(repo_root: Path, unit: str, level: str) -> Path:
    candidates = [
        repo_root / level / "sequences" / unit,
        repo_root / "03_progressions" / "supports" / level / unit,
    ]
    for c in candidates:
        if c.is_dir():
            return c
    raise SystemExit(f"unité introuvable : {unit} (niveau {level})")


def collect_docs(unit_dir: Path) -> list[Path]:
    found: list[Path] = []
    # noms canoniques d'abord
    for name in CANDIDATE_DOCS:
        p = unit_dir / name
        if p.exists():
            found.append(p)
    # puis les fichiers préfixés (modèle supports : P05_cours_*.md, P05_td_*.md…)
    for p in sorted(unit_dir.glob("*.md")):
        if p not in found and any(k in p.name.lower()
                                  for k in ("cours", "trace", "_td", "_tp", "corrige")):
            found.append(p)
    return found


def load_contract(repo_root: Path, unit: str) -> str:
    p = repo_root / "03_progressions" / "supports" / "contracts" / f"{unit}_contract.yml"
    return p.read_text(encoding="utf-8") if p.exists() else "(aucun contrat trouvé)"


def build_user_message(repo_root: Path, unit: str, level: str,
                       capacity_ids: list[str]) -> str:
    official = load_official_labels(repo_root)
    unit_dir = find_unit_dir(repo_root, unit, level)
    docs = collect_docs(unit_dir)

    out: list[str] = [f"UNITÉ À JUGER : {unit} (niveau : {level})", ""]
    out.append("## Capacités officielles visées")
    for cid in capacity_ids:
        out.append(f"- `{cid}` — {official.get(cid, '(intitulé absent du YAML)')}")
    out.append("")
    out.append("## Contrat de l'unité")
    out.append("```yaml")
    out.append(load_contract(repo_root, unit))
    out.append("```")
    out.append("")
    out.append("## Ancres disponibles (tu ne peux citer que celles-ci)")
    for d in docs:
        rel = d.relative_to(repo_root)
        out.append(f"### {rel}")
        for slug, sec in parse_sections(d.read_text(encoding="utf-8")).items():
            out.append(f"- `#{slug}`  ← « {sec.title} »")
        out.append("")
    out.append("## Texte intégral des documents")
    for d in docs:
        rel = d.relative_to(repo_root)
        out.append(f"================ FICHIER : {rel} ================")
        out.append(d.read_text(encoding="utf-8"))
        out.append("")
    out.append("CONSIGNE : une fiche de substance par capacité. Cite mot pour "
               "mot. Choisis needs_content au moindre doute. Réponds uniquement "
               "par le JSON conforme au schéma.")
    return "\n".join(out)


def call_judge(system_prompt: str, user_message: str, model: str) -> dict:
    """Appel du modèle juge. À brancher sur l'API Anthropic.

    Exemple (décommenter et installer anthropic) :

        from anthropic import Anthropic
        client = Anthropic()
        resp = client.messages.create(
            model=model, max_tokens=4000,
            system=system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )
        raw = "".join(b.text for b in resp.content if b.type == "text")
        return json.loads(raw)
    """
    raise NotImplementedError(
        "Brancher call_judge sur l'API. Utiliser --dry-run pour le prompt seul.")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--unit", required=True)
    ap.add_argument("--level", required=True, choices=["premiere", "terminale"])
    ap.add_argument("--repo-root", type=Path, default=Path("."))
    ap.add_argument("--capacities", nargs="*", default=None,
                    help="ids de capacités ; par défaut lues dans le contrat")
    ap.add_argument("--model", default="claude-opus-4-8")
    ap.add_argument("--out", type=Path, default=None)
    ap.add_argument("--dry-run", action="store_true",
                    help="écrit le prompt sur stdout sans appeler le modèle")
    args = ap.parse_args()

    repo = args.repo_root.resolve()
    caps = args.capacities
    if not caps:
        contract = load_contract(repo, args.unit)
        caps = [ln.split("-", 1)[1].strip()
                for ln in contract.splitlines()
                if ln.strip().startswith("-") and "-" in ln
                and any(ln.strip().lstrip("- ").startswith(p) for p in ("P-", "T-"))]
    if not caps:
        return _err("aucune capacité fournie ni trouvée dans le contrat")

    sys_path = Path(__file__).parent / "prompts" / "substance_judge.system.md"
    system_prompt = sys_path.read_text(encoding="utf-8")
    user_message = build_user_message(repo, args.unit, args.level, caps)

    if args.dry_run:
        print(user_message)
        return 0

    verdict = call_judge(system_prompt, user_message, args.model)
    out = args.out or (find_unit_dir(repo, args.unit, args.level)
                       / "_substance_review.json")
    out.write_text(json.dumps(verdict, ensure_ascii=False, indent=2),
                   encoding="utf-8")
    print(f"verdict écrit : {out}")
    print("→ lancer maintenant : python check_substance_anchors.py "
          f"{out} --repo-root {repo}")
    return 0


def _err(msg: str) -> int:
    print(f"ERREUR : {msg}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
