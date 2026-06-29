export PYTHONDONTWRITEBYTECODE=1
DELIVERED_ARCHIVE ?= dist/source_clean.tar.gz

audit: audit-core audit-metrics

audit-idempotence:
	$(MAKE) audit
	test -z "$$(git status --short)"
	$(MAKE) audit
	test -z "$$(git status --short)"

generate-reports:
	python scripts/rebuild_inventory.py
	python scripts/check_program_coverage.py
	python scripts/generate_pedagogical_indexes.py
	python scripts/generate_qa_report.py
	python scripts/rebuild_inventory.py

check-generated-freshness:
	python scripts/check_build_reports_freshness.py
	python scripts/check_qa_report_freshness.py
	python scripts/check_manifest_source_integrity.py

audit-core:
	python scripts/check_git_clean.py
	python scripts/check_audit_folder_policy.py
	python scripts/check_content_tree_policy.py
	python scripts/check_rag_config.py
	RAG_ENV_FILE=.env.rag.audit-core-missing python scripts/rag_smoke_test.py
	python scripts/check_agents_governance.py
	python scripts/check_skills_governance.py
	python scripts/check_program_coverage.py
	python scripts/check_coverage_gap_action_plan.py
	python scripts/check_sources_catalog.py
	python scripts/generate_pedagogical_indexes.py
	python scripts/check_pedagogical_indexes.py
	python scripts/check_substance_anchors.py
	python scripts/check_contract_substance_quality.py
	python scripts/check_differentiation_distinctness.py
	python scripts/check_rendered_unit_artifacts.py --unit P05
	python scripts/check_rendered_unit_artifacts.py --unit T10
	python scripts/check_no_private_data.py
	python scripts/check_no_committed_secrets.py
	python scripts/check_no_placeholders_docs.py
	python scripts/check_no_placeholders_code.py
	python scripts/run_python_tests.py

audit-metrics:
	-python scripts/check_required_sections.py
	-python scripts/check_document_depth.py
	-python scripts/check_document_style.py
	python scripts/check_full_sequence_resource_matrix.py
	python scripts/check_full_notional_resource_matrix.py
	python scripts/check_official_program_capacity_coverage_matrix.py
	python scripts/check_session_level_planning.py
	python scripts/check_session_duration_consistency.py
	python scripts/check_session_monthly_total.py
	python scripts/check_session_project_hours.py
	python scripts/check_session_week_calendar_consistency.py
	python scripts/check_session_specificity.py

