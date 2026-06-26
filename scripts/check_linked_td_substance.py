#!/usr/bin/env python3
"""Check disciplinary substance of TD supports linked to operational sheets."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re
import unicodedata

from _qa_common import ROOT, strip_frontmatter
from check_linked_td_quality import target_td_files

GENERIC_PHRASES = [
    "résultat indicatif",
    "resultat indicatif",
    "réponse explicite attendue",
    "reponse explicite attendue",
    "solution explicite attendue",
    "démarche : partir de la donnée fournie",
    "demarche : partir de la donnee fournie",
    "isoler les grandeurs utiles",
    "conclusion explicite",
    "réponse cohérente",
    "reponse coherente",
    "production vérifiable",
    "production verifiable",
]

CONCRETE_PATTERNS = [
    r"\bSELECT\b.*\bFROM\b",
    r"\bINSERT\b|\bUPDATE\b|\bDELETE\b",
    r"\bTTL\b|\bACK\b|\bIP\b|\bTCP\b|\bHTTPS\b|\bRIP\b|\bOSPF\b",
    r"\broute\b|\bpaquet\b|\bpasserelle\b|\bmasque\b",
    r"\breturn\b|\bfor\b|\bwhile\b|\bif\b|\bdef\b",
    r"\bpseudo-code\b|\bpseudocode\b",
    r"\brécurrence\b|\brecurrence\b|\bétat\b|\betat\b|\bmémoïsation\b|\bmemoisation\b|\btabulation\b",
    r"\btrace\b|\btableau\b|\binvariant\b|\bcomplexité\b|\bcomplexite\b",
    r"\b\d+\b",
    r"`[^`]+`",
    r"\"[^\"]+\"",
    r"\bTrue\b|\bFalse\b|\bNone\b",
    r"\baffiché\b|\baffiche\b|\bretourné\b|\bretourne\b",
    r"\|.*\|",
    r"```",
]


@dataclass
class TDSubstanceResult:
    errors: list[str] = field(default_factory=list)
    checked_files: int = 0


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value.lower())
    value = "".join(char for char in value if not unicodedata.combining(char))
    value = re.sub(r"`[^`]+`", "`code`", value)
    value = re.sub(r"\b\d+\b", "n", value)
    value = re.sub(r"[^a-z0-9_]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def has_concrete_evidence(text: str) -> bool:
    return any(re.search(pattern, text, flags=re.I | re.S) for pattern in CONCRETE_PATTERNS)


def split_numbered_blocks(body: str, title: str) -> dict[int, str]:
    pattern = re.compile(
        rf"^###\s+{re.escape(title)}\s+(\d+)\b(.*?)(?=^###\s+{re.escape(title)}\s+\d+\b|^##\s+|\Z)",
        flags=re.M | re.S | re.I,
    )
    return {int(match.group(1)): match.group(2).strip() for match in pattern.finditer(body)}


def data_values(body: str) -> list[str]:
    values = []
    for match in re.finditer(r"Donn(?:é|e)es?\s*:\s*(.+)", body, flags=re.I):
        values.append(normalize(match.group(1)))
    return [value for value in values if value]


def domain_requirements(path: Path, body: str) -> list[str]:
    errors: list[str] = []
    name = path.name.lower()
    lower = body.lower()
    if "sql" in name:
        if "select" not in lower or " from " not in lower:
            errors.append("TD SQL sans requête SELECT/FROM concrète")
        if "résultat" not in lower and "resultat" not in lower and "|" not in body:
            errors.append("TD SQL sans résultat de requête vérifiable")
    if any(token in name for token in ["reseaux", "protocoles", "routage", "chiffrement", "https"]):
        markers = sum(token in lower for token in ["ttl", "ip", "ack", "paquet", "route", "passerelle", "https", "certificat"])
        if markers < 2:
            errors.append("TD réseau/sécurité sans champs, paquets, routes ou décisions explicites")
    if any(token in name for token in ["tris", "dichotomie", "glouton", "knn", "parcours", "programmation_dynamique", "boyer", "diviser", "calculabilite"]):
        markers = sum(
            token in lower
            for token in [
                "pseudo-code",
                "pseudocode",
                "trace",
                "tableau",
                "récurrence",
                "recurrence",
                "invariant",
                "complexité",
                "complexite",
            ]
        )
        if markers < 2:
            errors.append("TD algorithmique sans pseudo-code, trace, invariant, tableau ou complexité")
    return errors


def analyze_one_td(path: Path, root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    body = strip_frontmatter(text)
    rel = path.relative_to(root) if path.is_relative_to(root) else path
    lower = normalize(body)

    for phrase in GENERIC_PHRASES:
        if normalize(phrase) in lower:
            errors.append(f"{rel}: corrigé générique ou formulation non vérifiable -> {phrase}")

    exercises = split_numbered_blocks(body, "Exercice")
    corrections = split_numbered_blocks(body, "Corrigé exercice")
    for number, exercise in exercises.items():
        if len(normalize(exercise)) < 40:
            errors.append(f"{rel}: exercice {number} sans donnée propre suffisante")
        correction = corrections.get(number, "")
        if not correction:
            errors.append(f"{rel}: corrigé exercice {number} absent")
        elif any(normalize(phrase) in normalize(correction) for phrase in GENERIC_PHRASES) and not has_concrete_evidence(correction):
            errors.append(f"{rel}: corrigé exercice {number} sans résultat réel vérifiable")

    values = data_values(body)
    if len(values) >= 8 and len(set(values)) < 5:
        errors.append(f"{rel}: les 8 exercices réutilisent trop souvent la même donnée")

    normalized_exercises = {normalize(block) for block in exercises.values()}
    if len(exercises) >= 8 and len(normalized_exercises) < 6:
        errors.append(f"{rel}: exercices quasi identiques, variation disciplinaire insuffisante")

    for message in domain_requirements(path, body):
        errors.append(f"{rel}: {message}")
    return errors


def analyze_linked_td_substance(root: Path = ROOT, files: list[Path] | None = None) -> TDSubstanceResult:
    result = TDSubstanceResult()
    paths = files if files is not None else target_td_files(root)
    for path in paths:
        result.checked_files += 1
        result.errors.extend(analyze_one_td(path, root))
    return result


def main() -> int:
    result = analyze_linked_td_substance()
    if result.errors:
        print("check_linked_td_substance: KO")
        for error in result.errors[:180]:
            print(f"- {error}")
        return 1
    print(f"check_linked_td_substance: PASS ({result.checked_files} TD)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
