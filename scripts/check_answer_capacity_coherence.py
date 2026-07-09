#!/usr/bin/env python3
"""Guard: verifie la coherence reponse/capacite/methode dans les supports.

Scanne toutes les sequences via leurs contrats et verifie dans chaque
support (TD, corrige, tp, trace, version_amenagee, evaluation, bareme,
remediation) :
1. reponse↔methode : la reponse attendue est coherente avec la methode
2. methode↔capacite : la methode de la consigne correspond a la capacite
3. pas de "cible 40 absente" hors contexte dichotomie (global, pas lie a answer_match)
4. les reponses positionnelles (version_amenagee) suivent l'ordre capacite
5. blocs corrige autonome "### Exercice N" avec "Capacite mobilisee" valides

Mapping autorite (programme_nsi_2019.yaml) :
  P-ALGO-03 = k-NN seul
  P-ALGO-04 = recherche dichotomique (recherche + variant)
  P-ALGO-05 = algorithmes gloutons

Usage :
    python -m scripts.check_answer_capacity_coherence
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONTRACTS_DIR = ROOT / "03_progressions" / "supports" / "contracts"
SUPPORTS_DIR = ROOT / "03_progressions" / "supports"

# ---------------------------------------------------------------------------
# Method signatures in consignes
# ---------------------------------------------------------------------------
METHOD_DICHOTOMIE = re.compile(
    r"calculer milieu|réduire intervalle|recherche dichotomique", re.I
)
METHOD_VARIANT = re.compile(
    r"droite.gauche diminue|droite.gauche décroît"
    r"|variant.*boucle|terminaison.*dichotom"
    r"|variant.*erroné|variant.*corriger", re.I
)
METHOD_GLOUTON = re.compile(
    r"plus grande pièce possible|algorithme glouton|rendu de monnaie", re.I
)
METHOD_KNN = re.compile(
    r"voter parmi.*voisins|k.NN|k plus proches|vote majoritaire"
    r"|classifier par k", re.I
)

# ---------------------------------------------------------------------------
# Answer fingerprints
# ---------------------------------------------------------------------------
ANSWER_DICHOTOMIE = re.compile(
    r"milieux?\s+18.*37.*indice\s+4|trouvé indice 4", re.I
)
ANSWER_VARIANT = re.compile(
    r"variant.*décroît|droite.gauche décroît|décroît de 5 à 1"
    r"|décroît.*terminaison|terminaison prouvée", re.I
)
ANSWER_GLOUTON = re.compile(
    r"10\s*\+\s*10\s*\+\s*5\s*\+\s*2\s*\+\s*1|28\s*=\s*10|5 pièces", re.I
)
ANSWER_KNN = re.compile(
    r"rouge.*voix.*bleu|classe rouge|vote.*rouge|rouge 2|A=2.*B=1", re.I
)

# ---------------------------------------------------------------------------
# Forbidden cross-contamination patterns (answer ↔ method)
# ---------------------------------------------------------------------------
FORBIDDEN: list[tuple[re.Pattern[str], re.Pattern[str], str]] = [
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

# cas-limite mismatches
CASLIMITE_GLOUTON = re.compile(r"pièce 1 absente|glouton.*échouer", re.I)
CASLIMITE_KNN = re.compile(r"égalité de vote|k pair", re.I)

CASLIMITE_FORBIDDEN: list[tuple[re.Pattern[str], re.Pattern[str], str]] = [
    (METHOD_GLOUTON, CASLIMITE_KNN, "cas-limite k-NN sous consigne glouton"),
    (METHOD_GLOUTON, re.compile(r"cible absente(?!.*variant)", re.I),
     "cas-limite dichotomie sous consigne glouton"),
    (METHOD_KNN, CASLIMITE_GLOUTON, "cas-limite glouton sous consigne k-NN"),
    (METHOD_KNN, re.compile(r"cible absente(?!.*variant)", re.I),
     "cas-limite dichotomie sous consigne k-NN"),
    (METHOD_DICHOTOMIE, CASLIMITE_GLOUTON,
     "cas-limite glouton sous consigne dichotomie"),
    (METHOD_DICHOTOMIE, CASLIMITE_KNN,
     "cas-limite k-NN sous consigne dichotomie"),
    (METHOD_VARIANT, CASLIMITE_GLOUTON,
     "cas-limite glouton sous consigne variant"),
    (METHOD_VARIANT, CASLIMITE_KNN,
     "cas-limite k-NN sous consigne variant"),
]

# ---------------------------------------------------------------------------
# Capacity → allowed methods mapping (autorite: programme_nsi_2019.yaml)
# P-ALGO-03 = k-NN seul
# P-ALGO-04 = recherche dichotomique (recherche + variant de terminaison)
# P-ALGO-05 = algorithmes gloutons
# ---------------------------------------------------------------------------
CAPACITY_METHODS: dict[str, list[str]] = {
    "P-ALGO-03": ["knn"],
    "P-ALGO-04": ["dichotomie", "variant"],
    "P-ALGO-05": ["glouton"],
}

# Positional answer expectations for version_amenagee "Réponses rapides"
CAPACITY_ANSWER_FINGERPRINTS: dict[str, re.Pattern[str]] = {
    "P-ALGO-04": ANSWER_DICHOTOMIE,  # position 1 = dichotomie-recherche
    "P-ALGO-03": ANSWER_KNN,         # k-NN is P-ALGO-03 now (not dichotomie)
    "P-ALGO-05": ANSWER_GLOUTON,
}

# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------
EXERCISE_HEADER_RE = re.compile(
    r"^#{2,3}\s+(?:Exercice|Corrigé exercice)\s+(\d+)\s*$", re.M
)

# Matches both exercise headers and section headers (## / ###)
SECTION_HEADER_RE = re.compile(r"^#{2,3}\s+", re.M)


def parse_blocks(text: str) -> list[dict[str, str]]:
    """Split a markdown document into exercise/corrige blocks.

    Delimits each block at the NEXT heading of same or higher level.
    """
    headers = list(EXERCISE_HEADER_RE.finditer(text))
    blocks: list[dict[str, str]] = []
    for i, m in enumerate(headers):
        # Find next heading (any ## or ###) after this one
        rest = text[m.end():]
        next_heading = SECTION_HEADER_RE.search(rest)
        if next_heading:
            end = m.end() + next_heading.start()
        else:
            end = len(text)
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
    """Identify the method from a consigne/method line."""
    if METHOD_DICHOTOMIE.search(text):
        return "dichotomie"
    if METHOD_VARIANT.search(text):
        return "variant"
    if METHOD_GLOUTON.search(text):
        return "glouton"
    if METHOD_KNN.search(text):
        return "knn"
    return None


# ---------------------------------------------------------------------------
# Block-level checks
# ---------------------------------------------------------------------------
def check_exercise_block(block: dict[str, str], filename: str) -> list[str]:
    """Check exercise block: answer↔method and method↔capacity."""
    errors: list[str] = []
    text = block["text"]
    title = block["title"]

    # Find method from consigne
    consigne_match = re.search(r"Consigne\s*:\s*(.+?)(?:\n|$)", text)
    method_line = consigne_match.group(1) if consigne_match else text
    method = detect_method(method_line)

    if method is None:
        return errors

    # --- method↔capacity ---
    cap_match = re.search(r"Capacité officielle\s*:\s*(P-ALGO-\d+)", text)
    if cap_match:
        cap_id = cap_match.group(1)
        allowed = CAPACITY_METHODS.get(cap_id, [])
        if allowed and method not in allowed:
            errors.append(
                f"{filename} {title}: methode '{method}' incompatible avec "
                f"capacite {cap_id} (attendu: {'/'.join(allowed)})"
            )

    # --- answer↔method ---
    answer_match = re.search(
        r"(?:Réponse attendue|Résultat attendu)\s*:\s*(.+?)(?:\n|$)", text
    )
    if answer_match:
        answer = answer_match.group(1)
        for method_re, forbidden_re, desc in FORBIDDEN:
            if method_re.search(method_line) and forbidden_re.search(answer):
                errors.append(f"{filename} {title}: {desc}")

    # --- cas-limite coherence ---
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
    """Check corrige block: method↔capacity via Capacité mobilisée.

    Applies to both '### Corrigé exercice N' and '### Exercice N' blocks
    in the corrigé autonome (P1-5).
    """
    errors: list[str] = []
    text = block["text"]
    title = block["title"]

    cap_match = re.search(r"Capacité mobilisée\s*:\s*(P-ALGO-\d+)", text)
    if not cap_match:
        return errors
    cap_id = cap_match.group(1)

    # Try Justification task first, then Méthode line
    task_match = re.search(r"la tâche\s*`([^`]+)`", text)
    method_match = re.search(r"Méthode\s*:\s*(.+?)(?:\n|$)", text)
    method_text = (
        task_match.group(1) if task_match
        else method_match.group(1) if method_match
        else ""
    )
    method = detect_method(method_text)
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
    """Check eval question for cible 40 absente contamination.

    Contextualised: only flag if the question does not mention dichotomie.
    """
    errors: list[str] = []
    text = q["text"]
    if CIBLE_40_RE.search(text):
        if not METHOD_DICHOTOMIE.search(text):
            errors.append(
                f"{filename} {q['title']}: 'cible 40 absente' dans corrige eval"
            )
    return errors


def check_positional_answers(
    text: str, filename: str, capacities: list[str],
) -> list[str]:
    """Check 'Reponses rapides' answers belong to contract capacities.

    Version amenagee follows pedagogical order, not contract order,
    so we verify each answer's method belongs to at least one capacity
    in the contract and detect cross-contamination between adjacent answers.
    """
    errors: list[str] = []
    m = re.search(r"##\s+Réponses rapides", text)
    if not m:
        return errors

    section = text[m.start():]
    answers: list[str] = re.findall(
        r"^-\s+Réponse\s+\d+\s*:\s*(.+)$", section, re.M,
    )

    # Collect all allowed methods from contract capacities
    allowed_methods: set[str] = set()
    for cap_id in capacities:
        for method in CAPACITY_METHODS.get(cap_id, []):
            allowed_methods.add(method)

    # Build fingerprint→method map
    fp_to_method: list[tuple[re.Pattern[str], str]] = [
        (ANSWER_DICHOTOMIE, "dichotomie"),
        (ANSWER_VARIANT, "variant"),
        (ANSWER_GLOUTON, "glouton"),
        (ANSWER_KNN, "knn"),
    ]

    seen_methods: list[str] = []
    for idx, answer in enumerate(answers):
        detected = None
        for fp, method_name in fp_to_method:
            if fp.search(answer):
                detected = method_name
                break
        if detected and detected not in allowed_methods:
            errors.append(
                f"{filename} Réponse {idx + 1}: methode '{detected}' "
                f"absente des capacites du contrat"
            )
        if detected:
            seen_methods.append(detected)

    # Detect duplicate adjacent methods that should be different
    for i in range(len(seen_methods) - 1):
        if seen_methods[i] == seen_methods[i + 1]:
            errors.append(
                f"{filename} Réponses {i + 1}/{i + 2}: "
                f"methode '{seen_methods[i]}' dupliquee"
            )

    return errors


# ---------------------------------------------------------------------------
# File-level check
# ---------------------------------------------------------------------------
def check_file(
    filepath: Path, capacities: list[str] | None = None,
) -> list[str]:
    """Check all blocks in a file."""
    if not filepath.exists():
        return []
    text = filepath.read_text(encoding="utf-8", errors="replace")
    filename = filepath.name
    errors: list[str] = []

    blocks = parse_blocks(text)
    for block in blocks:
        # Corrige block: has "Capacité mobilisée"
        if "Capacité mobilisée" in block["text"]:
            errors.extend(check_corrige_block(block, filename))
        # Exercise block: has "Capacité officielle" or "Consigne"
        if "Capacité officielle" in block["text"] or "Consigne" in block["text"]:
            errors.extend(check_exercise_block(block, filename))

    if "corrige" in filename.lower():
        for q in parse_eval_questions(text):
            errors.extend(check_eval_question(q, filename))

    if "version_amenagee" in filename.lower() and capacities:
        errors.extend(check_positional_answers(text, filename, capacities))

    # Global cible 40 absente check (independent of answer_match)
    if CIBLE_40_RE.search(text):
        errors.append(f"{filename}: contient 'cible 40 absente'")

    return errors


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------
def discover_sequences() -> list[tuple[str, str, list[str]]]:
    """Discover sequences from contracts that have P-ALGO capacities."""
    results: list[tuple[str, str, list[str]]] = []
    if not CONTRACTS_DIR.exists():
        return results
    for contract_path in sorted(CONTRACTS_DIR.glob("*_contract.yml")):
        data = yaml.safe_load(contract_path.read_text(encoding="utf-8"))
        if not data:
            continue
        caps = data.get("capacites_officielles", [])
        algo_caps = [c for c in caps if c in CAPACITY_METHODS]
        if algo_caps:
            seq_id = data.get("sequence", "")
            level = data.get("level", "")
            results.append((seq_id, level, caps))
    return results


def find_support_files(seq_id: str, level: str) -> list[Path]:
    """Find all support files for a sequence."""
    seq_dir = SUPPORTS_DIR / level / seq_id
    if not seq_dir.exists():
        return []
    return sorted(seq_dir.glob(f"{seq_id}_*.md"))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    all_errors: list[str] = []

    sequences = discover_sequences()
    if not sequences:
        p13_dir = SUPPORTS_DIR / "premiere" / "P13"
        for f in sorted(p13_dir.glob("P13_*.md")):
            all_errors.extend(check_file(f))
    else:
        for seq_id, level, capacities in sequences:
            for filepath in find_support_files(seq_id, level):
                all_errors.extend(check_file(filepath, capacities))

    if all_errors:
        print(f"FAIL  check_answer_capacity_coherence: {len(all_errors)} erreur(s)")
        for e in all_errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("OK  check_answer_capacity_coherence: coherence reponse/capacite verifiee")


if __name__ == "__main__":
    main()
