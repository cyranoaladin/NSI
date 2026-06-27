---
title: "T09 - cours - bases relationnelles, clés et contraintes"
level: "terminale"
sequence_id: "T09"
document_type: "cours"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "bases relationnelles, clés et contraintes"
notion: "bases relationnelles, clés et contraintes"
private_data: false
official_program:
  capacities:
    - "T-BDD-01A"
    - "T-BDD-01B"
    - "T-BDD-01C"
    - "T-BDD-02"
---

# T09 - Cours - bases relationnelles, clés et contraintes

## Objectifs spécifiques
- Identifier les données utiles de la situation : Livre(1,Dune), Livre(2,Fondation) ; Emprunt(10,1,Nora), Emprunt(11,9,Sam) invalide.
- Employer le vocabulaire : relation, attribut, tuple, clé primaire, clé étrangère, contrainte de domaine.
- Produire une trace, une table, une valeur ou un pseudo-code vérifiable.

## Capacités officielles
- T-BDD-01A.
- T-BDD-01B.
- T-BDD-01C.
- T-BDD-02.

## Situation-problème
Livre(1,Dune), Livre(2,Fondation) ; Emprunt(10,1,Nora), Emprunt(11,9,Sam) invalide

## À savoir
- relation.
- attribut.
- tuple.
- clé primaire.
- clé étrangère.
- contrainte de domaine.
- contrainte de référence.
- schéma.
- instance.
- anomalie.

## Méthodes
- identifier schéma et instance.
- vérifier unicité id_livre.
- contrôler Emprunt.id_livre.
- repérer id_livre=9 absent.

## Exemples corrigés
### Exemple corrigé 1
- Donnée : `Livre(1,Dune), Livre(2,Fondation) ; Emprunt(10,1,Nora), Emprunt(11,9,Sam) invalide`.
- Méthode : identifier schéma et instance.
- Résultat attendu : Livre.id_livre identifie chaque livre.
- Contrôle : capacité T-BDD-01A et cas limite `clé primaire nulle`.
### Exemple corrigé 2
- Donnée : `Livre(1,Dune), Livre(2,Fondation) ; Emprunt(10,1,Nora), Emprunt(11,9,Sam) invalide`.
- Méthode : vérifier unicité id_livre.
- Résultat attendu : Emprunt.id_livre référence Livre.id_livre.
- Contrôle : capacité T-BDD-01B et cas limite `doublon id_livre=1`.
### Exemple corrigé 3
- Donnée : `Livre(1,Dune), Livre(2,Fondation) ; Emprunt(10,1,Nora), Emprunt(11,9,Sam) invalide`.
- Méthode : contrôler Emprunt.id_livre.
- Résultat attendu : Emprunt(11,9,Sam) viole la référence.
- Contrôle : capacité T-BDD-01C et cas limite `suppression référencée`.
### Exemple corrigé 4
- Donnée : `Livre(1,Dune), Livre(2,Fondation) ; Emprunt(10,1,Nora), Emprunt(11,9,Sam) invalide`.
- Méthode : repérer id_livre=9 absent.
- Résultat attendu : suppression d un livre emprunté refusée.
- Contrôle : capacité T-BDD-02 et cas limite `clé primaire nulle`.

## Cas limites
- clé primaire nulle.
- doublon id_livre=1.
- suppression référencée.

## Erreurs fréquentes
- attribut confondu avec valeur.
- clé étrangère supposée unique.
- domaine ignoré.

## Exercices intégrés
1. Identifier les données utiles dans `Livre(1,Dune), Livre(2,Fondation) ; Emprunt(10,1,Nora), Emprunt(11,9,Sam) invalide`.
2. Appliquer : identifier schéma et instance.
3. Appliquer : vérifier unicité id_livre.
4. Décider le cas limite `clé primaire nulle`.

## Critères de réussite observables
- Une capacité parmi T-BDD-01A, T-BDD-01B, T-BDD-01C, T-BDD-02 est citée et utilisée.
- Le résultat attendu est explicite : Livre.id_livre identifie chaque livre.
- Le cas limite `doublon id_livre=1` est tranché.

## Lien avec la progression
- Séance : T09-S1 à T09-S4.
- TD : `T09_TD_bases_relationnelles_cles_contraintes.md`.
- TP : `T09_tp_bases_relationnelles_cles_contraintes.md`.
- Évaluation : `T09_evaluation_bases_relationnelles_cles_contraintes.md`.
