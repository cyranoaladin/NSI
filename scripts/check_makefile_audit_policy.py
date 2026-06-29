#!/usr/bin/env python3
"""Check Makefile audit targets against qa_gate_policy.md."""

from __future__ import annotations

import re
import sys
from pathlib import Path

SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(SCRIPT_ROOT))

from scripts import check_quality_gates  # noqa: E402
from scripts._qa_common import ROOT, print_result  # noqa: E402


MAKEFILE = ROOT / "Makefile"
POLICY = ROOT / "qa_gate_policy.md"


def target_body(text: str, target: str) -> str:
    match = re.search(rf"^{re.escape(target)}:\s*(.*?)\n(?=[A-Za-z0-9_.-]+:|\Z)", text, re.S | re.M)
    return match.group(1) if match else ""


def python_scripts(body: str) -> set[str]:
    scripts: set[str] = set()
    for match in re.finditer(r"(?:^|\s)(?:PYTHONDONTWRITEBYTECODE=1\s+)?(?:RAG_ENV_FILE=[^\s]+\s+)?-?python\s+(scripts/[^\s]+\.py)", body):
        scripts.add(match.group(1))
    return scripts


def documented_scripts(policy_text: str) -> set[str]:
    return set(re.findall(r"scripts/[A-Za-z0-9_./-]+\.py", policy_text))


def main() -> None:
    errors: list[str] = []
    text = MAKEFILE.read_text(encoding="utf-8")
    policy = POLICY.read_text(encoding="utf-8")
    if "\naudit: audit-core audit-metrics\n" not in text:
        errors.append("audit doit dépendre de audit-core audit-metrics")
    core = target_body(text, "audit-core")
    metrics = target_body(text, "audit-metrics")
    required = target_body(text, "rag-smoke-required")
    if not core:
        errors.append("cible audit-core absente")
    if not metrics:
        errors.append("cible audit-metrics absente")
    if "RAG_ENV_FILE=.env.rag.audit-core-missing python scripts/rag_smoke_test.py" not in core:
        errors.append("audit-core doit forcer le smoke RAG en mode clone-propre")
    if "python scripts/rag_smoke_test.py" not in required or "RAG_ENV_FILE" in required:
        errors.append("rag-smoke-required doit utiliser .env.rag réel")
    docs = documented_scripts(policy)
    for script in sorted(python_scripts(core)):
        if script not in docs:
            errors.append(f"{script}: gate audit-core non documenté dans qa_gate_policy.md")
    if "Divergence documentée check_quality_gates.py / audit-core" not in policy:
        quality_scripts = {" ".join(command) for command in check_quality_gates.CORE_CHECKS}
        core_scripts = python_scripts(core)
        missing_in_quality = {script for script in core_scripts if script not in quality_scripts}
        if missing_in_quality:
            errors.append(f"check_quality_gates.py diverge de audit-core: {sorted(missing_in_quality)}")
    print_result("check_makefile_audit_policy", errors)


if __name__ == "__main__":
    main()
