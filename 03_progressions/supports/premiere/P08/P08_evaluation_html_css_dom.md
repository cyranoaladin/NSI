---
title: "P08 - evaluation - HTML, CSS, DOM, HTTP et formulaires"
level: "premiere"
sequence_id: "P08"
document_type: "evaluation"
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

# P08 - Évaluation - HTML, CSS, DOM, HTTP et formulaires

## Modalités
- Durée : 30 minutes.
- Matériel autorisé : fiche de cours.
- Capacités évaluées : P-IHM-01A, P-IHM-01B, P-IHM-02, P-IHM-03A, P-IHM-03B, P-IHM-03C, P-IHM-04A, P-IHM-04B, P-IHM-04C.

## Questions
### Question 1
- Capacité officielle : P-IHM-01A.
- Énoncé : à partir de `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi`, repérer header main form label input.
- Réponse attendue : <label for=nom>Nom</label><input id=nom name=nom>.
- Barème : 1 point donnée, 1 point méthode, 1 point résultat, 1 point justification sur `champ nom vide`.
### Question 2
- Capacité officielle : P-IHM-01B.
- Énoncé : à partir de `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi`, cibler #nom en CSS et DOM.
- Réponse attendue : document.querySelector("#nom").value lit la saisie.
- Barème : 1 point donnée, 1 point méthode, 1 point résultat, 1 point justification sur `paramètre jour absent`.
### Question 3
- Capacité officielle : P-IHM-02.
- Énoncé : à partir de `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi`, lire jour dans URL.
- Réponse attendue : GET /club?jour=mercredi transporte jour.
- Barème : 1 point donnée, 1 point méthode, 1 point résultat, 1 point justification sur `formulaire sans action`.
### Question 4
- Capacité officielle : P-IHM-03A.
- Énoncé : à partir de `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi`, distinguer GET, POST et HTTPS.
- Réponse attendue : POST sans HTTPS ne chiffre pas.
- Barème : 1 point donnée, 1 point méthode, 1 point résultat, 1 point justification sur `champ nom vide`.

## Corrigé question par question
### Corrigé question 1
- Résultat attendu : <label for=nom>Nom</label><input id=nom name=nom>.
- Critère spécifique : repérer header main form label input et éviter `bouton hors formulaire`.
### Corrigé question 2
- Résultat attendu : document.querySelector("#nom").value lit la saisie.
- Critère spécifique : cibler #nom en CSS et DOM et éviter `sélecteur trop large`.
### Corrigé question 3
- Résultat attendu : GET /club?jour=mercredi transporte jour.
- Critère spécifique : lire jour dans URL et éviter `POST confondu avec chiffrement`.
### Corrigé question 4
- Résultat attendu : POST sans HTTPS ne chiffre pas.
- Critère spécifique : distinguer GET, POST et HTTPS et éviter `bouton hors formulaire`.

## Erreurs fréquentes et remédiation
- bouton hors formulaire.
- sélecteur trop large.
- POST confondu avec chiffrement.

## Cas limites travaillés
- champ nom vide.
- paramètre jour absent.
- formulaire sans action.

## Critères de réussite observables
- La donnée de départ est recopiée exactement.
- La trace ou le pseudo-code conduit à `<label for=nom>Nom</label><input id=nom name=nom>`.
- Au moins un cas limite de la section précédente est décidé.



## Barème question par question
- question 1: 1 point donnée exacte, 1 point méthode liée à la capacité, 1 point résultat vérifiable, 1 point justification du cas limite.
- question 2: 1 point donnée exacte, 1 point méthode liée à la capacité, 1 point résultat vérifiable, 1 point justification du cas limite.
- question 3: 1 point donnée exacte, 1 point méthode liée à la capacité, 1 point résultat vérifiable, 1 point justification du cas limite.
- question 4: 1 point donnée exacte, 1 point méthode liée à la capacité, 1 point résultat vérifiable, 1 point justification du cas limite.

## Fiche liée
- Fiche liée : fiche de cours P08 sur `html_css_dom`.

## Aménagement
- Version aménagée : `P08_version_amenagee_html_css_dom.md` ; consignes découpées et barème conservé.
