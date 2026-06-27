---
title: "P08 - cours - HTML, CSS, DOM, HTTP et formulaires"
level: "premiere"
sequence_id: "P08"
document_type: "cours"
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

# P08 - Cours - HTML, CSS, DOM, HTTP et formulaires

## Objectifs spécifiques
- Identifier les données utiles de la situation : <form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi.
- Employer le vocabulaire : HTML structurel, sélecteur CSS, DOM, événement submit, GET, POST.
- Produire une trace, une table, une valeur ou un pseudo-code vérifiable.

## Capacités officielles
- P-IHM-01A.
- P-IHM-01B.
- P-IHM-02.
- P-IHM-03A.
- P-IHM-03B.
- P-IHM-03C.
- P-IHM-04A.
- P-IHM-04B.
- P-IHM-04C.

## Situation-problème
<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi

## À savoir
- HTML structurel.
- sélecteur CSS.
- DOM.
- événement submit.
- GET.
- POST.
- paramètre URL.
- formulaire.
- HTTPS.

## Méthodes
- repérer header main form label input.
- cibler #nom en CSS et DOM.
- lire jour dans URL.
- distinguer GET, POST et HTTPS.

## Exemples corrigés
### Exemple corrigé 1
- Donnée : `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi`.
- Méthode : repérer header main form label input.
- Résultat attendu : <label for=nom>Nom</label><input id=nom name=nom>.
- Contrôle : capacité P-IHM-01A et cas limite `champ nom vide`.
### Exemple corrigé 2
- Donnée : `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi`.
- Méthode : cibler #nom en CSS et DOM.
- Résultat attendu : document.querySelector("#nom").value lit la saisie.
- Contrôle : capacité P-IHM-01B et cas limite `paramètre jour absent`.
### Exemple corrigé 3
- Donnée : `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi`.
- Méthode : lire jour dans URL.
- Résultat attendu : GET /club?jour=mercredi transporte jour.
- Contrôle : capacité P-IHM-02 et cas limite `formulaire sans action`.
### Exemple corrigé 4
- Donnée : `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi`.
- Méthode : distinguer GET, POST et HTTPS.
- Résultat attendu : POST sans HTTPS ne chiffre pas.
- Contrôle : capacité P-IHM-03A et cas limite `champ nom vide`.

## Cas limites
- champ nom vide.
- paramètre jour absent.
- formulaire sans action.

## Erreurs fréquentes
- bouton hors formulaire.
- sélecteur trop large.
- POST confondu avec chiffrement.

## Exercices intégrés
1. Identifier les données utiles dans `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi`.
2. Appliquer : repérer header main form label input.
3. Appliquer : cibler #nom en CSS et DOM.
4. Décider le cas limite `champ nom vide`.

## Critères de réussite observables
- Une capacité parmi P-IHM-01A, P-IHM-01B, P-IHM-02, P-IHM-03A, P-IHM-03B, P-IHM-03C, P-IHM-04A, P-IHM-04B, P-IHM-04C est citée et utilisée.
- Le résultat attendu est explicite : <label for=nom>Nom</label><input id=nom name=nom>.
- Le cas limite `paramètre jour absent` est tranché.

## Lien avec la progression
- Séance : P08-S1 à P08-S4.
- TD : `P08_TD_web_http_dom_formulaires.md`.
- TP : `P08_tp_web_http_dom_formulaires.md`.
- Évaluation : `P08_evaluation_web_http_dom_formulaires.md`.
