#!/usr/bin/env python3
"""Run unit tests in repository test files."""

from __future__ import annotations

from pathlib import Path
import importlib.util
import unittest
import sys

ROOT = Path(__file__).resolve().parents[1]


def load_tests_from_file(path: Path):
    name = 'nsitest_' + path.stem.replace('-', '_')
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return unittest.defaultTestLoader.loadTestsFromModule(module)


def main() -> None:
    suite = unittest.TestSuite()
    for path in sorted(ROOT.rglob('test*.py')):
        if 'tests' not in path.parts:
            continue
        if path.suffix != '.py':
            continue
        suite.addTests(load_tests_from_file(path))

    if suite.countTestCases() == 0:
        print('NO TESTS')
        return

    result = unittest.TestResult()
    suite.run(result)
    print(f"run_python_tests: tests exécutés = {result.testsRun}")
    for test, traceback in result.failures:
        print(f"FAIL: {test}")
        print(traceback)
    for test, traceback in result.errors:
        print(f"ERROR: {test}")
        print(traceback)
    if not result.wasSuccessful():
        print('run_python_tests: KO')
        raise SystemExit(1)
    print('run_python_tests: PASS')


if __name__ == '__main__':
    main()
