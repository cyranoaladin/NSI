#!/usr/bin/env python3
"""Smoke test : vérifie la connectivité RAG (search via API publique) et LLM.

Lit les variables depuis .env.rag (à la racine du dépôt nsi-enseignement).
N'affiche jamais de secret — uniquement des résumés de réponse.
Échoue proprement avec un message clair si une variable manque.

Prérequis réseau :
  - L'API RAG (/search) est publique (HTTPS) : aucun tunnel nécessaire.
    L'embedding est fait côté serveur par l'API.
  - Ollama (embedding direct, LLM) est en loopback sur le serveur.
    Pour les tests LLM, un tunnel SSH est nécessaire :
      ssh -L 11434:127.0.0.1:11434 root@88.99.254.59
    Sans tunnel, le test LLM est sauté avec un message explicite.
"""
from __future__ import annotations

import json
import sys
import urllib.request
import urllib.error
from pathlib import Path

ENV_FILE = Path(__file__).resolve().parent.parent / ".env.rag"

# Seules les variables pour l'API publique sont obligatoires.
# LLM et embedding direct sont optionnels (tunnel SSH).
REQUIRED_VARS = [
    "RAG_BACKEND",
    "RAG_API_BASE_URL",
    "RAG_API_KEY",
    "RAG_COLLECTION",
    "RAG_VECTOR_DIM",
]


def load_env(path: Path) -> dict[str, str]:
    """Parse un fichier .env basique (KEY=VALUE, commentaires ignorés)."""
    env: dict[str, str] = {}
    if not path.exists():
        print(f"ERREUR: fichier {path} introuvable.", file=sys.stderr)
        print("Copiez .env.rag.example vers .env.rag et remplissez les valeurs.",
              file=sys.stderr)
        sys.exit(1)
    for line in path.read_text().splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if "=" not in stripped:
            continue
        key, _, value = stripped.partition("=")
        env[key.strip()] = value.strip()
    return env


def check_required(env: dict[str, str]) -> None:
    missing = [v for v in REQUIRED_VARS if not env.get(v)]
    if missing:
        print("ERREUR: variables manquantes dans .env.rag :", file=sys.stderr)
        for m in missing:
            print(f"  - {m}", file=sys.stderr)
        sys.exit(1)


def mask(secret: str) -> str:
    """Masque un secret en ne montrant que les 4 derniers caractères."""
    if len(secret) <= 4:
        return "****"
    return f"****{secret[-4:]}"


def test_search(env: dict[str, str]) -> bool:
    """Recherche top-3 dans la collection via l'API publique (embedding côté serveur)."""
    print("\n[1/2] Test recherche RAG (API publique, embedding côté serveur)...")
    url = env["RAG_API_BASE_URL"]
    body = json.dumps({
        "q": "parcours arbre binaire ordre infixe",
        "collection": env["RAG_COLLECTION"],
        "k": 3,
        "include_documents": False,
    }).encode()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {env['RAG_API_KEY']}",
    }
    req = urllib.request.Request(url, data=body, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as exc:
        print(f"  ÉCHEC: HTTP {exc.code} — {exc.reason}", file=sys.stderr)
        if exc.code == 401:
            print("  Le token RAG_API_KEY est invalide ou a été révoqué.",
                  file=sys.stderr)
        return False
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        print(f"  ÉCHEC: impossible de joindre {url} — {exc}", file=sys.stderr)
        return False
    hits = data.get("hits", [])
    print(f"  Collection : {data.get('collection', '?')}")
    print(f"  Résultats  : {len(hits)}")
    for i, hit in enumerate(hits):
        meta = hit.get("metadata", {})
        score = hit.get("score")
        score_str = f"{score:.4f}" if isinstance(score, (int, float)) else str(score)
        print(f"  [{i+1}] score={score_str}  "
              f"source={meta.get('source', '?')}  "
              f"chunk={meta.get('chunk_index', '?')}  "
              f"type={meta.get('type_ressource', meta.get('document_type', '?'))}")
    if not hits:
        print("  ATTENTION: aucun résultat retourné.", file=sys.stderr)
        return False
    return True


def test_llm(env: dict[str, str]) -> bool:
    """Envoie une complétion courte au modèle LLM retenu (nécessite tunnel SSH)."""
    llm_url = env.get("LOCAL_LLM_BASE_URL", "")
    llm_model = env.get("LOCAL_LLM_MODEL", "")
    if not llm_url or not llm_model:
        print("\n[2/2] Test LLM : SAUTÉ (LOCAL_LLM_BASE_URL ou LOCAL_LLM_MODEL non défini)")
        return True  # pas un échec, c'est optionnel
    print(f"\n[2/2] Test LLM locale ({llm_model})...")
    print(f"  URL : {llm_url}")
    url = f"{llm_url}/chat/completions"
    body = json.dumps({
        "model": llm_model,
        "messages": [{"role": "user",
                      "content": "Réponds en une phrase : qu'est-ce qu'un arbre binaire ?"}],
        "temperature": 0,
    }).encode()
    headers = {"Content-Type": "application/json"}
    api_key = env.get("LOCAL_LLM_API_KEY", "")
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    req = urllib.request.Request(url, data=body, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read())
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        print(f"  ÉCHEC: impossible de joindre {url} — {exc}", file=sys.stderr)
        print("  Prérequis : tunnel SSH actif vers le serveur.", file=sys.stderr)
        print("  Commande : ssh -L 11434:127.0.0.1:11434 root@88.99.254.59",
              file=sys.stderr)
        return False
    answer = data["choices"][0]["message"]["content"]
    print(f"  Modèle  : {llm_model}")
    print(f"  Réponse : {answer[:200]}")
    return True


def main() -> None:
    print(f"Smoke test RAG+LLM — fichier : {ENV_FILE}")
    env = load_env(ENV_FILE)
    check_required(env)
    print(f"Backend  : {env['RAG_BACKEND']}")
    print(f"API      : {env['RAG_API_BASE_URL']}  (clé : {mask(env['RAG_API_KEY'])})")
    llm_url = env.get("LOCAL_LLM_BASE_URL", "(non défini)")
    llm_model = env.get("LOCAL_LLM_MODEL", "(non défini)")
    print(f"LLM      : {llm_url}  modèle={llm_model}")

    ok = True
    ok = test_search(env) and ok
    ok = test_llm(env) and ok

    if ok:
        print("\n--- Tous les tests ont réussi.")
    else:
        print("\n--- ÉCHEC: certains tests ont échoué.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
