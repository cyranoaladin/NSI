#!/usr/bin/env python3
"""Guard: verifie la coherence reponse/capacite/methode dans les supports P13.

Scanne toutes les sequences via leurs contrats et verifie dans CHAQUE
support (TD, corrige, tp, trace, version_amenagee, evaluation, bareme,
remediation, cours) :
1. reponse↔methode : la reponse attendue est coherente avec la methode
2. methode↔capacite : la methode de la consigne correspond a la capacite
3. les reponses positionnelles (version_amenagee) suivent l'ordre capacite

Parseurs etendus :
- TD/corrige : "Capacite officielle" / "Capacite mobilisee" + consigne/methode
- cours : "Controle : capacite P-ALGO-xx"
- trace : "Capacite P-ALGO-xx (...) : <reponse>" (multi-motif)
- evaluation/bareme : "### Question N" + "Capacite officielle" ou "P-ALGO-xx"
- remediation : "Relier ... P-ALGO-xx"

Mapping autorite (programme_nsi_2019.yaml) :
  P-ALGO-03 = k-NN seul
  P-ALGO-04 = recherche dichotomique (recherche + variant)
  P-ALGO-05 = algorithmes gloutons

Fail-closed PAR TYPE : chaque suffixe attendu doit exister.

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
# Method signatures
# ---------------------------------------------------------------------------
METHOD_DICHOTOMIE = re.compile(
    r"calculer milieu|réduire intervalle|recherche dichotomique", re.I
)
METHOD_VARIANT = re.compile(
    r"droite.gauche diminue|droite.gauche décroît"
    r"|variant.*boucle|terminaison.*dichotom"
    r"|variant.*erroné|variant.*corriger"
    r"|variant.*décroît", re.I
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
    r"variant.*décroît|droite.gauche décroît|décroît de \d+ à \d+"
    r"|décroît.*terminaison|terminaison prouvée|terminaison \(cible", re.I
)
ANSWER_GLOUTON = re.compile(
    r"10\s*\+\s*10\s*\+\s*5\s*\+\s*2\s*\+\s*1|28\s*=\s*10|5 pièces", re.I
)
ANSWER_KNN = re.compile(
    r"rouge.*voix.*bleu|classe rouge|vote.*rouge|rouge 2|A=2.*B=1", re.I
)

# Forbidden cross-contamination patterns (answer ↔ method)
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

# cas-limite mismatches (cubic #1 P2: ajout CASLIMITE_DICHOTOMIE)
CASLIMITE_DICHOTOMIE = re.compile(r"cible absente", re.I)
CASLIMITE_GLOUTON = re.compile(r"pièce 1 absente|glouton.*échouer", re.I)
CASLIMITE_KNN = re.compile(r"égalité de vote|k pair", re.I)
CASLIMITE_FORBIDDEN: list[tuple[re.Pattern[str], re.Pattern[str], str]] = [
    (METHOD_GLOUTON, CASLIMITE_KNN, "cas-limite k-NN sous consigne glouton"),
    (METHOD_GLOUTON, CASLIMITE_DICHOTOMIE, "cas-limite dichotomie sous consigne glouton"),
    (METHOD_KNN, CASLIMITE_GLOUTON, "cas-limite glouton sous consigne k-NN"),
    (METHOD_KNN, CASLIMITE_DICHOTOMIE, "cas-limite dichotomie sous consigne k-NN"),
    (METHOD_DICHOTOMIE, CASLIMITE_GLOUTON, "cas-limite glouton sous consigne dichotomie"),
    (METHOD_DICHOTOMIE, CASLIMITE_KNN, "cas-limite k-NN sous consigne dichotomie"),
    (METHOD_VARIANT, CASLIMITE_GLOUTON, "cas-limite glouton sous consigne variant"),
    (METHOD_VARIANT, CASLIMITE_KNN, "cas-limite k-NN sous consigne variant"),
]

# Capacity → allowed methods (autorite: programme_nsi_2019.yaml)
CAPACITY_METHODS: dict[str, list[str]] = {
    "P-ALGO-03": ["knn"],
    "P-ALGO-04": ["dichotomie", "variant"],
    "P-ALGO-05": ["glouton"],
}

# cubic #2 P1: P-ALGO-04 doit couvrir dichotomie ET variant
CAPACITY_ANSWER_FINGERPRINTS: dict[str, re.Pattern[str]] = {
    "P-ALGO-04": re.compile(
        f"{ANSWER_DICHOTOMIE.pattern}|{ANSWER_VARIANT.pattern}", re.I
    ),
    "P-ALGO-03": ANSWER_KNN,
    "P-ALGO-05": ANSWER_GLOUTON,
}

# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------
EXERCISE_HEADER_RE = re.compile(
    r"^#{2,3}\s+(?:Exercice|Corrigé exercice)\s+(\d+)\s*$", re.M
)
QUESTION_HEADER_RE = re.compile(
    r"^#{2,3}\s+(?:Question|Corrigé question)\s+(\d+)\s*$", re.M
)
SECTION_HEADER_RE = re.compile(r"^#{2,3}\s+", re.M)
EXAMPLE_HEADER_RE = re.compile(
    r"^###\s+Exemple corrigé\s+(\d+)", re.M
)


def _split_at_headers(
    text: str, header_re: re.Pattern[str],
) -> list[dict[str, str]]:
    headers = list(header_re.finditer(text))
    blocks: list[dict[str, str]] = []
    for i, m in enumerate(headers):
        rest = text[m.end():]
        nxt = SECTION_HEADER_RE.search(rest)
        end = m.end() + nxt.start() if nxt else len(text)
        blocks.append({
            "title": m.group(0).strip(),
            "num": m.group(1),
            "text": text[m.start():end],
        })
    return blocks


def detect_method(text: str) -> str | None:
    if METHOD_DICHOTOMIE.search(text):
        return "dichotomie"
    if METHOD_VARIANT.search(text):
        return "variant"
    if METHOD_GLOUTON.search(text):
        return "glouton"
    if METHOD_KNN.search(text):
        return "knn"
    return None


def _extract_cap(text: str) -> str | None:
    for pat in [
        r"Capacité officielle\s*:\s*(P-ALGO-0[345])",
        r"Capacité mobilisée\s*:\s*(P-ALGO-0[345])",
        r"capacité\s+(P-ALGO-0[345])",
        r"Capacité\s*:\s*(P-ALGO-0[345])",
        r"sur\s+(P-ALGO-0[345])",
        r"à\s+(P-ALGO-0[345])",
    ]:
        m = re.search(pat, text)
        if m:
            return m.group(1)
    return None


def _extract_method_text(text: str) -> str:
    for pat in [
        r"Consigne\s*:\s*(.+?)(?:\n|$)",
        r"Méthode\s*:\s*(.+?)(?:\n|$)",
        r"la tâche\s*`([^`]+)`",
        r"Énoncé\s*:\s*.+?,\s*(.+?)(?:\n|$)",
        r"Critère spécifique\s*:\s*(.+?)(?:\n|$)",
    ]:
        m = re.search(pat, text)
        if m:
            return m.group(1)
    return text


def _extract_answer(text: str) -> str | None:
    m = re.search(
        r"(?:Réponse attendue|Résultat attendu|Résultat final"
        r"|Résultat de référence|résultat)"
        r"\s*[:=]\s*(.+?)(?:\n|$)", text, re.I
    )
    return m.group(1) if m else None


# ---------------------------------------------------------------------------
# Check a generic capacity-bearing block
# ---------------------------------------------------------------------------
def check_cap_block(
    text: str, title: str, filename: str,
) -> list[str]:
    errors: list[str] = []
    cap_id = _extract_cap(text)
    if not cap_id:
        return errors
    allowed = CAPACITY_METHODS.get(cap_id, [])
    if not allowed:
        return errors

    method_text = _extract_method_text(text)
    method = detect_method(method_text)
    if method is None:
        return errors

    # method↔capacity
    if method not in allowed:
        errors.append(
            f"{filename} {title}: methode '{method}' incompatible avec "
            f"capacite {cap_id} (attendu: {'/'.join(allowed)})"
        )

    # answer↔method
    answer = _extract_answer(text)
    if answer:
        for method_re, forbidden_re, desc in FORBIDDEN:
            if method_re.search(method_text) and forbidden_re.search(answer):
                errors.append(f"{filename} {title}: {desc}")

    # cas-limite
    cl_match = re.search(r"traiter aussi\s*`([^`]+)`", text)
    cr_match = re.search(r"décision sur\s*`([^`]+)`", text)
    cl_text = ""
    if cl_match:
        cl_text += cl_match.group(1) + " "
    if cr_match:
        cl_text += cr_match.group(1)
    if cl_text:
        for method_re, forbidden_re, desc in CASLIMITE_FORBIDDEN:
            if method_re.search(method_text) and forbidden_re.search(cl_text):
                errors.append(f"{filename} {title}: {desc}")

    return errors


# ---------------------------------------------------------------------------
# Cours: "Contrôle : capacité P-ALGO-xx"
# ---------------------------------------------------------------------------
def check_cours(text: str, filename: str) -> list[str]:
    errors: list[str] = []
    for block in _split_at_headers(text, EXAMPLE_HEADER_RE):
        errors.extend(check_cap_block(block["text"], block["title"], filename))
    return errors


# ---------------------------------------------------------------------------
# Trace: multi-line and single-line capacity criteria
# ---------------------------------------------------------------------------
def check_trace(text: str, filename: str) -> list[str]:
    """Parse trace criteria — handles both single-line and multi-line formats.

    Single-line: "- Capacité P-ALGO-04 (dichotomie) : milieux 18 …"
    Multi-line:  "- Capacité : P-ALGO-03." followed by "- Résultat final : 28→…"
    """
    errors: list[str] = []
    lines = text.splitlines()

    # Single-line format: "- Capacité P-ALGO-xx (…) : <answer>"
    for line in lines:
        m = re.match(
            r"^-\s+Capacité\s+(P-ALGO-0[345])\s*\([^)]*\)\s*:\s*(.+)$", line
        )
        if m:
            cap_id, answer = m.group(1), m.group(2)
            _check_answer_vs_cap(cap_id, answer, filename, "Critère", errors)

    # Multi-line format: "- Capacité : P-ALGO-xx." then "- Résultat final : …"
    for i, line in enumerate(lines):
        m = re.match(r"^-\s+Capacité\s*:\s*(P-ALGO-0[345])\b", line)
        if not m:
            continue
        cap_id = m.group(1)
        # Look at next line(s) for a result
        for j in range(i + 1, min(i + 3, len(lines))):
            ans = _extract_answer(lines[j])
            if ans:
                _check_answer_vs_cap(cap_id, ans, filename, "Critère", errors)
                break

    return errors


def _check_answer_vs_cap(
    cap_id: str, answer: str, filename: str, label: str,
    errors: list[str],
) -> None:
    """Flag if an answer fingerprint belongs to a DIFFERENT capacity."""
    for other_cap, fp in CAPACITY_ANSWER_FINGERPRINTS.items():
        if other_cap != cap_id and fp.search(answer):
            errors.append(
                f"{filename} {label} {cap_id}: reponse {other_cap} "
                f"sous capacite {cap_id}"
            )


# ---------------------------------------------------------------------------
# Evaluation / Bareme: "### Question N" blocks + inline barème lines
# ---------------------------------------------------------------------------
def check_questions(text: str, filename: str) -> list[str]:
    errors: list[str] = []
    # Structured question blocks
    for block in _split_at_headers(text, QUESTION_HEADER_RE):
        errors.extend(check_cap_block(block["text"], block["title"], filename))

    # Inline barème lines: "- Question N : … sur P-ALGO-xx avec résultat `…`"
    for line in text.splitlines():
        m = re.match(
            r"^-\s+Question\s+(\d+)\s*:\s*.*?"
            r"(?:sur|P-ALGO)\s*(P-ALGO-0[345])\b.*?"
            r"(?:résultat|avec)\s*[`«]?(.+?)[`»]?\s*$",
            line, re.I,
        )
        if not m:
            continue
        q_num, cap_id, answer = m.group(1), m.group(2), m.group(3)
        _check_answer_vs_cap(
            cap_id, answer, filename, f"Barème Q{q_num}", errors
        )

    return errors


# ---------------------------------------------------------------------------
# Remediation: "Relier ... P-ALGO-xx"
# ---------------------------------------------------------------------------
def check_remediation(text: str, filename: str) -> list[str]:
    errors: list[str] = []
    for line in text.splitlines():
        m = re.search(r"Relier.*à\s+(P-ALGO-0[345])", line)
        if not m:
            continue
        cap_id = m.group(1)
        method = detect_method(line)
        if method is None:
            continue
        allowed = CAPACITY_METHODS.get(cap_id, [])
        if allowed and method not in allowed:
            errors.append(
                f"{filename}: 'Relier' methode '{method}' → {cap_id} "
                f"(attendu: {'/'.join(allowed)})"
            )
    return errors


# ---------------------------------------------------------------------------
# TP: "### Corrigé question N" blocks
# ---------------------------------------------------------------------------
TP_QUESTION_HEADER_RE = re.compile(
    r"^###\s+Corrigé question\s+(\d+)\s*$", re.M
)


def check_tp(text: str, filename: str) -> list[str]:
    """Check TP corrigé questions for answer↔method cross-contamination.

    Cross-references "Travail demandé" items (which carry the method)
    with "Corrigé question N" blocks (which carry the answer).
    """
    errors: list[str] = []

    # Extract work items from "Travail demandé"
    work_methods: dict[int, str | None] = {}
    travail_match = re.search(r"##\s+Travail demandé\s*\n((?:\d+\.\s+.+\n?)+)", text)
    if travail_match:
        for item_m in re.finditer(r"(\d+)\.\s+(.+)", travail_match.group(1)):
            idx = int(item_m.group(1))
            work_methods[idx] = detect_method(item_m.group(2))

    # Extract raw work item text for method regex matching
    work_texts: dict[int, str] = {}
    if travail_match:
        for item_m in re.finditer(r"(\d+)\.\s+(.+)", travail_match.group(1)):
            work_texts[int(item_m.group(1))] = item_m.group(2)

    # Check each corrigé question
    for block in _split_at_headers(text, TP_QUESTION_HEADER_RE):
        q_num = int(block["num"])
        answer = _extract_answer(block["text"])
        if not answer:
            continue
        method = work_methods.get(q_num)
        method_text_raw = work_texts.get(q_num, "")
        if method is None:
            continue
        # Check answer↔method using the raw work item text
        for method_re, forbidden_re, desc in FORBIDDEN:
            if method_re.search(method_text_raw) and forbidden_re.search(answer):
                errors.append(f"{filename} {block['title']}: {desc}")
    return errors


# ---------------------------------------------------------------------------
# Version amenagee: positional answers
# ---------------------------------------------------------------------------
def check_positional_answers(
    text: str, filename: str, capacities: list[str],
) -> list[str]:
    errors: list[str] = []
    m = re.search(r"##\s+Réponses rapides", text)
    if not m:
        return errors
    section = text[m.start():]
    answers: list[str] = re.findall(
        r"^-\s+Réponse\s+\d+\s*(?:\([^)]*\))?\s*:\s*(.+)$", section, re.M,
    )
    allowed_methods: set[str] = set()
    for cap_id in capacities:
        for mth in CAPACITY_METHODS.get(cap_id, []):
            allowed_methods.add(mth)
    fp_to_method: list[tuple[re.Pattern[str], str]] = [
        (ANSWER_DICHOTOMIE, "dichotomie"),
        (ANSWER_VARIANT, "variant"),
        (ANSWER_GLOUTON, "glouton"),
        (ANSWER_KNN, "knn"),
    ]
    for idx, answer in enumerate(answers):
        for fp, method_name in fp_to_method:
            if fp.search(answer) and method_name not in allowed_methods:
                errors.append(
                    f"{filename} Réponse {idx + 1}: methode '{method_name}' "
                    f"absente des capacites du contrat"
                )
    return errors


# ---------------------------------------------------------------------------
# File-level orchestration
# ---------------------------------------------------------------------------
EXPECTED_SUFFIXES = [
    "TD", "corrige", "tp", "trace", "version_amenagee",
    "evaluation", "bareme", "remediation", "cours",
]


def check_file(
    filepath: Path, capacities: list[str] | None = None,
) -> list[str]:
    if not filepath.exists():
        return []
    text = filepath.read_text(encoding="utf-8", errors="replace")
    filename = filepath.name
    fn_lower = filename.lower()
    errors: list[str] = []

    # Exercise/Corrigé blocks (TD, corrige)
    for block in _split_at_headers(text, EXERCISE_HEADER_RE):
        errors.extend(check_cap_block(block["text"], block["title"], filename))

    if "cours" in fn_lower:
        errors.extend(check_cours(text, filename))

    if "trace" in fn_lower:
        errors.extend(check_trace(text, filename))

    if "evaluation" in fn_lower or "bareme" in fn_lower:
        errors.extend(check_questions(text, filename))

    if "remediation" in fn_lower:
        errors.extend(check_remediation(text, filename))

    if "_tp_" in fn_lower or fn_lower.startswith("p13_tp"):
        errors.extend(check_tp(text, filename))

    if "version_amenagee" in fn_lower and capacities:
        errors.extend(check_positional_answers(text, filename, capacities))

    return errors


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------
def discover_sequences() -> list[tuple[str, str, list[str]]]:
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
            results.append((seq_id, level, algo_caps))
    return results


def find_support_files(seq_id: str, level: str) -> list[Path]:
    seq_dir = SUPPORTS_DIR / level / seq_id
    if not seq_dir.exists():
        return []
    return sorted(seq_dir.glob(f"{seq_id}_*.md"))


def _check_expected_files(
    seq_id: str, level: str, files: list[Path],
) -> list[str]:
    """cubic #3 P2: fail-closed par type — chaque suffixe attendu doit exister."""
    errors: list[str] = []
    found_suffixes: set[str] = set()
    seq_prefix = seq_id.lower() + "_"
    for f in files:
        name = f.stem.lower()  # e.g. p13_td_dichotomie_glouton_knn
        if not name.startswith(seq_prefix):
            continue
        rest = name[len(seq_prefix):]  # e.g. td_dichotomie_glouton_knn
        # Match compound suffixes first (version_amenagee, tp_papier)
        for suffix in EXPECTED_SUFFIXES:
            if rest.startswith(suffix.lower()):
                found_suffixes.add(suffix.lower())
                break
        else:
            # Fallback: first segment
            first = rest.split("_", 1)[0]
            found_suffixes.add(first)
    for suffix in EXPECTED_SUFFIXES:
        if suffix.lower() not in found_suffixes:
            errors.append(
                f"{seq_id}: support '{suffix}' absent "
                f"({SUPPORTS_DIR / level / seq_id})"
            )
    return errors


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
            files = find_support_files(seq_id, level)
            if not files:
                all_errors.append(
                    f"{seq_id}: aucun fichier support trouve dans "
                    f"{SUPPORTS_DIR / level / seq_id}"
                )
                continue
            # cubic #3: fail-closed par type
            all_errors.extend(_check_expected_files(seq_id, level, files))
            for filepath in files:
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
