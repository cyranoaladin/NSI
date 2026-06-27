#!/usr/bin/env python3
"""Measure the portable extracted-source audit command budget."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import os
import shlex
import subprocess
import time

from _qa_common import ROOT


@dataclass
class MeasuredCommand:
    command: str
    seconds: float
    returncode: int


@dataclass
class RuntimeBudgetResult:
    errors: list[str] = field(default_factory=list)
    commands: list[MeasuredCommand] = field(default_factory=list)
    total_seconds: float = 0.0


def audit_extracted_commands(root: Path = ROOT) -> list[str]:
    makefile = (root / "Makefile").read_text(encoding="utf-8")
    lines = makefile.splitlines()
    commands: list[str] = []
    in_target = False
    for line in lines:
        if line.startswith("audit-extracted-source:"):
            in_target = True
            continue
        if in_target and line and not line.startswith("\t") and not line.startswith(" "):
            break
        if in_target and line.startswith("\t"):
            command = line.strip()
            if command and not command.startswith("@"):
                commands.append(command)
    return commands


def run_command(command: str, root: Path, timeout_seconds: int = 120) -> MeasuredCommand:
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env.pop("NSI_DOCUMENTS_DRIVE_ROOT", None)
    start = time.monotonic()
    try:
        completed = subprocess.run(
            command,
            cwd=root,
            env=env,
            shell=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout_seconds,
        )
        returncode = completed.returncode
    except subprocess.TimeoutExpired:
        return MeasuredCommand(command, timeout_seconds, 124)
    seconds = time.monotonic() - start
    return MeasuredCommand(command, seconds, returncode)


def evaluate_runtime_budget(
    commands: list[MeasuredCommand],
    total_budget: float = 180.0,
    slow_threshold: float = 10.0,
) -> RuntimeBudgetResult:
    result = RuntimeBudgetResult(commands=commands, total_seconds=sum(item.seconds for item in commands))
    if result.total_seconds > total_budget:
        result.errors.append(f"durée totale {result.total_seconds:.2f}s > budget {total_budget:.0f}s")
    for item in commands:
        if item.returncode != 0:
            result.errors.append(f"commande en échec ({item.returncode}) -> {item.command}")
        if item.seconds > slow_threshold:
            result.errors.append(f"commande lente > {slow_threshold:.0f}s: {item.seconds:.2f}s -> {item.command}")
    return result


def analyze_audit_extracted_runtime_budget(root: Path = ROOT) -> RuntimeBudgetResult:
    commands = audit_extracted_commands(root)
    measured = [run_command(command, root) for command in commands]
    return evaluate_runtime_budget(measured)


def main() -> int:
    result = analyze_audit_extracted_runtime_budget()
    print("Durées audit-extracted-source:")
    for item in result.commands:
        print(f"- {item.seconds:.2f}s rc={item.returncode} :: {item.command}", flush=True)
    print(f"Durée totale audit-extracted-source: {result.total_seconds:.2f}s", flush=True)
    if result.errors:
        print("check_audit_extracted_runtime_budget: KO")
        for error in result.errors[:120]:
            print(f"- {error}")
        return 1
    print("check_audit_extracted_runtime_budget: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
