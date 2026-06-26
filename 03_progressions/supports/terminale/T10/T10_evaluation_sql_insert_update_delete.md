---
title: "T10 - Évaluation - SQL INSERT UPDATE DELETE"
level: "terminale"
sequence_id: "T10"
document_type: "evaluation"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Bases de données"
notion: "SQL INSERT UPDATE DELETE"
objectifs:
  - "évaluer la compréhension de la fiche"
  - "vérifier la capacité à produire une réponse justifiée"
  - "identifier les erreurs fréquentes"
  - "préparer une remédiation ciblée"
private_data: false
official_program:
  capacities:
    - "T-BDD-03F"
    - "T-BDD-03G"
    - "T-BDD-03H"
---

# T10 - Évaluation - SQL INSERT UPDATE DELETE

## Durée et matériel autorisé
- Durée : 25 minutes.
- Matériel autorisé : fiche personnelle, sans accès réseau ni corrigé.
- Statut : évaluation `needs_review`, non validée et non publiable.

## Capacités évaluées
- T-BDD-03F
- T-BDD-03G
- T-BDD-03H

## Fiche liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T10/T10_fiche_cours_sql_insert_update_delete.md`.
- Séance liée : `T10-S1`.
- TD lié : `T10_TD_sql_insert_update_delete.md`.

## Consignes
Répondre directement sur copie. Chaque réponse doit montrer la donnée utilisée, la méthode et un contrôle rapide.

## Questions
### Question 1 - Lire une table avant modification
- Capacité : T-BDD-03F.
- Données : Livre: (1,"Algo",2), (2,"Reseaux",0).
- Consigne : Dire quel livre est indisponible.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 2 - Prévoir un INSERT
- Capacité : T-BDD-03G.
- Données : INSERT INTO Livre(id,titre,stock) VALUES (3,"SQL",5);
- Consigne : Donner la table après.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 3 - Écrire un UPDATE ciblé
- Capacité : T-BDD-03H.
- Données : On emprunte Algo id=1, stock passe de 2 à 1.
- Consigne : Écrire la requête.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 4 - Écrire un DELETE ciblé
- Capacité : T-BDD-03F.
- Données : Supprimer le livre id=2 uniquement.
- Consigne : Écrire la requête et vérification.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.

## Barème
- Question 1: 1 point identification de la donnée, 1 point méthode, 1 point résultat exact, 1 point contrôle.
- Question 2: 1 point vocabulaire précis, 1 point méthode, 1 point résultat, 1 point justification.
- Question 3: 1 point modélisation, 1 point production correcte, 1 point test du résultat, 1 point lisibilité.
- Question 4: 1 point cas traité, 1 point résultat, 1 point justification, 1 point erreur fréquente évitée.
- Total : 16 points, conversion sur 20 après relecture pédagogique.

## Corrigé professeur
### Corrigé question 1
- Capacité évaluée : T-BDD-03F.
- Donnée utilisée : Livre: (1,"Algo",2), (2,"Reseaux",0).
- Réponse attendue : Le livre id=2, titre Reseaux, a stock=0 : il est indisponible.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 2
- Capacité évaluée : T-BDD-03G.
- Donnée utilisée : INSERT INTO Livre(id,titre,stock) VALUES (3,"SQL",5);
- Réponse attendue : Nouvelle ligne ajoutée: (3,"SQL",5). La table contient maintenant ids 1,2,3.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 3
- Capacité évaluée : T-BDD-03H.
- Donnée utilisée : On emprunte Algo id=1, stock passe de 2 à 1.
- Réponse attendue : UPDATE Livre SET stock = stock - 1 WHERE id = 1; Après exécution, Algo a stock=1.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 4
- Capacité évaluée : T-BDD-03F.
- Donnée utilisée : Supprimer le livre id=2 uniquement.
- Réponse attendue : DELETE FROM Livre WHERE id = 2; Vérification: SELECT * FROM Livre WHERE id=2; renvoie 0 ligne.
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