audit-local:
	python scripts/check_git_clean.py
	python scripts/check_audit_folder_policy.py
	python scripts/check_content_tree_policy.py
	python scripts/check_gate_policy_consistency.py
	python scripts/check_metadata.py
	python scripts/check_links.py
	python scripts/check_no_private_data.py
	python scripts/check_no_committed_secrets.py
	python scripts/check_no_placeholders_docs.py
	python scripts/check_no_placeholders_code.py
	python scripts/cleanup_python_artifacts.py
	python scripts/check_no_build_artifacts_in_index.py
	python scripts/check_uploaded_archive_policy.py
	python scripts/check_no_global_archive_in_delivery_context.py
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
	python scripts/check_missing_register_actionability.py
	python scripts/check_missing_register_semantic_consistency.py
	python scripts/check_register_no_hidden_operational_debt.py
	python scripts/check_document_naming_conventions.py
	python scripts/check_first_batch_document_quality.py
	python scripts/check_first_batch_alignment.py
	python scripts/check_first_batch_tp_assets.py
	python scripts/check_support_substance.py
	python scripts/check_no_line_padding.py
	python scripts/check_full_sequence_resource_matrix.py
	python scripts/check_full_notional_resource_matrix.py
	python scripts/check_official_program_capacity_coverage_matrix.py
	python scripts/check_program_coverage.py
	python scripts/check_capacity_status_ladder.py
	python scripts/check_course_explanatory_quality.py
	python scripts/check_sequence_pedagogical_coherence.py
	python scripts/check_paper_tp_justification.py
	MAX_EXECUTABLE_TP_OPPORTUNITIES=8 python scripts/check_tp_executable_opportunity.py
	python scripts/check_session_to_resource_alignment.py
	python scripts/check_session_classroom_operationality.py
	python scripts/check_human_review_register.py
	python scripts/check_human_review_wave_plan.py
	python scripts/check_sql_query_result_consistency.py
	python scripts/check_graph_algorithm_trace_consistency.py
	python scripts/check_tree_bst_invariant_consistency.py
	python scripts/check_network_packet_trace_consistency.py
	python scripts/check_dynamic_programming_recurrence_consistency.py
	python scripts/check_boyer_moore_trace_consistency.py
	python scripts/check_generated_template_residue.py
	python scripts/check_question_capacity_alignment.py
	python scripts/check_support_pedagogical_depth.py
	python scripts/check_substance_anchors.py
	python scripts/check_contract_substance_quality.py
	python scripts/check_differentiation_distinctness.py
	python scripts/check_rendered_unit_artifacts.py --unit P05
	python scripts/check_rendered_unit_artifacts.py --unit T10
	python scripts/check_session_operationalization_plan.py
	python scripts/check_sequence_pack_consistency.py
	python scripts/check_csv_numeric_fields_are_parseable.py
	python scripts/check_p05_pipeline_consistency.py
	python scripts/check_p05_semantic_consistency.py
	python scripts/check_p05_expected_outputs_are_explicit.py
	python scripts/check_course_sheet_exercise_answer_count.py
	python scripts/check_no_duplicate_capacity_lines.py
	python scripts/check_p04_key_consistency.py
	python scripts/check_t18_trace_table_quality.py
	python scripts/check_paper_tp_contract.py
	python scripts/check_no_token_only_validation.py
	python scripts/check_no_generic_scaffold_overuse.py
	python scripts/check_student_supports_no_scaffold_language.py
	python scripts/check_corrected_answers_are_concrete.py
	python scripts/check_tp_text_asset_alignment.py
	python scripts/check_sequence_capacity_alignment.py
	timeout 90 python -u scripts/check_tp_pedagogical_assets_runtime.py
	python scripts/check_sequence_contracts.py
	python scripts/check_local_drive_traceability.py
	python scripts/check_drive_integration_plan.py
	python scripts/check_drive_action_plan_completeness.py
	python scripts/check_drive_enrichment_traceability.py
	python scripts/check_ready_supports_required_sections.py
	python scripts/check_ready_supports_depth.py
	python scripts/check_ready_session_operationality.py
	python scripts/check_course_sheets_coverage.py
	python scripts/check_course_sheets_quality.py
	python scripts/check_course_sheets_alignment.py
	python scripts/check_course_sheets_substance.py
	python scripts/check_course_sheet_linked_resources_exist.py
	python scripts/check_course_sheets_no_template_abuse.py
	python scripts/check_course_sheet_readiness.py
	python scripts/check_course_sheet_readiness_strict.py
	python scripts/check_linked_td_quality.py
	python scripts/check_linked_td_substance.py
	python scripts/check_linked_evaluation_quality.py
	python scripts/check_linked_evaluation_substance.py
	python scripts/check_no_operational_scope_hardcoding.py
	python scripts/check_operational_supports_no_indicative_debt.py
	python scripts/check_operational_readiness_quality_coupling.py
	python scripts/check_evaluation_distribution.py
	python scripts/check_teacher_docs_depth.py
	python scripts/check_validated_documents_quality_gates.py
	python scripts/check_program_yaml_atomicity.py
	$(MAKE) check-generated-freshness
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
	python scripts/check_teacher_corrections_alignment.py
	python scripts/check_coverage_evidence.py
	python scripts/check_no_coverage_from_sheets_only.py
	python scripts/run_python_tests.py
	python scripts/check_quality_gates.py
	python scripts/check_git_clean.py

