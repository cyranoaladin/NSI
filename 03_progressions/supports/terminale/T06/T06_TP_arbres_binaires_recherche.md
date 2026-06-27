---
title: "T06 - tp_papier - arbres binaires de recherche"
level: "terminale"
sequence_id: "T06"
document_type: "tp_papier"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "arbres binaires de recherche"
notion: "arbres binaires de recherche"
private_data: false
official_program:
  capacities:
    - "T-ALGO-01E"
    - "T-ALGO-01F"
---

# T06 - TP - arbres binaires de recherche

## Statut du TP
TP papier : ce support n attend aucune ressource Python ; le livrable est une trace écrite vérifiable.

## Donnée fournie
`ABR racine=8, gauche=3 avec 1 et 6, droite=10 avec 14`

## Travail demandé
1. Préparer la donnée et nommer les champs utiles.
2. Réaliser : comparer à la racine.
3. Réaliser : descendre gauche ou droite.
4. Tester le cas limite `arbre vide`.
5. Produire le livrable : chercher 6 : 8 -> 3 -> 6.

## Barème associé
- 2 points : donnée préparée.
- 3 points : méthode principale.
- 3 points : résultat `chercher 6 : 8 -> 3 -> 6`.
- 2 points : cas limite `arbre vide`.

## Corrigé question par question
### Corrigé question 1
Résultat attendu : `ABR racine=8, gauche=3 avec 1 et 6, droite=10 avec 14`.
### Corrigé question 2
Résultat attendu : chercher 6 : 8 -> 3 -> 6.
### Corrigé question 3
Résultat attendu : insérer 7 : 8 -> 3 -> 6 -> droite.
### Corrigé question 4
Résultat attendu : `arbre vide` traité sans ambiguïté.

## Liens
- TD lié : `T06_TD_arbres_binaires_recherche.md`.
- Évaluation liée : `T06_evaluation_arbres_binaires_recherche.md`.

## Cas limites travaillés
- arbre vide.
- doublon 6.
- arbre dégénéré.

## Erreurs fréquentes
- gauche et droite inversées.
- logarithmique sans équilibre.
- racine vide oubliée.

## Critères de réussite observables
- La donnée de départ est recopiée exactement.
- La trace ou le pseudo-code conduit à `chercher 6 : 8 -> 3 -> 6`.
- Au moins un cas limite de la section précédente est décidé.



## Protocole de validation complémentaire
1. Préparer un jeu nominal propre à T06 et noter la sortie attendue avant exécution.
2. Préparer un cas limite distinct et expliquer pourquoi il doit être accepté ou refusé.
3. Exécuter le starter : il doit échouer sur au moins un test complet, ce qui confirme que le travail élève reste à produire.
4. Exécuter le corrigé professeur : il doit produire exactement les valeurs attendues dans les tests.
5. Comparer la trace obtenue avec la consigne : chaque étape doit être justifiée par une donnée du sujet.
6. Noter l'erreur fréquente observée et choisir la remédiation ciblée dans le support associé.

## Livrable vérifiable complémentaire
- Fichier élève complété avec les fonctions demandées dans le TP.
- Trace courte indiquant entrée, traitement, sortie et cas limite.
- Capture textuelle des tests attendus : nominal OK, cas limite OK, entrée invalide traitée.
- Commentaire final indiquant la capacité officielle réellement travaillée.
