from __future__ import annotations

import io
import unittest
import requests
import csv
from contextlib import redirect_stdout
from collections import deque
from tempfile import TemporaryDirectory
from pathlib import Path
from unittest.mock import patch

import scraper_nsi_v2 as scraper_module
from scraper_nsi_v2 import (
    DuplicateIndex,
    clean_filename,
    clean_folder_name,
    dedupe_preserve_order,
    download_file,
    dynamic_site_name,
    extract_links_from_html,
    fetch_html,
    filename_from_url,
    github_archive_urls,
    internal_scope_prefix,
    is_html_like_url,
    is_internal_html_url,
    is_annuaire_site,
    is_target_file_url,
    normalize_href,
    polite_pause,
    process_target_files,
    scrape_site,
    should_ignore_external_domain,
    site_output_folder,
    load_csv_sites,
    SiteStats,
)


class ScraperNsiV2HelpersTest(unittest.TestCase):
    def test_normalize_href_replaces_backslashes_before_resolution(self):
        self.assertEqual(
            normalize_href(r"NSI_premiere\NSI_premierePDF\cours.pdf"),
            "NSI_premiere/NSI_premierePDF/cours.pdf",
        )

    def test_detects_target_files_after_backslash_normalization(self):
        base = "https://prolifaxe.github.io/coursdecourtois/NSI_1ere.html"
        links = extract_links_from_html(
            '<a href="NSI_premiere\\NSI_premierePDF\\cours.pdf">PDF</a>',
            base,
        )
        self.assertEqual(len(links.target_files), 1)
        self.assertTrue(links.target_files[0].endswith("/NSI_premiere/NSI_premierePDF/cours.pdf"))
        self.assertTrue(is_target_file_url(links.target_files[0]))

    def test_extract_links_ignores_empty_mailto_javascript_ftp_and_social_external(self):
        links = extract_links_from_html(
            """
            <a href="">Vide</a>
            <a href="mailto:test@example.test">Mail</a>
            <a href="javascript:void(0)">JS</a>
            <a href="ftp://example.test/file.pdf">FTP</a>
            <a href="https://youtube.com/watch?v=1">Social</a>
            """,
            "https://annuaire.example/",
            annuaire=True,
        )

        self.assertEqual(links.target_files, [])
        self.assertEqual(links.internal_pages, [])
        self.assertEqual(links.external_sites, [])

    def test_detects_same_domain_html_pages_for_depth_one_crawl(self):
        base = "https://glassus.github.io/premiere_nsi/"
        url = "https://glassus.github.io/premiere_nsi/T1_Demarrer_en_Python/1.1_Variables/cours/"
        self.assertTrue(is_internal_html_url(url, base))

    def test_annuaire_mode_collects_external_html_sites(self):
        base = "https://annuaire.example/cours/"
        links = extract_links_from_html(
            """
            <a href="https://collegue.example/nsi/">Site collègue</a>
            <a href="https://annuaire.example/cours/page2/">Interne</a>
            <a href="https://collegue.example/nsi/sujet.pdf">PDF direct externe</a>
            """,
            base,
            annuaire=True,
        )
        self.assertIn("https://collegue.example/nsi/", links.external_sites)
        self.assertNotIn("https://collegue.example/nsi/sujet.pdf", links.external_sites)

    def test_annuaire_can_be_detected_from_site_name(self):
        self.assertTrue(is_annuaire_site("Nathalie Bessonnet - Annuaire", "Forge HTML/MkDocs"))
        self.assertFalse(
            is_annuaire_site(
                "Annuaire - collegue.example",
                "Découvert via annuaire",
                discovered=True,
            )
        )

    def test_internal_scope_blocks_math93_college_from_nsi_entrypoint(self):
        base = "https://www.math93.com/index.php/lycee/1re-spe-nsi"
        scope = internal_scope_prefix(base)
        self.assertTrue(
            is_internal_html_url(
                "https://www.math93.com/index.php/lycee/1re-spe-nsi",
                base,
                scope_prefix=scope,
            )
        )
        self.assertFalse(
            is_internal_html_url(
                "https://www.math93.com/index.php/college/troisieme",
                base,
                scope_prefix=scope,
            )
        )

    def test_annuaire_external_sites_exclude_same_domain_navigation(self):
        base = "https://annuaire.example/cours/sites/"
        links = extract_links_from_html(
            """
            <a href="https://annuaire.example/cours/autre/">Même site</a>
            <a href="https://collegue.example/nsi/">Site collègue</a>
            """,
            base,
            annuaire=True,
            scope_prefix="/cours/sites/",
        )
        self.assertEqual(links.external_sites, ["https://collegue.example/nsi/"])

    def test_duplicate_index_detects_existing_file_names_across_roots(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            existing = root / "site_a" / "pdf"
            existing.mkdir(parents=True)
            (existing / "Cours NSI.pdf").write_bytes(b"deja extrait")

            index = DuplicateIndex.from_roots([root])

            self.assertTrue(index.has_filename("Cours NSI.pdf"))
            self.assertTrue(index.has_filename("cours nsi.pdf"))
            self.assertFalse(index.has_filename("autre.pdf"))

    def test_duplicate_index_ignores_absent_roots_and_registers_url(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            index = DuplicateIndex.from_roots([root / "absent"])
            target = root / "cours.pdf"
            target.write_bytes(b"cours")

            index.register_file("https://example.test/cours.pdf#section", target)

            self.assertTrue(index.has_url("https://example.test/cours.pdf"))
            self.assertTrue(index.has_filename("cours.pdf"))

    def test_filename_and_url_helpers_cover_fallbacks(self):
        self.assertEqual(clean_filename("!?"), "ressource")
        self.assertEqual(clean_folder_name("!?"), "site")
        self.assertEqual(filename_from_url("https://example.test/"), "")
        self.assertEqual(dedupe_preserve_order(["a", "b", "a"]), ["a", "b"])
        self.assertFalse(is_html_like_url("ftp://example.test/index.html"))
        self.assertTrue(is_html_like_url("https://example.test/"))
        self.assertFalse(is_html_like_url("https://example.test/style.css"))
        self.assertTrue(is_html_like_url("https://example.test/page.php"))
        self.assertEqual(internal_scope_prefix("https://example.test/cours/page.html"), "/cours/")
        self.assertEqual(internal_scope_prefix("https://example.test/cours"), "/cours/")
        self.assertTrue(should_ignore_external_domain("https://youtube.com/watch?v=1"))
        self.assertEqual(site_output_folder("Site Test"), scraper_module.OUTPUT_ROOT / "Site Test")

    def test_out_of_scope_platforms_are_explicitly_configured(self):
        self.assertIn("Éduscol STI - Hub Spécialité NSI", scraper_module.OUT_OF_SCOPE_SCRAPE_TARGETS)
        self.assertIn("Wikibooks - Communauté NSI", scraper_module.OUT_OF_SCOPE_SCRAPE_TARGETS)

    def test_download_skips_global_duplicate_without_network_request(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            existing = root / "site_a" / "pdf"
            target = root / "site_b" / "pdf"
            existing.mkdir(parents=True)
            (existing / "fiche.pdf").write_bytes(b"deja extrait")
            index = DuplicateIndex.from_roots([root])
            stats = SiteStats("Site B", "https://example.test/")

            with redirect_stdout(io.StringIO()), patch(
                "scraper_nsi_v2.requests.get",
                side_effect=AssertionError("network called"),
            ):
                self.assertTrue(
                    download_file(
                        "https://example.test/nouveau/fiche.pdf",
                        target,
                        stats,
                        duplicate_index=index,
                    )
                )

            self.assertEqual(stats.files_skipped, 1)
            self.assertFalse((target / "fiche.pdf").exists())

    def test_download_handles_missing_filename_existing_file_http_error_and_success(self):
        class Response:
            def __init__(self, status_code: int, chunks: list[bytes] | None = None):
                self.status_code = status_code
                self._chunks = chunks or []

            def iter_content(self, chunk_size=8192):
                yield from self._chunks

        with TemporaryDirectory() as tmp:
            target = Path(tmp) / "pdf"
            stats = SiteStats("Site", "https://example.test/")
            duplicate_index = DuplicateIndex()

            with redirect_stdout(io.StringIO()):
                self.assertFalse(download_file("https://example.test/", target, stats))
            self.assertIn("Nom de fichier absent", stats.errors[0])

            existing = target / "cours.pdf"
            existing.parent.mkdir(parents=True)
            existing.write_bytes(b"existing")
            with redirect_stdout(io.StringIO()):
                self.assertTrue(
                    download_file(
                        "https://example.test/cours.pdf",
                        target,
                        stats,
                        duplicate_index=duplicate_index,
                    )
                )
            self.assertEqual(stats.files_skipped, 1)
            self.assertTrue(duplicate_index.has_filename("cours.pdf"))

            with redirect_stdout(io.StringIO()), patch(
                "scraper_nsi_v2.requests.get",
                return_value=Response(404),
            ):
                self.assertFalse(download_file("https://example.test/absent.pdf", target, stats))
            self.assertIn("Statut 404", stats.errors[-1])

            partial = target / "ok.pdf.part"
            partial.write_bytes(b"old")
            with redirect_stdout(io.StringIO()), patch(
                "scraper_nsi_v2.requests.get",
                return_value=Response(200, [b"new", b"", b" file"]),
            ):
                self.assertTrue(
                    download_file(
                        "https://example.test/ok.pdf",
                        target,
                        stats,
                        duplicate_index=duplicate_index,
                    )
                )
            self.assertEqual((target / "ok.pdf").read_bytes(), b"new file")
            self.assertFalse(partial.exists())
            self.assertTrue(duplicate_index.has_url("https://example.test/ok.pdf"))

    def test_github_repo_html_adds_default_branch_archive_url(self):
        html = '<a href="/DLatreyte/dlatreyte.github.io/tree/master">master</a>'

        self.assertEqual(
            github_archive_urls("https://github.com/DLatreyte/dlatreyte.github.io", html),
            ["https://github.com/DLatreyte/dlatreyte.github.io/archive/refs/heads/master.zip"],
        )

    def test_github_archive_filename_is_repo_specific_to_avoid_master_zip_collision(self):
        self.assertEqual(
            filename_from_url(
                "https://github.com/DLatreyte/dlatreyte.github.io/archive/refs/heads/master.zip"
            ),
            "DLatreyte_dlatreyte.github.io_master.zip",
        )

    def test_github_archive_urls_handles_non_repo_and_default_main(self):
        self.assertEqual(github_archive_urls("https://example.test/repo", ""), [])
        self.assertEqual(github_archive_urls("https://github.com/owner", ""), [])
        self.assertEqual(
            github_archive_urls("https://github.com/owner/repo", "<html></html>"),
            ["https://github.com/owner/repo/archive/refs/heads/main.zip"],
        )

    def test_fetch_html_and_polite_pause_cover_status_content_type_and_exception(self):
        class Response:
            def __init__(self, status_code: int, content_type: str = "text/html", text: str = "ok"):
                self.status_code = status_code
                self.headers = {"content-type": content_type}
                self.text = text

        with patch.object(scraper_module, "POLITE_DELAY_SECONDS", 0.25), patch(
            "scraper_nsi_v2.time.sleep"
        ) as sleep:
            polite_pause()
        sleep.assert_called_once_with(0.25)
        with patch.object(scraper_module, "POLITE_DELAY_SECONDS", 0), patch(
            "scraper_nsi_v2.time.sleep"
        ) as sleep:
            polite_pause()
        sleep.assert_not_called()

        with patch.object(scraper_module, "polite_pause"), patch(
            "scraper_nsi_v2.requests.get",
            return_value=Response(500),
        ):
            html, error = fetch_html("https://example.test/")
        self.assertIsNone(html)
        self.assertIn("Statut 500", error)

        with patch.object(scraper_module, "polite_pause"), patch(
            "scraper_nsi_v2.requests.get",
            return_value=Response(200, "application/pdf"),
        ):
            html, error = fetch_html("https://example.test/file.pdf")
        self.assertIsNone(html)
        self.assertIn("Contenu non HTML", error)

        with patch.object(scraper_module, "polite_pause"), patch(
            "scraper_nsi_v2.requests.get",
            return_value=Response(200, "", "<h1>OK</h1>"),
        ):
            html, error = fetch_html("https://example.test/page")
        self.assertEqual((html, error), ("<h1>OK</h1>", None))

        with patch.object(scraper_module, "polite_pause"), patch(
            "scraper_nsi_v2.requests.get",
            side_effect=requests.exceptions.Timeout("slow"),
        ):
            html, error = fetch_html("https://example.test/slow")
        self.assertIsNone(html)
        self.assertIn("Exception requête", error)

    def test_download_failure_does_not_leave_partial_final_file(self):
        class BrokenResponse:
            status_code = 200

            def iter_content(self, chunk_size=8192):
                yield b"debut archive"
                raise requests.exceptions.ChunkedEncodingError("connexion coupee")

        with TemporaryDirectory() as tmp:
            target = Path(tmp) / "site" / "zip"
            stats = SiteStats("Site", "https://example.test/")

            with redirect_stdout(io.StringIO()), patch(
                "scraper_nsi_v2.requests.get",
                return_value=BrokenResponse(),
            ):
                self.assertFalse(download_file("https://example.test/archive.zip", target, stats))

            self.assertFalse((target / "archive.zip").exists())
            self.assertFalse((target / "archive.zip.part").exists())
            self.assertEqual(len(stats.errors), 1)

    def test_download_request_exception_before_partial_path_is_recorded(self):
        with TemporaryDirectory() as tmp:
            target = Path(tmp) / "site" / "zip"
            stats = SiteStats("Site", "https://example.test/")

            with redirect_stdout(io.StringIO()), patch(
                "scraper_nsi_v2.requests.get",
                side_effect=requests.exceptions.Timeout("timeout"),
            ):
                self.assertFalse(download_file("https://example.test/archive.zip", target, stats))

            self.assertEqual(len(stats.errors), 1)
            self.assertIn("timeout", stats.errors[0])
            self.assertTrue(target.exists())
            self.assertEqual(list(target.iterdir()), [])

    def test_download_existing_file_without_duplicate_index_and_success_without_index(self):
        class Response:
            status_code = 200

            def iter_content(self, chunk_size=8192):
                yield b"ok"

        with TemporaryDirectory() as tmp:
            target = Path(tmp) / "pdf"
            stats = SiteStats("Site", "https://example.test/")
            existing = target / "cours.pdf"
            existing.parent.mkdir(parents=True)
            existing.write_bytes(b"existing")

            with redirect_stdout(io.StringIO()):
                self.assertTrue(download_file("https://example.test/cours.pdf", target, stats))
            self.assertEqual(stats.files_skipped, 1)

            with redirect_stdout(io.StringIO()), patch(
                "scraper_nsi_v2.requests.get",
                return_value=Response(),
            ):
                self.assertTrue(download_file("https://example.test/new.pdf", target, stats))
            self.assertEqual((target / "new.pdf").read_bytes(), b"ok")
            self.assertEqual(stats.files_downloaded, 1)

    def test_process_target_files_routes_by_extension(self):
        stats = SiteStats("Site", "https://example.test/")
        with TemporaryDirectory() as tmp:
            site_folder = Path(tmp)
            with patch("scraper_nsi_v2.download_file") as download:
                process_target_files(
                    ["https://example.test/a.PDF", "https://example.test/notebook.ipynb"],
                    site_folder,
                    stats,
                    duplicate_index=None,
                )

            self.assertEqual(download.call_count, 2)
            self.assertEqual(download.call_args_list[0].args[1], site_folder / "pdf")
            self.assertEqual(download.call_args_list[1].args[1], site_folder / "ipynb")

    def test_scrape_site_crawls_internal_pages_and_collects_annuaire_external_sites(self):
        base = "https://annuaire.example/cours/"
        page_html = """
        <a href="fiche.pdf">PDF</a>
        <a href="page2/">Interne</a>
        <a href="https://collegue.example/nsi/">Collègue</a>
        """
        page2_html = '<a href="tp.py">TP</a>'

        def fake_fetch(url: str):
            if url == base:
                return page_html, None
            if url == "https://annuaire.example/cours/page2/":
                return page2_html, None
            return None, f"unexpected {url}"

        with redirect_stdout(io.StringIO()), patch.object(
            scraper_module,
            "MAX_DEPTH",
            1,
        ), patch.object(scraper_module, "MAX_SUBPAGES_PER_SITE", 10), patch(
            "scraper_nsi_v2.fetch_html",
            side_effect=fake_fetch,
        ), patch("scraper_nsi_v2.process_target_files") as process_files:
            stats, external = scrape_site(
                "Annuaire NSI",
                base,
                "Annuaire",
                duplicate_index=DuplicateIndex(),
            )

        self.assertEqual(stats.pages_seen, 2)
        self.assertEqual(external, ["https://collegue.example/nsi/"])
        self.assertEqual(stats.external_sites_discovered, 1)
        self.assertEqual(process_files.call_count, 2)

    def test_scrape_site_records_page_errors_and_limits_subpages(self):
        base = "https://example.test/root/"
        html = """
        <a href="a/">A</a>
        <a href="b/">B</a>
        """

        def fake_fetch(url: str):
            if url == base:
                return html, None
            return None, "boom"

        with redirect_stdout(io.StringIO()), patch.object(
            scraper_module,
            "MAX_DEPTH",
            1,
        ), patch.object(scraper_module, "MAX_SUBPAGES_PER_SITE", 1), patch(
            "scraper_nsi_v2.fetch_html",
            side_effect=fake_fetch,
        ), patch("scraper_nsi_v2.process_target_files"):
            stats, external = scrape_site("Site", base, "Cours")

        self.assertEqual(stats.pages_seen, 2)
        self.assertEqual(len(stats.errors), 1)
        self.assertEqual(external, [])

    def test_scrape_site_handles_none_html_and_self_links_without_queue_growth(self):
        base = "https://example.test/root/"

        with redirect_stdout(io.StringIO()), patch.object(
            scraper_module,
            "MAX_DEPTH",
            1,
        ), patch(
            "scraper_nsi_v2.fetch_html",
            return_value=(None, None),
        ), patch("scraper_nsi_v2.process_target_files") as process_files:
            stats, external = scrape_site("Site", base, "Cours")

        self.assertEqual(stats.pages_seen, 1)
        self.assertEqual(stats.errors, [])
        self.assertEqual(external, [])
        process_files.assert_not_called()

        html = '<a href="https://example.test/root/">Self</a>'
        with redirect_stdout(io.StringIO()), patch.object(
            scraper_module,
            "MAX_DEPTH",
            1,
        ), patch(
            "scraper_nsi_v2.fetch_html",
            return_value=(html, None),
        ), patch("scraper_nsi_v2.process_target_files"):
            stats, _external = scrape_site("Site", base, "Cours")

        self.assertEqual(stats.pages_seen, 1)

    def test_scrape_site_skips_url_already_visited_if_queue_contains_duplicate(self):
        base = "https://example.test/root/"

        def duplicate_deque(initial):
            queue = deque(initial)
            if initial:
                queue.append(initial[0])
            return queue

        with redirect_stdout(io.StringIO()), patch(
            "scraper_nsi_v2.deque",
            side_effect=duplicate_deque,
        ), patch("scraper_nsi_v2.fetch_html", return_value=(None, None)), patch(
            "scraper_nsi_v2.process_target_files"
        ):
            stats, external = scrape_site("Site", base, "Cours")

        self.assertEqual(stats.pages_seen, 1)
        self.assertEqual(external, [])

    def test_load_csv_dynamic_name_and_main_are_exercised_without_network(self):
        with TemporaryDirectory() as tmp:
            csv_path = Path(tmp) / "sites.csv"
            with csv_path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=["Nom_Site", "URL", "Type_Structure"])
                writer.writeheader()
                writer.writerow(
                    {
                        "Nom_Site": "Annuaire",
                        "URL": "https://annuaire.example/#top",
                        "Type_Structure": "Annuaire",
                    }
                )
                writer.writerow(
                    {"Nom_Site": "", "URL": "https://ignored.example/", "Type_Structure": ""}
                )

            with redirect_stdout(io.StringIO()) as csv_output:
                loaded_sites = load_csv_sites(str(csv_path))
            self.assertEqual(
                loaded_sites,
                [("Annuaire", "https://annuaire.example/", "Annuaire")],
            )
            self.assertIn("[CSV IGNORÉ] ligne 3 incomplète", csv_output.getvalue())
            self.assertEqual(
                dynamic_site_name("https://collegue.example/nsi/cours/"),
                "Annuaire - collegue.example - nsi_cours",
            )
            self.assertEqual(
                dynamic_site_name("https://collegue.example/"),
                "Annuaire - collegue.example",
            )

            with self.assertRaises(SystemExit):
                with redirect_stdout(io.StringIO()):
                    load_csv_sites(str(Path(tmp) / "missing.csv"))

            def fake_scrape(site_name, url, structure, discovered=False, duplicate_index=None):
                if not discovered:
                    return SiteStats(site_name, url, pages_seen=1), [
                        "https://annuaire.example/",
                        "https://new.example/nsi/",
                    ]
                return SiteStats(site_name, url, discovered_from_annuaire=True, pages_seen=1), []

            with redirect_stdout(io.StringIO()), patch.object(
                scraper_module,
                "CSV_FILE",
                str(csv_path),
            ), patch.object(
                scraper_module,
                "DUPLICATE_SCAN_ROOTS",
                (Path(tmp) / "missing",),
            ), patch(
                "scraper_nsi_v2.scrape_site",
                side_effect=fake_scrape,
            ):
                scraper_module.main()


if __name__ == "__main__":
    unittest.main()
