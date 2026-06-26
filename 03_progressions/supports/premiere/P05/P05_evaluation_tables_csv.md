---
title: "P05 - Evaluation - Tables CSV et requêtes simples"
level: "premiere"
sequence_id: "P05"
document_type: "evaluation"
status: "needs_review"
version: "0.3.0"
source: "BO 2019 ; ressource locale candidate : Documents_DRIVE/1_1ères NSI/3_Bloc3_TdDeT/Evaluation/T.P_TdDeT.docx"
theme: "Traitement de tables"
notion: "CSV, dictionnaire ligne, sélection, projection"
objectifs:
  - "Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation."
  - "Objectif O2 - Appliquer une méthode explicite sur un exemple guidé."
  - "Objectif O3 - Justifier le résultat obtenu sur un cas nouveau."
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente."
private_data: false
official_program:
  capacities:
    - "P-TABLE-01"
    - "P-TABLE-02"
---


# P05 - Evaluation - Tables CSV et requêtes simples

## Objectifs spécifiques
- Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation.
- Objectif O2 - Appliquer une méthode explicite sur un exemple guidé.
- Objectif O3 - Justifier le résultat obtenu sur un cas nouveau.
- Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente.

## Capacités officielles atomiques
- P-TABLE-01
- P-TABLE-02

## Prérequis
- Lire une consigne technique sans confondre donnée, méthode et résultat.
- Écrire une réponse sous forme de phrases courtes et vérifiables.
- Utiliser Python en distinguant expression, valeur, variable et affichage.
- Conserver une trace de calcul ou de raisonnement exploitable pour la révision.

## Séance(s) correspondante(s)
- P05-S1 à P05-S6 : ce support est rattaché aux séances indiquées dans la progression.

## Situation-problème concrète
une association reçoit un fichier CSV de réservations et veut filtrer les lignes incohérentes. La tâche consiste à traiter CSV, dictionnaire ligne, sélection, projection sans réponse intuitive non vérifiée.

## Activité d’entrée
1. Lire la situation : une association reçoit un fichier CSV de réservations et veut filtrer les lignes incohérentes.
2. Isoler la donnée de départ : table structurée en lignes et colonnes.
3. Prédire individuellement le résultat de l’exemple `nom;age;ville avec trois enregistrements`.
4. Comparer deux stratégies et noter la divergence précise.
5. Appliquer la méthode retenue : lire l’en-tête, convertir les champs utiles, filtrer puis agréger.
6. Contrôler avec le résultat de référence : liste de dictionnaires filtrée puis moyenne calculée.
7. Tester le cas limite suivant : champ vide, séparateur inattendu ou nombre invalide.
8. Rédiger une phrase qui relie donnée, méthode, résultat et contrôle.

## Exemple corrigé précis
- Exemple d’entraînement : `nom;age;ville avec trois enregistrements` donne `liste de dictionnaires filtrée puis moyenne calculée` avec la méthode lire l’en-tête, convertir les champs utiles, filtrer puis agréger.

## Exercices numérotés
- Les questions d’évaluation ci-dessous remplacent les exercices longs par des tâches courtes et notées.

### Question 1
- Objectif évalué : O1.
- Capacité officielle : P-TABLE-01.
- Énoncé : traiter `nom;age;ville avec trois enregistrements` ou une variante fournie en appliquant lire l’en-tête, convertir les champs utiles, filtrer puis agréger.
- Réponse attendue : résultat contrôlé `liste de dictionnaires filtrée puis moyenne calculée` et justification courte.
- Barème : 2 points pour la méthode, 2 points pour le résultat, 1 point pour le contrôle EF1.

### Question 2
- Objectif évalué : O2.
- Capacité officielle : P-TABLE-02.
- Énoncé : traiter `nom;age;ville avec trois enregistrements` ou une variante fournie en appliquant lire l’en-tête, convertir les champs utiles, filtrer puis agréger.
- Réponse attendue : résultat contrôlé `liste de dictionnaires filtrée puis moyenne calculée` et justification courte.
- Barème : 2 points pour la méthode, 2 points pour le résultat, 1 point pour le contrôle EF2.

### Question 3
- Objectif évalué : O3.
- Capacité officielle : P-TABLE-01.
- Énoncé : traiter `nom;age;ville avec trois enregistrements` ou une variante fournie en appliquant lire l’en-tête, convertir les champs utiles, filtrer puis agréger.
- Réponse attendue : résultat contrôlé `liste de dictionnaires filtrée puis moyenne calculée` et justification courte.
- Barème : 2 points pour la méthode, 2 points pour le résultat, 1 point pour le contrôle EF3.

### Question 4
- Objectif évalué : O4.
- Capacité officielle : P-TABLE-02.
- Énoncé : traiter `nom;age;ville avec trois enregistrements` ou une variante fournie en appliquant lire l’en-tête, convertir les champs utiles, filtrer puis agréger.
- Réponse attendue : résultat contrôlé `liste de dictionnaires filtrée puis moyenne calculée` et justification courte.
- Barème : 2 points pour la méthode, 2 points pour le résultat, 1 point pour le contrôle EF4.

## Barème
- Total : 20 points.
- Question 1 : 5 points.
- Question 2 : 5 points.
- Question 3 : 5 points.
- Question 4 : 5 points.

## Corrigé
- Corrigé question 1 : appliquer lire l’en-tête, convertir les champs utiles, filtrer puis agréger, obtenir `liste de dictionnaires filtrée puis moyenne calculée` sur le cas de référence, puis citer EF1.
- Corrigé question 2 : appliquer lire l’en-tête, convertir les champs utiles, filtrer puis agréger, obtenir `liste de dictionnaires filtrée puis moyenne calculée` sur le cas de référence, puis citer EF2.
- Corrigé question 3 : appliquer lire l’en-tête, convertir les champs utiles, filtrer puis agréger, obtenir `liste de dictionnaires filtrée puis moyenne calculée` sur le cas de référence, puis citer EF3.
- Corrigé question 4 : appliquer lire l’en-tête, convertir les champs utiles, filtrer puis agréger, obtenir `liste de dictionnaires filtrée puis moyenne calculée` sur le cas de référence, puis citer EF4.

## Erreurs fréquentes
- Erreur fréquente EF1 - répondre seulement par `liste de dictionnaires filtrée puis moyenne calculée` sans écrire la méthode.
- Erreur fréquente EF2 - appliquer lire l’en-tête, convertir les champs utiles, filtrer puis agréger dans le mauvais ordre.
- Erreur fréquente EF3 - oublier le cas limite : champ vide, séparateur inattendu ou nombre invalide.
- Erreur fréquente EF4 - citer une capacité officielle sans la relier à une production observable.

## Remédiation ciblée
- Activité corrective EF1 : reprendre l’exemple en imposant quatre colonnes, donnée, opération, résultat, contrôle.
- Activité corrective EF2 : refaire la méthode avec des étapes numérotées et une vérification à chaque étape.
- Activité corrective EF3 : construire deux variantes du cas limite `champ vide, séparateur inattendu ou nombre invalide` et comparer les sorties.
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

