#!/usr/bin/env python3
"""Check that session statuses follow the resources that now exist."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re

from _qa_common import ROOT
from check_session_referenced_files_exist import (
    describe_session,
    session_blocks,
)


SESSION_FILES = [
    ROOT / "03_progressions" / "seances_premiere.md",
    ROOT / "03_progressions" / "seances_terminale.md",
]


@dataclass
class SessionResourceAlignmentResult:
    operational_count: int = 0
    theoretical_count: int = 0
    theoretical_with_existing_supports: int = 0
    corrected_candidates: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


def sequence_supports_exist(root: Path, prefix: str) -> bool:
    level = "premiere" if prefix.startswith("P") else "terminale"
    base = root / "03_progressions" / "supports" / level / prefix
    if not base.exists():
        return False
    required = ["cours", "trace", "td", "tp", "corrige", "bareme", "evaluation", "remediation", "version_amenagee"]
    names = [path.name.lower() for path in base.glob(f"{prefix}_*.md")]
    return all(any(token in name for name in names) for token in required)


def analyze_session_to_resource_alignment(root: Path = ROOT) -> SessionResourceAlignmentResult:
    result = SessionResourceAlignmentResult()
    files = [
        root / "03_progressions" / "seances_premiere.md",
        root / "03_progressions" / "seances_terminale.md",
    ]
    for path in files:
        if not path.exists():
            continue
        for session_id, block in session_blocks(path):
            info = describe_session(root, session_id, block)
            prefix = session_id.split("-", 1)[0]
            if info.existing_specific_refs and not info.theoretical:
                result.operational_count += 1
                continue
            result.theoretical_count += 1
            if info.theoretical and info.existing_specific_refs:
                result.theoretical_with_existing_supports += 1
                result.errors.append(
                    f"{path.relative_to(root).as_posix()}: {session_id} marqué théorique alors que les supports cités existent"
                )
            elif info.theoretical and sequence_supports_exist(root, prefix):
                result.corrected_candidates.append(
                    f"{path.relative_to(root).as_posix()}: {session_id} -> supports {prefix} produits, séance à relier"
                )
    return result


def main() -> int:
    result = analyze_session_to_resource_alignment()
    print(f"Séances opérationnelles : {result.operational_count}")
    print(f"Séances théoriques ou non reliées : {result.theoretical_count}")
    print(f"Séances théoriques avec supports cités existants : {result.theoretical_with_existing_supports}")
    if result.corrected_candidates:
        print("Séances théoriques avec paquet de ressources produit :")
        for item in result.corrected_candidates[:220]:
            print(f"- {item}")
    if result.errors:
        print("check_session_to_resource_alignment: KO")
        for error in result.errors:
            print(f"- {error}")
        return 1
    print("check_session_to_resource_alignment: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
