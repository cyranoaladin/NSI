---
title: "T05 - Bareme - Arbres binaires et parcours"
level: "terminale"
sequence_id: "T05"
document_type: "bareme"
status: "needs_review"
version: "0.3.0"
source: "BO 2019 ; ressource locale candidate : Documents_DRIVE/2_NSI/Formation TOULOUSE/BLOC4/Polycopié_v2.pdf"
theme: "Arbres et algorithmes"
notion: "nœud, parcours, recherche, complexité"
objectifs:
  - "Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation."
  - "Objectif O2 - Appliquer une méthode explicite sur un exemple guidé."
  - "Objectif O3 - Justifier le résultat obtenu sur un cas nouveau."
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente."
private_data: false
official_program:
  capacities:
    - "T-STRUCT-04A"
    - "T-STRUCT-04B"
    - "T-ALGO-01A"
    - "T-ALGO-01B"
    - "T-ALGO-01C"
    - "T-ALGO-01D"
---


# T05 - Bareme - Arbres binaires et parcours

## Objectifs spécifiques
- Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation.
- Objectif O2 - Appliquer une méthode explicite sur un exemple guidé.
- Objectif O3 - Justifier le résultat obtenu sur un cas nouveau.
- Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente.

## Capacités officielles atomiques
- T-STRUCT-04A
- T-STRUCT-04B
- T-ALGO-01A
- T-ALGO-01B
- T-ALGO-01C
- T-ALGO-01D

## Prérequis
- Lire une consigne technique sans confondre donnée, méthode et résultat.
- Écrire une réponse sous forme de phrases courtes et vérifiables.
- Utiliser Python en distinguant expression, valeur, variable et affichage.
- Conserver une trace de calcul ou de raisonnement exploitable pour la révision.

## Séance(s) correspondante(s)
- T05-S1 à T05-S7 : ce support est rattaché aux séances indiquées dans la progression.

## Situation-problème concrète
une collection hiérarchique doit être parcourue et interrogée sans la transformer en liste plate. La tâche consiste à traiter nœud, parcours, recherche, complexité sans réponse intuitive non vérifiée.

## Activité d’entrée
1. Lire la situation : une collection hiérarchique doit être parcourue et interrogée sans la transformer en liste plate.
2. Isoler la donnée de départ : nœud racine et sous-arbres gauche/droit.
3. Prédire individuellement le résultat de l’exemple `arbre 4 avec fils 2 et 7`.
4. Comparer deux stratégies et noter la divergence précise.
5. Appliquer la méthode retenue : raisonner récursivement sur arbre vide puis racine puis sous-arbres.
6. Contrôler avec le résultat de référence : parcours infixe 2, 4, 7.
7. Tester le cas limite suivant : arbre vide ou arbre très déséquilibré.
8. Rédiger une phrase qui relie donnée, méthode, résultat et contrôle.

## Exemple corrigé précis
- Exemple support : `arbre 4 avec fils 2 et 7`.
- Résultat support : `parcours infixe 2, 4, 7`.
- Le barème attribue des points à la méthode, au résultat, à la justification et au contrôle.

## Exercices numérotés
- Les quatre questions de l’évaluation sont découpées question par question.

### Barème question 1
- Objectif : O1.
- Capacité : T-STRUCT-04A.
- Méthode correcte : 2 points.
- Résultat correct : 1 point.
- Justification rédigée : 1 point.
- Contrôle du cas limite ou de EF1 : 1 point.
- Retrait maximal : 1 point si le vocabulaire officiel est absent.

### Barème question 2
- Objectif : O2.
- Capacité : T-STRUCT-04B.
- Méthode correcte : 2 points.
- Résultat correct : 1 point.
- Justification rédigée : 1 point.
- Contrôle du cas limite ou de EF2 : 1 point.
- Retrait maximal : 1 point si le vocabulaire officiel est absent.

### Barème question 3
- Objectif : O3.
- Capacité : T-ALGO-01A.
- Méthode correcte : 2 points.
- Résultat correct : 1 point.
- Justification rédigée : 1 point.
- Contrôle du cas limite ou de EF3 : 1 point.
- Retrait maximal : 1 point si le vocabulaire officiel est absent.

### Barème question 4
- Objectif : O4.
- Capacité : T-ALGO-01B.
- Méthode correcte : 2 points.
- Résultat correct : 1 point.
- Justification rédigée : 1 point.
- Contrôle du cas limite ou de EF4 : 1 point.
- Retrait maximal : 1 point si le vocabulaire officiel est absent.

## Corrigé
- La correction détaillée se trouve dans le corrigé professeur, mais le barème rappelle les critères observables.
- Corrigé question 1 : méthode raisonner récursivement sur arbre vide puis racine puis sous-arbres, résultat `parcours infixe 2, 4, 7`, contrôle EF1.
- Corrigé question 2 : méthode raisonner récursivement sur arbre vide puis racine puis sous-arbres, résultat `parcours infixe 2, 4, 7`, contrôle EF2.
- Corrigé question 3 : méthode raisonner récursivement sur arbre vide puis racine puis sous-arbres, résultat `parcours infixe 2, 4, 7`, contrôle EF3.
- Corrigé question 4 : méthode raisonner récursivement sur arbre vide puis racine puis sous-arbres, résultat `parcours infixe 2, 4, 7`, contrôle EF4.

## Erreurs fréquentes
- Erreur fréquente EF1 - répondre seulement par `parcours infixe 2, 4, 7` sans écrire la méthode.
- Erreur fréquente EF2 - appliquer raisonner récursivement sur arbre vide puis racine puis sous-arbres dans le mauvais ordre.
- Erreur fréquente EF3 - oublier le cas limite : arbre vide ou arbre très déséquilibré.
- Erreur fréquente EF4 - citer une capacité officielle sans la relier à une production observable.

## Remédiation ciblée
- Activité corrective EF1 : reprendre l’exemple en imposant quatre colonnes, donnée, opération, résultat, contrôle.
- Activité corrective EF2 : refaire la méthode avec des étapes numérotées et une vérification à chaque étape.
- Activité corrective EF3 : construire deux variantes du cas limite `arbre vide ou arbre très déséquilibré` et comparer les sorties.
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

