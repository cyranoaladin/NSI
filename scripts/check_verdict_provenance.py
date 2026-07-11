#!/usr/bin/env python3
"""Gate: verdict files modified in a commit must have fresh judged_at metadata.

Rule: any *_substance_review.json diff must be accompanied by a judged_at
timestamp produced by the pipeline (judge_campaign). A manual edit that changes
quote/justification/anchor without re-running the judge is a provenance
violation.

Detection method: for each changed verdict file, compare its judged_at to the
commit timestamp. If judged_at is older than the commit by more than
STALENESS_SECONDS, the verdict was edited manually.

Usage:
    python -m scripts.check_verdict_provenance [--base BASE_REF]

Exit codes:
    0: all changed verdicts have fresh provenance
    1: stale provenance detected (manual edit without re-judgment)
"""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STALENESS_SECONDS = 300  # 5 minutes tolerance between judge run and commit


def get_changed_verdict_files(base_ref: str = "HEAD~1") -> list[Path]:
    """Return verdict files changed between base_ref and HEAD."""
    result = subprocess.run(
        ["git", "diff", "--name-only", base_ref, "HEAD"],
        capture_output=True, text=True, cwd=ROOT,
    )
    changed = []
    for line in result.stdout.strip().splitlines():
        if line.endswith("_substance_review.json"):
            path = ROOT / line
            if path.exists():
                changed.append(path)
    return changed


def get_commit_timestamp() -> datetime:
    """Return the timestamp of HEAD commit."""
    result = subprocess.run(
        ["git", "log", "-1", "--format=%aI"],
        capture_output=True, text=True, cwd=ROOT,
    )
    return datetime.fromisoformat(result.stdout.strip())


def check_provenance(base_ref: str = "HEAD~1") -> list[str]:
    """Check all changed verdict files for fresh provenance."""
    errors: list[str] = []
    changed = get_changed_verdict_files(base_ref)
    if not changed:
        return errors

    commit_ts = get_commit_timestamp()

    for path in changed:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            errors.append(f"{path.name}: unreadable ({e})")
            continue

        judged_at_str = data.get("judged_at")
        if not judged_at_str:
            errors.append(
                f"{path.name}: missing judged_at — verdict must be produced by judge_campaign"
            )
            continue

        try:
            judged_at = datetime.fromisoformat(judged_at_str)
        except ValueError:
            errors.append(f"{path.name}: invalid judged_at format")
            continue

        # Ensure both are offset-aware for comparison
        if judged_at.tzinfo is None:
            judged_at = judged_at.replace(tzinfo=timezone.utc)
        if commit_ts.tzinfo is None:
            commit_ts = commit_ts.replace(tzinfo=timezone.utc)

        delta = (commit_ts - judged_at).total_seconds()
        if delta > STALENESS_SECONDS:
            errors.append(
                f"{path.name}: judged_at ({judged_at_str}) is {int(delta)}s older than commit — "
                f"verdict was edited manually without re-running judge_campaign. "
                f"Rule: all verdict edits must go through the pipeline."
            )

    return errors


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="HEAD~1", help="Base ref for diff")
    args = parser.parse_args()

    errors = check_provenance(args.base)
    if errors:
        print("check_verdict_provenance: FAIL")
        for e in errors:
            print(f"  ✗ {e}")
        sys.exit(1)
    else:
        print("check_verdict_provenance: PASS")


if __name__ == "__main__":
    main()
