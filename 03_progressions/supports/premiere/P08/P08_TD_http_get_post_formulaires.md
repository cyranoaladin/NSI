---
title: "P08 - td - HTML, CSS, DOM, HTTP et formulaires"
level: "premiere"
sequence_id: "P08"
document_type: "td"
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

# P08 - TD - HTML, CSS, DOM, HTTP et formulaires

## Objectifs
- Travailler HTML structurel, sélecteur CSS, DOM, événement submit, GET.
- Produire huit réponses vérifiables avec données explicites.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2.
- Standard : exercices 3 à 6.
- Approfondissement : exercices 7 et 8.

## Exercices
### Exercice 1
- Type : lecture/analyse.
- Capacité officielle : P-IHM-01A.
- Données : `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi`. ; jeu_exercice=alpha
- Consigne : repérer header main form label input ; traiter aussi `champ nom vide` si nécessaire.
- Réponse attendue : <label for=nom>Nom</label><input id=nom name=nom>.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `champ nom vide`.
### Exercice 2
- Type : production/écriture.
- Capacité officielle : P-IHM-01B.
- Données : `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi`. ; jeu_exercice=beta
- Consigne : cibler #nom en CSS et DOM ; traiter aussi `paramètre jour absent` si nécessaire.
- Réponse attendue : document.querySelector("#nom").value lit la saisie.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `paramètre jour absent`.
### Exercice 3
- Type : production/écriture.
- Capacité officielle : P-IHM-02.
- Données : `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi`. ; jeu_exercice=gamma
- Consigne : lire jour dans URL ; traiter aussi `formulaire sans action` si nécessaire.
- Réponse attendue : GET /club?jour=mercredi transporte jour.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `formulaire sans action`.
### Exercice 4
- Type : cas limite.
- Capacité officielle : P-IHM-03A.
- Données : `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi`. ; jeu_exercice=delta
- Consigne : distinguer GET, POST et HTTPS ; traiter aussi `champ nom vide` si nécessaire.
- Réponse attendue : POST sans HTTPS ne chiffre pas.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `champ nom vide`.
### Exercice 5
- Type : justification.
- Capacité officielle : P-IHM-03B.
- Données : un formulaire POST envoie `nom=Ali` au serveur ; le serveur répond avec `Set-Cookie: session_id=abc123; Path=/; HttpOnly`. L'utilisateur revient sur la page et le navigateur a aussi un `localStorage.setItem("theme", "sombre")`. ; jeu_exercice=epsilon
- Consigne : (5a) parmi `session_id`, `nom=Ali` (corps POST) et `theme=sombre` (localStorage), indiquer lesquels sont retransmis automatiquement au serveur à la prochaine requête ; (5b) expliquer pourquoi `localStorage` n'est pas retransmis ; traiter aussi le cas `cookie expiré` si nécessaire.
- Réponse attendue : seul le cookie `session_id` est retransmis automatiquement (en-tête Cookie) ; le corps POST n'est pas renvoyé ; le localStorage reste côté client et n'est jamais envoyé au serveur. Cas limite : un cookie expiré n'est plus retransmis.
- Critère de réussite : distinction mémorisé client / retransmis serveur explicite, chaque mécanisme classé.
### Exercice 6
- Type : lecture/analyse.
- Capacité officielle : P-IHM-03C.
- Données : deux scénarios : (A) formulaire de connexion avec mot de passe envoyé en POST sur `http://example.com/login` ; (B) le même formulaire envoyé en POST sur `https://example.com/login`. ; jeu_exercice=zeta
- Consigne : (6a) pour chaque scénario, dire si les données sont chiffrées sur le réseau et justifier ; (6b) expliquer pourquoi POST seul ne suffit pas à protéger les données ; traiter aussi le cas `GET avec HTTPS` si nécessaire.
- Réponse attendue : (A) données en clair sur le réseau (HTTP sans TLS), interceptables ; (B) données chiffrées par TLS (HTTPS). POST masque les données de l'URL mais ne les chiffre pas. Cas limite : GET avec HTTPS chiffre les paramètres sur le réseau mais ils restent dans l'historique local.
- Critère de réussite : distinction HTTP/HTTPS explicite, POST≠chiffrement clairement justifié.
### Exercice 7
- Type : production/écriture.
- Capacité officielle : P-IHM-04A.
- Données : `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi`. ; jeu_exercice=eta
- Consigne : lire jour dans URL ; traiter aussi `champ nom vide` si nécessaire.
- Réponse attendue : GET /club?jour=mercredi transporte jour.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `champ nom vide`.
### Exercice 8
- Type : justification.
- Capacité officielle : P-IHM-04B.
- Données : `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi`. ; jeu_exercice=theta
- Consigne : distinguer GET, POST et HTTPS ; traiter aussi `paramètre jour absent` si nécessaire.
- Réponse attendue : POST sans HTTPS ne chiffre pas.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `paramètre jour absent`.

