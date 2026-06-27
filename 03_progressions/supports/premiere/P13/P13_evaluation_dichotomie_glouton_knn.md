---
title: "P13 - evaluation - dichotomie, glouton et k-NN"
level: "premiere"
sequence_id: "P13"
document_type: "evaluation"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "dichotomie, glouton et k-NN"
notion: "dichotomie, glouton et k-NN"
private_data: false
official_program:
  capacities:
    - "P-ALGO-03"
    - "P-ALGO-04"
    - "P-ALGO-05"
---

# P13 - Évaluation - dichotomie, glouton et k-NN

## Modalités
- Durée : 30 minutes.
- Matériel autorisé : fiche de cours.
- Capacités évaluées : P-ALGO-03, P-ALGO-04, P-ALGO-05.

## Questions
### Question 1
- Capacité officielle : P-ALGO-03.
- Énoncé : à partir de `tableau=[4,9,18,23,37,41], cible=37 ; pièces=[10,5,2,1], montant=28 ; voisins=[rouge:1.2, bleu:2.0, rouge:2.4]`, calculer milieu puis réduire intervalle.
- Réponse attendue : milieux 18 puis 37 -> trouvé indice 4.
- Barème : 1 point donnée, 1 point méthode, 1 point résultat, 1 point justification sur `cible absente`.
### Question 2
- Capacité officielle : P-ALGO-04.
- Énoncé : à partir de `tableau=[4,9,18,23,37,41], cible=37 ; pièces=[10,5,2,1], montant=28 ; voisins=[rouge:1.2, bleu:2.0, rouge:2.4]`, montrer que droite-gauche diminue.
- Réponse attendue : 28 -> 10+10+5+2+1.
- Barème : 1 point donnée, 1 point méthode, 1 point résultat, 1 point justification sur `pièce 1 absente`.
### Question 3
- Capacité officielle : P-ALGO-05.
- Énoncé : à partir de `tableau=[4,9,18,23,37,41], cible=37 ; pièces=[10,5,2,1], montant=28 ; voisins=[rouge:1.2, bleu:2.0, rouge:2.4]`, prendre la plus grande pièce possible.
- Réponse attendue : rouge, bleu, rouge -> classe rouge.
- Barème : 1 point donnée, 1 point méthode, 1 point résultat, 1 point justification sur `égalité de vote`.
### Question 4
- Capacité officielle : P-ALGO-03.
- Énoncé : à partir de `tableau=[4,9,18,23,37,41], cible=37 ; pièces=[10,5,2,1], montant=28 ; voisins=[rouge:1.2, bleu:2.0, rouge:2.4]`, voter parmi k=3 voisins.
- Réponse attendue : cible 40 absente -> non trouvé.
- Barème : 1 point donnée, 1 point méthode, 1 point résultat, 1 point justification sur `cible absente`.

## Corrigé question par question
### Corrigé question 1
- Résultat attendu : milieux 18 puis 37 -> trouvé indice 4.
- Critère spécifique : calculer milieu puis réduire intervalle et éviter `dichotomie sur liste non triée`.
### Corrigé question 2
- Résultat attendu : 28 -> 10+10+5+2+1.
- Critère spécifique : montrer que droite-gauche diminue et éviter `glouton supposé toujours optimal`.
### Corrigé question 3
- Résultat attendu : rouge, bleu, rouge -> classe rouge.
- Critère spécifique : prendre la plus grande pièce possible et éviter `égalité k-NN non décidée`.
### Corrigé question 4
- Résultat attendu : cible 40 absente -> non trouvé.
- Critère spécifique : voter parmi k=3 voisins et éviter `dichotomie sur liste non triée`.

## Erreurs fréquentes et remédiation
- dichotomie sur liste non triée.
- glouton supposé toujours optimal.
- égalité k-NN non décidée.

## Cas limites travaillés
- cible absente.
- pièce 1 absente.
- égalité de vote.

## Critères de réussite observables
- La donnée de départ est recopiée exactement.
- La trace ou le pseudo-code conduit à `milieux 18 puis 37 -> trouvé indice 4`.
- Au moins un cas limite de la section précédente est décidé.



## Barème question par question
- question 1: 1 point donnée exacte, 1 point méthode liée à la capacité, 1 point résultat vérifiable, 1 point justification du cas limite.
- question 2: 1 point donnée exacte, 1 point méthode liée à la capacité, 1 point résultat vérifiable, 1 point justification du cas limite.
- question 3: 1 point donnée exacte, 1 point méthode liée à la capacité, 1 point résultat vérifiable, 1 point justification du cas limite.
- question 4: 1 point donnée exacte, 1 point méthode liée à la capacité, 1 point résultat vérifiable, 1 point justification du cas limite.

## Fiche liée
- Fiche liée : fiche de cours P13 sur `dichotomie_glouton_knn`.

## Aménagement
- Version aménagée : `P13_version_amenagee_dichotomie_glouton_knn.md` ; consignes découpées et barème conservé.
