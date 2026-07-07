#!/usr/bin/env python3
"""Adversarial fixture matrix for the hardened substance checker.

Each test creates a minimal verdict fixture and verifies that the checker
correctly rejects (ROUGE) or accepts (VERT) it.
"""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any

from scripts.check_substance_anchors import (
    check_capacity,
    check_intra_file_duplicates,
    validate_verdict_data,
)
from scripts.judge_campaign import validate_verdict_file


def _make_capacity(cap_id: str = "P-TEST-01",
                   label: str = "Tester la capacité.",
                   proof_course: dict | None = None,
                   proof_practice: dict | None = None,
                   proof_correction: dict | None = None,
                   justification: str = "Verdict de test.",
                   verdict: str = "needs_review",
                   flags: list | None = None) -> dict:
    default_absent = {"present": False, "file": None, "anchor": None,
                      "quote": None, "teaches": False}
    return {
        "capacity_id": cap_id,
        "official_label": label,
        "proof_course": proof_course or dict(default_absent),
        "proof_practice": proof_practice or dict(default_absent),
        "proof_correction": proof_correction or dict(default_absent),
        "verdict": verdict,
        "justification": justification,
        "scientific_flags": flags or ["human_review_required"],
    }


def _make_proof(present: bool = True, file: str = "test.md",
                anchor: str = "#section", quote: str = "Citation exacte du fichier.",
                teaches: bool = True) -> dict:
    if not present:
        return {"present": False, "file": None, "anchor": None,
                "quote": None, "teaches": False}
    return {"present": present, "file": file, "anchor": anchor,
            "quote": quote, "teaches": teaches}


