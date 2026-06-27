---
title: "T07 - tp_papier - graphes, listes et matrices"
level: "terminale"
sequence_id: "T07"
document_type: "tp_papier"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "graphes, listes et matrices"
notion: "graphes, listes et matrices"
private_data: false
official_program:
  capacities:
    - "T-STRUCT-05A"
    - "T-STRUCT-05B"
    - "T-STRUCT-05C"
    - "T-STRUCT-05D"
---

# T07 - TP - graphes, listes et matrices

## Statut du TP
TP papier : ce support n attend aucune ressource Python ; le livrable est une trace écrite vérifiable.

## Donnée fournie
`arcs=[(A,B),(A,C),(B,D),(C,D),(D,B)]`

## Travail demandé
1. Préparer la donnée et nommer les champs utiles.
2. Réaliser : lister voisins sortants.
3. Réaliser : remplir matrice 0/1.
4. Tester le cas limite `sommet isolé E`.
5. Produire le livrable : A -> [B,C], B -> [D], C -> [D], D -> [B].

## Barème associé
- 2 points : donnée préparée.
- 3 points : méthode principale.
- 3 points : résultat `A -> [B,C], B -> [D], C -> [D], D -> [B]`.
- 2 points : cas limite `sommet isolé E`.

## Corrigé question par question
### Corrigé question 1
Résultat attendu : `arcs=[(A,B),(A,C),(B,D),(C,D),(D,B)]`.
### Corrigé question 2
Résultat attendu : A -> [B,C], B -> [D], C -> [D], D -> [B].
### Corrigé question 3
Résultat attendu : ligne A : colonnes B et C valent 1.
### Corrigé question 4
Résultat attendu : `sommet isolé E` traité sans ambiguïté.

## Liens
- TD lié : `T07_TD_graphes_modelisation_listes_matrices.md`.
- Évaluation liée : `T07_evaluation_graphes_modelisation_listes_matrices.md`.

## Cas limites travaillés
- sommet isolé E.
- boucle A->A.
- arête non orientée.

## Erreurs fréquentes
- voisin entrant confondu.
- sommet isolé oublié.
- coût mémoire ignoré.

## Critères de réussite observables
- La donnée de départ est recopiée exactement.
- La trace ou le pseudo-code conduit à `A -> [B,C], B -> [D], C -> [D], D -> [B]`.
- Au moins un cas limite de la section précédente est décidé.



## Protocole de validation complémentaire
1. Préparer un jeu nominal propre à T07 et noter la sortie attendue avant exécution.
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
