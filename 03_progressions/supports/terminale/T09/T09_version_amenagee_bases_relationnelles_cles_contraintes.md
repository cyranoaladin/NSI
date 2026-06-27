---
title: "T09 - Version aménagée - relations, clés primaires, clés étrangères, contraintes"
level: "terminale"
sequence_id: "T09"
document_type: "version_amenagee"
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

# T09 - Version aménagée - relations, clés primaires, clés étrangères, contraintes

## Consigne aménagée
Tu travailles sur la donnée suivante : `Livre(1,"1984"), Livre(2,"Dune") ; Emprunt(10,2,"Ada") ; Emprunt(11,9,"Linus") invalide`.

## Étapes guidées
1. Entoure la valeur ou la clé utile.
2. Applique seulement cette méthode : identifier clé primaire id_livre.
3. Compare ton résultat avec : Emprunt 10 est valide ; Emprunt 11 viole la contrainte de clé étrangère car id_livre=9 absent.
4. Explique un cas limite en une phrase.

## Aides graduées
- Aide 1 : relire la donnée et nommer les objets.
- Aide 2 : écrire la première étape de calcul ou de parcours.
- Aide 3 : vérifier le résultat avec la trace fournie par le cours.

## Réponse attendue
La réponse minimale contient la donnée utilisée, l’étape appliquée et le résultat exact.
