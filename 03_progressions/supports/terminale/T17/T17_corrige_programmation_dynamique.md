---
title: "T17 - corrige - programmation dynamique"
level: "terminale"
sequence_id: "T17"
document_type: "corrige"
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

# T17 - Corrigé - programmation dynamique

## Corrigé du TD
### Exercice 1
- Réponse attendue : dp[6]=2 avec 5+1.
- Méthode : définir dp[m] coût minimal.
- Cas limite : montant 0.
### Exercice 2
- Réponse attendue : dp[11]=3 avec 5+5+1.
- Méthode : écrire dp[m]=1+min(dp[m-p]).
- Cas limite : montant impossible.
### Exercice 3
- Réponse attendue : tabulation stocke chaque dp[m].
- Méthode : initialiser dp[0]=0.
- Cas limite : pièce plus grande que m.
### Exercice 4
- Réponse attendue : sans pièce 1 certains montants impossibles.
- Méthode : remplir la table de 1 à 11.
- Cas limite : montant 0.
### Exercice 5
- Réponse attendue : dp[6]=2 avec 5+1.
- Méthode : définir dp[m] coût minimal.
- Cas limite : montant impossible.
### Exercice 6
- Réponse attendue : dp[11]=3 avec 5+5+1.
- Méthode : écrire dp[m]=1+min(dp[m-p]).
- Cas limite : pièce plus grande que m.
### Exercice 7
- Réponse attendue : tabulation stocke chaque dp[m].
- Méthode : initialiser dp[0]=0.
- Cas limite : montant 0.
### Exercice 8
- Réponse attendue : sans pièce 1 certains montants impossibles.
- Méthode : remplir la table de 1 à 11.
- Cas limite : montant impossible.

## Corrigé du TP
- Donnée : `pieces=[1,5,7], montant=11, dp[0]=0`.
- Résultat principal : dp[6]=2 avec 5+1.
- Résultat secondaire : dp[11]=3 avec 5+5+1.

## Corrigé de l évaluation
- Question 1 : dp[6]=2 avec 5+1.
- Question 2 : dp[11]=3 avec 5+5+1.
- Question 3 : tabulation stocke chaque dp[m].
- Question 4 : sans pièce 1 certains montants impossibles.
