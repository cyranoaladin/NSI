---
title: "P05 - Td - Tables CSV"
level: "premiere"
sequence_id: "P05"
document_type: "td"
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

# P05 - TD - Tables CSV

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
Un fichier CSV de pays contient des champs `PAYS`, `CAPITALE`, `CONTINENT`, `POPULATION`. L'extrait utilisé en classe est adapté depuis `Documents_DRIVE/2_NSI/Cours/Première NSI Pierrot caillabet/1_2019-2020/1_Cours/11_traitement de tables/pays_monde.csv`, sans donnée personnelle.

## Activité d’entrée
1. Lire l’en-tête `PAYS,CAPITALE,CONTINENT,POPULATION`.
2. Filtrer les lignes où `CONTINENT == "Europe"`.
3. Calculer la population totale d’un petit extrait européen.
4. Signaler une ligne dont la population n’est pas convertible en entier.

## Source de données utilisée

Le fichier élève normalisé est `03_progressions/supports/premiere/P05/data/pays_monde_extrait.csv`. Il contient uniquement des pays, capitales, continents et populations : aucune donnée élève, aucune note, aucun identifiant personnel.

## Exemples corrigés précis
### Exemple corrigé 1 - lecture CSV
- Donnée étudiée : `PAYS,CAPITALE,CONTINENT,POPULATION` puis `Allemagne,Berlin,Europe,82801531`.
- Méthode : lire l’en-tête, associer chaque champ à sa valeur, convertir `POPULATION` en entier.
- Résultat obtenu : `{"PAYS": "Allemagne", "CAPITALE": "Berlin", "CONTINENT": "Europe", "POPULATION": 82801531}`.
- Contrôle : le cas limite « fichier pays_monde.csv vide » est vérifié séparément.
### Exemple corrigé 2 - filtrage
- Donnée étudiée : Allemagne, Albanie, Brésil.
- Méthode : conserver les lignes dont `CONTINENT` vaut exactement `Europe`.
- Résultat obtenu : Allemagne et Albanie sont retenues ; Brésil est exclu.
- Contrôle : le cas limite « aucun pays du continent demandé » est vérifié séparément.
### Exemple corrigé 3 - traitement numérique des populations
- Donnée étudiée : populations Allemagne `82801531`, Albanie `3063320`, Andorre `77281`.
- Méthode : convertir les trois populations en entiers puis additionner.
- Résultat obtenu : `85942132`.
- Contrôle : le cas limite « sélection vide avant tri numérique » est vérifié séparément.
### Exemple corrigé 4 - tri par continent puis population
- Donnée étudiée : lignes regroupées par CONTINENT.
- Méthode : associer par une clé commune.
- Résultat obtenu : pays triés par CONTINENT puis POPULATION.
- Contrôle : le cas limite « continent absent » est vérifié séparément.
## Exercices numérotés
### Exercice 1
- Objectif travaillé : O1.
- Capacité officielle : P-TABLE-01.
- Énoncé disciplinaire : résoudre la lecture de `Allemagne,Berlin,Europe,82801531`.
- Production attendue : dictionnaire typé avec population entière.
- Contrainte de contrôle : faire apparaître le contrôle « fichier pays_monde.csv vide ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 2
- Objectif travaillé : O2.
- Capacité officielle : P-TABLE-01.
- Énoncé disciplinaire : expliquer le filtrage Europe sur Allemagne, Albanie et Brésil.
- Production attendue : deux lignes européennes sélectionnées.
- Contrainte de contrôle : rédiger la méthode avant le résultat.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 3
- Objectif travaillé : O3.
- Capacité officielle : P-TABLE-01.
- Énoncé disciplinaire : contrôler et convertir les populations Allemagne, Albanie, Andorre.
- Production attendue : `85942132`.
- Contrainte de contrôle : comparer avec le cas « sélection vide avant tri numérique ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 4
- Objectif travaillé : O4.
- Capacité officielle : P-TABLE-01.
- Énoncé disciplinaire : corriger tri par continent puis population pour lignes regroupées par CONTINENT.
- Production attendue : pays triés par CONTINENT puis POPULATION.
- Contrainte de contrôle : corriger l’erreur « Ignorer silencieusement une ligne mal formée. ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 5
- Objectif travaillé : O1.
- Capacité officielle : P-TABLE-01.
- Énoncé disciplinaire : tester un cas limite lié à fichier pays_monde.csv vide.
- Production attendue : le comportement de lecture CSV est contrôlé.
- Contrainte de contrôle : nommer la donnée minimale et la conclusion.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 6
- Objectif travaillé : O2.
- Capacité officielle : P-TABLE-01.
- Énoncé disciplinaire : classer deux méthodes possibles pour filtrage.
- Production attendue : la méthode robuste est choisie et justifiée.
- Contrainte de contrôle : identifier pourquoi « Comparer une valeur numérique restée chaîne. » est une erreur.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 7
- Objectif travaillé : O3.
- Capacité officielle : P-TABLE-01.
- Énoncé disciplinaire : justifier un transfert qui utilise traitement numérique des populations avec une donnée nouvelle.
- Production attendue : la justification reste valable sur le nouveau cas.
- Contrainte de contrôle : inclure une étape calculable par un pair.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 8
- Objectif travaillé : O4.
- Capacité officielle : P-TABLE-01.
- Énoncé disciplinaire : étendre un énoncé volontairement erroné sur tri par continent puis population.
- Production attendue : l’erreur est localisée puis réparée.
- Contrainte de contrôle : proposer une activité corrective inspirée de « Isoler les lignes invalides dans une liste de rejets. ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
## Corrigé
### Corrigé exercice 1
- Méthode : identifier l’en-tête, associer Allemagne à Berlin, Europe et `82801531`, puis convertir la population.
- Résultat : `{"PAYS": "Allemagne", "CAPITALE": "Berlin", "CONTINENT": "Europe", "POPULATION": 82801531}`.
- Contrôle : faire apparaître le contrôle « fichier pays_monde.csv vide ».
- Erreur traitée : EF1 - Traiter l’en-tête comme une donnée.
### Corrigé exercice 2
- Méthode : tester `CONTINENT == "Europe"` pour Allemagne, Albanie et Brésil.
- Résultat : Allemagne et Albanie sont sélectionnées ; Brésil ne l’est pas.
- Contrôle : rédiger la méthode avant le résultat.
- Erreur traitée : EF2 - Comparer une valeur numérique restée chaîne.
### Corrigé exercice 3
- Méthode : calculer `82801531 + 3063320 + 77281`.
- Résultat : `85942132`.
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
