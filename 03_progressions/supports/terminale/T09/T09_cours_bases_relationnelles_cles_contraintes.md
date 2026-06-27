---
title: "T09 - Cours - relations, clés primaires, clés étrangères, contraintes"
level: "terminale"
sequence_id: "T09"
document_type: "cours"
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

# T09 - Cours - relations, clés primaires, clés étrangères, contraintes

## Objectifs
- Lire la situation sans modifier les données.
- Appliquer une méthode explicitement liée aux capacités.
- Produire un résultat contrôlable.

## Capacités travaillées
- T-BDD-01A
- T-BDD-01B
- T-BDD-01C
- T-BDD-02

## Situation-problème
Une base bibliothèque relie Livre(id_livre,titre) et Emprunt(id_emprunt,id_livre,lecteur).

## Données de référence
`Livre(1,"1984"), Livre(2,"Dune") ; Emprunt(10,2,"Ada") ; Emprunt(11,9,"Linus") invalide`

## Méthodes disciplinaires
- identifier clé primaire id_livre.
- vérifier clé étrangère Emprunt.id_livre vers Livre.id_livre.
- refuser un emprunt sur livre absent.

## Exemple corrigé 1
Donnée : `Livre(1,"1984"), Livre(2,"Dune") ; Emprunt(10,2,"Ada") ; Emprunt(11,9,"Linus") invalide`.
Méthode : identifier clé primaire id_livre.
Résultat : Emprunt 10 est valide ; Emprunt 11 viole la contrainte de clé étrangère car id_livre=9 absent.

## Exemple corrigé 2 - cas limite
On modifie une seule donnée pour tester le cas limite du chapitre. La correction attendue explique pourquoi la méthode reste valable ou pourquoi elle doit refuser l’entrée.

## Erreurs fréquentes
- Confondre une clé, un indice ou un état temporaire avec la donnée stable.
- Conclure sans écrire le résultat contrôlable.
- Oublier le cas vide, absent ou invalide.

## Exercices intégrés
1. Reprendre la donnée de référence et écrire toutes les étapes.
2. Modifier une valeur et prévoir le nouveau résultat.
3. Construire un cas limite et dire si la méthode accepte ou refuse.
4. Relier chaque étape à une capacité officielle.
