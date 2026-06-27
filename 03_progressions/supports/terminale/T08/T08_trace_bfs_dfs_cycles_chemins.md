---
title: "T08 - Trace écrite - BFS, DFS, cycles et chemins"
level: "terminale"
sequence_id: "T08"
document_type: "trace"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Graphes et parcours"
notion: "BFS, DFS, cycles et chemins"
objectifs:
  - "identifier la donnée de référence"
  - "appliquer la méthode disciplinaire"
  - "produire un résultat vérifiable"
  - "contrôler un cas limite"
private_data: false
official_program:
  capacities:
    - "T-ALGO-02A"
    - "T-ALGO-02B"
    - "T-ALGO-02C"
    - "T-ALGO-02D"
---

# T08 - Trace écrite - BFS, DFS, cycles et chemins

## À retenir
- Situation : Dans un graphe A-B, A-C, B-D, C-D, D-E, on cherche un chemin de A à E.
- Donnée de référence : `file BFS initiale [A] ; pile DFS initiale [A] ; voisins triés alphabétiquement`.
- Résultat de référence : BFS découvre A, B, C, D, E et donne distance 3 ; DFS peut suivre A, B, D, E selon ordre choisi.

## Méthode courte
- BFS utilise une file et découvre par distance croissante.
- DFS utilise une pile ou récursion et explore en profondeur.
- marquer visité pour éviter le cycle A-B-D-C-A.

## Exemple minimal corrigé
Entrée : `file BFS initiale [A] ; pile DFS initiale [A] ; voisins triés alphabétiquement`.
Sortie attendue : BFS découvre A, B, C, D, E et donne distance 3 ; DFS peut suivre A, B, D, E selon ordre choisi.

## Point de vigilance
Le résultat doit être calculable à partir de la donnée, sans phrase de validation vague.

## Lien séance
- Séance T08-S1 : découverte et exemple.
- Séance T08-S2 : exercices et correction.
