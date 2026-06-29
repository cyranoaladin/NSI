from __future__ import annotations

import csv
import os
import subprocess
import sys
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_script(*args: str, extra_env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)
    return subprocess.run(
        [sys.executable, *args],
        cwd=ROOT,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=120,
    )


def env_example_map() -> dict[str, str]:
    values: dict[str, str] = {}
    for line in (ROOT / ".env.rag.example").read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, _, value = stripped.partition("=")
        values[key] = value
    return values


def absent_capacity_ids() -> set[str]:
    ids: set[str] = set()
    for line in (ROOT / "coverage.md").read_text(encoding="utf-8").splitlines():
        if "| absent |" not in line:
            continue
        columns = [column.strip() for column in line.strip().strip("|").split("|")]
        if len(columns) >= 4:
            ids.add(columns[3].split(" - ", 1)[0].strip())
    return ids


def test_rag_env_example_uses_internal_corpus_without_real_secret() -> None:
    values = env_example_map()

    assert values["RAG_BACKEND"] == "chroma"
    assert values["RAG_API_BASE_URL"] == "https://rag-api.nexusreussite.academy/search"
    assert values["RAG_API_KEY"] == ""
    assert values["RAG_COLLECTION"] == "nsi_corpus"
    assert values["RAG_DISTANCE"] == "cosine"
    assert values["RAG_VECTOR_DIM"] == "768"
    assert values["EMBEDDING_MODEL"] == "nomic-embed-text"
    assert values["LOCAL_LLM_ENGINE"] == "ollama"
    assert values["LOCAL_LLM_MODEL"] == "qwen2.5:7b"
    assert values["RAG_SSH_HOST"] == "88.99.254.59"
    assert values["RAG_SSH_USER"] == "root"
    assert ".env.rag" in (ROOT / ".gitignore").read_text(encoding="utf-8")


def test_rag_config_and_smoke_scripts_are_safe_without_local_config() -> None:
    config_result = run_script("scripts/check_rag_config.py")
    assert config_result.returncode == 0, config_result.stdout

    smoke_result = run_script(
        "scripts/rag_smoke_test.py",
        extra_env={"RAG_ENV_FILE": str(ROOT / ".env.rag.missing-for-test")},
    )
    assert smoke_result.returncode == 0, smoke_result.stdout
    assert "RAG_SMOKE_TEST_SKIPPED_NO_CONFIG" in smoke_result.stdout


def test_agents_and_skills_governance_lock_rag_doctrine() -> None:
    for script in ("scripts/check_agents_governance.py", "scripts/check_skills_governance.py"):
        result = run_script(script)
        assert result.returncode == 0, result.stdout

    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    skills = (ROOT / "SKILLS.md").read_text(encoding="utf-8")
    assert "Agent RAG" in agents
    assert "nsi_corpus" in agents
    assert "rag_education` peut servir d'inspiration" in agents
    assert "recherche sémantique dans `rag_education`" not in agents
    assert "recherche sémantique dans `rag_education`" not in skills


def test_coverage_gap_action_plan_covers_every_absent_capacity() -> None:
    result = run_script("scripts/check_coverage_gap_action_plan.py")
    assert result.returncode == 0, result.stdout

    plan = ROOT / "coverage_gap_action_plan.md"
    assert plan.exists()
    text = plan.read_text(encoding="utf-8")
    for capacity_id in absent_capacity_ids():
        assert f"| {capacity_id} |" in text
    assert "validated_pedagogy" not in text


def test_sources_catalog_and_scraping_policy_are_checked() -> None:
    for path in ("sources_catalog.yml", "scraping_strategy.md", "scraping_ingestion_plan.md"):
        assert (ROOT / path).exists(), f"{path} missing"

    result = run_script("scripts/check_sources_catalog.py")
    assert result.returncode == 0, result.stdout
    result = run_script("scripts/check_sources_catalog_schema.py")
    assert result.returncode == 0, result.stdout
    assert (ROOT / "sources_catalog.schema.json").exists()


def test_rag_index_metadata_uses_only_canonical_pedagogical_sources() -> None:
    result = run_script("scripts/check_rag_index_metadata.py")
    assert result.returncode == 0, result.stdout
    result = run_script("scripts/check_rag_metadata_canonical_fields.py")
    assert result.returncode == 0, result.stdout


