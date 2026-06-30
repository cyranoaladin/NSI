"""Gate: package-audit must never skip build_source_archive via a stale guard."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _package_audit_body() -> str:
    text = (ROOT / "Makefile").read_text(encoding="utf-8")
    match = re.search(r"^package-audit:.*?\n(.*?)(?=\n[A-Za-z0-9_-]+:|\Z)", text, re.S | re.M)
    return match.group(1) if match else ""


def test_no_stale_archive_guard() -> None:
    """package-audit must NOT contain a conditional guard around build_source_archive."""
    body = _package_audit_body()
    assert "test -f dist/source_clean.tar.gz" not in body, (
        "package-audit contains a stale-archive guard (@test -f). "
        "build_source_archive must always run for correctness."
    )
    assert "test -f dist/git_bundle.bundle" not in body, (
        "package-audit contains a stale-archive guard for git_bundle."
    )
