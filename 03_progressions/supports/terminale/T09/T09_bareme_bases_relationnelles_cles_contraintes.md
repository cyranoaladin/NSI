---
title: "T09 - Barème - relations, clés primaires, clés étrangères, contraintes"
level: "terminale"
sequence_id: "T09"
document_type: "bareme"
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

# T09 - Barème - relations, clés primaires, clés étrangères, contraintes

## Barème question par question
- Question 1 : 2 points pour la donnée exacte `Livre(1,"1984"), Livre(2,"Dune") ; Emprunt(10,2,"Ada") ; Emprunt(11,9,"Linus") invalide`.
- Question 2 : 3 points pour la méthode `identifier clé primaire id_livre`.
- Question 3 : 3 points pour le résultat `Emprunt 10 est valide ; Emprunt 11 viole la contrainte de clé étrangère car id_livre=9 absent`.
- Question 4 : 2 points pour un cas limite cohérent.

## Critères observables
- Les capacités évaluées sont : T-BDD-01A, T-BDD-01B, T-BDD-01C, T-BDD-02.
- Le résultat doit être écrit sous une forme vérifiable, pas seulement commenté.
