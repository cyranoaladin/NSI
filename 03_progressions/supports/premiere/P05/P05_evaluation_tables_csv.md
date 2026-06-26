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
notion: "table, CSV, filtrage, traitement numérique des populations"
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
Le fichier `pays_monde.csv` contient des pays, capitales, continents et populations à lire, filtrer, convertir et trier.

## Activité d’entrée
1. Lire une ligne d’en-tête.
2. Filtrer les lignes où `CONTINENT == "Europe"`.
3. Convertir puis trier numériquement les populations valides.
4. Signaler une ligne avec champ manquant.

## Questions
### Question 1
- Objectif évalué : O1.
- Capacité officielle : P-TABLE-01.
- Énoncé : résoudre lecture CSV avec `PAYS,CAPITALE,CONTINENT,POPULATION
Allemagne,Berlin,Europe,82801531`.
- Réponse attendue : une ligne exploitable.
- Critère de réussite : méthode visible, résultat correct et contrôle « fichier pays_monde.csv vide ».
### Question 2
- Objectif évalué : O2.
- Capacité officielle : P-TABLE-01.
- Énoncé : expliquer filtrage à partir de un extrait contenant Allemagne, Albanie et Brésil.
- Réponse attendue : deux lignes européennes sélectionnées.
- Critère de réussite : méthode visible, résultat correct et contrôle « aucun pays du continent demandé ».
### Question 3
- Objectif évalué : O3.
- Capacité officielle : P-TABLE-01.
- Énoncé : comparer traitement numérique des populations avec `82801531`, `3063320`, valeur `invalide`.
- Réponse attendue : ligne invalide isolée avant conversion.
- Critère de réussite : méthode visible, résultat correct et contrôle « sélection vide avant tri numérique ».
### Question 4
- Objectif évalué : O4.
- Capacité officielle : P-TABLE-01.
- Énoncé : corriger tri par continent puis population pour lignes regroupées par CONTINENT.
- Réponse attendue : pays triés par CONTINENT puis POPULATION.
- Critère de réussite : méthode visible, résultat correct et contrôle « continent absent ».
## Barème
- Question 1 : 2 points méthode, 1 point résultat, 1 point justification liée à fichier pays_monde.csv vide.
- Question 2 : 2 points méthode, 1 point résultat, 1 point justification liée à aucun pays du continent demandé.
- Question 3 : 2 points méthode, 1 point résultat, 1 point justification liée à sélection vide avant tri numérique.
- Question 4 : 2 points méthode, 1 point résultat, 1 point justification liée à continent absent.
## Erreurs fréquentes
- Erreur fréquente EF1 - Traiter l’en-tête comme une donnée.
- Erreur fréquente EF2 - Comparer une valeur numérique restée chaîne.
- Erreur fréquente EF3 - Diviser par zéro après filtrage vide.
- Erreur fréquente EF4 - Ignorer silencieusement une ligne mal formée.

## Remédiation ciblée
- Activité corrective EF1 : Marquer l’en-tête et commencer les données à la ligne suivante.
- Activité corrective EF2 : Convertir explicitement avant les comparaisons numériques.
- Activité corrective EF3 : Tester la sélection avant le tri numérique.
- Activité corrective EF4 : Isoler les lignes invalides dans une liste de rejets.

## Différenciation
- Socle : traiter `PAYS,CAPITALE,CONTINENT,POPULATION
Allemagne,Berlin,Europe,82801531` avec une fiche méthode fournie.
- Standard : traiter un extrait contenant Allemagne, Albanie et Brésil en rédigeant la justification complète.
- Expert : inventer un cas limite lié à « sélection vide avant tri numérique » et expliquer le comportement attendu.

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
- Critère de validation : méthode visible, résultat correct et contrôle « fichier pays_monde.csv vide ».
### Corrigé question 2
- Résultat attendu : deux lignes européennes sélectionnées.
- Méthode exigée : reprendre la démarche du cours puis vérifier le cas limite de la question 2.
- Critère de validation : méthode visible, résultat correct et contrôle « aucun pays du continent demandé ».
### Corrigé question 3
- Résultat attendu : ligne invalide isolée avant conversion.
- Méthode exigée : reprendre la démarche du cours puis vérifier le cas limite de la question 3.
- Critère de validation : méthode visible, résultat correct et contrôle « sélection vide avant tri numérique ».
### Corrigé question 4
- Résultat attendu : pays triés par CONTINENT puis POPULATION.
- Méthode exigée : reprendre la démarche du cours puis vérifier le cas limite de la question 4.
- Critère de validation : méthode visible, résultat correct et contrôle « continent absent ».

## Modalités de passation
- Durée : 25 minutes.
- Matériel autorisé : fiche tables CSV, sans corrigé distribué ni navigation externe.
- Capacités évaluées :
- P-TABLE-01
- P-TABLE-01

## Fiche liée et aménagement
- Fiche liée : fiche de cours opérationnelle de la séquence P05, statut `needs_review`.
- Séance liée : `P05-S1`, avec question centrée sur import, cohérence et recherche.
- Version aménagée : données import, cohérence et recherche surlignées et tableau réponse en trois zones.
- Remédiation : contrôler une ligne CSV avec clé manquante, puis verbaliser la méthode en binôme.

