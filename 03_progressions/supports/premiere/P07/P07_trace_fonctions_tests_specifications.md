---
title: "P07 - Trace écrite - fonctions, contrats, assertions et tests"
level: "premiere"
sequence_id: "P07"
document_type: "trace"
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

# P07 - Trace écrite - fonctions, contrats, assertions et tests

## À retenir
- Situation : On stabilise la fonction prix_ttc(ht, taux) avec contrat, assertions et tests.
- Donnée de référence : `prix_ttc(80, 0.20) -> 96.0 ; prix_ttc(0, 0.20) -> 0.0 ; prix_ttc(-5, 0.20) lève AssertionError`.
- Résultat de référence : fonction prix_ttc(ht, taux) retourne round(ht * (1 + taux), 2), refuse ht négatif et garde le cas ht=0.

## Méthode courte
- écrire une signature explicite avec return.
- rédiger précondition ht >= 0 et taux >= 0.
- tester nominal, zéro et entrée invalide avant généralisation.

## Exemple minimal corrigé
Entrée : `prix_ttc(80, 0.20) -> 96.0 ; prix_ttc(0, 0.20) -> 0.0 ; prix_ttc(-5, 0.20) lève AssertionError`.
Sortie attendue : fonction prix_ttc(ht, taux) retourne round(ht * (1 + taux), 2), refuse ht négatif et garde le cas ht=0.

## Point de vigilance
Le résultat doit être calculable à partir de la donnée, sans phrase de validation vague.

## Lien séance
- Séance P07-S1 : découverte et exemple.
- Séance P07-S2 : exercices et correction.
