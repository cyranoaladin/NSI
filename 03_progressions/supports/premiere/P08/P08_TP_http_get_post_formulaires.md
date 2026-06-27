---
title: "P08 - tp_papier - HTML, CSS, DOM, HTTP et formulaires"
level: "premiere"
sequence_id: "P08"
document_type: "tp_papier"
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
TP papier : ce support n attend aucune ressource Python ; le livrable est une trace écrite vérifiable.

## Donnée fournie
`<form method=post action=/reservation><input id=nom name=nom></form>, URL /club?jour=mercredi`

## Travail demandé
1. Préparer la donnée et nommer les champs utiles.
2. Réaliser : repérer header main form label input.
3. Réaliser : cibler #nom en CSS et DOM.
4. Tester le cas limite `champ nom vide`.
5. Produire le livrable : <label for=nom>Nom</label><input id=nom name=nom>.

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
