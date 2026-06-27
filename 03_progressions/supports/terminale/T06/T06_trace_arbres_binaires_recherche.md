---
title: "T06 - Trace écrite - invariant ABR, recherche et insertion"
level: "terminale"
sequence_id: "T06"
document_type: "trace"
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

# T06 - Trace écrite - invariant ABR, recherche et insertion

## À retenir
- Situation : On insère 7 dans un ABR contenant 8, 3, 10, 1, 6.
- Donnée de référence : `racine 8 ; gauche 3 avec enfants 1 et 6 ; droite 10`.
- Résultat de référence : chemin insertion : 8 -> 3 -> 6 ; parcours infixe après insertion : [1, 3, 6, 7, 8, 10].

## Méthode courte
- suivre les comparaisons 7<8 puis 7>3 puis 7>6.
- placer 7 comme fils droit de 6.
- vérifier le parcours infixe trié.

## Exemple minimal corrigé
Entrée : `racine 8 ; gauche 3 avec enfants 1 et 6 ; droite 10`.
Sortie attendue : chemin insertion : 8 -> 3 -> 6 ; parcours infixe après insertion : [1, 3, 6, 7, 8, 10].

## Point de vigilance
Le résultat doit être calculable à partir de la donnée, sans phrase de validation vague.

## Lien séance
- Séance T06-S1 : découverte et exemple.
- Séance T06-S2 : exercices et correction.
