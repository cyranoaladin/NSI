#!/usr/bin/env python3
"""Reject fixed prefix scopes in operational-support QA checks."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import ast
import re

from _qa_common import ROOT

CHECKS = [
    "scripts/check_linked_td_quality.py",
    "scripts/check_linked_evaluation_quality.py",
    "scripts/check_operational_supports_no_indicative_debt.py",
]


@dataclass
class ScopeHardcodingResult:
    errors: list[str] = field(default_factory=list)
    checked_files: int = 0


def contains_fixed_prefix_set(tree: ast.AST) -> bool:
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            targets = [target.id for target in node.targets if isinstance(target, ast.Name)]
            if any(name in {"TARGET_PREFIXES", "TARGET_SEQUENCES"} for name in targets):
                return True
        if isinstance(node, ast.For) and isinstance(node.iter, ast.Call):
            source = ast.unparse(node.iter)
            if re.search(r"range\(\s*\d+\s*,\s*\d+\s*\)", source) and re.search(r"[PT]\{|\bP\b|\bT\b", source):
                return True
    return False


def analyze_no_operational_scope_hardcoding(
    root: Path = ROOT,
    script_paths: list[Path] | None = None,
) -> ScopeHardcodingResult:
    result = ScopeHardcodingResult()
    paths = script_paths or [root / relative for relative in CHECKS]
    for path in paths:
        result.checked_files += 1
        text = path.read_text(encoding="utf-8", errors="replace")
        try:
            tree = ast.parse(text)
        except SyntaxError as exc:
            result.errors.append(f"{path}: syntaxe Python invalide -> {exc}")
            continue
        if contains_fixed_prefix_set(tree):
            result.errors.append(f"{path}: périmètre opérationnel codé en dur via TARGET_PREFIXES/TARGET_SEQUENCES")
        if re.search(r"path\.name\[:3\]\s+not\s+in", text):
            result.errors.append(f"{path}: filtre par préfixe de nom interdit pour supports opérationnels")
    return result


def main() -> int:
    result = analyze_no_operational_scope_hardcoding()
    if result.errors:
        print("check_no_operational_scope_hardcoding: KO")
        for error in result.errors[:80]:
            print(f"- {error}")
        return 1
    print(f"check_no_operational_scope_hardcoding: PASS ({result.checked_files} scripts)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
