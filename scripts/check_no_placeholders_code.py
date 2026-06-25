#!/usr/bin/env python3
"""Reject unfinished code constructs without blanket exclusion of Python files."""

from __future__ import annotations

from pathlib import Path
from typing import List
import ast
import io
import tokenize

from _qa_common import ROOT, print_result

COMMENT_MARKERS = ("TO" + "DO", "FIX" + "ME", "X" + "XX", "TBD")


def check_file(path: Path) -> List[str]:
    rel = path.relative_to(ROOT)
    text = path.read_text(encoding="utf-8", errors="replace")
    errors: List[str] = []

    try:
        tree = ast.parse(text, filename=str(path))
    except SyntaxError as exc:
        return [f"{rel}: syntaxe Python invalide ({exc})"]

    for node in ast.walk(tree):
        if isinstance(node, ast.Pass):
            errors.append(f"{rel}:{node.lineno}: instruction pass interdite")
        if isinstance(node, ast.Raise):
            exc = node.exc
            if isinstance(exc, ast.Call):
                name = getattr(exc.func, "id", "")
            else:
                name = getattr(exc, "id", "")
            if name == "NotImplementedError":
                errors.append(f"{rel}:{node.lineno}: NotImplementedError interdit")
        if isinstance(node, ast.Constant) and node.value is Ellipsis:
            errors.append(f"{rel}:{node.lineno}: ellipsis interdit")

    reader = io.StringIO(text).readline
    for token in tokenize.generate_tokens(reader):
        if token.type == tokenize.COMMENT:
            upper = token.string.upper()
            for marker in COMMENT_MARKERS:
                if marker in upper:
                    errors.append(f"{rel}:{token.start[0]}: marqueur de placeholder dans un commentaire")

    return errors


def main() -> None:
    errors: List[str] = []
    for path in sorted(ROOT.rglob("*.py")):
        if ".git" in path.parts or ".venv" in path.parts or "__pycache__" in path.parts:
            continue
        errors.extend(check_file(path))

    print_result("check_no_placeholders_code", errors)


if __name__ == "__main__":
    main()
