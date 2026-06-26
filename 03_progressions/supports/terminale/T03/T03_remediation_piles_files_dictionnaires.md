---
title: "T03 - Remediation - Piles, files et dictionnaires"
level: "terminale"
sequence_id: "T03"
document_type: "remediation"
status: "needs_review"
version: "0.3.0"
source: "BO 2019 ; ressource locale candidate : Documents_DRIVE/2_NSI/Formation TOULOUSE/BLOC4/TD EIL - TAD - 2019-2020.pdf"
theme: "Structures linéaires"
notion: "LIFO, FIFO, dictionnaire d’index"
objectifs:
  - "Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation."
  - "Objectif O2 - Appliquer une méthode explicite sur un exemple guidé."
  - "Objectif O3 - Justifier le résultat obtenu sur un cas nouveau."
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente."
private_data: false
official_program:
  capacities:
    - "T-STRUCT-03A"
    - "T-STRUCT-03B"
    - "T-STRUCT-03C"
---


# T03 - Remediation - Piles, files et dictionnaires

## Objectifs spécifiques
- Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation.
- Objectif O2 - Appliquer une méthode explicite sur un exemple guidé.
- Objectif O3 - Justifier le résultat obtenu sur un cas nouveau.
- Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente.

## Capacités officielles atomiques
- T-STRUCT-03A
- T-STRUCT-03B
- T-STRUCT-03C

## Prérequis
- Lire une consigne technique sans confondre donnée, méthode et résultat.
- Écrire une réponse sous forme de phrases courtes et vérifiables.
- Utiliser Python en distinguant expression, valeur, variable et affichage.
- Conserver une trace de calcul ou de raisonnement exploitable pour la révision.

## Séance(s) correspondante(s)
- T03-S1 à T03-S6 : ce support est rattaché aux séances indiquées dans la progression.

## Situation-problème concrète
une application doit gérer un historique d’annulation et une file d’attente de requêtes. La tâche consiste à traiter LIFO, FIFO, dictionnaire d’index sans réponse intuitive non vérifiée.

## Activité d’entrée
1. Lire la situation : une application doit gérer un historique d’annulation et une file d’attente de requêtes.
2. Isoler la donnée de départ : suite d’opérations sur collection linéaire.
3. Prédire individuellement le résultat de l’exemple `empiler A, empiler B, dépiler`.
4. Comparer deux stratégies et noter la divergence précise.
5. Appliquer la méthode retenue : choisir LIFO ou FIFO selon l’ordre de sortie attendu.
6. Contrôler avec le résultat de référence : B sort avant A pour une pile ; A sort avant B pour une file.
7. Tester le cas limite suivant : dépiler ou défiler une structure vide.
8. Rédiger une phrase qui relie donnée, méthode, résultat et contrôle.

## Diagnostic des erreurs
- EF1 apparaît quand l’élève donne `B sort avant A pour une pile ; A sort avant B pour une file` sans expliquer choisir LIFO ou FIFO selon l’ordre de sortie attendu.
- EF2 apparaît quand l’élève inverse les étapes de choisir LIFO ou FIFO selon l’ordre de sortie attendu.
- EF3 apparaît quand le cas limite `dépiler ou défiler une structure vide` n’est pas testé.
- EF4 apparaît quand la capacité officielle est citée sans production observable.

## Exemple corrigé précis
- Reprise guidée : `empiler A, empiler B, dépiler`.
- Correction : choisir LIFO ou FIFO selon l’ordre de sortie attendu.
- Résultat : `B sort avant A pour une pile ; A sort avant B pour une file`.

## Exercices numérotés
- Exercice 1 : reprendre EF1 avec une donnée voisine et écrire une vérification.
- Exercice 2 : reprendre EF2 avec une donnée voisine et écrire une vérification.
- Exercice 3 : reprendre EF3 avec une donnée voisine et écrire une vérification.
- Exercice 4 : reprendre EF4 avec une donnée voisine et écrire une vérification.
- Exercice 5 : reprendre EF1 avec une donnée voisine et écrire une vérification.
- Exercice 6 : reprendre EF2 avec une donnée voisine et écrire une vérification.
- Exercice 7 : reprendre EF3 avec une donnée voisine et écrire une vérification.
- Exercice 8 : reprendre EF4 avec une donnée voisine et écrire une vérification.

## Corrigé
- Corrigé exercice 1 : la réponse reconstruit la méthode, puis contrôle EF1.
- Corrigé exercice 2 : la réponse reconstruit la méthode, puis contrôle EF2.
- Corrigé exercice 3 : la réponse reconstruit la méthode, puis contrôle EF3.
- Corrigé exercice 4 : la réponse reconstruit la méthode, puis contrôle EF4.
- Corrigé exercice 5 : la réponse reconstruit la méthode, puis contrôle EF1.
- Corrigé exercice 6 : la réponse reconstruit la méthode, puis contrôle EF2.
- Corrigé exercice 7 : la réponse reconstruit la méthode, puis contrôle EF3.
- Corrigé exercice 8 : la réponse reconstruit la méthode, puis contrôle EF4.

## Erreurs fréquentes
- Erreur fréquente EF1 - répondre seulement par `B sort avant A pour une pile ; A sort avant B pour une file` sans écrire la méthode.
- Erreur fréquente EF2 - appliquer choisir LIFO ou FIFO selon l’ordre de sortie attendu dans le mauvais ordre.
- Erreur fréquente EF3 - oublier le cas limite : dépiler ou défiler une structure vide.
- Erreur fréquente EF4 - citer une capacité officielle sans la relier à une production observable.

## Remédiation ciblée
- Activité corrective EF1 : reprendre l’exemple en imposant quatre colonnes, donnée, opération, résultat, contrôle.
- Activité corrective EF2 : refaire la méthode avec des étapes numérotées et une vérification à chaque étape.
- Activité corrective EF3 : construire deux variantes du cas limite `dépiler ou défiler une structure vide` et comparer les sorties.
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

## Activités correctives détaillées
- Activité corrective EF1 : surligner donnée, opération, résultat, contrôle dans quatre couleurs.
- Activité corrective EF2 : remettre dans l’ordre cinq cartes décrivant les étapes de la méthode.
- Activité corrective EF3 : construire un tableau avec cas nominal, cas limite et cas impossible.
- Activité corrective EF4 : associer chaque ligne de solution à une capacité officielle.
