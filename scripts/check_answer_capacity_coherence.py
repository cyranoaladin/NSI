#!/usr/bin/env python3
"""Guard: verifie la coherence reponse/capacite/methode dans les exercices P13.

Deux niveaux de controle :
1. reponse↔methode : la reponse attendue est coherente avec la methode de la consigne
2. methode↔capacite : la methode de la consigne correspond a la capacite officielle

Motifs interdits (reponse incompatible avec la methode de la consigne) :
- variant/droite-gauche sous une consigne glouton ou k-NN
- glouton/pieces sous une consigne dichotomie ou variant
- k-NN/rouge/bleu/vote sous une consigne dichotomie ou glouton
- cible 40 absente hors contexte dichotomie

Usage :
    python -m scripts.check_answer_capacity_coherence
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Method signatures in consignes
METHOD_DICHOTOMIE = re.compile(
    r"calculer milieu|réduire intervalle|recherche dichotomique", re.I
)
METHOD_VARIANT = re.compile(
    r"droite.gauche diminue|variant.*boucle|terminaison.*dichotom|variant.*erroné|variant.*corriger", re.I
)
METHOD_GLOUTON = re.compile(
    r"plus grande pièce possible|algorithme glouton|rendu de monnaie", re.I
)
METHOD_KNN = re.compile(
    r"voter parmi.*voisins|k.NN|k plus proches|vote majoritaire|classifier par k", re.I
)

# Answer fingerprints
ANSWER_DICHOTOMIE = re.compile(
    r"milieux?\s+18.*37.*indice\s+4|trouvé indice 4", re.I
)
ANSWER_VARIANT = re.compile(
    r"variant.*décroît|droite.gauche décroît|décroît de 5 à 1|terminaison", re.I
)
ANSWER_GLOUTON = re.compile(
    r"10\s*\+\s*10\s*\+\s*5\s*\+\s*2\s*\+\s*1|28\s*=\s*10|5 pièces", re.I
)
ANSWER_KNN = re.compile(
    r"rouge.*voix.*bleu|classe rouge|vote.*rouge|rouge 2|A=2.*B=1", re.I
)

# Forbidden cross-contamination patterns
FORBIDDEN = [
    # (method_regex, forbidden_answer_regex, description)
    (METHOD_DICHOTOMIE, ANSWER_GLOUTON, "reponse glouton sous consigne dichotomie"),
    (METHOD_DICHOTOMIE, ANSWER_KNN, "reponse k-NN sous consigne dichotomie"),
    (METHOD_DICHOTOMIE, ANSWER_VARIANT, "reponse variant sous consigne dichotomie"),
    (METHOD_VARIANT, ANSWER_GLOUTON, "reponse glouton sous consigne variant"),
    (METHOD_VARIANT, ANSWER_KNN, "reponse k-NN sous consigne variant"),
    (METHOD_VARIANT, ANSWER_DICHOTOMIE, "reponse dichotomie sous consigne variant"),
    (METHOD_GLOUTON, ANSWER_DICHOTOMIE, "reponse dichotomie sous consigne glouton"),
    (METHOD_GLOUTON, ANSWER_KNN, "reponse k-NN sous consigne glouton"),
    (METHOD_GLOUTON, ANSWER_VARIANT, "reponse variant sous consigne glouton"),
    (METHOD_KNN, ANSWER_DICHOTOMIE, "reponse dichotomie sous consigne k-NN"),
    (METHOD_KNN, ANSWER_GLOUTON, "reponse glouton sous consigne k-NN"),
    (METHOD_KNN, ANSWER_VARIANT, "reponse variant sous consigne k-NN"),
]

# "cible 40 absente" must only appear in dichotomie context
CIBLE_40_RE = re.compile(r"cible\s+40\s+absente", re.I)

# cas-limite mismatches: each method has its own cas-limite
CASLIMITE_GLOUTON = re.compile(r"pièce 1 absente|glouton.*échouer", re.I)
CASLIMITE_KNN = re.compile(r"égalité de vote|k pair", re.I)

CASLIMITE_FORBIDDEN = [
    (METHOD_GLOUTON, CASLIMITE_KNN, "cas-limite k-NN sous consigne glouton"),
    (METHOD_GLOUTON, re.compile(r"cible absente(?!.*variant)", re.I), "cas-limite dichotomie sous consigne glouton"),
    (METHOD_KNN, CASLIMITE_GLOUTON, "cas-limite glouton sous consigne k-NN"),
    (METHOD_KNN, re.compile(r"cible absente(?!.*variant)", re.I), "cas-limite dichotomie sous consigne k-NN"),
    (METHOD_DICHOTOMIE, CASLIMITE_GLOUTON, "cas-limite glouton sous consigne dichotomie"),
    (METHOD_DICHOTOMIE, CASLIMITE_KNN, "cas-limite k-NN sous consigne dichotomie"),
    (METHOD_VARIANT, CASLIMITE_GLOUTON, "cas-limite glouton sous consigne variant"),
    (METHOD_VARIANT, CASLIMITE_KNN, "cas-limite k-NN sous consigne variant"),
]

# Capacity → allowed methods mapping
# P-ALGO-03 covers both dichotomie-recherche AND k-NN
# P-ALGO-04 covers variant de boucle (terminaison dichotomie)
# P-ALGO-05 covers glouton
CAPACITY_METHODS: dict[str, list[str]] = {
    "P-ALGO-03": ["dichotomie", "knn"],
    "P-ALGO-04": ["variant"],
    "P-ALGO-05": ["glouton"],
}

EXERCISE_HEADER_RE = re.compile(
    r"^#{2,3}\s+(?:Exercice|Corrigé exercice)\s+(\d+)\s*$", re.M
)


def parse_blocks(text: str) -> list[dict[str, str]]:
    """Split a markdown document into exercise/corrige blocks."""
    headers = list(EXERCISE_HEADER_RE.finditer(text))
    blocks: list[dict[str, str]] = []
    for i, m in enumerate(headers):
        end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        block_text = text[m.start():end]
        blocks.append({
            "title": m.group(0).strip(),
            "num": m.group(1),
            "text": block_text,
        })
    return blocks


def parse_eval_questions(text: str) -> list[dict[str, str]]:
    """Parse 'Corrige de l evaluation' section."""
    m = re.search(r"##\s+Corrigé de l.évaluation", text)
    if not m:
        return []
    section = text[m.start():]
    questions: list[dict[str, str]] = []
    for qm in re.finditer(r"^-\s+Question\s+(\d+)\s*:\s*(.+)$", section, re.M):
        questions.append({
            "title": f"Question {qm.group(1)} (eval)",
            "num": qm.group(1),
            "text": qm.group(2),
        })
    return questions


def detect_method(text: str) -> str | None:
    """Identify the method from a consigne line."""
    if METHOD_DICHOTOMIE.search(text):
        return "dichotomie"
    if METHOD_VARIANT.search(text):
        return "variant"
    if METHOD_GLOUTON.search(text):
        return "glouton"
    if METHOD_KNN.search(text):
        return "knn"
    return None


def check_block(block: dict[str, str], filename: str) -> list[str]:
    """Check a single exercise block for answer/method and method/capacity coherence."""
    errors: list[str] = []
    text = block["text"]
    title = block["title"]

    # Find method from consigne
    consigne_match = re.search(r"Consigne\s*:\s*(.+?)(?:\n|$)", text)
    method_line = consigne_match.group(1) if consigne_match else text
    method = detect_method(method_line)

    if method is None:
        return errors

    # --- Check method↔capacity coherence ---
    capacity_match = re.search(r"Capacité officielle\s*:\s*(P-ALGO-\d+)", text)
    if capacity_match:
        cap_id = capacity_match.group(1)
        allowed = CAPACITY_METHODS.get(cap_id, [])
        if allowed and method not in allowed:
            errors.append(
                f"{filename} {title}: methode '{method}' incompatible avec "
                f"capacite {cap_id} (attendu: {'/'.join(allowed)})"
            )

    # --- Check answer↔method coherence ---
    answer_match = re.search(
        r"(?:Réponse attendue|Résultat attendu)\s*:\s*(.+?)(?:\n|$)", text
    )
    if not answer_match:
        return errors
    answer = answer_match.group(1)

    # Check forbidden answer patterns
    for method_re, forbidden_re, desc in FORBIDDEN:
        if method_re.search(method_line) and forbidden_re.search(answer):
            errors.append(f"{filename} {title}: {desc}")

    # Check cible 40 absente outside dichotomie
    if method != "dichotomie" and CIBLE_40_RE.search(text):
        errors.append(
            f"{filename} {title}: 'cible 40 absente' hors contexte dichotomie"
        )

    # Check cas-limite coherence
    caslimite_match = re.search(r"traiter aussi\s*`([^`]+)`", text)
    critere_match = re.search(r"décision sur\s*`([^`]+)`", text)
    caslimite_text = ""
    if caslimite_match:
        caslimite_text += caslimite_match.group(1) + " "
    if critere_match:
        caslimite_text += critere_match.group(1)

    if caslimite_text:
        for method_re, forbidden_re, desc in CASLIMITE_FORBIDDEN:
            if method_re.search(method_line) and forbidden_re.search(caslimite_text):
                errors.append(f"{filename} {title}: {desc}")

    return errors


def check_corrige_block(block: dict[str, str], filename: str) -> list[str]:
    """Check a corrige block for method↔capacity coherence.

    In corrige blocks, the method appears in the Justification line
    (e.g. 'la tâche `<method>`') and the capacity in 'Capacité mobilisée'.
    """
    errors: list[str] = []
    text = block["text"]
    title = block["title"]

    # Extract capacity
    cap_match = re.search(r"Capacité mobilisée\s*:\s*(P-ALGO-\d+)", text)
    if not cap_match:
        return errors
    cap_id = cap_match.group(1)

    # Extract method from Justification task
    task_match = re.search(r"la tâche\s*`([^`]+)`", text)
    if not task_match:
        return errors
    task_text = task_match.group(1)
    method = detect_method(task_text)
    if method is None:
        return errors

    allowed = CAPACITY_METHODS.get(cap_id, [])
    if allowed and method not in allowed:
        errors.append(
            f"{filename} {title}: methode '{method}' incompatible avec "
            f"capacite {cap_id} (attendu: {'/'.join(allowed)})"
        )

    return errors


def check_eval_question(q: dict[str, str], filename: str) -> list[str]:
    """Check a single eval question for cible 40 absente contamination."""
    errors: list[str] = []
    if CIBLE_40_RE.search(q["text"]):
        errors.append(
            f"{filename} {q['title']}: 'cible 40 absente' dans corrige eval"
        )
    return errors


def check_file(filepath: Path) -> list[str]:
    """Check all blocks in a file."""
    if not filepath.exists():
        return []
    text = filepath.read_text(encoding="utf-8", errors="replace")
    filename = filepath.name
    errors: list[str] = []

    blocks = parse_blocks(text)
    for block in blocks:
        if block["title"].startswith("### Corrigé exercice"):
            errors.extend(check_corrige_block(block, filename))
        errors.extend(check_block(block, filename))

    # Check eval section in corrige
    if "corrige" in filename.lower():
        for q in parse_eval_questions(text):
            errors.extend(check_eval_question(q, filename))

    return errors


def main() -> None:
    p13_dir = (
        ROOT
        / "03_progressions"
        / "supports"
        / "premiere"
        / "P13"
    )
    files = [
        p13_dir / "P13_TD_dichotomie_glouton_knn.md",
        p13_dir / "P13_corrige_dichotomie_glouton_knn.md",
    ]

    all_errors: list[str] = []
    for f in files:
        all_errors.extend(check_file(f))

    if all_errors:
        print(f"FAIL  check_answer_capacity_coherence: {len(all_errors)} erreur(s)")
        for e in all_errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("OK  check_answer_capacity_coherence: coherence reponse/capacite verifiee")


if __name__ == "__main__":
    main()
