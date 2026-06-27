---
title: "T17 - cours - programmation dynamique"
level: "terminale"
sequence_id: "T17"
document_type: "cours"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "programmation dynamique"
notion: "programmation dynamique"
private_data: false
official_program:
  capacities:
    - "T-ALGO-04"
---

# T17 - Cours - programmation dynamique

## Objectifs spécifiques
- Identifier les données utiles de la situation : pieces=[1,5,7], montant=11, dp[0]=0.
- Employer le vocabulaire : état, récurrence, initialisation, mémoïsation, tabulation, sous-problèmes.
- Produire une trace, une table, une valeur ou un pseudo-code vérifiable.

## Capacités officielles
- T-ALGO-04.

## Situation-problème
pieces=[1,5,7], montant=11, dp[0]=0

## À savoir
- état.
- récurrence.
- initialisation.
- mémoïsation.
- tabulation.
- sous-problèmes.
- complexité mémoire.

## Méthodes
- définir dp[m] coût minimal.
- écrire dp[m]=1+min(dp[m-p]).
- initialiser dp[0]=0.
- remplir la table de 1 à 11.

## Exemples corrigés
### Exemple corrigé 1
- Donnée : `pieces=[1,5,7], montant=11, dp[0]=0`.
- Méthode : définir dp[m] coût minimal.
- Résultat attendu : dp[6]=2 avec 5+1.
- Contrôle : capacité T-ALGO-04 et cas limite `montant 0`.
### Exemple corrigé 2
- Donnée : `pieces=[1,5,7], montant=11, dp[0]=0`.
- Méthode : écrire dp[m]=1+min(dp[m-p]).
- Résultat attendu : dp[11]=3 avec 5+5+1.
- Contrôle : capacité T-ALGO-04 et cas limite `montant impossible`.
### Exemple corrigé 3
- Donnée : `pieces=[1,5,7], montant=11, dp[0]=0`.
- Méthode : initialiser dp[0]=0.
- Résultat attendu : tabulation stocke chaque dp[m].
- Contrôle : capacité T-ALGO-04 et cas limite `pièce plus grande que m`.
### Exemple corrigé 4
- Donnée : `pieces=[1,5,7], montant=11, dp[0]=0`.
- Méthode : remplir la table de 1 à 11.
- Résultat attendu : sans pièce 1 certains montants impossibles.
- Contrôle : capacité T-ALGO-04 et cas limite `montant 0`.

## Cas limites
- montant 0.
- montant impossible.
- pièce plus grande que m.

## Erreurs fréquentes
- état ambigu.
- initialisation oubliée.
- choix de pièce confondu avec valeur optimale.

## Exercices intégrés
1. Identifier les données utiles dans `pieces=[1,5,7], montant=11, dp[0]=0`.
2. Appliquer : définir dp[m] coût minimal.
3. Appliquer : écrire dp[m]=1+min(dp[m-p]).
4. Décider le cas limite `montant 0`.

## Critères de réussite observables
- Une capacité parmi T-ALGO-04 est citée et utilisée.
- Le résultat attendu est explicite : dp[6]=2 avec 5+1.
- Le cas limite `montant impossible` est tranché.

## Lien avec la progression
- Séance : T17-S1 à T17-S4.
- TD : `T17_TD_programmation_dynamique.md`.
- TP : `T17_tp_programmation_dynamique.md`.
- Évaluation : `T17_evaluation_programmation_dynamique.md`.

## Renforcement explicatif ciblé

Ce cours doit être lu comme une progression sur programmation dynamique. La notion ne se réduit pas à une liste de mots : on part d'une situation observable, on nomme les objets manipulés, puis on applique une méthode vérifiable sur un cas limité avant de généraliser.

### Savoir disciplinaire
- Vocabulaire à maîtriser : état, initialisation, récurrence, mémoïsation, tabulation, ordre de remplissage.
- Capacités reliées : T-ALGO-04.
- Le savoir attendu consiste à expliquer le rôle de chaque objet avant de l'utiliser dans un exercice.

### Savoir-faire et méthodes opérationnelles
- définir l’état dp[i] avant la relation.
- remplir une table dans un ordre qui respecte les dépendances.
- comparer récursion naïve et tabulation.

### Erreurs fréquentes spécifiques
- Un élève peut écrire une récurrence sans initialisation ; la correction consiste à reprendre la définition puis à refaire la trace sur un exemple minimal.
- Un élève peut lire une case non encore calculée ; la correction consiste à isoler le cas limite avant de recommencer le calcul ou le raisonnement.
- Un élève peut confondre glouton et programmation dynamique ; la correction consiste à vérifier le résultat avec une donnée différente.

### Cas limites à contrôler
- Cas minimal : une donnée vide, un seul élément, une route absente ou une structure sans enfant selon la notion.
- Cas ambigu : doublon, égalité, absence de correspondance ou choix local non optimal.

### Synthèse savoir / savoir-faire / méthode
- Savoir : définir précisément les objets de programmation dynamique.
- Savoir-faire : appliquer une méthode contrôlable à une donnée explicite.
- Méthode : annoncer la donnée, exécuter les étapes dans l'ordre, puis vérifier le résultat par un cas limite.
