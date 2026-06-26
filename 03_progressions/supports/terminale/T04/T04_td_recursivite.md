---
title: "T04 - Td - Récursivité"
level: "terminale"
sequence_id: "T04"
document_type: "td"
status: "needs_review"
version: "0.4.1"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Langage et preuve de terminaison"
notion: "appel récursif, cas de base, terminaison, pile d’appels"
objectifs:
  - "Objectif O1 - Identifier précisément la représentation ou la structure en jeu"
  - "Objectif O2 - Appliquer une méthode disciplinaire complète"
  - "Objectif O3 - Justifier le résultat sur un cas différent"
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur observée"
private_data: false
official_program:
  capacities:
    - "T-LANG-02A"
---

# T04 - TD - Récursivité

## Objectifs spécifiques
- Objectif O1 - Identifier précisément la représentation ou la structure en jeu.
- Objectif O2 - Appliquer une méthode disciplinaire complète.
- Objectif O3 - Justifier le résultat sur un cas différent.
- Objectif O4 - Contrôler un cas limite et corriger une erreur observée.

## Capacités officielles atomiques
- T-LANG-02A

## Prérequis
- Reconnaître une consigne liée à appel récursif.
- Distinguer donnée, méthode et conclusion dans le thème Langage et preuve de terminaison.
- Rédiger une justification courte en utilisant le vocabulaire du programme.
- Contrôler une réponse par un cas limite ou un contre-exemple explicite.

## Séance(s) correspondante(s)
- T04-S1 à T04-S5 : support rattaché aux séances prêtes de la progression.

## Situation-problème concrète
Un algorithme de parcours doit traiter une structure définie en se ramenant à un sous-problème plus petit.

## Activité d’entrée
1. Identifier le cas de base d’une factorielle.
2. Suivre les appels de `somme([4, 1, 3])`.
3. Comparer récursif et itératif.
4. Prévoir ce qui se passe sans décroissance.

