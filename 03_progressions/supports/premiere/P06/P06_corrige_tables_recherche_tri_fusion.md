---
title: "P06 - Corrigé - recherche, tri et fusion de tables"
level: "premiere"
sequence_id: "P06"
document_type: "corrige"
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

# P06 - Corrigé - recherche, tri et fusion de tables

## Réponse attendue principale
Donnée : `inscriptions = [{"id": 17, "nom": "Ada", "atelier": "robot"}, {"id": 4, "nom": "Linus", "atelier": "web"}, {"id": 17, "nom": "Ada", "atelier": "python"}]`.
Étapes :
- rechercher la première ligne de clé id=17 sans écraser le doublon.
- trier par (nom, atelier).
- fusionner inscriptions et présences avec vérification des clés absentes.
Résultat final : première ligne id=17 : Ada/robot ; doublon id=17 signalé ; tri : Ada/python, Ada/robot, Linus/web ; absence id=9 notée dans erreurs.

## Corrigé des exercices
### Exercice 1
La donnée de référence est recopiée, puis la première méthode est appliquée. Résultat : première ligne id=17 : Ada/robot ; doublon id=17 signalé ; tri : Ada/python, Ada/robot, Linus/web ; absence id=9 notée dans erreurs.
### Exercice 2
La variante doit conserver la structure du problème et produire un résultat recalculé.
### Exercice 3
Le cas limite est accepté seulement si la copie indique l’effet exact sur la méthode.
### Exercice 4
La capacité citée doit être reliée à une étape précise du raisonnement.
