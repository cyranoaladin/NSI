---
title: "T14 - Évaluation - modularité API paradigmes bugs"
level: "terminale"
sequence_id: "T14"
document_type: "evaluation"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Langages"
notion: "modularité API paradigmes bugs"
objectifs:
  - "évaluer la compréhension de la fiche"
  - "vérifier la capacité à produire une réponse justifiée"
  - "identifier les erreurs fréquentes"
  - "préparer une remédiation ciblée"
private_data: false
official_program:
  capacities:
    - "T-LANG-03A"
    - "T-LANG-03B"
    - "T-LANG-03C"
    - "T-LANG-04A"
    - "T-LANG-04B"
    - "T-LANG-05"
---

# T14 - Évaluation - modularité API paradigmes bugs

## Durée et matériel autorisé
- Durée : 25 minutes.
- Matériel autorisé : fiche personnelle, sans accès réseau ni corrigé.
- Statut : évaluation `needs_review`, non validée et non publiable.

## Capacités évaluées
- T-LANG-03A
- T-LANG-03B
- T-LANG-03C
- T-LANG-04A
- T-LANG-04B
- T-LANG-05

## Fiche liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T14/T14_fiche_cours_modularite_api_paradigmes_bugs.md`.
- Séance liée : `T14-S1`.
- TD lié : `T14_TD_modularite_api_paradigmes_bugs.md`.

## Consignes
Répondre directement sur copie. Chaque réponse doit montrer la donnée utilisée, la méthode et un contrôle rapide.

## Questions
### Question 1 - Identifier une API
- Capacité : T-LANG-03A.
- Données : Module notes.py expose moyenne(notes) et mediane(notes).
- Consigne : Dire ce qui appartient à l’API.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 2 - Lire une trace d’erreur
- Capacité : T-LANG-03B.
- Données : TypeError: unsupported operand type(s) for +: int and str dans somme += note.
- Consigne : Identifier la cause.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 3 - Écrire une fonction pure
- Capacité : T-LANG-03C.
- Données : notes=[10,14,16].
- Consigne : Coder moyenne sans effet de bord.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 4 - Ajouter un test unitaire
- Capacité : T-LANG-04A.
- Données : moyenne([10,20]) doit valoir 15.
- Consigne : Écrire un assert.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.

## Barème
- Question 1: 1 point identification de la donnée, 1 point méthode, 1 point résultat exact, 1 point contrôle.
- Question 2: 1 point vocabulaire précis, 1 point méthode, 1 point résultat, 1 point justification.
- Question 3: 1 point modélisation, 1 point production correcte, 1 point test du résultat, 1 point lisibilité.
- Question 4: 1 point cas traité, 1 point résultat, 1 point justification, 1 point erreur fréquente évitée.
- Total : 16 points, conversion sur 20 après relecture pédagogique.

## Corrigé professeur
### Corrigé question 1
- Capacité évaluée : T-LANG-03A.
- Donnée utilisée : Module notes.py expose moyenne(notes) et mediane(notes).
- Réponse attendue : Les signatures moyenne(notes) et mediane(notes), leur contrat d’entrée/sortie et exceptions appartiennent à l’API ; les variables internes non.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 2
- Capacité évaluée : T-LANG-03B.
- Donnée utilisée : TypeError: unsupported operand type(s) for +: int and str dans somme += note.
- Réponse attendue : Une note est une chaîne comme "12" au lieu d’un entier/float. Il faut convertir ou valider l’entrée.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 3
- Capacité évaluée : T-LANG-03C.
- Donnée utilisée : notes=[10,14,16].
- Réponse attendue : def moyenne(notes): return sum(notes)/len(notes). Pour [10,14,16], résultat 40/3 environ 13.33 ; la liste n’est pas modifiée.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 4
- Capacité évaluée : T-LANG-04A.
- Donnée utilisée : moyenne([10,20]) doit valoir 15.
- Réponse attendue : assert moyenne([10,20]) == 15. On ajoute aussi le cas vide selon contrat, par exemple pytest.raises(ValueError).
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
