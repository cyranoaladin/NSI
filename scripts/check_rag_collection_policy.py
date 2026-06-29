#!/usr/bin/env python3
"""Validate strict collection roles for NSI RAG usage."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from _qa_common import ROOT, print_result


EXTERNAL_SOURCE_TYPES = {
    "officiel",
    "annale_publique",
    "ressource_pedagogique_ouverte",
    "drive_interne",
    "inspiration",
    "rejet",
}


def load_catalog(path: Path) -> list[dict[str, Any]]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(payload, dict) or not isinstance(payload.get("sources"), list):
        return []
    return [row for row in payload["sources"] if isinstance(row, dict)]


def main() -> None:
    errors: list[str] = []
    judge = (ROOT / "scripts" / "substance_judge.py").read_text(encoding="utf-8")
    if '"collection": "nsi_corpus"' not in judge:
        errors.append("substance_judge.py doit interroger nsi_corpus")
    if '"collection": "rag_education"' in judge:
        errors.append("substance_judge.py ne doit pas interroger rag_education pour les preuves internes")

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
