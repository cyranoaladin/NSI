---
title: "T16 - Évaluation - diviser pour régner tri fusion"
level: "terminale"
sequence_id: "T16"
document_type: "evaluation"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Algorithmique"
notion: "diviser pour régner tri fusion"
objectifs:
  - "évaluer la compréhension de la fiche"
  - "vérifier la capacité à produire une réponse justifiée"
  - "identifier les erreurs fréquentes"
  - "préparer une remédiation ciblée"
private_data: false
official_program:
  capacities:
    - "T-ALGO-03"
---

# T16 - Évaluation - diviser pour régner tri fusion

## Durée et matériel autorisé
- Durée : 25 minutes.
- Matériel autorisé : fiche personnelle, sans accès réseau ni corrigé.
- Statut : évaluation `needs_review`, non validée et non publiable.

## Capacités évaluées
- T-ALGO-03

## Fiche liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T16/T16_fiche_cours_diviser_pour_regner_tri_fusion.md`.
- Séance liée : `T16-S1`.
- TD lié : `T16_TD_diviser_pour_regner_tri_fusion.md`.

## Consignes
Répondre directement sur copie. Chaque réponse doit montrer la donnée utilisée, la méthode et un contrôle rapide.

## Questions
### Question 1 - Découper une liste
- Capacité : T-ALGO-03.
- Données : [8,3,5,1,9,2].
- Consigne : Donner les deux moitiés.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 2 - Fusionner deux listes triées
- Capacité : T-ALGO-03.
- Données : [2,5,8] et [1,3,9].
- Consigne : Donner la fusion.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 3 - Écrire pseudo-code fusion
- Capacité : T-ALGO-03.
- Données : g=[2,8], d=[1,5].
- Consigne : Produire pseudo-code.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 4 - Tracer tri fusion complet
- Capacité : T-ALGO-03.
- Données : [4,1,3,2].
- Consigne : Donner étapes.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.

## Barème
- Question 1: 1 point identification de la donnée, 1 point méthode, 1 point résultat exact, 1 point contrôle.
- Question 2: 1 point vocabulaire précis, 1 point méthode, 1 point résultat, 1 point justification.
- Question 3: 1 point modélisation, 1 point production correcte, 1 point test du résultat, 1 point lisibilité.
- Question 4: 1 point cas traité, 1 point résultat, 1 point justification, 1 point erreur fréquente évitée.
- Total : 16 points, conversion sur 20 après relecture pédagogique.

## Corrigé professeur
### Corrigé question 1
- Capacité évaluée : T-ALGO-03.
- Donnée utilisée : [8,3,5,1,9,2].
- Réponse attendue : Moitié gauche [8,3,5], moitié droite [1,9,2]. On continue jusqu’aux listes de taille 1.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 2
- Capacité évaluée : T-ALGO-03.
- Donnée utilisée : [2,5,8] et [1,3,9].
- Réponse attendue : Comparer têtes: 1, puis 2, puis 3, puis 5, puis 8, puis 9. Résultat [1,2,3,5,8,9].
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 3
- Capacité évaluée : T-ALGO-03.
- Donnée utilisée : g=[2,8], d=[1,5].
- Réponse attendue : i=j=0 ; tant que i<len(g) et j<len(d), prendre le plus petit ; ajouter le reste. Résultat [1,2,5,8].
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 4
- Capacité évaluée : T-ALGO-03.
- Donnée utilisée : [4,1,3,2].
- Réponse attendue : Découpe [4,1]|[3,2], puis [4],[1],[3],[2]. Fusions [1,4], [2,3], puis [1,2,3,4].
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
