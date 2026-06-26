---
title: "P04 - Evaluation - Types construits Python"
level: "premiere"
sequence_id: "P04"
document_type: "evaluation"
status: "needs_review"
version: "0.3.0"
source: "BO 2019 ; ressource locale candidate : Documents_DRIVE/9_NSI_2025-2026/1ère/Séq2_Types construits _partie1/Cours_Tuples_Listes_Elève.pdf"
theme: "Tuples, listes, dictionnaires"
notion: "tuple, liste, dictionnaire, parcours"
objectifs:
  - "Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation."
  - "Objectif O2 - Appliquer une méthode explicite sur un exemple guidé."
  - "Objectif O3 - Justifier le résultat obtenu sur un cas nouveau."
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente."
private_data: false
official_program:
  capacities:
    - "P-DATA-CONSTR-01"
    - "P-DATA-CONSTR-02A"
    - "P-DATA-CONSTR-02B"
    - "P-DATA-CONSTR-02C"
    - "P-DATA-CONSTR-02D"
    - "P-DATA-CONSTR-03A"
    - "P-DATA-CONSTR-03B"
    - "P-DATA-CONSTR-03C"
---


# P04 - Evaluation - Types construits Python

## Objectifs spécifiques
- Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation.
- Objectif O2 - Appliquer une méthode explicite sur un exemple guidé.
- Objectif O3 - Justifier le résultat obtenu sur un cas nouveau.
- Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente.

## Capacités officielles atomiques
- P-DATA-CONSTR-01
- P-DATA-CONSTR-02A
- P-DATA-CONSTR-02B
- P-DATA-CONSTR-02C
- P-DATA-CONSTR-02D
- P-DATA-CONSTR-03A
- P-DATA-CONSTR-03B
- P-DATA-CONSTR-03C

## Prérequis
- Lire une consigne technique sans confondre donnée, méthode et résultat.
- Écrire une réponse sous forme de phrases courtes et vérifiables.
- Utiliser Python en distinguant expression, valeur, variable et affichage.
- Conserver une trace de calcul ou de raisonnement exploitable pour la révision.

## Séance(s) correspondante(s)
- P04-S1 à P04-S7 : ce support est rattaché aux séances indiquées dans la progression.

## Situation-problème concrète
un relevé météo mélange coordonnées fixes, mesures modifiables et accès par nom de station. La tâche consiste à traiter tuple, liste, dictionnaire, parcours sans réponse intuitive non vérifiée.

## Activité d’entrée
1. Lire la situation : un relevé météo mélange coordonnées fixes, mesures modifiables et accès par nom de station.
2. Isoler la donnée de départ : collection ordonnée ou associée à des clés.
3. Prédire individuellement le résultat de l’exemple `coord=(43.6,1.4), mesures=[12,14,13], station={"nom":"A","temp":14}`.
4. Comparer deux stratégies et noter la divergence précise.
5. Appliquer la méthode retenue : choisir le conteneur selon mutabilité, ordre et accès attendu.
6. Contrôler avec le résultat de référence : tuple non modifié, liste mise à jour, dictionnaire consulté par clé.
7. Tester le cas limite suivant : copie de liste et clé absente.
8. Rédiger une phrase qui relie donnée, méthode, résultat et contrôle.

## Exemple corrigé précis
- Exemple d’entraînement : `coord=(43.6,1.4), mesures=[12,14,13], station={"nom":"A","temp":14}` donne `tuple non modifié, liste mise à jour, dictionnaire consulté par clé` avec la méthode choisir le conteneur selon mutabilité, ordre et accès attendu.

## Exercices numérotés
- Les questions d’évaluation ci-dessous remplacent les exercices longs par des tâches courtes et notées.

### Question 1
- Objectif évalué : O1.
- Capacité officielle : P-DATA-CONSTR-01.
- Énoncé : traiter `coord=(43.6,1.4), mesures=[12,14,13], station={"nom":"A","temp":14}` ou une variante fournie en appliquant choisir le conteneur selon mutabilité, ordre et accès attendu.
- Réponse attendue : résultat contrôlé `tuple non modifié, liste mise à jour, dictionnaire consulté par clé` et justification courte.
- Barème : 2 points pour la méthode, 2 points pour le résultat, 1 point pour le contrôle EF1.

