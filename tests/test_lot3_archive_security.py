from __future__ import annotations

import io
import sys
import tarfile
import zipfile
import importlib
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRAPER_DIR = ROOT / "scrapping_NSI"
SCRIPTS_DIR = ROOT / "scripts"
for import_path in (SCRAPER_DIR, SCRIPTS_DIR):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from scraper_eduscol import extract_and_sort_zip  # noqa: E402


def test_safe_archive_module_is_canonical() -> None:
    module = importlib.import_module("scrapping_NSI.safe_archive")
    compatibility = importlib.import_module("scripts.archive_security")

    assert compatibility.safe_extract_zip is module.safe_extract_zip
    assert compatibility.safe_extract_tar is module.safe_extract_tar


def write_zip(path: Path, files: dict[str, bytes]) -> None:
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, content in files.items():
            archive.writestr(name, content)


def write_tar(path: Path, files: dict[str, bytes]) -> None:
    with tarfile.open(path, "w:gz") as archive:
        for name, content in files.items():
            info = tarfile.TarInfo(name)
            info.size = len(content)
            archive.addfile(info, io.BytesIO(content))


def test_zip_slip_vulnerability(tmp_path: Path) -> None:
    from scrapping_NSI.safe_archive import safe_extract_zip

    archive = tmp_path / "malicious.zip"
    write_zip(archive, {"../../malicious_file.txt": b"owned"})

    with pytest.raises(ValueError, match="Tentative de Zip-Slip détectée"):
        safe_extract_zip(archive, tmp_path / "dest")

    assert not (tmp_path / "malicious_file.txt").exists()
    assert not (tmp_path / "dest").exists()
    assert not (tmp_path / "dest.part").exists()


def test_zip_bomb_volume_limit(tmp_path: Path) -> None:
    from scrapping_NSI.safe_archive import safe_extract_zip

    archive = tmp_path / "bomb.zip"
    write_zip(archive, {"payload.bin": b"x"})
    original_infolist = zipfile.ZipFile.infolist

    def oversized_metadata(self: zipfile.ZipFile) -> list[zipfile.ZipInfo]:
        infos = original_infolist(self)
        infos[0].file_size = 600 * 1024 * 1024
        return infos

    with patch.object(zipfile.ZipFile, "infolist", oversized_metadata):
        with pytest.raises(ValueError, match="zip-bomb"):
            safe_extract_zip(archive, tmp_path / "dest")

    assert not (tmp_path / "dest").exists()
    assert not (tmp_path / "dest.part").exists()


def test_extraction_atomicity_on_failure(tmp_path: Path) -> None:
    from scrapping_NSI.safe_archive import safe_extract_zip

    archive = tmp_path / "partial.zip"
    write_zip(
        archive,
        {
            "safe_1.txt": b"ok",
            "safe_2.txt": b"ok",
            "../../malicious_file.txt": b"owned",
        },
    )

    with pytest.raises(ValueError, match="Tentative de Zip-Slip détectée"):
        safe_extract_zip(archive, tmp_path / "dest")

    assert not (tmp_path / "malicious_file.txt").exists()
    assert not (tmp_path / "dest").exists()
    assert not (tmp_path / "dest.part").exists()


def test_zip_bomb_ratio_uses_uncompressed_size_threshold(tmp_path: Path) -> None:
    from scrapping_NSI.safe_archive import safe_extract_zip

    archive = tmp_path / "ratio.zip"
    write_zip(archive, {"payload.bin": b"x"})
    original_infolist = zipfile.ZipFile.infolist

    def suspicious_ratio(self: zipfile.ZipFile) -> list[zipfile.ZipInfo]:
        infos = original_infolist(self)
        infos[0].compress_size = 8 * 1024
        infos[0].file_size = 2 * 1024 * 1024
        return infos

    with patch.object(zipfile.ZipFile, "infolist", suspicious_ratio):
        with pytest.raises(ValueError, match="ratio"):
            safe_extract_zip(archive, tmp_path / "dest")

    assert not (tmp_path / "dest").exists()
    assert not (tmp_path / "dest.part").exists()


def test_eduscol_zip_slip_is_rejected_and_writes_nothing_outside(tmp_path: Path) -> None:
    base = tmp_path / "output"
    base.mkdir()
    archive = tmp_path / "malicious.zip"
    write_zip(archive, {"../../malicious.txt": b"owned"})

    with pytest.raises(Exception, match="hors du repertoire cible|zip-slip|outside"):
        with redirect_stdout(io.StringIO()):
            extract_and_sort_zip(str(archive), str(base))

    assert not (tmp_path / "malicious.txt").exists()
    assert not (base / "_temp_zip_extraction").exists()
    assert not (base / "_temp_zip_extraction.part").exists()


