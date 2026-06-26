---
title: "T00 - Td - Diagnostic tests"
level: "terminale"
sequence_id: "T00"
document_type: "td"
status: "needs_review"
version: "0.4.1"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Reprise Python et tests"
notion: "fonction, assertion, cas limite, spécification"
objectifs:
  - "Objectif O1 - Identifier précisément la représentation ou la structure en jeu"
  - "Objectif O2 - Appliquer une méthode disciplinaire complète"
  - "Objectif O3 - Justifier le résultat sur un cas différent"
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur observée"
private_data: false
official_program:
  capacities:
    - "T-LANG-03A"
---

# T00 - TD - Diagnostic tests

## Objectifs spécifiques
- Objectif O1 - Identifier précisément la représentation ou la structure en jeu.
- Objectif O2 - Appliquer une méthode disciplinaire complète.
- Objectif O3 - Justifier le résultat sur un cas différent.
- Objectif O4 - Contrôler un cas limite et corriger une erreur observée.

## Capacités officielles atomiques
- T-LANG-03A

## Prérequis
- Reconnaître une consigne liée à fonction.
- Distinguer donnée, méthode et conclusion dans le thème Reprise Python et tests.
- Rédiger une justification courte en utilisant le vocabulaire du programme.
- Contrôler une réponse par un cas limite ou un contre-exemple explicite.

## Séance(s) correspondante(s)
- T00-S1 à T00-S4 : support rattaché aux séances prêtes de la progression.

## Situation-problème concrète
Une équipe reprend une bibliothèque Python de Première et doit écrire des tests avant de modifier le code.

## Activité d’entrée
1. Écrire le résultat attendu pour une fonction `maximum`.
2. Choisir un cas nominal, un cas limite et un cas invalide.
3. Distinguer spécification et implémentation.
4. Lire un message d’assertion échouée.

