---
title: "P07 - Cours - fonctions, contrats, assertions et tests"
level: "premiere"
sequence_id: "P07"
document_type: "cours"
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

# P07 - Cours - fonctions, contrats, assertions et tests

## Objectifs
- Lire la situation sans modifier les données.
- Appliquer une méthode explicitement liée aux capacités.
- Produire un résultat contrôlable.

## Capacités travaillées
- P-LANG-01
- P-LANG-02
- P-LANG-03A
- P-LANG-03B
- P-LANG-03C
- P-LANG-04
- P-LANG-05

## Situation-problème
On stabilise la fonction prix_ttc(ht, taux) avec contrat, assertions et tests.

## Données de référence
`prix_ttc(80, 0.20) -> 96.0 ; prix_ttc(0, 0.20) -> 0.0 ; prix_ttc(-5, 0.20) lève AssertionError`

## Méthodes disciplinaires
- écrire une signature explicite avec return.
- rédiger précondition ht >= 0 et taux >= 0.
- tester nominal, zéro et entrée invalide avant généralisation.

## Exemple corrigé 1
Donnée : `prix_ttc(80, 0.20) -> 96.0 ; prix_ttc(0, 0.20) -> 0.0 ; prix_ttc(-5, 0.20) lève AssertionError`.
Méthode : écrire une signature explicite avec return.
Résultat : fonction prix_ttc(ht, taux) retourne round(ht * (1 + taux), 2), refuse ht négatif et garde le cas ht=0.

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
