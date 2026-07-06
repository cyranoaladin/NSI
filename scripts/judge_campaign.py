#!/usr/bin/env python3
"""Judge campaign: evaluate capacity coverage using Anthropic Messages API.

Synchronous sequential calls with two-tier prompt caching:
  - Tier 1 (system): static protocol + schema + 4 gold examples, TTL 1h
  - Tier 2 (user prefix): sequence context (all evidence files), TTL 5min
  - Variable: capacity prompt (never cached)

Execution is sorted by sequence to maximize tier-2 cache hits.

V0d — Coverage derivation (ref: scripts/check_program_coverage.py L40-62):
  The coverage engine does NOT read judge verdicts. covered=0 until the lead
  promotes file statuses to validated_pedagogy.

J2d — Validate-before-save: each verdict passes the hardened checker BEFORE
  writing. If invalid, ONE retry with error feedback. If still invalid, the
  verdict is saved as needs_content with the error noted.

SECRETS: ANTHROPIC_API_KEY read from environment or .env — never committed.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

import yaml  # noqa: E402

from scripts._qa_common import (  # noqa: E402
    ROOT,
    SUPPORTS_DIR,
    read_frontmatter,
)

PROGRAMME_FILE = ROOT / "00_programmes_officiels" / "programme_nsi_2019.yaml"
OUTPUT_DIR = ROOT / "substance_reviews" / "campaign"
MODEL = "claude-sonnet-4-6"

# ── Verdict schema (sorted keys for byte-stability) ──
VERDICT_SCHEMA = {
    "type": "object",
    "required": ["proof_course", "proof_practice", "proof_correction", "comment"],
    "properties": {
        "proof_course": {
            "type": "object",
            "required": ["present", "file", "anchor", "quote"],
            "properties": {
                "present": {"type": "boolean"},
                "file": {"type": ["string", "null"]},
                "anchor": {"type": ["string", "null"]},
                "quote": {"type": ["string", "null"]},
            },
        },
        "proof_practice": {
            "type": "object",
            "required": ["present", "file", "anchor", "quote"],
            "properties": {
                "present": {"type": "boolean"},
                "file": {"type": ["string", "null"]},
                "anchor": {"type": ["string", "null"]},
                "quote": {"type": ["string", "null"]},
            },
        },
        "proof_correction": {
            "type": "object",
            "required": ["present", "file", "anchor", "quote"],
            "properties": {
                "present": {"type": "boolean"},
                "file": {"type": ["string", "null"]},
                "anchor": {"type": ["string", "null"]},
                "quote": {"type": ["string", "null"]},
            },
        },
        "comment": {"type": "string"},
    },
}

GOLD_EXAMPLES = """

=== EXEMPLE 1 (3/3 proofs) ===
Capacité : P-DATA-BASE-01 — Passer de la représentation d'une base dans une autre.
Verdict :
{"proof_course": {"present": true, "file": "03_progressions/supports/premiere/P01/P01_cours_conversions_bases.md", "anchor": "#méthode-de-conversion", "quote": "Enchaîner divisions par 2 puis lire les restes de bas en haut."}, "proof_practice": {"present": true, "file": "03_progressions/supports/premiere/P01/P01_td_conversions_bases.md", "anchor": "#exercice-1", "quote": "Convertir 13 en base 2 en appliquant la méthode des divisions."}, "proof_correction": {"present": true, "file": "03_progressions/supports/premiere/P01/P01_corrige_conversions_bases.md", "anchor": "#corrigé-exercice-1", "quote": "13 = 1101 en base 2."}, "comment": "Cours enseigne la méthode, TD la fait pratiquer, corrigé fournit la réponse."}

=== EXEMPLE 2 (0/3 — contenu ne correspond pas au libellé) ===
Capacité : P-HIST-01 — Situer dans le temps les principaux événements de l'histoire de l'informatique.
Verdict :
{"proof_course": {"present": false, "file": null, "anchor": null, "quote": null}, "proof_practice": {"present": false, "file": null, "anchor": null, "quote": null}, "proof_correction": {"present": false, "file": null, "anchor": null, "quote": null}, "comment": "Contenu porte sur un projet énergie solaire, pas sur l'histoire de l'informatique."}

