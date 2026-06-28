#!/usr/bin/env python3
"""Refuse toute promotion de statut sans verdict A vérifié et relecture humaine."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from check_substance_anchors import check_capacity, load_official_labels, validate_schema


ROOT = Path(__file__).resolve().parents[1]
CAPACITY_RE = re.compile(r"\b[PT]-[A-Z0-9-]+\b")
PROMOTED_STATUSES = {"validated_pedagogy", "published", "covered"}
STATUS_FILES = (
    "coverage.md",
    "INDEX.md",
    "manifest.csv",
    "substance_report*.md",
    "substance_review*.json",
)


@dataclass(frozen=True)
class PromotionClaim:
    capacity_id: str
    status: str
    source: Path
    detail: str


def _normalize_json_strings(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: _normalize_json_strings(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_normalize_json_strings(item) for item in value]
    if isinstance(value, str):
        return re.sub(r"\s+", " ", value).strip()
    return value


def canonical_verdict_hash(verdict: dict[str, Any]) -> str:
    normalized = _normalize_json_strings(verdict)
    payload = json.dumps(
        normalized,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _iter_status_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for pattern in STATUS_FILES:
        files.extend(path for path in root.glob(pattern) if path.is_file())
    return sorted(set(files))


def _claims_from_text(path: Path, text: str) -> list[PromotionClaim]:
    claims: list[PromotionClaim] = []
    current_capacity = ""
    for line in text.splitlines():
        ids = CAPACITY_RE.findall(line)
        if ids:
            current_capacity = ids[0]
        lowered = line.lower()
        for status in PROMOTED_STATUSES:
            if status == "covered":
                count_match = re.search(r"\bcovered\s*[:=]\s*(\d+)\b", lowered)
                if count_match and int(count_match.group(1)) <= 0:
                    continue
                if "covered" not in lowered:
                    continue
            elif status not in lowered:
                continue
            cid = ids[0] if ids else current_capacity or "__GLOBAL__"
            claims.append(PromotionClaim(cid, status, path, line.strip()))
    return claims


def _walk_json_for_claims(path: Path, value: Any, current_capacity: str = "") -> list[PromotionClaim]:
    claims: list[PromotionClaim] = []
    if isinstance(value, dict):
        capacity = str(value.get("capacity_id") or value.get("id") or current_capacity)
        for key, item in value.items():
            if key in {"verdict", "status", "statut", "decision"} and str(item) in PROMOTED_STATUSES:
                claims.append(PromotionClaim(capacity or "__GLOBAL__", str(item), path, key))
            elif key in {"covered", "published"} and item not in {0, "0", False, None, ""}:
                claims.append(PromotionClaim(capacity or "__GLOBAL__", key, path, f"{key}={item}"))
            else:
                claims.extend(_walk_json_for_claims(path, item, capacity))
    elif isinstance(value, list):
        for item in value:
            claims.extend(_walk_json_for_claims(path, item, current_capacity))
    return claims


def _claims_from_csv(path: Path) -> list[PromotionClaim]:
    claims: list[PromotionClaim] = []
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            capacity = (
                row.get("capacity_id")
                or row.get("capacite_id")
                or row.get("capacité")
                or row.get("id")
                or "__GLOBAL__"
            )
            for key, value in row.items():
                if value in PROMOTED_STATUSES:
                    claims.append(PromotionClaim(capacity, value, path, key or "csv"))
                if key and key.lower() in {"covered", "published"} and value not in {"", "0", "false", "False"}:
                    claims.append(PromotionClaim(capacity, key.lower(), path, f"{key}={value}"))
    return claims


def collect_promotion_claims(root: Path) -> list[PromotionClaim]:
    claims: list[PromotionClaim] = []
    for path in _iter_status_files(root):
        if path.suffix == ".csv":
            claims.extend(_claims_from_csv(path))
            continue
        if path.suffix == ".json":
            try:
                claims.extend(_walk_json_for_claims(path, json.loads(path.read_text(encoding="utf-8"))))
            except json.JSONDecodeError:
                claims.append(PromotionClaim("__GLOBAL__", "invalid_json", path, "JSON illisible"))
            continue
        claims.extend(_claims_from_text(path, path.read_text(encoding="utf-8")))
    return claims


def _valid_verdict_hashes(root: Path) -> dict[str, set[str]]:
    valid: dict[str, set[str]] = {}
    official = load_official_labels(root)
    schema = root / "substance_verdict.schema.json"
    section_cache: dict[Path, Any] = {}
    verdict_files = sorted(root.glob("substance_review*.json"))
    verdict_files += sorted((root / "substance_reviews").glob("**/*.json")) if (root / "substance_reviews").exists() else []
    for path in verdict_files:
        try:
            verdict = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        if not isinstance(verdict, dict) or "capacities" not in verdict:
            continue
        if any(message.startswith("schéma @") for message in validate_schema(verdict, schema)):
            continue
        verdict_hash = canonical_verdict_hash(verdict)
        for capacity in verdict.get("capacities", []):
            result = check_capacity(capacity, root, official, section_cache)
            if (
                result.capacity_id != "?"
                and result.declared_verdict == "validated_pedagogy"
                and result.effective_verdict == "validated_pedagogy"
                and not result.downgraded
            ):
                valid.setdefault(result.capacity_id, set()).add(verdict_hash)
    return valid


def _load_confirmations(root: Path) -> dict[str, set[str]]:
    confirmations: dict[str, set[str]] = {}
    for path in sorted((root / "reviewer_confirmations").glob("*.json")) if (root / "reviewer_confirmations").exists() else []:
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        if not isinstance(payload, dict):
            continue
        required = {"capacite_id", "verdict_hash", "relecteur", "date", "marqueur"}
        if not required <= payload.keys():
            continue
        confirmations.setdefault(str(payload["capacite_id"]), set()).add(str(payload["verdict_hash"]))
    return confirmations


def analyze_status_promotions(root: Path = ROOT) -> list[str]:
    claims = collect_promotion_claims(root)
    if not claims:
        return []
    valid_hashes = _valid_verdict_hashes(root)
    confirmations = _load_confirmations(root)
    errors: list[str] = []
    for claim in claims:
        if claim.status == "invalid_json":
            errors.append(f"{claim.source}: JSON illisible")
            continue
        cid = claim.capacity_id
        if cid == "__GLOBAL__":
            errors.append(f"{claim.source}: promotion globale {claim.status} sans capacité traçable")
            continue
        hashes = valid_hashes.get(cid, set())
        if not hashes:
            errors.append(f"{claim.source}: {cid} déclare {claim.status} sans verdict A valide")
            continue
        confirmed = confirmations.get(cid, set())
        if not hashes & confirmed:
            errors.append(f"{claim.source}: {cid} déclare {claim.status} sans confirmation relecteur concordante")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Garde anti-promotion doctrinale")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    errors = analyze_status_promotions(args.root.resolve())
    if errors:
        print("check_status_promotion_guard: KO")
        for error in errors:
            print(f"- {error}")
        return 1
    print("check_status_promotion_guard: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
