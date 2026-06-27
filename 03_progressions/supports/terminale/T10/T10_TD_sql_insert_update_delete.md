---
title: "T10 - TD - SQL INSERT UPDATE DELETE"
level: "terminale"
sequence_id: "T10"
document_type: "td"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Bases de données"
notion: "SQL INSERT UPDATE DELETE"
objectifs:
  - "travailler SQL INSERT UPDATE DELETE sur des données explicites"
  - "produire une réponse justifiée et contrôlée"
  - "identifier les cas limites"
  - "corriger les erreurs fréquentes du chapitre"
private_data: false
official_program:
  capacities:
    - "T-BDD-03F"
    - "T-BDD-03G"
    - "T-BDD-03H"
---

# T10 - TD - SQL INSERT UPDATE DELETE

## Objectifs
- Lire une donnée disciplinaire précise avant de répondre.
- Produire une méthode vérifiable et un résultat contrôlable.
- Traiter un cas limite sans le transformer en généralité.
- Relier chaque correction à une erreur fréquente observable.

## Capacités officielles
- T-BDD-03F
- T-BDD-03G
- T-BDD-03H

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T10/T10_fiche_cours_sql_insert_update_delete.md`.
- Séance liée : `T10-S1` dans la progression annuelle.
- Statut : support `needs_review`, non validé et non publiable.

## Situation de travail
Table Livre(id, titre, stock) initiale: (1,"Algo",2), (2,"Reseaux",0).

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée.
- Standard : exercices 3 à 6, production écrite et justification.
- Approfondissement : exercices 7 et 8, transfert ou comparaison.

## Exercices
### Exercice 1 - Lire une table avant modification
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-BDD-03F.
- Données : Livre: (1,"Algo",2), (2,"Reseaux",0).
- Consigne : Dire quel livre est indisponible.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 2 - Prévoir un INSERT
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-BDD-03G.
- Données : INSERT INTO Livre(id,titre,stock) VALUES (3,"SQL",5);
- Consigne : Donner la table après.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 3 - Écrire un UPDATE ciblé
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-BDD-03H.
- Données : On emprunte Algo id=1, stock passe de 2 à 1.
- Consigne : Écrire la requête.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 4 - Écrire un DELETE ciblé
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-BDD-03F.
- Données : Supprimer le livre id=2 uniquement.
- Consigne : Écrire la requête et vérification.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 5 - Identifier UPDATE sans WHERE
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : T-BDD-03G.
- Données : UPDATE Livre SET stock=0;
- Consigne : Dire l’effet.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 6 - Justifier une vérification par SELECT
- Type : justification.
- Niveau : standard.
- Capacité officielle : T-BDD-03H.
- Données : Après UPDATE id=1.
- Consigne : Donner le SELECT utile.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 7 - Détecter violation de clé
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : T-BDD-03F.
- Données : INSERT id=1 alors que id=1 existe déjà.
- Consigne : Prévoir le résultat.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 8 - Transaction courte
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : T-BDD-03G.
- Données : Emprunt: diminuer stock puis créer ligne Emprunt.
- Consigne : Écrire les étapes.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : T-BDD-03F.
- Donnée utilisée : Livre: (1,"Algo",2), (2,"Reseaux",0).
- Résultat attendu : Le livre id=2, titre Reseaux, a stock=0 : il est indisponible.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 2
- Capacité mobilisée : T-BDD-03G.
- Donnée utilisée : INSERT INTO Livre(id,titre,stock) VALUES (3,"SQL",5);
- Résultat attendu : Nouvelle ligne ajoutée: (3,"SQL",5). La table contient maintenant ids 1,2,3.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 3
- Capacité mobilisée : T-BDD-03H.
- Donnée utilisée : On emprunte Algo id=1, stock passe de 2 à 1.
- Résultat attendu : UPDATE Livre SET stock = stock - 1 WHERE id = 1; Après exécution, Algo a stock=1.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 4
- Capacité mobilisée : T-BDD-03F.
- Donnée utilisée : Supprimer le livre id=2 uniquement.
- Résultat attendu : DELETE FROM Livre WHERE id = 2; Vérification: SELECT * FROM Livre WHERE id=2; renvoie 0 ligne.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 5
- Capacité mobilisée : T-BDD-03G.
- Donnée utilisée : UPDATE Livre SET stock=0;
- Résultat attendu : Toutes les lignes passent à stock=0. C’est dangereux car Algo, Reseaux et SQL deviennent indisponibles.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 6
- Capacité mobilisée : T-BDD-03H.
- Donnée utilisée : Après UPDATE id=1.
- Résultat attendu : SELECT id,titre,stock FROM Livre WHERE id=1; doit renvoyer (1,"Algo",1). Cette requête vérifie la ligne modifiée seulement.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 7
- Capacité mobilisée : T-BDD-03F.
- Donnée utilisée : INSERT id=1 alors que id=1 existe déjà.
- Résultat attendu : La clé primaire id interdit deux lignes id=1. Le SGBD refuse l’insertion avec une erreur de contrainte.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 8
- Capacité mobilisée : T-BDD-03G.
- Donnée utilisée : Emprunt: diminuer stock puis créer ligne Emprunt.
- Résultat attendu : BEGIN; UPDATE Livre SET stock=stock-1 WHERE id=1 AND stock>0; INSERT INTO Emprunt(id_livre) VALUES(1); COMMIT; si stock=0, ROLLBACK.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.

## Erreurs fréquentes
- EF1 : répondre par un mot-clé sans citer la donnée ; remédiation : entourer les valeurs utiles avant de rédiger.
- EF2 : donner un résultat sans méthode ; remédiation : imposer une ligne méthode puis une ligne résultat.
- EF3 : oublier le cas limite ; remédiation : refaire l’exercice 5 avec la donnée minimale.
- EF4 : confondre justification et paraphrase ; remédiation : écrire une phrase qui relie donnée, règle et conclusion.

## Remédiation ciblée
- Reprendre deux exercices en ne gardant que les données numériques ou symboliques.
- Faire corriger une réponse incomplète par un binôme avec une grille donnée/méthode/résultat/contrôle.
- Produire une variante courte avec une donnée changée et vérifier que la méthode reste valable.

## Différenciation
- Socle : fournir les données annotées et demander seulement le résultat contrôlé.
- Standard : demander méthode complète, résultat et contrôle écrit.
- Approfondissement : demander une variante de la donnée et une comparaison de deux démarches.

## Lien avec la progression
| Élément | Référence | Statut |
|---|---|---|
| Fiche | T10_fiche_cours_sql_insert_update_delete.md | needs_review |
| Séance | T10-S1 | progression existante |
| Évaluation | T10_evaluation_sql_insert_update_delete.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans le dossier Documents_DRIVE avant création.
- Aucun fichier Drive n’a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