audit-source:
	python scripts/cleanup_python_artifacts.py
	python scripts/check_archive_portability.py
	python scripts/check_session_duration_consistency.py
	python scripts/check_session_monthly_total.py
	python scripts/check_session_project_hours.py
	python scripts/check_session_referenced_files_exist.py
	python scripts/check_missing_register_actionability.py
	python scripts/check_missing_register_semantic_consistency.py
	python scripts/check_register_no_hidden_operational_debt.py
	python scripts/check_document_naming_conventions.py
	python scripts/check_session_specificity.py
	python scripts/check_session_week_calendar_consistency.py
	python scripts/check_evaluation_distribution.py
	python scripts/check_metadata.py
	python scripts/check_links.py
	python scripts/check_no_private_data.py
	python scripts/check_no_committed_secrets.py
	python scripts/check_no_placeholders_docs.py
	python scripts/check_no_placeholders_code.py
	python scripts/check_no_build_artifacts_in_index.py
	-python scripts/check_required_sections.py
	-python scripts/check_document_depth.py
	python scripts/check_qcm_schema.py
	-python scripts/check_document_style.py

audit-extracted-source:
	@if test -d .git; then PYTHONDONTWRITEBYTECODE=1 python scripts/run_audit_extracted_source.py; else $(MAKE) audit-extracted-source-local; fi

audit-extracted-source-local:
	python scripts/cleanup_python_artifacts.py
	python scripts/check_audit_folder_policy.py
	python scripts/check_content_tree_policy.py
	python scripts/check_gate_policy_consistency.py
	python scripts/check_metadata.py
	python scripts/check_qcm_schema.py
	timeout 30 python scripts/check_session_referenced_files_exist.py
	timeout 30 python scripts/check_first_batch_document_quality.py
	timeout 30 python scripts/check_first_batch_alignment.py
	python scripts/check_first_batch_tp_assets.py
	timeout 30 python scripts/check_support_substance.py
	python scripts/check_no_line_padding.py
	timeout 30 python scripts/check_full_sequence_resource_matrix.py
	timeout 30 python scripts/check_full_notional_resource_matrix.py
	timeout 30 python scripts/check_official_program_capacity_coverage_matrix.py
	timeout 30 python scripts/check_program_coverage.py
	timeout 30 python scripts/check_capacity_status_ladder.py
	timeout 30 python scripts/check_course_explanatory_quality.py
	timeout 30 python scripts/check_sequence_pedagogical_coherence.py
	timeout 30 python scripts/check_paper_tp_justification.py
	MAX_EXECUTABLE_TP_OPPORTUNITIES=8 timeout 30 python scripts/check_tp_executable_opportunity.py
	timeout 30 python scripts/check_session_to_resource_alignment.py
	timeout 30 python scripts/check_session_classroom_operationality.py
	timeout 30 python scripts/check_human_review_register.py
	timeout 30 python scripts/check_human_review_wave_plan.py
	python scripts/check_sql_query_result_consistency.py
	python scripts/check_graph_algorithm_trace_consistency.py
	python scripts/check_tree_bst_invariant_consistency.py
	python scripts/check_network_packet_trace_consistency.py
	python scripts/check_dynamic_programming_recurrence_consistency.py
	python scripts/check_boyer_moore_trace_consistency.py
	python scripts/check_generated_template_residue.py
	python scripts/check_question_capacity_alignment.py
	timeout 30 python scripts/check_support_pedagogical_depth.py
	timeout 30 python scripts/check_substance_anchors.py
	timeout 30 python scripts/check_contract_substance_quality.py
	timeout 30 python scripts/check_differentiation_distinctness.py
	timeout 30 python scripts/check_rendered_unit_artifacts.py --unit P05
	timeout 30 python scripts/check_session_operationalization_plan.py
	python scripts/check_sequence_pack_consistency.py
	python scripts/check_csv_numeric_fields_are_parseable.py
	python scripts/check_p05_pipeline_consistency.py
	python scripts/check_p05_semantic_consistency.py
	python scripts/check_p05_expected_outputs_are_explicit.py
	python scripts/check_course_sheet_exercise_answer_count.py
	python scripts/check_no_duplicate_capacity_lines.py
	python scripts/check_p04_key_consistency.py
	python scripts/check_t18_trace_table_quality.py
	python scripts/check_paper_tp_contract.py
	python scripts/check_no_token_only_validation.py
	python scripts/check_no_generic_scaffold_overuse.py
	python scripts/check_student_supports_no_scaffold_language.py
	python scripts/check_corrected_answers_are_concrete.py
	python scripts/check_tp_text_asset_alignment.py
	python scripts/check_sequence_capacity_alignment.py
	timeout 90 python -u scripts/check_tp_pedagogical_assets_runtime.py
	python scripts/check_sequence_contracts.py
	python scripts/check_drive_enrichment_traceability_portable.py
	python scripts/check_drive_action_plan_completeness.py
	python scripts/check_drive_trace_no_absolute_local_paths.py
	timeout 30 python scripts/check_ready_supports_required_sections.py
	timeout 30 python scripts/check_ready_supports_depth.py
	timeout 30 python scripts/check_ready_session_operationality.py
	python scripts/check_course_sheets_coverage.py
	python scripts/check_course_sheets_quality.py
	python scripts/check_course_sheets_alignment.py
	python scripts/check_course_sheets_substance.py
	python scripts/check_course_sheet_linked_resources_exist.py
	python scripts/check_course_sheets_no_template_abuse.py
	python scripts/check_course_sheet_readiness.py
	python scripts/check_course_sheet_readiness_strict.py
	python scripts/check_linked_td_quality.py
	python scripts/check_linked_td_substance.py
	python scripts/check_linked_evaluation_quality.py
	python scripts/check_linked_evaluation_substance.py
	python scripts/check_no_operational_scope_hardcoding.py
	python scripts/check_operational_supports_no_indicative_debt.py
	timeout 30 python scripts/check_operational_readiness_quality_coupling.py
	python scripts/check_no_private_data.py
	python scripts/check_no_placeholders_docs.py
	python scripts/check_no_build_artifacts_in_index.py
	python scripts/check_no_sensitive_drive_in_source_clean.py
	python scripts/check_no_coverage_from_sheets_only.py

