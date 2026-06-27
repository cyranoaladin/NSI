---
title: "T07 - cours - graphes, listes et matrices"
level: "terminale"
sequence_id: "T07"
document_type: "cours"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "graphes, listes et matrices"
notion: "graphes, listes et matrices"
private_data: false
official_program:
  capacities:
    - "T-STRUCT-05A"
    - "T-STRUCT-05B"
    - "T-STRUCT-05C"
    - "T-STRUCT-05D"
---

# T07 - Cours - graphes, listes et matrices

## Objectifs spécifiques
- Identifier les données utiles de la situation : arcs=[(A,B),(A,C),(B,D),(C,D),(D,B)].
- Employer le vocabulaire : graphe orienté, graphe non orienté, liste d adjacence, matrice d adjacence, degré, voisinage.
- Produire une trace, une table, une valeur ou un pseudo-code vérifiable.

## Capacités officielles
- T-STRUCT-05A.
- T-STRUCT-05B.
- T-STRUCT-05C.
- T-STRUCT-05D.

## Situation-problème
arcs=[(A,B),(A,C),(B,D),(C,D),(D,B)]

## À savoir
- graphe orienté.
- graphe non orienté.
- liste d adjacence.
- matrice d adjacence.
- degré.
- voisinage.
- coût mémoire.

## Méthodes
- lister voisins sortants.
- remplir matrice 0/1.
- calculer degré sortant.
- choisir liste pour graphe peu dense.

## Exemples corrigés
### Exemple corrigé 1
- Donnée : `arcs=[(A,B),(A,C),(B,D),(C,D),(D,B)]`.
- Méthode : lister voisins sortants.
- Résultat attendu : A -> [B,C], B -> [D], C -> [D], D -> [B].
- Contrôle : capacité T-STRUCT-05A et cas limite `sommet isolé E`.
### Exemple corrigé 2
- Donnée : `arcs=[(A,B),(A,C),(B,D),(C,D),(D,B)]`.
- Méthode : remplir matrice 0/1.
- Résultat attendu : ligne A : colonnes B et C valent 1.
- Contrôle : capacité T-STRUCT-05B et cas limite `boucle A->A`.
### Exemple corrigé 3
- Donnée : `arcs=[(A,B),(A,C),(B,D),(C,D),(D,B)]`.
- Méthode : calculer degré sortant.
- Résultat attendu : matrice 4x4 -> 16 cases.
- Contrôle : capacité T-STRUCT-05C et cas limite `arête non orientée`.
### Exemple corrigé 4
- Donnée : `arcs=[(A,B),(A,C),(B,D),(C,D),(D,B)]`.
- Méthode : choisir liste pour graphe peu dense.
- Résultat attendu : sommet E isolé -> liste vide.
- Contrôle : capacité T-STRUCT-05D et cas limite `sommet isolé E`.

## Cas limites
- sommet isolé E.
- boucle A->A.
- arête non orientée.

## Erreurs fréquentes
- voisin entrant confondu.
- sommet isolé oublié.
- coût mémoire ignoré.

## Exercices intégrés
1. Identifier les données utiles dans `arcs=[(A,B),(A,C),(B,D),(C,D),(D,B)]`.
2. Appliquer : lister voisins sortants.
3. Appliquer : remplir matrice 0/1.
4. Décider le cas limite `sommet isolé E`.

## Critères de réussite observables
- Une capacité parmi T-STRUCT-05A, T-STRUCT-05B, T-STRUCT-05C, T-STRUCT-05D est citée et utilisée.
- Le résultat attendu est explicite : A -> [B,C], B -> [D], C -> [D], D -> [B].
- Le cas limite `boucle A->A` est tranché.

## Lien avec la progression
- Séance : T07-S1 à T07-S4.
- TD : `T07_TD_graphes_modelisation_listes_matrices.md`.
- TP : `T07_tp_graphes_modelisation_listes_matrices.md`.
- Évaluation : `T07_evaluation_graphes_modelisation_listes_matrices.md`.
