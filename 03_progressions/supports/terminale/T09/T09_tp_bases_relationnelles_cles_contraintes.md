---
title: "T09 - TP papier - relations, clés primaires, clés étrangères, contraintes"
level: "terminale"
sequence_id: "T09"
document_type: "tp_papier"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Bases de données relationnelles"
notion: "relations, clés primaires, clés étrangères, contraintes"
objectifs:
  - "identifier la donnée de référence"
  - "appliquer la méthode disciplinaire"
  - "produire un résultat vérifiable"
  - "contrôler un cas limite"
private_data: false
official_program:
  capacities:
    - "T-BDD-01A"
    - "T-BDD-01B"
    - "T-BDD-01C"
    - "T-BDD-02"
---

# T09 - TP papier - relations, clés primaires, clés étrangères, contraintes

## Statut du TP
Ce support est un TP papier : aucune ressource Python n’est attendue dans cette passe pour T09. Le livrable est une trace manuscrite ou Markdown avec données, méthode, résultat et contrôle du cas limite.

## Donnée fournie
`Livre(1,"1984"), Livre(2,"Dune") ; Emprunt(10,2,"Ada") ; Emprunt(11,9,"Linus") invalide`

## Travail demandé
1. Recopier la donnée utile sans l’altérer.
2. Appliquer la méthode principale : identifier clé primaire id_livre.
3. Vérifier le résultat : Emprunt 10 est valide ; Emprunt 11 viole la contrainte de clé étrangère car id_livre=9 absent.
4. Tester un cas limite explicitement.

## Barème associé
- 2 points : donnée de départ correctement identifiée.
- 3 points : méthode appliquée dans le bon ordre.
- 3 points : résultat final exact.
- 2 points : cas limite justifié.

## Corrigé question par question
### Corrigé question 1
Résultat attendu : la donnée utile est `Livre(1,"1984"), Livre(2,"Dune") ; Emprunt(10,2,"Ada") ; Emprunt(11,9,"Linus") invalide`.
### Corrigé question 2
Résultat attendu : `Livre.id_livre` est clé primaire ; `Emprunt.id_livre` est clé étrangère vers `Livre.id_livre`.
### Corrigé question 3
Résultat attendu : Emprunt 10 est valide ; Emprunt 11 viole la contrainte de clé étrangère car id_livre=9 absent.
### Corrigé question 4
Résultat attendu : si `Livre(9,"Fondation")` est ajouté, `Emprunt(11,9,"Linus")` devient valide ; sans cette ligne, la contrainte est violée.

## Liens
- TD lié : `T09_TD_bases_relationnelles_cles_contraintes.md`.
- Évaluation liée : `T09_evaluation_bases_relationnelles_cles_contraintes.md`.
