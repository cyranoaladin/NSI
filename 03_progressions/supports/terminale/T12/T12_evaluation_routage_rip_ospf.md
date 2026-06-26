---
title: "T12 - Évaluation - routage RIP OSPF"
level: "terminale"
sequence_id: "T12"
document_type: "evaluation"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Réseaux"
notion: "routage RIP OSPF"
objectifs:
  - "évaluer la compréhension de la fiche"
  - "vérifier la capacité à produire une réponse justifiée"
  - "identifier les erreurs fréquentes"
  - "préparer une remédiation ciblée"
private_data: false
official_program:
  capacities:
    - "T-ARCH-03"
---

# T12 - Évaluation - routage RIP OSPF

## Durée et matériel autorisé
- Durée : 25 minutes.
- Matériel autorisé : fiche personnelle, sans accès réseau ni corrigé.
- Statut : évaluation `needs_review`, non validée et non publiable.

## Capacités évaluées
- T-ARCH-03

## Fiche liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T12/T12_fiche_cours_routage_rip_ospf.md`.
- Séance liée : `T12-S1`.
- TD lié : `T12_TD_routage_rip_ospf.md`.

## Consignes
Répondre directement sur copie. Chaque réponse doit montrer la donnée utilisée, la méthode et un contrôle rapide.

## Questions
### Question 1 - Lire une table de routage
- Capacité : T-ARCH-03.
- Données : R1 connaît R2 coût1, R3 coût4 direct, R4 via R3 coût6.
- Consigne : Identifier la meilleure route vers R3.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 2 - Calculer métrique RIP
- Capacité : T-ARCH-03.
- Données : R1 vers R4 via R2 puis R3, 3 sauts.
- Consigne : Donner métrique.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 3 - Appliquer Dijkstra OSPF
- Capacité : T-ARCH-03.
- Données : Coûts: R1-R2=1, R2-R3=1, R1-R3=4, R3-R4=2.
- Consigne : Donner distances depuis R1.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 4 - Écrire une entrée de table
- Capacité : T-ARCH-03.
- Données : Destination réseau 10.4.0.0/24 derrière R4.
- Consigne : Donner next-hop depuis R1.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.

## Barème
- Question 1: 1 point identification de la donnée, 1 point méthode, 1 point résultat exact, 1 point contrôle.
- Question 2: 1 point vocabulaire précis, 1 point méthode, 1 point résultat, 1 point justification.
- Question 3: 1 point modélisation, 1 point production correcte, 1 point test du résultat, 1 point lisibilité.
- Question 4: 1 point cas traité, 1 point résultat, 1 point justification, 1 point erreur fréquente évitée.
- Total : 16 points, conversion sur 20 après relecture pédagogique.

## Corrigé professeur
### Corrigé question 1
- Capacité évaluée : T-ARCH-03.
- Donnée utilisée : R1 connaît R2 coût1, R3 coût4 direct, R4 via R3 coût6.
- Réponse attendue : Meilleure route R1->R2->R3 coût 2 si R2 annonce R3 à 1 ; elle bat le lien direct coût 4.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 2
- Capacité évaluée : T-ARCH-03.
- Donnée utilisée : R1 vers R4 via R2 puis R3, 3 sauts.
- Réponse attendue : En RIP, la métrique est le nombre de sauts: R1->R2, R2->R3, R3->R4 donc 3.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 3
- Capacité évaluée : T-ARCH-03.
- Donnée utilisée : Coûts: R1-R2=1, R2-R3=1, R1-R3=4, R3-R4=2.
- Réponse attendue : D(R1)=0, D(R2)=1, D(R3)=2 via R2, D(R4)=4 via R2 puis R3.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 4
- Capacité évaluée : T-ARCH-03.
- Donnée utilisée : Destination réseau 10.4.0.0/24 derrière R4.
- Réponse attendue : Entrée: destination 10.4.0.0/24, next-hop R2, coût OSPF 4. Le chemin calculé est R1-R2-R3-R4.
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
