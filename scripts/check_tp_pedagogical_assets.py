#!/usr/bin/env python3
"""Check that first-batch TP Python assets are pedagogically meaningful."""

from __future__ import annotations

from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path
import ast
import os
import re
import shutil
import subprocess
import sys
import tempfile

from _qa_common import ROOT
from check_first_batch_document_quality import FIRST_BATCH_PREFIXES


@dataclass
class TpPedagogyResult:
    errors: list[str] = field(default_factory=list)


def normalize(text: str) -> str:
    text = re.sub(r"\s+", " ", text.lower())
    text = re.sub(r"['\"][^'\"]{8,}['\"]", "'CONST'", text)
    return text.strip()


def code_similarity(left: str, right: str) -> float:
    return SequenceMatcher(None, normalize(left), normalize(right)).ratio()


def find_code_dir(root: Path, prefix: str) -> Path:
    base = root / "03_progressions" / "supports"
    search_root = base if base.exists() else root
    matches = sorted(path for path in search_root.rglob(prefix) if path.is_dir())
    return (matches[0] / "code") if matches else search_root / prefix / "code"


def first_asset(code_dir: Path, pattern: str) -> Path | None:
    matches = sorted(code_dir.glob(pattern))
    return matches[0] if matches else None


def hardcoded_returns(path: Path) -> bool:
    try:
        tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
    except SyntaxError:
        return True
    for node in ast.walk(tree):
        if isinstance(node, ast.Return):
            value = node.value
            if isinstance(value, ast.Constant):
                return True
            if isinstance(value, ast.Dict):
                constant_values = sum(isinstance(item, ast.Constant) for item in value.values if item is not None)
                if constant_values >= max(1, len(value.values) - 1):
                    return True
    return False


def test_function_names(text: str) -> set[str]:
    return set(re.findall(r"^def\s+(test_[A-Za-z0-9_]+)\s*\(", text, flags=re.M))


def call_arguments(text: str) -> set[str]:
    return set(re.findall(r"\w+\(([^()\n]+)\)", text))


def tests_are_substantive(text: str) -> list[str]:
    errors: list[str] = []
    tests = test_function_names(text)
    if len(tests) < 3:
        errors.append("tests insuffisants: moins de 3 fonctions test")
    lowered = text.lower()
    if "none" not in lowered and "valueerror" not in lowered and "invalid" not in lowered:
        errors.append("tests insuffisants: entrée invalide absente")
    if "limite" not in lowered and "edge" not in lowered and "cas_" not in lowered:
        errors.append("tests insuffisants: cas limite absent")
    if len(call_arguments(text)) < 3:
        errors.append("tests insuffisants: moins de 3 entrées distinctes")
    if re.search(r"assert\s+[^=\n]+==\s*['\"][^'\"]+['\"]", text) and len(tests) < 3:
        errors.append("tests insuffisants: validation de constante textuelle")
    return errors


def run_tests(code_dir: Path, tests: Path, module_name: str) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["TP_MODULE"] = module_name
    return subprocess.run(
        [sys.executable, str(tests.name)],
        cwd=code_dir,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        timeout=10,
    )


def analyze_prefix(root: Path, prefix: str) -> list[str]:
    errors: list[str] = []
    code_dir = find_code_dir(root, prefix)
    starter = first_asset(code_dir, f"{prefix}_starter*.py")
    tests = first_asset(code_dir, f"{prefix}_tests_attendus*.py")
    corrige = first_asset(code_dir, f"{prefix}_corrige_professeur*.py")
    if not starter or not tests or not corrige:
        return [f"{prefix}: assets TP incomplets"]

    starter_text = starter.read_text(encoding="utf-8", errors="replace")
    corrige_text = corrige.read_text(encoding="utf-8", errors="replace")
    tests_text = tests.read_text(encoding="utf-8", errors="replace")

    if hardcoded_returns(starter):
        errors.append(f"{starter}: starter hardcodé ou solution complète")
    if code_similarity(starter_text, corrige_text) >= 0.82:
        errors.append(f"{prefix}: corrigé professeur quasi identique au starter")
    errors.extend(f"{tests}: {error}" for error in tests_are_substantive(tests_text))

    with tempfile.TemporaryDirectory() as raw:
        temp_code = Path(raw)
        for path in [starter, tests, corrige]:
            shutil.copy2(path, temp_code / path.name)
        corrige_module = corrige.stem
        starter_module = starter.stem
        corrige_run = run_tests(temp_code, temp_code / tests.name, corrige_module)
        if corrige_run.returncode != 0:
            errors.append(f"{prefix}: les tests attendus échouent sur le corrigé professeur")
        starter_run = run_tests(temp_code, temp_code / tests.name, starter_module)
        if starter_run.returncode == 0:
            errors.append(f"{prefix}: le starter valide les tests complets")
        for cache in temp_code.rglob("__pycache__"):
            shutil.rmtree(cache)
    return errors


def analyze_tp_pedagogy(root: Path = ROOT, prefixes: list[str] | None = None) -> TpPedagogyResult:
    prefixes = prefixes or FIRST_BATCH_PREFIXES
    result = TpPedagogyResult()
    for prefix in prefixes:
        result.errors.extend(analyze_prefix(root, prefix))
    return result


def main() -> int:
    result = analyze_tp_pedagogy()
    if result.errors:
        print("check_tp_pedagogical_assets: KO")
        for error in result.errors[:160]:
            print(f"- {error}")
        return 1
    print("check_tp_pedagogical_assets: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
