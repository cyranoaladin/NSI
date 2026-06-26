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
- Matériel autorisé : fiche personnelle, sans accès réseau ni corrigé.
- Statut : évaluation `needs_review`, non validée et non publiable.

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
Répondre directement sur copie. Chaque réponse doit montrer la donnée utilisée, la méthode et un contrôle rapide.

## Questions
### Question 1 - Lire un schéma relationnel
- Capacité : T-BDD-03A.
- Données : Eleve(1,"Ada","T1"), Eleve(2,"Linus","T2") ; Note(10,1,"NSI",16), Note(11,2,"NSI",12).
- Consigne : Identifier clé primaire et clé étrangère.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 2 - Prévoir le résultat d’un SELECT
- Capacité : T-BDD-03B.
- Données : Table Eleve avec lignes (1,Ada,T1), (2,Linus,T2), (3,Grace,T1). Requête SELECT nom FROM Eleve WHERE classe="T1" ORDER BY nom;
- Consigne : Donner la sortie.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 3 - Écrire une requête WHERE
- Capacité : T-BDD-03C.
- Données : Table Note, chercher notes de NSI supérieures ou égales à 15.
- Consigne : Écrire la requête SQL.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 4 - Écrire une jointure
- Capacité : T-BDD-03D.
- Données : Afficher nom et note en NSI.
- Consigne : Écrire la requête avec condition de jointure.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.

## Barème
- Question 1: 1 point identification de la donnée, 1 point méthode, 1 point résultat exact, 1 point contrôle.
- Question 2: 1 point vocabulaire précis, 1 point méthode, 1 point résultat, 1 point justification.
- Question 3: 1 point modélisation, 1 point production correcte, 1 point test du résultat, 1 point lisibilité.
- Question 4: 1 point cas traité, 1 point résultat, 1 point justification, 1 point erreur fréquente évitée.
- Total : 16 points, conversion sur 20 après relecture pédagogique.

## Corrigé professeur
### Corrigé question 1
- Capacité évaluée : T-BDD-03A.
- Donnée utilisée : Eleve(1,"Ada","T1"), Eleve(2,"Linus","T2") ; Note(10,1,"NSI",16), Note(11,2,"NSI",12).
- Réponse attendue : Eleve.id_eleve est clé primaire ; Note.id_note est clé primaire ; Note.id_eleve référence Eleve.id_eleve.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 2
- Capacité évaluée : T-BDD-03B.
- Donnée utilisée : Table Eleve avec lignes (1,Ada,T1), (2,Linus,T2), (3,Grace,T1). Requête SELECT nom FROM Eleve WHERE classe="T1" ORDER BY nom;
- Réponse attendue : Résultat: Ada puis Grace, une colonne nom, car seuls les élèves de T1 sont gardés et triés alphabétiquement.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 3
- Capacité évaluée : T-BDD-03C.
- Donnée utilisée : Table Note, chercher notes de NSI supérieures ou égales à 15.
- Réponse attendue : SELECT id_eleve, note FROM Note WHERE matiere = "NSI" AND note >= 15; Résultat sur les données: (1,16).
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 4
- Capacité évaluée : T-BDD-03D.
- Donnée utilisée : Afficher nom et note en NSI.
- Réponse attendue : SELECT Eleve.nom, Note.note FROM Eleve JOIN Note ON Eleve.id_eleve = Note.id_eleve WHERE Note.matiere = "NSI"; Résultat: (Ada,16), (Linus,12).
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
