---
title: "T17 - remediation - programmation dynamique"
level: "terminale"
sequence_id: "T17"
document_type: "remediation"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "programmation dynamique"
notion: "programmation dynamique"
private_data: false
official_program:
  capacities:
    - "T-ALGO-04"
---

# T17 - Remédiation - programmation dynamique

## Diagnostic
- état ambigu.
- initialisation oubliée.
- choix de pièce confondu avec valeur optimale.

## Activités correctives
1. Annoter `pieces=[1,5,7], montant=11, dp[0]=0`.
2. Refaire la tâche `définir dp[m] coût minimal` et comparer avec `dp[6]=2 avec 5+1`.
3. Traiter le cas limite `montant 0`.
4. Relier la réponse à T-ALGO-04.

## Critères de sortie
- Donnée exacte.
- Résultat final explicite.
- Cas limite décidé.
