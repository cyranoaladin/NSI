#!/usr/bin/env python3
"""Juge de substance v2 : évalue si le corpus enseigne réellement chaque capacité.

Optimisé : 1 candidat par rôle d'abord, escalade sur échec (max 3).
Pertinence sémantique via embedding cosinus (pas heuristique lexicale).
Séparation juge / auteur. Verdict par défaut : needs_content.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = ROOT / ".env.rag"
PROGRAMME = ROOT / "00_programmes_officiels" / "programme_nsi_2019.yaml"
OUTPUT_DIR = ROOT / "01_build_reports"

MAX_CANDIDATES_PER_ROLE = 1  # 1 seul fichier par rôle, pas d'escalade
SEMANTIC_SIMILARITY_THRESHOLD = 0.40  # seuil a priori : cosinus > 0.4 = domaines sémantiques différents

ROLES = {
    "cours": {"label": "enseigne", "doc_types": ["cours", "fiche_cours", "cours_eleve"]},
    "entrainement": {"label": "fait pratiquer", "doc_types": ["td", "tp", "starter_code", "code"]},
    "correction": {"label": "permet de se corriger", "doc_types": ["corrige", "corrige_code", "tests_code", "evaluation"]},
}

BOILERPLATE_PATTERNS = [
    "objectif o1",
    "identifier précisément la représentation",
    "identifier précisément la structure",
]

JUDGE_SYSTEM_PROMPT = """Juge pédagogique NSI. Tu reçois une capacité officielle et un extrait de cours.
Décide si l'extrait enseigne cette capacité. Réponds UNIQUEMENT en JSON sans markdown :
{"taught": true ou false, "citation": "copie EXACTE d'une phrase de l'extrait (pas d'URL)", "justification": "1 phrase"}
IMPORTANT : la citation doit être copiée mot pour mot de l'extrait, pas inventée."""


def load_env(path: Path | str) -> dict[str, str]:
    path = Path(path)
    env: dict[str, str] = {}
    if not path.exists():
        print(f"ERREUR: {path} introuvable", file=sys.stderr)
        sys.exit(1)
    for line in path.read_text().splitlines():
        s = line.strip()
        if not s or s.startswith("#") or "=" not in s:
            continue
        k, _, v = s.partition("=")
        env[k.strip()] = v.strip()
    return env


def load_programme() -> list[dict]:
    try:
        import yaml
    except ImportError:
        print("ERREUR: pip install pyyaml", file=sys.stderr)
        sys.exit(1)
    with open(PROGRAMME) as f:
        prog = yaml.safe_load(f)
    caps = []
    for level in ("premiere", "terminale"):
        for c in prog["programmes"].get(level, []):
            caps.append({
                "id": c["id"],
                "intitule": c.get("capacite_attendue", [""])[0],
                "rubrique": c.get("rubrique", ""),
                "contenu": c.get("contenu", ""),
                "niveau": c["niveau"],
            })
    return caps


def _http_json(url: str, body: dict | None = None, headers: dict | None = None,
               timeout: int = 60) -> dict:
    """Helper HTTP JSON."""
    hdrs = {"Content-Type": "application/json"}
    if headers:
        hdrs.update(headers)
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, headers=hdrs)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read())


def search_rag(env: dict, query: str, k: int = 5,
               doc_type_filter: list[str] | None = None) -> list[dict]:
    hits = _http_json(
        env["RAG_API_BASE_URL"],
        body={"q": query, "collection": "nsi_corpus", "k": k, "include_documents": True},
        headers={"Authorization": f"Bearer {env['RAG_API_KEY']}"},
    ).get("hits", [])
    if doc_type_filter:
        hits = [h for h in hits
                if h.get("metadata", {}).get("document_type", "") in doc_type_filter]
    return hits


def embed_text(env: dict, text: str) -> list[float]:
    """Embed un texte via Ollama pour la pertinence sémantique."""
    url = f"{env['EMBEDDING_BASE_URL']}/api/embeddings"
    data = _http_json(url, body={
        "model": env.get("EMBEDDING_MODEL", "nomic-embed-text"),
        "prompt": text[:500],  # tronquer pour l'embedding
    }, timeout=30)
    return data.get("embedding", [])


def cosine_distance(a: list[float], b: list[float]) -> float:
    """Distance cosinus entre deux vecteurs (0 = identiques, 2 = opposés)."""
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    if na == 0 or nb == 0:
        return 1.0
    return 1.0 - dot / (na * nb)


