"""Tests for check_verdict_provenance gate."""

from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timezone, timedelta
from pathlib import Path
from unittest.mock import patch

from scripts.check_verdict_provenance import check_provenance


class VerdictProvenanceTest(unittest.TestCase):
    def _make_verdict(self, judged_at: str) -> str:
        return json.dumps({
            "schema_version": "1.0.0",
            "unit": "campaign",
            "level": "premiere",
            "judged_at": judged_at,
            "judge_model": "claude-sonnet-4-6",
            "author_model": "campaign-tooling",
            "capacities": [{
                "capacity_id": "P-TEST-01",
                "official_label": "Test",
                "proof_course": {"present": False},
                "proof_practice": {"present": False},
                "proof_correction": {"present": False},
                "verdict": "needs_content",
                "justification": "test",
                "scientific_flags": [],
            }],
        })

    def test_fresh_verdict_passes(self) -> None:
        """Verdict judged_at within STALENESS_SECONDS of commit → PASS."""
        now = datetime.now(timezone.utc)
        judged_at = now.isoformat()
        commit_ts = (now + timedelta(seconds=60)).isoformat()

        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            verdict_path = root / "P-TEST-01_substance_review.json"
            verdict_path.write_text(self._make_verdict(judged_at), encoding="utf-8")

            with patch("scripts.check_verdict_provenance.get_changed_verdict_files", return_value=[verdict_path]):
                with patch("scripts.check_verdict_provenance.get_commit_timestamp",
                           return_value=datetime.fromisoformat(commit_ts)):
                    errors = check_provenance()

        self.assertEqual(errors, [])

    def test_stale_verdict_fails(self) -> None:
        """Verdict judged_at much older than commit → FAIL (manual edit detected)."""
        old_time = datetime(2026, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        commit_time = datetime(2026, 7, 11, 19, 0, 0, tzinfo=timezone.utc)

        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            verdict_path = root / "P-TEST-01_substance_review.json"
            verdict_path.write_text(
                self._make_verdict(old_time.isoformat()), encoding="utf-8"
            )

            with patch("scripts.check_verdict_provenance.get_changed_verdict_files", return_value=[verdict_path]):
                with patch("scripts.check_verdict_provenance.get_commit_timestamp", return_value=commit_time):
                    errors = check_provenance()

        self.assertTrue(len(errors) == 1)
        self.assertIn("edited manually", errors[0])

    def test_missing_judged_at_fails(self) -> None:
        """Verdict without judged_at field → FAIL."""
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            verdict_path = root / "P-TEST-01_substance_review.json"
            data = json.loads(self._make_verdict("2026-01-01T00:00:00Z"))
            del data["judged_at"]
            verdict_path.write_text(json.dumps(data), encoding="utf-8")

            with patch("scripts.check_verdict_provenance.get_changed_verdict_files", return_value=[verdict_path]):
                with patch("scripts.check_verdict_provenance.get_commit_timestamp",
                           return_value=datetime.now(timezone.utc)):
                    errors = check_provenance()

        self.assertTrue(len(errors) == 1)
        self.assertIn("missing judged_at", errors[0])


if __name__ == "__main__":
    unittest.main()
