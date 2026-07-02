"""Guard: resolve_env_file must be the ONLY place reading RAG_ENV_FILE in scripts/.

If a future consumer re-inlines the resolution, this test fails.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Pattern: os.getenv("RAG_ENV_FILE" or os.environ["RAG_ENV_FILE"] or
# os.environ.get("RAG_ENV_FILE" — the resolution pattern itself.
INLINE_PATTERN = re.compile(
    r"""(?:os\.getenv|os\.environ(?:\[|\.get))\s*\(\s*['"]RAG_ENV_FILE['"]"""
)


def test_no_inline_env_resolution_outside_rag_core() -> None:
    """Only rag_core.resolve_env_file may read RAG_ENV_FILE."""
    violations: list[str] = []
    scripts_dir = ROOT / "scripts"
    for py in sorted(scripts_dir.glob("*.py")):
        if py.name == "rag_core.py":
            continue
        text = py.read_text(encoding="utf-8")
        for i, line in enumerate(text.splitlines(), 1):
            if INLINE_PATTERN.search(line):
                violations.append(f"{py.name}:{i}: {line.strip()}")
    assert not violations, (
        "Inline RAG_ENV_FILE resolution found outside rag_core.py — "
        "use resolve_env_file() instead:\n" + "\n".join(violations)
    )
