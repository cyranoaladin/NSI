---
title: "P00 - Bareme - Diagnostic Python et carnet de bord"
level: "premiere"
sequence_id: "P00"
document_type: "bareme"
status: "needs_review"
version: "0.3.0"
source: "BO 2019 ; ressource locale candidate : Documents_DRIVE/1_1ères NSI/1_Rentrée/2_Introduction_NSI.pdf"
theme: "Rentrée et méthode"
notion: "affectation, expression, trace, test"
objectifs:
  - "Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation."
  - "Objectif O2 - Appliquer une méthode explicite sur un exemple guidé."
  - "Objectif O3 - Justifier le résultat obtenu sur un cas nouveau."
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente."
private_data: false
official_program:
  capacities:
    - "P-HIST-01"
    - "P-LANG-01"
---


# P00 - Bareme - Diagnostic Python et carnet de bord

## Objectifs spécifiques
- Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation.
- Objectif O2 - Appliquer une méthode explicite sur un exemple guidé.
- Objectif O3 - Justifier le résultat obtenu sur un cas nouveau.
- Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente.

## Capacités officielles atomiques
- P-HIST-01
- P-LANG-01

## Prérequis
- Lire une consigne technique sans confondre donnée, méthode et résultat.
- Écrire une réponse sous forme de phrases courtes et vérifiables.
- Utiliser Python en distinguant expression, valeur, variable et affichage.
- Conserver une trace de calcul ou de raisonnement exploitable pour la révision.

## Séance(s) correspondante(s)
- P00-S1 à P00-S4 : ce support est rattaché aux séances indiquées dans la progression.

## Situation-problème concrète
une classe de Première démarre avec des habitudes Python inégales et doit produire une trace vérifiable. La tâche consiste à traiter affectation, expression, trace, test sans réponse intuitive non vérifiée.

## Activité d’entrée
1. Lire la situation : une classe de Première démarre avec des habitudes Python inégales et doit produire une trace vérifiable.
2. Isoler la donnée de départ : variable x initialisée à 3 puis réaffectée.
3. Prédire individuellement le résultat de l’exemple `x = 3 ; x = x + 2 ; print(x)`.
4. Comparer deux stratégies et noter la divergence précise.
5. Appliquer la méthode retenue : suivre l’état de la variable après chaque affectation.
6. Contrôler avec le résultat de référence : 5.
7. Tester le cas limite suivant : réaffectation avec zéro ou valeur négative.
8. Rédiger une phrase qui relie donnée, méthode, résultat et contrôle.

## Exemple corrigé précis
- Exemple support : `x = 3 ; x = x + 2 ; print(x)`.
- Résultat support : `5`.
- Le barème attribue des points à la méthode, au résultat, à la justification et au contrôle.

## Exercices numérotés
- Les quatre questions de l’évaluation sont découpées question par question.

### Barème question 1
- Objectif : O1.
- Capacité : P-HIST-01.
- Méthode correcte : 2 points.
- Résultat correct : 1 point.
- Justification rédigée : 1 point.
- Contrôle du cas limite ou de EF1 : 1 point.
- Retrait maximal : 1 point si le vocabulaire officiel est absent.

### Barème question 2
- Objectif : O2.
- Capacité : P-LANG-01.
- Méthode correcte : 2 points.
- Résultat correct : 1 point.
- Justification rédigée : 1 point.
- Contrôle du cas limite ou de EF2 : 1 point.
- Retrait maximal : 1 point si le vocabulaire officiel est absent.

### Barème question 3
- Objectif : O3.
- Capacité : P-HIST-01.
- Méthode correcte : 2 points.
- Résultat correct : 1 point.
- Justification rédigée : 1 point.
- Contrôle du cas limite ou de EF3 : 1 point.
- Retrait maximal : 1 point si le vocabulaire officiel est absent.

### Barème question 4
- Objectif : O4.
- Capacité : P-LANG-01.
- Méthode correcte : 2 points.
- Résultat correct : 1 point.
- Justification rédigée : 1 point.
- Contrôle du cas limite ou de EF4 : 1 point.
- Retrait maximal : 1 point si le vocabulaire officiel est absent.

## Corrigé
- La correction détaillée se trouve dans le corrigé professeur, mais le barème rappelle les critères observables.
- Corrigé question 1 : méthode suivre l’état de la variable après chaque affectation, résultat `5`, contrôle EF1.
- Corrigé question 2 : méthode suivre l’état de la variable après chaque affectation, résultat `5`, contrôle EF2.
- Corrigé question 3 : méthode suivre l’état de la variable après chaque affectation, résultat `5`, contrôle EF3.
- Corrigé question 4 : méthode suivre l’état de la variable après chaque affectation, résultat `5`, contrôle EF4.

## Erreurs fréquentes
- Erreur fréquente EF1 - répondre seulement par `5` sans écrire la méthode.
- Erreur fréquente EF2 - appliquer suivre l’état de la variable après chaque affectation dans le mauvais ordre.
- Erreur fréquente EF3 - oublier le cas limite : réaffectation avec zéro ou valeur négative.
- Erreur fréquente EF4 - citer une capacité officielle sans la relier à une production observable.

## Remédiation ciblée
- Activité corrective EF1 : reprendre l’exemple en imposant quatre colonnes, donnée, opération, résultat, contrôle.
- Activité corrective EF2 : refaire la méthode avec des étapes numérotées et une vérification à chaque étape.
- Activité corrective EF3 : construire deux variantes du cas limite `réaffectation avec zéro ou valeur négative` et comparer les sorties.
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

