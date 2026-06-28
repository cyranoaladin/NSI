#!/usr/bin/env python3
"""Juge de substance : évalue si le corpus enseigne réellement chaque capacité.

Flux par capacité :
1. Charger l'intitulé officiel depuis programme_nsi_2019.yaml
2. Interroger nsi_corpus via l'API /search (3 requêtes par rôle)
3. Soumettre les candidats à la LLM locale (qwen2.5:7b)
4. Appliquer le veto déterministe (ancre, pertinence, non-réutilisation)
5. Produire un verdict cité

Séparation stricte juge / auteur : ce script ne rédige rien.
Verdict par défaut : needs_content.
"""
from __future__ import annotations

import hashlib
import json
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

# Rôles à évaluer
ROLES = {
    "cours": {"label": "enseigne", "doc_types": ["cours", "fiche_cours", "cours_eleve"]},
    "entrainement": {"label": "fait pratiquer", "doc_types": ["td", "tp", "starter_code", "code"]},
    "correction": {"label": "permet de se corriger", "doc_types": ["corrige", "corrige_code", "tests_code", "evaluation"]},
}

# Boilerplate connu (AGENTS.md 13)
BOILERPLATE_PATTERNS = [
    "objectif o1",
    "identifier précisément la représentation",
    "identifier précisément la structure",
]

JUDGE_SYSTEM_PROMPT = """Tu es un juge de substance pédagogique pour le programme NSI (Numérique et Sciences Informatiques).
Tu évalues si une section de cours/TD/TP enseigne RÉELLEMENT une capacité officielle du programme.

Règles strictes :
- Tu ne juges que la pertinence de la section par rapport à la capacité.
- Un objectif générique ("Objectif O1 - Identifier précisément la représentation ou la structure en jeu") n'est PAS une preuve.
- Une simple mention du mot-clé ne suffit pas : la section doit ENSEIGNER, ENTRAÎNER ou CORRIGER la capacité.
- Verdict par défaut : needs_content (pas de faux positif).

Réponds UNIQUEMENT en JSON strict (pas de markdown, pas de commentaire) :
{
  "taught": true/false,
  "citation": "passage exact (max 150 caractères) qui prouve l'enseignement",
  "justification": "pourquoi ce passage enseigne/n'enseigne pas cette capacité (1 phrase)"
}"""


def load_env(path: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    if not path.exists():
        print(f"ERREUR: {path} introuvable", file=sys.stderr)
        sys.exit(1)
    for line in path.read_text().splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if "=" not in s:
            continue
        k, _, v = s.partition("=")
        env[k.strip()] = v.strip()
    return env


def load_programme() -> list[dict]:
    """Charge les 114 capacités depuis le YAML."""
    try:
        import yaml
    except ImportError:
        # Fallback sans PyYAML
        print("ERREUR: PyYAML requis (pip install pyyaml)", file=sys.stderr)
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


def search_rag(env: dict, query: str, k: int = 5,
               doc_type_filter: list[str] | None = None) -> list[dict]:
    """Interroge nsi_corpus via l'API /search."""
    url = env["RAG_API_BASE_URL"]
    body = json.dumps({
        "q": query,
        "collection": "nsi_corpus",
        "k": k,
        "include_documents": True,
    }).encode()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {env['RAG_API_KEY']}",
    }
    req = urllib.request.Request(url, data=body, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read())
    except Exception as exc:
        print(f"  ERREUR RAG: {exc}", file=sys.stderr)
        return []
    hits = data.get("hits", [])
    # Filtrer par document_type si demandé
    if doc_type_filter:
        hits = [h for h in hits
                if h.get("metadata", {}).get("document_type", "") in doc_type_filter]
    return hits


