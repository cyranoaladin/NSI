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


def test_build_chunks_has_canonical_metadata() -> None:
    """Every chunk from a real source file carries all canonical keys."""
    files = rag_ingest.iter_source_files()
    if not files:
        pytest.skip("No source files found")
    chunks = rag_ingest.build_chunks(files[0])
    assert chunks, "Expected at least one chunk"
    for chunk in chunks:
        missing = CANONICAL_KEYS - set(chunk.metadata.keys())
        assert not missing, f"Missing metadata keys: {missing}"


def test_build_chunks_refuses_private_data_flag() -> None:
    """A file with private_data: true produces zero chunks."""
    # Use a temporary file inside the repo tree so path operations work
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
    """Dry-run produces a valid report without writing to any DB."""
    with tempfile.TemporaryDirectory() as td:
        report = rag_ingest.ingest(Path(td), dry_run=True)
    assert report.files_seen > 0, "Expected source files to be seen"
    assert report.chunks_upserted >= 0
    assert report.errors == []


def test_deterministic_two_runs_same_output() -> None:
    """Two consecutive ingestions into an ephemeral DB produce identical state."""
    try:
        import chromadb  # noqa: F401
    except ImportError:
        pytest.skip("chromadb not installed")

    with tempfile.TemporaryDirectory() as td:
        db_path = Path(td) / "chroma"

        # Deterministic embedding: fixed vector for reproducibility
        class FixedEmbedding:
            def __call__(self, input: list[str]) -> list[list[float]]:
                return [[0.1] * 10 for _ in input]

        r1 = rag_ingest.ingest(db_path, embedding_fn=FixedEmbedding())
        r2 = rag_ingest.ingest(db_path, embedding_fn=FixedEmbedding())

        assert r1.files_ingested == r2.files_ingested
        assert r1.chunks_upserted == r2.chunks_upserted
