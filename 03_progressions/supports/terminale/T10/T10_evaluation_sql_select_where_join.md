---
title: "T10 - Évaluation - SQL SELECT WHERE JOIN"
level: "terminale"
sequence_id: "T10"
document_type: "evaluation"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Bases de données"
notion: "SQL SELECT WHERE JOIN"
objectifs:
  - "évaluer la compréhension de la fiche"
  - "vérifier la capacité à produire une réponse justifiée"
  - "identifier les erreurs fréquentes"
  - "préparer une remédiation ciblée"
private_data: false
official_program:
  capacities:
    - "T-BDD-03A"
    - "T-BDD-03B"
    - "T-BDD-03C"
    - "T-BDD-03D"
    - "T-BDD-03E"
---
# T10 - Évaluation - SQL SELECT WHERE JOIN

## Durée et matériel autorisé
- Durée : 25 minutes.
- Matériel autorisé : fiche de cours personnelle, sans accès réseau ni correction.
- Statut : évaluation créée en `needs_review`, non publiée et non validée.

## Capacités évaluées
- T-BDD-03A
- T-BDD-03B
- T-BDD-03C
- T-BDD-03D
- T-BDD-03E

## Fiche liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T10/T10_fiche_cours_sql_select_where_join.md`.
- Séance liée : `T10-S1`.
- TD lié : `T10_TD_sql_select_where_join.md`.

## Consignes
Répondre directement sur copie. Chaque réponse doit citer la donnée utilisée, la méthode et un contrôle rapide.

## Questions
### Question 1 - Lire les colonnes utiles dans un select simple
- Capacité : T-BDD-03A.
- Données : Eleve : (1,"E1","T1"), (2,"E2","T2"), (3,"E3","T1"). Note : (10,1,"NSI",15), (11,1,"Maths",13), (12,2,"NSI",9), (13,3,"NSI",18).
- Consigne : répondre à la tâche « lire les colonnes utiles dans un SELECT simple » avec méthode, résultat et contrôle.
- Format attendu : réponse courte mais justifiée, avec notation ou pseudo-code si nécessaire.
### Question 2 - Écrire un where qui filtre les élèves de t1
- Capacité : T-BDD-03B.
- Données : Eleve : (1,"E1","T1"), (2,"E2","T2"), (3,"E3","T1"). Note : (10,1,"NSI",15), (11,1,"Maths",13), (12,2,"NSI",9), (13,3,"NSI",18).
- Consigne : répondre à la tâche « écrire un WHERE qui filtre les élèves de T1 » avec méthode, résultat et contrôle.
- Format attendu : réponse courte mais justifiée, avec notation ou pseudo-code si nécessaire.
### Question 3 - Produire une jointure eleve-note avec condition on
- Capacité : T-BDD-03C.
- Données : Eleve : (1,"E1","T1"), (2,"E2","T2"), (3,"E3","T1"). Note : (10,1,"NSI",15), (11,1,"Maths",13), (12,2,"NSI",9), (13,3,"NSI",18).
- Consigne : répondre à la tâche « produire une jointure Eleve-Note avec condition ON » avec méthode, résultat et contrôle.
- Format attendu : réponse courte mais justifiée, avec notation ou pseudo-code si nécessaire.
### Question 4 - Écrire une requête triée par note décroissante
- Capacité : T-BDD-03D.
- Données : Eleve : (1,"E1","T1"), (2,"E2","T2"), (3,"E3","T1"). Note : (10,1,"NSI",15), (11,1,"Maths",13), (12,2,"NSI",9), (13,3,"NSI",18).
- Consigne : répondre à la tâche « écrire une requête triée par note décroissante » avec méthode, résultat et contrôle.
- Format attendu : réponse courte mais justifiée, avec notation ou pseudo-code si nécessaire.

## Barème
- Question 1: 2 points méthode, 1 point résultat, 1 point contrôle ou justification.
- Question 2: 2 points méthode, 1 point résultat, 1 point contrôle ou justification.
- Question 3: 2 points méthode, 1 point résultat, 1 point contrôle ou justification.
- Question 4: 2 points méthode, 1 point résultat, 1 point contrôle ou justification.
- Total : 16 points convertibles sur 20 après relecture pédagogique.

## Corrigé professeur
### Corrigé question 1
- Capacité évaluée : T-BDD-03A.
- Réponse attendue : la solution explicite « lire les colonnes utiles dans un SELECT simple » à partir des données fournies.
- Justification : les étapes doivent permettre de retrouver le résultat sans deviner.
- Point de vigilance : une conclusion isolée sans contrôle perd les points de méthode.
### Corrigé question 2
- Capacité évaluée : T-BDD-03B.
- Réponse attendue : la solution explicite « écrire un WHERE qui filtre les élèves de T1 » à partir des données fournies.
- Justification : les étapes doivent permettre de retrouver le résultat sans deviner.
- Point de vigilance : une conclusion isolée sans contrôle perd les points de méthode.
### Corrigé question 3
- Capacité évaluée : T-BDD-03C.
- Réponse attendue : la solution explicite « produire une jointure Eleve-Note avec condition ON » à partir des données fournies.
- Justification : les étapes doivent permettre de retrouver le résultat sans deviner.
- Point de vigilance : une conclusion isolée sans contrôle perd les points de méthode.
### Corrigé question 4
- Capacité évaluée : T-BDD-03D.
- Réponse attendue : la solution explicite « écrire une requête triée par note décroissante » à partir des données fournies.
- Justification : les étapes doivent permettre de retrouver le résultat sans deviner.
- Point de vigilance : une conclusion isolée sans contrôle perd les points de méthode.

## Critères de réussite
- Les capacités officielles sont reliées à une action observable.
- La réponse ne se limite pas à un mot-clé de la fiche.
- Le cas limite ou le contrôle demandé apparaît explicitement.
- Le vocabulaire disciplinaire est utilisé dans le contexte de la donnée.

## Version aménagée et indications d’aménagement
- Version aménagée : conserver les mêmes questions mais fournir la donnée surlignée et un espace « méthode / résultat / contrôle ».
- Aménagement temps : ajouter 10 minutes si l'élève doit recopier la donnée.
- Aide autorisée : liste des verbes d'action, sans résultat numérique ni requête complète.

## Erreurs fréquentes et remédiation
- EF1 : réponse sans donnée citée ; remédiation : refaire la question 1 avec les valeurs encadrées.
- EF2 : méthode correcte mais résultat non contrôlé ; remédiation : ajouter une ligne de vérification.
- EF3 : confusion entre vocabulaire et preuve ; remédiation : demander une phrase « parce que ».
- EF4 : oubli du cas limite ; remédiation : reprendre le TD associé, exercice 5.

## Source et traçabilité
- Recherche locale effectuée dans `/home/alaeddine/Documents/NSI/Documents_DRIVE` avant création.
- Aucun fichier Drive n'a été repris directement dans cette évaluation.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
