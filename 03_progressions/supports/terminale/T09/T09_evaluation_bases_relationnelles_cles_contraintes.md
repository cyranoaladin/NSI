---
title: "T09 - evaluation - bases relationnelles, clés et contraintes"
level: "terminale"
sequence_id: "T09"
document_type: "evaluation"
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

# T09 - Évaluation - bases relationnelles, clés et contraintes

## Modalités
- Durée : 30 minutes.
- Matériel autorisé : fiche de cours.
- Capacités évaluées : T-BDD-01A, T-BDD-01B, T-BDD-01C, T-BDD-02.

## Questions
### Question 1
- Capacité officielle : T-BDD-01A.
- Énoncé : à partir de `Livre(1,Dune), Livre(2,Fondation) ; Emprunt(10,1,Nora), Emprunt(11,9,Sam) invalide`, identifier schéma et instance.
- Réponse attendue : Livre.id_livre identifie chaque livre.
- Barème : 1 point donnée, 1 point méthode, 1 point résultat, 1 point justification sur `clé primaire nulle`.
### Question 2
- Capacité officielle : T-BDD-01B.
- Énoncé : à partir de `Livre(1,Dune), Livre(2,Fondation) ; Emprunt(10,1,Nora), Emprunt(11,9,Sam) invalide`, vérifier unicité id_livre.
- Réponse attendue : Emprunt.id_livre référence Livre.id_livre.
- Barème : 1 point donnée, 1 point méthode, 1 point résultat, 1 point justification sur `doublon id_livre=1`.
### Question 3
- Capacité officielle : T-BDD-01C.
- Énoncé : à partir de `Livre(1,Dune), Livre(2,Fondation) ; Emprunt(10,1,Nora), Emprunt(11,9,Sam) invalide`, contrôler Emprunt.id_livre.
- Réponse attendue : Emprunt(11,9,Sam) viole la référence.
- Barème : 1 point donnée, 1 point méthode, 1 point résultat, 1 point justification sur `suppression référencée`.
### Question 4
- Capacité officielle : T-BDD-02.
- Énoncé : à partir de `Livre(1,Dune), Livre(2,Fondation) ; Emprunt(10,1,Nora), Emprunt(11,9,Sam) invalide`, repérer id_livre=9 absent.
- Réponse attendue : suppression d un livre emprunté refusée.
- Barème : 1 point donnée, 1 point méthode, 1 point résultat, 1 point justification sur `clé primaire nulle`.

## Corrigé question par question
### Corrigé question 1
- Résultat attendu : Livre.id_livre identifie chaque livre.
- Critère spécifique : identifier schéma et instance et éviter `attribut confondu avec valeur`.
### Corrigé question 2
- Résultat attendu : Emprunt.id_livre référence Livre.id_livre.
- Critère spécifique : vérifier unicité id_livre et éviter `clé étrangère supposée unique`.
### Corrigé question 3
- Résultat attendu : Emprunt(11,9,Sam) viole la référence.
- Critère spécifique : contrôler Emprunt.id_livre et éviter `domaine ignoré`.
### Corrigé question 4
- Résultat attendu : suppression d un livre emprunté refusée.
- Critère spécifique : repérer id_livre=9 absent et éviter `attribut confondu avec valeur`.

## Erreurs fréquentes et remédiation
- attribut confondu avec valeur.
- clé étrangère supposée unique.
- domaine ignoré.

## Cas limites travaillés
- clé primaire nulle.
- doublon id_livre=1.
- suppression référencée.

## Critères de réussite observables
- La donnée de départ est recopiée exactement.
- La trace ou le pseudo-code conduit à `Livre.id_livre identifie chaque livre`.
- Au moins un cas limite de la section précédente est décidé.



## Barème question par question
- question 1: 1 point donnée exacte, 1 point méthode liée à la capacité, 1 point résultat vérifiable, 1 point justification du cas limite.
- question 2: 1 point donnée exacte, 1 point méthode liée à la capacité, 1 point résultat vérifiable, 1 point justification du cas limite.
- question 3: 1 point donnée exacte, 1 point méthode liée à la capacité, 1 point résultat vérifiable, 1 point justification du cas limite.
- question 4: 1 point donnée exacte, 1 point méthode liée à la capacité, 1 point résultat vérifiable, 1 point justification du cas limite.

## Fiche liée
- Fiche liée : fiche de cours T09 sur `bases_relationnelles_cles_contraintes`.

## Aménagement
- Version aménagée : `T09_version_amenagee_bases_relationnelles_cles_contraintes.md` ; consignes découpées et barème conservé.
