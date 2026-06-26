---
title: "T18 - Évaluation - Boyer-Moore"
level: "terminale"
sequence_id: "T18"
document_type: "evaluation"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Algorithmique"
notion: "Boyer-Moore"
objectifs:
  - "évaluer la compréhension de la fiche"
  - "vérifier la capacité à produire une réponse justifiée"
  - "identifier les erreurs fréquentes"
  - "préparer une remédiation ciblée"
private_data: false
official_program:
  capacities:
    - "T-ALGO-05"
---

# T18 - Évaluation - Boyer-Moore

## Durée et matériel autorisé
- Durée : 25 minutes.
- Matériel autorisé : fiche personnelle, sans accès réseau ni corrigé.
- Statut : évaluation `needs_review`, non validée et non publiable.

## Capacités évaluées
- T-ALGO-05

## Fiche liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T18/T18_fiche_cours_boyer_moore.md`.
- Séance liée : `T18-S1`.
- TD lié : `T18_TD_boyer_moore.md`.

## Consignes
Répondre directement sur copie. Chaque réponse doit montrer la donnée utilisée, la méthode et un contrôle rapide.

## Questions
### Question 1 - Construire table mauvais caractère
- Capacité : T-ALGO-05.
- Données : motif ABA.
- Consigne : Donner derniers indices.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 2 - Comparer depuis la droite
- Capacité : T-ALGO-05.
- Données : texte CABAABABA, motif ABA aligné au début.
- Consigne : Donner première comparaison.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 3 - Tracer la première occurrence
- Capacité : T-ALGO-05.
- Données : texte CABAABABA, motif ABA.
- Consigne : Donner indice trouvé.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 4 - Écrire pseudo-code simplifié
- Capacité : T-ALGO-05.
- Données : motif m, texte t.
- Consigne : Produire boucle.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.

## Barème
- Question 1: 1 point identification de la donnée, 1 point méthode, 1 point résultat exact, 1 point contrôle.
- Question 2: 1 point vocabulaire précis, 1 point méthode, 1 point résultat, 1 point justification.
- Question 3: 1 point modélisation, 1 point production correcte, 1 point test du résultat, 1 point lisibilité.
- Question 4: 1 point cas traité, 1 point résultat, 1 point justification, 1 point erreur fréquente évitée.
- Total : 16 points, conversion sur 20 après relecture pédagogique.

## Corrigé professeur
### Corrigé question 1
- Capacité évaluée : T-ALGO-05.
- Donnée utilisée : motif ABA.
- Réponse attendue : A apparaît aux indices 0 et 2, donc dernier indice A=2 ; B=1 ; autre caractère -> -1.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 2
- Capacité évaluée : T-ALGO-05.
- Donnée utilisée : texte CABAABABA, motif ABA aligné au début.
- Réponse attendue : On compare motif[2]=A avec texte[2]=B : mismatch B. Dernier B dans motif à 1, décalage max(1,2-1)=1.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 3
- Capacité évaluée : T-ALGO-05.
- Donnée utilisée : texte CABAABABA, motif ABA.
- Réponse attendue : Après décalage 1, alignement texte[1:4]=ABA. Comparaisons droite à gauche A=A, B=B, A=A. Occurrence trouvée à l’indice 1.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 4
- Capacité évaluée : T-ALGO-05.
- Donnée utilisée : motif m, texte t.
- Réponse attendue : i=0 ; tant que i<=n-p: comparer j=p-1 vers 0 ; si j<0 retourner i ; sinon i += max(1, j-last[t[i+j]]).
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
