from __future__ import annotations

import csv
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from organizer_nsi import (
    DUPLICATE_DRIVE_DIR,
    SKIPPED_DRIVE_DIR,
    compute_sha256,
    is_internal_final_path,
    should_skip,
)
from scraper_nsi_v2 import OUT_OF_SCOPE_SCRAPE_TARGETS, clean_folder_name


ROOT = Path(__file__).resolve().parent
CSV_FILE = ROOT / "urls_a_scraper.csv"
V1_DIR = ROOT / "ressources_nsi_extraites"
V2_DIR = ROOT / "ressources_nsi_extraites_v2"
DRIVE_DIR = ROOT.parent / "Documents_DRIVE"
FINAL_DIR = ROOT / "ressources_nsi_centralisees"
REPORT_FILE = ROOT / "audit_reconciliation_report.md"

SOURCE_DIRS = (V2_DIR, V1_DIR, DRIVE_DIR)
INTERNAL_FINAL_DIR_NAMES = {str(DUPLICATE_DRIVE_DIR), str(SKIPPED_DRIVE_DIR)}
EXPECTED_LEVEL_DIRS = {
    "00_Programmes_et_Informations",
    "01_Premiere_NSI",
    "02_Terminale_NSI",
    "03_Autres_et_Transversal",
}
EXPECTED_TYPE_DIRS = {
    "01_Cours",
    "02_Fiches_et_Syntheses",
    "03_TD",
    "04_TP",
    "05_Programmation",
    "06_Projets",
    "07_Evaluations",
}
TECHNICAL_PARTS = {
    "__pycache__",
    ".git",
    ".venv",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "__macosx",
}
TECHNICAL_SUFFIXES = {".pyc", ".pyo", ".tmp", ".part", ".crdownload"}
ARCHIVE_SUFFIXES = {".zip"}


@dataclass(frozen=True)
class FileEntry:
    path: Path
    sha256: str
    source_root: Path


@dataclass(frozen=True)
class ScrapeFolderStatus:
    site_name: str
    url: str
    expected_folder: Path
    status: str
    valid_file_count: int
    reason: str = ""


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def has_technical_part(path: Path) -> bool:
    return bool({part.lower() for part in path.parts} & TECHNICAL_PARTS)


def is_valid_resource_file(path: Path, *, include_archives: bool = False) -> bool:
    if not path.is_file():
        return False
    if has_technical_part(path):
        return False
    if path.suffix.lower() in TECHNICAL_SUFFIXES:
        return False
    if should_skip(path):
        return False
    if not include_archives and path.suffix.lower() in ARCHIVE_SUFFIXES:
        return False
    return True


def valid_file_count(root: Path) -> int:
    if not root.exists():
        return 0
    return sum(1 for path in root.rglob("*") if is_valid_resource_file(path))


def read_scrape_rows() -> list[dict[str, str]]:
    if not CSV_FILE.exists():
        return []
    with CSV_FILE.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def audit_scraping() -> list[ScrapeFolderStatus]:
    statuses: list[ScrapeFolderStatus] = []
    for row in read_scrape_rows():
        site_name = row.get("Nom_Site", "").strip()
        url = row.get("URL", "").strip()
        structure = row.get("Type_Structure", "").strip().lower()
        expected_folder = V2_DIR / clean_folder_name(site_name)
        if not expected_folder.exists():
            if site_name in OUT_OF_SCOPE_SCRAPE_TARGETS:
                statuses.append(
                    ScrapeFolderStatus(
                        site_name,
                        url,
                        expected_folder,
                        "excluded_out_of_scope",
                        0,
                        OUT_OF_SCOPE_SCRAPE_TARGETS[site_name],
                    )
                )
                continue
            if "annuaire" in f"{site_name} {structure}".lower():
                discovered = sorted(V2_DIR.glob("Annuaire - *"))
                discovered_count = sum(valid_file_count(path) for path in discovered)
                if discovered_count:
                    statuses.append(
                        ScrapeFolderStatus(
                            site_name,
                            url,
                            expected_folder,
                            "expanded_annuaire",
                            discovered_count,
                        )
                    )
                    continue
            statuses.append(
                ScrapeFolderStatus(site_name, url, expected_folder, "missing_folder", 0)
            )
            continue
        count = valid_file_count(expected_folder)
        statuses.append(
            ScrapeFolderStatus(
                site_name,
                url,
                expected_folder,
                "empty_folder" if count == 0 else "ok",
                count,
            )
        )
    return statuses


def is_quarantined_zip(path: Path) -> bool:
    lower_parts = {part.lower() for part in path.parts}
    return "_skipped" in lower_parts or "_skipped_drive" in lower_parts


def find_active_zips(roots: Iterable[Path]) -> list[Path]:
    active: list[Path] = []
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*.zip"):
            if path.is_file() and not is_quarantined_zip(path):
                active.append(path)
    return sorted(active)


