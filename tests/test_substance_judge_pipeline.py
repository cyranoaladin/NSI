import json
import subprocess
import sys
import tempfile
import unittest
import urllib.request
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))


def capacity() -> dict:
    return {
        "id": "P-DATA-BASE-01",
        "intitule": "Passer de la représentation d'une base dans une autre.",
        "rubrique": "Représentation des données",
        "contenu": "Ecriture d'un entier positif dans une base b >= 2",
        "niveau": "premiere",
    }


class SubstanceJudgePipelineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "doc.md").write_text(
            "# Section\n\n"
            "Passer de la représentation d'une base dans une autre avec une méthode explicite.\n"
            "L'élève s'entraîne sur une conversion vérifiable.\n"
            "Le corrigé donne la base de départ et la base d'arrivée.\n"
            "Citation avec\n"
            "espaces   multiples.\n"
            "Objectif O1 - Identifier précisément la représentation.\n",
            encoding="utf-8",
        )
        (self.root / "substance_verdict.schema.json").write_text(
            (ROOT / "substance_verdict.schema.json").read_text(encoding="utf-8"),
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def hit(self) -> dict:
        return {
            "metadata": {"path": "doc.md", "anchor": "#section", "document_type": "cours"},
            "document": (self.root / "doc.md").read_text(encoding="utf-8"),
            "score": 0.1,
        }

    def test_b_produces_schema_a_and_never_validated_pedagogy(self) -> None:
        import substance_judge

        quotes = {
            "enseigne": "Passer de la représentation d'une base dans une autre avec une méthode explicite.",
            "fait pratiquer": "L'élève s'entraîne sur une conversion vérifiable.",
            "permet de se corriger": "Le corrigé donne la base de départ et la base d'arrivée.",
        }

        def fake_llm(_env: dict, _capacity_text: str, _section_text: str, role_label: str) -> dict:
            return {"taught": True, "citation": quotes[role_label], "justification": "preuve réelle"}

        with (
            patch.object(substance_judge, "ROOT", self.root),
            patch.object(substance_judge, "search_rag", return_value=[self.hit()]),
            patch.object(substance_judge, "call_llm", side_effect=fake_llm),
        ):
            cap = substance_judge.judge_capacity({}, capacity(), set())

        self.assertEqual(cap["verdict"], "needs_review")
        self.assertIn("proof_course", cap)
        self.assertIn("proof_practice", cap)
        self.assertIn("proof_correction", cap)
        self.assertNotIn("roles", cap)
        self.assertTrue(cap["proof_course"]["present"])
        self.assertIn("lexical_", cap["proof_course"]["note"])
        self.assertNotEqual(cap["verdict"], "validated_pedagogy")

    def test_hallucinated_quote_is_rejected(self) -> None:
        import substance_judge

        with (
            patch.object(substance_judge, "ROOT", self.root),
            patch.object(substance_judge, "search_rag", return_value=[self.hit()]),
            patch.object(
                substance_judge,
                "call_llm",
                return_value={"taught": True, "citation": "Citation absente du fichier source.", "justification": "non"},
            ),
        ):
            cap = substance_judge.judge_capacity({}, capacity(), set())

        self.assertEqual(cap["verdict"], "needs_content")
        self.assertFalse(cap["proof_course"]["present"])
        self.assertIn("citation_introuvable", cap["proof_course"]["note"])

    def test_quote_with_different_spacing_is_accepted(self) -> None:
        import substance_judge

        with (
            patch.object(substance_judge, "ROOT", self.root),
            patch.object(substance_judge, "search_rag", return_value=[self.hit()]),
            patch.object(
                substance_judge,
                "call_llm",
                return_value={"taught": True, "citation": "Citation avec espaces multiples.", "justification": "ok"},
            ),
        ):
            cap = substance_judge.judge_capacity({}, capacity(), set())

        self.assertTrue(cap["proof_course"]["present"])

    def test_boilerplate_and_reused_citation_are_rejected(self) -> None:
        import substance_judge

        with (
            patch.object(substance_judge, "ROOT", self.root),
            patch.object(substance_judge, "search_rag", return_value=[self.hit()]),
            patch.object(
                substance_judge,
                "call_llm",
                return_value={
                    "taught": True,
                    "citation": "Objectif O1 - Identifier précisément la représentation.",
                    "justification": "non",
                },
            ),
        ):
            boilerplate = substance_judge.judge_capacity({}, capacity(), set())
        self.assertFalse(boilerplate["proof_course"]["present"])
        self.assertIn("boilerplate", boilerplate["proof_course"]["note"])

        reused_quote = "Passer de la représentation d'une base dans une autre avec une méthode explicite."
        with (
            patch.object(substance_judge, "ROOT", self.root),
            patch.object(substance_judge, "search_rag", return_value=[self.hit()]),
            patch.object(
                substance_judge,
                "call_llm",
                return_value={"taught": True, "citation": reused_quote, "justification": "ok"},
            ),
        ):
            reused = substance_judge.judge_capacity({}, capacity(), set())
        self.assertTrue(reused["proof_course"]["present"])
        self.assertFalse(reused["proof_practice"]["present"])
        self.assertIn("citation_reused", reused["proof_practice"]["note"])

    def test_offline_fixture_writes_schema_a_json(self) -> None:
        output = self.root / "out.json"
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "substance_judge.py"),
                "--offline-fixture",
                "--unit",
                "P05",
                "--output",
                str(output),
            ],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=60,
        )

        self.assertEqual(result.returncode, 0, result.stdout)
        payload = json.loads(output.read_text(encoding="utf-8"))
        self.assertEqual(payload["schema_version"], "1.0.0")
        self.assertEqual({cap["verdict"] for cap in payload["capacities"]}, {"needs_content"})


class SubstanceAnchorStrictCitationTests(unittest.TestCase):
    def test_strict_citation_status_accepts_only_case_sensitive_spacing_normalization(self) -> None:
        from check_substance_anchors import citation_status

        body = "Citation avec\nespaces   multiples."

        self.assertEqual(citation_status("Citation avec espaces multiples.", body, strict=True)[0], "normalized")
        self.assertEqual(citation_status("citation avec espaces multiples.", body, strict=True)[0], "absent")


class TestNetworkGuard:
    def test_real_network_calls_are_blocked_in_tests(self) -> None:
        try:
            urllib.request.urlopen("https://example.invalid", timeout=1)
        except AssertionError as exc:
            assert "réseau réel interdit" in str(exc)
        else:
            raise AssertionError("urlopen réel non bloqué")


class SubstanceReviewsIndexTests(unittest.TestCase):
    def test_eight_pilot_units_are_listed_as_needs_content(self) -> None:
        text = (ROOT / "substance_reviews_index.md").read_text(encoding="utf-8")
        for unit in ("P05", "P06", "T06", "T07", "T08", "T10", "T17", "T18"):
            self.assertIn(f"| {unit} |", text)
        self.assertNotIn("validated_pedagogy", text)
        self.assertIn("covered = 0", text)
        self.assertIn("validated_* = 0", text)
        self.assertIn("published = 0", text)


if __name__ == "__main__":
    unittest.main()
