#!/usr/bin/env python3
"""Check that course documents are explanatory courses, not answer sheets."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re

from _qa_common import ROOT, read_frontmatter, strip_frontmatter


COURSE_RE = re.compile(r"(^|_)cours_", re.I)
GENERIC_SECTION_ONLY_RE = re.compile(
    r"Objectifs spécifiques\s*#+\s*À savoir\s*#+\s*Méthodes\s*#+\s*Exemples corrigés\s*#+\s*Critères",
    re.I | re.S,
)


@dataclass
class CourseQualityResult:
    errors: list[str] = field(default_factory=list)
    files_checked: int = 0


def useful_word_count(text: str) -> int:
    body = strip_frontmatter(text)
    body = re.sub(r"^#+.*$", " ", body, flags=re.M)
    return len(re.findall(r"\b[\wÀ-ÿ]{3,}\b", body))


def count_heading_or_marker(text: str, pattern: str) -> int:
    return len(re.findall(pattern, strip_frontmatter(text), re.I))


def introductory_block(text: str) -> str:
    body = strip_frontmatter(text)
    match = re.search(r"^##\s+Exemples corrigés", body, flags=re.I | re.M)
    return body[: match.start()] if match else body[:1600]


def course_quality_errors(text: str, rel: str) -> list[str]:
    errors: list[str] = []
    body = strip_frontmatter(text)
    intro = introductory_block(text)
    if useful_word_count(text) < 170:
        errors.append(f"{rel}: cours trop court pour être autonome")
    if GENERIC_SECTION_ONLY_RE.search(body) and useful_word_count(text) < 80:
        errors.append(f"{rel}: structure de fiche sans explication disciplinaire")
    if not re.search(r"Situation-problème|Situation-probleme|À savoir|A savoir|Définition|Definition", intro, re.I):
        errors.append(f"{rel}: introduction conceptuelle insuffisamment explicative")
    if count_heading_or_marker(text, r"Exemple corrigé\s+\d+|###\s+Exemple") < 3:
        errors.append(f"{rel}: moins de trois exemples gradués")
    if count_heading_or_marker(text, r"erreur fréquente|##\s+Erreurs fréquentes|-\s+[^.\n]*(?:confond|oublie|écrase|inverse)") < 1:
        errors.append(f"{rel}: erreurs fréquentes spécifiques insuffisantes")
    if count_heading_or_marker(text, r"cas limite|vide|absent|invalide|doublon|exception|interblocage") < 2:
        errors.append(f"{rel}: cas limites spécifiques insuffisants")
    if not re.search(r"##\s+(?:Critères|À retenir|A retenir|Synthèse|Synthese)", body, re.I):
        errors.append(f"{rel}: synthèse finale ou critères de révision absents")
    if not re.search(r"[PT](?:-[A-Z]+)+-\d{2}[A-Z]?", text):
        errors.append(f"{rel}: capacité officielle non citée")
    has_knowledge = bool(re.search(r"À savoir|A savoir|Définitions?|Definitions?|formalisation", body, re.I))
    has_method = bool(re.search(r"Méthodes?|Methodes?|savoir-faire|Démarche attendue|Demarche attendue", body, re.I))
    if not has_knowledge or not has_method:
        errors.append(f"{rel}: distinction savoir / savoir-faire / méthode insuffisante")
    return errors


def candidate_courses(root: Path = ROOT) -> list[Path]:
    paths: list[Path] = []
    base = root / "03_progressions" / "supports"
    for path in sorted(base.rglob("*.md")):
        metadata = read_frontmatter(path)
        if str(metadata.get("document_type", "")).lower() == "cours" or COURSE_RE.search(path.name):
            paths.append(path)
    return paths


def analyze_course_explanatory_quality(root: Path = ROOT) -> CourseQualityResult:
    result = CourseQualityResult()
    for path in candidate_courses(root):
        result.files_checked += 1
        rel = path.relative_to(root).as_posix()
        result.errors.extend(course_quality_errors(path.read_text(encoding="utf-8", errors="replace"), rel))
    return result


def main() -> int:
    result = analyze_course_explanatory_quality()
    if result.errors:
        print("check_course_explanatory_quality: KO")
        for error in result.errors[:200]:
            print(f"- {error}")
        return 1
    print(f"check_course_explanatory_quality: PASS ({result.files_checked} cours)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
