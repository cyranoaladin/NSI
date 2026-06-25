export PYTHONDONTWRITEBYTECODE=1

audit:
	python scripts/rebuild_inventory.py
	python scripts/check_metadata.py
	python scripts/check_links.py
	python scripts/check_no_private_data.py
	python scripts/check_no_placeholders_docs.py
	python scripts/check_no_placeholders_code.py
	python scripts/check_no_build_artifacts_in_index.py
	python scripts/check_required_sections.py
	python scripts/check_document_depth.py
	python scripts/check_qcm_schema.py
	python scripts/check_sequence_completeness.py
	python scripts/check_program_coverage.py
	python scripts/check_coverage_evidence.py
	python scripts/run_python_tests.py
	python scripts/check_quality_gates.py
