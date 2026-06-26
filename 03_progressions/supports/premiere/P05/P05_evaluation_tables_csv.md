---
title: "P05 - Evaluation - Tables CSV"
level: "premiere"
sequence_id: "P05"
document_type: "evaluation"
status: "needs_review"
version: "0.4.1"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Traitement de tables"
notion: "table, CSV, filtrage, agrégation"
objectifs:
  - "Objectif O1 - Identifier précisément la représentation ou la structure en jeu"
  - "Objectif O2 - Appliquer une méthode disciplinaire complète"
  - "Objectif O3 - Justifier le résultat sur un cas différent"
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur observée"
private_data: false
official_program:
  capacities:
    - "P-TABLE-01"
---


# P05 - Évaluation courte - Tables CSV

## Objectifs spécifiques
- Objectif O1 - Identifier précisément la représentation ou la structure en jeu.
- Objectif O2 - Appliquer une méthode disciplinaire complète.
- Objectif O3 - Justifier le résultat sur un cas différent.
- Objectif O4 - Contrôler un cas limite et corriger une erreur observée.

## Capacités officielles atomiques
- P-TABLE-01

## Prérequis
- Reconnaître une consigne liée à table.
- Distinguer donnée, méthode et conclusion dans le thème Traitement de tables.
- Rédiger une justification courte en utilisant le vocabulaire du programme.
- Contrôler une réponse par un cas limite ou un contre-exemple explicite.

## Séance(s) correspondante(s)
- P05-S1 à P05-S7 : support rattaché aux séances prêtes de la progression.

## Situation-problème concrète
Un fichier CSV de mesures contient des lignes incomplètes, des séparateurs et des valeurs numériques à agréger.

## Activité d’entrée
1. Lire une ligne d’en-tête.
2. Filtrer les lignes où `ville == "Tunis"`.
3. Calculer une moyenne de températures valides.
4. Signaler une ligne avec champ manquant.

## Questions
### Question 1
- Objectif évalué : O1.
- Capacité officielle : P-TABLE-01.
- Énoncé : résoudre lecture CSV avec `ville,temp
Tunis,24`.
- Réponse attendue : une ligne exploitable.
- Critère de réussite : méthode visible, résultat correct et contrôle « fichier vide ».
### Question 2
- Objectif évalué : O2.
- Capacité officielle : P-TABLE-01.
- Énoncé : expliquer filtrage à partir de trois villes dont deux Tunis.
- Réponse attendue : deux lignes sélectionnées.
- Critère de réussite : méthode visible, résultat correct et contrôle « aucune ligne retenue ».
### Question 3
- Objectif évalué : O3.
- Capacité officielle : P-TABLE-01.
- Énoncé : comparer agrégation avec `24`, `26`, champ vide.
- Réponse attendue : `25`.
- Critère de réussite : méthode visible, résultat correct et contrôle « division par zéro ».
### Question 4
- Objectif évalué : O4.
- Capacité officielle : P-TABLE-01.
- Énoncé : corriger jointure simple pour table villes et table régions.
- Réponse attendue : ville enrichie par région.
- Critère de réussite : méthode visible, résultat correct et contrôle « clé inconnue ».
## Barème
- Question 1 : 2 points méthode, 1 point résultat, 1 point justification liée à fichier vide.
- Question 2 : 2 points méthode, 1 point résultat, 1 point justification liée à aucune ligne retenue.
- Question 3 : 2 points méthode, 1 point résultat, 1 point justification liée à division par zéro.
- Question 4 : 2 points méthode, 1 point résultat, 1 point justification liée à clé inconnue.
## Erreurs fréquentes
- Erreur fréquente EF1 - Traiter l’en-tête comme une donnée.
- Erreur fréquente EF2 - Comparer une valeur numérique restée chaîne.
- Erreur fréquente EF3 - Diviser par zéro après filtrage vide.
- Erreur fréquente EF4 - Ignorer silencieusement une ligne mal formée.

## Remédiation ciblée
- Activité corrective EF1 : Marquer l’en-tête et commencer les données à la ligne suivante.
- Activité corrective EF2 : Convertir explicitement avant les comparaisons numériques.
- Activité corrective EF3 : Tester la taille de la sélection avant la moyenne.
- Activité corrective EF4 : Isoler les lignes invalides dans une liste de rejets.

## Différenciation
- Socle : traiter `ville,temp
Tunis,24` avec une fiche méthode fournie.
- Standard : traiter trois villes dont deux Tunis en rédigeant la justification complète.
- Expert : inventer un cas limite lié à « division par zéro » et expliquer le comportement attendu.

## Critères de réussite
- La capacité officielle est citée dans la copie.
- La méthode contient au moins une étape vérifiable par un pair.
- Le cas limite est discuté avec une donnée concrète.
- La correction explique quelle erreur fréquente est évitée.

## Exercices numérotés
- Exercice 1 : reprendre question 1 en explicitant donnée, méthode, résultat et contrôle pour P05.
- Exercice 2 : reprendre question 2 en explicitant donnée, méthode, résultat et contrôle pour P05.
- Exercice 3 : reprendre question 3 en explicitant donnée, méthode, résultat et contrôle pour P05.
- Exercice 4 : reprendre question 4 en explicitant donnée, méthode, résultat et contrôle pour P05.

## Corrigé
### Corrigé question 1
- Résultat attendu : une ligne exploitable.
- Méthode exigée : reprendre la démarche du cours puis vérifier le cas limite de la question 1.
- Critère de validation : méthode visible, résultat correct et contrôle « fichier vide ».
### Corrigé question 2
- Résultat attendu : deux lignes sélectionnées.
- Méthode exigée : reprendre la démarche du cours puis vérifier le cas limite de la question 2.
- Critère de validation : méthode visible, résultat correct et contrôle « aucune ligne retenue ».
### Corrigé question 3
- Résultat attendu : `25`.
- Méthode exigée : reprendre la démarche du cours puis vérifier le cas limite de la question 3.
- Critère de validation : méthode visible, résultat correct et contrôle « division par zéro ».
### Corrigé question 4
- Résultat attendu : ville enrichie par région.
- Méthode exigée : reprendre la démarche du cours puis vérifier le cas limite de la question 4.
- Critère de validation : méthode visible, résultat correct et contrôle « clé inconnue ».