### Question 2
- Objectif évalué : O2.
- Capacité officielle : P-DATA-CONSTR-02A.
- Énoncé : traiter `coord=(43.6,1.4), mesures=[12,14,13], station={"nom":"A","temp":14}` ou une variante fournie en appliquant choisir le conteneur selon mutabilité, ordre et accès attendu.
- Réponse attendue : résultat contrôlé `tuple non modifié, liste mise à jour, dictionnaire consulté par clé` et justification courte.
- Barème : 2 points pour la méthode, 2 points pour le résultat, 1 point pour le contrôle EF2.

### Question 3
- Objectif évalué : O3.
- Capacité officielle : P-DATA-CONSTR-02B.
- Énoncé : traiter `coord=(43.6,1.4), mesures=[12,14,13], station={"nom":"A","temp":14}` ou une variante fournie en appliquant choisir le conteneur selon mutabilité, ordre et accès attendu.
- Réponse attendue : résultat contrôlé `tuple non modifié, liste mise à jour, dictionnaire consulté par clé` et justification courte.
- Barème : 2 points pour la méthode, 2 points pour le résultat, 1 point pour le contrôle EF3.

### Question 4
- Objectif évalué : O4.
- Capacité officielle : P-DATA-CONSTR-02C.
- Énoncé : traiter `coord=(43.6,1.4), mesures=[12,14,13], station={"nom":"A","temp":14}` ou une variante fournie en appliquant choisir le conteneur selon mutabilité, ordre et accès attendu.
- Réponse attendue : résultat contrôlé `tuple non modifié, liste mise à jour, dictionnaire consulté par clé` et justification courte.
- Barème : 2 points pour la méthode, 2 points pour le résultat, 1 point pour le contrôle EF4.

## Barème
- Total : 20 points.
- Question 1 : 5 points.
- Question 2 : 5 points.
- Question 3 : 5 points.
- Question 4 : 5 points.

## Corrigé
- Corrigé question 1 : appliquer choisir le conteneur selon mutabilité, ordre et accès attendu, obtenir `tuple non modifié, liste mise à jour, dictionnaire consulté par clé` sur le cas de référence, puis citer EF1.
- Corrigé question 2 : appliquer choisir le conteneur selon mutabilité, ordre et accès attendu, obtenir `tuple non modifié, liste mise à jour, dictionnaire consulté par clé` sur le cas de référence, puis citer EF2.
- Corrigé question 3 : appliquer choisir le conteneur selon mutabilité, ordre et accès attendu, obtenir `tuple non modifié, liste mise à jour, dictionnaire consulté par clé` sur le cas de référence, puis citer EF3.
- Corrigé question 4 : appliquer choisir le conteneur selon mutabilité, ordre et accès attendu, obtenir `tuple non modifié, liste mise à jour, dictionnaire consulté par clé` sur le cas de référence, puis citer EF4.

## Erreurs fréquentes
- Erreur fréquente EF1 - répondre seulement par `tuple non modifié, liste mise à jour, dictionnaire consulté par clé` sans écrire la méthode.
- Erreur fréquente EF2 - appliquer choisir le conteneur selon mutabilité, ordre et accès attendu dans le mauvais ordre.
- Erreur fréquente EF3 - oublier le cas limite : copie de liste et clé absente.
- Erreur fréquente EF4 - citer une capacité officielle sans la relier à une production observable.

## Remédiation ciblée
- Activité corrective EF1 : reprendre l’exemple en imposant quatre colonnes, donnée, opération, résultat, contrôle.
- Activité corrective EF2 : refaire la méthode avec des étapes numérotées et une vérification à chaque étape.
- Activité corrective EF3 : construire deux variantes du cas limite `copie de liste et clé absente` et comparer les sorties.
- Activité corrective EF4 : associer chaque phrase de réponse à une capacité officielle citée en début de copie.

## Différenciation
- Socle : la méthode est fournie sous forme de tableau à compléter.
- Standard : l’élève choisit la méthode et rédige la justification complète.
- Expert : l’élève crée un contre-exemple ou un cas limite et explique l’échec attendu.

## Critères de réussite
- Les objectifs O1 à O4 apparaissent dans la production ou dans la correction.
- Au moins une capacité officielle est reliée à une question traitée.
- Le résultat est accompagné d’une méthode et d’un contrôle.
- Les erreurs fréquentes sont nommées et corrigées par une activité de remédiation.