=== EXEMPLE 3 (2/3 — cours manquant) ===
Capacité : T-ALGO-01C — Parcourir un arbre en ordres infixe, préfixe ou suffixe.
Verdict :
{"proof_course": {"present": false, "file": null, "anchor": null, "quote": null}, "proof_practice": {"present": true, "file": "03_progressions/supports/terminale/T06/T06_TP_arbres_binaires_recherche.md", "anchor": "#trace-attendue-détaillée", "quote": "Parcours infixe attendu (T-ALGO-01C) : [1, 3, 6, 8, 10, 14]."}, "proof_correction": {"present": true, "file": "03_progressions/supports/terminale/T06/T06_corrige_arbres_binaires_recherche.md", "anchor": "#exercice-3", "quote": "Méthode : parcours infixe (gauche, racine, droite) — T-ALGO-01C."}, "comment": "TP et corrigé exercent le parcours infixe. Pas de cours dédié."}

=== EXEMPLE 4 (3/3 avec itération explicite) ===
Capacité : P-DATA-CONSTR-02D — Itérer sur les éléments d'un tableau.
Verdict :
{"proof_course": {"present": true, "file": "03_progressions/supports/premiere/P04/P04_trace_types_construits.md", "anchor": "#repère-2---liste-de-relevés", "quote": "À retenir : parcourir les valeurs et calculer une moyenne."}, "proof_practice": {"present": true, "file": "03_progressions/supports/premiere/P04/P04_td_types_construits.md", "anchor": "#exercice-2", "quote": "Écrire une boucle for valeur in releves qui calcule la moyenne."}, "proof_correction": {"present": true, "file": "03_progressions/supports/premiere/P04/P04_corrige_types_construits.md", "anchor": "#corrigé-exercice-2", "quote": "parcourir les valeurs et calculer une moyenne."}, "comment": "Trace enseigne l'itération, TD fait pratiquer avec boucle for."}"""

# ── J2c: Hardened protocol ──
PROTOCOLE_JUGE = """Tu es un juge pédagogique NSI. Pour chaque capacité officielle du programme,
tu reçois le libellé officiel et les extraits des fichiers d'évidence.
Chaque extrait est précédé de son chemin === chemin/fichier.md === et du tag [CAPACITÉ: X-Y-Z].

Réponds UNIQUEMENT en JSON valide (sans markdown, sans backticks), conforme au schéma ci-dessous.

