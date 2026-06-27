---
title: "P07 - EVALUATION - Fonctions, spécifications et tests"
level: "premiere"
sequence_id: "P07"
document_type: "evaluation"
status: "needs_review"
version: "0.2.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Langage Python"
notion: "fonctions, paramètres, assertions, tests"
objectifs:
  - "écrire la signature et le rôle des paramètres"
  - "formuler précondition et postcondition"
  - "ajouter une assertion sur le prix négatif"
  - "tester cas nominal, zéro et entrée invalide"
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

# P07 - Évaluation courte - Fonctions, spécifications et tests

## Objectifs évalués
- O1 : écrire la signature et le rôle des paramètres.
- O2 : formuler précondition et postcondition.
- O3 : ajouter une assertion sur le prix négatif.
- O4 : tester cas nominal, zéro et entrée invalide.

## Capacités officielles
- P-LANG-01
- P-LANG-02
- P-LANG-03A
- P-LANG-03B
- P-LANG-03C
- P-LANG-04
- P-LANG-05

## Questions
### Question 1
- Capacité : P-LANG-01.
- Énoncé : avec `prix_ttc(80, 0.20), prix_ttc(0, 0.20), prix_ttc(-5, 0.20)`, écrire la signature et le rôle des paramètres.
- Réponse attendue : méthode explicite, résultat contrôlé et vocabulaire du chapitre P07.
- Critère de réussite : l’erreur « écrire un print au lieu de return » est évitée ou corrigée.
### Question 2
- Capacité : P-LANG-02.
- Énoncé : avec `prix_ttc(80, 0.20), prix_ttc(0, 0.20), prix_ttc(-5, 0.20)`, formuler précondition et postcondition.
- Réponse attendue : méthode explicite, résultat contrôlé et vocabulaire du chapitre P07.
- Critère de réussite : l’erreur « oublier le cas limite ht=0 » est évitée ou corrigée.
### Question 3
- Capacité : P-LANG-03A.
- Énoncé : avec `prix_ttc(80, 0.20), prix_ttc(0, 0.20), prix_ttc(-5, 0.20)`, ajouter une assertion sur le prix négatif.
- Réponse attendue : méthode explicite, résultat contrôlé et vocabulaire du chapitre P07.
- Critère de réussite : l’erreur « tester seulement la valeur 80 » est évitée ou corrigée.
### Question 4
- Capacité : P-LANG-03B.
- Énoncé : avec `prix_ttc(80, 0.20), prix_ttc(0, 0.20), prix_ttc(-5, 0.20)`, tester cas nominal, zéro et entrée invalide.
- Réponse attendue : méthode explicite, résultat contrôlé et vocabulaire du chapitre P07.
- Critère de réussite : l’erreur « modifier une variable globale depuis la fonction » est évitée ou corrigée.

## Barème
- Question 1 : 2 points méthode, 1 point résultat, 1 point contrôle du cas limite.
- Question 2 : 2 points méthode, 1 point résultat, 1 point contrôle du cas limite.
- Question 3 : 2 points méthode, 1 point résultat, 1 point contrôle du cas limite.
- Question 4 : 2 points méthode, 1 point résultat, 1 point contrôle du cas limite.

## Corrigé
### Corrigé question 1
- Démarche : écrire la signature et le rôle des paramètres.
- Résultat attendu : une conclusion justifiée par les valeurs obtenues avec `prix_ttc(80, 0.20), prix_ttc(0, 0.20), prix_ttc(-5, 0.20)`.
- Justification : le contrôle explicite empêche l’erreur « écrire un print au lieu de return ».
### Corrigé question 2
- Démarche : formuler précondition et postcondition.
- Résultat attendu : une conclusion justifiée par les valeurs obtenues avec `prix_ttc(80, 0.20), prix_ttc(0, 0.20), prix_ttc(-5, 0.20)`.
- Justification : le contrôle explicite empêche l’erreur « oublier le cas limite ht=0 ».
### Corrigé question 3
- Démarche : ajouter une assertion sur le prix négatif.
- Résultat attendu : une conclusion justifiée par les valeurs obtenues avec `prix_ttc(80, 0.20), prix_ttc(0, 0.20), prix_ttc(-5, 0.20)`.
- Justification : le contrôle explicite empêche l’erreur « tester seulement la valeur 80 ».
### Corrigé question 4
- Démarche : tester cas nominal, zéro et entrée invalide.
- Résultat attendu : une conclusion justifiée par les valeurs obtenues avec `prix_ttc(80, 0.20), prix_ttc(0, 0.20), prix_ttc(-5, 0.20)`.
- Justification : le contrôle explicite empêche l’erreur « modifier une variable globale depuis la fonction ».

## Critères de réussite
- Les capacités officielles sont citées dans les réponses.
- Chaque question contient donnée, méthode, résultat et contrôle.
- Le vocabulaire disciplinaire est utilisé sans remplacer la justification.
- Le barème reste indicatif tant que la ressource est en needs_review.

## Modalités de passation
- Durée : 25 minutes.
- Matériel autorisé : fiche personnelle, sans corrigé ni accès réseau.
- Capacités évaluées :
- P-LANG-01
- P-LANG-02
- P-LANG-03A
- P-LANG-03B
- P-LANG-03C
- P-LANG-04
- P-LANG-05

## Fiche liée et aménagement
- Fiche liée : fiche de cours opérationnelle de la séquence P07, statut `needs_review`.
- Séance liée : `P07-S1` dans la progression annuelle.
- Version aménagée : même sujet avec données surlignées et tableau méthode / résultat / contrôle.
- Remédiation : reprendre la question la moins réussie avec une donnée plus courte puis faire verbaliser la méthode.
## Erreurs fréquentes
- EF1 : répondre sans citer la donnée utilisée ; correction : encadrer la donnée avant de rédiger.
- EF2 : donner un résultat sans méthode ; correction : séparer méthode, résultat et contrôle.
- EF3 : oublier le cas limite ; correction : refaire une question avec une donnée minimale.

