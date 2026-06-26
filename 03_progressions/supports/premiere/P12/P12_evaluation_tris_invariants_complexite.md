---
title: "P12 - Évaluation - tris invariants complexité"
level: "premiere"
sequence_id: "P12"
document_type: "evaluation"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Algorithmique"
notion: "tris invariants complexité"
objectifs:
  - "évaluer la compréhension de la fiche"
  - "vérifier la capacité à produire une réponse justifiée"
  - "identifier les erreurs fréquentes"
  - "préparer une remédiation ciblée"
private_data: false
official_program:
  capacities:
    - "P-ALGO-02A"
    - "P-ALGO-02B"
    - "P-ALGO-02C"
    - "P-ALGO-02D"
---

# P12 - Évaluation - tris invariants complexité

## Durée et matériel autorisé
- Durée : 25 minutes.
- Matériel autorisé : fiche personnelle, sans accès réseau ni corrigé.
- Statut : évaluation `needs_review`, non validée et non publiable.

## Capacités évaluées
- P-ALGO-02A
- P-ALGO-02B
- P-ALGO-02C
- P-ALGO-02D

## Fiche liée
- Fiche liée : `03_progressions/fiches_cours/premiere/P12/P12_fiche_cours_tris_invariants_complexite.md`.
- Séance liée : `P12-S1`.
- TD lié : `P12_TD_tris_invariants_complexite.md`.

## Consignes
Répondre directement sur copie. Chaque réponse doit montrer la donnée utilisée, la méthode et un contrôle rapide.

## Questions
### Question 1 - Tracer un tri par insertion
- Capacité : P-ALGO-02A.
- Données : liste initiale [5, 2, 4, 1].
- Consigne : Donner les états après chaque insertion.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 2 - Reconnaître un invariant
- Capacité : P-ALGO-02B.
- Données : Dans le tri par insertion, après l’étape i, le préfixe de longueur i+1 est trié.
- Consigne : Vérifier l’invariant après l’insertion de 4 dans [5,2,4,1].
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 3 - Écrire un tri par sélection
- Capacité : P-ALGO-02C.
- Données : liste [3, 1, 4, 2].
- Consigne : Donner pseudo-code et premier échange.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 4 - Compter les comparaisons
- Capacité : P-ALGO-02D.
- Données : tri par sélection sur n=5 éléments.
- Consigne : Calculer le nombre de comparaisons.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.

## Barème
- Question 1: 1 point identification de la donnée, 1 point méthode, 1 point résultat exact, 1 point contrôle.
- Question 2: 1 point vocabulaire précis, 1 point méthode, 1 point résultat, 1 point justification.
- Question 3: 1 point modélisation, 1 point production correcte, 1 point test du résultat, 1 point lisibilité.
- Question 4: 1 point cas traité, 1 point résultat, 1 point justification, 1 point erreur fréquente évitée.
- Total : 16 points, conversion sur 20 après relecture pédagogique.

## Corrigé professeur
### Corrigé question 1
- Capacité évaluée : P-ALGO-02A.
- Donnée utilisée : liste initiale [5, 2, 4, 1].
- Réponse attendue : États: [5,2,4,1] ; insérer 2 -> [2,5,4,1] ; insérer 4 -> [2,4,5,1] ; insérer 1 -> [1,2,4,5].
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 2
- Capacité évaluée : P-ALGO-02B.
- Donnée utilisée : Dans le tri par insertion, après l’étape i, le préfixe de longueur i+1 est trié.
- Réponse attendue : Après insertion de 4, le préfixe [2,4,5] est trié. L’invariant est vrai pour i=2 ; le suffixe [1] n’est pas encore traité.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 3
- Capacité évaluée : P-ALGO-02C.
- Donnée utilisée : liste [3, 1, 4, 2].
- Réponse attendue : Pseudo-code: pour i, chercher j_min dans i..n-1 puis échanger. Pour i=0, minimum 1 à j=1, échange -> [1,3,4,2].
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 4
- Capacité évaluée : P-ALGO-02D.
- Donnée utilisée : tri par sélection sur n=5 éléments.
- Réponse attendue : Comparaisons: 4+3+2+1=10. Formule n(n-1)/2 = 5*4/2 = 10.
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
