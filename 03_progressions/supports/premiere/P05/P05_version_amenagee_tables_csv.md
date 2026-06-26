---
title: "P05 - Version amenagee - Tables CSV"
level: "premiere"
sequence_id: "P05"
document_type: "version_amenagee"
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


# P05 - Version aménagée - Tables CSV

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

## Version aménagée - Énoncé élève
### Question aménagée 1
- Énoncé élève : traiter lecture CSV avec la donnée `ville,temp
Tunis,24`.
- Aide intégrée : commencer par séparer en-tête et données puis convertir la température.
- Espace de réponse : méthode : ______ ; résultat : ______ ; contrôle : ______.
- Point de vigilance : Traiter l’en-tête comme une donnée.
### Question aménagée 2
- Énoncé élève : traiter filtrage avec la donnée trois villes dont deux Tunis.
- Aide intégrée : commencer par conserver les lignes respectant un prédicat.
- Espace de réponse : méthode : ______ ; résultat : ______ ; contrôle : ______.
- Point de vigilance : Comparer une valeur numérique restée chaîne.
### Question aménagée 3
- Énoncé élève : traiter agrégation avec la donnée `24`, `26`, champ vide.
- Aide intégrée : commencer par ignorer ou signaler le champ vide avant moyenne.
- Espace de réponse : méthode : ______ ; résultat : ______ ; contrôle : ______.
- Point de vigilance : Diviser par zéro après filtrage vide.
### Question aménagée 4
- Énoncé élève : traiter jointure simple avec la donnée table villes et table régions.
- Aide intégrée : commencer par associer par une clé commune.
- Espace de réponse : méthode : ______ ; résultat : ______ ; contrôle : ______.
- Point de vigilance : Ignorer silencieusement une ligne mal formée.
## Exercices numérotés
- Exercice 1 : résoudre lecture CSV avec `ville,temp
Tunis,24` avec aide possible sur la méthode.
- Exercice 2 : expliquer filtrage à partir de trois villes dont deux Tunis avec aide possible sur la méthode.
- Exercice 3 : comparer agrégation avec `24`, `26`, champ vide avec aide possible sur la méthode.
- Exercice 4 : corriger jointure simple pour table villes et table régions avec aide possible sur la méthode.
- Exercice 5 : tester un cas limite lié à fichier vide avec aide possible sur la méthode.
- Exercice 6 : classer deux méthodes possibles pour filtrage avec aide possible sur la méthode.
- Exercice 7 : justifier un transfert qui utilise agrégation avec une donnée nouvelle avec aide possible sur la méthode.
- Exercice 8 : étendre un énoncé volontairement erroné sur jointure simple avec aide possible sur la méthode.
## Corrigés complets des exercices du cours
- Corrigé exercice 1 : méthode : identifier `ville,temp
Tunis,24`, appliquer la méthode « séparer en-tête et données puis convertir la température », puis écrire une ligne exploitable ; résultat : une ligne exploitable ; contrôle : faire apparaître le contrôle « fichier vide ».
- Corrigé exercice 2 : méthode : expliciter chaque étape de conserver les lignes respectant un prédicat avant de conclure par deux lignes sélectionnées ; résultat : deux lignes sélectionnées ; contrôle : rédiger la méthode avant le résultat.
- Corrigé exercice 3 : méthode : comparer la donnée avec le cas limite « division par zéro » et valider `25` ; résultat : `25` ; contrôle : comparer avec le cas « division par zéro ».
- Corrigé exercice 4 : méthode : isoler l’erreur fréquente « Ignorer silencieusement une ligne mal formée. » puis reprendre la procédure correcte ; résultat : ville enrichie par région ; contrôle : corriger l’erreur « Ignorer silencieusement une ligne mal formée. ».
- Corrigé exercice 5 : méthode : identifier `ville,temp
Tunis,24`, appliquer la méthode « séparer en-tête et données puis convertir la température », puis écrire une ligne exploitable ; résultat : le comportement de lecture CSV est contrôlé ; contrôle : nommer la donnée minimale et la conclusion.
- Corrigé exercice 6 : méthode : expliciter chaque étape de conserver les lignes respectant un prédicat avant de conclure par deux lignes sélectionnées ; résultat : la méthode robuste est choisie et justifiée ; contrôle : identifier pourquoi « Comparer une valeur numérique restée chaîne. » est une erreur.
- Corrigé exercice 7 : méthode : comparer la donnée avec le cas limite « division par zéro » et valider `25` ; résultat : la justification reste valable sur le nouveau cas ; contrôle : inclure une étape calculable par un pair.
- Corrigé exercice 8 : méthode : isoler l’erreur fréquente « Ignorer silencieusement une ligne mal formée. » puis reprendre la procédure correcte ; résultat : l’erreur est localisée puis réparée ; contrôle : proposer une activité corrective inspirée de « Isoler les lignes invalides dans une liste de rejets. ».

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
