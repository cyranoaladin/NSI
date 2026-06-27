---
title: "T10 - evaluation - SQL SELECT, JOIN, INSERT, UPDATE et DELETE"
level: "terminale"
sequence_id: "T10"
document_type: "evaluation"
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

# T10 - Évaluation - SQL SELECT, JOIN, INSERT, UPDATE et DELETE

## Modalités
- Durée : 30 minutes.
- Matériel autorisé : fiche de cours.
- Capacités évaluées : T-BDD-03A, T-BDD-03B, T-BDD-03C, T-BDD-03D, T-BDD-03E, T-BDD-03F, T-BDD-03G, T-BDD-03H.

## Questions
### Question 1
- Capacité officielle : T-BDD-03A.
- Énoncé : à partir de `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)`, projeter nom et classe.
- Réponse attendue : SELECT nom FROM Eleve ORDER BY nom -> Ada, Linus.
- Barème : 1 point donnée, 1 point méthode, 1 point résultat, 1 point justification sur `JOIN sans ON`.
### Question 2
- Capacité officielle : T-BDD-03B.
- Énoncé : à partir de `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)`, filtrer note >= 15.
- Réponse attendue : JOIN -> Ada 17.
- Barème : 1 point donnée, 1 point méthode, 1 point résultat, 1 point justification sur `UPDATE sans WHERE`.
### Question 3
- Capacité officielle : T-BDD-03C.
- Énoncé : à partir de `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)`, joindre Eleve.id_eleve = Note.id_eleve.
- Réponse attendue : UPDATE id_note=10 -> Ada 18.
- Barème : 1 point donnée, 1 point méthode, 1 point résultat, 1 point justification sur `DELETE sans WHERE`.
### Question 4
- Capacité officielle : T-BDD-03D.
- Énoncé : à partir de `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)`, vérifier modification par SELECT.
- Réponse attendue : DELETE WHERE id_note=11 retire Linus.
- Barème : 1 point donnée, 1 point méthode, 1 point résultat, 1 point justification sur `JOIN sans ON`.

## Corrigé question par question
### Corrigé question 1
- Résultat attendu : SELECT nom FROM Eleve ORDER BY nom -> Ada, Linus.
- Critère spécifique : projeter nom et classe et éviter `condition de jointure oubliée`.
### Corrigé question 2
- Résultat attendu : JOIN -> Ada 17.
- Critère spécifique : filtrer note >= 15 et éviter `WHERE confondu avec ORDER BY`.
### Corrigé question 3
- Résultat attendu : UPDATE id_note=10 -> Ada 18.
- Critère spécifique : joindre Eleve.id_eleve = Note.id_eleve et éviter `WHERE omis dans UPDATE`.
### Corrigé question 4
- Résultat attendu : DELETE WHERE id_note=11 retire Linus.
- Critère spécifique : vérifier modification par SELECT et éviter `condition de jointure oubliée`.

## Erreurs fréquentes et remédiation
- condition de jointure oubliée.
- WHERE confondu avec ORDER BY.
- WHERE omis dans UPDATE.

## Cas limites travaillés
- JOIN sans ON.
- UPDATE sans WHERE.
- DELETE sans WHERE.

## Critères de réussite observables
- La donnée de départ est recopiée exactement.
- La trace ou le pseudo-code conduit à `SELECT nom FROM Eleve ORDER BY nom -> Ada, Linus`.
- Au moins un cas limite de la section précédente est décidé.



## Barème question par question
- question 1: 1 point donnée exacte, 1 point méthode liée à la capacité, 1 point résultat vérifiable, 1 point justification du cas limite.
- question 2: 1 point donnée exacte, 1 point méthode liée à la capacité, 1 point résultat vérifiable, 1 point justification du cas limite.
- question 3: 1 point donnée exacte, 1 point méthode liée à la capacité, 1 point résultat vérifiable, 1 point justification du cas limite.
- question 4: 1 point donnée exacte, 1 point méthode liée à la capacité, 1 point résultat vérifiable, 1 point justification du cas limite.

## Fiche liée
- Fiche liée : fiche de cours T10 sur `sql_select_where_join`.

## Aménagement
- Version aménagée : `T10_version_amenagee_sql_select_where_join.md` ; consignes découpées et barème conservé.
