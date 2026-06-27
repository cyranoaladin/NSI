---
title: "T10 - remediation - SQL SELECT, JOIN, INSERT, UPDATE et DELETE"
level: "terminale"
sequence_id: "T10"
document_type: "remediation"
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

# T10 - Remédiation - SQL SELECT, JOIN, INSERT, UPDATE et DELETE

## Diagnostic
- condition de jointure oubliée.
- WHERE confondu avec ORDER BY.
- WHERE omis dans UPDATE.

## Activités correctives
1. Annoter `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)`.
2. Refaire la tâche `projeter nom et classe` et comparer avec `SELECT nom FROM Eleve ORDER BY nom -> Ada, Linus`.
3. Traiter le cas limite `JOIN sans ON`.
4. Relier la réponse à T-BDD-03A.

## Critères de sortie
- Donnée exacte.
- Résultat final explicite.
- Cas limite décidé.
