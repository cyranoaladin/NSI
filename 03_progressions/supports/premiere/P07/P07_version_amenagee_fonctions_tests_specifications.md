---
title: "P07 - Version aménagée - fonctions, contrats, assertions et tests"
level: "premiere"
sequence_id: "P07"
document_type: "version_amenagee"
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

# P07 - Version aménagée - fonctions, contrats, assertions et tests

## Consigne aménagée
Tu travailles sur la donnée suivante : `prix_ttc(80, 0.20) -> 96.0 ; prix_ttc(0, 0.20) -> 0.0 ; prix_ttc(-5, 0.20) lève AssertionError`.

## Étapes guidées
1. Entoure la valeur ou la clé utile.
2. Applique seulement cette méthode : écrire une signature explicite avec return.
3. Compare ton résultat avec : fonction prix_ttc(ht, taux) retourne round(ht * (1 + taux), 2), refuse ht négatif et garde le cas ht=0.
4. Explique un cas limite en une phrase.

## Aides graduées
- Aide 1 : relire la donnée et nommer les objets.
- Aide 2 : écrire la première étape de calcul ou de parcours.
- Aide 3 : vérifier le résultat avec la trace fournie par le cours.

## Réponse attendue
La réponse minimale contient la donnée utilisée, l’étape appliquée et le résultat exact.
