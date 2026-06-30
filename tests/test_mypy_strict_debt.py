"""Ratchet test for mypy --strict debt.

Pins the exact set of known mypy errors in tests/mypy_baseline.txt.
- A NEW error not in baseline -> test FAILS (regression).
- Errors REMOVED from actual but still in baseline -> test FAILS
  (update baseline to lock the improvement).
- Baseline == actual -> PASS.

To update after fixing errors:
  mypy --strict scripts/ scrapping_NSI/ 2>&1 | grep ': error:' \
    | sed 's|<repo_root>/||' | sort > tests/mypy_baseline.txt
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = Path(__file__).with_name("mypy_baseline.txt")


def _normalise(line: str) -> str:
    """Strip the repo prefix so lines are comparable across machines."""
    root_str = str(ROOT) + "/"
    if line.startswith(root_str):
        return line[len(root_str):]
    return line


def test_mypy_ratchet() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "mypy", "--strict", "scripts/", "scrapping_NSI/"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=300,
    )

    actual = sorted(
        _normalise(line)
        for line in result.stdout.splitlines()
        if ": error:" in line
    )
    baseline = sorted(
        line.strip()
        for line in BASELINE.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )

    new_errors = sorted(set(actual) - set(baseline))
    fixed_errors = sorted(set(baseline) - set(actual))

    messages: list[str] = []
    if new_errors:
        messages.append(
            f"{len(new_errors)} NEW mypy error(s) — fix them before merging:\n"
            + "\n".join(f"  + {e}" for e in new_errors[:20])
        )
    if fixed_errors:
        messages.append(
            f"{len(fixed_errors)} error(s) FIXED — update tests/mypy_baseline.txt:\n"
            + "\n".join(f"  - {e}" for e in fixed_errors[:20])
        )
    assert not messages, "\n\n".join(messages)
