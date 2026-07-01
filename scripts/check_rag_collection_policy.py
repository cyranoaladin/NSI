#!/usr/bin/env python3
"""Validate strict collection roles for NSI RAG usage."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml

from scripts._qa_common import ROOT, print_result
EXTERNAL_SOURCE_TYPES = {
    "officiel",
    "annale_publique",
    "ressource_pedagogique_ouverte",
    "drive_interne",
    "inspiration",
    "rejet",
}
# Collection literals that must NEVER appear hardcoded in search bodies.
HARDCODED_COLLECTIONS = {
    "nsi_corpus", "nsi_corpus_v2", "rag_education", "rag_francais_premiere",
    "rag_maths_premiere", "rag_math_correction", "rag_divers",
    "ressources_pedagogiques_terminale",
}
def check_judge_collection_policy(judge_text: str) -> list[str]:
    """Check substance_judge.py collection routing policy.

    Rules:
    - No hardcoded collection literal in search body dicts.
    - Collection must come from config (RAG_COLLECTION / env).
    - Default must be "nsi_corpus" (the KIND).
    - Must NOT query rag_education for internal proofs.
    """
    errors: list[str] = []

    # Find all "collection": "..." patterns in the judge source
    hardcoded = re.findall(r'"collection"\s*:\s*"([^"]+)"', judge_text)
    for lit in hardcoded:
        errors.append(
            f"substance_judge.py hardcode collection littéral '{lit}' "
            f"dans un body de recherche — doit lire la config"
        )

    # Verify config-based resolution exists (env.get("RAG_COLLECTION", ...))
    if 'RAG_COLLECTION' not in judge_text:
        errors.append(
            "substance_judge.py ne lit pas RAG_COLLECTION depuis la config"
        )

    # Verify default is nsi_corpus
    default_match = re.search(
        r'env\.get\(["\']RAG_COLLECTION["\'],\s*["\'](\w+)["\']',
        judge_text,
    )
    if default_match and default_match.group(1) != "nsi_corpus":
        errors.append(
            f"substance_judge.py défaut RAG_COLLECTION={default_match.group(1)}, "
            f"attendu nsi_corpus"
        )

    return errors
def load_catalog(path: Path) -> list[dict[str, Any]]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(payload, dict) or not isinstance(payload.get("sources"), list):
        return []
    return [row for row in payload["sources"] if isinstance(row, dict)]
def main() -> None:
    errors: list[str] = []
    judge_text = (ROOT / "scripts" / "substance_judge.py").read_text(encoding="utf-8")
    errors.extend(check_judge_collection_policy(judge_text))

    coverage = (ROOT / "coverage.md").read_text(encoding="utf-8", errors="replace")
    if "rag_education" in coverage:
        errors.append("coverage.md ne doit jamais citer rag_education comme preuve interne")

    config = yaml.safe_load((ROOT / "rag_config.example.yml").read_text(encoding="utf-8")) or {}
    collections = config.get("collections", {}) if isinstance(config, dict) else {}
    rag_education = collections.get("rag_education", {}) if isinstance(collections, dict) else {}
    if "inspiration" not in str(rag_education).lower():
        errors.append("rag_education doit être décrit comme inspiration uniquement")

    catalog_path = ROOT / "sources_catalog.yml"
    if catalog_path.exists():
        for row in load_catalog(catalog_path):
            identifier = str(row.get("id") or row.get("title") or "?")
            if row.get("rag_collection") == "nsi_corpus" and row.get("source_type") in EXTERNAL_SOURCE_TYPES:
                errors.append(f"{identifier}: source externe interdite dans nsi_corpus")
            if row.get("source_type") == "drive_interne" and row.get("rag_collection") != "rag_education":
                errors.append(f"{identifier}: Documents_DRIVE doit rester rag_education ou rejet")
    print_result("check_rag_collection_policy", errors)
if __name__ == "__main__":
    main()
