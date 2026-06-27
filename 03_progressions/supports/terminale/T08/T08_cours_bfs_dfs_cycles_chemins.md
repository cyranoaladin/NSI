---
title: "T08 - Cours - BFS, DFS, cycles et chemins"
level: "terminale"
sequence_id: "T08"
document_type: "cours"
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

# T08 - Cours - BFS, DFS, cycles et chemins

## Objectifs
- Lire la situation sans modifier les données.
- Appliquer une méthode explicitement liée aux capacités.
- Produire un résultat contrôlable.

## Capacités travaillées
- T-ALGO-02A
- T-ALGO-02B
- T-ALGO-02C
- T-ALGO-02D

## Situation-problème
Dans un graphe A-B, A-C, B-D, C-D, D-E, on cherche un chemin de A à E.

## Données de référence
`file BFS initiale [A] ; pile DFS initiale [A] ; voisins triés alphabétiquement`

## Méthodes disciplinaires
- BFS utilise une file et découvre par distance croissante.
- DFS utilise une pile ou récursion et explore en profondeur.
- marquer visité pour éviter le cycle A-B-D-C-A.

## Exemple corrigé 1
Donnée : `file BFS initiale [A] ; pile DFS initiale [A] ; voisins triés alphabétiquement`.
Méthode : BFS utilise une file et découvre par distance croissante.
Résultat : BFS découvre A, B, C, D, E et donne distance 3 ; DFS peut suivre A, B, D, E selon ordre choisi.

## Exemple corrigé 2 - cas limite
On modifie une seule donnée pour tester le cas limite du chapitre. La correction attendue explique pourquoi la méthode reste valable ou pourquoi elle doit refuser l’entrée.

## Erreurs fréquentes
- Confondre une clé, un indice ou un état temporaire avec la donnée stable.
- Conclure sans écrire le résultat contrôlable.
- Oublier le cas vide, absent ou invalide.

## Exercices intégrés
1. Reprendre la donnée de référence et écrire toutes les étapes.
2. Modifier une valeur et prévoir le nouveau résultat.
3. Construire un cas limite et dire si la méthode accepte ou refuse.
4. Relier chaque étape à une capacité officielle.
