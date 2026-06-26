---
title: "T11 - Évaluation - processus ordonnancement interblocage"
level: "terminale"
sequence_id: "T11"
document_type: "evaluation"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Architecture"
notion: "processus ordonnancement interblocage"
objectifs:
  - "évaluer la compréhension de la fiche"
  - "vérifier la capacité à produire une réponse justifiée"
  - "identifier les erreurs fréquentes"
  - "préparer une remédiation ciblée"
private_data: false
official_program:
  capacities:
    - "T-ARCH-01"
    - "T-ARCH-02A"
    - "T-ARCH-02B"
    - "T-ARCH-02C"
---

# T11 - Évaluation - processus ordonnancement interblocage

## Durée et matériel autorisé
- Durée : 25 minutes.
- Matériel autorisé : fiche personnelle, sans accès réseau ni corrigé.
- Statut : évaluation `needs_review`, non validée et non publiable.

## Capacités évaluées
- T-ARCH-01
- T-ARCH-02A
- T-ARCH-02B
- T-ARCH-02C

## Fiche liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T11/T11_fiche_cours_processus_ordonnancement_interblocage.md`.
- Séance liée : `T11-S1`.
- TD lié : `T11_TD_processus_ordonnancement_interblocage.md`.

## Consignes
Répondre directement sur copie. Chaque réponse doit montrer la donnée utilisée, la méthode et un contrôle rapide.

## Questions
### Question 1 - Tracer FCFS
- Capacité : T-ARCH-01.
- Données : P1 arrivée 0 durée 3 ; P2 arrivée 1 durée 2 ; P3 arrivée 2 durée 1.
- Consigne : Donner le diagramme.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 2 - Tracer Round Robin quantum 1
- Capacité : T-ARCH-02A.
- Données : P1 durée 3, P2 durée 2, arrivées toutes à 0.
- Consigne : Donner la séquence CPU.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 3 - Calculer temps de séjour
- Capacité : T-ARCH-02B.
- Données : Données FCFS de l’exercice 1.
- Consigne : Calculer turnaround.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 4 - Écrire un pseudo-code ordonnanceur simple
- Capacité : T-ARCH-02C.
- Données : File prête [P1,P2,P3].
- Consigne : Produire pseudo-code FCFS.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.

## Barème
- Question 1: 1 point identification de la donnée, 1 point méthode, 1 point résultat exact, 1 point contrôle.
- Question 2: 1 point vocabulaire précis, 1 point méthode, 1 point résultat, 1 point justification.
- Question 3: 1 point modélisation, 1 point production correcte, 1 point test du résultat, 1 point lisibilité.
- Question 4: 1 point cas traité, 1 point résultat, 1 point justification, 1 point erreur fréquente évitée.
- Total : 16 points, conversion sur 20 après relecture pédagogique.

## Corrigé professeur
### Corrigé question 1
- Capacité évaluée : T-ARCH-01.
- Donnée utilisée : P1 arrivée 0 durée 3 ; P2 arrivée 1 durée 2 ; P3 arrivée 2 durée 1.
- Réponse attendue : FCFS: P1 de 0 à 3, P2 de 3 à 5, P3 de 5 à 6. Attentes: P1=0, P2=2, P3=3.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 2
- Capacité évaluée : T-ARCH-02A.
- Donnée utilisée : P1 durée 3, P2 durée 2, arrivées toutes à 0.
- Réponse attendue : RR q=1: P1(0-1), P2(1-2), P1(2-3), P2(3-4), P1(4-5). Fin P2=4, P1=5.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 3
- Capacité évaluée : T-ARCH-02B.
- Donnée utilisée : Données FCFS de l’exercice 1.
- Réponse attendue : Séjour = fin - arrivée: P1=3-0=3, P2=5-1=4, P3=6-2=4.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 4
- Capacité évaluée : T-ARCH-02C.
- Donnée utilisée : File prête [P1,P2,P3].
- Réponse attendue : tant que file non vide: p=defiler(); exécuter p jusqu’à fin; enregistrer temps_fin[p]. La file conserve l’ordre d’arrivée.
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
