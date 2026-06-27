---
title: "T06 - cours - arbres binaires de recherche"
level: "terminale"
sequence_id: "T06"
document_type: "cours"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "arbres binaires de recherche"
notion: "arbres binaires de recherche"
private_data: false
official_program:
  capacities:
    - "T-ALGO-01E"
    - "T-ALGO-01F"
---

# T06 - Cours - arbres binaires de recherche

## Objectifs spécifiques
- Identifier les données utiles de la situation : ABR racine=8, gauche=3 avec 1 et 6, droite=10 avec 14.
- Employer le vocabulaire : invariant ABR, recherche, insertion, parcours infixe, arbre vide, doublon.
- Produire une trace, une table, une valeur ou un pseudo-code vérifiable.

## Capacités officielles
- T-ALGO-01E.
- T-ALGO-01F.

## Situation-problème
ABR racine=8, gauche=3 avec 1 et 6, droite=10 avec 14

## À savoir
- invariant ABR.
- recherche.
- insertion.
- parcours infixe.
- arbre vide.
- doublon.
- complexité hauteur.

## Méthodes
- comparer à la racine.
- descendre gauche ou droite.
- insérer une feuille.
- parcours infixe pour clés triées.

## Exemples corrigés
### Exemple corrigé 1
- Donnée : `ABR racine=8, gauche=3 avec 1 et 6, droite=10 avec 14`.
- Méthode : comparer à la racine.
- Résultat attendu : chercher 6 : 8 -> 3 -> 6.
- Contrôle : capacité T-ALGO-01E et cas limite `arbre vide`.
### Exemple corrigé 2
- Donnée : `ABR racine=8, gauche=3 avec 1 et 6, droite=10 avec 14`.
- Méthode : descendre gauche ou droite.
- Résultat attendu : insérer 7 : 8 -> 3 -> 6 -> droite.
- Contrôle : capacité T-ALGO-01F et cas limite `doublon 6`.
### Exemple corrigé 3
- Donnée : `ABR racine=8, gauche=3 avec 1 et 6, droite=10 avec 14`.
- Méthode : insérer une feuille.
- Résultat attendu : infixe -> 1,3,6,8,10,14.
- Contrôle : capacité T-ALGO-01E et cas limite `arbre dégénéré`.
### Exemple corrigé 4
- Donnée : `ABR racine=8, gauche=3 avec 1 et 6, droite=10 avec 14`.
- Méthode : parcours infixe pour clés triées.
- Résultat attendu : arbre vide -> nouvelle racine.
- Contrôle : capacité T-ALGO-01F et cas limite `arbre vide`.

## Cas limites
- arbre vide.
- doublon 6.
- arbre dégénéré.

## Erreurs fréquentes
- gauche et droite inversées.
- logarithmique sans équilibre.
- racine vide oubliée.

## Exercices intégrés
1. Identifier les données utiles dans `ABR racine=8, gauche=3 avec 1 et 6, droite=10 avec 14`.
2. Appliquer : comparer à la racine.
3. Appliquer : descendre gauche ou droite.
4. Décider le cas limite `arbre vide`.

## Critères de réussite observables
- Une capacité parmi T-ALGO-01E, T-ALGO-01F est citée et utilisée.
- Le résultat attendu est explicite : chercher 6 : 8 -> 3 -> 6.
- Le cas limite `doublon 6` est tranché.

## Lien avec la progression
- Séance : T06-S1 à T06-S4.
- TD : `T06_TD_arbres_binaires_recherche.md`.
- TP : `T06_tp_arbres_binaires_recherche.md`.
- Évaluation : `T06_evaluation_arbres_binaires_recherche.md`.
