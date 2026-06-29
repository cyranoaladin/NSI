#!/usr/bin/env python3
"""Check that locally prepared NSI chunks expose required RAG metadata."""

from __future__ import annotations

from typing import Any

from _qa_common import print_result
import ingest_nsi_corpus


REQUIRED_METADATA = {
    "path",
    "level",
    "sequence_id",
    "document_type",
    "theme",
    "notion",
    "capacities",
    "status",
    "anchor",
    "sha256",
    "chunk_index",
    "source_type",
    "collection",
}


def check_chunk(chunk: dict[str, Any]) -> list[str]:
    metadata = chunk.get("metadata")
    if not isinstance(metadata, dict):
        return ["chunk sans metadata objet"]
    errors: list[str] = []
    missing = REQUIRED_METADATA - set(metadata)
    for key in sorted(missing):
        errors.append(f"{metadata.get('path', '?')}: metadata manquante {key}")
    if metadata.get("collection") != "nsi_corpus":
        errors.append(f"{metadata.get('path', '?')}: collection != nsi_corpus")
    if metadata.get("source_type") != "nsi_corpus":
        errors.append(f"{metadata.get('path', '?')}: source_type != nsi_corpus")
    if metadata.get("status") not in {"needs_review", "needs_content", "draft"}:
        errors.append(f"{metadata.get('path', '?')}: statut RAG non conservateur")
    return errors


def main() -> None:
    errors: list[str] = []
    checked = 0
    for path in ingest_nsi_corpus.iter_source_files():
        for chunk in ingest_nsi_corpus.build_chunks(path):
            checked += 1
            errors.extend(check_chunk(chunk))
    if checked == 0:
        errors.append("aucun chunk local préparé")
    print_result("check_rag_index_metadata", errors)


if __name__ == "__main__":
    main()
