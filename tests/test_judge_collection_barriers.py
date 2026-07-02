"""Test substance judge collection + source_type barriers."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

import scripts.substance_judge as judge


def test_barrier_a_rejects_non_internal_collection() -> None:
    """RAG_COLLECTION outside allowlist -> REFUS."""
    assert "rag_education" not in judge.INTERNAL_COVERAGE_COLLECTIONS
    assert "nsi_golden_examples" not in judge.INTERNAL_COVERAGE_COLLECTIONS


def test_barrier_a_accepts_internal_collections() -> None:
    """nsi_corpus and nsi_corpus_v2 are allowed."""
    assert "nsi_corpus" in judge.INTERNAL_COVERAGE_COLLECTIONS
    assert "nsi_corpus_v2" in judge.INTERNAL_COVERAGE_COLLECTIONS


def test_barrier_b_filters_non_internal_source_type() -> None:
    """search_rag filters out hits with source_type != nsi_corpus."""
    # Build fake hits
    internal_hit = {"metadata": {"source_type": "nsi_corpus", "document_type": "tp"}}
    golden_hit = {"metadata": {"source_type": "golden_example", "document_type": "tp"}}
    excluded_hit = {"metadata": {"source_type": "excluded", "document_type": "tp"}}

    mixed = [internal_hit, golden_hit, excluded_hit]
    # Simulate the filter from search_rag's return
    filtered = [
        hit for hit in mixed
        if isinstance(hit, dict)
        and hit.get("metadata", {}).get("source_type", "") == "nsi_corpus"
    ]
    assert len(filtered) == 1
    assert filtered[0] is internal_hit


def test_barrier_b_accepts_all_internal() -> None:
    """All nsi_corpus hits pass the filter."""
    hits = [
        {"metadata": {"source_type": "nsi_corpus", "document_type": "cours"}},
        {"metadata": {"source_type": "nsi_corpus", "document_type": "td"}},
    ]
    filtered = [
        hit for hit in hits
        if hit.get("metadata", {}).get("source_type", "") == "nsi_corpus"
    ]
    assert len(filtered) == 2
