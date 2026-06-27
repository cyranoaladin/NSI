---
title: "T10 - corrige - SQL SELECT, JOIN, INSERT, UPDATE et DELETE"
level: "terminale"
sequence_id: "T10"
document_type: "corrige"
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

# T10 - Corrigé - SQL SELECT, JOIN, INSERT, UPDATE et DELETE

## Corrigé du TD
### Exercice 1
- Réponse attendue : SELECT nom FROM Eleve ORDER BY nom -> Ada, Linus.
- Méthode : projeter nom et classe.
- Cas limite : JOIN sans ON.
### Exercice 2
- Réponse attendue : JOIN -> Ada 17, Linus 13.
- Méthode : filtrer note >= 15.
- Cas limite : UPDATE sans WHERE.
### Exercice 3
- Réponse attendue : UPDATE id_note=10 -> Ada 18.
- Méthode : joindre Eleve.id_eleve = Note.id_eleve.
- Cas limite : DELETE sans WHERE.
### Exercice 4
- Réponse attendue : DELETE WHERE id_note=11 retire Linus.
- Méthode : vérifier modification par SELECT.
- Cas limite : JOIN sans ON.
### Exercice 5
- Réponse attendue : SELECT nom FROM Eleve ORDER BY nom -> Ada, Linus.
- Méthode : projeter nom et classe.
- Cas limite : UPDATE sans WHERE.
### Exercice 6
- Réponse attendue : JOIN -> Ada 17, Linus 13.
- Méthode : filtrer note >= 15.
- Cas limite : DELETE sans WHERE.
### Exercice 7
- Réponse attendue : UPDATE id_note=10 -> Ada 18.
- Méthode : joindre Eleve.id_eleve = Note.id_eleve.
- Cas limite : JOIN sans ON.
### Exercice 8
- Réponse attendue : DELETE WHERE id_note=11 retire Linus.
- Méthode : vérifier modification par SELECT.
- Cas limite : UPDATE sans WHERE.

## Corrigé du TP
- Donnée : `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)`.
- Résultat principal : SELECT nom FROM Eleve ORDER BY nom -> Ada, Linus.
- Résultat secondaire : JOIN -> Ada 17, Linus 13.

## Corrigé de l évaluation
- Question 1 : SELECT nom FROM Eleve ORDER BY nom -> Ada, Linus.
- Question 2 : JOIN -> Ada 17, Linus 13.
- Question 3 : UPDATE id_note=10 -> Ada 18.
- Question 4 : DELETE WHERE id_note=11 retire Linus.
