---
title: "T10 - tp_papier - SQL SELECT, JOIN, INSERT, UPDATE et DELETE"
level: "terminale"
sequence_id: "T10"
document_type: "tp_papier"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "SQL SELECT, JOIN, INSERT, UPDATE et DELETE"
notion: "SQL SELECT, JOIN, INSERT, UPDATE et DELETE"
private_data: false
official_program:
  capacities:
    - "T-BDD-03A"
    - "T-BDD-03B"
    - "T-BDD-03C"
    - "T-BDD-03D"
    - "T-BDD-03E"
    - "T-BDD-03F"
    - "T-BDD-03G"
    - "T-BDD-03H"
---

# T10 - TP - SQL SELECT, JOIN, INSERT, UPDATE et DELETE

## Statut du TP
TP papier : ce support n attend aucune ressource Python ; le livrable est une trace écrite vérifiable.

## Donnée fournie
`Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)`

## Travail demandé
1. Préparer la donnée et nommer les champs utiles.
2. Réaliser : projeter nom et classe.
3. Réaliser : filtrer note >= 15.
4. Tester le cas limite `JOIN sans ON`.
5. Produire le livrable : SELECT nom FROM Eleve ORDER BY nom -> Ada, Linus.

## Barème associé
- 2 points : donnée préparée.
- 3 points : méthode principale.
- 3 points : résultat `SELECT nom FROM Eleve ORDER BY nom -> Ada, Linus`.
- 2 points : cas limite `JOIN sans ON`.

## Corrigé question par question
### Corrigé question 1
Résultat attendu : `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)`.
### Corrigé question 2
Résultat attendu : SELECT nom FROM Eleve ORDER BY nom -> Ada, Linus.
### Corrigé question 3
Résultat attendu : JOIN -> Ada 17, Linus 13.
### Corrigé question 4
Résultat attendu : `JOIN sans ON` traité sans ambiguïté.

## Liens
- TD lié : `T10_TD_sql_select_where_join.md`.
- Évaluation liée : `T10_evaluation_sql_select_where_join.md`.

## Cas limites travaillés
- JOIN sans ON.
- UPDATE sans WHERE.
- DELETE sans WHERE.

## Erreurs fréquentes
- condition de jointure oubliée.
- WHERE confondu avec ORDER BY.
- WHERE omis dans UPDATE.

## Critères de réussite observables
- La donnée de départ est recopiée exactement.
- La trace ou le pseudo-code conduit à `SELECT nom FROM Eleve ORDER BY nom -> Ada, Linus`.
- Au moins un cas limite de la section précédente est décidé.

