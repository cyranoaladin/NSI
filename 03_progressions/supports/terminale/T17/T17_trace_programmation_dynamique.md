---
title: "T17 - trace - programmation dynamique"
level: "terminale"
sequence_id: "T17"
document_type: "trace"
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

# T17 - Trace - programmation dynamique

## Trace courte
- Donnée : `pieces=[1,5,7], montant=11, dp[0]=0`.
- Vocabulaire : état, récurrence, initialisation, mémoïsation, tabulation.
- Étape 1 : définir dp[m] coût minimal.
- Étape 2 : écrire dp[m]=1+min(dp[m-p]).
- Résultat de référence : dp[6]=2 avec 5+1.

## Cas limites à mémoriser
- montant 0.
- montant impossible.
- pièce plus grande que m.

## Erreurs fréquentes
- état ambigu.
- initialisation oubliée.
- choix de pièce confondu avec valeur optimale.

## Critères de réussite observables
- Capacité : T-ALGO-04.
- Résultat final : dp[11]=3 avec 5+5+1.
- Cas limite : montant 0.
