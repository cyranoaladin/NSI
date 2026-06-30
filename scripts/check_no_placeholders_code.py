#!/usr/bin/env python3
"""Reject unfinished code constructs without blanket exclusion of Python files."""

from __future__ import annotations

from pathlib import Path
from typing import List
import ast
import io
import tokenize

from scripts._qa_common import ROOT, print_result

COMMENT_MARKERS = ("TO" + "DO", "FIX" + "ME", "X" + "XX", "TBD")


def _set_parents(tree: ast.AST) -> None:
    """Annotate every node with a _parent attribute."""
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            child._parent = node  # type: ignore[attr-defined]


def _ellipsis_is_in_annotation(node: ast.Constant) -> bool:
    """Return True if the Ellipsis node sits inside a type annotation context.

    Allowed: tuple[Any, ...], Callable[..., int], slice Subscript, etc.
    Forbidden: def f(): ..., x = ..., standalone Expr(...).
    """
    current: ast.AST = node
    while hasattr(current, "_parent"):
        parent = current._parent
        # Ellipsis inside a Subscript slice (e.g. tuple[Any, ...]) -> annotation
        if isinstance(parent, ast.Subscript) and current is parent.slice:
            return True
        if isinstance(parent, ast.Tuple) and hasattr(parent, "_parent"):
            grandparent = parent._parent
            if isinstance(grandparent, ast.Subscript) and parent is grandparent.slice:
                return True
        # Ellipsis in a function annotation (return type or arg annotation)
        if isinstance(parent, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if current is parent.returns:
                return True
        if isinstance(parent, ast.arg) and current is parent.annotation:
            return True
        if isinstance(parent, ast.AnnAssign):
            if current is parent.annotation:
                return True
        current = parent
    return False


def check_file(path: Path) -> List[str]:
    rel = path.relative_to(ROOT)
    text = path.read_text(encoding="utf-8", errors="replace")
    errors: List[str] = []

    try:
        tree = ast.parse(text, filename=str(path))
    except SyntaxError as exc:
        return [f"{rel}: syntaxe Python invalide ({exc})"]

    _set_parents(tree)

    for node in ast.walk(tree):
        if isinstance(node, ast.Pass):
            errors.append(f"{rel}:{node.lineno}: instruction pass interdite")
        if isinstance(node, ast.Raise):
            raised = node.exc
            if isinstance(raised, ast.Call):
                name = getattr(raised.func, "id", "")
            else:
                name = getattr(raised, "id", "")
            if name == "NotImplementedError":
                errors.append(f"{rel}:{node.lineno}: NotImplementedError interdit")
        if isinstance(node, ast.Constant) and node.value is Ellipsis:
            if not _ellipsis_is_in_annotation(node):
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
