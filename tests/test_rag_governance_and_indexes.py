from __future__ import annotations

import csv
import os
import subprocess
import sys
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


def test_rag_index_metadata_uses_only_canonical_pedagogical_sources() -> None:
    result = run_script("scripts/check_rag_index_metadata.py")
    assert result.returncode == 0, result.stdout


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


def test_quality_gates_run_rag_smoke_in_clone_clean_mode() -> None:
    text = (ROOT / "scripts" / "check_quality_gates.py").read_text(encoding="utf-8")
    assert "RAG_ENV_FILE" in text
    assert ".env.rag.audit-core-missing" in text


def test_manifest_keeps_all_resources_non_promoted() -> None:
    with (ROOT / "manifest.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert rows
    assert {row["statut"] for row in rows} == {"needs_review"}
    assert "covered : 0" in (ROOT / "coverage.md").read_text(encoding="utf-8")
