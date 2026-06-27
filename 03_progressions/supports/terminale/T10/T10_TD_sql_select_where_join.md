---
title: "T10 - TD - SQL SELECT WHERE JOIN"
level: "terminale"
sequence_id: "T10"
document_type: "td"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Bases de données"
notion: "SQL SELECT WHERE JOIN"
objectifs:
  - "travailler SQL SELECT WHERE JOIN sur des données explicites"
  - "produire une réponse justifiée et contrôlée"
  - "identifier les cas limites"
  - "corriger les erreurs fréquentes du chapitre"
private_data: false
official_program:
  capacities:
    - "T-BDD-03A"
    - "T-BDD-03B"
    - "T-BDD-03C"
    - "T-BDD-03D"
    - "T-BDD-03E"
---

# T10 - TD - SQL SELECT WHERE JOIN

## Objectifs
- Lire une donnée disciplinaire précise avant de répondre.
- Produire une méthode vérifiable et un résultat contrôlable.
- Traiter un cas limite sans le transformer en généralité.
- Relier chaque correction à une erreur fréquente observable.

## Capacités officielles
- T-BDD-03A
- T-BDD-03B
- T-BDD-03C
- T-BDD-03D
- T-BDD-03E

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T10/T10_fiche_cours_sql_select_where_join.md`.
- Séance liée : `T10-S1` dans la progression annuelle.
- Statut : support `needs_review`, non validé et non publiable.

## Situation de travail
Base minimale: Eleve(id_eleve, nom, classe) et Note(id_note, id_eleve, matiere, note).

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée.
- Standard : exercices 3 à 6, production écrite et justification.
- Approfondissement : exercices 7 et 8, transfert ou comparaison.

## Exercices
### Exercice 1 - Lire un schéma relationnel
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-BDD-03A.
- Données : Eleve(1,"Ada","T1"), Eleve(2,"Linus","T2") ; Note(10,1,"NSI",16), Note(11,2,"NSI",12).
- Consigne : Identifier clé primaire et clé étrangère.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 2 - Prévoir le résultat d’un SELECT
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-BDD-03B.
- Données : Table Eleve avec lignes (1,Ada,T1), (2,Linus,T2), (3,Grace,T1). Requête SELECT nom FROM Eleve WHERE classe="T1" ORDER BY nom;
- Consigne : Donner la sortie.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 3 - Écrire une requête WHERE
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-BDD-03C.
- Données : Table Note, chercher notes de NSI supérieures ou égales à 15.
- Consigne : Écrire la requête SQL.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 4 - Écrire une jointure
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-BDD-03D.
- Données : Afficher nom et note en NSI.
- Consigne : Écrire la requête avec condition de jointure.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 5 - Repérer une jointure sans condition
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : T-BDD-03E.
- Données : SELECT nom, note FROM Eleve, Note; avec 3 élèves et 2 notes.
- Consigne : Dire le nombre de lignes et l’erreur.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 6 - Justifier ORDER BY
- Type : justification.
- Niveau : standard.
- Capacité officielle : T-BDD-03A.
- Données : Notes NSI: Ada 16, Linus 12, Grace 18.
- Consigne : Écrire et justifier le tri décroissant.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 7 - Filtrer avant/après jointure
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : T-BDD-03B.
- Données : Comparer WHERE matiere="NSI" avant ou après join logique.
- Consigne : Expliquer l’effet.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 8 - Combiner agrégat simple
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : T-BDD-03C.
- Données : Notes NSI 16,12,18.
- Consigne : Écrire la moyenne NSI.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : T-BDD-03A.
- Donnée utilisée : Eleve(1,"Ada","T1"), Eleve(2,"Linus","T2") ; Note(10,1,"NSI",16), Note(11,2,"NSI",12).
- Résultat attendu : Eleve.id_eleve est clé primaire ; Note.id_note est clé primaire ; Note.id_eleve référence Eleve.id_eleve.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 2
- Capacité mobilisée : T-BDD-03B.
- Donnée utilisée : Table Eleve avec lignes (1,Ada,T1), (2,Linus,T2), (3,Grace,T1). Requête SELECT nom FROM Eleve WHERE classe="T1" ORDER BY nom;
- Résultat attendu : Résultat: Ada puis Grace, une colonne nom, car seuls les élèves de T1 sont gardés et triés alphabétiquement.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 3
- Capacité mobilisée : T-BDD-03C.
- Donnée utilisée : Table Note, chercher notes de NSI supérieures ou égales à 15.
- Résultat attendu : SELECT id_eleve, note FROM Note WHERE matiere = "NSI" AND note >= 15; Résultat sur les données: (1,16).
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 4
- Capacité mobilisée : T-BDD-03D.
- Donnée utilisée : Afficher nom et note en NSI.
- Résultat attendu : SELECT Eleve.nom, Note.note FROM Eleve JOIN Note ON Eleve.id_eleve = Note.id_eleve WHERE Note.matiere = "NSI"; Résultat: (Ada,16), (Linus,12).
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 5
- Capacité mobilisée : T-BDD-03E.
- Donnée utilisée : SELECT nom, note FROM Eleve, Note; avec 3 élèves et 2 notes.
- Résultat attendu : Sans condition, produit cartésien: 3*2=6 lignes. Erreur: notes associées à tous les élèves au lieu de leur id_eleve.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 6
- Capacité mobilisée : T-BDD-03A.
- Donnée utilisée : Notes NSI: Ada 16, Linus 12, Grace 18.
- Résultat attendu : SELECT nom, note FROM ... ORDER BY note DESC; produit Grace 18, Ada 16, Linus 12. DESC place les plus grandes notes en premier.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 7
- Capacité mobilisée : T-BDD-03B.
- Donnée utilisée : Comparer WHERE matiere="NSI" avant ou après join logique.
- Résultat attendu : Le résultat relationnel final est identique si la condition porte seulement sur Note. Filtrer Note avant peut réduire les lignes intermédiaires.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 8
- Capacité mobilisée : T-BDD-03C.
- Donnée utilisée : Notes NSI 16,12,18.
- Résultat attendu : SELECT AVG(note) FROM Note WHERE matiere="NSI"; résultat (15.333...). On peut arrondir dans l’affichage, pas dans le calcul.
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
| Fiche | T10_fiche_cours_sql_select_where_join.md | needs_review |
| Séance | T10-S1 | progression existante |
| Évaluation | T10_evaluation_sql_select_where_join.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans le dossier Documents_DRIVE avant création.
- Aucun fichier Drive n’a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
