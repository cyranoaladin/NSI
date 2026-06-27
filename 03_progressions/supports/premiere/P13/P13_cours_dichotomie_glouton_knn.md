---
title: "P13 - cours - dichotomie, glouton et k-NN"
level: "premiere"
sequence_id: "P13"
document_type: "cours"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "dichotomie, glouton et k-NN"
notion: "dichotomie, glouton et k-NN"
private_data: false
official_program:
  capacities:
    - "P-ALGO-03"
    - "P-ALGO-04"
    - "P-ALGO-05"
---

# P13 - Cours - dichotomie, glouton et k-NN

## Objectifs spécifiques
- Identifier les données utiles de la situation : tableau=[4,9,18,23,37,41], cible=37 ; pièces=[10,5,2,1], montant=28 ; voisins=[rouge:1.2, bleu:2.0, rouge:2.4].
- Employer le vocabulaire : dichotomie, variant droite-gauche, glouton, choix local, k-NN, distance.
- Produire une trace, une table, une valeur ou un pseudo-code vérifiable.

## Capacités officielles
- P-ALGO-03.
- P-ALGO-04.
- P-ALGO-05.

## Situation-problème
tableau=[4,9,18,23,37,41], cible=37 ; pièces=[10,5,2,1], montant=28 ; voisins=[rouge:1.2, bleu:2.0, rouge:2.4]

## À savoir
- dichotomie.
- variant droite-gauche.
- glouton.
- choix local.
- k-NN.
- distance.
- vote majoritaire.

## Méthodes
- calculer milieu puis réduire intervalle.
- montrer que droite-gauche diminue.
- prendre la plus grande pièce possible.
- voter parmi k=3 voisins.

## Exemples corrigés
### Exemple corrigé 1
- Donnée : `tableau=[4,9,18,23,37,41], cible=37 ; pièces=[10,5,2,1], montant=28 ; voisins=[rouge:1.2, bleu:2.0, rouge:2.4]`.
- Méthode : calculer milieu puis réduire intervalle.
- Résultat attendu : milieux 18 puis 37 -> trouvé indice 4.
- Contrôle : capacité P-ALGO-03 et cas limite `cible absente`.
### Exemple corrigé 2
- Donnée : `tableau=[4,9,18,23,37,41], cible=37 ; pièces=[10,5,2,1], montant=28 ; voisins=[rouge:1.2, bleu:2.0, rouge:2.4]`.
- Méthode : montrer que droite-gauche diminue.
- Résultat attendu : 28 -> 10+10+5+2+1.
- Contrôle : capacité P-ALGO-04 et cas limite `pièce 1 absente`.
### Exemple corrigé 3
- Donnée : `tableau=[4,9,18,23,37,41], cible=37 ; pièces=[10,5,2,1], montant=28 ; voisins=[rouge:1.2, bleu:2.0, rouge:2.4]`.
- Méthode : prendre la plus grande pièce possible.
- Résultat attendu : rouge, bleu, rouge -> classe rouge.
- Contrôle : capacité P-ALGO-05 et cas limite `égalité de vote`.
### Exemple corrigé 4
- Donnée : `tableau=[4,9,18,23,37,41], cible=37 ; pièces=[10,5,2,1], montant=28 ; voisins=[rouge:1.2, bleu:2.0, rouge:2.4]`.
- Méthode : voter parmi k=3 voisins.
- Résultat attendu : cible 40 absente -> non trouvé.
- Contrôle : capacité P-ALGO-03 et cas limite `cible absente`.

## Cas limites
- cible absente.
- pièce 1 absente.
- égalité de vote.

## Erreurs fréquentes
- dichotomie sur liste non triée.
- glouton supposé toujours optimal.
- égalité k-NN non décidée.

## Exercices intégrés
1. Identifier les données utiles dans `tableau=[4,9,18,23,37,41], cible=37 ; pièces=[10,5,2,1], montant=28 ; voisins=[rouge:1.2, bleu:2.0, rouge:2.4]`.
2. Appliquer : calculer milieu puis réduire intervalle.
3. Appliquer : montrer que droite-gauche diminue.
4. Décider le cas limite `cible absente`.

## Critères de réussite observables
- Une capacité parmi P-ALGO-03, P-ALGO-04, P-ALGO-05 est citée et utilisée.
- Le résultat attendu est explicite : milieux 18 puis 37 -> trouvé indice 4.
- Le cas limite `pièce 1 absente` est tranché.

## Lien avec la progression
- Séance : P13-S1 à P13-S4.
- TD : `P13_TD_dichotomie_glouton_knn.md`.
- TP : `P13_tp_dichotomie_glouton_knn.md`.
- Évaluation : `P13_evaluation_dichotomie_glouton_knn.md`.

## Renforcement explicatif ciblé

Ce cours doit être lu comme une progression sur dichotomie, glouton et k plus proches voisins. La notion ne se réduit pas à une liste de mots : on part d'une situation observable, on nomme les objets manipulés, puis on applique une méthode vérifiable sur un cas limité avant de généraliser.

### Savoir disciplinaire
- Vocabulaire à maîtriser : intervalle de recherche, milieu, choix glouton, contre-exemple, distance.
- Capacités reliées : P-ALGO-03, P-ALGO-04, P-ALGO-05.
- Le savoir attendu consiste à expliquer le rôle de chaque objet avant de l'utiliser dans un exercice.

### Savoir-faire et méthodes opérationnelles
- réduire l’intervalle de dichotomie après chaque comparaison.
- justifier un choix glouton local.
- calculer les distances avant de classer les voisins.

### Erreurs fréquentes spécifiques
- Un élève peut oublier que la dichotomie exige des données triées ; la correction consiste à reprendre la définition puis à refaire la trace sur un exemple minimal.
- Un élève peut confondre choix local et optimal global ; la correction consiste à isoler le cas limite avant de recommencer le calcul ou le raisonnement.
- Un élève peut ignorer une égalité de distance ; la correction consiste à vérifier le résultat avec une donnée différente.

### Cas limites à contrôler
- Cas minimal : une donnée vide, un seul élément, une route absente ou une structure sans enfant selon la notion.
- Cas ambigu : doublon, égalité, absence de correspondance ou choix local non optimal.

### Synthèse savoir / savoir-faire / méthode
- Savoir : définir précisément les objets de dichotomie, glouton et k plus proches voisins.
- Savoir-faire : appliquer une méthode contrôlable à une donnée explicite.
- Méthode : annoncer la donnée, exécuter les étapes dans l'ordre, puis vérifier le résultat par un cas limite.
