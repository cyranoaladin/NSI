---
title: "T09 - Trace écrite - relations, clés primaires, clés étrangères, contraintes"
level: "terminale"
sequence_id: "T09"
document_type: "trace"
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

# T09 - Trace écrite - relations, clés primaires, clés étrangères, contraintes

## À retenir
- Situation : Une base bibliothèque relie Livre(id_livre,titre) et Emprunt(id_emprunt,id_livre,lecteur).
- Donnée de référence : `Livre(1,"1984"), Livre(2,"Dune") ; Emprunt(10,2,"Ada") ; Emprunt(11,9,"Linus") invalide`.
- Résultat de référence : Emprunt 10 est valide ; Emprunt 11 viole la contrainte de clé étrangère car id_livre=9 absent.

## Méthode courte
- identifier clé primaire id_livre.
- vérifier clé étrangère Emprunt.id_livre vers Livre.id_livre.
- refuser un emprunt sur livre absent.

## Exemple minimal corrigé
Entrée : `Livre(1,"1984"), Livre(2,"Dune") ; Emprunt(10,2,"Ada") ; Emprunt(11,9,"Linus") invalide`.
Sortie attendue : Emprunt 10 est valide ; Emprunt 11 viole la contrainte de clé étrangère car id_livre=9 absent.

## Point de vigilance
Le résultat doit être calculable à partir de la donnée, sans phrase de validation vague.

## Lien séance
- Séance T09-S1 : découverte et exemple.
- Séance T09-S2 : exercices et correction.
