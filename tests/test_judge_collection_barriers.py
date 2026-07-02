"""Test substance judge collection + source_type barriers.

Tests call the REAL predicates and search_rag (via monkeypatch), never
reimplementing the filter logic locally.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]

import scripts.substance_judge as judge


# ---------------------------------------------------------------------------
# Barrier A — is_internal_collection (predicate + refusal path)
# ---------------------------------------------------------------------------

def test_barrier_a_predicate_accepts_internal() -> None:
    assert judge.is_internal_collection("nsi_corpus")
    assert judge.is_internal_collection("nsi_corpus_v2")


def test_barrier_a_predicate_rejects_external() -> None:
    assert not judge.is_internal_collection("rag_education")
    assert not judge.is_internal_collection("nsi_golden_examples")
    assert not judge.is_internal_collection("")


# ---------------------------------------------------------------------------
# Barrier B — is_internal_hit (predicate)
# ---------------------------------------------------------------------------

def test_barrier_b_predicate_accepts_nsi_corpus() -> None:
    hit = {"metadata": {"source_type": "nsi_corpus"}}
    assert judge.is_internal_hit(hit)


def test_barrier_b_predicate_rejects_golden_example() -> None:
    assert not judge.is_internal_hit({"metadata": {"source_type": "golden_example"}})


def test_barrier_b_predicate_rejects_excluded() -> None:
    assert not judge.is_internal_hit({"metadata": {"source_type": "excluded"}})


def test_barrier_b_predicate_rejects_non_dict() -> None:
    assert not judge.is_internal_hit("not a dict")  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# Barrier B via search_rag (end-to-end with monkeypatched network)
# ---------------------------------------------------------------------------

def _fake_http_json_mixed(*args: Any, **kwargs: Any) -> dict[str, Any]:
    """Return a mix of internal + non-internal hits."""
    return {
        "hits": [
            {"metadata": {"source_type": "nsi_corpus", "document_type": "tp"}},
            {"metadata": {"source_type": "golden_example", "document_type": "tp"}},
            {"metadata": {"source_type": "excluded", "document_type": "cours"}},
            "not-a-dict",
        ]
    }


def test_search_rag_filters_non_internal_hits() -> None:
    """search_rag must return ONLY hits passing is_internal_hit."""
    env = {"RAG_API_BASE_URL": "http://fake", "RAG_API_KEY": "fake", "RAG_COLLECTION": "nsi_corpus_v2"}
    with patch.object(judge, "_http_json", _fake_http_json_mixed):
        result = judge.search_rag(env, "test query")
    assert len(result) == 1
    assert result[0]["metadata"]["source_type"] == "nsi_corpus"
