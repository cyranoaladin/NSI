#!/usr/bin/env python3
"""Render a unit to a temporary directory and verify student/prof separation."""

from __future__ import annotations

import argparse
import tempfile
from pathlib import Path

from _qa_common import ROOT, print_result
from render_unit import CHARTER, render


def check_unit(unit: str) -> list[str]:
    errors: list[str] = []
    with tempfile.TemporaryDirectory(prefix="nsi_render_") as tmp:
        out = render(unit, Path(tmp))
        expected = {
            "version élève HTML": out / f"{unit}_eleve.html",
            "version prof HTML": out / f"{unit}_prof.html",
            "version élève PDF": out / f"{unit}_eleve.pdf",
            "version prof PDF": out / f"{unit}_prof.pdf",
        }
        for label, path in expected.items():
            if not path.exists() or path.stat().st_size < 80:
                errors.append(f"{unit}: {label} absent ou vide")
        student = (out / f"{unit}_eleve.html").read_text(encoding="utf-8", errors="replace")
        teacher = (out / f"{unit}_prof.html").read_text(encoding="utf-8", errors="replace")
        if CHARTER not in student or CHARTER not in teacher:
            errors.append(f"{unit}: marqueur de charte absent")
        forbidden = ["corrigé professeur", "corrige professeur", "corrige_professeur", "barème", "bareme", "professeur"]
        lower_student = student.lower()
        if any(token in lower_student for token in forbidden):
            errors.append(f"{unit}: version élève contient un marqueur de corrigé/professeur")
        lower_teacher = teacher.lower()
        if not any(token in lower_teacher for token in ["corrige", "corrigé", "bareme", "barème"]):
            errors.append(f"{unit}: version prof ne contient pas corrigé/barème")
        print(f"{unit}: version élève et version prof vérifiées dans un rendu temporaire")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--unit", required=True)
    args = parser.parse_args()
    print_result("check_rendered_unit_artifacts", check_unit(args.unit))


if __name__ == "__main__":
    main()
