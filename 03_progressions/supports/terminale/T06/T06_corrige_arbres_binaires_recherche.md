---
title: "T06 - Corrigé - invariant ABR, recherche et insertion"
level: "terminale"
sequence_id: "T06"
document_type: "corrige"
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

# T06 - Corrigé - invariant ABR, recherche et insertion

## Réponse attendue principale
Donnée : `racine 8 ; gauche 3 avec enfants 1 et 6 ; droite 10`.
Étapes :
- suivre les comparaisons 7<8 puis 7>3 puis 7>6.
- placer 7 comme fils droit de 6.
- vérifier le parcours infixe trié.
Résultat final : chemin insertion : 8 -> 3 -> 6 ; parcours infixe après insertion : [1, 3, 6, 7, 8, 10].

## Corrigé des exercices
### Exercice 1
La donnée de référence est recopiée, puis la première méthode est appliquée. Résultat : chemin insertion : 8 -> 3 -> 6 ; parcours infixe après insertion : [1, 3, 6, 7, 8, 10].
### Exercice 2
La variante doit conserver la structure du problème et produire un résultat recalculé.
### Exercice 3
Le cas limite est accepté seulement si la copie indique l’effet exact sur la méthode.
### Exercice 4
La capacité citée doit être reliée à une étape précise du raisonnement.
