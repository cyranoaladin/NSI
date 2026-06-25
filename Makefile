export PYTHONDONTWRITEBYTECODE=1

audit:
	python scripts/rebuild_inventory.py
	python scripts/check_git_clean.py
	python scripts/check_metadata.py
	python scripts/check_links.py
	python scripts/check_no_private_data.py
	python scripts/check_no_placeholders_docs.py
	python scripts/check_no_placeholders_code.py
	python scripts/check_no_build_artifacts_in_index.py
	python scripts/check_required_sections.py
	python scripts/check_document_depth.py
	python scripts/check_qcm_schema.py
	python scripts/check_document_style.py
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
	python scripts/check_coverage_evidence.py
	python scripts/run_python_tests.py
	python scripts/check_quality_gates.py

release-audit:
	python scripts/check_git_clean.py
	python scripts/check_drive_mapping_release.py
	python scripts/check_no_needs_review_for_release.py
	python scripts/check_no_absent_coverage_for_release.py
	python scripts/check_no_teacher_content_in_student_export.py
	python scripts/check_validated_statuses.py
