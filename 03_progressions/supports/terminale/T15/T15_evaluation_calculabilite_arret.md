---
title: "T15 - Évaluation - calculabilité arrêt"
level: "terminale"
sequence_id: "T15"
document_type: "evaluation"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Langages et calculabilité"
notion: "calculabilité arrêt"
objectifs:
  - "évaluer la compréhension de la fiche"
  - "vérifier la capacité à produire une réponse justifiée"
  - "identifier les erreurs fréquentes"
  - "préparer une remédiation ciblée"
private_data: false
official_program:
  capacities:
    - "T-LANG-01A"
    - "T-LANG-01B"
    - "T-LANG-01C"
---

# T15 - Évaluation - calculabilité arrêt

## Durée et matériel autorisé
- Durée : 25 minutes.
- Matériel autorisé : fiche personnelle, sans accès réseau ni corrigé.
- Statut : évaluation `needs_review`, non validée et non publiable.

## Capacités évaluées
- T-LANG-01A
- T-LANG-01B
- T-LANG-01C

## Fiche liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T15/T15_fiche_cours_calculabilite_arret.md`.
- Séance liée : `T15-S1`.
- TD lié : `T15_TD_calculabilite_arret.md`.

## Consignes
Répondre directement sur copie. Chaque réponse doit montrer la donnée utilisée, la méthode et un contrôle rapide.

## Questions
### Question 1 - Tracer une boucle terminante
- Capacité : T-LANG-01A.
- Données : n=3 ; while n>0: n=n-1.
- Consigne : Donner la trace.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 2 - Repérer une boucle infinie
- Capacité : T-LANG-01B.
- Données : while True: pass.
- Consigne : Dire ce qui manque pour terminer.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 3 - Écrire un variant
- Capacité : T-LANG-01C.
- Données : while n>0: n=n//2 pour n=10.
- Consigne : Donner variant et trace.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 4 - Construire un semi-décideur
- Capacité : T-LANG-01A.
- Données : Chercher si une valeur apparaît dans un flux infini.
- Consigne : Expliquer.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.

## Barème
- Question 1: 1 point identification de la donnée, 1 point méthode, 1 point résultat exact, 1 point contrôle.
- Question 2: 1 point vocabulaire précis, 1 point méthode, 1 point résultat, 1 point justification.
- Question 3: 1 point modélisation, 1 point production correcte, 1 point test du résultat, 1 point lisibilité.
- Question 4: 1 point cas traité, 1 point résultat, 1 point justification, 1 point erreur fréquente évitée.
- Total : 16 points, conversion sur 20 après relecture pédagogique.

## Corrigé professeur
### Corrigé question 1
- Capacité évaluée : T-LANG-01A.
- Donnée utilisée : n=3 ; while n>0: n=n-1.
- Réponse attendue : Trace n: 3 -> 2 -> 1 -> 0, puis condition n>0 fausse. Le programme termine.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 2
- Capacité évaluée : T-LANG-01B.
- Donnée utilisée : while True: pass.
- Réponse attendue : Aucune variable ne rapproche d’un cas d’arrêt et la condition reste True. La boucle ne termine pas.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 3
- Capacité évaluée : T-LANG-01C.
- Donnée utilisée : while n>0: n=n//2 pour n=10.
- Réponse attendue : Variant n entier naturel diminue: 10 -> 5 -> 2 -> 1 -> 0. Il assure la terminaison.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 4
- Capacité évaluée : T-LANG-01A.
- Donnée utilisée : Chercher si une valeur apparaît dans un flux infini.
- Réponse attendue : On lit les valeurs une à une ; si cible trouvée, on répond oui. Si elle n’apparaît jamais, l’algorithme peut tourner sans répondre.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.

## Critères de réussite
- Les capacités officielles sont reliées à une action observable.
- Le résultat attendu peut être comparé à une valeur, une table, une trace ou un pseudo-code.
- Le cas limite ou le contrôle demandé apparaît explicitement.
- Le vocabulaire disciplinaire est utilisé dans le contexte de la donnée.

## Version aménagée et indications d’aménagement
- Version aménagée : conserver les mêmes questions mais fournir la donnée surlignée et un tableau méthode / résultat / contrôle.
- Aménagement temps : ajouter 10 minutes si l’élève doit recopier les données.
- Aide autorisée : liste des verbes d’action, sans résultat numérique ni requête complète.

## Erreurs fréquentes et remédiation
- EF1 : réponse sans donnée citée ; remédiation : refaire la question 1 avec les valeurs encadrées.
- EF2 : méthode correcte mais résultat non contrôlé ; remédiation : ajouter une ligne de vérification.
- EF3 : confusion entre vocabulaire et preuve ; remédiation : demander une phrase « parce que ».
- EF4 : oubli du cas limite ; remédiation : reprendre le TD associé, exercice 5.

## Source et traçabilité
- Recherche locale effectuée dans le dossier Documents_DRIVE avant création.
- Aucun fichier Drive n’a été repris directement dans cette évaluation.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
