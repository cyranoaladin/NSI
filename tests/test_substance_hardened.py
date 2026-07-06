#!/usr/bin/env python3
"""Adversarial fixture matrix for the hardened substance checker.

Each test creates a minimal verdict fixture and verifies that the checker
correctly rejects (ROUGE) or accepts (VERT) it.
"""

import tempfile
import unittest
from pathlib import Path

from scripts.check_substance_anchors import (
    check_capacity,
)


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


if __name__ == "__main__":
    unittest.main()
