export PYTHONDONTWRITEBYTECODE=1

audit: audit-local

audit-local:
	python scripts/rebuild_inventory.py
	python scripts/check_git_clean.py
	python scripts/check_metadata.py
	python scripts/check_links.py
	python scripts/check_no_private_data.py
	python scripts/check_no_placeholders_docs.py
	python scripts/check_no_placeholders_code.py
	python scripts/cleanup_python_artifacts.py
	python scripts/check_no_build_artifacts_in_index.py
	python scripts/check_uploaded_archive_policy.py
	-python scripts/check_required_sections.py
	-python scripts/check_document_depth.py
	python scripts/check_qcm_schema.py
	-python scripts/check_document_style.py
	python scripts/check_progression_calendar_alignment.py
	python scripts/check_project_quarter_requirement.py
	python scripts/check_progression_project_consistency.py
	python scripts/check_monthly_load_balance.py
	python scripts/check_session_level_planning.py
	python scripts/check_session_duration_consistency.py
	python scripts/check_session_monthly_total.py
	python scripts/check_session_project_hours.py
	python scripts/check_session_week_calendar_consistency.py
	python scripts/check_session_specificity.py
	python scripts/check_session_referenced_files_exist.py
	python scripts/check_document_naming_conventions.py
	python scripts/check_first_batch_document_quality.py
	python scripts/check_evaluation_distribution.py
	python scripts/check_teacher_docs_depth.py
	python scripts/check_validated_documents_quality_gates.py
	python scripts/check_program_yaml_atomicity.py
	python scripts/check_build_reports_freshness.py
	python scripts/check_archive_portability.py
	python scripts/check_sequence_completeness.py
	python scripts/check_course_internal_coherence.py
	python scripts/check_td_corrige_alignment.py
	python scripts/check_tp_test_alignment.py
	python scripts/check_evaluation_bareme_alignment.py
	python scripts/check_learning_objectives_assessed.py
	python scripts/check_differentiation_quality.py
	python scripts/check_scientific_claims_review.py
	python scripts/check_program_capacity_evidence_depth.py
	python scripts/check_program_coverage.py
	python scripts/generate_qa_report.py
	python scripts/check_qa_report_freshness.py
	python scripts/check_manifest_source_integrity.py
	python scripts/check_teacher_corrections_alignment.py
	python scripts/check_coverage_evidence.py
	python scripts/run_python_tests.py
	python scripts/check_quality_gates.py

audit-source:
	python scripts/cleanup_python_artifacts.py
	python scripts/check_archive_portability.py
	python scripts/check_session_duration_consistency.py
	python scripts/check_session_monthly_total.py
	python scripts/check_session_project_hours.py
	python scripts/check_session_referenced_files_exist.py
	python scripts/check_document_naming_conventions.py
	python scripts/check_session_specificity.py
	python scripts/check_session_week_calendar_consistency.py
	python scripts/check_evaluation_distribution.py
	python scripts/check_metadata.py
	python scripts/check_links.py
	python scripts/check_no_private_data.py
	python scripts/check_no_placeholders_docs.py
	python scripts/check_no_placeholders_code.py
	python scripts/check_no_build_artifacts_in_index.py
	-python scripts/check_required_sections.py
	-python scripts/check_document_depth.py
	python scripts/check_qcm_schema.py
	-python scripts/check_document_style.py

package-audit:
	python scripts/cleanup_python_artifacts.py
	python scripts/build_source_archive.py
	python scripts/check_archive_portability.py

render-s01:
	python scripts/render_sequence.py premiere/sequences/s01_representation_donnees

release-audit:
	python scripts/cleanup_python_artifacts.py
	python scripts/check_git_clean.py
	python scripts/check_drive_mapping_release.py
	python scripts/check_no_needs_review_for_release.py
	python scripts/check_no_absent_coverage_for_release.py
	python scripts/check_no_teacher_content_in_student_export.py
	python scripts/check_validated_statuses.py
