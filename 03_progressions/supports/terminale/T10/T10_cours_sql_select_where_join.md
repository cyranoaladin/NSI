---
title: "T10 - cours - SQL SELECT, JOIN, INSERT, UPDATE et DELETE"
level: "terminale"
sequence_id: "T10"
document_type: "cours"
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

# T10 - Cours - SQL SELECT, JOIN, INSERT, UPDATE et DELETE

## Objectifs spécifiques
- Identifier les données utiles de la situation : Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13).
- Employer le vocabulaire : SELECT, FROM, WHERE, JOIN, ORDER BY, INSERT.
- Produire une trace, une table, une valeur ou un pseudo-code vérifiable.

## Capacités officielles
- T-BDD-03A.
- T-BDD-03B.
- T-BDD-03C.
- T-BDD-03D.
- T-BDD-03E.
- T-BDD-03F.
- T-BDD-03G.
- T-BDD-03H.

## Situation-problème
Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)

## À savoir
- SELECT.
- FROM.
- WHERE.
- JOIN.
- ORDER BY.
- INSERT.
- UPDATE avec WHERE.
- DELETE avec WHERE.

## Méthodes
- projeter nom et classe.
- filtrer note >= 15.
- joindre Eleve.id_eleve = Note.id_eleve.
- vérifier modification par SELECT.

## Exemples corrigés
### Exemple corrigé 1
- Donnée : `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)`.
- Méthode : projeter nom et classe.
- Résultat attendu : SELECT nom FROM Eleve ORDER BY nom -> Ada, Linus.
- Contrôle : capacité T-BDD-03A et cas limite `JOIN sans ON`.
### Exemple corrigé 2
- Donnée : `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)`.
- Méthode : filtrer note >= 15.
- Résultat attendu : JOIN -> Ada 17.
- Contrôle : capacité T-BDD-03B et cas limite `UPDATE sans WHERE`.
### Exemple corrigé 3
- Donnée : `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)`.
- Méthode : joindre Eleve.id_eleve = Note.id_eleve.
- Résultat attendu : UPDATE id_note=10 -> Ada 18.
- Contrôle : capacité T-BDD-03C et cas limite `DELETE sans WHERE`.
### Exemple corrigé 4
- Donnée : `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)`.
- Méthode : vérifier modification par SELECT.
- Résultat attendu : DELETE WHERE id_note=11 retire Linus.
- Contrôle : capacité T-BDD-03D et cas limite `JOIN sans ON`.

## Cas limites
- JOIN sans ON.
- UPDATE sans WHERE.
- DELETE sans WHERE.

## Erreurs fréquentes
- condition de jointure oubliée.
- WHERE confondu avec ORDER BY.
- WHERE omis dans UPDATE.

## Exercices intégrés
1. Identifier les données utiles dans `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)`.
2. Appliquer : projeter nom et classe.
3. Appliquer : filtrer note >= 15.
4. Décider le cas limite `JOIN sans ON`.

## Critères de réussite observables
- Une capacité parmi T-BDD-03A, T-BDD-03B, T-BDD-03C, T-BDD-03D, T-BDD-03E, T-BDD-03F, T-BDD-03G, T-BDD-03H est citée et utilisée.
- Le résultat attendu est explicite : SELECT nom FROM Eleve ORDER BY nom -> Ada, Linus.
- Le cas limite `UPDATE sans WHERE` est tranché.

## Lien avec la progression
- Séance : T10-S1 à T10-S4.
- TD : `T10_TD_sql_select_where_join.md`.
- TP : `T10_tp_sql_select_where_join.md`.
- Évaluation : `T10_evaluation_sql_select_where_join.md`.
