---
title: "P13 - Évaluation - dichotomie glouton k-NN"
level: "premiere"
sequence_id: "P13"
document_type: "evaluation"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Algorithmique"
notion: "dichotomie glouton k-NN"
objectifs:
  - "évaluer la compréhension de la fiche"
  - "vérifier la capacité à produire une réponse justifiée"
  - "identifier les erreurs fréquentes"
  - "préparer une remédiation ciblée"
private_data: false
official_program:
  capacities:
    - "P-ALGO-03"
    - "P-ALGO-04"
    - "P-ALGO-05"
---

# P13 - Évaluation - dichotomie glouton knn

## Durée et matériel autorisé
- Durée : 25 minutes.
- Matériel autorisé : fiche personnelle, sans accès réseau ni corrigé.
- Statut : évaluation `needs_review`, non validée et non publiable.

## Capacités évaluées
- P-ALGO-03
- P-ALGO-04
- P-ALGO-05

## Fiche liée
- Fiche liée : `03_progressions/fiches_cours/premiere/P13/P13_fiche_cours_dichotomie_glouton_knn.md`.
- Séance liée : `P13-S1`.
- TD lié : `P13_TD_dichotomie_glouton_knn.md`.

## Consignes
Répondre directement sur copie. Chaque réponse doit montrer la donnée utilisée, la méthode et un contrôle rapide.

## Questions
### Question 1 - Tracer une recherche dichotomique
- Capacité : P-ALGO-03.
- Données : tableau trié [3,8,12,19,27,31], cible=19.
- Consigne : Donner les bornes et milieux successifs.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 2 - Repérer la condition de tri
- Capacité : P-ALGO-04.
- Données : tableau [4,9,2,11], cible=2.
- Consigne : Dire si la dichotomie est applicable.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 3 - Écrire un glouton de monnaie
- Capacité : P-ALGO-05.
- Données : pièces [50,20,10,5,2,1], montant=87.
- Consigne : Donner les pièces choisies.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 4 - Calculer un k-NN
- Capacité : P-ALGO-03.
- Données : Points A(0,0) rouge, B(2,0) rouge, C(0,3) bleu ; point X(1,1), k=3.
- Consigne : Calculer les distances carrées et la classe.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.

## Barème
- Question 1: 1 point identification de la donnée, 1 point méthode, 1 point résultat exact, 1 point contrôle.
- Question 2: 1 point vocabulaire précis, 1 point méthode, 1 point résultat, 1 point justification.
- Question 3: 1 point modélisation, 1 point production correcte, 1 point test du résultat, 1 point lisibilité.
- Question 4: 1 point cas traité, 1 point résultat, 1 point justification, 1 point erreur fréquente évitée.
- Total : 16 points, conversion sur 20 après relecture pédagogique.

## Corrigé professeur
### Corrigé question 1
- Capacité évaluée : P-ALGO-03.
- Donnée utilisée : tableau trié [3,8,12,19,27,31], cible=19.
- Réponse attendue : g=0,d=5,m=2,val=12 -> cible à droite ; g=3,d=5,m=4,val=27 -> cible à gauche ; g=3,d=3,m=3,val=19 -> trouvé indice 3.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 2
- Capacité évaluée : P-ALGO-04.
- Donnée utilisée : tableau [4,9,2,11], cible=2.
- Réponse attendue : Non, le tableau n’est pas trié. Une dichotomie pourrait éliminer la mauvaise moitié. Il faut trier ou utiliser une recherche séquentielle.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 3
- Capacité évaluée : P-ALGO-05.
- Donnée utilisée : pièces [50,20,10,5,2,1], montant=87.
- Réponse attendue : Choix glouton: 50 reste 37 ; 20 reste 17 ; 10 reste 7 ; 5 reste 2 ; 2 reste 0. Réponse [50,20,10,5,2].
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 4
- Capacité évaluée : P-ALGO-03.
- Donnée utilisée : Points A(0,0) rouge, B(2,0) rouge, C(0,3) bleu ; point X(1,1), k=3.
- Réponse attendue : d2(A)=2, d2(B)=2, d2(C)=5. Les 3 voisins contiennent 2 rouges et 1 bleu ; X est classé rouge.
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
