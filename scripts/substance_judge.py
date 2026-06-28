#!/usr/bin/env python3
"""Proposeur de substance NSI.

System B propose des preuves au format strict de System A. Il combine une
pertinence lexicale minimale et un jugement LLM, puis délègue toujours le veto
mécanique final à `check_substance_anchors.py`. Il ne produit jamais de verdict
final `validated_pedagogy`.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import urllib.request
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, TypedDict

from check_substance_anchors import citation_status, parse_sections, validate_schema


ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = ROOT / ".env.rag"
PROGRAMME = ROOT / "00_programmes_officiels" / "programme_nsi_2019.yaml"
OUTPUT_DIR = ROOT / "01_build_reports"
MAX_CANDIDATES_PER_ROLE = 1


class RoleConfig(TypedDict):
    search_key: str
    label: str
    doc_types: list[str]


ROLES: dict[str, RoleConfig] = {
    "proof_course": {
        "search_key": "cours",
        "label": "enseigne",
        "doc_types": ["cours", "fiche_cours", "cours_eleve"],
    },
    "proof_practice": {
        "search_key": "entrainement",
        "label": "fait pratiquer",
        "doc_types": ["td", "tp", "starter_code", "code"],
    },
    "proof_correction": {
        "search_key": "correction",
        "label": "permet de se corriger",
        "doc_types": ["corrige", "corrige_code", "tests_code", "evaluation"],
    },
}

BOILERPLATE_PATTERNS = [
    "objectif o1",
    "identifier précisément la représentation",
    "identifier précisément la structure",
]

JUDGE_SYSTEM_PROMPT = """Juge pédagogique NSI. Tu reçois une capacité officielle et un extrait.
Décide si l'extrait enseigne cette capacité. Réponds uniquement en JSON :
{"taught": true ou false, "citation": "copie exacte d'une phrase de l'extrait", "justification": "1 phrase"}"""


def load_env(path: Path | str) -> dict[str, str]:
    path = Path(path)
    env: dict[str, str] = {}
    if not path.exists():
        print(f"ERREUR: {path} introuvable", file=sys.stderr)
        raise SystemExit(1)
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, _, value = stripped.partition("=")
        env[key.strip()] = value.strip()
    return env


def load_programme() -> list[dict[str, str]]:
    try:
        import yaml
    except ImportError as exc:
        print("ERREUR: pip install pyyaml", file=sys.stderr)
        raise SystemExit(1) from exc
    with PROGRAMME.open(encoding="utf-8") as handle:
        programme = yaml.safe_load(handle)
    capacities: list[dict[str, str]] = []
    for level in ("premiere", "terminale"):
        for item in programme["programmes"].get(level, []):
            capacities.append(
                {
                    "id": str(item["id"]),
                    "intitule": str((item.get("capacite_attendue") or [""])[0]),
                    "rubrique": str(item.get("rubrique", "")),
                    "contenu": str(item.get("contenu", "")),
                    "niveau": str(item["niveau"]),
                }
            )
    return capacities


def _http_json(url: str, body: dict[str, Any] | None = None, headers: dict[str, str] | None = None,
               timeout: int = 60) -> dict[str, Any]:
    request_headers = {"Content-Type": "application/json"}
    if headers:
        request_headers.update(headers)
    data = json.dumps(body).encode("utf-8") if body else None
    req = urllib.request.Request(url, data=data, headers=request_headers)
    with urllib.request.urlopen(req, timeout=timeout) as response:
        payload = json.loads(response.read())
    if not isinstance(payload, dict):
        raise ValueError(f"réponse JSON non objet depuis {url}")
    return payload


def search_rag(env: dict[str, str], query: str, k: int = 5,
               doc_type_filter: list[str] | None = None) -> list[dict[str, Any]]:
    raw_hits = _http_json(
        env["RAG_API_BASE_URL"],
        body={"q": query, "collection": "nsi_corpus", "k": k, "include_documents": True},
        headers={"Authorization": f"Bearer {env['RAG_API_KEY']}"},
    ).get("hits", [])
    hits = raw_hits if isinstance(raw_hits, list) else []
    if doc_type_filter:
        hits = [
            hit for hit in hits
            if isinstance(hit, dict)
            and hit.get("metadata", {}).get("document_type", "") in doc_type_filter
        ]
    return [hit for hit in hits if isinstance(hit, dict)]


def call_llm(env: dict[str, str], capacity_text: str, section_text: str, role_label: str) -> dict[str, Any]:
    llm_url = env.get("LOCAL_LLM_BASE_URL", "")
    llm_model = env.get("LOCAL_LLM_MODEL", "qwen2.5:7b")
    if not llm_url:
        return {"taught": False, "citation": "", "justification": "LLM non configurée"}

    user_prompt = (
        f"Capacité NSI : \"{capacity_text}\"\n"
        f"Rôle : {role_label}\n\n"
        f"Extrait :\n---\n{section_text[:800]}\n---\n\n"
        f"Cette section {role_label}-t-elle cette capacité ?"
    )
    data = _http_json(
        f"{llm_url}/chat/completions",
        body={
            "model": llm_model,
            "messages": [
                {"role": "system", "content": JUDGE_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": 0,
        },
        timeout=90,
    )
    content = data["choices"][0]["message"]["content"].strip()
    if content.startswith("```"):
        content = re.sub(r"^```\w*\n?", "", content)
        content = re.sub(r"\n?```$", "", content)
    result = json.loads(content)
    if not isinstance(result, dict):
        return {"taught": False, "citation": "", "justification": "JSON LLM non objet"}
    if "taught" not in result:
        return {"taught": False, "citation": "", "justification": "JSON LLM incomplet"}
    return result


def is_boilerplate(text: str) -> bool:
    lowered = text.lower()
    return any(pattern in lowered for pattern in BOILERPLATE_PATTERNS)


def has_lexical_overlap(citation: str, capacity_text: str) -> bool:
    citation_words = set(re.findall(r"\w{4,}", citation.lower()))
    capacity_words = set(re.findall(r"\w{4,}", capacity_text.lower()))
    return bool(citation_words & capacity_words) if capacity_words else True


def absent_proof(note: str) -> dict[str, Any]:
    return {
        "present": False,
        "file": None,
        "anchor": None,
        "quote": None,
        "teaches": False,
        "note": note[:400],
    }


def accepted_proof(file_path: str, anchor: str, quote: str, note: str) -> dict[str, Any]:
    return {
        "present": True,
        "file": file_path,
        "anchor": anchor,
        "quote": quote,
        "teaches": True,
        "note": note[:400],
    }


def source_section_text(repo_root: Path, file_path: str, anchor: str) -> str:
    full_path = repo_root / file_path
    if not full_path.exists():
        return ""
    sections = parse_sections(full_path.read_text(encoding="utf-8"))
    section = sections.get(anchor.lstrip("#"))
    if section is None:
        return ""
    return section.body


def vet_llm_evidence(
    *,
    repo_root: Path,
    file_path: str,
    anchor: str,
    verdict: dict[str, Any],
    capacity_text: str,
    used_citations: set[str],
) -> dict[str, Any]:
    citation = str(verdict.get("citation") or "")
    if not verdict.get("taught"):
        return absent_proof(str(verdict.get("justification") or "LLM: preuve non enseignante"))
    if is_boilerplate(citation):
        return absent_proof("boilerplate_detected")
    citation_hash = hashlib.md5(citation.encode("utf-8")).hexdigest()
    if citation_hash in used_citations:
        return absent_proof("citation_reused")
    body = source_section_text(repo_root, file_path, anchor)
    status, _ = citation_status(citation, body, strict=True)
    if status == "absent":
        return absent_proof("citation_introuvable")
    lexical = "lexical_overlap" if has_lexical_overlap(citation, capacity_text) else "lexical_limited"
    used_citations.add(citation_hash)
    note = f"{lexical}; {verdict.get('justification') or 'preuve proposée'}"
    return accepted_proof(file_path, anchor, citation, note)


def _candidate_text(repo_root: Path, hit: dict[str, Any]) -> tuple[str, str, str]:
    meta = hit.get("metadata", {})
    file_path = str(meta.get("path", ""))
    anchor = str(meta.get("anchor", ""))
    body = source_section_text(repo_root, file_path, anchor) if file_path and anchor else ""
    if not body:
        body = str(hit.get("document", ""))
    return file_path, anchor, body


def judge_capacity(env: dict[str, str], cap: dict[str, str], used_citations: set[str]) -> dict[str, Any]:
    capacity_text = f"{cap['intitule']} {cap.get('contenu', '')} {cap.get('rubrique', '')}"
    query = f"{cap.get('contenu', '')} {cap['intitule']}"
    result: dict[str, Any] = {
        "capacity_id": cap["id"],
        "official_label": cap["intitule"],
        "proof_course": absent_proof("aucune preuve proposée"),
        "proof_practice": absent_proof("aucune preuve proposée"),
        "proof_correction": absent_proof("aucune preuve proposée"),
        "verdict": "needs_content",
        "justification": "Proposition outillée : aucune validation humaine n'est déclarée.",
        "scientific_flags": ["human_review_required"],
    }
    local_citations: set[str] = set()
    for proof_key, role in ROLES.items():
        hits = search_rag(env, query, k=5, doc_type_filter=role["doc_types"])
        if not hits:
            hits = search_rag(env, query, k=5)
        selected = absent_proof("aucun candidat dans le corpus")
        for hit in hits[:MAX_CANDIDATES_PER_ROLE]:
            file_path, anchor, text = _candidate_text(ROOT, hit)
            if not file_path or not anchor or len(text.strip()) < 12:
                selected = absent_proof("candidat incomplet")
                continue
            llm_verdict = call_llm(env, cap["intitule"], text, role["label"])
            selected = vet_llm_evidence(
                repo_root=ROOT,
                file_path=file_path,
                anchor=anchor,
                verdict=llm_verdict,
                capacity_text=capacity_text,
                used_citations=used_citations | local_citations,
            )
            if selected["present"]:
                local_citations.add(hashlib.md5(str(selected["quote"]).encode("utf-8")).hexdigest())
                used_citations.update(local_citations)
                break
        result[proof_key] = selected
    present_count = sum(1 for key in ("proof_course", "proof_practice", "proof_correction") if result[key]["present"])
    if present_count:
        result["verdict"] = "needs_review"
        result["justification"] = "Proposition outillée : preuves citées à relire, sans promotion de statut."
    return result


def build_verdict(unit: str, level: str, capacities: list[dict[str, str]], env: dict[str, str]) -> dict[str, Any]:
    used_citations: set[str] = set()
    payload: dict[str, Any] = {
        "schema_version": "1.0.0",
        "unit": unit,
        "level": level,
        "judged_at": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
        "judge_model": env.get("LOCAL_LLM_MODEL", "substance-judge-proposer"),
        "author_model": "unknown",
        "capacities": [judge_capacity(env, cap, used_citations) for cap in capacities],
    }
    errors = validate_schema(payload, ROOT / "substance_verdict.schema.json")
    hard_errors = [error for error in errors if error.startswith("schéma @")]
    if hard_errors:
        raise ValueError("; ".join(hard_errors))
    return payload


def offline_fixture(unit: str) -> dict[str, Any]:
    matches = sorted(ROOT.glob(f"03_progressions/supports/**/{unit}/_substance_review.json"))
    if not matches:
        raise FileNotFoundError(f"fixture offline introuvable pour {unit}")
    payload = json.loads(matches[0].read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"fixture offline non objet pour {unit}")
    return payload


def write_outputs(payload: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Proposeur de substance NSI")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--cap-id", type=str, default="")
    parser.add_argument("--unit", type=str, default="ALL")
    parser.add_argument("--output", type=Path, default=OUTPUT_DIR / "substance_review.json")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--offline-fixture", action="store_true")
    args = parser.parse_args()

    if args.offline_fixture:
        payload = offline_fixture(args.unit)
        write_outputs(payload, args.output)
        print(f"substance_judge: fixture offline {args.unit} -> {args.output}")
        return 0

    env = load_env(ENV_FILE)
    capacities = load_programme()
    if args.cap_id:
        capacities = [cap for cap in capacities if cap["id"] == args.cap_id]
        if not capacities:
            print(f"ERREUR: {args.cap_id} non trouvée", file=sys.stderr)
            return 1
    if args.limit > 0:
        capacities = capacities[:args.limit]
    if args.dry_run:
        for cap in capacities:
            print(f"  {cap['id']} [{cap['niveau']}]: {cap['intitule'][:80]}")
        return 0

    level = capacities[0]["niveau"] if capacities else "premiere"
    print("Juge de substance : pertinence lexicale + jugement LLM")
    print(f"Jugement de {len(capacities)} capacités (max {MAX_CANDIDATES_PER_ROLE} candidat/rôle)")
    payload = build_verdict(args.unit, level, capacities, env)
    write_outputs(payload, args.output)
    stats: dict[str, int] = {}
    for cap in payload["capacities"]:
        stats[cap["verdict"]] = stats.get(cap["verdict"], 0) + 1
    print(f"Sortie : {args.output}")
    for status, count in sorted(stats.items()):
        print(f"{status}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