def test_eduscol_zip_bomb_metadata_is_rejected_before_extraction(tmp_path: Path) -> None:
    base = tmp_path / "output"
    base.mkdir()
    archive = tmp_path / "bomb.zip"
    write_zip(archive, {"huge.txt": b"small"})

    original_infolist = zipfile.ZipFile.infolist

    def huge_metadata(self: zipfile.ZipFile) -> list[zipfile.ZipInfo]:
        infos = original_infolist(self)
        infos[0].file_size = 5 * 1024 * 1024 * 1024
        return infos

    with patch.object(zipfile.ZipFile, "infolist", huge_metadata):
        with pytest.raises(Exception, match="taille decompression|zip-bomb|uncompressed"):
            with redirect_stdout(io.StringIO()):
                extract_and_sort_zip(str(archive), str(base))

    assert not (base / "Archives_Extraites_Triees").exists()
    assert not (base / "_temp_zip_extraction").exists()
    assert not (base / "_temp_zip_extraction.part").exists()


def test_eduscol_archive_failure_is_atomic(tmp_path: Path) -> None:
    base = tmp_path / "output"
    base.mkdir()
    archive = tmp_path / "partial.zip"
    write_zip(archive, {"safe.py": b"print('ok')\n", "../../malicious.txt": b"owned"})

    with pytest.raises(Exception, match="hors du repertoire cible|zip-slip|outside"):
        with redirect_stdout(io.StringIO()):
            extract_and_sort_zip(str(archive), str(base))

    assert not (tmp_path / "malicious.txt").exists()
    assert not (base / "Archives_Extraites_Triees").exists()
    assert not (base / "_temp_zip_extraction").exists()
    assert not (base / "_temp_zip_extraction.part").exists()


def test_safe_tar_extraction_rejects_tar_slip(tmp_path: Path) -> None:
    from scripts.archive_security import safe_extract_tar

    archive = tmp_path / "payload.tar.gz"
    write_tar(archive, {"../../escaped.txt": b"owned"})

    with pytest.raises(Exception, match="hors du repertoire cible|zip-slip|outside"):
        safe_extract_tar(archive, tmp_path / "dest")

    assert not (tmp_path / "escaped.txt").exists()
    assert not (tmp_path / "dest").exists()
    assert not (tmp_path / "dest.part").exists()


def test_safe_zip_extraction_rejects_suspicious_compression_ratio(tmp_path: Path) -> None:
    from scripts.archive_security import safe_extract_zip

    archive = tmp_path / "ratio.zip"
    write_zip(archive, {"payload.txt": b"x"})
    original_infolist = zipfile.ZipFile.infolist

    def suspicious_ratio(self: zipfile.ZipFile) -> list[zipfile.ZipInfo]:
        infos = original_infolist(self)
        infos[0].compress_size = 1_048_577
        infos[0].file_size = 200 * 1024 * 1024
        return infos

    with patch.object(zipfile.ZipFile, "infolist", suspicious_ratio):
        with pytest.raises(Exception, match="ratio"):
            safe_extract_zip(archive, tmp_path / "dest")

    assert not (tmp_path / "dest").exists()
    assert not (tmp_path / "dest.part").exists()


def test_safe_zip_extraction_accepts_large_metadata_with_normal_ratio(tmp_path: Path) -> None:
    from scripts.archive_security import ArchiveSecurityLimits, _validate_compression_ratio

    _validate_compression_ratio(
        2 * 1024 * 1024,
        2 * 1024 * 1024,
        ArchiveSecurityLimits(),
    )


def test_safe_tar_extraction_accepts_clean_archive(tmp_path: Path) -> None:
    from scripts.archive_security import safe_extract_tar

    archive = tmp_path / "clean.tar.gz"
    with tarfile.open(archive, "w:gz") as tar:
        directory = tarfile.TarInfo("nsi-enseignement")
        directory.type = tarfile.DIRTYPE
        tar.addfile(directory)
        info = tarfile.TarInfo("nsi-enseignement/README.md")
        payload = b"ok"
        info.size = len(payload)
        tar.addfile(info, io.BytesIO(payload))

    destination = tmp_path / "dest"
    destination.mkdir()
    safe_extract_tar(archive, destination)

    assert (tmp_path / "dest" / "nsi-enseignement" / "README.md").read_bytes() == b"ok"


