import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))


class StatusPromotionGuardTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "00_programmes_officiels").mkdir()
        (self.root / "substance_reviews").mkdir()
        (self.root / "reviewer_confirmations").mkdir()
        (self.root / "source.md").write_text(
            "# Section\n\n"
            "Passer de la représentation d'une base dans une autre avec une méthode explicite.\n"
            "L'élève s'entraîne sur une conversion vérifiable.\n"
            "Le corrigé donne la base de départ et la base d'arrivée.\n",
            encoding="utf-8",
        )
        (self.root / "00_programmes_officiels" / "programme_nsi_2019.yaml").write_text(
            "programmes:\n"
            "  premiere:\n"
            "    - id: P-DATA-BASE-01\n"
            "      capacite_attendue:\n"
            "        - Passer de la représentation d'une base dans une autre.\n"
            "      niveau: premiere\n"
            "  terminale: []\n",
            encoding="utf-8",
        )
        (self.root / "substance_verdict.schema.json").write_text(
            (ROOT / "substance_verdict.schema.json").read_text(encoding="utf-8"),
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def write_valid_verdict(self) -> Path:
        verdict = {
            "schema_version": "1.0.0",
            "unit": "P01",
            "level": "premiere",
            "judged_at": "2026-06-28T20:00:00Z",
            "judge_model": "human-reviewer",
            "author_model": "author",
            "capacities": [
                {
                    "capacity_id": "P-DATA-BASE-01",
                    "official_label": "Passer de la représentation d'une base dans une autre.",
                    "proof_course": {
                        "present": True,
                        "file": "source.md",
                        "anchor": "#section",
                        "quote": "Passer de la représentation d'une base dans une autre avec une méthode explicite.",
                        "teaches": True,
                    },
                    "proof_practice": {
                        "present": True,
                        "file": "source.md",
                        "anchor": "#section",
                        "quote": "L'élève s'entraîne sur une conversion vérifiable.",
                        "teaches": True,
                    },
                    "proof_correction": {
                        "present": True,
                        "file": "source.md",
                        "anchor": "#section",
                        "quote": "Le corrigé donne la base de départ et la base d'arrivée.",
                        "teaches": True,
                    },
                    "verdict": "validated_pedagogy",
                    "justification": "Les trois preuves sont présentes, citées et vérifiables mécaniquement.",
                    "scientific_flags": [],
                }
            ],
        }
        path = self.root / "substance_reviews" / "P01.valid.json"
        path.write_text(json.dumps(verdict, ensure_ascii=False), encoding="utf-8")
        return path

    def run_guard(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check_status_promotion_guard.py"), "--root", str(self.root)],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=60,
        )

    def test_canonical_verdict_hash_is_reproducible(self) -> None:
        from check_status_promotion_guard import canonical_verdict_hash

        first = {"b": [1, 2], "a": {"x": " y "}}
        second = {"a": {"x": " y "}, "b": [1, 2]}
        changed = {"a": {"x": "z"}, "b": [1, 2]}

        self.assertEqual(canonical_verdict_hash(first), canonical_verdict_hash(second))
        self.assertNotEqual(canonical_verdict_hash(first), canonical_verdict_hash(changed))

    def test_rejects_reverted_fraud_report_without_proof(self) -> None:
        report = "\n".join(
            [
                "# Rapport de substance frauduleux reconstruit",
                "",
                "validated_pedagogy: 15",
                "",
                "| Capacité | Verdict |",
                "| --- | --- |",
                *[
                    f"| P-FAKE-{index:02d} | validated_pedagogy |"
                    for index in range(1, 16)
                ],
            ]
        )
        review = {
            "schema_version": "1.0.0",
            "unit": "FRAUD",
            "level": "premiere",
            "judged_at": "2026-06-28T20:00:00Z",
            "judge_model": "fraudulent-fixture",
            "author_model": "unknown",
            "capacities": [
                {
                    "capacity_id": f"P-FAKE-{index:02d}",
                    "official_label": "Capacité fictive",
                    "proof_course": {"present": False, "teaches": False},
                    "proof_practice": {"present": False, "teaches": False},
                    "proof_correction": {"present": False, "teaches": False},
                    "verdict": "validated_pedagogy",
                    "justification": "Promotion sans preuve mécanique.",
                    "scientific_flags": [],
                }
                for index in range(1, 16)
            ],
        }
        (self.root / "substance_report.md").write_text(report, encoding="utf-8")
        (self.root / "substance_review.json").write_text(
            json.dumps(review, ensure_ascii=False),
            encoding="utf-8",
        )

        result = self.run_guard()

        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn("validated_pedagogy", result.stdout)

    def test_rejects_covered_without_valid_verdict(self) -> None:
        (self.root / "coverage.md").write_text(
            "- covered : 1\n\n| Capacité | Statut |\n|---|---|\n| P-DATA-BASE-01 | covered |\n",
            encoding="utf-8",
        )

        result = self.run_guard()

        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn("covered", result.stdout)

    def test_rejects_published_without_reviewer_confirmation(self) -> None:
        self.write_valid_verdict()
        (self.root / "manifest.csv").write_text(
            "id,statut\nP-DATA-BASE-01,published\n",
            encoding="utf-8",
        )

        result = self.run_guard()

        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn("confirmation", result.stdout)

    def test_accepts_promotion_with_valid_verdict_and_confirmation(self) -> None:
        from check_status_promotion_guard import canonical_verdict_hash

        verdict_path = self.write_valid_verdict()
        verdict = json.loads(verdict_path.read_text(encoding="utf-8"))
        (self.root / "reviewer_confirmations" / "P-DATA-BASE-01.json").write_text(
            json.dumps(
                {
                    "capacite_id": "P-DATA-BASE-01",
                    "verdict_hash": canonical_verdict_hash(verdict),
                    "relecteur": "Relecteur NSI",
                    "date": "2026-06-28",
                    "marqueur": "confirmation_humaine_tracee",
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        (self.root / "manifest.csv").write_text(
            "id,statut\nP-DATA-BASE-01,validated_pedagogy\n",
            encoding="utf-8",
        )

        result = self.run_guard()

        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("check_status_promotion_guard: PASS", result.stdout)


if __name__ == "__main__":
    unittest.main()