## Exemples corrigés précis
### Exemple corrigé 1 - factorielle
- Donnée étudiée : `4!`.
- Méthode : appliquer `n * fact(n-1)` jusqu’au cas `0!`.
- Résultat obtenu : `24`.
- Contrôle : le cas limite « entier négatif refusé » est vérifié séparément.
### Exemple corrigé 2 - somme de liste
- Donnée étudiée : `[4, 1, 3]`.
- Méthode : séparer tête et reste.
- Résultat obtenu : `8`.
- Contrôle : le cas limite « liste vide » est vérifié séparément.
### Exemple corrigé 3 - longueur
- Donnée étudiée : `["a", "b"]`.
- Méthode : ajouter 1 à la longueur du reste.
- Résultat obtenu : `2`.
- Contrôle : le cas limite « reste vide » est vérifié séparément.
### Exemple corrigé 4 - terminaison
- Donnée étudiée : `n` décroît vers 0.
- Méthode : montrer une mesure entière strictement décroissante.
- Résultat obtenu : preuve de terminaison.
- Contrôle : le cas limite « appel avec même argument » est vérifié séparément.
## Exercices numérotés
### Exercice 1
- Objectif travaillé : O1.
- Capacité officielle : T-LANG-02A.
- Énoncé disciplinaire : résoudre factorielle avec `4!`.
- Production attendue : `24`.
- Contrainte de contrôle : faire apparaître le contrôle « entier négatif refusé ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 2
- Objectif travaillé : O2.
- Capacité officielle : T-LANG-02A.
- Énoncé disciplinaire : expliquer somme de liste à partir de `[4, 1, 3]`.
- Production attendue : `8`.
- Contrainte de contrôle : rédiger la méthode avant le résultat.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 3
- Objectif travaillé : O3.
- Capacité officielle : T-LANG-02A.
- Énoncé disciplinaire : comparer longueur avec `["a", "b"]`.
- Production attendue : `2`.
- Contrainte de contrôle : comparer avec le cas « reste vide ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 4
- Objectif travaillé : O4.
- Capacité officielle : T-LANG-02A.
- Énoncé disciplinaire : corriger terminaison pour `n` décroît vers 0.
- Production attendue : preuve de terminaison.
- Contrainte de contrôle : corriger l’erreur « Ne pas traiter l’entrée vide. ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 5
- Objectif travaillé : O1.
- Capacité officielle : T-LANG-02A.
- Énoncé disciplinaire : tester un cas limite lié à entier négatif refusé.
- Production attendue : le comportement de factorielle est contrôlé.
- Contrainte de contrôle : nommer la donnée minimale et la conclusion.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 6
- Objectif travaillé : O2.
- Capacité officielle : T-LANG-02A.
- Énoncé disciplinaire : classer deux méthodes possibles pour somme de liste.
- Production attendue : la méthode robuste est choisie et justifiée.
- Contrainte de contrôle : identifier pourquoi « Faire un appel récursif qui ne rapproche pas du cas de base. » est une erreur.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 7
- Objectif travaillé : O3.
- Capacité officielle : T-LANG-02A.
- Énoncé disciplinaire : justifier un transfert qui utilise longueur avec une donnée nouvelle.
- Production attendue : la justification reste valable sur le nouveau cas.
- Contrainte de contrôle : inclure une étape calculable par un pair.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 8
- Objectif travaillé : O4.
- Capacité officielle : T-LANG-02A.
- Énoncé disciplinaire : étendre un énoncé volontairement erroné sur terminaison.
- Production attendue : l’erreur est localisée puis réparée.
- Contrainte de contrôle : proposer une activité corrective inspirée de « Tester d’abord la liste vide ou `n = 0`. ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
## Corrigé
### Corrigé exercice 1
- Méthode : identifier `4!`, appliquer la méthode « appliquer `n * fact(n-1)` jusqu’au cas `0!` », puis écrire `24`.
- Résultat : `24`.
- Contrôle : faire apparaître le contrôle « entier négatif refusé ».
- Erreur traitée : EF1 - Oublier le cas de base.
### Corrigé exercice 2
- Méthode : expliciter chaque étape de séparer tête et reste avant de conclure par `8`.
- Résultat : `8`.
- Contrôle : rédiger la méthode avant le résultat.
- Erreur traitée : EF2 - Faire un appel récursif qui ne rapproche pas du cas de base.
### Corrigé exercice 3
- Méthode : comparer la donnée avec le cas limite « reste vide » et valider `2`.
- Résultat : `2`.
- Contrôle : comparer avec le cas « reste vide ».
- Erreur traitée : EF3 - Confondre valeur retournée et affichage des appels.
### Corrigé exercice 4
- Méthode : isoler l’erreur fréquente « Ne pas traiter l’entrée vide. » puis reprendre la procédure correcte.
- Résultat : preuve de terminaison.
- Contrôle : corriger l’erreur « Ne pas traiter l’entrée vide. ».
- Erreur traitée : EF4 - Ne pas traiter l’entrée vide.
### Corrigé exercice 5
- Méthode : identifier `4!`, appliquer la méthode « appliquer `n * fact(n-1)` jusqu’au cas `0!` », puis écrire `24`.
- Résultat : le comportement de factorielle est contrôlé.
- Contrôle : nommer la donnée minimale et la conclusion.
- Erreur traitée : EF1 - Oublier le cas de base.
### Corrigé exercice 6
- Méthode : expliciter chaque étape de séparer tête et reste avant de conclure par `8`.
- Résultat : la méthode robuste est choisie et justifiée.
- Contrôle : identifier pourquoi « Faire un appel récursif qui ne rapproche pas du cas de base. » est une erreur.
- Erreur traitée : EF2 - Faire un appel récursif qui ne rapproche pas du cas de base.
### Corrigé exercice 7
- Méthode : comparer la donnée avec le cas limite « reste vide » et valider `2`.
- Résultat : la justification reste valable sur le nouveau cas.
- Contrôle : inclure une étape calculable par un pair.
- Erreur traitée : EF3 - Confondre valeur retournée et affichage des appels.
### Corrigé exercice 8
- Méthode : isoler l’erreur fréquente « Ne pas traiter l’entrée vide. » puis reprendre la procédure correcte.
- Résultat : l’erreur est localisée puis réparée.
- Contrôle : proposer une activité corrective inspirée de « Tester d’abord la liste vide ou `n = 0`. ».
- Erreur traitée : EF4 - Ne pas traiter l’entrée vide.
## Erreurs fréquentes
- Erreur fréquente EF1 - Oublier le cas de base.
- Erreur fréquente EF2 - Faire un appel récursif qui ne rapproche pas du cas de base.
- Erreur fréquente EF3 - Confondre valeur retournée et affichage des appels.
- Erreur fréquente EF4 - Ne pas traiter l’entrée vide.

## Remédiation ciblée
- Activité corrective EF1 : Encadrer le cas de base avant d’écrire l’appel récursif.
- Activité corrective EF2 : Tracer la valeur de l’argument à chaque appel.
- Activité corrective EF3 : Dessiner la pile d’appels avec valeurs de retour.
- Activité corrective EF4 : Tester d’abord la liste vide ou `n = 0`.

## Différenciation
- Socle : traiter `4!` avec une fiche méthode fournie.
- Standard : traiter `[4, 1, 3]` en rédigeant la justification complète.
- Expert : inventer un cas limite lié à « reste vide » et expliquer le comportement attendu.

## Critères de réussite
- La capacité officielle est citée dans la copie.
- La méthode contient au moins une étape vérifiable par un pair.
- Le cas limite est discuté avec une donnée concrète.
- La correction explique quelle erreur fréquente est évitée.
