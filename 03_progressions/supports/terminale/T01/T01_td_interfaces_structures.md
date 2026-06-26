---
title: "T01 - Td - Interfaces et structures"
level: "terminale"
sequence_id: "T01"
document_type: "td"
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

# T01 - TD - Interfaces et structures

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

## Exemples corrigés précis
### Exemple corrigé 1 - interface pile
- Donnée étudiée : `push`, `pop`, `is_empty`.
- Méthode : décrire contrat d’entrée et résultat de chaque opération.
- Résultat obtenu : interface indépendante du stockage.
- Contrôle : le cas limite « dépilement vide » est vérifié séparément.
### Exemple corrigé 2 - invariant
- Donnée étudiée : taille après deux empilements.
- Méthode : relier nombre d’éléments et opérations réalisées.
- Résultat obtenu : taille augmentée de 2.
- Contrôle : le cas limite « opération refusée » est vérifié séparément.
### Exemple corrigé 3 - file
- Donnée étudiée : arrivées A puis B.
- Méthode : sortir dans l’ordre FIFO.
- Résultat obtenu : A sort avant B.
- Contrôle : le cas limite « file vide » est vérifié séparément.
### Exemple corrigé 4 - encapsulation
- Donnée étudiée : liste interne `_items`.
- Méthode : ne jamais dépendre du détail privé.
- Résultat obtenu : tests écrits sur méthodes publiques.
- Contrôle : le cas limite « changement de représentation » est vérifié séparément.
## Exercices numérotés
### Exercice 1
- Objectif travaillé : O1.
- Capacité officielle : T-STRUCT-01A.
- Énoncé disciplinaire : résoudre interface pile avec `push`, `pop`, `is_empty`.
- Production attendue : interface indépendante du stockage.
- Contrainte de contrôle : faire apparaître le contrôle « dépilement vide ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 2
- Objectif travaillé : O2.
- Capacité officielle : T-STRUCT-01A.
- Énoncé disciplinaire : expliquer invariant à partir de taille après deux empilements.
- Production attendue : taille augmentée de 2.
- Contrainte de contrôle : rédiger la méthode avant le résultat.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 3
- Objectif travaillé : O3.
- Capacité officielle : T-STRUCT-01A.
- Énoncé disciplinaire : comparer file avec arrivées A puis B.
- Production attendue : A sort avant B.
- Contrainte de contrôle : comparer avec le cas « file vide ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 4
- Objectif travaillé : O4.
- Capacité officielle : T-STRUCT-01A.
- Énoncé disciplinaire : corriger encapsulation pour liste interne `_items`.
- Production attendue : tests écrits sur méthodes publiques.
- Contrainte de contrôle : corriger l’erreur « Mélanger ordre LIFO et ordre FIFO. ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 5
- Objectif travaillé : O1.
- Capacité officielle : T-STRUCT-01A.
- Énoncé disciplinaire : tester un cas limite lié à dépilement vide.
- Production attendue : le comportement de interface pile est contrôlé.
- Contrainte de contrôle : nommer la donnée minimale et la conclusion.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 6
- Objectif travaillé : O2.
- Capacité officielle : T-STRUCT-01A.
- Énoncé disciplinaire : classer deux méthodes possibles pour invariant.
- Production attendue : la méthode robuste est choisie et justifiée.
- Contrainte de contrôle : identifier pourquoi « Tester un attribut interne au lieu de l’opération publique. » est une erreur.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 7
- Objectif travaillé : O3.
- Capacité officielle : T-STRUCT-01A.
- Énoncé disciplinaire : justifier un transfert qui utilise file avec une donnée nouvelle.
- Production attendue : la justification reste valable sur le nouveau cas.
- Contrainte de contrôle : inclure une étape calculable par un pair.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 8
- Objectif travaillé : O4.
- Capacité officielle : T-STRUCT-01A.
- Énoncé disciplinaire : étendre un énoncé volontairement erroné sur encapsulation.
- Production attendue : l’erreur est localisée puis réparée.
- Contrainte de contrôle : proposer une activité corrective inspirée de « Comparer une pile et une file avec la même suite d’entrées. ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
## Corrigé
### Corrigé exercice 1
- Méthode : identifier `push`, `pop`, `is_empty`, appliquer la méthode « décrire contrat d’entrée et résultat de chaque opération », puis écrire interface indépendante du stockage.
- Résultat : interface indépendante du stockage.
- Contrôle : faire apparaître le contrôle « dépilement vide ».
- Erreur traitée : EF1 - Confondre interface et implémentation.
### Corrigé exercice 2
- Méthode : expliciter chaque étape de relier nombre d’éléments et opérations réalisées avant de conclure par taille augmentée de 2.
- Résultat : taille augmentée de 2.
- Contrôle : rédiger la méthode avant le résultat.
- Erreur traitée : EF2 - Tester un attribut interne au lieu de l’opération publique.
### Corrigé exercice 3
- Méthode : comparer la donnée avec le cas limite « file vide » et valider A sort avant B.
- Résultat : A sort avant B.
- Contrôle : comparer avec le cas « file vide ».
- Erreur traitée : EF3 - Oublier l’état vide.
### Corrigé exercice 4
- Méthode : isoler l’erreur fréquente « Mélanger ordre LIFO et ordre FIFO. » puis reprendre la procédure correcte.
- Résultat : tests écrits sur méthodes publiques.
- Contrôle : corriger l’erreur « Mélanger ordre LIFO et ordre FIFO. ».
- Erreur traitée : EF4 - Mélanger ordre LIFO et ordre FIFO.
### Corrigé exercice 5
- Méthode : identifier `push`, `pop`, `is_empty`, appliquer la méthode « décrire contrat d’entrée et résultat de chaque opération », puis écrire interface indépendante du stockage.
- Résultat : le comportement de interface pile est contrôlé.
- Contrôle : nommer la donnée minimale et la conclusion.
- Erreur traitée : EF1 - Confondre interface et implémentation.
### Corrigé exercice 6
- Méthode : expliciter chaque étape de relier nombre d’éléments et opérations réalisées avant de conclure par taille augmentée de 2.
- Résultat : la méthode robuste est choisie et justifiée.
- Contrôle : identifier pourquoi « Tester un attribut interne au lieu de l’opération publique. » est une erreur.
- Erreur traitée : EF2 - Tester un attribut interne au lieu de l’opération publique.
### Corrigé exercice 7
- Méthode : comparer la donnée avec le cas limite « file vide » et valider A sort avant B.
- Résultat : la justification reste valable sur le nouveau cas.
- Contrôle : inclure une étape calculable par un pair.
- Erreur traitée : EF3 - Oublier l’état vide.
### Corrigé exercice 8
- Méthode : isoler l’erreur fréquente « Mélanger ordre LIFO et ordre FIFO. » puis reprendre la procédure correcte.
- Résultat : l’erreur est localisée puis réparée.
- Contrôle : proposer une activité corrective inspirée de « Comparer une pile et une file avec la même suite d’entrées. ».
- Erreur traitée : EF4 - Mélanger ordre LIFO et ordre FIFO.
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
