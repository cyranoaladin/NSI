---
title: "T10 - trace - SQL SELECT, JOIN, INSERT, UPDATE et DELETE"
level: "terminale"
sequence_id: "T10"
document_type: "trace"
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

# T10 - Trace - SQL SELECT, JOIN, INSERT, UPDATE et DELETE

## Trace courte
- Donnée : `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)`.
- Vocabulaire : SELECT, FROM, WHERE, JOIN, ORDER BY.
- Étape 1 : projeter nom et classe.
- Étape 2 : filtrer note >= 15.
- Résultat de référence : SELECT nom FROM Eleve ORDER BY nom -> Ada, Linus.

## Cas limites à mémoriser
- JOIN sans ON.
- UPDATE sans WHERE.
- DELETE sans WHERE.

## Erreurs fréquentes
- condition de jointure oubliée.
- WHERE confondu avec ORDER BY.
- WHERE omis dans UPDATE.

## Critères de réussite observables
- Capacité : T-BDD-03A.
- Résultat final : JOIN -> Ada 17.
- Cas limite : JOIN sans ON.