package-audit:
	python scripts/cleanup_python_artifacts.py
	python scripts/build_source_archive.py
	python scripts/check_packaging_mode.py
	python scripts/check_archive_portability.py
	python scripts/check_no_sensitive_drive_in_source_clean.py
	python scripts/check_no_global_archive_in_delivery_context.py

verify-delivery-archive:
	DELIVERED_ARCHIVE="$(DELIVERED_ARCHIVE)" python scripts/check_delivered_archive_exactly_source_clean.py

deliver-pedagogical-archive:
	python scripts/build_source_archive.py
	python scripts/check_packaging_mode.py
	DELIVERED_ARCHIVE=dist/source_clean.tar.gz python scripts/check_delivered_archive_exactly_source_clean.py
	python scripts/check_no_global_archive_in_delivery_context.py
	@echo "LIVRABLE_PEDAGOGIQUE=dist/source_clean.tar.gz"

deliver-source-zip:
	python scripts/build_source_zip.py
	@echo "ZIP_EXPLOITABLE=dist/nsi-enseignement_source_clean.zip"

render-s01:
	python scripts/render_sequence.py premiere/sequences/s01_representation_donnees

render-unit:
	python scripts/render_unit.py --unit "$(U)"

judge:
	test -n "$(U)"
	python scripts/substance_judge.py --unit "$(U)" --level premiere --offline-fixture "tests/fixtures/substance_judge/$(U).json" --output "01_build_reports/$(U)_substance_review.json"
	python scripts/check_substance_anchors.py "01_build_reports/$(U)_substance_review.json" --repo-root .

render-substance-report:
	test -n "$(V)"
	mkdir -p 01_build_reports/substance_reports
	python scripts/render_substance_report.py --verdict "$(V)" --repo-root . --out-md 01_build_reports/substance_reports/$$(basename "$(V)" .json).md --out-html 01_build_reports/substance_reports/$$(basename "$(V)" .json).html

release-audit:
	python scripts/cleanup_python_artifacts.py
	python scripts/check_git_clean.py
	python scripts/check_drive_mapping_release.py
	python scripts/check_no_needs_review_for_release.py
	python scripts/check_no_absent_coverage_for_release.py
	python scripts/check_no_teacher_content_in_student_export.py
	python scripts/check_validated_statuses.py

pre-release-audit:
	python scripts/check_git_clean.py
	python scripts/check_quality_gates.py
	python scripts/check_archive_portability.py
	@echo "qualité interne contrôlée"
	@echo "publication bloquée tant que make release-audit échoue"
