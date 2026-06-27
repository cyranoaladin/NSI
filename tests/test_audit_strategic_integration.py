import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_script(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=120,
    )


class AuditStrategicIntegrationTests(unittest.TestCase):
    def test_program_coverage_indexes_supports_and_writes_sources(self):
        result = run_script("scripts/check_program_coverage.py")
        self.assertEqual(result.returncode, 0, result.stdout)
        coverage = (ROOT / "coverage.md").read_text(encoding="utf-8")
        sources = (ROOT / "coverage_sources.md").read_text(encoding="utf-8")
        self.assertIn("03_progressions/supports/", coverage)
        self.assertIn("03_progressions/supports/", sources)
        self.assertIn("- covered : 0", coverage)

    def test_audit_folder_policy_excludes_audit_from_pedagogical_corpus(self):
        result = run_script("scripts/check_audit_folder_policy.py")
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("corpus pédagogique", result.stdout)

    def test_substance_anchor_checker_global_mode_and_poisoned_fixture(self):
        result = run_script("scripts/check_substance_anchors.py")
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("test adverse", result.stdout.lower())

    def test_gate_policy_has_small_blocking_core(self):
        result = run_script("scripts/check_gate_policy_consistency.py")
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("bloquants hors tests", result.stdout)

    def test_rendered_unit_checker_builds_temp_student_and_teacher_outputs(self):
        result = run_script("scripts/check_rendered_unit_artifacts.py", "--unit", "P05")
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("version élève", result.stdout)
        self.assertIn("version prof", result.stdout)

    def test_substance_review_files_use_needs_content_only(self):
        reviews = sorted(ROOT.glob("03_progressions/supports/**/_substance_review.json"))
        self.assertTrue(reviews, "aucun verdict pilote de substance")
        for review in reviews:
            payload = json.loads(review.read_text(encoding="utf-8"))
            verdicts = {cap["verdict"] for cap in payload.get("capacities", [])}
            self.assertLessEqual(verdicts, {"needs_content", "BLOCKER"}, str(review))
