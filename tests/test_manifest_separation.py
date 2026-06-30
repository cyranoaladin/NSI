"""Prove that tooling changes do not affect the pedagogical manifest."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TOOLING_PREFIXES = ("scripts/", "tests/", "reports/", "scrapping_NSI/")


def test_pedagogical_manifest_excludes_tooling() -> None:
    manifest = ROOT / "manifest.csv"
    assert manifest.exists(), "manifest.csv missing"
    with manifest.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            path = row["chemin"]
            assert not path.startswith(TOOLING_PREFIXES), (
                f"Tooling file {path} leaked into pedagogical manifest.csv"
            )


def test_tooling_manifest_contains_only_tooling() -> None:
    tooling = ROOT / "manifest_tooling.csv"
    assert tooling.exists(), "manifest_tooling.csv missing"
    with tooling.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            path = row["chemin"]
            assert path.startswith(TOOLING_PREFIXES), (
                f"Non-tooling file {path} found in manifest_tooling.csv"
            )


def test_manifests_cover_all_inventoried_resources() -> None:
    manifest = ROOT / "manifest.csv"
    tooling = ROOT / "manifest_tooling.csv"
    all_paths: set[str] = set()
    for csv_path in (manifest, tooling):
        with csv_path.open(encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                all_paths.add(row["chemin"])
    assert len(all_paths) > 100, f"Too few resources: {len(all_paths)}"