def test_rag_collection_and_golden_example_policies_are_enforced() -> None:
    for script in (
        "scripts/check_rag_collection_policy.py",
        "scripts/check_rag_golden_examples_policy.py",
    ):
        result = run_script(script)
        assert result.returncode == 0, result.stdout

    sys.path.insert(0, str(ROOT / "scripts"))
    import ingest_nsi_corpus

    source_dirs = {path.relative_to(ROOT).as_posix() for path in ingest_nsi_corpus.SOURCE_DIRS}
    assert source_dirs == {
        "03_progressions/supports",
        "03_progressions/fiches_cours",
    }
    assert "premiere/sequences" not in "\n".join(source_dirs)
    assert "terminale/sequences" not in "\n".join(source_dirs)


def test_pedagogical_indexes_are_generated_and_checked() -> None:
    result = run_script("scripts/generate_pedagogical_indexes.py")
    assert result.returncode == 0, result.stdout
    result = run_script("scripts/check_pedagogical_indexes.py")
    assert result.returncode == 0, result.stdout

    forbidden = ("AUDIT/", "dist/", ".git/", "Documents_DRIVE/", "NotesEleves.csv", "Fichier_Eleves.csv")
    for name in (
        "INDEX_BY_LEVEL.md",
        "INDEX_BY_THEME.md",
        "INDEX_BY_DOMAIN.md",
        "INDEX_BY_CHAPTER.md",
        "INDEX_BY_SEQUENCE.md",
        "INDEX_BY_SESSION.md",
        "INDEX_BY_DOCUMENT_TYPE.md",
        "INDEX_BY_CAPACITY.md",
        "INDEX_BY_AUDIENCE.md",
        "INDEX_BY_RAG_COLLECTION.md",
    ):
        text = (ROOT / name).read_text(encoding="utf-8")
        assert any(path in text for path in ("03_progressions/supports/", "Aucune ressource"))
        assert "## Synthèse" in text
        assert "Ressources avec capacity_ids" in text
        for marker in forbidden:
            assert marker not in text


def test_makefile_separates_core_and_metrics_audits() -> None:
    text = (ROOT / "Makefile").read_text(encoding="utf-8")
    assert "\naudit-core:" in text
    assert "\naudit-metrics:" in text
    assert "\naudit: audit-core audit-metrics" in text
    core_section = text.split("\naudit-core:", 1)[1].split("\n\n", 1)[0]
    for required in (
        "scripts/check_git_clean.py",
        "scripts/check_audit_folder_policy.py",
        "scripts/check_content_tree_policy.py",
        "scripts/check_rag_config.py",
        "scripts/rag_smoke_test.py",
        "scripts/check_agents_governance.py",
        "scripts/check_skills_governance.py",
        "scripts/check_program_coverage.py",
        "scripts/check_substance_anchors.py",
        "scripts/check_contract_substance_quality.py",
        "scripts/check_differentiation_distinctness.py",
        "scripts/check_rendered_unit_artifacts.py --unit P05",
        "scripts/check_rendered_unit_artifacts.py --unit T10",
        "scripts/check_no_private_data.py",
        "scripts/check_no_committed_secrets.py",
        "scripts/check_no_placeholders_docs.py",
        "scripts/check_no_placeholders_code.py",
        "scripts/run_python_tests.py",
    ):
        assert required in core_section
    assert "RAG_ENV_FILE=.env.rag.audit-core-missing python scripts/rag_smoke_test.py" in core_section
    assert "\nrag-smoke-required:" in text

    result = run_script("scripts/check_makefile_audit_policy.py")
    assert result.returncode == 0, result.stdout


def test_quality_gates_run_rag_smoke_in_clone_clean_mode() -> None:
    text = (ROOT / "scripts" / "check_quality_gates.py").read_text(encoding="utf-8")
    assert "RAG_ENV_FILE" in text
    assert ".env.rag.audit-core-missing" in text
    for script in (
        "check_rag_collection_policy.py",
        "check_rag_golden_examples_policy.py",
        "check_rag_metadata_canonical_fields.py",
        "check_no_secret_file_mutation_policy.py",
        "check_makefile_audit_policy.py",
        "check_reports_policy.py",
    ):
        assert script in text


