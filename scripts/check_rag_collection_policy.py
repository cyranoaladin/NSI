#!/usr/bin/env python3
"""Validate strict collection roles for NSI RAG usage.

Uses AST (not regex) to verify substance_judge.py policy compliance.
"""

from __future__ import annotations

import ast
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


def check_judge_collection_policy(source: str) -> list[str]:
    """AST-based policy checker for substance_judge.py.

    Verifies:
    1. No hardcoded collection literal in search body dicts (any quote style).
    2. RAG_COLLECTION resolved with default "nsi_corpus" (absent/wrong = fail).
    3. Barrier A present: is_internal_collection defined + INTERNAL_COVERAGE_COLLECTIONS.
    4. Barrier B present: is_internal_hit defined with isinstance(metadata, dict) guard,
       and called in search_rag.
    """
    errors: list[str] = []

    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        return [f"substance_judge.py: erreur de syntaxe ({exc})"]

    # --- Rule 1: No hardcoded collection literal in dict body ---
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            for key, val in zip(node.keys, node.values):
                if (
                    isinstance(key, ast.Constant)
                    and key.value == "collection"
                    and isinstance(val, ast.Constant)
                    and isinstance(val.value, str)
                ):
                    errors.append(
                        f"L{val.lineno}: collection littéral {val.value!r} "
                        f"dans un body — doit lire la config"
                    )

    # --- Rule 2: RAG_COLLECTION read with default "nsi_corpus" ---
    found_rag_col_read = False
    default_value: str | None = None
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        # Match env.get("RAG_COLLECTION", ...) or env.get("RAG_COLLECTION")
        func = node.func
        if isinstance(func, ast.Attribute) and func.attr == "get":
            args = node.args
            if args and isinstance(args[0], ast.Constant) and args[0].value == "RAG_COLLECTION":
                found_rag_col_read = True
                if len(args) >= 2 and isinstance(args[1], ast.Constant):
                    default_value = str(args[1].value)
                else:
                    default_value = None  # no default
    if not found_rag_col_read:
        errors.append("RAG_COLLECTION n'est pas lu depuis la config")
    elif default_value is None:
        errors.append("RAG_COLLECTION lu sans défaut — doit avoir défaut 'nsi_corpus'")
    elif default_value != "nsi_corpus":
        errors.append(f"RAG_COLLECTION défaut={default_value!r}, attendu 'nsi_corpus'")

    # --- Rule 3: Barrier A (is_internal_collection + INTERNAL_COVERAGE_COLLECTIONS) ---
    func_names = {
        node.name for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    assign_names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    assign_names.add(target.id)

    if "is_internal_collection" not in func_names:
        errors.append("is_internal_collection non définie (Barrière A absente)")
    if "INTERNAL_COVERAGE_COLLECTIONS" not in assign_names:
        errors.append("INTERNAL_COVERAGE_COLLECTIONS non définie (allowlist absente)")

    # --- Rule 4: Barrier B (is_internal_hit + isinstance guard + called in search_rag) ---
    if "is_internal_hit" not in func_names:
        errors.append("is_internal_hit non définie (Barrière B absente)")
    else:
        # Check isinstance(metadata, dict) guard inside is_internal_hit
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == "is_internal_hit":
                # Look for isinstance() call with "metadata" arg inside this function
                has_metadata_isinstance = False
                for child in ast.walk(node):
                    if (
                        isinstance(child, ast.Call)
                        and isinstance(child.func, ast.Name)
                        and child.func.id == "isinstance"
                        and len(child.args) >= 1
                        and isinstance(child.args[0], ast.Name)
                        and child.args[0].id == "metadata"
                    ):
                        has_metadata_isinstance = True
                        break
                if not has_metadata_isinstance:
                    errors.append("is_internal_hit sans garde isinstance(metadata, dict)")
                break

    # Check is_internal_hit is called inside search_rag
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == "search_rag":
            search_src = ast.dump(node)
            if "is_internal_hit" not in search_src:
                errors.append("is_internal_hit non appelée dans search_rag (Barrière B non câblée)")
            break

    # --- Rule negative: no rag_education query ---
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            for key, val in zip(node.keys, node.values):
                if (
                    isinstance(key, ast.Constant)
                    and key.value == "collection"
                    and isinstance(val, ast.Constant)
                    and val.value == "rag_education"
                ):
                    errors.append(
                        f"L{val.lineno}: requête rag_education pour preuves internes interdite"
                    )

    return errors


def load_catalog(path: Path) -> list[dict[str, Any]]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(payload, dict) or not isinstance(payload.get("sources"), list):
        return []
    return [row for row in payload["sources"] if isinstance(row, dict)]


def main() -> None:
    errors: list[str] = []
    judge_source = (ROOT / "scripts" / "substance_judge.py").read_text(encoding="utf-8")
    errors.extend(check_judge_collection_policy(judge_source))

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
