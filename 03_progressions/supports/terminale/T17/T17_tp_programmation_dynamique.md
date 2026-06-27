---
title: "T17 - tp - programmation dynamique"
level: "terminale"
sequence_id: "T17"
document_type: "tp"
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

# T17 - TP - programmation dynamique

## Statut du TP
TP exécutable : utiliser les fichiers du dossier `code/` (T17_starter_programmation_dynamique.py, T17_tests_attendus_programmation_dynamique.py, T17_corrige_professeur_programmation_dynamique.py).

## Donnée fournie
`pieces=[1,5,7], montant=11, dp[0]=0`

## Travail demandé
1. Préparer la donnée et nommer les champs utiles.
2. Réaliser : définir dp[m] coût minimal.
3. Réaliser : écrire dp[m]=1+min(dp[m-p]).
4. Tester le cas limite `montant 0`.
5. Produire le livrable : dp[6]=2 avec 5+1.

## Barème associé
- 2 points : donnée préparée.
- 3 points : méthode principale.
- 3 points : résultat `dp[6]=2 avec 5+1`.
- 2 points : cas limite `montant 0`.

## Corrigé question par question
### Corrigé question 1
Résultat attendu : `pieces=[1,5,7], montant=11, dp[0]=0`.
### Corrigé question 2
Résultat attendu : dp[6]=2 avec 5+1.
### Corrigé question 3
Résultat attendu : dp[11]=3 avec 5+5+1.
### Corrigé question 4
Résultat attendu : `montant 0` traité sans ambiguïté.

## Liens
- TD lié : `T17_TD_programmation_dynamique.md`.
- Évaluation liée : `T17_evaluation_programmation_dynamique.md`.

## Cas limites travaillés
- montant 0.
- montant impossible.
- pièce plus grande que m.

## Erreurs fréquentes
- état ambigu.
- initialisation oubliée.
- choix de pièce confondu avec valeur optimale.

## Critères de réussite observables
- La donnée de départ est recopiée exactement.
- La trace ou le pseudo-code conduit à `dp[6]=2 avec 5+1`.
- Au moins un cas limite de la section précédente est décidé.



## Assets Python
- Starter élève : `code/T17_starter_programmation_dynamique.py`.
- Tests attendus : `code/T17_tests_attendus_programmation_dynamique.py`.
- Corrigé professeur : `code/T17_corrige_professeur_programmation_dynamique.py`.
- Le starter doit échouer aux tests complets ; le corrigé professeur doit passer.
