---
title: "T04 - Evaluation - Récursivité"
level: "terminale"
sequence_id: "T04"
document_type: "evaluation"
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
    - "T-LANG-02B"
---


# T04 - Évaluation courte - Récursivité

## Objectifs spécifiques
- Objectif O1 - Identifier précisément la représentation ou la structure en jeu.
- Objectif O2 - Appliquer une méthode disciplinaire complète.
- Objectif O3 - Justifier le résultat sur un cas différent.
- Objectif O4 - Contrôler un cas limite et corriger une erreur observée.

## Capacités officielles atomiques
- T-LANG-02A
- T-LANG-02B

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

## Questions
### Question 1
- Objectif évalué : O1.
- Capacité officielle : T-LANG-02A.
- Énoncé : résoudre factorielle avec `4!`.
- Réponse attendue : `24`.
- Critère de réussite : méthode visible, résultat correct et contrôle « entier négatif refusé ».
### Question 2
- Objectif évalué : O2.
- Capacité officielle : T-LANG-02A.
- Énoncé : expliquer somme de liste à partir de `[4, 1, 3]`.
- Réponse attendue : `8`.
- Critère de réussite : méthode visible, résultat correct et contrôle « liste vide ».
### Question 3
- Objectif évalué : O3.
- Capacité officielle : T-LANG-02A.
- Énoncé : comparer longueur avec `["a", "b"]`.
- Réponse attendue : `2`.
- Critère de réussite : méthode visible, résultat correct et contrôle « reste vide ».
### Question 4
- Objectif évalué : O4.
- Capacité officielle : T-LANG-02A, T-LANG-02B.
- Énoncé : soit `def decompte(n): print(n); return decompte(n - 1)`. Tracer les 3 premiers appels pour `decompte(2)` (valeur de `n` à chaque appel). Identifier le problème de terminaison, corriger la fonction, donner le variant.
- Réponse attendue : trace `n=2, n=1, n=0` ; cas de base `if n == 0: return` ; variant = `n`.
- Critère de réussite : trace d'appels correcte, cas de base identifié, variant explicité et contrôle « appel avec même argument ».
## Barème
- Question 1 : 2 points méthode, 1 point résultat, 1 point justification liée à entier négatif refusé.
- Question 2 : 2 points méthode, 1 point résultat, 1 point justification liée à liste vide.
- Question 3 : 2 points méthode, 1 point résultat, 1 point justification liée à reste vide.
- Question 4 : 2 points méthode, 1 point résultat, 1 point justification liée à appel avec même argument.
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

## Exercices numérotés
- Exercice 1 : reprendre question 1 en explicitant donnée, méthode, résultat et contrôle pour T04.
- Exercice 2 : reprendre question 2 en explicitant donnée, méthode, résultat et contrôle pour T04.
- Exercice 3 : reprendre question 3 en explicitant donnée, méthode, résultat et contrôle pour T04.
- Exercice 4 : reprendre question 4 en explicitant donnée, méthode, résultat et contrôle pour T04.

## Corrigé
### Corrigé question 1
- Résultat attendu : `24`.
- Méthode exigée : reprendre la démarche du cours puis vérifier le cas limite de la question 1.
- Critère de validation : méthode visible, résultat correct et contrôle « entier négatif refusé ».
### Corrigé question 2
- Résultat attendu : `8`.
- Méthode exigée : reprendre la démarche du cours puis vérifier le cas limite de la question 2.
- Critère de validation : méthode visible, résultat correct et contrôle « liste vide ».
### Corrigé question 3
- Résultat attendu : `2`.
- Méthode exigée : reprendre la démarche du cours puis vérifier le cas limite de la question 3.
- Critère de validation : méthode visible, résultat correct et contrôle « reste vide ».
### Corrigé question 4
- Résultat attendu : preuve de terminaison.
- Méthode exigée : reprendre la démarche du cours puis vérifier le cas limite de la question 4.
- Critère de validation : méthode visible, résultat correct et contrôle « appel avec même argument ».

## Modalités de passation
- Durée : 25 minutes.
- Matériel autorisé : fiche récursivité, sans corrigé distribué ni navigation externe.
- Capacités évaluées :
- T-LANG-02A
- T-LANG-02B

## Fiche liée et aménagement
- Fiche liée : fiche de cours opérationnelle de la séquence T04, statut `needs_review`.
- Séance liée : `T04-S1`, avec question centrée sur cas de base et terminaison.
- Version aménagée : données cas de base et terminaison surlignées et tableau réponse en trois zones.
- Remédiation : écrire la trace de trois appels récursifs, puis verbaliser la méthode en binôme.

