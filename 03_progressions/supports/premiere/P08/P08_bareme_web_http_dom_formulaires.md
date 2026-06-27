---
title: "P08 - bareme - HTML, CSS, DOM, HTTP et formulaires"
level: "premiere"
sequence_id: "P08"
document_type: "bareme"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "HTML, CSS, DOM, HTTP et formulaires"
notion: "HTML, CSS, DOM, HTTP et formulaires"
private_data: false
official_program:
  capacities:
    - "P-IHM-01A"
    - "P-IHM-01B"
    - "P-IHM-02"
    - "P-IHM-03A"
    - "P-IHM-03B"
    - "P-IHM-03C"
    - "P-IHM-04A"
    - "P-IHM-04B"
    - "P-IHM-04C"
---

# P08 - Barème - HTML, CSS, DOM, HTTP et formulaires

## TD
- 8 exercices : 1 point donnée, 1 point méthode, 1 point résultat, 1 point cas limite.

## TP
- 2 points donnée `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi`.
- 3 points tâche `repérer header main form label input`.
- 3 points résultat `<label for=nom>Nom</label><input id=nom name=nom>`.
- 2 points cas limite `champ nom vide`.

## Évaluation question par question
- Question 1 : 4 points sur P-IHM-01A avec résultat `<label for=nom>Nom</label><input id=nom name=nom>`.
- Question 2 : 4 points sur P-IHM-01B avec résultat `document.querySelector("#nom").value lit la saisie`.
- Question 3 : 4 points sur P-IHM-02 avec résultat `GET /club?jour=mercredi transporte jour`.
- Question 4 : 4 points sur P-IHM-03A avec résultat `POST sans HTTPS ne chiffre pas`.

## Critères observables
- Trace, table, valeur ou pseudo-code présent.
- Cas limite et erreur fréquente explicités.
