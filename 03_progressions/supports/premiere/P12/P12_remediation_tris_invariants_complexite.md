---
title: "P12 - remediation - tris, invariants et complexité"
level: "premiere"
sequence_id: "P12"
document_type: "remediation"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "tris, invariants et complexité"
notion: "tris, invariants et complexité"
private_data: false
official_program:
  capacities:
    - "P-ALGO-02A"
    - "P-ALGO-02B"
    - "P-ALGO-02C"
    - "P-ALGO-02D"
---

# P12 - Remédiation - tris, invariants et complexité

## Diagnostic
- invariant confondu avec résultat.
- décalage oublié.
- coût linéaire annoncé.

## Activités correctives
1. Annoter `temps=[42,17,23,17,9]`.
2. Refaire la tâche `insérer la clé dans la partie gauche triée` et comparer avec `insertion après i=1 -> [17,42,23,17,9]`.
3. Traiter le cas limite `liste vide`.
4. Relier la réponse à P-ALGO-02A.

## Critères de sortie
- Donnée exacte.
- Résultat final explicite.
- Cas limite décidé.
