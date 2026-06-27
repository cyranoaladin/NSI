---
title: "T10 - bareme - SQL SELECT, JOIN, INSERT, UPDATE et DELETE"
level: "terminale"
sequence_id: "T10"
document_type: "bareme"
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

# T10 - Barème - SQL SELECT, JOIN, INSERT, UPDATE et DELETE

## TD
- 8 exercices : 1 point donnée, 1 point méthode, 1 point résultat, 1 point cas limite.

## TP
- 2 points donnée `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)`.
- 3 points tâche `projeter nom et classe`.
- 3 points résultat `SELECT nom FROM Eleve ORDER BY nom -> Ada, Linus`.
- 2 points cas limite `JOIN sans ON`.

## Évaluation question par question
- Question 1 : 4 points sur T-BDD-03A avec résultat `SELECT nom FROM Eleve ORDER BY nom -> Ada, Linus`.
- Question 2 : 4 points sur T-BDD-03B avec résultat `JOIN -> Ada 17, Linus 13`.
- Question 3 : 4 points sur T-BDD-03C avec résultat `UPDATE id_note=10 -> Ada 18`.
- Question 4 : 4 points sur T-BDD-03D avec résultat `DELETE WHERE id_note=11 retire Linus`.

## Critères observables
- Trace, table, valeur ou pseudo-code présent.
- Cas limite et erreur fréquente explicités.