class TestSubstanceHardened(unittest.TestCase):
    """Adversarial matrix: one fixture per hardened rule."""

    def setUp(self):
        """Create a temp .md file with known sections for anchor/quote tests."""
        self.tmpdir = tempfile.mkdtemp()
        self.md_path = Path(self.tmpdir) / "test.md"
        self.md_path.write_text(
            "## Section\nCitation exacte du fichier.\n\n"
            "## Autre section\nAutre contenu réel ici.\n",
            encoding="utf-8",
        )
        self.root = Path(self.tmpdir)
        self.section_cache: dict[Path, dict] = {}
        self.official = {"P-TEST-01": "Tester la capacité."}

    # ── ROUGE: fabricated suffix ──
    def test_injected_suffix_rejected(self):
        """Quote with '(capacité vérifiée dans le fichier)' must fail."""
        cap = _make_capacity(
            proof_course=_make_proof(
                quote="mot. (capacité vérifiée dans le fichier)"),
        )
        result = check_capacity(cap, self.root, self.official, self.section_cache)
        course_proof = result.proofs[0]
        # The quote won't match the section body
        self.assertFalse(course_proof.verified,
                         "Injected suffix should make quote absent")

    # ── ROUGE: anchor inexistante ──
    def test_absent_anchor_rejected(self):
        """Non-existent anchor must fail."""
        cap = _make_capacity(
            proof_course=_make_proof(anchor="#nonexistent-section"),
        )
        result = check_capacity(cap, self.root, self.official, self.section_cache)
        self.assertFalse(result.proofs[0].anchor_ok)
        self.assertFalse(result.proofs[0].verified)

    # ── ROUGE: quote dupliquée entre rôles ──
    def test_duplicate_quote_rejected(self):
        """Same quote in two roles must flag the duplicate."""
        same_quote = "Citation exacte du fichier."
        cap = _make_capacity(
            proof_course=_make_proof(quote=same_quote),
            proof_practice=_make_proof(quote=same_quote),
        )
        result = check_capacity(cap, self.root, self.official, self.section_cache)
        # At least one of the two must be flagged
        flagged = [p for p in result.proofs if not p.quote_ok and p.present]
        self.assertTrue(len(flagged) >= 1,
                        "Duplicate quote should be flagged")

    # ── ROUGE: label templaté ──
    def test_template_label_quote_rejected(self):
        """Quote that is just '<ID> : <label>' must be rejected."""
        self.md_path.write_text(
            "## Section\nP-TEST-01 : Tester la capacité.\n",
            encoding="utf-8",
        )
        self.section_cache.clear()
        cap = _make_capacity(
            proof_course=_make_proof(
                quote="P-TEST-01 : Tester la capacité."),
        )
        result = check_capacity(cap, self.root, self.official, self.section_cache)
        course = result.proofs[0]
        self.assertFalse(course.quote_ok,
                         "Template label citation should be rejected")

    # ── ROUGE: reformulation ** ──
    def test_markdown_bold_not_in_body(self):
        """Quote with ** formatting that doesn't exist in body must fail."""
        cap = _make_capacity(
            proof_course=_make_proof(
                quote="**Citation** exacte du fichier."),
        )
        result = check_capacity(cap, self.root, self.official, self.section_cache)
        # The quote has ** which isn't in the body (body has no **)
        # Actually "**Citation** exacte du fichier." IS in the body if we check...
        # The body is "Citation exacte du fichier." without **.
        # So the quote should NOT match (** is not in body).
        self.assertFalse(result.proofs[0].quote_ok,
                         "Quote with ** not in body should fail")

    # ── VERT: cas conforme ──
    def test_valid_verdict_accepted(self):
        """Correct verdict with valid anchor, quote, and file must pass."""
        cap = _make_capacity(
            proof_course=_make_proof(
                quote="Citation exacte du fichier."),
            proof_practice=_make_proof(
                anchor="#autre-section",
                quote="Autre contenu réel ici."),
        )
        result = check_capacity(cap, self.root, self.official, self.section_cache)
        for p in result.proofs:
            if p.present:
                self.assertTrue(p.verified,
                                f"Valid proof should be verified: {p.role}")


    # ── ROUGE: doublon intra-fichier — shared function ──

    _DUP_VERDICT: dict = {
        "schema_version": "1.0.0",
        "unit": "test-dup",
        "level": "premiere",
        "judged_at": "2026-01-01T00:00:00Z",
        "judge_model": "test",
        "author_model": "test-author",
        "capacities": [
            {
                "capacity_id": "DUP-01",
                "official_label": "Capacité dupliquée",
                "proof_course": {"present": False, "file": None, "anchor": None, "quote": None, "teaches": False},
                "proof_practice": {"present": False, "file": None, "anchor": None, "quote": None, "teaches": False},
                "proof_correction": {"present": False, "file": None, "anchor": None, "quote": None, "teaches": False},
                "verdict": "needs_content",
                "justification": "Test",
                "scientific_flags": [],
            },
            {
                "capacity_id": "DUP-01",
                "official_label": "Capacité dupliquée (bis)",
                "proof_course": {"present": False, "file": None, "anchor": None, "quote": None, "teaches": False},
                "proof_practice": {"present": False, "file": None, "anchor": None, "quote": None, "teaches": False},
                "proof_correction": {"present": False, "file": None, "anchor": None, "quote": None, "teaches": False},
                "verdict": "needs_content",
                "justification": "Test bis",
                "scientific_flags": [],
            },
        ],
    }

    def test_intra_file_duplicate_shared_function(self):
        """check_intra_file_duplicates returns errors for duplicate capacity_id."""
        errs = check_intra_file_duplicates(self._DUP_VERDICT)
        self.assertTrue(errs, "Should detect intra-file duplicate")
        self.assertIn("DUP-01", errs[0])

    def test_intra_file_duplicate_single_file_mode(self):
        """Single-file mode (--verdict) rejects duplicate capacity_id (exit != 0)."""
        verdict_path = Path(self.tmpdir) / "dup_verdict.json"
        verdict_path.write_text(json.dumps(self._DUP_VERDICT), encoding="utf-8")
        result = subprocess.run(
            [sys.executable, "-m", "scripts.check_substance_anchors",
             str(verdict_path), "--repo-root", self.tmpdir],
            cwd=str(Path(__file__).resolve().parents[1]),
            text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        )
        self.assertNotEqual(result.returncode, 0,
                            f"Single-file mode should reject duplicate:\n{result.stdout}")
        self.assertIn("DOUBLON intra-fichier", result.stdout)

    def test_intra_file_duplicate_batch_mode(self):
        """Batch mode (no --verdict) rejects duplicate capacity_id."""
        supports_dir = Path(self.tmpdir) / "03_progressions" / "supports" / "test"
        supports_dir.mkdir(parents=True, exist_ok=True)
        verdict_path = supports_dir / "_substance_review.json"
        verdict_path.write_text(json.dumps(self._DUP_VERDICT), encoding="utf-8")
        adv_dir = Path(self.tmpdir) / "substance_reviews" / "_adversarial"
        adv_dir.mkdir(parents=True, exist_ok=True)
        (adv_dir / "poisoned.verdict.json").write_text('{"bad": true}', encoding="utf-8")
        result = subprocess.run(
            [sys.executable, "-m", "scripts.check_substance_anchors",
             "--repo-root", self.tmpdir],
            cwd=str(Path(__file__).resolve().parents[1]),
            text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        )
        self.assertNotEqual(result.returncode, 0,
                            f"Batch mode should reject duplicate:\n{result.stdout}")
        self.assertIn("DOUBLON intra-fichier", result.stdout)

    def test_intra_file_duplicate_validate_verdict_file(self):
        """validate_verdict_file (campaign path, direct import) returns errors
        for duplicate capacity_id, preventing .tmp -> final promotion."""
        verdict_path = Path(self.tmpdir) / "dup_verdict.json"
        verdict_path.write_text(json.dumps(self._DUP_VERDICT), encoding="utf-8")
        errors = validate_verdict_file(verdict_path)
        self.assertTrue(errors, "validate_verdict_file must reject duplicate capacity_id")
        self.assertTrue(any("DOUBLON" in e for e in errors))

    # ── FIX 1: non-dict root on ALL paths ──

    def test_non_dict_root_all_paths(self):
        """Non-dict JSON roots ([], null, "str", 42) must produce a blocking
        error on BOTH the direct gate and the CLI, with ZERO traceback."""
        schema_path = Path(__file__).resolve().parents[1] / "substance_verdict.schema.json"
        repo_cwd = str(Path(__file__).resolve().parents[1])
        for bad_root in [[], None, "string", 42]:
            label = repr(bad_root)
            # (a) validate_verdict_data — direct gate
            errors = validate_verdict_data(bad_root, schema_path)
            self.assertTrue(errors, f"Direct gate must reject root={label}")
            self.assertIn("objet", errors[0])
            # (b) CLI single-file
            verdict_path = Path(self.tmpdir) / "bad_root.json"
            verdict_path.write_text(json.dumps(bad_root), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, "-m", "scripts.check_substance_anchors",
                 str(verdict_path), "--repo-root", self.tmpdir],
                cwd=repo_cwd, text=True,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            )
            self.assertNotEqual(result.returncode, 0,
                                f"CLI must reject root={label}: {result.stdout}")
            self.assertNotIn("Traceback", result.stdout,
                             f"CLI must not traceback on root={label}")

    # ── FIX 2: schema before deep checks ──

    def test_proof_course_null_returns_schema_error(self):
        """proof_course:null must produce a schema error, not an exception."""
        schema_path = Path(__file__).resolve().parents[1] / "substance_verdict.schema.json"
        bad_verdict = {
            "schema_version": "1.0.0", "unit": "P05_test", "level": "premiere",
            "judged_at": "2026-01-01T00:00:00Z",
            "judge_model": "test", "author_model": "test-author",
            "capacities": [{
                "capacity_id": "P-NULL-01", "official_label": "Test null proof",
                "proof_course": None,
                "proof_practice": {"present": False, "file": None, "anchor": None, "quote": None, "teaches": False},
                "proof_correction": {"present": False, "file": None, "anchor": None, "quote": None, "teaches": False},
                "verdict": "needs_content", "justification": "Test null proof_course.",
                "scientific_flags": [],
            }],
        }
        errors = validate_verdict_data(bad_verdict, schema_path, repo_root=self.root)
        self.assertTrue(errors, "proof_course:null must produce schema errors")
        self.assertTrue(any("schéma" in e for e in errors))

    # ── FIX 3: BLOCKER parity ──

    def test_blocker_verdict_rejected_by_direct_gate(self):
        """A capacity declaring verdict:BLOCKER must be rejected by the direct
        gate, matching CLI behavior."""
        schema_path = Path(__file__).resolve().parents[1] / "substance_verdict.schema.json"
        blocker = {
            "schema_version": "1.0.0", "unit": "P05_test", "level": "premiere",
            "judged_at": "2026-01-01T00:00:00Z",
            "judge_model": "test", "author_model": "test-author",
            "capacities": [{
                "capacity_id": "P-BLOCK-01", "official_label": "Blocker test",
                "proof_course": {"present": False, "file": None, "anchor": None, "quote": None, "teaches": False},
                "proof_practice": {"present": False, "file": None, "anchor": None, "quote": None, "teaches": False},
                "proof_correction": {"present": False, "file": None, "anchor": None, "quote": None, "teaches": False},
                "verdict": "BLOCKER",
                "justification": "Incoherence bloquante detectee par le juge de substance sur cette capacite.",
                "scientific_flags": [],
            }],
        }
        errors = validate_verdict_data(blocker, schema_path, repo_root=self.root)
        self.assertTrue(errors, "BLOCKER verdict must be rejected by direct gate")
        self.assertTrue(any("BLOCKER" in e for e in errors))

    # ── FIX 4: gate parity — direct vs CLI ──

    def _cli_accepts(self, verdict_data: Any) -> bool:
        """Run CLI single-file and return True if exit code == 0."""
        path = Path(self.tmpdir) / "parity_test.json"
        path.write_text(json.dumps(verdict_data), encoding="utf-8")
        result = subprocess.run(
            [sys.executable, "-m", "scripts.check_substance_anchors",
             str(path), "--repo-root", self.tmpdir],
            cwd=str(Path(__file__).resolve().parents[1]),
            text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        )
        return result.returncode == 0

    def _direct_accepts(self, verdict_data: Any) -> bool:
        """Run validate_verdict_data and return True if errors is empty."""
        schema_path = Path(__file__).resolve().parents[1] / "substance_verdict.schema.json"
        errors = validate_verdict_data(verdict_data, schema_path, repo_root=self.root)
        return len(errors) == 0

    def _make_full_verdict(self, **cap_overrides) -> dict:
        """Build a minimal schema-valid verdict envelope."""
        absent = {"present": False, "file": None, "anchor": None, "quote": None, "teaches": False}
        cap = {
            "capacity_id": "P-PARITY-01", "official_label": "Parity test",
            "proof_course": dict(absent), "proof_practice": dict(absent),
            "proof_correction": dict(absent),
            "verdict": "needs_content",
            "justification": "Aucune preuve verifiable retenue par le juge de substance.",
            "scientific_flags": [],
        }
        cap.update(cap_overrides)
        return {
            "schema_version": "1.0.0", "unit": "P05_test", "level": "premiere",
            "judged_at": "2026-01-01T00:00:00Z",
            "judge_model": "test", "author_model": "test-author",
            "capacities": [cap],
        }

    def test_gate_parity_direct_vs_cli(self):
        """For a battery of verdicts, validate_verdict_data (direct gate) and
        CLI single-file must render the SAME accept/reject decision."""
        cases = {
            "needs_content_valid": (self._make_full_verdict(), True),
            "duplicate_intra": (self._DUP_VERDICT, False),
            "blocker_declared": (self._make_full_verdict(
                verdict="BLOCKER",
                justification="Incoherence bloquante detectee par le juge de substance sur cette capacite.",
            ), False),
            "root_list": ([], False),
            "root_null": (None, False),
        }
        for label, (verdict_data, expected_accept) in cases.items():
            cli = self._cli_accepts(verdict_data)
            direct = self._direct_accepts(verdict_data)
            self.assertEqual(cli, direct,
                             f"Parity broken for {label}: CLI={cli} direct={direct}")
            self.assertEqual(cli, expected_accept,
                             f"Wrong decision for {label}: got={cli} expected={expected_accept}")

    # ── FIX 5: validate_verdict_file exercises direct import path ──
    # (test_intra_file_duplicate_validate_verdict_file above already does this)

    # ── INVARIANT: needs_content promotable through full gate ──

    def test_needs_content_promotable_through_full_gate(self):
        """A needs_content verdict with 3 roles present:False, file:None must
        pass the COMPLETE pre-promotion gate and be promotable.
        This is the Phase K go/no-go invariant."""
        verdict = self._make_full_verdict()
        verdict_path = Path(self.tmpdir) / "promotable.json"
        verdict_path.write_text(json.dumps(verdict), encoding="utf-8")
        errors = validate_verdict_file(verdict_path)
        self.assertEqual(errors, [],
                         f"needs_content verdict must be promotable: {errors}")

    # ── ROUGE: donnees corrompues = echec bruyant ──

    def test_corrupted_data_fails_loudly(self):
        """Corrupted/unexpected data in capacities must produce errors,
        never be silently treated as valid."""
        schema_path = Path(__file__).resolve().parents[1] / "substance_verdict.schema.json"
        corrupted = {"capacities": "not-a-list"}
        errors = validate_verdict_data(corrupted, schema_path)
        self.assertTrue(errors,
                        "Corrupted verdict must produce errors, not pass silently")

    def test_missing_schema_file_blocks_promotion(self):
        """When the schema file does not exist, validate_verdict_data must
        return errors (fail-closed), not silently pass."""
        valid_verdict = self._make_full_verdict()
        missing_schema = Path(self.tmpdir) / "nonexistent.schema.json"
        errors = validate_verdict_data(valid_verdict, missing_schema)
        self.assertTrue(errors,
                        "Missing schema file must block promotion (fail-closed)")


if __name__ == "__main__":
    unittest.main()
