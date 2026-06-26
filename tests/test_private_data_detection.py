from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_no_private_data as privacy


class PrivateDataDetectionTest(unittest.TestCase):
    def test_year_range_is_not_tunisian_phone(self) -> None:
        text = "Documents_DRIVE/9_NSI_2025-2026/sequence.pdf"
        matches = [match.group(0) for match in privacy.TN_PHONE_RE.finditer(text)]

        self.assertTrue(all(privacy.YEAR_RANGE_RE.fullmatch(value) for value in matches))

    def test_hash_fragment_is_not_tunisian_phone(self) -> None:
        text = "242224f04a4ae0efd8ed2a17e8d74b054f8d53e33eb1e33ae163c62f" + "24" + "170779,non"

        self.assertEqual(list(privacy.TN_PHONE_RE.finditer(text)), [])

    def test_standalone_tunisian_phone_is_detected(self) -> None:
        value = "24" + "170779"
        text = "Contact temporaire " + value

        self.assertEqual([match.group(0) for match in privacy.TN_PHONE_RE.finditer(text)], [value])


if __name__ == "__main__":
    unittest.main()
