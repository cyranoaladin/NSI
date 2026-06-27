---
title: "T07 - Cours - modélisation, listes d’adjacence, matrices"
level: "terminale"
sequence_id: "T07"
document_type: "cours"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Graphes"
notion: "modélisation, listes d’adjacence, matrices"
objectifs:
  - "identifier la donnée de référence"
  - "appliquer la méthode disciplinaire"
  - "produire un résultat vérifiable"
  - "contrôler un cas limite"
private_data: false
official_program:
  capacities:
    - "T-STRUCT-05A"
    - "T-STRUCT-05B"
    - "T-STRUCT-05C"
    - "T-STRUCT-05D"
---

# T07 - Cours - modélisation, listes d’adjacence, matrices

## Objectifs
- Lire la situation sans modifier les données.
- Appliquer une méthode explicitement liée aux capacités.
- Produire un résultat contrôlable.

## Capacités travaillées
- T-STRUCT-05A
- T-STRUCT-05B
- T-STRUCT-05C
- T-STRUCT-05D

## Situation-problème
On modélise un mini-réseau A-B, A-C, B-D, C-D en graphe non orienté.

## Données de référence
`sommets A,B,C,D ; arêtes AB, AC, BD, CD`

## Méthodes disciplinaires
- écrire la liste d’adjacence sans doublon.
- construire la matrice symétrique 4x4.
- comparer coût mémoire liste/matrice.

## Exemple corrigé 1
Donnée : `sommets A,B,C,D ; arêtes AB, AC, BD, CD`.
Méthode : écrire la liste d’adjacence sans doublon.
Résultat : adj[A]=[B,C], adj[B]=[A,D], adj[C]=[A,D], adj[D]=[B,C] ; matrice symétrique avec quatre arêtes.

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
