---
title: "T09 - Corrigé - relations, clés primaires, clés étrangères, contraintes"
level: "terminale"
sequence_id: "T09"
document_type: "corrige"
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

# T09 - Corrigé - relations, clés primaires, clés étrangères, contraintes

## Réponse attendue principale
Donnée : `Livre(1,"1984"), Livre(2,"Dune") ; Emprunt(10,2,"Ada") ; Emprunt(11,9,"Linus") invalide`.
Étapes :
- identifier clé primaire id_livre.
- vérifier clé étrangère Emprunt.id_livre vers Livre.id_livre.
- refuser un emprunt sur livre absent.
Résultat final : Emprunt 10 est valide ; Emprunt 11 viole la contrainte de clé étrangère car id_livre=9 absent.

## Corrigé des exercices
### Exercice 1
La donnée de référence est recopiée, puis la première méthode est appliquée. Résultat : Emprunt 10 est valide ; Emprunt 11 viole la contrainte de clé étrangère car id_livre=9 absent.
### Exercice 2
La variante doit conserver la structure du problème et produire un résultat recalculé.
### Exercice 3
Le cas limite est accepté seulement si la copie indique l’effet exact sur la méthode.
### Exercice 4
La capacité citée doit être reliée à une étape précise du raisonnement.
