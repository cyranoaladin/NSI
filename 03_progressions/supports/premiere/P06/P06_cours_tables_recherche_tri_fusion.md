---
title: "P06 - Cours - recherche, tri et fusion de tables"
level: "premiere"
sequence_id: "P06"
document_type: "cours"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Traitement de tables"
notion: "recherche, tri et fusion de tables"
objectifs:
  - "identifier la donnée de référence"
  - "appliquer la méthode disciplinaire"
  - "produire un résultat vérifiable"
  - "contrôler un cas limite"
private_data: false
official_program:
  capacities:
    - "P-TABLE-03"
    - "P-TABLE-04"
---

# P06 - Cours - recherche, tri et fusion de tables

## Objectifs
- Lire la situation sans modifier les données.
- Appliquer une méthode explicitement liée aux capacités.
- Produire un résultat contrôlable.

## Capacités travaillées
- P-TABLE-03
- P-TABLE-04

## Situation-problème
Une association fusionne une table inscriptions et une table présences avec la clé id.

## Données de référence
`inscriptions = [{"id": 17, "nom": "Ada", "atelier": "robot"}, {"id": 4, "nom": "Linus", "atelier": "web"}, {"id": 17, "nom": "Ada", "atelier": "python"}]`

## Méthodes disciplinaires
- rechercher la première ligne de clé id=17 sans écraser le doublon.
- trier par (nom, atelier).
- fusionner inscriptions et présences avec vérification des clés absentes.

## Exemple corrigé 1
Donnée : `inscriptions = [{"id": 17, "nom": "Ada", "atelier": "robot"}, {"id": 4, "nom": "Linus", "atelier": "web"}, {"id": 17, "nom": "Ada", "atelier": "python"}]`.
Méthode : rechercher la première ligne de clé id=17 sans écraser le doublon.
Résultat : première ligne id=17 : Ada/robot ; doublon id=17 signalé ; tri : Ada/python, Ada/robot, Linus/web ; absence id=9 notée dans erreurs.

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