def test_safe_zip_extraction_accepts_directory_and_removes_stale_part(
    tmp_path: Path,
) -> None:
    from scripts.archive_security import safe_extract_zip

    archive = tmp_path / "clean.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zip_handle:
        zip_handle.writestr("folder/", b"")
        zip_handle.writestr("folder/a.txt", b"ok")
    stale_part = tmp_path / "dest.part"
    stale_part.mkdir()
    (stale_part / "stale.txt").write_text("stale", encoding="utf-8")

    safe_extract_zip(archive, tmp_path / "dest")

    assert (tmp_path / "dest" / "folder" / "a.txt").read_bytes() == b"ok"
    assert not stale_part.exists()


def test_safe_zip_rejects_absolute_member_and_file_count_limit(tmp_path: Path) -> None:
    from scripts.archive_security import ArchiveSecurityLimits, safe_extract_zip

    absolute_archive = tmp_path / "absolute.zip"
    write_zip(absolute_archive, {"/absolute.txt": b"owned"})
    with pytest.raises(ValueError, match="Tentative de Zip-Slip détectée.*absolu"):
        safe_extract_zip(absolute_archive, tmp_path / "absolute-dest")

    counted_archive = tmp_path / "counted.zip"
    write_zip(counted_archive, {"one.txt": b"one"})
    with pytest.raises(Exception, match="nombre de fichiers"):
        safe_extract_zip(
            counted_archive,
            tmp_path / "counted-dest",
            limits=ArchiveSecurityLimits(max_files=0),
        )


def test_safe_tar_rejects_unsupported_members_in_preflight_and_stream(
    tmp_path: Path,
) -> None:
    import scrapping_NSI.safe_archive as safe_archive
    from scrapping_NSI.safe_archive import safe_extract_tar

    archive = tmp_path / "link.tar.gz"
    with tarfile.open(archive, "w:gz") as tar:
        link = tarfile.TarInfo("link")
        link.type = tarfile.SYMTYPE
        link.linkname = "target"
        tar.addfile(link)

    with pytest.raises(Exception, match="type de membre tar refuse"):
        safe_extract_tar(archive, tmp_path / "preflight-dest")

    with patch.object(safe_archive, "_preflight_tar_members", return_value=None):
        with pytest.raises(Exception, match="type de membre tar refuse"):
            safe_extract_tar(archive, tmp_path / "stream-dest")

    assert not (tmp_path / "preflight-dest").exists()
    assert not (tmp_path / "stream-dest").exists()
    assert not (tmp_path / "stream-dest.part").exists()


def test_safe_tar_rejects_unreadable_regular_member(tmp_path: Path) -> None:
    from scripts.archive_security import safe_extract_tar

    archive = tmp_path / "unreadable.tar.gz"
    write_tar(archive, {"file.txt": b"ok"})

    with patch.object(tarfile.TarFile, "extractfile", return_value=None):
        with pytest.raises(Exception, match="illisible"):
            safe_extract_tar(archive, tmp_path / "dest")

    assert not (tmp_path / "dest").exists()
    assert not (tmp_path / "dest.part").exists()


def test_invalid_archives_propagate_and_cleanup(tmp_path: Path) -> None:
    from scripts.archive_security import safe_extract_tar, safe_extract_zip

    invalid_zip = tmp_path / "invalid.zip"
    invalid_zip.write_text("not a zip", encoding="utf-8")
    with pytest.raises(zipfile.BadZipFile):
        safe_extract_zip(invalid_zip, tmp_path / "zip-dest")

    invalid_tar = tmp_path / "invalid.tar.gz"
    invalid_tar.write_text("not a tar", encoding="utf-8")
    with pytest.raises(tarfile.TarError):
        safe_extract_tar(invalid_tar, tmp_path / "tar-dest")

    assert not (tmp_path / "zip-dest.part").exists()
    assert not (tmp_path / "tar-dest.part").exists()


def test_copy_stream_enforces_runtime_limit(tmp_path: Path) -> None:
    from scripts.archive_security import _copy_stream_with_limit

    with pytest.raises(Exception, match="flux decompresse"):
        _copy_stream_with_limit(io.BytesIO(b"abc"), tmp_path / "out.txt", 2)
