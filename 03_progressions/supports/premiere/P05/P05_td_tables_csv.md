---
title: "P05 - Td - Tables CSV"
level: "premiere"
sequence_id: "P05"
document_type: "td"
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
Un fichier CSV de mesures contient des lignes incomplètes, des séparateurs et des valeurs numériques à agréger.

## Activité d’entrée
1. Lire une ligne d’en-tête.
2. Filtrer les lignes où `ville == "Tunis"`.
3. Calculer une moyenne de températures valides.
4. Signaler une ligne avec champ manquant.

## Exemples corrigés précis
### Exemple corrigé 1 - lecture CSV
- Donnée étudiée : `ville,temp
Tunis,24`.
- Méthode : séparer en-tête et données puis convertir la température.
- Résultat obtenu : une ligne exploitable.
- Contrôle : le cas limite « fichier vide » est vérifié séparément.
### Exemple corrigé 2 - filtrage
- Donnée étudiée : trois villes dont deux Tunis.
- Méthode : conserver les lignes respectant un prédicat.
- Résultat obtenu : deux lignes sélectionnées.
- Contrôle : le cas limite « aucune ligne retenue » est vérifié séparément.
### Exemple corrigé 3 - agrégation
- Donnée étudiée : `24`, `26`, champ vide.
- Méthode : ignorer ou signaler le champ vide avant moyenne.
- Résultat obtenu : `25`.
- Contrôle : le cas limite « division par zéro » est vérifié séparément.
### Exemple corrigé 4 - jointure simple
- Donnée étudiée : table villes et table régions.
- Méthode : associer par une clé commune.
- Résultat obtenu : ville enrichie par région.
- Contrôle : le cas limite « clé inconnue » est vérifié séparément.
## Exercices numérotés
### Exercice 1
- Objectif travaillé : O1.
- Capacité officielle : P-TABLE-01.
- Énoncé disciplinaire : résoudre lecture CSV avec `ville,temp
Tunis,24`.
- Production attendue : une ligne exploitable.
- Contrainte de contrôle : faire apparaître le contrôle « fichier vide ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 2
- Objectif travaillé : O2.
- Capacité officielle : P-TABLE-01.
- Énoncé disciplinaire : expliquer filtrage à partir de trois villes dont deux Tunis.
- Production attendue : deux lignes sélectionnées.
- Contrainte de contrôle : rédiger la méthode avant le résultat.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 3
- Objectif travaillé : O3.
- Capacité officielle : P-TABLE-01.
- Énoncé disciplinaire : comparer agrégation avec `24`, `26`, champ vide.
- Production attendue : `25`.
- Contrainte de contrôle : comparer avec le cas « division par zéro ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 4
- Objectif travaillé : O4.
- Capacité officielle : P-TABLE-01.
- Énoncé disciplinaire : corriger jointure simple pour table villes et table régions.
- Production attendue : ville enrichie par région.
- Contrainte de contrôle : corriger l’erreur « Ignorer silencieusement une ligne mal formée. ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 5
- Objectif travaillé : O1.
- Capacité officielle : P-TABLE-01.
- Énoncé disciplinaire : tester un cas limite lié à fichier vide.
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
- Énoncé disciplinaire : justifier un transfert qui utilise agrégation avec une donnée nouvelle.
- Production attendue : la justification reste valable sur le nouveau cas.
- Contrainte de contrôle : inclure une étape calculable par un pair.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 8
- Objectif travaillé : O4.
- Capacité officielle : P-TABLE-01.
- Énoncé disciplinaire : étendre un énoncé volontairement erroné sur jointure simple.
- Production attendue : l’erreur est localisée puis réparée.
- Contrainte de contrôle : proposer une activité corrective inspirée de « Isoler les lignes invalides dans une liste de rejets. ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
## Corrigé
### Corrigé exercice 1
- Méthode : identifier `ville,temp
Tunis,24`, appliquer la méthode « séparer en-tête et données puis convertir la température », puis écrire une ligne exploitable.
- Résultat : une ligne exploitable.
- Contrôle : faire apparaître le contrôle « fichier vide ».
- Erreur traitée : EF1 - Traiter l’en-tête comme une donnée.
### Corrigé exercice 2
- Méthode : expliciter chaque étape de conserver les lignes respectant un prédicat avant de conclure par deux lignes sélectionnées.
- Résultat : deux lignes sélectionnées.
- Contrôle : rédiger la méthode avant le résultat.
- Erreur traitée : EF2 - Comparer une valeur numérique restée chaîne.
### Corrigé exercice 3
- Méthode : comparer la donnée avec le cas limite « division par zéro » et valider `25`.
- Résultat : `25`.
- Contrôle : comparer avec le cas « division par zéro ».
- Erreur traitée : EF3 - Diviser par zéro après filtrage vide.
### Corrigé exercice 4
- Méthode : isoler l’erreur fréquente « Ignorer silencieusement une ligne mal formée. » puis reprendre la procédure correcte.
- Résultat : ville enrichie par région.
- Contrôle : corriger l’erreur « Ignorer silencieusement une ligne mal formée. ».
- Erreur traitée : EF4 - Ignorer silencieusement une ligne mal formée.
### Corrigé exercice 5
- Méthode : identifier `ville,temp
Tunis,24`, appliquer la méthode « séparer en-tête et données puis convertir la température », puis écrire une ligne exploitable.
- Résultat : le comportement de lecture CSV est contrôlé.
- Contrôle : nommer la donnée minimale et la conclusion.
- Erreur traitée : EF1 - Traiter l’en-tête comme une donnée.
### Corrigé exercice 6
- Méthode : expliciter chaque étape de conserver les lignes respectant un prédicat avant de conclure par deux lignes sélectionnées.
- Résultat : la méthode robuste est choisie et justifiée.
- Contrôle : identifier pourquoi « Comparer une valeur numérique restée chaîne. » est une erreur.
- Erreur traitée : EF2 - Comparer une valeur numérique restée chaîne.
### Corrigé exercice 7
- Méthode : comparer la donnée avec le cas limite « division par zéro » et valider `25`.
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
