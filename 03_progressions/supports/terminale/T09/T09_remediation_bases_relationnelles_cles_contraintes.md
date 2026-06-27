---
title: "T09 - Remédiation - relations, clés primaires, clés étrangères, contraintes"
level: "terminale"
sequence_id: "T09"
document_type: "remediation"
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

# T09 - Remédiation - relations, clés primaires, clés étrangères, contraintes

## Erreur fréquente 1
Oublier la donnée stable. Activité corrective : surligner dans `Livre(1,"1984"), Livre(2,"Dune") ; Emprunt(10,2,"Ada") ; Emprunt(11,9,"Linus") invalide` les valeurs qui pilotent la méthode.

## Erreur fréquente 2
Appliquer une étape dans le mauvais ordre. Activité corrective : remettre ces étapes dans l’ordre : identifier clé primaire id_livre, vérifier clé étrangère Emprunt.id_livre vers Livre.id_livre, refuser un emprunt sur livre absent.

## Erreur fréquente 3
Donner une conclusion non vérifiable. Activité corrective : retrouver le résultat `Emprunt 10 est valide ; Emprunt 11 viole la contrainte de clé étrangère car id_livre=9 absent` à partir de la donnée.

## Différenciation
- Socle : refaire l’exemple de référence.
- Standard : traiter une valeur modifiée.
- Approfondissement : créer un cas limite et le corriger.