## Exemples corrigés précis
### Exemple corrigé 1 - maximum nominal
- Donnée étudiée : `[3, 7, 2]`.
- Méthode : parcourir la liste en conservant le meilleur élément.
- Résultat obtenu : `7`.
- Contrôle : le cas limite « liste d’un élément » est vérifié séparément.
### Exemple corrigé 2 - liste vide
- Donnée étudiée : `[]`.
- Méthode : refuser l’entrée avant le parcours.
- Résultat obtenu : exception documentée.
- Contrôle : le cas limite « aucune valeur initiale » est vérifié séparément.
### Exemple corrigé 3 - assertion
- Donnée étudiée : `assert maximum([1]) == 1`.
- Méthode : traduire une exigence en test exécutable.
- Résultat obtenu : test passant.
- Contrôle : le cas limite « message utile en cas d’échec » est vérifié séparément.
### Exemple corrigé 4 - entrée invalide
- Donnée étudiée : `[1, "x"]`.
- Méthode : définir si le mélange de types est autorisé.
- Résultat obtenu : erreur contrôlée.
- Contrôle : le cas limite « comparaison impossible » est vérifié séparément.
## Exercices numérotés
### Exercice 1
- Objectif travaillé : O1.
- Capacité officielle : T-LANG-03A.
- Énoncé disciplinaire : résoudre maximum nominal avec `[3, 7, 2]`.
- Production attendue : `7`.
- Contrainte de contrôle : faire apparaître le contrôle « liste d’un élément ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 2
- Objectif travaillé : O2.
- Capacité officielle : T-LANG-03A.
- Énoncé disciplinaire : expliquer liste vide à partir de `[]`.
- Production attendue : exception documentée.
- Contrainte de contrôle : rédiger la méthode avant le résultat.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 3
- Objectif travaillé : O3.
- Capacité officielle : T-LANG-03A.
- Énoncé disciplinaire : comparer assertion avec `assert maximum([1]) == 1`.
- Production attendue : test passant.
- Contrainte de contrôle : comparer avec le cas « message utile en cas d’échec ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 4
- Objectif travaillé : O4.
- Capacité officielle : T-LANG-03A.
- Énoncé disciplinaire : corriger entrée invalide pour `[1, "x"]`.
- Production attendue : erreur contrôlée.
- Contrainte de contrôle : corriger l’erreur « Ne pas lire le message d’échec. ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 5
- Objectif travaillé : O1.
- Capacité officielle : T-LANG-03A.
- Énoncé disciplinaire : tester un cas limite lié à liste d’un élément.
- Production attendue : le comportement de maximum nominal est contrôlé.
- Contrainte de contrôle : nommer la donnée minimale et la conclusion.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 6
- Objectif travaillé : O2.
- Capacité officielle : T-LANG-03A.
- Énoncé disciplinaire : classer deux méthodes possibles pour liste vide.
- Production attendue : la méthode robuste est choisie et justifiée.
- Contrainte de contrôle : identifier pourquoi « Écrire un test qui reproduit le code au lieu de la spécification. » est une erreur.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 7
- Objectif travaillé : O3.
- Capacité officielle : T-LANG-03A.
- Énoncé disciplinaire : justifier un transfert qui utilise assertion avec une donnée nouvelle.
- Production attendue : la justification reste valable sur le nouveau cas.
- Contrainte de contrôle : inclure une étape calculable par un pair.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 8
- Objectif travaillé : O4.
- Capacité officielle : T-LANG-03A.
- Énoncé disciplinaire : étendre un énoncé volontairement erroné sur entrée invalide.
- Production attendue : l’erreur est localisée puis réparée.
- Contrainte de contrôle : proposer une activité corrective inspirée de « Réécrire le message d’échec comme diagnostic. ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
## Corrigé
### Corrigé exercice 1
- Méthode : identifier `[3, 7, 2]`, appliquer la méthode « parcourir la liste en conservant le meilleur élément », puis écrire `7`.
- Résultat : `7`.
- Contrôle : faire apparaître le contrôle « liste d’un élément ».
- Erreur traitée : EF1 - Tester seulement le cas donné en exemple.
### Corrigé exercice 2
- Méthode : expliciter chaque étape de refuser l’entrée avant le parcours avant de conclure par exception documentée.
- Résultat : exception documentée.
- Contrôle : rédiger la méthode avant le résultat.
- Erreur traitée : EF2 - Écrire un test qui reproduit le code au lieu de la spécification.
### Corrigé exercice 3
- Méthode : comparer la donnée avec le cas limite « message utile en cas d’échec » et valider test passant.
- Résultat : test passant.
- Contrôle : comparer avec le cas « message utile en cas d’échec ».
- Erreur traitée : EF3 - Oublier le cas vide.
### Corrigé exercice 4
- Méthode : isoler l’erreur fréquente « Ne pas lire le message d’échec. » puis reprendre la procédure correcte.
- Résultat : erreur contrôlée.
- Contrôle : corriger l’erreur « Ne pas lire le message d’échec. ».
- Erreur traitée : EF4 - Ne pas lire le message d’échec.
### Corrigé exercice 5
- Méthode : identifier `[3, 7, 2]`, appliquer la méthode « parcourir la liste en conservant le meilleur élément », puis écrire `7`.
- Résultat : le comportement de maximum nominal est contrôlé.
- Contrôle : nommer la donnée minimale et la conclusion.
- Erreur traitée : EF1 - Tester seulement le cas donné en exemple.
### Corrigé exercice 6
- Méthode : expliciter chaque étape de refuser l’entrée avant le parcours avant de conclure par exception documentée.
- Résultat : la méthode robuste est choisie et justifiée.
- Contrôle : identifier pourquoi « Écrire un test qui reproduit le code au lieu de la spécification. » est une erreur.
- Erreur traitée : EF2 - Écrire un test qui reproduit le code au lieu de la spécification.
### Corrigé exercice 7
- Méthode : comparer la donnée avec le cas limite « message utile en cas d’échec » et valider test passant.
- Résultat : la justification reste valable sur le nouveau cas.
- Contrôle : inclure une étape calculable par un pair.
- Erreur traitée : EF3 - Oublier le cas vide.
### Corrigé exercice 8
- Méthode : isoler l’erreur fréquente « Ne pas lire le message d’échec. » puis reprendre la procédure correcte.
- Résultat : l’erreur est localisée puis réparée.
- Contrôle : proposer une activité corrective inspirée de « Réécrire le message d’échec comme diagnostic. ».
- Erreur traitée : EF4 - Ne pas lire le message d’échec.
## Erreurs fréquentes
- Erreur fréquente EF1 - Tester seulement le cas donné en exemple.
- Erreur fréquente EF2 - Écrire un test qui reproduit le code au lieu de la spécification.
- Erreur fréquente EF3 - Oublier le cas vide.
- Erreur fréquente EF4 - Ne pas lire le message d’échec.

## Remédiation ciblée
- Activité corrective EF1 : Construire un tableau cas nominal, limite, invalide.
- Activité corrective EF2 : Formuler le résultat attendu en français avant le code du test.
- Activité corrective EF3 : Ajouter systématiquement une entrée minimale.
- Activité corrective EF4 : Réécrire le message d’échec comme diagnostic.

## Différenciation
- Socle : traiter `[3, 7, 2]` avec une fiche méthode fournie.
- Standard : traiter `[]` en rédigeant la justification complète.
- Expert : inventer un cas limite lié à « message utile en cas d’échec » et expliquer le comportement attendu.

## Critères de réussite
- La capacité officielle est citée dans la copie.
- La méthode contient au moins une étape vérifiable par un pair.
- Le cas limite est discuté avec une donnée concrète.
- La correction explique quelle erreur fréquente est évitée.
