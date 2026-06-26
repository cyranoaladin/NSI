---
title: "T09 - EVALUATION - Bases relationnelles, clés et contraintes"
level: "terminale"
sequence_id: "T09"
document_type: "evaluation"
status: "needs_review"
version: "0.2.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Bases de données"
notion: "tables, clés primaires, clés étrangères, contraintes"
objectifs:
  - "identifier la clé primaire de chaque table"
  - "repérer la clé étrangère Note.id_eleve"
  - "signaler une référence vers un élève absent"
  - "distinguer contrainte de domaine et contrainte de référence"
private_data: false
official_program:
  capacities:
    - "T-BDD-01A"
    - "T-BDD-01B"
    - "T-BDD-01C"
    - "T-BDD-02"
---

# T09 - Évaluation courte - Bases relationnelles, clés et contraintes

## Objectifs évalués
- O1 : identifier la clé primaire de chaque table.
- O2 : repérer la clé étrangère Note.id_eleve.
- O3 : signaler une référence vers un élève absent.
- O4 : distinguer contrainte de domaine et contrainte de référence.

## Capacités officielles
- T-BDD-01A
- T-BDD-01B
- T-BDD-01C
- T-BDD-02

## Questions
### Question 1
- Capacité : T-BDD-01A.
- Énoncé : avec `Eleve(1, "E2", "1G1"), Note(10, 1, "NSI", 15), Note(11, 9, "NSI", 12)`, identifier la clé primaire de chaque table.
- Réponse attendue : méthode explicite, résultat contrôlé et vocabulaire du chapitre T09.
- Critère de réussite : l’erreur « utiliser le nom comme clé primaire » est évitée ou corrigée.
### Question 2
- Capacité : T-BDD-01B.
- Énoncé : avec `Eleve(1, "E2", "1G1"), Note(10, 1, "NSI", 15), Note(11, 9, "NSI", 12)`, repérer la clé étrangère Note.id_eleve.
- Réponse attendue : méthode explicite, résultat contrôlé et vocabulaire du chapitre T09.
- Critère de réussite : l’erreur « accepter une note hors 0..20 » est évitée ou corrigée.
### Question 3
- Capacité : T-BDD-01C.
- Énoncé : avec `Eleve(1, "E2", "1G1"), Note(10, 1, "NSI", 15), Note(11, 9, "NSI", 12)`, signaler une référence vers un élève absent.
- Réponse attendue : méthode explicite, résultat contrôlé et vocabulaire du chapitre T09.
- Critère de réussite : l’erreur « insérer une note pour un élève absent » est évitée ou corrigée.
### Question 4
- Capacité : T-BDD-02.
- Énoncé : avec `Eleve(1, "E2", "1G1"), Note(10, 1, "NSI", 15), Note(11, 9, "NSI", 12)`, distinguer contrainte de domaine et contrainte de référence.
- Réponse attendue : méthode explicite, résultat contrôlé et vocabulaire du chapitre T09.
- Critère de réussite : l’erreur « confondre clé primaire et clé étrangère » est évitée ou corrigée.

## Barème
- Question 1 : 2 points méthode, 1 point résultat, 1 point contrôle du cas limite.
- Question 2 : 2 points méthode, 1 point résultat, 1 point contrôle du cas limite.
- Question 3 : 2 points méthode, 1 point résultat, 1 point contrôle du cas limite.
- Question 4 : 2 points méthode, 1 point résultat, 1 point contrôle du cas limite.

## Corrigé
### Corrigé question 1
- Démarche : identifier la clé primaire de chaque table.
- Résultat attendu : une conclusion compatible avec `Eleve(1, "E2", "1G1"), Note(10, 1, "NSI", 15), Note(11, 9, "NSI", 12)`.
- Justification : le contrôle explicite empêche l’erreur « utiliser le nom comme clé primaire ».
### Corrigé question 2
- Démarche : repérer la clé étrangère Note.id_eleve.
- Résultat attendu : une conclusion compatible avec `Eleve(1, "E2", "1G1"), Note(10, 1, "NSI", 15), Note(11, 9, "NSI", 12)`.
- Justification : le contrôle explicite empêche l’erreur « accepter une note hors 0..20 ».
### Corrigé question 3
- Démarche : signaler une référence vers un élève absent.
- Résultat attendu : une conclusion compatible avec `Eleve(1, "E2", "1G1"), Note(10, 1, "NSI", 15), Note(11, 9, "NSI", 12)`.
- Justification : le contrôle explicite empêche l’erreur « insérer une note pour un élève absent ».
### Corrigé question 4
- Démarche : distinguer contrainte de domaine et contrainte de référence.
- Résultat attendu : une conclusion compatible avec `Eleve(1, "E2", "1G1"), Note(10, 1, "NSI", 15), Note(11, 9, "NSI", 12)`.
- Justification : le contrôle explicite empêche l’erreur « confondre clé primaire et clé étrangère ».

## Critères de réussite
- Les capacités officielles sont citées dans les réponses.
- Chaque question contient donnée, méthode, résultat et contrôle.
- Le vocabulaire disciplinaire est utilisé sans remplacer la justification.
- Le barème reste indicatif tant que la ressource est en needs_review.
