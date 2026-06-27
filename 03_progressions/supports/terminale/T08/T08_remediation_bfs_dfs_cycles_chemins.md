---
title: "T08 - Remédiation - BFS, DFS, cycles et chemins"
level: "terminale"
sequence_id: "T08"
document_type: "remediation"
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

# T08 - Remédiation - BFS, DFS, cycles et chemins

## Erreur fréquente 1
Oublier la donnée stable. Activité corrective : surligner dans `file BFS initiale [A] ; pile DFS initiale [A] ; voisins triés alphabétiquement` les valeurs qui pilotent la méthode.

## Erreur fréquente 2
Appliquer une étape dans le mauvais ordre. Activité corrective : remettre ces étapes dans l’ordre : BFS utilise une file et découvre par distance croissante, DFS utilise une pile ou récursion et explore en profondeur, marquer visité pour éviter le cycle A-B-D-C-A.

## Erreur fréquente 3
Donner une conclusion non vérifiable. Activité corrective : retrouver le résultat `BFS découvre A, B, C, D, E et donne distance 3 ; DFS peut suivre A, B, D, E selon ordre choisi` à partir de la donnée.

## Différenciation
- Socle : refaire l’exemple de référence.
- Standard : traiter une valeur modifiée.
- Approfondissement : créer un cas limite et le corriger.