def test_secret_file_mutation_policy_rejects_direct_env_rag_edits(tmp_path: Path) -> None:
    sys.path.insert(0, str(ROOT / "scripts"))
    import check_no_secret_file_mutation_policy as policy

    bad = tmp_path / "docs" / "bad.md"
    good = tmp_path / "docs" / "good.md"
    bad.parent.mkdir()
    bad.write_text("perl -0pi -e 's/^RAG_COLLECTION=.*/x/' .env.rag\n", encoding="utf-8")
    good.write_text(
        "sed -n 's/^\\([A-Z0-9_]*\\)=.*/\\1=<hidden>/p' .env.rag\n"
        "RAG_COLLECTION=nsi_corpus dans .env.rag.example\n",
        encoding="utf-8",
    )

    errors = policy.scan_paths([bad, good], tmp_path)

    assert errors == ["docs/bad.md: mutation directe interdite de .env.rag"]


def test_rag_timeout_diagnostic_skips_without_config() -> None:
    result = run_script(
        "scripts/rag_diagnose_search_timeout.py",
        extra_env={"RAG_ENV_FILE": str(ROOT / ".env.rag.missing-for-timeout-test")},
    )
    assert result.returncode == 0, result.stdout
    assert "RAG_TIMEOUT_DIAG_SKIPPED_NO_CONFIG" in result.stdout
    assert "RAG_API_KEY" not in result.stdout
    assert "Authorization" not in result.stdout


def test_reports_policy_is_documented_and_checked() -> None:
    assert (ROOT / "reports_policy.md").exists()
    result = run_script("scripts/check_reports_policy.py")
    assert result.returncode == 0, result.stdout


def test_coverage_gap_plan_uses_typed_actionable_rows() -> None:
    plan = (ROOT / "coverage_gap_action_plan.md").read_text(encoding="utf-8")
    assert "type_ecart" in plan
    assert "TODO" not in plan
    assert "TBD" not in plan
    assert "à définir" not in plan.lower()
    result = run_script("scripts/check_coverage_gap_action_plan.py")
    assert result.returncode == 0, result.stdout


def test_rag_server_timeout_reports_are_actionable() -> None:
    timeout_report = ROOT / "rag_timeout_diagnostic.md"
    fix_plan = ROOT / "rag_server_fix_plan.md"
    assert timeout_report.exists()
    assert fix_plan.exists()
    text = timeout_report.read_text(encoding="utf-8")
    for expected in (
        "hypothèse 1 : timeout embedding",
        "hypothèse 2 : timeout Chroma query",
        "hypothèse 3 : endpoint /search attend un mauvais payload",
        "hypothèse 4 : collection absente ou volumétrie problématique",
        "hypothèse 5 : proxy public non responsable",
    ):
        assert expected in text
    assert "RAG_API_KEY" not in text
    assert "Authorization: Bearer" not in text


def test_sources_catalog_schema_rejects_external_source_in_internal_collection(tmp_path: Path) -> None:
    sys.path.insert(0, str(ROOT / "scripts"))
    import check_sources_catalog_schema as schema_check

    catalog = tmp_path / "sources_catalog.yml"
    catalog.write_text(
        textwrap.dedent(
            """
            sources:
              - id: external_bad
                title: Source ouverte
                url: https://example.test
                local_path: external.md
                source_type: ressource_pedagogique_ouverte
                license: libre
                copyright_status: ok
                rgpd_status: aucune_donnee_personnelle
                level: premiere
                theme: tables
                capacity_ids: []
                reuse_policy: inspiration seulement
                rag_collection: nsi_corpus
                decision: classer_reference
                reviewer: QA
                date_review: 2026-06-29
                risk_level: low
                allowed_actions:
                  - inspire
            """
        ).strip()
        + "\n",
        encoding="utf-8",
    )

    errors = schema_check.check_catalog(catalog)

    assert errors == ["external_bad: une source externe ne peut pas aller dans nsi_corpus"]


def test_manifest_keeps_all_resources_non_promoted() -> None:
    with (ROOT / "manifest.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert rows
    assert {row["statut"] for row in rows} == {"needs_review"}
    assert "covered : 0" in (ROOT / "coverage.md").read_text(encoding="utf-8")
