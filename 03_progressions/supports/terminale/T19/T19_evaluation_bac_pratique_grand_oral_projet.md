---
title: "T19 - Évaluation - bac pratique grand oral projet"
level: "terminale"
sequence_id: "T19"
document_type: "evaluation"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Synthèse"
notion: "bac pratique grand oral projet"
objectifs:
  - "évaluer la compréhension de la fiche"
  - "vérifier la capacité à produire une réponse justifiée"
  - "identifier les erreurs fréquentes"
  - "préparer une remédiation ciblée"
private_data: false
official_program:
  capacities:
    - "T-LANG-05"
---

# T19 - Évaluation - bac pratique grand oral projet

## Durée et matériel autorisé
- Durée : 25 minutes.
- Matériel autorisé : fiche personnelle, sans accès réseau ni corrigé.
- Statut : évaluation `needs_review`, non validée et non publiable.

## Capacités évaluées
- T-LANG-05

## Fiche liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T19/T19_fiche_cours_bac_pratique_grand_oral_projet.md`.
- Séance liée : `T19-S1`.
- TD lié : `T19_TD_bac_pratique_grand_oral_projet.md`.

## Consignes
Répondre directement sur copie. Chaque réponse doit montrer la donnée utilisée, la méthode et un contrôle rapide.

## Questions
### Question 1 - Lire un sujet pratique
- Capacité : T-LANG-05.
- Données : Écrire occurrence(valeurs, x) qui compte x dans valeurs.
- Consigne : Identifier entrée/sortie.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 2 - Analyser un test
- Capacité : T-LANG-05.
- Données : assert occurrence([1,2,1],1)==2 ; assert occurrence([],3)==0.
- Consigne : Dire les cas couverts.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 3 - Écrire la fonction
- Capacité : T-LANG-05.
- Données : valeurs=[4,4,2], x=4.
- Consigne : Donner code.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 4 - Préparer explication orale
- Capacité : T-LANG-05.
- Données : Fonction occurrence.
- Consigne : Plan en 45 secondes.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.

## Barème
- Question 1: 1 point identification de la donnée, 1 point méthode, 1 point résultat exact, 1 point contrôle.
- Question 2: 1 point vocabulaire précis, 1 point méthode, 1 point résultat, 1 point justification.
- Question 3: 1 point modélisation, 1 point production correcte, 1 point test du résultat, 1 point lisibilité.
- Question 4: 1 point cas traité, 1 point résultat, 1 point justification, 1 point erreur fréquente évitée.
- Total : 16 points, conversion sur 20 après relecture pédagogique.

## Corrigé professeur
### Corrigé question 1
- Capacité évaluée : T-LANG-05.
- Donnée utilisée : Écrire occurrence(valeurs, x) qui compte x dans valeurs.
- Réponse attendue : Entrée: liste valeurs et cible x. Sortie: entier nombre d’occurrences. Exemple [1,2,1],1 -> 2.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 2
- Capacité évaluée : T-LANG-05.
- Donnée utilisée : assert occurrence([1,2,1],1)==2 ; assert occurrence([],3)==0.
- Réponse attendue : Cas nominal avec doublon et cas limite liste vide.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 3
- Capacité évaluée : T-LANG-05.
- Donnée utilisée : valeurs=[4,4,2], x=4.
- Réponse attendue : def occurrence(valeurs,x): c=0 ; for v in valeurs: if v==x: c+=1 ; return c. Résultat 2.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 4
- Capacité évaluée : T-LANG-05.
- Donnée utilisée : Fonction occurrence.
- Réponse attendue : Dire contrat, boucle et invariant c compte les occurrences déjà lues, puis complexité O(n).
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
