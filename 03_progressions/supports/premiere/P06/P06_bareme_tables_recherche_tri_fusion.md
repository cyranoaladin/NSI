---
title: "P06 - Barème - recherche, tri et fusion de tables"
level: "premiere"
sequence_id: "P06"
document_type: "bareme"
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

# P06 - Barème - recherche, tri et fusion de tables

## Barème question par question
- Question 1 : 2 points pour la donnée exacte `inscriptions = [{"id": 17, "nom": "Ada", "atelier": "robot"}, {"id": 4, "nom": "Linus", "atelier": "web"}, {"id": 17, "nom": "Ada", "atelier": "python"}]`.
- Question 2 : 3 points pour la méthode `rechercher la première ligne de clé id=17 sans écraser le doublon`.
- Question 3 : 3 points pour le résultat `première ligne id=17 : Ada/robot ; doublon id=17 signalé ; tri : Ada/python, Ada/robot, Linus/web ; absence id=9 notée dans erreurs`.
- Question 4 : 2 points pour un cas limite cohérent.

## Critères observables
- Les capacités évaluées sont : P-TABLE-03, P-TABLE-04.
- Le résultat doit être écrit sous une forme vérifiable, pas seulement commenté.
