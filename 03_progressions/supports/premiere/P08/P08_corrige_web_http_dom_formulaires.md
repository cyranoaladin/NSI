---
title: "P08 - corrige - HTML, CSS, DOM, HTTP et formulaires"
level: "premiere"
sequence_id: "P08"
document_type: "corrige"
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

# P08 - Corrigé - HTML, CSS, DOM, HTTP et formulaires

## Corrigé du TD
### Exercice 1
- Réponse attendue : <label for=nom>Nom</label><input id=nom name=nom>.
- Méthode : repérer header main form label input.
- Cas limite : champ nom vide.
### Exercice 2
- Réponse attendue : document.querySelector("#nom").value lit la saisie.
- Méthode : cibler #nom en CSS et DOM.
- Cas limite : paramètre jour absent.
### Exercice 3
- Réponse attendue : GET /club?jour=mercredi transporte jour.
- Méthode : lire jour dans URL.
- Cas limite : formulaire sans action.
### Exercice 4
- Réponse attendue : POST sans HTTPS ne chiffre pas.
- Méthode : distinguer GET, POST et HTTPS.
- Cas limite : champ nom vide.
### Exercice 5
- Capacité mobilisée : P-IHM-03B.
- Réponse attendue : cookie → stocké côté client ET retransmis automatiquement au serveur selon Domain/Path ; localStorage → stocké côté client uniquement, jamais retransmis au serveur ; donnée de formulaire → transmise au serveur à la soumission uniquement ; session → stockée côté serveur (seul l'identifiant de session transite dans le cookie).
- Méthode : classer chaque mécanisme selon le lieu de stockage (client/serveur) et la retransmission automatique (oui/non, selon Domain et Path pour le cookie).
- Cas limite : en navigation privée le cookie et le localStorage sont effacés à la fermeture ; un cookie expiré (Max-Age écoulé) n'est plus retransmis.
### Exercice 6
- Réponse attendue : document.querySelector("#nom").value lit la saisie.
- Méthode : cibler #nom en CSS et DOM.
- Cas limite : formulaire sans action.
### Exercice 7
- Réponse attendue : GET /club?jour=mercredi transporte jour.
- Méthode : lire jour dans URL.
- Cas limite : champ nom vide.
### Exercice 8
- Réponse attendue : POST sans HTTPS ne chiffre pas.
- Méthode : distinguer GET, POST et HTTPS.
- Cas limite : paramètre jour absent.

### Exercice 9
- Capacité mobilisée : P-IHM-04C.
- Réponse attendue : (A) POST+HTTPS (mot de passe), (B) GET (recherche), (C) POST (contact), (D) risque token visible.
- Méthode : classification par confidentialité (URL, historique, logs, chiffrement).
- Cas limite : POST sans HTTPS ne chiffre pas les données sur le réseau.

## Corrigé du TP
- Donnée : `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi`.
- Résultat principal : <label for=nom>Nom</label><input id=nom name=nom>.
- Résultat secondaire : document.querySelector("#nom").value lit la saisie.

## Corrigé de l évaluation
- Question 1 : <label for=nom>Nom</label><input id=nom name=nom>.
- Question 2 : document.querySelector("#nom").value lit la saisie.
- Question 3 : GET /club?jour=mercredi transporte jour.
- Question 4 : POST sans HTTPS ne chiffre pas.
