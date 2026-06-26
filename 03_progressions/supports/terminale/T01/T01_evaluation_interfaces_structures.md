---
title: "T01 - Evaluation - Interfaces et structures"
level: "terminale"
sequence_id: "T01"
document_type: "evaluation"
status: "needs_review"
version: "0.4.1"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Structures de données abstraites"
notion: "interface, invariant, pile, file"
objectifs:
  - "Objectif O1 - Identifier précisément la représentation ou la structure en jeu"
  - "Objectif O2 - Appliquer une méthode disciplinaire complète"
  - "Objectif O3 - Justifier le résultat sur un cas différent"
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur observée"
private_data: false
official_program:
  capacities:
    - "T-STRUCT-01A"
---


# T01 - Évaluation courte - Interfaces et structures

## Objectifs spécifiques
- Objectif O1 - Identifier précisément la représentation ou la structure en jeu.
- Objectif O2 - Appliquer une méthode disciplinaire complète.
- Objectif O3 - Justifier le résultat sur un cas différent.
- Objectif O4 - Contrôler un cas limite et corriger une erreur observée.

## Capacités officielles atomiques
- T-STRUCT-01A

## Prérequis
- Reconnaître une consigne liée à interface.
- Distinguer donnée, méthode et conclusion dans le thème Structures de données abstraites.
- Rédiger une justification courte en utilisant le vocabulaire du programme.
- Contrôler une réponse par un cas limite ou un contre-exemple explicite.

## Séance(s) correspondante(s)
- T01-S1 à T01-S5 : support rattaché aux séances prêtes de la progression.

## Situation-problème concrète
Un module doit exposer une pile sans révéler si elle est stockée par liste Python ou par maillons.

## Activité d’entrée
1. Lister les opérations d’une pile.
2. Écrire un invariant après empilement.
3. Comparer interface et représentation.
4. Prévoir le comportement sur structure vide.

## Questions
### Question 1
- Objectif évalué : O1.
- Capacité officielle : T-STRUCT-01A.
- Énoncé : résoudre interface pile avec `push`, `pop`, `is_empty`.
- Réponse attendue : interface indépendante du stockage.
- Critère de réussite : méthode visible, résultat correct et contrôle « dépilement vide ».
### Question 2
- Objectif évalué : O2.
- Capacité officielle : T-STRUCT-01A.
- Énoncé : expliquer invariant à partir de taille après deux empilements.
- Réponse attendue : taille augmentée de 2.
- Critère de réussite : méthode visible, résultat correct et contrôle « opération refusée ».
### Question 3
- Objectif évalué : O3.
- Capacité officielle : T-STRUCT-01A.
- Énoncé : comparer file avec arrivées A puis B.
- Réponse attendue : A sort avant B.
- Critère de réussite : méthode visible, résultat correct et contrôle « file vide ».
### Question 4
- Objectif évalué : O4.
- Capacité officielle : T-STRUCT-01A.
- Énoncé : corriger encapsulation pour liste interne `_items`.
- Réponse attendue : tests écrits sur méthodes publiques.
- Critère de réussite : méthode visible, résultat correct et contrôle « changement de représentation ».
## Barème
- Question 1 : 2 points méthode, 1 point résultat, 1 point justification liée à dépilement vide.
- Question 2 : 2 points méthode, 1 point résultat, 1 point justification liée à opération refusée.
- Question 3 : 2 points méthode, 1 point résultat, 1 point justification liée à file vide.
- Question 4 : 2 points méthode, 1 point résultat, 1 point justification liée à changement de représentation.
## Erreurs fréquentes
- Erreur fréquente EF1 - Confondre interface et implémentation.
- Erreur fréquente EF2 - Tester un attribut interne au lieu de l’opération publique.
- Erreur fréquente EF3 - Oublier l’état vide.
- Erreur fréquente EF4 - Mélanger ordre LIFO et ordre FIFO.

## Remédiation ciblée
- Activité corrective EF1 : Écrire le contrat avant le choix de représentation.
- Activité corrective EF2 : Réécrire les tests en utilisant seulement les méthodes publiques.
- Activité corrective EF3 : Faire une trace d’opérations depuis la structure vide.
- Activité corrective EF4 : Comparer une pile et une file avec la même suite d’entrées.

## Différenciation
- Socle : traiter `push`, `pop`, `is_empty` avec une fiche méthode fournie.
- Standard : traiter taille après deux empilements en rédigeant la justification complète.
- Expert : inventer un cas limite lié à « file vide » et expliquer le comportement attendu.

## Critères de réussite
- La capacité officielle est citée dans la copie.
- La méthode contient au moins une étape vérifiable par un pair.
- Le cas limite est discuté avec une donnée concrète.
- La correction explique quelle erreur fréquente est évitée.

## Exercices numérotés
- Exercice 1 : reprendre question 1 en explicitant donnée, méthode, résultat et contrôle pour T01.
- Exercice 2 : reprendre question 2 en explicitant donnée, méthode, résultat et contrôle pour T01.
- Exercice 3 : reprendre question 3 en explicitant donnée, méthode, résultat et contrôle pour T01.
- Exercice 4 : reprendre question 4 en explicitant donnée, méthode, résultat et contrôle pour T01.

## Corrigé
### Corrigé question 1
- Résultat attendu : interface indépendante du stockage.
- Méthode exigée : reprendre la démarche du cours puis vérifier le cas limite de la question 1.
- Critère de validation : méthode visible, résultat correct et contrôle « dépilement vide ».
### Corrigé question 2
- Résultat attendu : taille augmentée de 2.
- Méthode exigée : reprendre la démarche du cours puis vérifier le cas limite de la question 2.
- Critère de validation : méthode visible, résultat correct et contrôle « opération refusée ».
### Corrigé question 3
- Résultat attendu : A sort avant B.
- Méthode exigée : reprendre la démarche du cours puis vérifier le cas limite de la question 3.
- Critère de validation : méthode visible, résultat correct et contrôle « file vide ».
### Corrigé question 4
- Résultat attendu : tests écrits sur méthodes publiques.
- Méthode exigée : reprendre la démarche du cours puis vérifier le cas limite de la question 4.
- Critère de validation : méthode visible, résultat correct et contrôle « changement de représentation ».
