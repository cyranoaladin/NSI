---
title: "P08 - corrige - HTML, CSS, DOM, HTTP et formulaires"
level: "premiere"
sequence_id: "P08"
document_type: "corrige"
status: "needs_review"
version: "0.7.0"
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

## Corrigé du TD HTML/CSS/DOM

Les exercices 1 à 6 ci-dessous correspondent au TD `P08_TD_html_css_dom.md`. Ne pas les utiliser pour corriger le TD HTTP/formulaires.

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

## Corrigé du TD HTTP/formulaires

Les exercices 7 et 8 ci-dessous correspondent au TD `P08_TD_http_get_post_formulaires.md`. Le corrigé détaillé des 8 exercices HTTP se trouve dans les repères enseignant intégrés au TD et dans `P08_corrige_http_get_post_formulaires.md`.

### Exercice 7
- Capacité mobilisée : P-IHM-04A.
- Donnée : formulaire avec `<input id="nom">` sans attribut `name` et sans attribut `method`.
- Réponse attendue : erreur 1 — `name` manquant, le champ nom n'est pas transmis ; correction : `<label for=nom>Nom</label><input id=nom name=nom>`. Erreur 2 — `method` absent, GET par défaut ; ajouter `method="post"` si POST souhaité.
- Méthode : identifier chaque erreur HTML et son impact sur la requête.
- Cas limite : champ nom vide après correction, le paramètre est transmis avec une valeur vide.
### Exercice 8
- Capacité mobilisée : P-IHM-04B.
- Donnée : quatre affirmations fausses d'élèves sur POST, HTTPS, `name` et validation serveur.
- Réponse attendue : F1 — POST masque de l'URL mais ne chiffre pas, seul HTTPS chiffre ; F2 — HTTPS ne transforme pas GET en POST, il chiffre via TLS ; F3 — un champ sans `name` n'est pas transmis ; F4 — la validation côté serveur est indispensable, le JavaScript peut être contourné.
- Méthode : identifier la confusion précise et reformuler avec le vocabulaire technique.
- Cas limite : paramètre jour absent si le champ n'a pas d'attribut `name`.

## Corrigé du TP
- Donnée : `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi`.
- Résultat principal : <label for=nom>Nom</label><input id=nom name=nom>.
- Résultat secondaire : document.querySelector("#nom").value lit la saisie.

## Corrigés des deux évaluations

Les deux sujets ne partagent plus un corrigé générique :

- HTML, CSS et DOM : `P08_corrige_html_css_dom.md` ;
- HTTP, formulaires et confidentialité : `P08_corrige_http_get_post_formulaires.md`.

Cette séparation est disciplinaire : le premier corrigé suit l'arbre HTML, les sélecteurs et les états du gestionnaire d'événement ; le second suit les paramètres HTTP, l'ordre client-serveur, les lieux de stockage et les critères de confidentialité.
