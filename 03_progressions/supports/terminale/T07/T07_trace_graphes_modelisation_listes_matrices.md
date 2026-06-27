---
title: "T07 - Trace écrite - modélisation, listes d’adjacence, matrices"
level: "terminale"
sequence_id: "T07"
document_type: "trace"
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

# T07 - Trace écrite - modélisation, listes d’adjacence, matrices

## À retenir
- Situation : On modélise un mini-réseau A-B, A-C, B-D, C-D en graphe non orienté.
- Donnée de référence : `sommets A,B,C,D ; arêtes AB, AC, BD, CD`.
- Résultat de référence : adj[A]=[B,C], adj[B]=[A,D], adj[C]=[A,D], adj[D]=[B,C] ; matrice symétrique avec quatre arêtes.

## Méthode courte
- écrire la liste d’adjacence sans doublon.
- construire la matrice symétrique 4x4.
- comparer coût mémoire liste/matrice.

## Exemple minimal corrigé
Entrée : `sommets A,B,C,D ; arêtes AB, AC, BD, CD`.
Sortie attendue : adj[A]=[B,C], adj[B]=[A,D], adj[C]=[A,D], adj[D]=[B,C] ; matrice symétrique avec quatre arêtes.

## Point de vigilance
Le résultat doit être calculable à partir de la donnée, sans phrase de validation vague.

## Lien séance
- Séance T07-S1 : découverte et exemple.
- Séance T07-S2 : exercices et correction.