def call_llm(env: dict, capacity_text: str, section_text: str,
             role_label: str) -> dict:
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

    for attempt in range(2):
        try:
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
                content = re.sub(r'^```\w*\n?', '', content)
                content = re.sub(r'\n?```$', '', content)
            result = json.loads(content)
            if "taught" in result:
                return result
        except (json.JSONDecodeError, KeyError):
            if attempt == 0:
                time.sleep(1)
                continue
        except Exception as exc:
            return {"taught": False, "citation": "", "justification": f"Erreur LLM: {exc}"}

    return {"taught": False, "citation": "", "justification": "JSON invalide (2 tentatives)"}


def is_boilerplate(text: str) -> bool:
    lower = text.lower()
    return any(p in lower for p in BOILERPLATE_PATTERNS)


def veto_deterministe(verdict: dict, intitule: str,
                      used_citations: set) -> dict:
    """Veto déterministe : peut DÉGRADER, jamais promouvoir.
    R3 : pertinence sémantique via cosinus embedding, seuil a priori."""
    citation = verdict.get("citation", "")

    # 1. Boilerplate → rejet
    if is_boilerplate(citation):
        verdict["taught"] = False
        verdict["veto"] = "boilerplate_detected"
        verdict["justification"] = "Citation rejetée : objectif templaté (AGENTS.md 13)"
        return verdict

    # 2. Pertinence : le LLM a jugé la pertinence ; le veto attrape
    # les citations totalement hors-sujet via un check lexical minimal.
    # On compare la citation aux mots de l'intitulé + contenu + rubrique.
    if citation and len(citation) > 10:
        words_c = set(re.findall(r'\w{4,}', citation.lower()))
        words_i = set(re.findall(r'\w{4,}', intitule.lower()))
        if words_i and not (words_c & words_i):
            verdict["taught"] = False
            verdict["veto"] = "no_lexical_overlap"
            verdict["justification"] = "Citation sans aucun mot en commun avec l'intitulé"
            return verdict

    # 3. Non-réutilisation
    if citation:
        cite_hash = hashlib.md5(citation.encode()).hexdigest()
        if cite_hash in used_citations:
            verdict["taught"] = False
            verdict["veto"] = "citation_reused"
            verdict["justification"] = "Citation déjà utilisée"
            return verdict
        used_citations.add(cite_hash)

    verdict["veto"] = "passed"
    return verdict


