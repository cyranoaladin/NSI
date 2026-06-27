---
title: "P08 - tp - HTML, CSS, DOM, HTTP et formulaires"
level: "premiere"
sequence_id: "P08"
document_type: "tp"
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

# P08 - TP - HTML, CSS, DOM, HTTP et formulaires

## Statut du TP
TP exécutable : le livrable élève est un fichier Python d'analyse HTML/URL complété et vérifié par tests.

## Objectifs opérationnels
- Objectif 1 : extraire un titre HTML et signaler un document sans balise `title`.
- Objectif 2 : repérer les textes associés à une classe CSS sans confondre balise, attribut et contenu.
- Objectif 3 : analyser une URL GET et transformer la chaîne de requête en dictionnaire.
- Objectif 4 : distinguer l'emplacement des paramètres selon la méthode HTTP `GET` ou `POST`.

## Donnée fournie
`<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi`

## Travail demandé
1. Préparer la donnée et nommer les champs utiles.
2. Réaliser : repérer header main form label input.
3. Réaliser : cibler #nom en CSS et DOM.
4. Tester le cas limite `champ nom vide`.
5. Produire le livrable : <label for=nom>Nom</label><input id=nom name=nom>.

## Déroulé en classe
1. Ouvrir le starter et repérer les fonctions d'analyse HTML et d'analyse HTTP.
2. Lire l'extrait HTML en distinguant balise, attribut et contenu textuel.
3. Extraire le contenu de `<title>` avant de chercher les classes CSS.
4. Pour `textes_classe`, chercher uniquement les éléments qui portent la classe demandée.
5. Vérifier sur l'exemple que la classe `alerte` donne la liste `["Erreur"]`.
6. Lire l'URL `/club?jour=mercredi` comme une ressource suivie d'une chaîne de requête.
7. Transformer `jour=mercredi` en dictionnaire `{"jour": "mercredi"}`.
8. Comparer `GET` et `POST` : les paramètres GET sont dans l'URL, les paramètres POST sont dans le corps.
9. Lancer les tests sur le starter pour identifier les fonctions encore incomplètes.
10. Relancer les tests après chaque fonction corrigée pour localiser les erreurs.

## Tests attendus à interpréter
- Test HTML : `titre_page(HTML)` doit renvoyer `"Mini site NSI"`.
- Test DOM : `textes_classe(HTML, "alerte")` doit renvoyer `["Erreur"]`.
- Test GET : `parametres_get("https://nsi.test/recherche?q=tri&page=2")` doit renvoyer `{"q": "tri", "page": "2"}`.
- Test POST : `action_formulaire("POST", {"nom": "Ada"})` doit renvoyer `"paramètres dans le corps de la requête"`.
- Test invalide : un document HTML sans `<title>` doit lever `ValueError`.

## Remédiation immédiate
- Si le titre contient des balises, reprendre la suppression du balisage avant le nettoyage des espaces.
- Si la classe absente renvoie une valeur, vérifier que le sélecteur ne récupère pas tous les paragraphes.
- Si `GET` et `POST` sont inversés, revenir au schéma URL / corps de requête.

## Barème associé
- 2 points : donnée préparée.
- 3 points : méthode principale.
- 3 points : résultat `<label for=nom>Nom</label><input id=nom name=nom>`.
- 2 points : cas limite `champ nom vide`.

## Corrigé question par question
### Corrigé question 1
Résultat attendu : `<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi`.
### Corrigé question 2
Résultat attendu : `<label for="nom">Nom</label><input id="nom" name="nom">` relie le libellé au champ.
### Corrigé question 3
Résultat attendu : `document.querySelector("#nom").value` renvoie par exemple `"Nora"` après saisie.
### Corrigé question 4
Résultat attendu : `champ nom vide` traité sans ambiguïté.

## Liens
- TD lié : `P08_TD_web_http_dom_formulaires.md`.
- Évaluation liée : `P08_evaluation_web_http_dom_formulaires.md`.

## Cas limites travaillés
- champ nom vide.
- paramètre jour absent.
- formulaire sans action.

## Erreurs fréquentes
- bouton hors formulaire.
- sélecteur trop large.
- POST confondu avec chiffrement.

## Critères de réussite observables
- La donnée de départ est recopiée exactement.
- La trace ou le pseudo-code conduit à `<label for=nom>Nom</label><input id=nom name=nom>`.
- Au moins un cas limite de la section précédente est décidé.



## Protocole de validation complémentaire
1. Préparer un jeu nominal propre à P08 et noter la sortie attendue avant exécution.
2. Préparer un cas limite distinct et expliquer pourquoi il doit être accepté ou refusé.
3. Exécuter le starter : il doit échouer sur au moins un test complet, ce qui confirme que le travail élève reste à produire.
4. Exécuter le corrigé professeur : il doit produire exactement les valeurs attendues dans les tests.
5. Comparer la trace obtenue avec la consigne : chaque étape doit être justifiée par une donnée du sujet.
6. Noter l'erreur fréquente observée et choisir la remédiation ciblée dans le support associé.

## Livrable vérifiable complémentaire
- Fichier élève complété avec les fonctions demandées dans le TP.
- Trace courte indiquant entrée, traitement, sortie et cas limite.
- Capture textuelle des tests attendus : nominal OK, cas limite OK, entrée invalide traitée.
- Commentaire final indiquant la capacité officielle réellement travaillée.

## Assets Python
- Starter élève : `code/P08_starter_web_http_dom_formulaires.py`.
- Tests attendus : `code/P08_tests_attendus_web_http_dom_formulaires.py`.
- Corrigé professeur : `code/P08_corrige_professeur_web_http_dom_formulaires.py`.
- Fonctions à compléter : `titre_page`, `textes_classe`, `parametres_get`, `action_formulaire`.
- Cas testés : titre HTML, classe DOM répétée, paramètre GET absent, formulaire sans action.
