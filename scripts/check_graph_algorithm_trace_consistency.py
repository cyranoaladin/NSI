#!/usr/bin/env python3
"""Check basic graph algorithm traces for disciplinary contradictions."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re

from _qa_common import ROOT, strip_frontmatter


TARGETS = [
    ROOT / "03_progressions" / "supports" / "terminale" / "T07",
    ROOT / "03_progressions" / "supports" / "terminale" / "T08",
    ROOT / "03_progressions" / "fiches_cours" / "terminale" / "T07",
    ROOT / "03_progressions" / "fiches_cours" / "terminale" / "T08",
]


@dataclass
class GraphTraceResult:
    errors: list[str] = field(default_factory=list)
    files_checked: int = 0


def graph_block_errors(text: str) -> list[str]:
    errors: list[str] = []
    text = strip_frontmatter(text)
    checked_text = re.sub(r"BFS\s+confondu\s+avec\s+DFS", "", text, flags=re.I)
    checked_text = re.sub(r"^#.*DFS.*$", "", checked_text, flags=re.I | re.M)
    checked_text = re.sub(r"`[^`]*`", "", checked_text)
    lowered = checked_text.lower()
    if "bfs" in lowered and "file" not in lowered:
        errors.append("BFS mentionné sans file")
    if "dfs" in lowered and not re.search(r"pile|récurs|recurs|profondeur|avant retour", lowered):
        errors.append("DFS mentionné sans pile ni récursion")
    if re.search(r"graphe\s+non\s+orient", lowered):
        edges = set(re.findall(r"\b([A-Z])\s*-\s*([A-Z])\b", text))
        for a, b in edges:
            matrix_hint = f"{b},{a}"
            if "matrice" in lowered and matrix_hint in text and (b, a) not in edges:
                errors.append(f"graphe non orienté non symétrique pour {a}-{b}")
    if re.search(r"A\s*-\s*B", text) and re.search(r"B\s*-\s*C", text):
        if re.search(r"chemin\s+reconstruit\s+A\s*->\s*C(?!\s*->|\s*via)", text, re.I):
            errors.append("chemin A -> C reconstruit sans passer par B dans le graphe A-B, B-C")
    if re.search(r"cycle\s+(?:présent|existe|déclaré)", lowered):
        if not re.search(r"\b[A-Z]\s*-\s*[A-Z].*\b[A-Z]\s*-\s*[A-Z].*\b[A-Z]\s*-\s*[A-Z]", text, re.S):
            errors.append("cycle déclaré sans arêtes suffisantes pour le vérifier")
    return errors


def graph_block_is_consistent(text: str) -> bool:
    return not graph_block_errors(text)


def candidate_files(root: Path = ROOT) -> list[Path]:
    files: list[Path] = []
    for base in TARGETS:
        if base.exists():
            files.extend(sorted(base.glob("*.md")))
    return files


def analyze_graph_algorithm_trace_consistency(root: Path = ROOT) -> GraphTraceResult:
    result = GraphTraceResult()
    for path in candidate_files(root):
        result.files_checked += 1
        text = path.read_text(encoding="utf-8", errors="replace")
        for error in graph_block_errors(text):
            result.errors.append(f"{path.relative_to(root).as_posix()}: {error}")
    return result


def main() -> int:
    result = analyze_graph_algorithm_trace_consistency()
    if result.errors:
        print("check_graph_algorithm_trace_consistency: KO")
        for error in result.errors[:160]:
            print(f"- {error}")
        return 1
    print(f"check_graph_algorithm_trace_consistency: PASS ({result.files_checked} fichiers)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
