"""Track mypy --strict debt and prevent regression.

This test documents the known mypy --strict error count.  When the count
drops (fixes applied), the test forces an update of the threshold so the
debt can only shrink.  When the count rises, the test fails.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]

KNOWN_ERROR_COUNT = 112


@pytest.mark.xfail(reason="mypy --strict legacy debt: 112 errors in 29 files (reports/reconciliation/mypy_debt.md)", strict=True)
def test_mypy_strict_known_debt() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "mypy", "--strict", "scripts/", "scrapping_NSI/"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=300,
    )
    assert result.returncode == 0, (
        f"mypy --strict has {result.stdout.strip().splitlines()[-1]}"
    )
