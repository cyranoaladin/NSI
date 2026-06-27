---
title: "P06 - Remédiation - recherche, tri et fusion de tables"
level: "premiere"
sequence_id: "P06"
document_type: "remediation"
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

# P06 - Remédiation - recherche, tri et fusion de tables

## Erreur fréquente 1
Oublier la donnée stable. Activité corrective : surligner dans `inscriptions = [{"id": 17, "nom": "Ada", "atelier": "robot"}, {"id": 4, "nom": "Linus", "atelier": "web"}, {"id": 17, "nom": "Ada", "atelier": "python"}]` les valeurs qui pilotent la méthode.

## Erreur fréquente 2
Appliquer une étape dans le mauvais ordre. Activité corrective : remettre ces étapes dans l’ordre : rechercher la première ligne de clé id=17 sans écraser le doublon, trier par (nom, atelier), fusionner inscriptions et présences avec vérification des clés absentes.

## Erreur fréquente 3
Donner une conclusion non vérifiable. Activité corrective : retrouver le résultat `première ligne id=17 : Ada/robot ; doublon id=17 signalé ; tri : Ada/python, Ada/robot, Linus/web ; absence id=9 notée dans erreurs` à partir de la donnée.

## Différenciation
- Socle : refaire l’exemple de référence.
- Standard : traiter une valeur modifiée.
- Approfondissement : créer un cas limite et le corriger.
