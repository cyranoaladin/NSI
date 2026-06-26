---
title: "P05 - Remediation - Tables CSV"
level: "premiere"
sequence_id: "P05"
document_type: "remediation"
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


# P05 - Remédiation - Tables CSV

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

### Remédiation EF1
- Erreur fréquente EF1 - Traiter l’en-tête comme une donnée.
- Diagnostic : refaire lecture CSV avec `PAYS,CAPITALE,CONTINENT,POPULATION
Allemagne,Berlin,Europe,82801531` et repérer l’étape fautive.
- Activité corrective EF1 : Marquer l’en-tête et commencer les données à la ligne suivante.
- Nouvelle tâche : produire une réponse sur un cas voisin qui vérifie « fichier pays_monde.csv vide ».
- Critère de sortie : l’élève explique la correction sans reprendre la phrase du cours.
### Remédiation EF2
- Erreur fréquente EF2 - Comparer une valeur numérique restée chaîne.
- Diagnostic : refaire filtrage avec un extrait contenant Allemagne, Albanie et Brésil et repérer l’étape fautive.
- Activité corrective EF2 : Convertir explicitement avant les comparaisons numériques.
- Nouvelle tâche : produire une réponse sur un cas voisin qui vérifie « aucun pays du continent demandé ».
- Critère de sortie : l’élève explique la correction sans reprendre la phrase du cours.
### Remédiation EF3
- Erreur fréquente EF3 - Diviser par zéro après filtrage vide.
- Diagnostic : refaire traitement numérique des populations avec `82801531`, `3063320`, valeur `invalide` et repérer l’étape fautive.
- Activité corrective EF3 : Tester la sélection avant le tri numérique.
- Nouvelle tâche : produire une réponse sur un cas voisin qui vérifie « sélection vide avant tri numérique ».
- Critère de sortie : l’élève explique la correction sans reprendre la phrase du cours.
### Remédiation EF4
- Erreur fréquente EF4 - Ignorer silencieusement une ligne mal formée.
- Diagnostic : refaire tri par continent puis population avec lignes regroupées par CONTINENT et repérer l’étape fautive.
- Activité corrective EF4 : Isoler les lignes invalides dans une liste de rejets.
- Nouvelle tâche : produire une réponse sur un cas voisin qui vérifie « continent absent ».
- Critère de sortie : l’élève explique la correction sans reprendre la phrase du cours.
## Exercices numérotés
- Exercice 1 : résoudre lecture CSV avec `PAYS,CAPITALE,CONTINENT,POPULATION
Allemagne,Berlin,Europe,82801531` ; attendu : une ligne exploitable.
- Exercice 2 : expliquer filtrage à partir de un extrait contenant Allemagne, Albanie et Brésil ; attendu : deux lignes européennes sélectionnées.
- Exercice 3 : comparer traitement numérique des populations avec `82801531`, `3063320`, valeur `invalide` ; attendu : ligne invalide isolée avant conversion.
- Exercice 4 : corriger tri par continent puis population pour lignes regroupées par CONTINENT ; attendu : pays triés par CONTINENT puis POPULATION.
- Exercice 5 : tester un cas limite lié à fichier pays_monde.csv vide ; attendu : le comportement de lecture CSV est contrôlé.
- Exercice 6 : classer deux méthodes possibles pour filtrage ; attendu : la méthode robuste est choisie et justifiée.
- Exercice 7 : justifier un transfert qui utilise traitement numérique des populations avec une donnée nouvelle ; attendu : la justification reste valable sur le nouveau cas.
- Exercice 8 : étendre un énoncé volontairement erroné sur tri par continent puis population ; attendu : l’erreur est localisée puis réparée.

## Corrigés complets des exercices du cours
- Corrigé exercice 1 : méthode : identifier `PAYS,CAPITALE,CONTINENT,POPULATION
Allemagne,Berlin,Europe,82801531`, appliquer la méthode « lire avec csv.reader puis convertir POPULATION en int », puis écrire une ligne exploitable ; résultat : une ligne exploitable ; contrôle : faire apparaître le contrôle « fichier pays_monde.csv vide ».
- Corrigé exercice 2 : méthode : expliciter chaque étape de conserver les lignes dont CONTINENT vaut Europe avant de conclure par deux lignes européennes sélectionnées ; résultat : deux lignes européennes sélectionnées ; contrôle : rédiger la méthode avant le résultat.
- Corrigé exercice 3 : méthode : comparer la donnée avec le cas limite « sélection vide avant tri numérique » et valider le rejet de la ligne invalide avant conversion ; résultat : ligne invalide isolée avant conversion ; contrôle : comparer avec le cas « sélection vide avant tri numérique ».
- Corrigé exercice 4 : méthode : isoler l’erreur fréquente « Ignorer silencieusement une ligne mal formée. » puis reprendre la procédure correcte ; résultat : pays triés par CONTINENT puis POPULATION ; contrôle : corriger l’erreur « Ignorer silencieusement une ligne mal formée. ».
- Corrigé exercice 5 : méthode : identifier `PAYS,CAPITALE,CONTINENT,POPULATION
Allemagne,Berlin,Europe,82801531`, appliquer la méthode « lire avec csv.reader puis convertir POPULATION en int », puis écrire une ligne exploitable ; résultat : le comportement de lecture CSV est contrôlé ; contrôle : nommer la donnée minimale et la conclusion.
- Corrigé exercice 6 : méthode : expliciter chaque étape de conserver les lignes dont CONTINENT vaut Europe avant de conclure par deux lignes européennes sélectionnées ; résultat : la méthode robuste est choisie et justifiée ; contrôle : identifier pourquoi « Comparer une valeur numérique restée chaîne. » est une erreur.
- Corrigé exercice 7 : méthode : comparer la donnée avec le cas limite « sélection vide avant tri numérique » et valider le rejet de la ligne invalide avant conversion ; résultat : la justification reste valable sur le nouveau cas ; contrôle : inclure une étape calculable par un pair.
- Corrigé exercice 8 : méthode : isoler l’erreur fréquente « Ignorer silencieusement une ligne mal formée. » puis reprendre la procédure correcte ; résultat : l’erreur est localisée puis réparée ; contrôle : proposer une activité corrective inspirée de « Isoler les lignes invalides dans une liste de rejets. ».

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
