---
title: "T06 - Remédiation - invariant ABR, recherche et insertion"
level: "terminale"
sequence_id: "T06"
document_type: "remediation"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Arbres binaires de recherche"
notion: "invariant ABR, recherche et insertion"
objectifs:
  - "identifier la donnée de référence"
  - "appliquer la méthode disciplinaire"
  - "produire un résultat vérifiable"
  - "contrôler un cas limite"
private_data: false
official_program:
  capacities:
    - "T-ALGO-01E"
    - "T-ALGO-01F"
---

# T06 - Remédiation - invariant ABR, recherche et insertion

## Erreur fréquente 1
Oublier la donnée stable. Activité corrective : surligner dans `racine 8 ; gauche 3 avec enfants 1 et 6 ; droite 10` les valeurs qui pilotent la méthode.

## Erreur fréquente 2
Appliquer une étape dans le mauvais ordre. Activité corrective : remettre ces étapes dans l’ordre : suivre les comparaisons 7<8 puis 7>3 puis 7>6, placer 7 comme fils droit de 6, vérifier le parcours infixe trié.

## Erreur fréquente 3
Donner une conclusion non vérifiable. Activité corrective : retrouver le résultat `chemin insertion : 8 -> 3 -> 6 ; parcours infixe après insertion : [1, 3, 6, 7, 8, 10]` à partir de la donnée.

## Différenciation
- Socle : refaire l’exemple de référence.
- Standard : traiter une valeur modifiée.
- Approfondissement : créer un cas limite et le corriger.
