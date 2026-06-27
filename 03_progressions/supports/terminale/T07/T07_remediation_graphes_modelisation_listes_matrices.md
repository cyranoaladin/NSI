---
title: "T07 - Remédiation - modélisation, listes d’adjacence, matrices"
level: "terminale"
sequence_id: "T07"
document_type: "remediation"
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

# T07 - Remédiation - modélisation, listes d’adjacence, matrices

## Erreur fréquente 1
Oublier la donnée stable. Activité corrective : surligner dans `sommets A,B,C,D ; arêtes AB, AC, BD, CD` les valeurs qui pilotent la méthode.

## Erreur fréquente 2
Appliquer une étape dans le mauvais ordre. Activité corrective : remettre ces étapes dans l’ordre : écrire la liste d’adjacence sans doublon, construire la matrice symétrique 4x4, comparer coût mémoire liste/matrice.

## Erreur fréquente 3
Donner une conclusion non vérifiable. Activité corrective : retrouver le résultat `adj[A]=[B,C], adj[B]=[A,D], adj[C]=[A,D], adj[D]=[B,C] ; matrice symétrique avec quatre arêtes` à partir de la donnée.

## Différenciation
- Socle : refaire l’exemple de référence.
- Standard : traiter une valeur modifiée.
- Approfondissement : créer un cas limite et le corriger.
