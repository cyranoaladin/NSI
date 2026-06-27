---
title: "T08 - Corrigé - BFS, DFS, cycles et chemins"
level: "terminale"
sequence_id: "T08"
document_type: "corrige"
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

# T08 - Corrigé - BFS, DFS, cycles et chemins

## Réponse attendue principale
Donnée : `file BFS initiale [A] ; pile DFS initiale [A] ; voisins triés alphabétiquement`.
Étapes :
- BFS utilise une file et découvre par distance croissante.
- DFS utilise une pile ou récursion et explore en profondeur.
- marquer visité pour éviter le cycle A-B-D-C-A.
Résultat final : BFS découvre A, B, C, D, E et donne distance 3 ; DFS peut suivre A, B, D, E selon ordre choisi.

## Corrigé des exercices
### Exercice 1
La donnée de référence est recopiée, puis la première méthode est appliquée. Résultat : BFS découvre A, B, C, D, E et donne distance 3 ; DFS peut suivre A, B, D, E selon ordre choisi.
### Exercice 2
La variante doit conserver la structure du problème et produire un résultat recalculé.
### Exercice 3
Le cas limite est accepté seulement si la copie indique l’effet exact sur la méthode.
### Exercice 4
La capacité citée doit être reliée à une étape précise du raisonnement.
