---
title: "P06 - TP papier - recherche, tri et fusion de tables"
level: "premiere"
sequence_id: "P06"
document_type: "tp_papier"
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

# P06 - TP papier - recherche, tri et fusion de tables

## Statut du TP
Ce support est un TP papier : aucune ressource Python n’est attendue dans cette passe pour P06. Le livrable est une trace manuscrite ou Markdown avec données, méthode, résultat et contrôle du cas limite.

## Donnée fournie
`inscriptions = [{"id": 17, "nom": "Ada", "atelier": "robot"}, {"id": 4, "nom": "Linus", "atelier": "web"}, {"id": 17, "nom": "Ada", "atelier": "python"}]`

## Travail demandé
1. Recopier la donnée utile sans l’altérer.
2. Appliquer la méthode principale : rechercher la première ligne de clé id=17 sans écraser le doublon.
3. Vérifier le résultat : première ligne id=17 : Ada/robot ; doublon id=17 signalé ; tri : Ada/python, Ada/robot, Linus/web ; absence id=9 notée dans erreurs.
4. Tester un cas limite explicitement.

## Barème associé
- 2 points : donnée de départ correctement identifiée.
- 3 points : méthode appliquée dans le bon ordre.
- 3 points : résultat final exact.
- 2 points : cas limite justifié.

## Corrigé question par question
### Corrigé question 1
Résultat attendu : la donnée utile est `inscriptions = [{"id": 17, "nom": "Ada", "atelier": "robot"}, {"id": 4, "nom": "Linus", "atelier": "web"}, {"id": 17, "nom": "Ada", "atelier": "python"}]`.
### Corrigé question 2
Résultat attendu : la recherche s'arrête sur `{"id": 17, "nom": "Ada", "atelier": "robot"}` et conserve le second `id=17` comme doublon à signaler.
### Corrigé question 3
Résultat attendu : première ligne id=17 : Ada/robot ; doublon id=17 signalé ; tri : Ada/python, Ada/robot, Linus/web ; absence id=9 notée dans erreurs.
### Corrigé question 4
Résultat attendu : si `id=9` est demandé, aucune inscription ne correspond et la liste d'erreurs contient `id absent: 9`.

## Liens
- TD lié : `P06_TD_tables_recherche_tri_fusion.md`.
- Évaluation liée : `P06_evaluation_tables_recherche_tri_fusion.md`.
