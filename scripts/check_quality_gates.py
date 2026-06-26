#!/usr/bin/env python3
"""Aggregate quality checks without hiding individual failures."""

from __future__ import annotations

from pathlib import Path
import os
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable

BLOCKING_CHECKS = [
    "scripts/check_git_clean.py",
    "scripts/check_metadata.py",
    "scripts/check_links.py",
    "scripts/check_no_private_data.py",
    "scripts/check_no_placeholders_docs.py",
    "scripts/check_no_placeholders_code.py",
    "scripts/check_no_build_artifacts_in_index.py",
    "scripts/check_uploaded_archive_policy.py",
    "scripts/check_no_global_archive_in_delivery_context.py",
    "scripts/check_qcm_schema.py",
    "scripts/check_qcm_contract_consistency.py",
    "scripts/check_progression_calendar_alignment.py",
    "scripts/check_project_quarter_requirement.py",
    "scripts/check_progression_project_consistency.py",
    "scripts/check_monthly_load_balance.py",
    "scripts/check_session_level_planning.py",
    "scripts/check_session_duration_consistency.py",
    "scripts/check_session_monthly_total.py",
    "scripts/check_session_project_hours.py",
    "scripts/check_session_week_calendar_consistency.py",
    "scripts/check_session_specificity.py",
    "scripts/check_session_referenced_files_exist.py",
    "scripts/check_missing_register_actionability.py",
    "scripts/check_missing_register_semantic_consistency.py",
    "scripts/check_register_no_hidden_operational_debt.py",
    "scripts/check_document_naming_conventions.py",
    "scripts/check_first_batch_document_quality.py",
    "scripts/check_first_batch_alignment.py",
    "scripts/check_first_batch_tp_assets.py",
    "scripts/check_support_substance.py",
    "scripts/check_no_line_padding.py",
    "scripts/check_tp_pedagogical_assets_runtime.py",
    "scripts/check_sequence_contracts.py",
    "scripts/check_local_drive_traceability.py",
    "scripts/check_drive_integration_plan.py",
    "scripts/check_drive_enrichment_traceability.py",
    "scripts/check_drive_enrichment_traceability_portable.py",
    "scripts/check_manifest_source_trace_consistency.py",
    "scripts/check_drive_trace_no_absolute_local_paths.py",
    "scripts/check_delivered_archive_exactly_source_clean.py",
    "scripts/check_no_sensitive_drive_in_source_clean.py",
    "scripts/check_ready_supports_required_sections.py",
    "scripts/check_ready_supports_depth.py",
    "scripts/check_ready_session_operationality.py",
    "scripts/check_course_sheets_coverage.py",
    "scripts/check_course_sheets_quality.py",
    "scripts/check_course_sheets_alignment.py",
    "scripts/check_course_sheets_substance.py",
    "scripts/check_course_sheet_linked_resources_exist.py",
    "scripts/check_course_sheets_no_template_abuse.py",
    "scripts/check_course_sheet_readiness.py",
    "scripts/check_course_sheet_readiness_strict.py",
    "scripts/check_linked_td_quality.py",
    "scripts/check_linked_td_substance.py",
    "scripts/check_linked_evaluation_quality.py",
    "scripts/check_linked_evaluation_substance.py",
    "scripts/check_no_operational_scope_hardcoding.py",
    "scripts/check_operational_supports_no_indicative_debt.py",
    "scripts/check_operational_readiness_quality_coupling.py",
    "scripts/check_evaluation_distribution.py",
    "scripts/check_teacher_docs_depth.py",
    "scripts/check_validated_documents_quality_gates.py",
    "scripts/check_program_yaml_atomicity.py",
    "scripts/check_build_reports_freshness.py",
    "scripts/check_archive_portability.py",
    "scripts/check_python_quality.py",
    "scripts/check_python_cache_stability.py",
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
    "scripts/check_drive_quarantine_privacy.py",
    "scripts/check_coverage_evidence.py",
    "scripts/check_no_coverage_from_sheets_only.py",
    "scripts/check_qa_report_freshness.py",
    "scripts/check_manifest_source_integrity.py",
    "scripts/check_teacher_corrections_alignment.py",
    "scripts/run_python_tests.py",
]

INDICATIVE_CHECKS = [
    "scripts/check_required_sections.py",
    "scripts/check_document_depth.py",
    "scripts/check_document_style.py",
]


def remove_python_caches() -> None:
    for path in ROOT.rglob("__pycache__"):
        if path.is_dir():
            shutil.rmtree(path)


def run_check(script: str, env: dict[str, str], indicative: bool = False) -> int:
    suffix = " (indicatif)" if indicative else ""
    print(f"== {script}{suffix} ==")
    result = subprocess.run([PYTHON, script], cwd=ROOT, env=env)
    return result.returncode


def main() -> None:
    failures: list[str] = []
    indicative_failures: list[str] = []
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    remove_python_caches()
    try:
        for script in BLOCKING_CHECKS:
            if run_check(script, env) != 0:
                failures.append(script)
        for script in INDICATIVE_CHECKS:
            if run_check(script, env, indicative=True) != 0:
                indicative_failures.append(script)
        if failures:
            print("check_quality_gates: KO")
            for script in failures:
                print(f"- {script}")
            raise SystemExit(1)
        if indicative_failures:
            print("Gates indicatifs non bloquants en échec:")
            for script in indicative_failures:
                print(f"- {script}")
        print("check_quality_gates: PASS")
    finally:
        remove_python_caches()

if __name__ == "__main__":
    main()
