---
title: "P05 - Tp - Tables CSV"
level: "premiere"
sequence_id: "P05"
document_type: "tp"
status: "needs_review"
version: "0.4.1"
source: "BO 2019"
source_creation: "adapted_from_drive"
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


# P05 - TP - Tables CSV

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
Un extrait CSV de pays contient `PAYS`, `CAPITALE`, `CONTINENT`, `POPULATION`. Il est adapté depuis `Documents_DRIVE/2_NSI/Cours/Première NSI Pierrot caillabet/1_2019-2020/1_Cours/11_traitement de tables/pays_monde.csv`, sans donnée personnelle.

## Activité d’entrée
1. Charger `data/pays_monde_extrait.csv`.
2. Filtrer les pays européens de l’extrait.
3. Calculer la population totale de ces pays.
4. Rejeter explicitement une ligne dont `POPULATION` n’est pas un entier.

## Donnée fournie

- Fichier élève : `data/pays_monde_extrait.csv`.
- Origine : ressource Drive `pays_monde.csv`, reprise partiellement et normalisée.
- Champs attendus : `PAYS`, `CAPITALE`, `CONTINENT`, `POPULATION`.
- Résultat de contrôle sur l’extrait : les pays européens Allemagne, Albanie et Andorre totalisent `85942132` habitants.

## Consigne technique détaillée
- Problème à programmer : Lire pays_monde.csv avec csv.reader et csv.DictReader, filtrer par CONTINENT, convertir POPULATION en int, comparer tri numérique et tri lexicographique, puis isoler une ligne invalide.
- Starter code : `code/P05_starter_tables_csv.py`.
- Tests attendus : `code/P05_tests_attendus_tables_csv.py`.
- Corrigé professeur séparé : `code/P05_corrige_professeur_tables_csv.py`.
- Livrable vérifiable : fichier Python complété, sortie de tests nominal, limite et invalide, puis commentaire de deux lignes sur le cas limite.
- Exemple d’exécution : lancer les tests avec `TP_MODULE` pointant vers le module à contrôler.
- Cas limite principal : fichier pays_monde.csv vide.
## Étapes de réalisation
- Étape 1 : coder ou tester la lecture de `Allemagne,Berlin,Europe,82801531`, puis contrôler fichier pays_monde.csv vide.
- Étape 2 : coder ou tester le filtrage du continent Europe, puis contrôler aucun pays du continent demandé.
- Étape 3 : coder ou tester le traitement numérique des populations `82801531 + 3063320 + 77281`, puis contrôler sélection vide avant tri numérique ou sélection vide.
- Étape 4 : coder ou tester tri par continent puis population à partir de lignes regroupées par CONTINENT, puis contrôler continent absent.
## Tests attendus
- Test nominal : donnée ordinaire issue du premier exemple.
- Test limite : entrée minimale, vide ou borne de représentation.
- Test invalide : type ou valeur explicitement refusé par la spécification.
## Exercices numérotés
- Exercice 1 : résoudre la lecture CSV de `Allemagne,Berlin,Europe,82801531` ; attendu : dictionnaire typé.
- Exercice 2 : expliquer le filtrage Europe sur Allemagne, Albanie, Brésil ; attendu : deux lignes européennes sélectionnées.
- Exercice 3 : comparer le traitement numérique des populations des populations Allemagne, Albanie, Andorre ; attendu : `85942132`.
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

## Validation opérationnelle du TP
- Vérification P05-1 : exécuter le starter et constater au moins un échec de test nominal.
- Vérification P05-2 : exécuter le corrigé professeur et obtenir les trois catégories de tests au vert.
- Vérification P05-3 : modifier une entrée limite et expliquer pourquoi le résultat reste contrôlable.
- Vérification P05-4 : refuser explicitement une entrée invalide au lieu de produire une valeur arbitraire.
- Vérification P05-5 : joindre au livrable la commande exécutée et la sortie courte des tests.
- Vérification P05-6 : comparer l’algorithme écrit avec la capacité officielle citée.