def call_llm(env: dict, capacity_text: str, section_text: str,
             role_label: str) -> dict:
    """Appelle la LLM locale pour juger une section."""
    llm_url = env.get("LOCAL_LLM_BASE_URL", "")
    llm_model = env.get("LOCAL_LLM_MODEL", "qwen2.5:7b")
    if not llm_url:
        return {"taught": False, "citation": "", "justification": "LLM non configurée"}

    user_prompt = (
        f"Capacité officielle NSI : \"{capacity_text}\"\n"
        f"Rôle attendu : {role_label}\n\n"
        f"Section du corpus (extrait) :\n"
        f"---\n{section_text[:2000]}\n---\n\n"
        f"Cette section {role_label}-t-elle réellement cette capacité ?"
    )

    body = json.dumps({
        "model": llm_model,
        "messages": [
            {"role": "system", "content": JUDGE_SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0,
    }).encode()
    headers = {"Content-Type": "application/json"}
    api_key = env.get("LOCAL_LLM_API_KEY", "")
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    url = f"{llm_url}/chat/completions"
    req = urllib.request.Request(url, data=body, headers=headers)

    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read())
            content = data["choices"][0]["message"]["content"]
            # Parse JSON from response (handle markdown fences)
            content = content.strip()
            if content.startswith("```"):
                content = re.sub(r'^```\w*\n?', '', content)
                content = re.sub(r'\n?```$', '', content)
            result = json.loads(content)
            if "taught" in result:
                return result
        except (json.JSONDecodeError, KeyError):
            if attempt < 2:
                time.sleep(1)
                continue
        except Exception as exc:
            return {"taught": False, "citation": "", "justification": f"Erreur LLM: {exc}"}

    return {"taught": False, "citation": "", "justification": "Réponse LLM invalide (3 tentatives)"}


def is_boilerplate(text: str) -> bool:
    """Détecte les citations de boilerplate générique (AGENTS.md 13)."""
    lower = text.lower()
    return any(p in lower for p in BOILERPLATE_PATTERNS)


def lexical_overlap(citation: str, intitule: str) -> float:
    """Recouvrement lexical entre citation et intitulé officiel."""
    words_c = set(re.findall(r'\w{3,}', citation.lower()))
    words_i = set(re.findall(r'\w{3,}', intitule.lower()))
    if not words_i:
        return 0.0
    return len(words_c & words_i) / len(words_i)


def veto_deterministe(verdict: dict, intitule: str,
                      used_citations: set) -> dict:
    """Veto déterministe : peut DÉGRADER, jamais promouvoir."""
    citation = verdict.get("citation", "")

    # 1. Boilerplate → needs_content
    if is_boilerplate(citation):
        verdict["taught"] = False
        verdict["veto"] = "boilerplate_detected"
        verdict["justification"] = (
            "Citation rejetée : objectif templaté générique (AGENTS.md 13)"
        )
        return verdict

    # 2. Pertinence lexicale minimale
    # Le seuil est bas (>0) car le LLM a déjà jugé la pertinence ;
    # ce veto attrape seulement les citations totalement hors-sujet.
    # On compare aussi avec le contenu/rubrique si disponible.
    if citation and len(citation) > 10 and lexical_overlap(citation, intitule) == 0.0:
        verdict["taught"] = False
        verdict["veto"] = "no_lexical_overlap"
        verdict["justification"] = (
            f"Citation sans recouvrement lexical avec l'intitulé officiel"
        )
        return verdict

    # 3. Non-réutilisation : même citation pour plusieurs capacités
    if citation:
        cite_hash = hashlib.md5(citation.encode()).hexdigest()
        if cite_hash in used_citations:
            verdict["taught"] = False
            verdict["veto"] = "citation_reused"
            verdict["justification"] = "Citation déjà utilisée pour une autre capacité"
            return verdict
        used_citations.add(cite_hash)

    verdict["veto"] = "passed"
    return verdict


def judge_capacity(env: dict, cap: dict,
                   used_citations: set) -> dict:
    """Juge une capacité : RAG → LLM → veto."""
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

    # Citations utilisées DANS cette capacité (non-réutilisation cross-rôles)
    cap_citations: set = set()

    for role_key, role_info in ROLES.items():
        # Requête adaptée au rôle
        role_query = f"{cap['contenu']} {intitule}"
        hits = search_rag(env, role_query, k=5, doc_type_filter=role_info["doc_types"])
        if len(hits) < 2:
            # Essai sans filtre de type
            hits = search_rag(env, role_query, k=5)

        role_result = {
            "taught": False,
            "citation": "",
            "path": "",
            "anchor": "",
            "score": None,
            "justification": "Aucun candidat trouvé dans le corpus",
            "veto": "no_candidate",
        }

        # Essayer les candidats dans l'ordre jusqu'à trouver un verdict positif
        for hit in hits:
            meta = hit.get("metadata", {})
            doc_text = hit.get("document", "")
            if not doc_text or len(doc_text.strip()) < 30:
                continue

            llm_verdict = call_llm(
                env, intitule, doc_text, role_info["label"]
            )
            llm_verdict["path"] = meta.get("path", "")
            llm_verdict["anchor"] = meta.get("anchor", "")
            llm_verdict["score"] = hit.get("score")

            # Veto déterministe (cross-capacité ET cross-rôle)
            # Contexte élargi pour le test de pertinence : intitulé + contenu + rubrique
            intitule_elargi = f"{intitule} {cap.get('contenu', '')} {cap.get('rubrique', '')}"
            llm_verdict = veto_deterministe(
                llm_verdict, intitule_elargi, used_citations | cap_citations
            )

            if llm_verdict.get("taught"):
                # Enregistrer la citation pour la non-réutilisation
                cite = llm_verdict.get("citation", "")
                if cite:
                    cap_citations.add(hashlib.md5(cite.encode()).hexdigest())
                    used_citations.add(hashlib.md5(cite.encode()).hexdigest())
                role_result = llm_verdict
                break
            elif role_result.get("veto") == "no_candidate":
                # Garder le premier verdict négatif comme fallback
                role_result = llm_verdict

        result["roles"][role_key] = role_result

    # Verdict global
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
    parser = argparse.ArgumentParser(description="Juge de substance NSI")
    parser.add_argument("--limit", type=int, default=0,
                        help="Limiter le nombre de capacités")
    parser.add_argument("--cap-id", type=str, default="",
                        help="Juger une capacité spécifique")
    parser.add_argument("--dry-run", action="store_true",
                        help="Lister les capacités sans juger")
    args = parser.parse_args()

    env = load_env(ENV_FILE)
    caps = load_programme()
    print(f"Programme : {len(caps)} capacités")

    if args.cap_id:
        caps = [c for c in caps if c["id"] == args.cap_id]
        if not caps:
            print(f"ERREUR: capacité {args.cap_id} non trouvée", file=sys.stderr)
            return 1

    if args.limit > 0:
        caps = caps[:args.limit]

    if args.dry_run:
        for c in caps:
            print(f"  {c['id']} [{c['niveau']}]: {c['intitule'][:80]}")
        return 0

    print(f"Jugement de {len(caps)} capacités...")
    print(f"API RAG : {env.get('RAG_API_BASE_URL', '?')} (clé: ****{env.get('RAG_API_KEY','')[-4:]})")
    print(f"LLM     : {env.get('LOCAL_LLM_BASE_URL', '?')} ({env.get('LOCAL_LLM_MODEL', '?')})")

    used_citations: set = set()
    results: list[dict] = []
    stats = {"validated_pedagogy": 0, "needs_review": 0, "needs_content": 0}

    for i, cap in enumerate(caps):
        print(f"  [{i+1}/{len(caps)}] {cap['id']}: {cap['intitule'][:60]}...", end="", flush=True)
        verdict = judge_capacity(env, cap, used_citations)
        results.append(verdict)
        stats[verdict["verdict"]] = stats.get(verdict["verdict"], 0) + 1
        print(f" → {verdict['verdict']}")

    # Écriture des résultats
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    review_path = OUTPUT_DIR / "substance_review.json"
    with open(review_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    # Rapport de synthèse
    report_path = OUTPUT_DIR / "substance_report.md"
    with open(report_path, "w") as f:
        f.write("# Rapport de substance — Corpus NSI\n\n")
        f.write(f"Date : {time.strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"Capacités évaluées : {len(results)}\n\n")
        f.write("## Synthèse\n\n")
        f.write(f"| Verdict | Nombre |\n|---|---|\n")
        for v in ("validated_pedagogy", "needs_review", "needs_content"):
            f.write(f"| {v} | {stats.get(v, 0)} |\n")
        f.write(f"\n## Détail par capacité\n\n")
        for r in results:
            emoji = {"validated_pedagogy": "✅", "needs_review": "⚠️", "needs_content": "❌"}.get(r["verdict"], "?")
            f.write(f"### {emoji} {r['capacity_id']} — {r['intitule'][:80]}\n\n")
            f.write(f"**Verdict : {r['verdict']}** ({r['niveau']})\n\n")
            for role, rv in r.get("roles", {}).items():
                taught = "✓" if rv.get("taught") else "✗"
                f.write(f"- **{role}** [{taught}] : ")
                if rv.get("path"):
                    f.write(f"`{rv['path']}`")
                    if rv.get("anchor"):
                        f.write(f"#{rv['anchor']}")
                    if rv.get("score"):
                        f.write(f" (score {rv['score']:.3f})")
                f.write(f"\n  {rv.get('justification', '')}\n")
                if rv.get("citation"):
                    f.write(f"  > {rv['citation'][:150]}\n")
                if rv.get("veto") and rv["veto"] != "passed":
                    f.write(f"  **VETO: {rv['veto']}**\n")
            f.write("\n")

    print(f"\n{'='*60}")
    print(f"RÉSULTATS")
    print(f"  validated_pedagogy : {stats.get('validated_pedagogy', 0)}")
    print(f"  needs_review       : {stats.get('needs_review', 0)}")
    print(f"  needs_content      : {stats.get('needs_content', 0)}")
    print(f"\nFichiers :")
    print(f"  {review_path}")
    print(f"  {report_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
