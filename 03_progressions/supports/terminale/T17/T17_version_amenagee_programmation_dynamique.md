---
title: "T17 - version_amenagee - programmation dynamique"
level: "terminale"
sequence_id: "T17"
document_type: "version_amenagee"
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

# T17 - Version aménagée - programmation dynamique

## Aides intégrées
- Donnée fournie : `pieces=[1,5,7], montant=11, dp[0]=0`.
- Mots utiles : état, récurrence, initialisation, mémoïsation, tabulation.
- Méthode guidée : définir dp[m] coût minimal puis écrire dp[m]=1+min(dp[m-p]).

## Exercice guidé
1. Recopier la donnée utile.
2. Choisir la capacité : T-ALGO-04 ou T-ALGO-04.
3. Compléter le résultat : dp[6]=2 avec 5+1.
4. Cocher le cas limite : montant 0.

## Réponses rapides
- Réponse 1 : dp[6]=2 avec 5+1.
- Réponse 2 : dp[11]=3 avec 5+5+1.
- Réponse 3 : tabulation stocke chaque dp[m].
