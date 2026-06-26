---
title: "P11 - Évaluation - parcours recherche extremum moyenne"
level: "premiere"
sequence_id: "P11"
document_type: "evaluation"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Algorithmique"
notion: "parcours recherche extremum moyenne"
objectifs:
  - "évaluer la compréhension de la fiche"
  - "vérifier la capacité à produire une réponse justifiée"
  - "identifier les erreurs fréquentes"
  - "préparer une remédiation ciblée"
private_data: false
official_program:
  capacities:
    - "P-ALGO-01A"
    - "P-ALGO-01B"
---

# P11 - Évaluation - parcours recherche extremum moyenne

## Durée et matériel autorisé
- Durée : 25 minutes.
- Matériel autorisé : fiche personnelle, sans accès réseau ni corrigé.
- Statut : évaluation `needs_review`, non validée et non publiable.

## Capacités évaluées
- P-ALGO-01A
- P-ALGO-01B

## Fiche liée
- Fiche liée : `03_progressions/fiches_cours/premiere/P11/P11_fiche_cours_parcours_recherche_extremum_moyenne.md`.
- Séance liée : `P11-S1`.
- TD lié : `P11_TD_parcours_recherche_extremum_moyenne.md`.

## Consignes
Répondre directement sur copie. Chaque réponse doit montrer la donnée utilisée, la méthode et un contrôle rapide.

## Questions
### Question 1 - Tracer une recherche séquentielle
- Capacité : P-ALGO-01A.
- Données : liste = [12, 7, 19, 7, 3], valeur cherchée = 7.
- Consigne : Donner les indices lus jusqu’à la première occurrence.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 2 - Calculer un maximum avec trace
- Capacité : P-ALGO-01B.
- Données : mesures = [4, 11, 6, 11, 2].
- Consigne : Donner la valeur de max après chaque élément.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 3 - Écrire un parcours de moyenne
- Capacité : P-ALGO-01A.
- Données : notes = [8, 12, 15, 5].
- Consigne : Écrire un pseudo-code qui renvoie la moyenne.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 4 - Écrire une recherche avec booléen
- Capacité : P-ALGO-01B.
- Données : mots = ["NSI", "maths", "SI"], cible="physique".
- Consigne : Produire un algorithme qui renvoie True ou False.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.

## Barème
- Question 1: 1 point identification de la donnée, 1 point méthode, 1 point résultat exact, 1 point contrôle.
- Question 2: 1 point vocabulaire précis, 1 point méthode, 1 point résultat, 1 point justification.
- Question 3: 1 point modélisation, 1 point production correcte, 1 point test du résultat, 1 point lisibilité.
- Question 4: 1 point cas traité, 1 point résultat, 1 point justification, 1 point erreur fréquente évitée.
- Total : 16 points, conversion sur 20 après relecture pédagogique.

## Corrigé professeur
### Corrigé question 1
- Capacité évaluée : P-ALGO-01A.
- Donnée utilisée : liste = [12, 7, 19, 7, 3], valeur cherchée = 7.
- Réponse attendue : On lit indice 0 -> 12, puis indice 1 -> 7. La première occurrence est à l’indice 1 ; on peut arrêter la recherche.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 2
- Capacité évaluée : P-ALGO-01B.
- Donnée utilisée : mesures = [4, 11, 6, 11, 2].
- Réponse attendue : Trace max: départ 4 ; après 11 -> 11 ; après 6 -> 11 ; après 11 -> 11 ; après 2 -> 11. Maximum final 11.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 3
- Capacité évaluée : P-ALGO-01A.
- Donnée utilisée : notes = [8, 12, 15, 5].
- Réponse attendue : Pseudo-code: somme=0 ; pour x dans notes: somme=somme+x ; moyenne=somme/len(notes). Ici somme=40, len=4, moyenne=10.0.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 4
- Capacité évaluée : P-ALGO-01B.
- Donnée utilisée : mots = ["NSI", "maths", "SI"], cible="physique".
- Réponse attendue : trouve=False ; pour mot dans mots: si mot==cible alors trouve=True. Aucune égalité trouvée ; résultat False.
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
