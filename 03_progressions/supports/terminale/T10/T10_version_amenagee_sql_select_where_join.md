---
title: "T10 - version_amenagee - SQL SELECT, JOIN, INSERT, UPDATE et DELETE"
level: "terminale"
sequence_id: "T10"
document_type: "version_amenagee"
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

# T10 - Version aménagée - SQL SELECT, JOIN, INSERT, UPDATE et DELETE

## Aides intégrées
- Donnée fournie : `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)`.
- Mots utiles : SELECT, FROM, WHERE, JOIN, ORDER BY.
- Méthode guidée : projeter nom et classe puis filtrer note >= 15.

## Exercice guidé
1. Recopier la donnée utile.
2. Choisir la capacité : T-BDD-03A ou T-BDD-03B.
3. Compléter le résultat : SELECT nom FROM Eleve ORDER BY nom -> Ada, Linus.
4. Cocher le cas limite : JOIN sans ON.

## Réponses rapides
- Réponse 1 : SELECT nom FROM Eleve ORDER BY nom -> Ada, Linus.
- Réponse 2 : JOIN -> Ada 17.
- Réponse 3 : UPDATE id_note=10 -> Ada 18.
