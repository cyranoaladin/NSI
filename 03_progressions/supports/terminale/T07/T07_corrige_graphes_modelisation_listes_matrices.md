---
title: "T07 - Corrigé - modélisation, listes d’adjacence, matrices"
level: "terminale"
sequence_id: "T07"
document_type: "corrige"
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

# T07 - Corrigé - modélisation, listes d’adjacence, matrices

## Réponse attendue principale
Donnée : `sommets A,B,C,D ; arêtes AB, AC, BD, CD`.
Étapes :
- écrire la liste d’adjacence sans doublon.
- construire la matrice symétrique 4x4.
- comparer coût mémoire liste/matrice.
Résultat final : adj[A]=[B,C], adj[B]=[A,D], adj[C]=[A,D], adj[D]=[B,C] ; matrice symétrique avec quatre arêtes.

## Corrigé des exercices
### Exercice 1
La donnée de référence est recopiée, puis la première méthode est appliquée. Résultat : adj[A]=[B,C], adj[B]=[A,D], adj[C]=[A,D], adj[D]=[B,C] ; matrice symétrique avec quatre arêtes.
### Exercice 2
La variante doit conserver la structure du problème et produire un résultat recalculé.
### Exercice 3
Le cas limite est accepté seulement si la copie indique l’effet exact sur la méthode.
### Exercice 4
La capacité citée doit être reliée à une étape précise du raisonnement.
