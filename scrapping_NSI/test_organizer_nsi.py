from __future__ import annotations

import io
import json
import unittest
import zipfile
from collections import Counter
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

import organizer_nsi as organizer_module
from organizer_nsi import (
    classify_destination,
    compute_sha256,
    extract_zip_to_transit,
    integrate_drive_dir,
    main,
    organize_transit,
    organize_file,
    safe_filename,
    seed_existing_hashes,
    should_skip,
    unique_nested_destination,
)


class OrganizerNsiTest(unittest.TestCase):
    def test_classifies_premiere_tp_notebook(self):
        path = Path("/tmp/nsi_transit/site/1ere_nsi/tp_variables.ipynb")

        self.assertEqual(
            classify_destination(path),
            Path("01_Premiere_NSI/04_TP"),
        )

    def test_classifies_terminale_bac_subject_as_evaluation(self):
        path = Path("/tmp/nsi_transit/site/TNSI/sujet_bac_graphes.pdf")

        self.assertEqual(
            classify_destination(path),
            Path("02_Terminale_NSI/07_Evaluations"),
        )

    def test_classifies_programme_and_swinnen_as_transversal_or_official(self):
        self.assertEqual(
            classify_destination(Path("/tmp/nsi_transit/eduscol/boenjs_nsi.pdf")),
            Path("00_Programmes_et_Informations"),
        )
        self.assertEqual(
            classify_destination(Path("/tmp/nsi_transit/swinnen/apprendre_python.pdf")),
            Path("03_Autres_et_Transversal"),
        )

    def test_classifies_all_document_type_markers_and_unclassified_fallback(self):
        cases = {
            "/tmp/1ere/projet_final.pdf": Path("01_Premiere_NSI/06_Projets"),
            "/tmp/1ere/fiche_resume.pdf": Path("01_Premiere_NSI/02_Fiches_et_Syntheses"),
            "/tmp/1ere/exercices_listes.pdf": Path("01_Premiere_NSI/03_TD"),
            "/tmp/1ere/script_autonome.py": Path("01_Premiere_NSI/05_Programmation"),
            "/tmp/1ere/document_inclassable.bin": Path("03_Autres_et_Transversal"),
        }

        for raw_path, expected in cases.items():
            with self.subTest(raw_path=raw_path):
                self.assertEqual(classify_destination(Path(raw_path)), expected)

        self.assertEqual(
            organizer_module.classify_level(Path("/tmp/ressource_inconnue.pdf")),
            organizer_module.LEVEL_TRANSVERSAL,
        )

    def test_low_level_helpers_cover_fallbacks_and_skips(self):
        self.assertEqual(organizer_module.safe_filename("!!!.pdf"), "ressource.pdf")
        self.assertEqual(organizer_module.safe_stem("!!!"), "ressource")
        self.assertEqual(
            organizer_module.safe_relative_path(Path("Dossier élève/!!!.pdf")),
            Path("Dossier_eleve/ressource.pdf"),
        )
        self.assertTrue(should_skip(Path("/tmp/.venv/module.py")))
        self.assertTrue(should_skip(Path("/tmp/cache.pyc")))
        self.assertFalse(should_skip(Path("/tmp/.nojekyll")))

    def test_hash_deduplicates_content_even_when_names_differ(self):
        with TemporaryDirectory() as tmp:
            transit = Path(tmp) / "transit"
            final = Path(tmp) / "final"
            source_a = transit / "Gilles Lassus" / "premiere" / "cours.pdf"
            source_b = transit / "Autre Site" / "1ere" / "copie.pdf"
            source_a.parent.mkdir(parents=True)
            source_b.parent.mkdir(parents=True)
            source_a.write_bytes(b"meme contenu")
            source_b.write_bytes(b"meme contenu")
            hashes = {}
            counts = {}

            first = organize_file(source_a, transit, final, hashes, counts)
            second = organize_file(source_b, transit, final, hashes, counts)

            self.assertEqual(first.status, "copied")
            self.assertEqual(second.status, "duplicate")
            self.assertEqual(len(list(final.rglob("*.pdf"))), 1)

    def test_filename_collision_keeps_both_unique_files_with_origin_suffix(self):
        with TemporaryDirectory() as tmp:
            transit = Path(tmp) / "transit"
            final = Path(tmp) / "final"
            source_a = transit / "Site A" / "premiere" / "cours.pdf"
            source_b = transit / "Site B" / "premiere" / "cours.pdf"
            source_a.parent.mkdir(parents=True)
            source_b.parent.mkdir(parents=True)
            source_a.write_bytes(b"contenu A")
            source_b.write_bytes(b"contenu B")
            hashes = {}
            counts = {}

            organize_file(source_a, transit, final, hashes, counts)
            result = organize_file(source_b, transit, final, hashes, counts)

            self.assertEqual(result.status, "copied_renamed")
            files = sorted(p.name for p in final.rglob("*.pdf"))
            self.assertEqual(files, ["cours.pdf", "cours_Site_B.pdf"])

    def test_extract_zip_removes_archive_only_after_valid_extraction(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive = root / "pack.zip"
            with zipfile.ZipFile(archive, "w") as zf:
                zf.writestr("premiere/tp.py", "print('ok')\n")

            extracted = extract_zip_to_transit(archive, root)

            self.assertEqual(extracted, 1)
            self.assertFalse(archive.exists())
            self.assertTrue((root / "_extracted_zips" / "pack" / "premiere" / "tp.py").exists())

    def test_extract_zip_uses_numbered_directory_when_extract_base_exists(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive = root / "pack.zip"
            occupied = root / "_extracted_zips" / "pack"
            occupied.mkdir(parents=True)
            with zipfile.ZipFile(archive, "w") as zf:
                zf.writestr("cours.pdf", "ok")

            extracted = extract_zip_to_transit(archive, root)

            self.assertEqual(extracted, 1)
            self.assertTrue((root / "_extracted_zips" / "pack_2" / "cours.pdf").exists())

    def test_encrypted_zip_is_reported_without_crashing_or_deleting_archive(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive = root / "encrypted.zip"
            archive.write_bytes(b"fake zip marker")

            with redirect_stdout(io.StringIO()), patch(
                "organizer_nsi.zipfile.is_zipfile",
                return_value=True,
            ), patch("organizer_nsi.zipfile.ZipFile") as zip_cls:
                zip_cls.return_value.__enter__.return_value.testzip.side_effect = RuntimeError(
                    "password required for extraction"
                )
                extracted = extract_zip_to_transit(archive, root)

            self.assertEqual(extracted, 0)
            self.assertTrue(archive.exists())

    def test_failed_zip_marker_is_not_centralized_as_resource(self):
        path = Path("/tmp/nsi_transit/source/NSI_1iere_S1_DRco.zip.failed")

        self.assertTrue(should_skip(path))

    def test_origin_helpers_cover_outside_empty_and_extracted_paths(self):
        with TemporaryDirectory() as tmp:
            transit = Path(tmp) / "transit"
            drive = Path(tmp) / "drive"

            self.assertEqual(
                organizer_module.origin_name(Path(tmp) / "outside.pdf", transit),
                "source",
            )
            self.assertEqual(organizer_module.origin_name(transit, transit), "source")
            self.assertEqual(
                organizer_module.origin_name(
                    transit / "ressources_nsi_extraites" / "Site A" / "cours.pdf",
                    transit,
                ),
                "Site A",
            )
            self.assertEqual(
                organizer_module.origin_name(
                    transit / "_extracted_zips" / "archive" / "tp.py",
                    transit,
                ),
                "archive",
            )
            self.assertEqual(
                organizer_module.drive_origin_name(Path(tmp) / "outside.pdf", drive),
                "Documents_DRIVE",
            )
            self.assertEqual(organizer_module.drive_origin_name(drive, drive), "Documents_DRIVE")

    def test_unique_destination_counters_after_repeated_collisions(self):
        with TemporaryDirectory() as tmp:
            destination_dir = Path(tmp)
            (destination_dir / "cours.pdf").write_bytes(b"a")
            (destination_dir / "cours_Site.pdf").write_bytes(b"b")

            destination, renamed = organizer_module.unique_destination(
                destination_dir,
                "cours.pdf",
                "Site",
            )

            self.assertTrue(renamed)
            self.assertEqual(destination, destination_dir / "cours_Site_2.pdf")

            nested_base = Path(tmp) / "nested"
            existing = nested_base / "assets" / "style.css"
            first_collision = nested_base / "assets" / "style_Site.css"
            existing.parent.mkdir(parents=True)
            existing.write_bytes(b"a")
            first_collision.write_bytes(b"b")
            nested_destination, nested_renamed = organizer_module.unique_nested_destination(
                nested_base,
                Path("assets/style.css"),
                "Site",
            )
            self.assertTrue(nested_renamed)
            self.assertEqual(nested_destination, nested_base / "assets" / "style_Site_2.css")

    def test_drive_asset_helpers_cover_outside_and_non_asset_paths(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            drive = root / "drive"
            outside_asset = root / "outside" / "assets" / "image.png"
            regular = drive / "Premiere" / "cours.pdf"

            self.assertTrue(organizer_module.is_structured_drive_asset(outside_asset, drive))
            self.assertFalse(organizer_module.is_structured_drive_asset(regular, drive))
            self.assertIsNone(organizer_module.drive_asset_container(regular, drive))
            self.assertIsNone(
                organizer_module.drive_asset_container(root / "outside" / "cours.pdf", drive)
            )

    def test_integrate_drive_dir_processes_all_initial_files_while_pruning_drive(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            drive = root / "Documents_DRIVE"
            final = root / "ressources_nsi_centralisees"
            first = drive / "Premiere" / "Cours A.pdf"
            second = drive / "Terminale" / "Cours B.pdf"
            junk = drive / "Premiere" / "assets" / ".DS_Store"
            first.parent.mkdir(parents=True)
            second.parent.mkdir(parents=True)
            junk.parent.mkdir(parents=True)
            first.write_bytes(b"premiere")
            second.write_bytes(b"terminale")
            junk.write_bytes(b"metadata")

            counts = integrate_drive_dir(drive, final, {}, {})

            self.assertEqual(counts["drive_moved"], 2)
            self.assertEqual(counts["drive_junk_deleted"], 1)
            self.assertTrue((final / "01_Premiere_NSI" / "01_Cours" / "Cours_A.pdf").exists())
            self.assertTrue((final / "02_Terminale_NSI" / "01_Cours" / "Cours_B.pdf").exists())
            self.assertEqual([p for p in drive.rglob("*")], [])

    def test_drive_missing_and_disappearing_file_are_reported_without_crash(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            missing_drive = root / "missing"
            final = root / "final"

            with redirect_stdout(io.StringIO()):
                missing_counts = integrate_drive_dir(missing_drive, final, {}, {})
            self.assertEqual(missing_counts["drive_missing"], 1)

            drive = root / "drive"
            first = drive / "Premiere" / "Cours A.pdf"
            second = drive / "Premiere" / "Cours B.pdf"
            first.parent.mkdir(parents=True)
            first.write_bytes(b"a")
            second.write_bytes(b"b")
            original_move = organizer_module.move_drive_file

            def remove_second_then_move(
                source,
                drive_root,
                final_root,
                seen_hashes,
                category_counts,
                registry=None,
            ):
                if source == first and second.exists():
                    second.unlink()
                return original_move(
                    source,
                    drive_root,
                    final_root,
                    seen_hashes,
                    category_counts,
                    registry=registry,
                )

            with patch.object(
                organizer_module,
                "move_drive_file",
                side_effect=remove_second_then_move,
            ):
                counts = integrate_drive_dir(drive, final, {}, {})

            self.assertEqual(counts["drive_moved"], 1)
            self.assertFalse(second.exists())

    def test_drive_file_is_moved_and_classified_into_final_tree(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            drive = root / "Documents_DRIVE"
            final = root / "ressources_nsi_centralisees"
            source = drive / "Algo_Premiere" / "Cours variables.pdf"
            source.parent.mkdir(parents=True)
            source.write_bytes(b"contenu drive premiere")
            hashes = {}
            category_counts = {}

            counts = integrate_drive_dir(drive, final, hashes, category_counts)

            destination = final / "01_Premiere_NSI" / "01_Cours" / "Cours_variables.pdf"
            self.assertFalse(source.exists())
            self.assertTrue(destination.exists())
            self.assertEqual(destination.read_bytes(), b"contenu drive premiere")
            self.assertEqual(counts["drive_moved"], 1)
            self.assertEqual(category_counts["01_Premiere_NSI/01_Cours"], 1)

    def test_drive_zip_is_evacuated_to_skipped_quarantine(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            drive = root / "Documents_DRIVE"
            final = root / "ressources_nsi_centralisees"
            archive = drive / "Premiere" / "pack.zip"
            archive.parent.mkdir(parents=True)
            archive.write_bytes(b"zip residue")

            counts = integrate_drive_dir(drive, final, {}, {})

            self.assertEqual(counts["drive_skipped"], 1)
            self.assertFalse(archive.exists())
            self.assertTrue((final / "_skipped_drive" / "Premiere" / "pack.zip").exists())

    def test_drive_duplicate_is_moved_to_duplicate_quarantine(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            drive = root / "Documents_DRIVE"
            final = root / "ressources_nsi_centralisees"
            existing = final / "01_Premiere_NSI" / "01_Cours" / "Cours_variables.pdf"
            duplicate = drive / "Algo_Premiere" / "copie_cours.pdf"
            existing.parent.mkdir(parents=True)
            duplicate.parent.mkdir(parents=True)
            existing.write_bytes(b"meme contenu")
            duplicate.write_bytes(b"meme contenu")
            hashes = {compute_sha256(existing): existing}
            category_counts = {}

            counts = integrate_drive_dir(drive, final, hashes, category_counts)

            quarantined = list((final / "_doublons_drive").rglob("copie_cours.pdf"))
            self.assertFalse(duplicate.exists())
            self.assertEqual(len(quarantined), 1)
            self.assertEqual(quarantined[0].read_bytes(), b"meme contenu")
            self.assertEqual(counts["drive_duplicate"], 1)
            self.assertEqual(category_counts, {})

    def test_drive_duplicate_is_detected_from_existing_final_tree_without_preseeded_hashes(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            drive = root / "Documents_DRIVE"
            final = root / "ressources_nsi_centralisees"
            existing = final / "01_Premiere_NSI" / "01_Cours" / "Cours_variables.pdf"
            duplicate = drive / "Algo_Premiere" / "copie_cours.pdf"
            existing.parent.mkdir(parents=True)
            duplicate.parent.mkdir(parents=True)
            existing.write_bytes(b"meme contenu")
            duplicate.write_bytes(b"meme contenu")
            hashes = {}
            category_counts = {}

            counts = integrate_drive_dir(drive, final, hashes, category_counts)

            self.assertFalse(duplicate.exists())
            self.assertEqual(counts["drive_duplicate"], 1)
            self.assertEqual(len(list((final / "_doublons_drive").rglob("copie_cours.pdf"))), 1)
            self.assertEqual(len(list(final.rglob("Cours_variables.pdf"))), 1)

    def test_drive_asset_keeps_container_relative_structure_inside_classified_folder(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            drive = root / "Documents_DRIVE"
            final = root / "ressources_nsi_centralisees"
            source = drive / "TP_Premiere" / "site" / "assets" / "style.css"
            source.parent.mkdir(parents=True)
            source.write_text("body { color: black; }\n", encoding="utf-8")

            counts = integrate_drive_dir(drive, final, {}, {})

            destination = (
                final
                / "01_Premiere_NSI"
                / "04_TP"
                / "assets"
                / "style.css"
            )
            self.assertFalse(source.exists())
            self.assertTrue(destination.exists())
            self.assertEqual(counts["drive_moved"], 1)

    def test_drive_renamed_collision_still_counts_as_moved_integration(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            drive = root / "Documents_DRIVE"
            final = root / "ressources_nsi_centralisees"
            existing = final / "01_Premiere_NSI" / "01_Cours" / "Cours_variables.pdf"
            source = drive / "Algo_Premiere" / "Cours variables.pdf"
            existing.parent.mkdir(parents=True)
            source.parent.mkdir(parents=True)
            existing.write_bytes(b"contenu deja centralise")
            source.write_bytes(b"contenu drive different")

            counts = integrate_drive_dir(drive, final, {}, {})

            renamed = final / "01_Premiere_NSI" / "01_Cours" / "Cours_variables_Algo_Premiere.pdf"
            self.assertTrue(renamed.exists())
            self.assertEqual(counts["drive_moved"], 1)
            self.assertEqual(counts["drive_moved_renamed"], 1)

    def test_successive_transit_runs_preserve_previous_drive_imports(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            transit = root / "transit"
            final = root / "ressources_nsi_centralisees"
            drive_import = final / "01_Premiere_NSI" / "01_Cours" / "Cours_drive.pdf"
            first_source = transit / "run1" / "premiere" / "cours_1.pdf"
            second_source = transit / "run2" / "premiere" / "cours_2.pdf"

            drive_import.parent.mkdir(parents=True)
            first_source.parent.mkdir(parents=True)
            drive_import.write_bytes(b"drive import a conserver")
            first_source.write_bytes(b"transit initial")
            organize_transit(transit, final)

            second_source.parent.mkdir(parents=True, exist_ok=True)
            second_source.write_bytes(b"nouveau transit")
            organize_transit(transit, final)

            self.assertTrue(drive_import.exists())
            self.assertEqual(drive_import.read_bytes(), b"drive import a conserver")

    def test_reset_copy_zip_and_transit_error_branches(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            reset_target = root / "reset"
            reset_target.mkdir()
            (reset_target / "old.txt").write_text("old", encoding="utf-8")
            organizer_module.reset_dir(reset_target)
            self.assertTrue(reset_target.exists())
            self.assertEqual(list(reset_target.iterdir()), [])

            transit = root / "transit"
            source_root = root / "source"
            source = source_root / "site" / "cours.pdf"
            source.parent.mkdir(parents=True)
            source.write_bytes(b"cours")
            with redirect_stdout(io.StringIO()):
                copied = organizer_module.copy_sources_to_transit(
                    [root / "absent", source_root],
                    transit,
                )
            copied_again = organizer_module.copy_sources_to_transit([source_root], transit)
            self.assertEqual((copied, copied_again), (1, 1))
            self.assertTrue((transit / source_root.name / "site" / "cours_2.pdf").exists())

            invalid_zip = root / "invalid.zip"
            invalid_zip.write_bytes(b"not a zip")
            with redirect_stdout(io.StringIO()):
                self.assertEqual(organizer_module.extract_zip_to_transit(invalid_zip, root), 0)

            corrupt_zip = root / "corrupt.zip"
            with zipfile.ZipFile(corrupt_zip, "w") as zf:
                zf.writestr("bad.txt", "bad")
            with redirect_stdout(io.StringIO()), patch.object(
                organizer_module.zipfile.ZipFile,
                "testzip",
                return_value="bad.txt",
            ):
                self.assertEqual(organizer_module.extract_zip_to_transit(corrupt_zip, root), 0)

            zip_scan = root / "zip_scan"
            zip_scan.mkdir()
            zip_a = zip_scan / "zip_a.zip"
            zip_b = zip_scan / "zip_b.zip"
            with zipfile.ZipFile(zip_a, "w") as zf:
                zf.writestr("a.txt", "a")
            zip_b.write_bytes(b"not a zip")
            with redirect_stdout(io.StringIO()):
                extracted, failed = organizer_module.extract_all_zips(zip_scan)
            self.assertEqual((extracted, failed), (1, 1))
            self.assertTrue((zip_scan / "zip_b.zip.failed").exists())

            failed_only = root / "failed_only"
            failed_only.mkdir()
            invalid_only = failed_only / "invalid.zip"
            invalid_only.write_bytes(b"not zip")
            with redirect_stdout(io.StringIO()):
                self.assertEqual(organizer_module.extract_all_zips(failed_only), (0, 1))

    def test_seed_and_normalized_category_edge_cases(self):
        with TemporaryDirectory() as tmp:
            final = Path(tmp) / "final"
            root_file = final / "root.pdf"
            internal = final / "_skipped_drive" / "ignored.pdf"
            programme = final / "00_Programmes_et_Informations" / "bo.pdf"
            terminale_root = final / "02_Terminale_NSI" / "loose.pdf"
            for path in (root_file, internal, programme, terminale_root):
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(path.name.encode("utf-8"))

            self.assertIsNone(organizer_module.normalized_category_key(root_file, final))
            self.assertIsNone(
                organizer_module.normalized_category_key(Path(tmp) / "outside.pdf", final)
            )
            self.assertIsNone(organizer_module.normalized_category_key(internal, final))
            self.assertEqual(
                organizer_module.normalized_category_key(programme, final),
                "00_Programmes_et_Informations",
            )
            self.assertEqual(
                organizer_module.normalized_category_key(terminale_root, final),
                "02_Terminale_NSI",
            )
            unknown = final / "unknown" / "file.pdf"
            unknown.parent.mkdir(parents=True)
            unknown.write_bytes(b"unknown")
            self.assertEqual(organizer_module.normalized_category_key(unknown, final), "unknown")
            self.assertFalse(
                organizer_module.is_internal_final_path(Path(tmp) / "outside.pdf", final)
            )
            seen_hashes, category_counts = seed_existing_hashes(final)
            self.assertIn(compute_sha256(root_file), seen_hashes)
            self.assertNotIn("", category_counts)

    def test_organize_transit_merges_existing_hashes_when_partial_state_is_provided(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            final = root / "final"
            existing = final / "01_Premiere_NSI" / "01_Cours" / "ancien.pdf"
            transit = root / "transit"
            duplicate = transit / "site" / "premiere" / "copie.pdf"
            existing.parent.mkdir(parents=True)
            duplicate.parent.mkdir(parents=True)
            existing.write_bytes(b"same")
            duplicate.write_bytes(b"same")

            category_counts, status_counts, seen_hashes = organize_transit(
                transit,
                final,
                seen_hashes={},
                category_counts=None,
            )

            self.assertEqual(status_counts["duplicate"], 1)
            self.assertIn(compute_sha256(existing), seen_hashes)
            self.assertEqual(category_counts["01_Premiere_NSI/01_Cours"], 1)

            provided_counts = Counter()
            _, status_counts, _ = organize_transit(
                transit,
                final,
                seen_hashes=None,
                category_counts=provided_counts,
            )
            self.assertEqual(status_counts["duplicate"], 1)

    def test_organize_file_skip_branch_is_explicit(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            transit = root / "transit"
            final = root / "final"
            archive = transit / "site" / "pack.zip"
            archive.parent.mkdir(parents=True)
            archive.write_bytes(b"zip")

            result = organize_file(archive, transit, final, {}, {})

            self.assertEqual(result.status, "skipped")
            self.assertFalse(final.exists())

    def test_cleanup_final_files_and_report_cover_filtered_branches(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            transit = root / "transit"
            transit.mkdir()
            with patch.dict(organizer_module.os.environ, {"NSI_KEEP_TRANSIT": "oui"}):
                with redirect_stdout(io.StringIO()):
                    organizer_module.cleanup_transit(transit)
            self.assertTrue(transit.exists())

            final = root / "final"
            active = final / "01_Premiere_NSI" / "01_Cours" / "cours.pdf"
            internal = final / "_doublons_drive" / "cours.pdf"
            active.parent.mkdir(parents=True)
            internal.parent.mkdir(parents=True)
            active.write_bytes(b"active")
            internal.write_bytes(b"duplicate")
            self.assertEqual(organizer_module.final_resource_files(final), [active])

            with redirect_stdout(io.StringIO()) as output:
                organizer_module.print_report(Counter({"empty": 0}), Counter(), Counter(), final)
            self.assertIn("total_final_resource_files=1", output.getvalue())

    def test_seed_existing_hashes_ignores_drive_duplicate_quarantine(self):
        with TemporaryDirectory() as tmp:
            final = Path(tmp) / "ressources_nsi_centralisees"
            active = final / "01_Premiere_NSI" / "01_Cours" / "Cours_drive.pdf"
            quarantined = final / "_doublons_drive" / "Cours_drive.pdf"
            active.parent.mkdir(parents=True)
            quarantined.parent.mkdir(parents=True)
            active.write_bytes(b"actif")
            quarantined.write_bytes(b"doublon")

            seen_hashes, category_counts = seed_existing_hashes(final)

            self.assertIn(compute_sha256(active), seen_hashes)
            self.assertNotIn(compute_sha256(quarantined), seen_hashes)
            self.assertEqual(category_counts["01_Premiere_NSI/01_Cours"], 1)

    def test_seed_existing_hashes_normalizes_deep_asset_categories_to_two_levels(self):
        with TemporaryDirectory() as tmp:
            final = Path(tmp) / "ressources_nsi_centralisees"
            asset = (
                final
                / "01_Premiere_NSI"
                / "01_Cours"
                / "_assets_drive"
                / "Sous_Dossier"
                / "img.png"
            )
            asset.parent.mkdir(parents=True)
            asset.write_bytes(b"image")

            _, category_counts = seed_existing_hashes(final)

            self.assertEqual(category_counts["01_Premiere_NSI/01_Cours"], 1)
            self.assertNotIn("01_Premiere_NSI/01_Cours/_assets_drive/Sous_Dossier", category_counts)

    def test_drive_skipped_files_are_evacuated_to_allow_total_pruning(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            drive = root / "Documents_DRIVE"
            final = root / "ressources_nsi_centralisees"
            junk = drive / "Projet_Premiere" / "assets" / ".DS_Store"
            skipped = drive / "Projet_Premiere" / "assets" / ".payload.bin"
            junk.parent.mkdir(parents=True)
            junk.write_bytes(b"finder metadata")
            skipped.write_bytes(b"ignored binary")

            counts = integrate_drive_dir(drive, final, {}, {})

            quarantined = final / "_skipped_drive" / "Projet_Premiere" / "assets" / ".payload.bin"
            self.assertTrue(drive.exists())
            self.assertEqual([p for p in drive.rglob("*")], [])
            self.assertFalse(junk.exists())
            self.assertTrue(quarantined.exists())
            self.assertEqual(quarantined.read_bytes(), b"ignored binary")
            self.assertEqual(counts["drive_junk_deleted"], 1)
            self.assertEqual(counts["drive_skipped"], 1)

    def test_unique_nested_destination_renames_only_terminal_file_on_collision(self):
        with TemporaryDirectory() as tmp:
            base = Path(tmp) / "final" / "01_Premiere_NSI" / "04_TP"
            existing = base / "assets" / "style.css"
            existing.parent.mkdir(parents=True)
            existing.write_text("body { color: black; }\n", encoding="utf-8")

            destination, renamed = unique_nested_destination(
                base,
                Path("assets/style.css"),
                "TP_Premiere",
            )

            self.assertTrue(renamed)
            self.assertEqual(destination, base / "assets" / "style_TP_Premiere.css")

    def test_safe_filename_keeps_ascii_slug(self):
        self.assertEqual(safe_filename("Cours variables [Élève].pdf"), "Cours_variables_Eleve.pdf")

    def test_main_accepts_explicit_paths_for_isolated_pipeline(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            source_root = root / "ressources_nsi_extraites"
            drive_root = root / "Documents_DRIVE"
            transit_root = root / "transit"
            final_root = root / "ressources_nsi_centralisees"
            transit_source = source_root / "Site_Source" / "premiere" / "cours_source.pdf"
            drive_source = drive_root / "Algo_Premiere" / "Cours drive.pdf"
            transit_source.parent.mkdir(parents=True)
            drive_source.parent.mkdir(parents=True)
            transit_source.write_bytes(b"source transit")
            drive_source.write_bytes(b"source drive")

            with redirect_stdout(io.StringIO()):
                main(
                    source_dirs=[source_root],
                    drive_dir=drive_root,
                    transit_dir=transit_root,
                    final_dir=final_root,
                    keep_transit=False,
                )

            self.assertFalse(transit_root.exists())
            self.assertFalse(drive_source.exists())
            self.assertTrue(
                (final_root / "01_Premiere_NSI" / "01_Cours" / "cours_source.pdf").exists()
            )
            self.assertTrue(
                (final_root / "01_Premiere_NSI" / "01_Cours" / "Cours_drive.pdf").exists()
            )

    def test_main_resolves_default_paths_from_current_globals_at_call_time(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            source_root = root / "sources"
            drive_root = root / "drive"
            transit_root = root / "transit"
            final_root = root / "final"

            with patch.object(organizer_module, "SOURCE_DIRS", [source_root]), patch.object(
                organizer_module,
                "DRIVE_DIR",
                drive_root,
            ), patch.object(organizer_module, "TRANSIT_DIR", transit_root), patch.object(
                organizer_module,
                "FINAL_DIR",
                final_root,
            ), patch.object(organizer_module, "REGISTRY_FILE", root / "registry.json"), patch.object(
                organizer_module,
                "RUN_SUMMARY_FILE",
                root / "summary.log",
            ), patch.object(organizer_module, "reset_dir") as reset_dir, patch.object(
                organizer_module,
                "copy_sources_to_transit",
                return_value=0,
            ) as copy_sources, patch.object(
                organizer_module,
                "extract_all_zips",
                return_value=(0, 0),
            ) as extract_zips, patch.object(
                organizer_module,
                "initialize_state_from_final",
                return_value=({}, Counter()),
            ) as initialize_state, patch.object(
                organizer_module,
                "organize_transit",
                return_value=(Counter(), Counter(), {}),
            ) as organize_transit_mock, patch.object(
                organizer_module,
                "integrate_drive_dir",
                return_value=Counter(),
            ) as integrate_drive, patch.object(organizer_module, "print_report"), patch.object(
                organizer_module,
                "cleanup_transit",
            ) as cleanup:
                with redirect_stdout(io.StringIO()):
                    organizer_module.main(keep_transit=True)

            reset_dir.assert_called_once_with(transit_root)
            copy_sources.assert_called_once()
            self.assertEqual(copy_sources.call_args.args[:2], ([source_root], transit_root))
            self.assertEqual(copy_sources.call_args.kwargs["registry"], {})
            self.assertIsInstance(copy_sources.call_args.kwargs["copy_counts"], Counter)
            extract_zips.assert_called_once()
            self.assertEqual(extract_zips.call_args.args, (transit_root,))
            self.assertEqual(extract_zips.call_args.kwargs["registry"], {})
            initialize_state.assert_called_once_with(final_root, {})
            organize_transit_mock.assert_called_once()
            self.assertEqual(organize_transit_mock.call_args.args[:2], (transit_root, final_root))
            integrate_drive.assert_called_once()
            self.assertEqual(integrate_drive.call_args.args[:2], (drive_root, final_root))
            cleanup.assert_called_once_with(transit_root, True)

    def test_document_type_markers_are_global_configuration_constants(self):
        self.assertTrue(hasattr(organizer_module, "EVALUATION_MARKERS"))
        self.assertTrue(hasattr(organizer_module, "TP_MARKERS"))
        self.assertTrue(hasattr(organizer_module, "TD_MARKERS"))
        self.assertIn("sujet bac", organizer_module.EVALUATION_MARKERS)
        self.assertIn("pratique", organizer_module.TP_MARKERS)
        self.assertIn("exercices", organizer_module.TD_MARKERS)

    def test_registry_records_new_transit_integration(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            transit = root / "transit"
            final = root / "final"
            source = transit / "Site" / "premiere" / "cours.pdf"
            source.parent.mkdir(parents=True)
            source.write_bytes(b"contenu registre")
            registry = organizer_module.load_migration_registry(root / "registry.json")

            result = organize_file(source, transit, final, {}, {}, registry=registry)

            self.assertEqual(result.status, "copied")
            self.assertEqual(len(registry), 1)
            entry = registry[compute_sha256(source)]
            self.assertEqual(entry["hash_sha256"], compute_sha256(source))
            self.assertEqual(entry["chemin_source_original"], str(source))
            self.assertEqual(entry["chemin_destination_final"], str(result.destination))
            self.assertIn("timestamp_integration", entry)

    def test_registry_loader_ignores_malformed_payloads_and_entries(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            absent = root / "absent.json"
            self.assertEqual(organizer_module.load_migration_registry(absent), {})
            self.assertEqual(organizer_module.load_source_cache(absent), {})

            malformed = root / "malformed.json"
            malformed.write_text("{", encoding="utf-8")
            self.assertEqual(organizer_module.load_migration_registry(malformed), {})
            self.assertEqual(organizer_module.load_source_cache(malformed), {})

            non_dict = root / "non_dict.json"
            non_dict.write_text("[]", encoding="utf-8")
            self.assertEqual(organizer_module.load_migration_registry(non_dict), {})
            self.assertEqual(organizer_module.load_source_cache(non_dict), {})

            entries_not_dict = root / "entries_not_dict.json"
            entries_not_dict.write_text('{"entries": [], "source_cache": []}', encoding="utf-8")
            self.assertEqual(organizer_module.load_migration_registry(entries_not_dict), {})
            self.assertEqual(organizer_module.load_source_cache(entries_not_dict), {})

            mixed = root / "mixed.json"
            mixed.write_text(
                """
                {
                  "entries": {
                    "bad-type": [],
                    "bad-hash": {"hash_sha256": 12, "chemin_destination_final": "x"},
                    "bad-destination": {"hash_sha256": "h", "chemin_destination_final": 5},
                    "missing-destination": {"hash_sha256": "h2"},
                    "good": {
                      "hash_sha256": "abc",
                      "chemin_source_original": "source.pdf",
                      "chemin_destination_final": "final.pdf",
                      "timestamp_integration": "2026-01-01T00:00:00Z"
                    }
                  },
                  "source_cache": {
                    "bad-type": [],
                    "bad-fields": {"hash_sha256": "", "size": "1", "mtime_ns": "2"},
                    "good-source": {"hash_sha256": "abc", "size": "1", "mtime_ns": "2"}
                  }
                }
                """,
                encoding="utf-8",
            )

            loaded = organizer_module.load_migration_registry(mixed)
            source_cache = organizer_module.load_source_cache(mixed)

            self.assertEqual(list(loaded), ["abc"])
            self.assertEqual(loaded["abc"]["chemin_destination_final"], "final.pdf")
            self.assertEqual(list(source_cache), ["good-source"])
            self.assertEqual(source_cache["good-source"]["hash_sha256"], "abc")

    def test_registry_known_hash_with_existing_destination_is_ignored(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            transit = root / "transit"
            final = root / "final"
            destination = final / "01_Premiere_NSI" / "01_Cours" / "cours.pdf"
            source = transit / "Site" / "premiere" / "copie.pdf"
            destination.parent.mkdir(parents=True)
            source.parent.mkdir(parents=True)
            destination.write_bytes(b"deja integre")
            source.write_bytes(b"deja integre")
            sha256 = compute_sha256(destination)
            registry = {
                sha256: {
                    "hash_sha256": sha256,
                    "chemin_source_original": "ancienne/source.pdf",
                    "chemin_destination_final": str(destination),
                    "timestamp_integration": "2026-01-01T00:00:00Z",
                }
            }

            result = organize_file(source, transit, final, {}, {}, registry=registry)

            self.assertEqual(result.status, "registry_known")
            self.assertEqual(result.destination, destination)
            self.assertEqual(len(list(final.rglob("*.pdf"))), 1)

    def test_copy_sources_to_transit_skips_registry_known_sources(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            source_root = root / "source"
            transit = root / "transit"
            final = root / "final"
            source = source_root / "site" / "premiere" / "cours.pdf"
            destination = final / "01_Premiere_NSI" / "01_Cours" / "cours.pdf"
            source.parent.mkdir(parents=True)
            destination.parent.mkdir(parents=True)
            source.write_bytes(b"source deja connue")
            destination.write_bytes(b"source deja connue")
            sha256 = compute_sha256(source)
            registry = {
                sha256: {
                    "hash_sha256": sha256,
                    "chemin_source_original": str(source),
                    "chemin_destination_final": str(destination),
                    "timestamp_integration": "2026-01-01T00:00:00Z",
                }
            }
            copy_counts = Counter()

            copied = organizer_module.copy_sources_to_transit(
                [source_root],
                transit,
                registry=registry,
                copy_counts=copy_counts,
            )

            self.assertEqual(copied, 0)
            self.assertEqual(copy_counts["source_registry_known"], 1)
            self.assertFalse((transit / source_root.name / "site" / "premiere" / "cours.pdf").exists())

            copied_without_counter = organizer_module.copy_sources_to_transit(
                [source_root],
                root / "other_transit",
                registry=registry,
            )

            self.assertEqual(copied_without_counter, 0)

    def test_copy_sources_to_transit_handles_disappearing_and_skipped_sources(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            source_root = root / "source"
            transit = root / "transit"
            first = source_root / "site" / "premiere" / "cours.pdf"
            disappearing = source_root / "site" / "premiere" / "td.pdf"
            skipped = source_root / "site" / "premiere" / "cache.pyc"
            first.parent.mkdir(parents=True)
            first.write_bytes(b"cours")
            disappearing.write_bytes(b"td")
            skipped.write_bytes(b"cache")
            original_hash = organizer_module.compute_sha256

            def remove_second_then_hash(path: Path) -> str:
                if path == first and disappearing.exists():
                    disappearing.unlink()
                return original_hash(path)

            with patch.object(
                organizer_module,
                "compute_sha256",
                side_effect=remove_second_then_hash,
            ):
                copied = organizer_module.copy_sources_to_transit([source_root], transit)

            self.assertEqual(copied, 1)
            self.assertTrue((transit / source_root.name / "site" / "premiere" / "cours.pdf").exists())
            self.assertFalse((transit / source_root.name / "site" / "premiere" / "td.pdf").exists())

    def test_purge_source_file_keeps_zips_and_tolerates_missing_files(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            source_root = root / "source"
            archive = source_root / "site" / "pack.zip"
            missing = source_root / "site" / "missing.pdf"
            archive.parent.mkdir(parents=True)
            archive.write_bytes(b"archive")

            organizer_module.purge_source_file(archive, source_root, True)
            organizer_module.purge_source_file(missing, source_root, True)

            self.assertTrue(archive.exists())
            self.assertFalse(missing.exists())

    def test_extract_all_zips_records_archive_hash_for_future_skip(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            transit = root / "transit"
            source_root = root / "source"
            transit.mkdir()
            archive = transit / "pack.zip"
            with zipfile.ZipFile(archive, "w") as zf:
                zf.writestr("premiere/cours.pdf", "cours")
            archive_bytes = archive.read_bytes()
            archive_hash = compute_sha256(archive)
            registry = {}

            extracted, failed = organizer_module.extract_all_zips(transit, registry=registry)

            self.assertEqual((extracted, failed), (1, 0))
            self.assertIn(archive_hash, registry)
            self.assertEqual(
                registry[archive_hash]["chemin_destination_final"],
                organizer_module.ARCHIVE_PROCESSED_DESTINATION,
            )

            source_archive = source_root / "site" / "pack.zip"
            source_archive.parent.mkdir(parents=True)
            source_archive.write_bytes(archive_bytes)
            copy_counts = Counter()
            copied = organizer_module.copy_sources_to_transit(
                [source_root],
                root / "second_transit",
                registry=registry,
                copy_counts=copy_counts,
            )

            self.assertEqual(copied, 0)
            self.assertEqual(copy_counts["source_registry_known"], 1)

    def test_copy_sources_to_transit_uses_source_cache_without_rehashing(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            source_root = root / "source"
            transit = root / "transit"
            final = root / "final"
            source = source_root / "site" / "premiere" / "cours.pdf"
            destination = final / "01_Premiere_NSI" / "01_Cours" / "cours.pdf"
            source.parent.mkdir(parents=True)
            destination.parent.mkdir(parents=True)
            source.write_bytes(b"cache source")
            destination.write_bytes(b"cache source")
            sha256 = compute_sha256(source)
            stat = source.stat()
            registry = {
                sha256: {
                    "hash_sha256": sha256,
                    "chemin_source_original": str(source),
                    "chemin_destination_final": str(destination),
                    "timestamp_integration": "2026-01-01T00:00:00Z",
                }
            }
            source_cache = {
                str(source): {
                    "hash_sha256": sha256,
                    "size": str(stat.st_size),
                    "mtime_ns": str(stat.st_mtime_ns),
                }
            }
            copy_counts = Counter()

            with patch.object(
                organizer_module,
                "compute_sha256",
                side_effect=AssertionError("hash should not be recomputed"),
            ):
                copied = organizer_module.copy_sources_to_transit(
                    [source_root],
                    transit,
                    registry=registry,
                    copy_counts=copy_counts,
                    source_cache=source_cache,
                )

            self.assertEqual(copied, 0)
            self.assertEqual(copy_counts["source_registry_known"], 1)
            self.assertFalse(transit.exists())

            with patch.object(
                organizer_module,
                "compute_sha256",
                side_effect=AssertionError("hash should not be recomputed"),
            ):
                copied_without_counter = organizer_module.copy_sources_to_transit(
                    [source_root],
                    root / "other_transit",
                    registry=registry,
                    source_cache=source_cache,
                )
            self.assertEqual(copied_without_counter, 0)

            stale_size = {str(source): dict(source_cache[str(source)], size="999")}
            self.assertFalse(organizer_module.source_cache_hit(source, registry, stale_size))
            stale_mtime = {str(source): dict(source_cache[str(source)], mtime_ns="999")}
            self.assertFalse(organizer_module.source_cache_hit(source, registry, stale_mtime))

    def test_registry_can_be_seeded_from_existing_final_tree(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            final = root / "final"
            existing = final / "01_Premiere_NSI" / "01_Cours" / "cours.pdf"
            skipped = final / "01_Premiere_NSI" / "01_Cours" / "cache.pyc"
            existing.parent.mkdir(parents=True)
            existing.write_bytes(b"ancien fichier central")
            skipped.write_bytes(b"compiled cache")
            registry = {}

            organizer_module.seed_registry_from_final(registry, final)
            organizer_module.seed_registry_from_final(registry, final)

            sha256 = compute_sha256(existing)
            self.assertIn(sha256, registry)
            self.assertNotIn(compute_sha256(skipped), registry)
            self.assertEqual(registry[sha256]["chemin_source_original"], str(existing))
            self.assertEqual(registry[sha256]["chemin_destination_final"], str(existing))

    def test_seed_existing_from_registry_counts_categories_without_hashing(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            final = root / "final"
            active = final / "01_Premiere_NSI" / "01_Cours" / "cours.pdf"
            root_file = final / "loose.pdf"
            internal = final / "_doublons_drive" / "dup.pdf"
            active.parent.mkdir(parents=True)
            internal.parent.mkdir(parents=True)
            active.write_bytes(b"active")
            root_file.write_bytes(b"loose")
            internal.write_bytes(b"dup")
            registry = {
                "archive": {
                    "hash_sha256": "archive",
                    "chemin_source_original": "pack.zip",
                    "chemin_destination_final": organizer_module.ARCHIVE_PROCESSED_DESTINATION,
                    "timestamp_integration": "2026-01-01T00:00:00Z",
                },
                "missing": {
                    "hash_sha256": "missing",
                    "chemin_source_original": "missing.pdf",
                    "chemin_destination_final": str(final / "missing.pdf"),
                    "timestamp_integration": "2026-01-01T00:00:00Z",
                },
                "internal": {
                    "hash_sha256": "internal",
                    "chemin_source_original": str(internal),
                    "chemin_destination_final": str(internal),
                    "timestamp_integration": "2026-01-01T00:00:00Z",
                },
                "active": {
                    "hash_sha256": "active",
                    "chemin_source_original": str(active),
                    "chemin_destination_final": str(active),
                    "timestamp_integration": "2026-01-01T00:00:00Z",
                },
            }

            seen_hashes, category_counts = organizer_module.seed_existing_from_registry(
                final,
                registry,
            )

            self.assertEqual(seen_hashes["active"], active)
            self.assertEqual(seen_hashes[compute_sha256(root_file)], root_file)
            self.assertEqual(category_counts["01_Premiere_NSI/01_Cours"], 1)
            self.assertNotIn("", category_counts)

    def test_initialize_state_from_final_single_pass_counts_hashes_and_updates_registry(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            final = root / "final"
            registered = final / "01_Premiere_NSI" / "01_Cours" / "registered.pdf"
            missing_registry = final / "01_Premiere_NSI" / "03_TD" / "missing.pdf"
            internal = final / "_doublons_drive" / "ignored.pdf"
            skipped = final / "01_Premiere_NSI" / "01_Cours" / "cache.pyc"
            for path in (registered, missing_registry, internal, skipped):
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(path.name.encode("utf-8"))
            registered_hash = compute_sha256(registered)
            registry = {
                registered_hash: {
                    "hash_sha256": registered_hash,
                    "chemin_source_original": "old/source.pdf",
                    "chemin_destination_final": str(registered),
                    "timestamp_integration": "2026-01-01T00:00:00Z",
                }
            }
            hashed_paths: list[Path] = []
            original_hash = organizer_module.compute_sha256

            def counted_hash(path: Path) -> str:
                hashed_paths.append(path)
                return original_hash(path)

            with patch.object(organizer_module, "compute_sha256", side_effect=counted_hash):
                seen_hashes, category_counts = organizer_module.initialize_state_from_final(
                    final,
                    registry,
                )

            self.assertEqual(hashed_paths, [missing_registry])
            self.assertEqual(seen_hashes[registered_hash], registered)
            self.assertIn(original_hash(missing_registry), seen_hashes)
            self.assertIn(original_hash(missing_registry), registry)
            self.assertEqual(category_counts["01_Premiere_NSI/01_Cours"], 1)
            self.assertEqual(category_counts["01_Premiere_NSI/03_TD"], 1)
            self.assertNotIn(original_hash(internal), seen_hashes)
            self.assertNotIn(original_hash(skipped), seen_hashes)

    def test_registry_hash_for_destination_linear_helper_has_been_removed(self):
        self.assertFalse(hasattr(organizer_module, "registry_hash_for_destination"))

    def test_main_can_purge_source_directories_after_successful_integration(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            source_v1 = root / "ressources_nsi_extraites"
            source_v2 = root / "ressources_nsi_extraites_v2"
            drive_root = root / "Documents_DRIVE"
            transit_root = root / "transit"
            final_root = root / "ressources_nsi_centralisees"
            registry_path = root / "migration_registry.json"
            summary_path = root / "last_run_summary.log"

            v1_file = source_v1 / "Site_V1" / "premiere" / "cours_v1.pdf"
            v2_file = source_v2 / "Site_V2" / "terminale" / "tp_v2.py"
            drive_file = drive_root / "Algo_Premiere" / "Cours drive.pdf"
            for path, content in (
                (v1_file, b"cours depuis v1"),
                (v2_file, b"tp depuis v2"),
                (drive_file, b"cours depuis drive"),
            ):
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)

            with redirect_stdout(io.StringIO()):
                main(
                    source_dirs=[source_v1, source_v2],
                    drive_dir=drive_root,
                    transit_dir=transit_root,
                    final_dir=final_root,
                    registry_path=registry_path,
                    summary_path=summary_path,
                    keep_transit=False,
                    purge_source_files=True,
                )

            self.assertTrue((final_root / "01_Premiere_NSI" / "01_Cours" / "cours_v1.pdf").exists())
            self.assertTrue((final_root / "02_Terminale_NSI" / "04_TP" / "tp_v2.py").exists())
            self.assertTrue(
                (final_root / "01_Premiere_NSI" / "01_Cours" / "Cours_drive.pdf").exists()
            )
            for source_root in (source_v1, source_v2, drive_root):
                active_files = [
                    path
                    for path in source_root.rglob("*")
                    if path.is_file() and not should_skip(path)
                ]
                self.assertEqual(active_files, [])
            registry_payload = json.loads(registry_path.read_text(encoding="utf-8"))
            destinations = {
                entry["chemin_destination_final"]
                for entry in registry_payload["entries"].values()
                if entry["chemin_destination_final"]
                != organizer_module.ARCHIVE_PROCESSED_DESTINATION
            }
            self.assertIn(str(final_root / "01_Premiere_NSI" / "01_Cours" / "cours_v1.pdf"), destinations)
            self.assertIn(str(final_root / "02_Terminale_NSI" / "04_TP" / "tp_v2.py"), destinations)
            self.assertIn(
                str(final_root / "01_Premiere_NSI" / "01_Cours" / "Cours_drive.pdf"),
                destinations,
            )

    def test_drive_registry_known_hash_is_evacuated_without_new_integration(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            drive = root / "Documents_DRIVE"
            final = root / "ressources_nsi_centralisees"
            destination = final / "01_Premiere_NSI" / "01_Cours" / "cours.pdf"
            source = drive / "Premiere" / "cours_reimporte.pdf"
            destination.parent.mkdir(parents=True)
            source.parent.mkdir(parents=True)
            destination.write_bytes(b"deja integre drive")
            source.write_bytes(b"deja integre drive")
            sha256 = compute_sha256(destination)
            registry = {
                sha256: {
                    "hash_sha256": sha256,
                    "chemin_source_original": "ancienne/source.pdf",
                    "chemin_destination_final": str(destination),
                    "timestamp_integration": "2026-01-01T00:00:00Z",
                }
            }

            counts = integrate_drive_dir(drive, final, {}, {}, registry=registry)

            self.assertEqual(counts["drive_registry_known"], 1)
            self.assertEqual(counts["drive_moved"], 0)
            self.assertFalse(source.exists())
            self.assertTrue(
                (final / "_doublons_drive" / "Premiere" / "cours_reimporte.pdf").exists()
            )

    def test_main_writes_registry_and_second_run_summary_marks_known_files(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            source_root = root / "ressources_nsi_extraites"
            drive_root = root / "Documents_DRIVE"
            transit_root = root / "transit"
            final_root = root / "ressources_nsi_centralisees"
            registry_path = root / "migration_registry.json"
            summary_path = root / "last_run_summary.log"
            source = source_root / "Site_Source" / "premiere" / "cours_source.pdf"
            source.parent.mkdir(parents=True)
            drive_root.mkdir()
            source.write_bytes(b"source stable")

            with redirect_stdout(io.StringIO()):
                main(
                    source_dirs=[source_root],
                    drive_dir=drive_root,
                    transit_dir=transit_root,
                    final_dir=final_root,
                    registry_path=registry_path,
                    summary_path=summary_path,
                    keep_transit=False,
                )
                main(
                    source_dirs=[source_root],
                    drive_dir=drive_root,
                    transit_dir=transit_root,
                    final_dir=final_root,
                    registry_path=registry_path,
                    summary_path=summary_path,
                    keep_transit=False,
                )

            self.assertTrue(registry_path.exists())
            self.assertTrue(summary_path.exists())
            self.assertEqual(len(list(final_root.rglob("cours_source*.pdf"))), 1)
            summary = summary_path.read_text(encoding="utf-8")
            self.assertIn("known_ignored=1", summary)
            self.assertIn("new_integrated=0", summary)

    def test_main_uses_existing_registry_without_hashing_final_tree(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            source_root = root / "sources"
            drive_root = root / "drive"
            transit_root = root / "transit"
            final_root = root / "final"
            registry_path = root / "migration_registry.json"
            summary_path = root / "summary.log"
            final_file = final_root / "01_Premiere_NSI" / "01_Cours" / "cours.pdf"
            source = source_root / "site" / "premiere" / "cours.pdf"
            final_file.parent.mkdir(parents=True)
            source.parent.mkdir(parents=True)
            drive_root.mkdir()
            final_file.write_bytes(b"contenu stable")
            source.write_bytes(b"contenu stable")
            sha256 = compute_sha256(final_file)
            registry = {
                sha256: {
                    "hash_sha256": sha256,
                    "chemin_source_original": str(final_file),
                    "chemin_destination_final": str(final_file),
                    "timestamp_integration": "2026-01-01T00:00:00Z",
                }
            }
            stat = source.stat()
            source_cache = {
                str(source): {
                    "hash_sha256": sha256,
                    "size": str(stat.st_size),
                    "mtime_ns": str(stat.st_mtime_ns),
                }
            }
            organizer_module.save_migration_registry(registry_path, registry, source_cache)

            with patch.object(
                organizer_module,
                "seed_existing_hashes",
                side_effect=AssertionError("final tree should be seeded from registry"),
            ):
                with redirect_stdout(io.StringIO()):
                    main(
                        source_dirs=[source_root],
                        drive_dir=drive_root,
                        transit_dir=transit_root,
                        final_dir=final_root,
                        registry_path=registry_path,
                        summary_path=summary_path,
                        keep_transit=False,
                    )

            self.assertIn("source_registry_known=1", summary_path.read_text(encoding="utf-8"))

    def test_main_falls_back_to_final_scan_when_registry_has_no_live_destination(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            source_root = root / "sources"
            drive_root = root / "drive"
            transit_root = root / "transit"
            final_root = root / "final"
            registry_path = root / "migration_registry.json"
            summary_path = root / "summary.log"
            final_file = final_root / "01_Premiere_NSI" / "01_Cours" / "cours.pdf"
            final_file.parent.mkdir(parents=True)
            source_root.mkdir()
            drive_root.mkdir()
            final_file.write_bytes(b"contenu final")
            registry = {
                "archive": {
                    "hash_sha256": "archive",
                    "chemin_source_original": "pack.zip",
                    "chemin_destination_final": organizer_module.ARCHIVE_PROCESSED_DESTINATION,
                    "timestamp_integration": "2026-01-01T00:00:00Z",
                }
            }
            organizer_module.save_migration_registry(registry_path, registry, {})

            with redirect_stdout(io.StringIO()):
                main(
                    source_dirs=[source_root],
                    drive_dir=drive_root,
                    transit_dir=transit_root,
                    final_dir=final_root,
                    registry_path=registry_path,
                    summary_path=summary_path,
                    keep_transit=False,
                )

            loaded = organizer_module.load_migration_registry(registry_path)
            self.assertIn(compute_sha256(final_file), loaded)


if __name__ == "__main__":
    unittest.main()