### Exercice 9
- Type : lecture/analyse.
- Capacité officielle : P-IHM-04C.
- Données : quatre situations de transmission de données sur le Web : (A) un formulaire de connexion avec mot de passe, (B) une barre de recherche sur un site, (C) un formulaire de contact (nom, email, message), (D) un lien contenant un token d'authentification dans l'URL.
- Consigne : (9a) pour chaque situation, indiquer si GET ou POST est approprié et justifier ; (9b) pour chaque situation, indiquer si HTTPS est nécessaire et pourquoi ; (9c) expliquer pourquoi le token dans l'URL de la situation (D) pose un problème de confidentialité.
- Réponse attendue : (A) POST+HTTPS ; (B) GET ; (C) POST ; (D) risque — token visible dans l'historique et les logs.
- Critère de réussite : chaque situation classée avec justification, distinction GET/POST/HTTPS explicite.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : P-IHM-01A.
- Résultat attendu : <label for=nom>Nom</label><input id=nom name=nom>.
- Justification : la tâche `repérer header main form label input` s applique à `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi` ; erreur évitée : bouton hors formulaire.
- Donnée utilisée alpha dans P08 TD http get post formulaires : cas alpha de l exercice 1 avec les valeurs indiquées dans l énoncé.
- Méthode alpha dans P08 TD http get post formulaires : trace courte, pseudo-code local `if cas_alpha: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat alpha dans P08 TD http get post formulaires : sortie vérifiable de l exercice 1, reliée à la capacité officielle du bloc.
- Contrôle alpha dans P08 TD http get post formulaires : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 2
- Capacité mobilisée : P-IHM-01B.
- Résultat attendu : document.querySelector("#nom").value lit la saisie.
- Justification : la tâche `cibler #nom en CSS et DOM` s applique à `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi` ; erreur évitée : sélecteur trop large.
- Donnée utilisée beta dans P08 TD http get post formulaires : cas beta de l exercice 2 avec les valeurs indiquées dans l énoncé.
- Méthode beta dans P08 TD http get post formulaires : trace courte, pseudo-code local `if cas_beta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat beta dans P08 TD http get post formulaires : sortie vérifiable de l exercice 2, reliée à la capacité officielle du bloc.
- Contrôle beta dans P08 TD http get post formulaires : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 3
- Capacité mobilisée : P-IHM-02.
- Résultat attendu : GET /club?jour=mercredi transporte jour.
- Justification : la tâche `lire jour dans URL` s applique à `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi` ; erreur évitée : POST confondu avec chiffrement.
- Donnée utilisée gamma dans P08 TD http get post formulaires : cas gamma de l exercice 3 avec les valeurs indiquées dans l énoncé.
- Méthode gamma dans P08 TD http get post formulaires : trace courte, pseudo-code local `if cas_gamma: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat gamma dans P08 TD http get post formulaires : sortie vérifiable de l exercice 3, reliée à la capacité officielle du bloc.
- Contrôle gamma dans P08 TD http get post formulaires : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 4
- Capacité mobilisée : P-IHM-03A.
- Résultat attendu : POST sans HTTPS ne chiffre pas.
- Justification : la tâche `distinguer GET, POST et HTTPS` s applique à `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi` ; erreur évitée : bouton hors formulaire.
- Donnée utilisée delta dans P08 TD http get post formulaires : cas delta de l exercice 4 avec les valeurs indiquées dans l énoncé.
- Méthode delta dans P08 TD http get post formulaires : trace courte, pseudo-code local `if cas_delta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat delta dans P08 TD http get post formulaires : sortie vérifiable de l exercice 4, reliée à la capacité officielle du bloc.
- Contrôle delta dans P08 TD http get post formulaires : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 5
- Capacité mobilisée : P-IHM-03B.
- Résultat attendu : (5a) seul `session_id` (cookie) est retransmis automatiquement au serveur via l'en-tête `Cookie` ; le corps POST `nom=Ali` n'est pas renvoyé ; `theme=sombre` (localStorage) reste côté client. (5b) localStorage est un stockage local du navigateur, jamais inclus dans les requêtes HTTP. Cas limite : un cookie expiré n'est plus retransmis.
- Justification : la tâche « distinguer ce qui est mémorisé côté client et retransmis au serveur » s'applique aux trois mécanismes (cookie, POST body, localStorage) ; erreur évitée : croire que localStorage est envoyé au serveur.
- Donnée utilisée epsilon dans P08 TD http get post formulaires : cookie `session_id`, corps POST `nom=Ali`, localStorage `theme=sombre`.
- Méthode epsilon dans P08 TD http get post formulaires : classer chaque donnée selon son mécanisme de stockage et de transmission.
- Résultat epsilon dans P08 TD http get post formulaires : tableau de classification mémorisé/retransmis pour chaque mécanisme.
- Contrôle epsilon dans P08 TD http get post formulaires : le cas limite « cookie expiré » est décidé explicitement.
### Corrigé exercice 6
- Capacité mobilisée : P-IHM-03C.
- Résultat attendu : (6a) scénario A : données POST en clair sur le réseau (HTTP, pas de TLS) ; scénario B : données POST chiffrées (HTTPS = HTTP + TLS). (6b) POST masque les données de l'URL et de l'historique, mais ne les chiffre pas sur le réseau. Cas limite : GET avec HTTPS chiffre les paramètres en transit, mais ils restent dans l'historique et les logs locaux.
- Justification : la tâche « reconnaître quand et pourquoi la transmission est chiffrée » s'applique à la comparaison HTTP/HTTPS ; erreur évitée : POST confondu avec chiffrement.
- Donnée utilisée zeta dans P08 TD http get post formulaires : deux scénarios HTTP vs HTTPS avec formulaire de connexion.
- Méthode zeta dans P08 TD http get post formulaires : comparer le niveau de protection réseau (TLS ou non) indépendamment de la méthode HTTP.
- Résultat zeta dans P08 TD http get post formulaires : distinction explicite HTTP/HTTPS avec justification de la nécessité du chiffrement.
- Contrôle zeta dans P08 TD http get post formulaires : le cas limite « GET avec HTTPS » est décidé explicitement.
### Corrigé exercice 7
- Capacité mobilisée : P-IHM-04A.
- Résultat attendu : GET /club?jour=mercredi transporte jour.
- Justification : la tâche `lire jour dans URL` s applique à `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi` ; erreur évitée : bouton hors formulaire.
- Donnée utilisée eta dans P08 TD http get post formulaires : cas eta de l exercice 7 avec les valeurs indiquées dans l énoncé.
- Méthode eta dans P08 TD http get post formulaires : trace courte, pseudo-code local `if cas_eta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat eta dans P08 TD http get post formulaires : sortie vérifiable de l exercice 7, reliée à la capacité officielle du bloc.
- Contrôle eta dans P08 TD http get post formulaires : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 8
- Capacité mobilisée : P-IHM-04B.
- Résultat attendu : POST sans HTTPS ne chiffre pas.
- Justification : la tâche `distinguer GET, POST et HTTPS` s applique à `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi` ; erreur évitée : sélecteur trop large.
- Donnée utilisée theta dans P08 TD http get post formulaires : cas theta de l exercice 8 avec les valeurs indiquées dans l énoncé.
- Méthode theta dans P08 TD http get post formulaires : trace courte, pseudo-code local `if cas_theta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat theta dans P08 TD http get post formulaires : sortie vérifiable de l exercice 8, reliée à la capacité officielle du bloc.
- Contrôle theta dans P08 TD http get post formulaires : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.

### Corrigé exercice 9
- Capacité mobilisée : P-IHM-04C.
- Résultat attendu : (A) POST+HTTPS — mot de passe sensible, ne doit pas apparaître dans l'URL ni les logs. (B) GET — recherche non sensible, URL partageable. (C) POST — données personnelles, pas dans l'historique. (D) Risque : le token est visible dans la barre d'adresse, l'historique du navigateur et les logs serveur ; préférer un cookie HttpOnly ou un header Authorization avec HTTPS.
- Justification : la tâche `classer 4 cas d'usage selon GET/POST/HTTPS` s'applique à des données de confidentialité variée ; erreur évitée : croire que POST seul suffit à protéger les données.
- Donnée utilisée iota dans P08 TD http get post formulaires : cas iota de l'exercice 9 avec les quatre scénarios Web.
- Méthode iota dans P08 TD http get post formulaires : classification par critère de confidentialité (visible URL, historique, logs, chiffrement réseau).
- Résultat iota dans P08 TD http get post formulaires : tableau de classification avec justification pour chaque cas d'usage.
- Contrôle iota dans P08 TD http get post formulaires : le cas limite « POST sans HTTPS ne chiffre pas » est explicitement discuté.

## Erreurs fréquentes
- bouton hors formulaire.
- sélecteur trop large.
- POST confondu avec chiffrement.

## Différenciation
- Socle : données annotées.
- Standard : méthode complète.
- Expert : transfert avec `paramètre jour absent`.

## Cas limites travaillés
- champ nom vide.
- paramètre jour absent.
- formulaire sans action.

## Critères de réussite observables
- La donnée de départ est recopiée exactement.
- La trace ou le pseudo-code conduit à `<label for=nom>Nom</label><input id=nom name=nom>`.
- Au moins un cas limite de la section précédente est décidé.

