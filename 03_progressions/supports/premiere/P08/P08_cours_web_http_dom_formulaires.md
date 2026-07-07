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

## Confidentialité des requêtes

La capacité P-IHM-04C demande de discuter les types de requêtes selon les valeurs à transmettre et leur confidentialité.

### GET vs POST — visibilité des données

| Aspect | GET | POST |
|--------|-----|------|
| Données visibles dans l'URL | Oui (`?nom=valeur&...`) | Non (corps de la requête) |
| Historique du navigateur | Enregistrées | Non enregistrées |
| Logs du serveur | Paramètres visibles | Paramètres non loggués par défaut |
| Longueur maximale | Limitée (~2048 caractères) | Pas de limite pratique |
| Mise en cache | Possible | Non |

### Ni GET ni POST ne chiffrent les données

Sans HTTPS, les données transmises par GET **et** par POST circulent en clair sur le réseau. POST masque les données de la barre d'adresse et de l'historique, mais ne les chiffre pas. Seul HTTPS (HTTP + TLS) chiffre l'intégralité de l'échange, y compris les paramètres GET dans l'URL.

### Critère de choix

- **GET** : recherche, navigation, filtres — données non sensibles, résultat partageable par URL.
- **POST** : mot de passe, formulaire de contact, données personnelles — ne doit pas apparaître dans l'historique ni les logs.
- **HTTPS** : obligatoire dès qu'une donnée est sensible (mot de passe, token, coordonnées).

### Exemple : classer des situations

1. Mot de passe de connexion → **POST + HTTPS** (sensible, ne doit pas apparaître dans l'URL ni les logs).
2. Recherche sur un site → **GET** (non sensible, URL partageable : `?q=python+cours`).
3. Formulaire de contact (nom, email, message) → **POST** (données personnelles, pas dans l'historique).
4. Token d'authentification dans un lien → **risque** : le token est dans l'URL, visible dans l'historique et les logs serveur. Préférer un cookie HttpOnly ou un header Authorization avec HTTPS.

### Cas limites

- Un formulaire POST sans HTTPS transmet les données en clair sur le réseau (sniffable).
- Un GET avec HTTPS chiffre les paramètres sur le réseau, mais ils restent visibles dans la barre d'adresse et l'historique local.

## Renforcement explicatif ciblé

Ce cours doit être lu comme une progression sur Web, DOM et HTTP. La notion ne se réduit pas à une liste de mots : on part d'une situation observable, on nomme les objets manipulés, puis on applique une méthode vérifiable sur un cas limité avant de généraliser.

### Savoir disciplinaire
- Vocabulaire à maîtriser : balise, attribut, sélecteur CSS, nœud DOM, événement, méthode GET, méthode POST, paramètre URL.
- Capacités reliées : P-IHM-01A, P-IHM-01B, P-IHM-02, P-IHM-03A, P-IHM-03B, P-IHM-03C, P-IHM-04A, P-IHM-04B, P-IHM-04C.
- Le savoir attendu consiste à expliquer le rôle de chaque objet avant de l'utiliser dans un exercice.

### Savoir-faire et méthodes opérationnelles
- construire un formulaire GET puis lire la query string.
- associer un sélecteur CSS à l’élément modifié.
- décrire l’événement DOM qui déclenche le traitement.

### Erreurs fréquentes spécifiques
- Un élève peut confondre id CSS et classe CSS ; la correction consiste à reprendre la définition puis à refaire la trace sur un exemple minimal.
- Un élève peut envoyer un mot de passe dans une URL GET ; la correction consiste à isoler le cas limite avant de recommencer le calcul ou le raisonnement.
- Un élève peut modifier le texte affiché sans vérifier l’élément DOM ciblé ; la correction consiste à vérifier le résultat avec une donnée différente.

### Cas limites à contrôler
- Cas minimal : une donnée vide, un seul élément, une route absente ou une structure sans enfant selon la notion.
- Cas ambigu : doublon, égalité, absence de correspondance ou choix local non optimal.

### Synthèse savoir / savoir-faire / méthode
- Savoir : définir précisément les objets de Web, DOM et HTTP.
- Savoir-faire : appliquer une méthode contrôlable à une donnée explicite.
- Méthode : annoncer la donnée, exécuter les étapes dans l'ordre, puis vérifier le résultat par un cas limite.
