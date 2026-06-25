#!/usr/bin/env python3
"""Aggregate quality checks without hiding individual failures."""

from __future__ import annotations

from pathlib import Path
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable

CHECKS = [
    "scripts/check_git_clean.py",
    "scripts/check_metadata.py",
    "scripts/check_links.py",
    "scripts/check_no_private_data.py",
    "scripts/check_no_placeholders_docs.py",
    "scripts/check_no_placeholders_code.py",
    "scripts/check_no_build_artifacts_in_index.py",
    "scripts/check_required_sections.py",
    "scripts/check_document_depth.py",
    "scripts/check_qcm_schema.py",
    "scripts/check_document_style.py",
    "scripts/check_python_quality.py",
    "scripts/check_sequence_completeness.py",
    "scripts/check_course_internal_coherence.py",
    "scripts/check_td_corrige_alignment.py",
    "scripts/check_tp_test_alignment.py",
    "scripts/check_evaluation_bareme_alignment.py",
    "scripts/check_learning_objectives_assessed.py",
    "scripts/check_differentiation_quality.py",
    "scripts/check_scientific_claims_review.py",
    "scripts/check_program_capacity_evidence_depth.py",
    "scripts/check_pedagogical_alignment.py",
    "scripts/check_bank_strategy.py",
    "scripts/check_drive_mapping.py",
    "scripts/check_coverage_evidence.py",
    "scripts/run_python_tests.py",
]


def main() -> None:
    failures: list[str] = []
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    for script in CHECKS:
        print(f"== {script} ==")
        result = subprocess.run([PYTHON, script], cwd=ROOT, env=env)
        if result.returncode != 0:
            failures.append(script)

    if failures:
        print("check_quality_gates: KO")
        for script in failures:
            print(f"- {script}")
        raise SystemExit(1)

    print("check_quality_gates: PASS")


if __name__ == "__main__":
    main()
