"""Tests for the RAG ingestion pipeline (scripts/rag_ingest.py)."""
from __future__ import annotations

import tempfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]

import scripts.rag_ingest as rag_ingest

CANONICAL_KEYS = {
    "path", "section_anchor", "capacity_ids", "document_type", "status",
    "level", "theme", "notion", "sequence_id", "sha256", "collection",
    "source_type", "private_data",
}


def test_build_chunks_has_canonical_scalar_metadata() -> None:
    """Every chunk carries all canonical keys as scalars (Chroma-safe)."""
    files = rag_ingest.iter_source_files()
    if not files:
        pytest.skip("No source files found")
    chunks = rag_ingest.build_chunks(files[0])
    assert chunks, "Expected at least one chunk"
    for chunk in chunks:
        missing = CANONICAL_KEYS - set(chunk.metadata.keys())
        assert not missing, f"Missing metadata keys: {missing}"
        for key, val in chunk.metadata.items():
            assert not isinstance(val, (list, dict)), (
                f"Non-scalar metadata {key}={val!r} — Chroma will reject this"
            )


def test_capacity_ids_read_from_official_program() -> None:
    """capacity_ids comes from official_program.capacities, not top-level."""
    p07 = ROOT / "03_progressions" / "supports" / "premiere" / "P07"
    candidates = sorted(p07.glob("P07_tp_*.md"))
    if not candidates:
        pytest.skip("P07 TP file not found")
    chunks = rag_ingest.build_chunks(candidates[0])
    assert chunks, "Expected chunks"
    caps_csv = chunks[0].metadata["capacity_ids"]
    assert caps_csv, f"capacity_ids is empty: {caps_csv!r}"
    assert "P-LANG" in caps_csv, f"Expected P-LANG capacities, got: {caps_csv}"


def test_adapt_metadata_roundtrip() -> None:
    """ingest(list) -> store(csv) -> adapt -> list identical."""
    original = ["P-TABLE-01", "P-TABLE-02"]
    csv_str = ",".join(original)
    adapted = rag_ingest.adapt_metadata({"capacity_ids": csv_str})
    assert adapted["capacity_ids"] == original


def test_adapt_metadata_empty() -> None:
    adapted = rag_ingest.adapt_metadata({"capacity_ids": ""})
    assert adapted["capacity_ids"] == []


def test_build_chunks_refuses_private_data_flag() -> None:
    """private_data: true → zero chunks."""
    test_dir = ROOT / "03_progressions" / "supports"
    if not test_dir.exists():
        pytest.skip("supports dir missing")
    sentinel = test_dir / "_test_private_sentinel.md"
    try:
        sentinel.write_text(
            "---\nprivate_data: true\nstatus: needs_review\n---\nContenu privé.\n",
            encoding="utf-8",
        )
        chunks = rag_ingest.build_chunks(sentinel)
        assert chunks == [], "private_data: true should produce zero chunks"
    finally:
        sentinel.unlink(missing_ok=True)


def test_dry_run_produces_report() -> None:
    with tempfile.TemporaryDirectory() as td:
        report = rag_ingest.ingest(Path(td), dry_run=True)
    assert report.files_seen > 0
    assert report.errors == []
