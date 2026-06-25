#!/usr/bin/env python3
"""Detect private data in publishable resources, manifests and reports."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Iterable, List
import re

import yaml

from _qa_common import ROOT, print_result

ALLOWLIST = ROOT / "privacy_allowlist.yml"
TEXT_SUFFIXES = {".md", ".tex", ".py", ".json", ".yml", ".yaml", ".txt", ".csv"}

EMAIL_RE = re.compile(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}")
FR_PHONE_RE = re.compile(r"(?:(?:\+|00)33|0)\s*[1-9](?:[\s().-]?\d){8}\b")
TN_PHONE_RE = re.compile(r"(?:(?:\+|00)216\s*)?(?:[24579]\d)(?:[\s().-]?\d){6}\b")
COORD_RE = re.compile(
    r"\b(?:adresse|domicile|rue|avenue|boulevard|code postal|gouvernorat|ville)\b",
    re.IGNORECASE,
)


def load_allowlist() -> Dict[str, List[str]]:
    if not ALLOWLIST.exists():
        return {}
    data = yaml.safe_load(ALLOWLIST.read_text(encoding="utf-8")) or {}
    return {key: value or [] for key, value in data.items() if isinstance(value, list)}


def allowed(value: str, allowlist: Dict[str, List[str]]) -> bool:
    candidates = []
    candidates.extend(allowlist.get("allowed_emails", []))
    candidates.extend(allowlist.get("allowed_phone_patterns", []))
    candidates.extend(allowlist.get("allowed_name_patterns", []))
    candidates.extend(allowlist.get("institutional_patterns", []))
    for pattern in candidates:
        if pattern and re.search(pattern, value, flags=re.IGNORECASE):
            return True
    return False


def student_names(allowlist: Dict[str, List[str]]) -> List[str]:
    names: List[str] = []
    for raw in allowlist.get("student_names_files", []):
        path = (ROOT / raw).resolve()
        if not path.exists() or ROOT not in path.parents:
            continue
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                names.append(line)
    return names


def iter_text_files() -> Iterable[Path]:
    for path in sorted(ROOT.rglob("*")):
        if path.is_dir():
            continue
        if ".git" in path.parts or ".venv" in path.parts or "__pycache__" in path.parts:
            continue
        if path.suffix in TEXT_SUFFIXES or path.name in {"manifest.csv"}:
            yield path


def main() -> None:
    allowlist = load_allowlist()
    names = student_names(allowlist)
    errors: List[str] = []

    for path in iter_text_files():
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8", errors="replace")

        for match in EMAIL_RE.finditer(text):
            value = match.group(0)
            if not allowed(value, allowlist):
                errors.append(f"{rel}: email personnel possible -> {value}")

        for label, regex in {"telephone_fr": FR_PHONE_RE, "telephone_tn": TN_PHONE_RE}.items():
            for match in regex.finditer(text):
                value = match.group(0)
                if not allowed(value, allowlist):
                    errors.append(f"{rel}: {label} possible -> {value}")

        if COORD_RE.search(text) and "private_data: false" not in text:
            if not allowed(str(rel), allowlist):
                errors.append(f"{rel}: coordonnée personnelle possible, vérifier le contexte")

        for name in names:
            pattern = r"\b" + re.escape(name) + r"\b"
            if re.search(pattern, text, flags=re.IGNORECASE) and not allowed(name, allowlist):
                errors.append(f"{rel}: nom d'élève possible -> {name}")

    print_result("check_no_private_data", errors)


if __name__ == "__main__":
    main()
