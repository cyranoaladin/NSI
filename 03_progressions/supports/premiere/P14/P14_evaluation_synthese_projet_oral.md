---
title: "P14 - Évaluation - synthese projet oral"
level: "premiere"
sequence_id: "P14"
document_type: "evaluation"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Synthèse et projet"
notion: "synthese projet oral"
objectifs:
  - "évaluer la compréhension de la fiche"
  - "vérifier la capacité à produire une réponse justifiée"
  - "identifier les erreurs fréquentes"
  - "préparer une remédiation ciblée"
private_data: false
official_program:
  capacities:
    - "P-HIST-01"
---

# P14 - Évaluation - synthèse projet oral

## Durée et matériel autorisé
- Durée : 25 minutes.
- Matériel autorisé : fiche personnelle, sans accès réseau ni corrigé.
- Statut : évaluation `needs_review`, non validée et non publiable.

## Capacités évaluées
- P-HIST-01

## Fiche liée
- Fiche liée : `03_progressions/fiches_cours/premiere/P14/P14_fiche_cours_synthese_projet_oral.md`.
- Séance liée : `P14-S1`.
- TD lié : `P14_TD_synthese_projet_oral.md`.

## Consignes
Répondre directement sur copie. Chaque réponse doit montrer la donnée utilisée, la méthode et un contrôle rapide.

## Questions
### Question 1 - Lire un cahier des charges
- Capacité : P-HIST-01.
- Données : Projet: carnet de scores, données stockées en CSV, recherche par joueur, tri par score.
- Consigne : Identifier deux fonctionnalités et deux contraintes.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 2 - Analyser un extrait de test
- Capacité : P-HIST-01.
- Données : assert meilleur_score([12,9,15]) == 15 ; assert meilleur_score([]) is None.
- Consigne : Dire les cas couverts.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 3 - Rédiger une spécification de fonction
- Capacité : P-HIST-01.
- Données : fonction moyenne_scores(scores).
- Consigne : Écrire entrée, sortie, cas limite.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 4 - Construire un plan d’oral
- Capacité : P-HIST-01.
- Données : Sujet: expliquer un tri utilisé dans le projet.
- Consigne : Donner un plan en trois parties.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.

## Barème
- Question 1: 1 point identification de la donnée, 1 point méthode, 1 point résultat exact, 1 point contrôle.
- Question 2: 1 point vocabulaire précis, 1 point méthode, 1 point résultat, 1 point justification.
- Question 3: 1 point modélisation, 1 point production correcte, 1 point test du résultat, 1 point lisibilité.
- Question 4: 1 point cas traité, 1 point résultat, 1 point justification, 1 point erreur fréquente évitée.
- Total : 16 points, conversion sur 20 après relecture pédagogique.

## Corrigé professeur
### Corrigé question 1
- Capacité évaluée : P-HIST-01.
- Donnée utilisée : Projet: carnet de scores, données stockées en CSV, recherche par joueur, tri par score.
- Réponse attendue : Fonctionnalités: ajouter un score, rechercher un joueur, trier par score. Contraintes: format CSV cohérent et tests sur recherche/tri.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 2
- Capacité évaluée : P-HIST-01.
- Donnée utilisée : assert meilleur_score([12,9,15]) == 15 ; assert meilleur_score([]) is None.
- Réponse attendue : Premier test couvre cas nominal avec maximum 15 ; second test couvre cas limite liste vide, contrat None.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 3
- Capacité évaluée : P-HIST-01.
- Donnée utilisée : fonction moyenne_scores(scores).
- Réponse attendue : Entrée: liste de nombres. Sortie: moyenne flottante. Cas limite: liste vide -> None ou ValueError ; choix à fixer dans la spécification.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 4
- Capacité évaluée : P-HIST-01.
- Donnée utilisée : Sujet: expliquer un tri utilisé dans le projet.
- Réponse attendue : Plan: 1 contexte du besoin ; 2 principe du tri avec exemple [3,1,2] -> [1,2,3] ; 3 limites et complexité O(n^2) ou O(n log n) selon algorithme.
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
