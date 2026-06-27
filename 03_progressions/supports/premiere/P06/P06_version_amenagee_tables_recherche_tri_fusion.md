---
title: "P06 - Version aménagée - recherche, tri et fusion de tables"
level: "premiere"
sequence_id: "P06"
document_type: "version_amenagee"
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

# P06 - Version aménagée - recherche, tri et fusion de tables

## Consigne aménagée
Tu travailles sur la donnée suivante : `inscriptions = [{"id": 17, "nom": "Ada", "atelier": "robot"}, {"id": 4, "nom": "Linus", "atelier": "web"}, {"id": 17, "nom": "Ada", "atelier": "python"}]`.

## Étapes guidées
1. Entoure la valeur ou la clé utile.
2. Applique seulement cette méthode : rechercher la première ligne de clé id=17 sans écraser le doublon.
3. Compare ton résultat avec : première ligne id=17 : Ada/robot ; doublon id=17 signalé ; tri : Ada/python, Ada/robot, Linus/web ; absence id=9 notée dans erreurs.
4. Explique un cas limite en une phrase.

## Aides graduées
- Aide 1 : relire la donnée et nommer les objets.
- Aide 2 : écrire la première étape de calcul ou de parcours.
- Aide 3 : vérifier le résultat avec la trace fournie par le cours.

## Réponse attendue
La réponse minimale contient la donnée utilisée, l’étape appliquée et le résultat exact.
