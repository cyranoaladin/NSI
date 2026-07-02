"""Guard: resolve_env_file must be the ONLY place READING RAG_ENV_FILE in scripts/.

Uses AST to detect ANY form of read access to the env var, regardless of syntax:
os.getenv("RAG_ENV_FILE"), os.environ["RAG_ENV_FILE"], os.environ.get(...),
from os import environ; environ[...], from os import getenv; getenv(...), etc.

Distinguishes READS (forbidden outside rag_core) from WRITES/overrides (allowed,
e.g. command_env["RAG_ENV_FILE"] = ... in check_quality_gates.py).
"""
from __future__ import annotations

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _find_rag_env_file_reads(source: str) -> list[int]:
    """Return line numbers where RAG_ENV_FILE is READ (not assigned)."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []

    reads: list[int] = []

    # Annotate parents for context detection
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            child._parent = node  # type: ignore[attr-defined]

    for node in ast.walk(tree):
        if not isinstance(node, ast.Constant) or node.value != "RAG_ENV_FILE":
            continue
        parent = getattr(node, "_parent", None)
        if parent is None:
            continue

        # Case: function call argument — os.getenv("RAG_ENV_FILE", ...)
        # or os.environ.get("RAG_ENV_FILE", ...)
        if isinstance(parent, ast.Call):
            reads.append(node.lineno)
            continue

        # Case: subscript index — os.environ["RAG_ENV_FILE"] or environ["..."]
        if isinstance(parent, ast.Subscript):
            # Distinguish read (Load) from write (Store/Del)
            if isinstance(parent.ctx, ast.Load):
                reads.append(node.lineno)
            # Store = assignment target (e.g. env["RAG_ENV_FILE"] = ...) -> OK
            continue

        # Case: argument in args list of a call (e.g. getenv("RAG_ENV_FILE"))
        # Already caught by Call parent above for direct args
        # For keyword args:
        if isinstance(parent, ast.keyword):
            reads.append(node.lineno)
            continue

    return sorted(set(reads))


# ---------------------------------------------------------------------------
# Guard on real codebase
# ---------------------------------------------------------------------------

def test_no_inline_env_resolution_outside_rag_core() -> None:
    """Only rag_core.resolve_env_file may read RAG_ENV_FILE."""
    violations: list[str] = []
    scripts_dir = ROOT / "scripts"
    for py in sorted(scripts_dir.glob("*.py")):
        if py.name == "rag_core.py":
            continue
        source = py.read_text(encoding="utf-8")
        for lineno in _find_rag_env_file_reads(source):
            line = source.splitlines()[lineno - 1].strip()
            violations.append(f"{py.name}:{lineno}: {line}")
    assert not violations, (
        "Inline RAG_ENV_FILE read found outside rag_core.py — "
        "use resolve_env_file() instead:\n" + "\n".join(violations)
    )


# ---------------------------------------------------------------------------
# Exhaustive adverse matrix — each form must be DETECTED
# ---------------------------------------------------------------------------

_ADVERSE_CASES: list[tuple[str, str, bool]] = [
    # (label, code, should_detect)
    ("os.getenv no default", 'import os\nx = os.getenv("RAG_ENV_FILE")\n', True),
    ("os.getenv with default", 'import os\nx = os.getenv("RAG_ENV_FILE", "d")\n', True),
    ("os.environ brackets", 'import os\nx = os.environ["RAG_ENV_FILE"]\n', True),
    ("os.environ.get no default", 'import os\nx = os.environ.get("RAG_ENV_FILE")\n', True),
    ("os.environ.get with default", 'import os\nx = os.environ.get("RAG_ENV_FILE", "d")\n', True),
    ("from os import environ brackets", 'from os import environ\nx = environ["RAG_ENV_FILE"]\n', True),
    ("from os import getenv", 'from os import getenv\nx = getenv("RAG_ENV_FILE")\n', True),
    # WRITE (assignment) — must NOT be detected
    ("assignment (override)", 'import os\nos.environ["RAG_ENV_FILE"] = "/path"\n', False),
    ("dict assignment", 'env = {}\nenv["RAG_ENV_FILE"] = "/path"\n', False),
    # Clean — no access at all
    ("no access", 'x = 1\n', False),
]


def test_adverse_matrix() -> None:
    """Each form of RAG_ENV_FILE access must be correctly detected or ignored."""
    failures: list[str] = []
    for label, code, should_detect in _ADVERSE_CASES:
        lines = _find_rag_env_file_reads(code)
        detected = len(lines) > 0
        if detected != should_detect:
            expected = "ROUGE" if should_detect else "VERT"
            actual = "ROUGE" if detected else "VERT"
            failures.append(f"  {label}: expected {expected}, got {actual} (lines={lines})")
    assert not failures, "Adverse matrix failures:\n" + "\n".join(failures)