RÈGLES DE CITATION (J2c — CRITIQUES, le vérificateur mécanique rejette les infractions) :
1. "quote" doit être une SOUS-CHAÎNE VERBATIM de l'extrait : conserver la casse, le gras (**),
   les puces (- ), les backticks (`). NE PAS reformuler, NE PAS concaténer, NE PAS inventer.
2. "quote" DOIT contenir au moins 25 caractères de contenu réel (pas un label comme "P-ALGO-01A").
3. Chaque rôle (cours/practice/correction) doit avoir une citation DISTINCTE — JAMAIS la même.
4. "anchor" = slug GitHub d'un titre ## ou ### EXISTANT (#en-minuscules-avec-tirets).
5. "file" = chemin EXACT copié depuis la ligne === chemin ===.
6. Ne citer que des sections dont le TAG [CAPACITÉ: ...] correspond à la capacité jugée.
   Si le tag ne correspond pas, chercher dans les autres extraits. Si aucun extrait ne correspond,
   mettre present: false.
7. Si aucune preuve solide n'existe pour un rôle → present: false honnête. JAMAIS de remplissage.

RÈGLES DE VERDICT :
- proof_course : le COURS ou la TRACE enseigne la capacité (définition, méthode, explication)
- proof_practice : le TD ou TP fait PRATIQUER (exercice réel avec consigne et production attendue)
- proof_correction : le corrigé ou l'évaluation permet de SE CORRIGER (réponse, barème, correction)
- present: false si le contenu ne correspond PAS au libellé officiel (étiquette administrative seule)
- "comment" : justification en 1-3 phrases, ≤ 400 caractères, phrase complète

"""

SYSTEM_TEXT = (
    PROTOCOLE_JUGE
    + "SCHÉMA JSON ATTENDU :\n"
    + json.dumps(VERDICT_SCHEMA, sort_keys=True, ensure_ascii=False, indent=2)
    + "\n\nEXEMPLES DE VERDICTS CORRECTS :"
    + GOLD_EXAMPLES
)

SYSTEM_BLOCKS = [
    {
        "type": "text",
        "text": SYSTEM_TEXT,
        "cache_control": {"type": "ephemeral"},
    }
]


def load_programme() -> dict[str, dict[str, str]]:
    data = yaml.safe_load(PROGRAMME_FILE.read_text(encoding="utf-8"))
    entries: dict[str, dict[str, str]] = {}
    for level in ("premiere", "terminale"):
        for cap in data["programmes"].get(level, []):
            cap_attendue = cap.get("capacite_attendue", [""])
            cap_id = str(cap["id"])
            entries[cap_id] = {
                "id": cap_id,
                "intitule": cap_attendue[0] if isinstance(cap_attendue, list) else str(cap_attendue),
                "contenu": str(cap.get("contenu", "")),
                "rubrique": str(cap.get("rubrique", "")),
                "niveau": level,
            }
    return entries


def extract_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:]
    return text


def find_sequences_for_capacity(cap_id: str) -> list[str]:
    prefix_pattern = re.compile(r"[PT]\d{2}")
    sequences: set[str] = set()
    for level_dir in [SUPPORTS_DIR / "premiere", SUPPORTS_DIR / "terminale"]:
        if not level_dir.is_dir():
            continue
        for seq_dir in sorted(level_dir.iterdir()):
            if not seq_dir.is_dir() or not prefix_pattern.fullmatch(seq_dir.name):
                continue
            for md_path in seq_dir.rglob("*.md"):
                if "contracts" in md_path.parts:
                    continue
                fm = read_frontmatter(md_path)
                official = fm.get("official_program")
                if not isinstance(official, dict):
                    continue
                caps = official.get("capacities", [])
                if isinstance(caps, list) and cap_id in {str(c) for c in caps if isinstance(c, str)}:
                    sequences.add(seq_dir.name)
                    break
    return sorted(sequences)


def build_sequence_context(seq_id: str, cap_id: str) -> str:
    """Build context for a sequence, tagging each file with its declared capacities.

    J2b: NO truncation — full body. Each extrait tagged with [CAPACITÉ: ...] for
    anti cross-attribution.
    """
    level = "premiere" if seq_id.startswith("P") else "terminale"
    seq_dir = SUPPORTS_DIR / level / seq_id
    if not seq_dir.is_dir():
        return ""
    parts: list[str] = []
    for md_path in sorted(seq_dir.rglob("*.md")):
        if "contracts" in md_path.parts:
            continue
        fm = read_frontmatter(md_path)
        official = fm.get("official_program")
        file_caps: list[str] = []
        if isinstance(official, dict):
            raw = official.get("capacities", [])
            if isinstance(raw, list):
                file_caps = [str(c) for c in raw if isinstance(c, str)]
        # Only include files that declare the target capacity
        if cap_id not in file_caps:
            continue
        rel = md_path.relative_to(ROOT).as_posix()
        body = extract_body(md_path)
        cap_tag = ", ".join(file_caps)
        parts.append(f"=== {rel} ===\n[CAPACITÉ: {cap_tag}]\n{body}")
    return "\n\n".join(parts)


def build_capacity_prompt(cap_id: str, programme: dict[str, dict[str, str]]) -> str:
    cap = programme[cap_id]
    return (
        f"CAPACITÉ À JUGER : {cap_id} — {cap['intitule']}\n"
        f"Rubrique : {cap['rubrique']}\n"
        f"Contenu : {cap['contenu']}\n\n"
        f"Analyse les extraits ci-dessus et produis le verdict JSON."
    )


def call_anthropic_cached(
    api_key: str,
    seq_context: str,
    capacity_prompt: str,
) -> tuple[dict[str, Any], dict[str, int]]:
    user_content: list[dict[str, Any]] = []
    if seq_context:
        user_content.append({
            "type": "text",
            "text": seq_context,
            "cache_control": {"type": "ephemeral"},
        })
    user_content.append({"type": "text", "text": capacity_prompt})

    body = {
        "model": MODEL,
        "max_tokens": 2500,  # J2e: increased from 1500
        "temperature": 0,
        "system": SYSTEM_BLOCKS,
        "messages": [{"role": "user", "content": user_content}],
    }
    data = json.dumps(body).encode("utf-8")

    last_err: Exception | None = None
    for attempt in range(3):
        if attempt > 0:
            delay = 2 ** attempt
            print(f"  retry {attempt+1}/3 in {delay}s...", end=" ", flush=True)
            time.sleep(delay)
        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages",
            data=data,
            headers={
                "Content-Type": "application/json",
                "x-api-key": api_key,
                "anthropic-version": "2023-06-01",
            },
        )
        try:
            resp = urllib.request.urlopen(req, timeout=120)
            last_err = None
            break
        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8", errors="replace")
            if e.code in (429, 529) or "overloaded" in error_body.lower():
                last_err = RuntimeError(f"API {e.code}: {error_body[:200]}")
                continue
            raise RuntimeError(f"API {e.code}: {error_body[:300]}") from e
        except (TimeoutError, OSError) as e:
            last_err = e
            continue
    if last_err is not None:
        raise last_err

    result = json.loads(resp.read())
    usage = result.get("usage", {})
    usage_dict = {
        "read": usage.get("cache_read_input_tokens", 0),
        "write": usage.get("cache_creation_input_tokens", 0),
        "fresh": usage.get("input_tokens", 0),
        "out": usage.get("output_tokens", 0),
    }

    content = ""
    for block in result.get("content", []):
        if block.get("type") == "text":
            content += block.get("text", "")

    content = content.strip()
    if content.startswith("```"):
        content = re.sub(r"^```\w*\n?", "", content)
        content = re.sub(r"\n?```$", "", content)
    try:
        parsed = json.loads(content)
    except json.JSONDecodeError:
        parsed = {"error": "JSON parse failed", "raw": content[:500]}

    return parsed, usage_dict


def format_verdict(cap_id: str, cap_info: dict[str, str], judge_result: dict[str, Any]) -> dict[str, Any]:
    """Format verdict. J2a: NO padding, NO truncation. Quotes are verbatim from the LLM."""
    def make_proof(role_key: str) -> dict[str, Any]:
        role_data = judge_result.get(role_key, {})
        if not isinstance(role_data, dict):
            return {"present": False, "file": None, "anchor": None, "quote": None, "teaches": False}
        present = bool(role_data.get("present", False))
        return {
            "present": present,
            "file": str(role_data.get("file", "")) if present else None,
            "anchor": str(role_data.get("anchor", "")) if present else None,
            "quote": str(role_data.get("quote", "")) if present else None,
            "teaches": present,
        }

    proofs = {
        "proof_course": make_proof("proof_course"),
        "proof_practice": make_proof("proof_practice"),
        "proof_correction": make_proof("proof_correction"),
    }
    present_count = sum(1 for p in proofs.values() if p.get("present"))
    verdict = "needs_review" if present_count else "needs_content"

    # J2e: guard justification — ensure complete sentence, no placeholder
    justification = str(judge_result.get("comment", ""))
    if not justification or len(justification) < 20:
        justification = "Verdict campagne Sonnet 4.6."
    if len(justification) > 400:
        # Truncate at last sentence boundary
        cut = justification[:400].rfind(".")
        justification = justification[:cut + 1] if cut > 100 else justification[:397] + "..."

    return {
        "capacity_id": cap_id,
        "official_label": cap_info["intitule"],
        **proofs,
        "verdict": verdict,
        "justification": justification,
        "scientific_flags": ["human_review_required"],
    }


def validate_verdict_file(verdict_path: Path) -> list[str]:
    """J2d: Run the hardened checker on a single verdict file.
    Returns list of error messages (empty = valid)."""
    result = subprocess.run(
        [sys.executable, "-m", "scripts.check_substance_anchors",
         str(verdict_path), "--repo-root", str(ROOT)],
        cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )
    if result.returncode == 0:
        return []
    errors = []
    for line in result.stdout.splitlines():
        if "INVALIDE" in line or "introuvable" in line or "absente" in line:
            errors.append(line.strip())
    return errors or [f"checker returned code {result.returncode}"]


def save_verdict(cap_id: str, verdict: dict[str, Any], programme: dict[str, dict[str, str]],
                 output_dir: Path) -> Path:
    review = {
        "schema_version": "1.0.0",
        "unit": "campaign",
        "level": programme[cap_id]["niveau"],
        "judged_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "judge_model": MODEL,
        "author_model": "campaign-tooling",
        "capacities": [verdict],
    }
    out_path = output_dir / f"{cap_id}_substance_review.json"
    out_path.write_text(json.dumps(review, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return out_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Judge campaign via Anthropic API (cached, hardened)")
    parser.add_argument("--cap-ids", type=str, default="", help="Comma-separated capacity IDs")
    parser.add_argument("--all", action="store_true", help="Judge all capacities")
    parser.add_argument("--dry-run", action="store_true", help="List capacities without calling API")
    parser.add_argument("--count-tokens", action="store_true", help="Count system block tokens")
    parser.add_argument("--force", action="store_true", help="Re-judge even if verdict file exists")
    parser.add_argument("--output-dir", type=Path, default=OUTPUT_DIR)
    args = parser.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        env_path = ROOT / ".env"
        if env_path.exists():
            for line in env_path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line.startswith("ANTHROPIC_API_KEY="):
                    api_key = line.split("=", 1)[1].strip()
                    break
    if not api_key and not args.dry_run:
        print("ERROR: ANTHROPIC_API_KEY not set in environment", file=sys.stderr)
        return 1

    programme = load_programme()

    if args.cap_ids:
        cap_ids = [c.strip() for c in args.cap_ids.split(",") if c.strip()]
    elif args.all:
        cap_ids = sorted(programme.keys())
    else:
        print("ERROR: specify --cap-ids or --all", file=sys.stderr)
        return 1

    selected = [c for c in cap_ids if c in programme]

    if args.dry_run:
        if args.count_tokens:
            sys_tokens = len(SYSTEM_TEXT) // 4
            print(f"System block: {len(SYSTEM_TEXT)} chars ~ {sys_tokens} tokens")
            print(f"  (minimum 1024 for cache: {'OK' if sys_tokens >= 1024 else 'TOO SHORT'})")
        print(f"Would judge {len(selected)} capacities:")
        seq_map: dict[str, list[str]] = {}
        for cap_id in selected:
            seqs = find_sequences_for_capacity(cap_id)
            seq_map.setdefault(seqs[0] if seqs else "?", []).append(cap_id)
        for seq_id in sorted(seq_map):
            print(f"  {seq_id}: {', '.join(seq_map[seq_id])}")
        return 0

    def seq_sort_key(cid: str) -> str:
        seqs = find_sequences_for_capacity(cid)
        return seqs[0] if seqs else "zzz"

    selected.sort(key=seq_sort_key)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    results: list[dict[str, Any]] = []
    usage_log: list[dict[str, Any]] = []
    seq_context_cache: dict[tuple[str, str], str] = {}  # (seq_id, cap_id) -> context
    api_calls = 0

    for i, cap_id in enumerate(selected):
        seqs = find_sequences_for_capacity(cap_id)
        seq_id = seqs[0] if seqs else ""

        # J2b: context is per (seq, cap) — includes only files declaring this cap
        cache_key = (seq_id, cap_id)
        if cache_key not in seq_context_cache:
            seq_context_cache[cache_key] = build_sequence_context(seq_id, cap_id) if seq_id else ""
        seq_context = seq_context_cache[cache_key]

        if not seq_context:
            print(f"  [{i+1}/{len(selected)}] {cap_id}: no evidence, skipping")
            continue

        out_path = args.output_dir / f"{cap_id}_substance_review.json"
        if out_path.exists() and not args.force:
            print(f"  [{i+1}/{len(selected)}] {cap_id} ({seq_id}): skip (use --force)")
            continue

        cap_prompt = build_capacity_prompt(cap_id, programme)

        print(f"  [{i+1}/{len(selected)}] {cap_id} ({seq_id})...", end=" ", flush=True)
        try:
            judge_result, usage = call_anthropic_cached(api_key, seq_context, cap_prompt)
            api_calls += 1
            verdict = format_verdict(cap_id, programme[cap_id], judge_result)

            # J2d: validate-before-save
            tmp_path = save_verdict(cap_id, verdict, programme, args.output_dir)
            errors = validate_verdict_file(tmp_path)

            if errors:
                # ONE retry with error feedback
                print("INVALID, retrying...", end=" ", flush=True)
                feedback = (
                    "Le verdict précédent a échoué la validation mécanique :\n"
                    + "\n".join(errors[:5])
                    + "\n\nCorrige les erreurs. Rappel : quote = sous-chaîne VERBATIM, "
                    "≥25 chars, anchor = slug existant, une citation DISTINCTE par rôle."
                )
                retry_prompt = cap_prompt + "\n\nFEEDBACK DU VÉRIFICATEUR :\n" + feedback
                judge_result2, usage2 = call_anthropic_cached(api_key, seq_context, retry_prompt)
                api_calls += 1
                # Merge usage
                for k in usage:
                    usage[k] += usage2[k]
                verdict = format_verdict(cap_id, programme[cap_id], judge_result2)
                tmp_path = save_verdict(cap_id, verdict, programme, args.output_dir)
                errors2 = validate_verdict_file(tmp_path)
                if errors2:
                    # Still invalid — degrade to needs_content with error noted
                    verdict["verdict"] = "needs_content"
                    verdict["justification"] = f"Auto-dégradé : preuve invalide après 2 tentatives. {'; '.join(errors2[:3])}"
                    for role in ["proof_course", "proof_practice", "proof_correction"]:
                        verdict[role] = {"present": False, "file": None, "anchor": None, "quote": None, "teaches": False}
                    save_verdict(cap_id, verdict, programme, args.output_dir)
                    print("DEGRADED to needs_content")
                else:
                    print("FIXED", end=" ")

            results.append(verdict)
            present_count = sum(1 for k in ["proof_course", "proof_practice", "proof_correction"]
                              if verdict[k].get("present"))
            cost = (usage["read"] * 0.30 + usage["write"] * 3.75
                    + usage["fresh"] * 3.0 + usage["out"] * 15.0) / 1_000_000
            usage_log.append({"cap": cap_id, "seq": seq_id, **usage, "cost_usd": round(cost, 6),
                              "api_calls": api_calls})

            print(f"{present_count}/3 | r={usage['read']} w={usage['write']} f={usage['fresh']} o={usage['out']} ${cost:.4f}")

            if api_calls >= 2 and usage["read"] < 1024:
                print(f"  WARNING: CACHE MISS on API call {api_calls}")

            if i < len(selected) - 1:
                time.sleep(0.5)
        except Exception as exc:
            print(f"ERROR: {exc}")
            err_verdict = format_verdict(cap_id, programme[cap_id], {"comment": f"API error: {exc}"})
            err_verdict["verdict"] = "needs_content"
            for role in ["proof_course", "proof_practice", "proof_correction"]:
                err_verdict[role] = {"present": False, "file": None, "anchor": None, "quote": None, "teaches": False}
            save_verdict(cap_id, err_verdict, programme, args.output_dir)
            results.append(err_verdict)
            usage_log.append({"cap": cap_id, "seq": seq_id, "read": 0, "write": 0,
                              "fresh": 0, "out": 0, "cost_usd": 0, "error": str(exc)[:100]})

    # Summary
    total_cost = sum(u.get("cost_usd", 0) for u in usage_log)
    total_read = sum(u.get("read", 0) for u in usage_log)
    total_write = sum(u.get("write", 0) for u in usage_log)
    total_fresh = sum(u.get("fresh", 0) for u in usage_log)
    total_out = sum(u.get("out", 0) for u in usage_log)

    print(f"\n{'='*60}")
    print(f"{len(results)} verdicts written to {args.output_dir}/")
    with_proofs = sum(1 for v in results if v["verdict"] == "needs_review")
    print(f"  needs_review (with proofs): {with_proofs}")
    print(f"  needs_content (no proofs): {len(results) - with_proofs}")
    print(f"\nAPI calls: {api_calls}")
    print("Token usage totals:")
    print(f"  cache_read: {total_read:,}  cache_write: {total_write:,}")
    print(f"  fresh_input: {total_fresh:,}  output: {total_out:,}")
    print(f"  TOTAL COST: ${total_cost:.4f}")

    log_path = args.output_dir / "_usage_log.json"
    log_path.write_text(json.dumps(usage_log, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\nUsage log: {log_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