def build_file_entries(roots: Iterable[Path]) -> list[FileEntry]:
    entries: list[FileEntry] = []
    for root in roots:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*")):
            if not is_valid_resource_file(path):
                continue
            entries.append(FileEntry(path, compute_sha256(path), root))
    return entries


def build_final_entries() -> tuple[list[FileEntry], list[FileEntry]]:
    active: list[FileEntry] = []
    quarantine: list[FileEntry] = []
    if not FINAL_DIR.exists():
        return active, quarantine
    for path in sorted(FINAL_DIR.rglob("*")):
        if not is_valid_resource_file(path):
            continue
        entry = FileEntry(path, compute_sha256(path), FINAL_DIR)
        if is_internal_final_path(path, FINAL_DIR):
            quarantine.append(entry)
        else:
            active.append(entry)
    return active, quarantine


def index_by_hash(entries: Iterable[FileEntry]) -> dict[str, list[FileEntry]]:
    indexed: dict[str, list[FileEntry]] = defaultdict(list)
    for entry in entries:
        indexed[entry.sha256].append(entry)
    return dict(indexed)


def explain_source_entry(
    entry: FileEntry,
    source_hash_counts: Counter[str],
    final_active_hashes: set[str],
    final_quarantine_hashes: set[str],
) -> str:
    if entry.sha256 in final_active_hashes:
        if source_hash_counts[entry.sha256] > 1:
            return "migrated_or_duplicate_collapsed"
        return "migrated"
    if entry.sha256 in final_quarantine_hashes:
        return "quarantined_in_final"
    if source_hash_counts[entry.sha256] > 1:
        return "duplicate_source_without_final_match"
    return "orphan_unexplained"


def audit_migration() -> dict[str, object]:
    source_entries = build_file_entries(SOURCE_DIRS)
    final_active_entries, final_quarantine_entries = build_final_entries()
    source_hash_counts = Counter(entry.sha256 for entry in source_entries)
    final_active_hashes = {entry.sha256 for entry in final_active_entries}
    final_quarantine_hashes = {entry.sha256 for entry in final_quarantine_entries}

    explanations: dict[str, list[FileEntry]] = defaultdict(list)
    for entry in source_entries:
        reason = explain_source_entry(
            entry,
            source_hash_counts,
            final_active_hashes,
            final_quarantine_hashes,
        )
        explanations[reason].append(entry)

    return {
        "source_entries": source_entries,
        "final_active_entries": final_active_entries,
        "final_quarantine_entries": final_quarantine_entries,
        "explanations": dict(explanations),
        "source_unique_hashes": len(source_hash_counts),
        "final_active_hashes": len(final_active_hashes),
        "final_quarantine_hashes": len(final_quarantine_hashes),
    }


def validate_final_tree() -> list[str]:
    violations: list[str] = []
    if not FINAL_DIR.exists():
        return ["ressources_nsi_centralisees absent"]
    for path in sorted(FINAL_DIR.rglob("*")):
        if not path.is_file():
            continue
        try:
            relative = path.relative_to(FINAL_DIR)
        except ValueError:
            continue
        parts = relative.parts
        if len(parts) == 1:
            violations.append(f"file_at_root: {rel(path)}")
            continue
        first = parts[0]
        if first in INTERNAL_FINAL_DIR_NAMES:
            continue
        if first not in EXPECTED_LEVEL_DIRS:
            violations.append(f"unexpected_level: {rel(path)}")
            continue
        if first in {"01_Premiere_NSI", "02_Terminale_NSI"}:
            if len(parts) < 3:
                violations.append(f"file_directly_under_level: {rel(path)}")
                continue
            if parts[1] not in EXPECTED_TYPE_DIRS:
                violations.append(f"unexpected_type: {rel(path)}")
    return violations


def format_limited_paths(paths: Iterable[Path], *, limit: int = 80) -> list[str]:
    listed = [f"- `{rel(path)}`" for path in paths]
    if len(listed) <= limit:
        return listed
    omitted = len(listed) - limit
    return listed[:limit] + [f"- ... {omitted} chemin(s) supplémentaires omis dans l'affichage"]


