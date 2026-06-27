---
title: "P07 - Corrigé - fonctions, contrats, assertions et tests"
level: "premiere"
sequence_id: "P07"
document_type: "corrige"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Langage Python"
notion: "fonctions, contrats, assertions et tests"
objectifs:
  - "identifier la donnée de référence"
  - "appliquer la méthode disciplinaire"
  - "produire un résultat vérifiable"
  - "contrôler un cas limite"
private_data: false
official_program:
  capacities:
    - "P-LANG-01"
    - "P-LANG-02"
    - "P-LANG-03A"
    - "P-LANG-03B"
    - "P-LANG-03C"
    - "P-LANG-04"
    - "P-LANG-05"
---

# P07 - Corrigé - fonctions, contrats, assertions et tests

## Réponse attendue principale
Donnée : `prix_ttc(80, 0.20) -> 96.0 ; prix_ttc(0, 0.20) -> 0.0 ; prix_ttc(-5, 0.20) lève AssertionError`.
Étapes :
- écrire une signature explicite avec return.
- rédiger précondition ht >= 0 et taux >= 0.
- tester nominal, zéro et entrée invalide avant généralisation.
Résultat final : fonction prix_ttc(ht, taux) retourne round(ht * (1 + taux), 2), refuse ht négatif et garde le cas ht=0.

## Corrigé des exercices
### Exercice 1
La donnée de référence est recopiée, puis la première méthode est appliquée. Résultat : fonction prix_ttc(ht, taux) retourne round(ht * (1 + taux), 2), refuse ht négatif et garde le cas ht=0.
### Exercice 2
La variante doit conserver la structure du problème et produire un résultat recalculé.
### Exercice 3
Le cas limite est accepté seulement si la copie indique l’effet exact sur la méthode.
### Exercice 4
La capacité citée doit être reliée à une étape précise du raisonnement.
