---
title: "P05 - Cours - Tables CSV"
level: "premiere"
sequence_id: "P05"
document_type: "cours"
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

# P05 - Cours - Tables CSV

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

## Définitions et formalisation
- Définition D1 : table est utilisé dans Traitement de tables avec une donnée, une règle et un contrôle.
- Définition D2 : CSV est utilisé dans Traitement de tables avec une donnée, une règle et un contrôle.
- Définition D3 : filtrage est utilisé dans Traitement de tables avec une donnée, une règle et un contrôle.
- Définition D4 : agrégation est utilisé dans Traitement de tables avec une donnée, une règle et un contrôle.
- Cas limite principal : fichier vide.

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
## Objectif O1 - Identifier précisément la représentation ou la structure en jeu
- Capacité mobilisée : P-TABLE-01.
- Point de départ : `ville,temp
Tunis,24`.
- Angle disciplinaire : repérage initial autour de lecture CSV.
- Démarche attendue : séparer en-tête et données puis convertir la température.
- Exemple associé : une ligne exploitable.
- Point de vigilance : Traiter l’en-tête comme une donnée.
- Activité de reprise associée : Marquer l’en-tête et commencer les données à la ligne suivante.
- Mini-production : produire un court diagnostic de la donnée et du vocabulaire.
## Objectif O2 - Appliquer une méthode disciplinaire complète
- Capacité mobilisée : P-TABLE-01.
- Point de départ : trois villes dont deux Tunis.
- Angle disciplinaire : méthode guidée autour de filtrage.
- Démarche attendue : conserver les lignes respectant un prédicat.
- Exemple associé : deux lignes sélectionnées.
- Point de vigilance : Comparer une valeur numérique restée chaîne.
- Activité de reprise associée : Convertir explicitement avant les comparaisons numériques.
- Mini-production : produire une procédure numérotée avec contrôle intermédiaire.
## Objectif O3 - Justifier le résultat sur un cas différent
- Capacité mobilisée : P-TABLE-01.
- Point de départ : `24`, `26`, champ vide.
- Angle disciplinaire : transfert argumenté autour de agrégation.
- Démarche attendue : ignorer ou signaler le champ vide avant moyenne.
- Exemple associé : `25`.
- Point de vigilance : Diviser par zéro après filtrage vide.
- Activité de reprise associée : Tester la taille de la sélection avant la moyenne.
- Mini-production : produire une justification qui compare deux cas distincts.
## Objectif O4 - Contrôler un cas limite et corriger une erreur observée
- Capacité mobilisée : P-TABLE-01.
- Point de départ : table villes et table régions.
- Angle disciplinaire : vérification critique autour de jointure simple.
- Démarche attendue : associer par une clé commune.
- Exemple associé : ville enrichie par région.
- Point de vigilance : Ignorer silencieusement une ligne mal formée.
- Activité de reprise associée : Isoler les lignes invalides dans une liste de rejets.
- Mini-production : produire une correction d’erreur avec un nouveau test.
## Exercices numérotés
- Exercice 1 : résoudre lecture CSV avec `ville,temp
Tunis,24` ; attendu : une ligne exploitable.
- Exercice 2 : expliquer filtrage à partir de trois villes dont deux Tunis ; attendu : deux lignes sélectionnées.
- Exercice 3 : comparer agrégation avec `24`, `26`, champ vide ; attendu : `25`.
- Exercice 4 : corriger jointure simple pour table villes et table régions ; attendu : ville enrichie par région.
- Exercice 5 : tester un cas limite lié à fichier vide ; attendu : le comportement de lecture CSV est contrôlé.
- Exercice 6 : classer deux méthodes possibles pour filtrage ; attendu : la méthode robuste est choisie et justifiée.
- Exercice 7 : justifier un transfert qui utilise agrégation avec une donnée nouvelle ; attendu : la justification reste valable sur le nouveau cas.
- Exercice 8 : étendre un énoncé volontairement erroné sur jointure simple ; attendu : l’erreur est localisée puis réparée.
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
## Banque de situations complémentaires
- Situation complémentaire 1 : reprendre lecture CSV avec une donnée construite par un binôme.
- Question orale 1 : expliquer pourquoi le cas limite « fichier vide » change ou ne change pas la méthode.
- Trace attendue 1 : une phrase de méthode, une ligne de calcul et une vérification indépendante.
- Situation complémentaire 2 : reprendre filtrage avec une donnée construite par un binôme.
- Question orale 2 : expliquer pourquoi le cas limite « aucune ligne retenue » change ou ne change pas la méthode.
- Trace attendue 2 : une phrase de méthode, une ligne de calcul et une vérification indépendante.
- Situation complémentaire 3 : reprendre agrégation avec une donnée construite par un binôme.
- Question orale 3 : expliquer pourquoi le cas limite « division par zéro » change ou ne change pas la méthode.
- Trace attendue 3 : une phrase de méthode, une ligne de calcul et une vérification indépendante.
- Situation complémentaire 4 : reprendre jointure simple avec une donnée construite par un binôme.
- Question orale 4 : expliquer pourquoi le cas limite « clé inconnue » change ou ne change pas la méthode.
- Trace attendue 4 : une phrase de méthode, une ligne de calcul et une vérification indépendante.
## Atelier de synthèse
- Synthèse 1 : relier lecture CSV à une erreur fréquente et à une remédiation ciblée.
- Synthèse 2 : relier filtrage à une erreur fréquente et à une remédiation ciblée.
- Synthèse 3 : relier agrégation à une erreur fréquente et à une remédiation ciblée.
- Synthèse 4 : relier jointure simple à une erreur fréquente et à une remédiation ciblée.
## Lexique actif
- table : terme à employer dans une justification écrite de la séquence.
- CSV : terme à employer dans une justification écrite de la séquence.
- filtrage : terme à employer dans une justification écrite de la séquence.
- agrégation : terme à employer dans une justification écrite de la séquence.

## Analyse de variantes disciplinaires
- Variante P05-A : modifier la donnée du premier exemple de P05 - Cours - Tables CSV et conserver exactement la même méthode.
- Variante P05-B : changer le cas limite et expliquer quelle étape de contrôle devient obligatoire.
- Variante P05-C : demander à un pair de retrouver l’erreur fréquente avant de lire la correction.
- Variante P05-D : produire une trace écrite qui sépare définition, calcul et justification.
- Variante P05-E : comparer deux solutions d’élèves et isoler celle qui cite la capacité officielle.
- Variante P05-F : construire une donnée minimale qui force une décision de méthode.
- Variante P05-G : transformer un exemple corrigé en question d’évaluation courte.
- Variante P05-H : écrire un contre-exemple qui invalide une réponse seulement déclarative.
- Variante P05-I : relier une erreur fréquente à une activité corrective précise.
- Variante P05-J : rédiger un critère de réussite observable pour une copie réelle.
- Variante P05-K : vérifier que le vocabulaire utilisé correspond au thème de la séquence.
- Variante P05-L : préparer une question orale de trente secondes avec réponse vérifiable.
- Variante P05-M : isoler la donnée, l’algorithme mental et le résultat final dans trois lignes.
- Variante P05-N : expliquer ce que le TP apporte que le TD ne permet pas de tester.
- Variante P05-O : compléter la trace écrite par une mise en garde liée au cas limite.
- Variante P05-P : vérifier la cohérence entre exercice, corrigé, barème et remédiation.
