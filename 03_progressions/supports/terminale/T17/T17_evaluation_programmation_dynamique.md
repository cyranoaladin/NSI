---
title: "T17 - evaluation - programmation dynamique"
level: "terminale"
sequence_id: "T17"
document_type: "evaluation"
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

# T17 - Évaluation - programmation dynamique

## Modalités
- Durée : 30 minutes.
- Matériel autorisé : fiche de cours.
- Capacités évaluées : T-ALGO-04.

## Questions
### Question 1
- Capacité officielle : T-ALGO-04.
- Énoncé : à partir de `pieces=[1,5,7], montant=11, dp[0]=0`, définir dp[m] coût minimal.
- Réponse attendue : dp[6]=2 avec 5+1.
- Barème : 1 point donnée, 1 point méthode, 1 point résultat, 1 point justification sur `montant 0`.
### Question 2
- Capacité officielle : T-ALGO-04.
- Énoncé : à partir de `pieces=[1,5,7], montant=11, dp[0]=0`, écrire dp[m]=1+min(dp[m-p]).
- Réponse attendue : dp[11]=3 avec 5+5+1.
- Barème : 1 point donnée, 1 point méthode, 1 point résultat, 1 point justification sur `montant impossible`.
### Question 3
- Capacité officielle : T-ALGO-04.
- Énoncé : à partir de `pieces=[1,5,7], montant=11, dp[0]=0`, initialiser dp[0]=0.
- Réponse attendue : tabulation stocke chaque dp[m].
- Barème : 1 point donnée, 1 point méthode, 1 point résultat, 1 point justification sur `pièce plus grande que m`.
### Question 4
- Capacité officielle : T-ALGO-04.
- Énoncé : à partir de `pieces=[1,5,7], montant=11, dp[0]=0`, remplir la table de 1 à 11.
- Réponse attendue : sans pièce 1 certains montants impossibles.
- Barème : 1 point donnée, 1 point méthode, 1 point résultat, 1 point justification sur `montant 0`.

## Corrigé question par question
### Corrigé question 1
- Résultat attendu : dp[6]=2 avec 5+1.
- Critère spécifique : définir dp[m] coût minimal et éviter `état ambigu`.
### Corrigé question 2
- Résultat attendu : dp[11]=3 avec 5+5+1.
- Critère spécifique : écrire dp[m]=1+min(dp[m-p]) et éviter `initialisation oubliée`.
### Corrigé question 3
- Résultat attendu : tabulation stocke chaque dp[m].
- Critère spécifique : initialiser dp[0]=0 et éviter `choix de pièce confondu avec valeur optimale`.
### Corrigé question 4
- Résultat attendu : sans pièce 1 certains montants impossibles.
- Critère spécifique : remplir la table de 1 à 11 et éviter `état ambigu`.

## Erreurs fréquentes et remédiation
- état ambigu.
- initialisation oubliée.
- choix de pièce confondu avec valeur optimale.

## Cas limites travaillés
- montant 0.
- montant impossible.
- pièce plus grande que m.

## Critères de réussite observables
- La donnée de départ est recopiée exactement.
- La trace ou le pseudo-code conduit à `dp[6]=2 avec 5+1`.
- Au moins un cas limite de la section précédente est décidé.



## Barème question par question
- question 1: 1 point donnée exacte, 1 point méthode liée à la capacité, 1 point résultat vérifiable, 1 point justification du cas limite.
- question 2: 1 point donnée exacte, 1 point méthode liée à la capacité, 1 point résultat vérifiable, 1 point justification du cas limite.
- question 3: 1 point donnée exacte, 1 point méthode liée à la capacité, 1 point résultat vérifiable, 1 point justification du cas limite.
- question 4: 1 point donnée exacte, 1 point méthode liée à la capacité, 1 point résultat vérifiable, 1 point justification du cas limite.

## Fiche liée
- Fiche liée : fiche de cours T17 sur `programmation_dynamique`.

## Aménagement
- Version aménagée : `T17_version_amenagee_programmation_dynamique.md` ; consignes découpées et barème conservé.
