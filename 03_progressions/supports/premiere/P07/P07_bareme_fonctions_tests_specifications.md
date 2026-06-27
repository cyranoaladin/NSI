---
title: "P07 - Barème - fonctions, contrats, assertions et tests"
level: "premiere"
sequence_id: "P07"
document_type: "bareme"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Langage Python"
notion: "fonctions, contrats, assertions et tests"
objectifs:
  - "identifier la donnée de référence"
  - "appliquer la méthode disciplinaire"
  - "produire un résultat vérifiable"
  - "contrôler un cas limite"
private_data: false
official_program:
  capacities:
    - "P-LANG-01"
    - "P-LANG-02"
    - "P-LANG-03A"
    - "P-LANG-03B"
    - "P-LANG-03C"
    - "P-LANG-04"
    - "P-LANG-05"
---

# P07 - Barème - fonctions, contrats, assertions et tests

## Barème question par question
- Question 1 : 2 points pour la donnée exacte `prix_ttc(80, 0.20) -> 96.0 ; prix_ttc(0, 0.20) -> 0.0 ; prix_ttc(-5, 0.20) lève AssertionError`.
- Question 2 : 3 points pour la méthode `écrire une signature explicite avec return`.
- Question 3 : 3 points pour le résultat `fonction prix_ttc(ht, taux) retourne round(ht * (1 + taux), 2), refuse ht négatif et garde le cas ht=0`.
- Question 4 : 2 points pour un cas limite cohérent.

## Critères observables
- Les capacités évaluées sont : P-LANG-01, P-LANG-02, P-LANG-03A, P-LANG-03B, P-LANG-03C, P-LANG-04, P-LANG-05.
- Le résultat doit être écrit sous une forme vérifiable, pas seulement commenté.
