---
title: "P05 - Corrige - Tables CSV"
level: "premiere"
sequence_id: "P05"
document_type: "corrige"
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


# P05 - Corrigé professeur - Tables CSV

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

## Méthode générale de correction
- Point 1 : pour lecture CSV, exiger la donnée `PAYS,CAPITALE,CONTINENT,POPULATION
Allemagne,Berlin,Europe,82801531`, la méthode « lire avec csv.reader puis convertir POPULATION en int » et le contrôle « fichier pays_monde.csv vide ».
- Point 2 : pour filtrage, exiger la donnée un extrait contenant Allemagne, Albanie et Brésil, la méthode « conserver les lignes dont CONTINENT vaut Europe » et le contrôle « aucun pays du continent demandé ».
- Point 3 : pour traitement numérique des populations, exiger la donnée `82801531`, `3063320`, valeur `invalide`, la méthode « isoler une ligne invalide avant conversion de POPULATION en int » et le contrôle « sélection vide avant tri numérique ».
- Point 4 : pour tri par continent puis population, exiger la donnée lignes regroupées par CONTINENT, la méthode « associer par une clé commune » et le contrôle « continent absent ».
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

## Corrigé
### Corrigé exercice 1
- Méthode : identifier `PAYS,CAPITALE,CONTINENT,POPULATION
Allemagne,Berlin,Europe,82801531`, appliquer la méthode « lire avec csv.reader puis convertir POPULATION en int », puis écrire une ligne exploitable.
- Résultat : une ligne exploitable.
- Contrôle : faire apparaître le contrôle « fichier pays_monde.csv vide ».
- Erreur traitée : EF1 - Traiter l’en-tête comme une donnée.
### Corrigé exercice 2
- Méthode : expliciter chaque étape de conserver les lignes dont CONTINENT vaut Europe avant de conclure par deux lignes européennes sélectionnées.
- Résultat : deux lignes européennes sélectionnées.
- Contrôle : rédiger la méthode avant le résultat.
- Erreur traitée : EF2 - Comparer une valeur numérique restée chaîne.
### Corrigé exercice 3
- Méthode : comparer la donnée avec le cas limite « sélection vide avant tri numérique » et valider le rejet de la ligne invalide avant conversion.
- Résultat : ligne invalide isolée avant conversion.
- Contrôle : comparer avec le cas « sélection vide avant tri numérique ».
- Erreur traitée : EF3 - Diviser par zéro après filtrage vide.
### Corrigé exercice 4
- Méthode : isoler l’erreur fréquente « Ignorer silencieusement une ligne mal formée. » puis reprendre la procédure correcte.
- Résultat : pays triés par CONTINENT puis POPULATION.
- Contrôle : corriger l’erreur « Ignorer silencieusement une ligne mal formée. ».
- Erreur traitée : EF4 - Ignorer silencieusement une ligne mal formée.
### Corrigé exercice 5
- Méthode : identifier `PAYS,CAPITALE,CONTINENT,POPULATION
Allemagne,Berlin,Europe,82801531`, appliquer la méthode « lire avec csv.reader puis convertir POPULATION en int », puis écrire une ligne exploitable.
- Résultat : le comportement de lecture CSV est contrôlé.
- Contrôle : nommer la donnée minimale et la conclusion.
- Erreur traitée : EF1 - Traiter l’en-tête comme une donnée.
### Corrigé exercice 6
- Méthode : expliciter chaque étape de conserver les lignes dont CONTINENT vaut Europe avant de conclure par deux lignes européennes sélectionnées.
- Résultat : la méthode robuste est choisie et justifiée.
- Contrôle : identifier pourquoi « Comparer une valeur numérique restée chaîne. » est une erreur.
- Erreur traitée : EF2 - Comparer une valeur numérique restée chaîne.
### Corrigé exercice 7
- Méthode : comparer la donnée avec le cas limite « sélection vide avant tri numérique » et valider le rejet de la ligne invalide avant conversion.
- Résultat : la justification reste valable sur le nouveau cas.
- Contrôle : inclure une étape calculable par un pair.
- Erreur traitée : EF3 - Diviser par zéro après filtrage vide.
### Corrigé exercice 8
- Méthode : isoler l’erreur fréquente « Ignorer silencieusement une ligne mal formée. » puis reprendre la procédure correcte.
- Résultat : l’erreur est localisée puis réparée.
- Contrôle : proposer une activité corrective inspirée de « Isoler les lignes invalides dans une liste de rejets. ».
- Erreur traitée : EF4 - Ignorer silencieusement une ligne mal formée.

## Barème de correction rapide
- Exercice 1 : 1 point méthode, 0,5 point résultat, 0,5 point contrôle sur « faire apparaître le contrôle « fichier pays_monde.csv vide » ».
- Exercice 2 : 1 point méthode, 0,5 point résultat, 0,5 point contrôle sur « rédiger la méthode avant le résultat ».
- Exercice 3 : 1 point méthode, 0,5 point résultat, 0,5 point contrôle sur « comparer avec le cas « sélection vide avant tri numérique » ».
- Exercice 4 : 1 point méthode, 0,5 point résultat, 0,5 point contrôle sur « corriger l’erreur « Ignorer silencieusement une ligne mal formée. » ».
- Exercice 5 : 1 point méthode, 0,5 point résultat, 0,5 point contrôle sur « nommer la donnée minimale et la conclusion ».
- Exercice 6 : 1 point méthode, 0,5 point résultat, 0,5 point contrôle sur « identifier pourquoi « Comparer une valeur numérique restée chaîne. » est une erreur ».
- Exercice 7 : 1 point méthode, 0,5 point résultat, 0,5 point contrôle sur « inclure une étape calculable par un pair ».
- Exercice 8 : 1 point méthode, 0,5 point résultat, 0,5 point contrôle sur « proposer une activité corrective inspirée de « Isoler les lignes invalides dans une liste de rejets. » ».
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
