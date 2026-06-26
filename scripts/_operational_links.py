#!/usr/bin/env python3
"""Discover resources linked from operational course sheets."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import unicodedata
import re

from _qa_common import ROOT, read_frontmatter
from _course_sheets_common import CourseSheetLink, course_sheet_links, sheet_files


@dataclass(frozen=True)
class OperationalLinkedResource:
    sheet: Path
    link: CourseSheetLink
    path: Path | None


def normalize_label(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value.lower())
    normalized = "".join(char for char in normalized if not unicodedata.combining(char))
    return re.sub(r"\s+", " ", normalized).strip()


def resolve_reference(root: Path, reference: str) -> Path | None:
    candidate = root / reference
    if candidate.exists():
        return candidate
    if "/" in reference:
        return None
    matches = sorted(root.rglob(reference))
    return matches[0] if matches else None


def operational_sheets(root: Path = ROOT) -> list[Path]:
    return [
        path
        for path in sheet_files(root)
        if str(read_frontmatter(path).get("readiness") or "").strip() == "operational"
    ]


def operational_resource_links(
    root: Path = ROOT,
    element_prefixes: set[str] | None = None,
    existing_only: bool = False,
) -> list[OperationalLinkedResource]:
    prefixes = {normalize_label(prefix) for prefix in element_prefixes} if element_prefixes else None
    resources: list[OperationalLinkedResource] = []
    for sheet in operational_sheets(root):
        for link in course_sheet_links(sheet):
            if link.is_session or not link.is_resource:
                continue
            element = normalize_label(link.element)
            if prefixes and not any(element.startswith(prefix) for prefix in prefixes):
                continue
            path = resolve_reference(root, link.file)
            if existing_only and path is None:
                continue
            resources.append(OperationalLinkedResource(sheet=sheet, link=link, path=path))
    return sorted(resources, key=lambda item: (item.sheet.as_posix(), item.link.file))