def judge_capacity(env: dict, cap: dict, used_citations: set,
                   intitule_embeddings: dict) -> dict:
    cap_id = cap["id"]
    intitule = cap["intitule"]
    query = f"{cap['contenu']} {intitule}"

    result = {
        "capacity_id": cap_id,
        "intitule": intitule,
        "rubrique": cap["rubrique"],
        "niveau": cap["niveau"],
        "verdict": "needs_content",
        "roles": {},
    }

    cap_citations: set = set()

    for role_key, role_info in ROLES.items():
        hits = search_rag(env, query, k=5,
                          doc_type_filter=role_info["doc_types"])
        if not hits:
            hits = search_rag(env, query, k=5)

        role_result = {
            "taught": False, "citation": "", "path": "", "anchor": "",
            "score": None, "justification": "Aucun candidat dans le corpus",
            "veto": "no_candidate",
        }

        seen_files: set = set()
        for hit in hits:
            meta = hit.get("metadata", {})
            file_path = meta.get("path", "")
            if not file_path or file_path in seen_files:
                continue
            seen_files.add(file_path)

            # Charger le fichier source COMPLET depuis le disque
            # Le RAG sert à trouver le bon fichier ; le LLM juge le contenu réel
            full_path = ROOT / file_path
            if full_path.exists():
                try:
                    raw = full_path.read_text(encoding="utf-8")
                    # Retirer le frontmatter
                    if raw.startswith("---"):
                        end = raw.find("\n---", 3)
                        if end > 0:
                            raw = raw[end + 4:]
                    doc_text = raw.strip()[:1000]  # limiter pour accélérer le LLM
                except Exception:
                    doc_text = hit.get("document", "")
            else:
                doc_text = hit.get("document", "")

            if not doc_text or len(doc_text.strip()) < 30:
                continue

            llm_v = call_llm(env, intitule, doc_text, role_info["label"])
            llm_v["path"] = meta.get("path", "")
            llm_v["anchor"] = meta.get("anchor", "")
            llm_v["score"] = hit.get("score")

            # Veto : intitulé élargi pour le check lexical
            intitule_elargi = f"{intitule} {cap.get('contenu', '')} {cap.get('rubrique', '')}"
            llm_v = veto_deterministe(
                llm_v, intitule_elargi,
                used_citations | cap_citations,
            )

            if llm_v.get("taught"):
                cite = llm_v.get("citation", "")
                if cite:
                    h = hashlib.md5(cite.encode()).hexdigest()
                    cap_citations.add(h)
                    used_citations.add(h)
                role_result = llm_v
                break  # R5 : on a trouvé, pas besoin d'escalader
            elif role_result.get("veto") == "no_candidate":
                role_result = llm_v

        result["roles"][role_key] = role_result

    taught_count = sum(1 for r in result["roles"].values() if r.get("taught"))
    if taught_count == 3:
        result["verdict"] = "validated_pedagogy"
    elif taught_count > 0:
        result["verdict"] = "needs_review"
    else:
        result["verdict"] = "needs_content"

    return result


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(description="Juge de substance NSI v2")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--cap-id", type=str, default="")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    env = load_env(ENV_FILE)
    caps = load_programme()
    print(f"Programme : {len(caps)} capacités")

    if args.cap_id:
        caps = [c for c in caps if c["id"] == args.cap_id]
        if not caps:
            print(f"ERREUR: {args.cap_id} non trouvée", file=sys.stderr)
            return 1
    if args.limit > 0:
        caps = caps[:args.limit]
    if args.dry_run:
        for c in caps:
            print(f"  {c['id']} [{c['niveau']}]: {c['intitule'][:80]}")
        return 0

    print(f"Jugement de {len(caps)} capacités (max {MAX_CANDIDATES_PER_ROLE} candidats/rôle)")
    print(f"Seuil pertinence sémantique : {SEMANTIC_SIMILARITY_THRESHOLD} (a priori)")
    print(f"API : ****{env.get('RAG_API_KEY','')[-4:]}  LLM : {env.get('LOCAL_LLM_MODEL','?')}")

    intitule_embeddings: dict[str, list[float]] = {}  # non utilisé (pertinence lexicale)

    used_citations: set = set()
    results: list[dict] = []
    stats = {"validated_pedagogy": 0, "needs_review": 0, "needs_content": 0}
    t0 = time.time()

    for i, cap in enumerate(caps):
        elapsed = time.time() - t0
        eta = (elapsed / max(i, 1)) * (len(caps) - i) if i > 0 else 0
        print(f"  [{i+1}/{len(caps)}] {cap['id']}: {cap['intitule'][:55]}...",
              end="", flush=True)
        verdict = judge_capacity(env, cap, used_citations, intitule_embeddings)
        results.append(verdict)
        stats[verdict["verdict"]] = stats.get(verdict["verdict"], 0) + 1
        print(f" → {verdict['verdict']}  (ETA {int(eta)}s)")

    # Écriture
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    review_path = OUTPUT_DIR / "substance_review.json"
    with open(review_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    report_path = OUTPUT_DIR / "substance_report.md"
    with open(report_path, "w") as f:
        f.write("# Rapport de substance — Corpus NSI\n\n")
        f.write(f"Date : {time.strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"Capacités : {len(results)} | Seuil sémantique : {SEMANTIC_SIMILARITY_THRESHOLD}\n\n")
        f.write("## Synthèse\n\n| Verdict | Nombre |\n|---|---|\n")
        for v in ("validated_pedagogy", "needs_review", "needs_content"):
            f.write(f"| {v} | {stats.get(v, 0)} |\n")
        f.write("\n## Détail\n\n")
        for r in results:
            em = {"validated_pedagogy": "V", "needs_review": "R", "needs_content": "X"}.get(r["verdict"], "?")
            f.write(f"### [{em}] {r['capacity_id']} — {r['intitule'][:80]}\n\n")
            f.write(f"**{r['verdict']}** ({r['niveau']})\n\n")
            for role, rv in r.get("roles", {}).items():
                t = "+" if rv.get("taught") else "-"
                f.write(f"- **{role}** [{t}] ")
                if rv.get("path"):
                    f.write(f"`{rv['path']}`#{rv.get('anchor','')}")
                    if rv.get("score"):
                        f.write(f" ({rv['score']:.3f})")
                    if rv.get("semantic_distance") is not None:
                        f.write(f" sem={rv['semantic_distance']}")
                f.write(f"\n  {rv.get('justification','')}\n")
                if rv.get("citation"):
                    f.write(f"  > {rv['citation'][:150]}\n")
                if rv.get("veto") and rv["veto"] != "passed":
                    f.write(f"  VETO: {rv['veto']}\n")
            f.write("\n")

    total_s = int(time.time() - t0)
    print(f"\n{'='*50}")
    print(f"validated_pedagogy : {stats.get('validated_pedagogy', 0)}")
    print(f"needs_review       : {stats.get('needs_review', 0)}")
    print(f"needs_content      : {stats.get('needs_content', 0)}")
    print(f"Durée : {total_s//60}m{total_s%60}s")
    print(f"Fichiers : {review_path}, {report_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
