from __future__ import annotations

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

import audit_reconciliation as audit_module


class AuditReconciliationTest(unittest.TestCase):
    def test_missing_configured_out_of_scope_site_is_not_counted_as_scrape_missing(self) -> None:
        with TemporaryDirectory() as tmp:
            v2_root = Path(tmp) / "ressources_nsi_extraites_v2"
            v2_root.mkdir()
            rows = [
                {
                    "Nom_Site": "Éduscol STI - Hub Spécialité NSI",
                    "URL": "https://sti.eduscol.education.fr/formations/bac-voie-generale/specialite-nsi-numerique-et-sciences-informatiques",
                    "Type_Structure": "HTML / PDF / ZIP",
                }
            ]

            with patch.object(audit_module, "V2_DIR", v2_root), patch.object(
                audit_module,
                "read_scrape_rows",
                return_value=rows,
            ):
                statuses = audit_module.audit_scraping()

        self.assertEqual(len(statuses), 1)
        self.assertEqual(statuses[0].status, "excluded_out_of_scope")
        self.assertEqual(statuses[0].valid_file_count, 0)


if __name__ == "__main__":
    unittest.main()