def write_report(
    scrape_statuses: list[ScrapeFolderStatus],
    active_zips: list[Path],
    migration: dict[str, object],
    tree_violations: list[str],
) -> None:
    explanations = migration["explanations"]
    assert isinstance(explanations, dict)
    lines: list[str] = []
    lines.append("# Audit de réconciliation NSI\n")
    lines.append("## Scraping V2")
    lines.append(f"- lignes CSV: {len(scrape_statuses)}")
    lines.append(f"- dossiers OK: {sum(s.status == 'ok' for s in scrape_statuses)}")
    lines.append(
        f"- annuaires développés en dossiers externes: "
        f"{sum(s.status == 'expanded_annuaire' for s in scrape_statuses)}"
    )
    lines.append(
        f"- plateformes hors périmètre explicite: "
        f"{sum(s.status == 'excluded_out_of_scope' for s in scrape_statuses)}"
    )
    lines.append(f"- dossiers manquants: {sum(s.status == 'missing_folder' for s in scrape_statuses)}")
    lines.append(f"- dossiers vides: {sum(s.status == 'empty_folder' for s in scrape_statuses)}")
    for status in scrape_statuses:
        if status.status != "ok":
            reason = f" - {status.reason}" if status.reason else ""
            lines.append(
                f"- {status.status}: `{status.site_name}` -> "
                f"`{rel(status.expected_folder)}` ({status.valid_file_count} fichier(s)){reason}"
            )

    lines.append("\n## Archives ZIP actives")
    lines.append(f"- total: {len(active_zips)}")
    by_root = Counter(
        rel(next(root for root in SOURCE_DIRS if root == path or root in path.parents))
        for path in active_zips
    )
    for root, count in sorted(by_root.items()):
        lines.append(f"- {root}: {count}")
    final_zips = [
        path
        for path in FINAL_DIR.rglob("*.zip")
        if path.is_file() and not is_internal_final_path(path, FINAL_DIR)
    ]
    lines.append(f"- ZIP actifs dans la banque centrale: {len(final_zips)}")
    lines.extend(format_limited_paths(active_zips))

    source_entries = migration["source_entries"]
    final_active_entries = migration["final_active_entries"]
    final_quarantine_entries = migration["final_quarantine_entries"]
    assert isinstance(source_entries, list)
    assert isinstance(final_active_entries, list)
    assert isinstance(final_quarantine_entries, list)
    lines.append("\n## Migration par hash")
    lines.append(f"- fichiers sources valides analysés: {len(source_entries)}")
    lines.append(f"- hash sources uniques: {migration['source_unique_hashes']}")
    lines.append(f"- fichiers actifs en banque centrale: {len(final_active_entries)}")
    lines.append(f"- hash actifs en banque centrale: {migration['final_active_hashes']}")
    lines.append(f"- fichiers en quarantaine centrale: {len(final_quarantine_entries)}")
    lines.append(f"- hash en quarantaine centrale: {migration['final_quarantine_hashes']}")
    for reason in sorted(explanations):
        entries = explanations[reason]
        lines.append(f"- {reason}: {len(entries)}")

    orphans = explanations.get("orphan_unexplained", [])
    lines.append("\n## Orphelins non justifiés")
    lines.append(f"- total: {len(orphans)}")
    lines.extend(format_limited_paths((entry.path for entry in orphans), limit=120))

    lines.append("\n## Validation de l'arborescence centrale")
    lines.append(f"- violations: {len(tree_violations)}")
    lines.extend(f"- `{violation}`" for violation in tree_violations[:120])
    if len(tree_violations) > 120:
        lines.append(f"- ... {len(tree_violations) - 120} violation(s) supplémentaires")

    REPORT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def print_summary(
    scrape_statuses: list[ScrapeFolderStatus],
    active_zips: list[Path],
    migration: dict[str, object],
    tree_violations: list[str],
) -> None:
    explanations = migration["explanations"]
    assert isinstance(explanations, dict)
    print("AUDIT_RECONCILIATION_NSI")
    print(f"csv_rows={len(scrape_statuses)}")
    print(f"scrape_ok={sum(s.status == 'ok' for s in scrape_statuses)}")
    print(f"scrape_expanded_annuaire={sum(s.status == 'expanded_annuaire' for s in scrape_statuses)}")
    print(
        "scrape_excluded_out_of_scope="
        f"{sum(s.status == 'excluded_out_of_scope' for s in scrape_statuses)}"
    )
    print(f"scrape_missing={sum(s.status == 'missing_folder' for s in scrape_statuses)}")
    print(f"scrape_empty={sum(s.status == 'empty_folder' for s in scrape_statuses)}")
    print(f"active_zip_count={len(active_zips)}")
    final_zip_count = sum(
        1
        for path in FINAL_DIR.rglob("*.zip")
        if path.is_file() and not is_internal_final_path(path, FINAL_DIR)
    )
    print(f"final_active_zip_count={final_zip_count}")
    print(f"source_valid_files={len(migration['source_entries'])}")
    print(f"source_unique_hashes={migration['source_unique_hashes']}")
    print(f"final_active_files={len(migration['final_active_entries'])}")
    print(f"final_active_hashes={migration['final_active_hashes']}")
    print(f"final_quarantine_files={len(migration['final_quarantine_entries'])}")
    for reason in sorted(explanations):
        print(f"{reason}={len(explanations[reason])}")
    print(f"tree_violations={len(tree_violations)}")
    print(f"report={rel(REPORT_FILE)}")


def main() -> None:
    scrape_statuses = audit_scraping()
    active_zips = find_active_zips(SOURCE_DIRS)
    migration = audit_migration()
    tree_violations = validate_final_tree()
    write_report(scrape_statuses, active_zips, migration, tree_violations)
    print_summary(scrape_statuses, active_zips, migration, tree_violations)


if __name__ == "__main__":
    main()
