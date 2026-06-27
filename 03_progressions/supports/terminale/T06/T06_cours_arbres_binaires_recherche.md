---
title: "T06 - Cours - invariant ABR, recherche et insertion"
level: "terminale"
sequence_id: "T06"
document_type: "cours"
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

# T06 - Cours - invariant ABR, recherche et insertion

## Objectifs
- Lire la situation sans modifier les données.
- Appliquer une méthode explicitement liée aux capacités.
- Produire un résultat contrôlable.

## Capacités travaillées
- T-ALGO-01E
- T-ALGO-01F

## Situation-problème
On insère 7 dans un ABR contenant 8, 3, 10, 1, 6.

## Données de référence
`racine 8 ; gauche 3 avec enfants 1 et 6 ; droite 10`

## Méthodes disciplinaires
- suivre les comparaisons 7<8 puis 7>3 puis 7>6.
- placer 7 comme fils droit de 6.
- vérifier le parcours infixe trié.

## Exemple corrigé 1
Donnée : `racine 8 ; gauche 3 avec enfants 1 et 6 ; droite 10`.
Méthode : suivre les comparaisons 7<8 puis 7>3 puis 7>6.
Résultat : chemin insertion : 8 -> 3 -> 6 ; parcours infixe après insertion : [1, 3, 6, 7, 8, 10].

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
