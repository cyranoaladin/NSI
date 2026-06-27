---
title: "P06 - Trace écrite - recherche, tri et fusion de tables"
level: "premiere"
sequence_id: "P06"
document_type: "trace"
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

# P06 - Trace écrite - recherche, tri et fusion de tables

## À retenir
- Situation : Une association fusionne une table inscriptions et une table présences avec la clé id.
- Donnée de référence : `inscriptions = [{"id": 17, "nom": "Ada", "atelier": "robot"}, {"id": 4, "nom": "Linus", "atelier": "web"}, {"id": 17, "nom": "Ada", "atelier": "python"}]`.
- Résultat de référence : première ligne id=17 : Ada/robot ; doublon id=17 signalé ; tri : Ada/python, Ada/robot, Linus/web ; absence id=9 notée dans erreurs.

## Méthode courte
- rechercher la première ligne de clé id=17 sans écraser le doublon.
- trier par (nom, atelier).
- fusionner inscriptions et présences avec vérification des clés absentes.

## Exemple minimal corrigé
Entrée : `inscriptions = [{"id": 17, "nom": "Ada", "atelier": "robot"}, {"id": 4, "nom": "Linus", "atelier": "web"}, {"id": 17, "nom": "Ada", "atelier": "python"}]`.
Sortie attendue : première ligne id=17 : Ada/robot ; doublon id=17 signalé ; tri : Ada/python, Ada/robot, Linus/web ; absence id=9 notée dans erreurs.

## Point de vigilance
Le résultat doit être calculable à partir de la donnée, sans phrase de validation vague.

## Lien séance
- Séance P06-S1 : découverte et exemple.
- Séance P06-S2 : exercices et correction.
