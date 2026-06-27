---
title: "P14 - TD - synthese projet oral"
level: "premiere"
sequence_id: "P14"
document_type: "td"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Synthèse et projet"
notion: "synthese projet oral"
objectifs:
  - "travailler synthese projet oral sur des données explicites"
  - "produire une réponse justifiée et contrôlée"
  - "identifier les cas limites"
  - "corriger les erreurs fréquentes du chapitre"
private_data: false
official_program:
  capacities:
    - "P-HIST-01"
---

# P14 - TD - synthèse projet oral

## Objectifs
- Lire une donnée disciplinaire précise avant de répondre.
- Produire une méthode vérifiable et un résultat contrôlable.
- Traiter un cas limite sans le transformer en généralité.
- Relier chaque correction à une erreur fréquente observable.

## Capacités officielles
- P-HIST-01

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/premiere/P14/P14_fiche_cours_synthese_projet_oral.md`.
- Séance liée : `P14-S1` dans la progression annuelle.
- Statut : support `needs_review`, non validé et non publiable.

## Situation de travail
Un groupe prépare une démonstration de mini-projet NSI avec code, tests et justification orale.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée.
- Standard : exercices 3 à 6, production écrite et justification.
- Approfondissement : exercices 7 et 8, transfert ou comparaison.

## Exercices
### Exercice 1 - Lire un cahier des charges
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : P-HIST-01.
- Données : Projet: carnet de scores, données stockées en CSV, recherche par joueur, tri par score.
- Consigne : Identifier deux fonctionnalités et deux contraintes.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 2 - Analyser un extrait de test
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : P-HIST-01.
- Données : assert meilleur_score([12,9,15]) == 15 ; assert meilleur_score([]) is None.
- Consigne : Dire les cas couverts.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 3 - Rédiger une spécification de fonction
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : P-HIST-01.
- Données : fonction moyenne_scores(scores).
- Consigne : Écrire entrée, sortie, cas limite.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 4 - Construire un plan d’oral
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : P-HIST-01.
- Données : Sujet: expliquer un tri utilisé dans le projet.
- Consigne : Donner un plan en trois parties.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 5 - Identifier un risque de démonstration
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : P-HIST-01.
- Données : Le projet lit scores.csv, mais le fichier peut être absent.
- Consigne : Prévoir le comportement.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 6 - Justifier une décision technique
- Type : justification.
- Niveau : standard.
- Capacité officielle : P-HIST-01.
- Données : Choix: dictionnaire joueur -> liste de scores.
- Consigne : Justifier.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 7 - Évaluer une grille de projet
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : P-HIST-01.
- Données : Critères: exactitude, tests, lisibilité, oral. Scores 3/4, 2/4, 3/4, 1/4.
- Consigne : Identifier priorité de remédiation.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 8 - Écrire une conclusion d’oral
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : P-HIST-01.
- Données : Projet carnet de scores.
- Consigne : Rédiger une conclusion qui cite résultat et limite.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : P-HIST-01.
- Donnée utilisée : Projet: carnet de scores, données stockées en CSV, recherche par joueur, tri par score.
- Résultat attendu : Fonctionnalités: ajouter un score, rechercher un joueur, trier par score. Contraintes: format CSV cohérent et tests sur recherche/tri.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 2
- Capacité mobilisée : P-HIST-01.
- Donnée utilisée : assert meilleur_score([12,9,15]) == 15 ; assert meilleur_score([]) is None.
- Résultat attendu : Premier test couvre cas nominal avec maximum 15 ; second test couvre cas limite liste vide, contrat None.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 3
- Capacité mobilisée : P-HIST-01.
- Donnée utilisée : fonction moyenne_scores(scores).
- Résultat attendu : Entrée: liste de nombres. Sortie: moyenne flottante. Cas limite: liste vide -> None ou ValueError ; choix à fixer dans la spécification.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 4
- Capacité mobilisée : P-HIST-01.
- Donnée utilisée : Sujet: expliquer un tri utilisé dans le projet.
- Résultat attendu : Plan: 1 contexte du besoin ; 2 principe du tri avec exemple [3,1,2] -> [1,2,3] ; 3 limites et complexité O(n^2) ou O(n log n) selon algorithme.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 5
- Capacité mobilisée : P-HIST-01.
- Donnée utilisée : Le projet lit scores.csv, mais le fichier peut être absent.
- Résultat attendu : La démonstration doit tester l’existence du fichier, afficher un message clair ou créer un fichier vide. Elle ne doit pas échouer avec une trace non expliquée.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 6
- Capacité mobilisée : P-HIST-01.
- Donnée utilisée : Choix: dictionnaire joueur -> liste de scores.
- Résultat attendu : Le dictionnaire donne accès direct par nom de joueur ; la liste conserve plusieurs scores. Exemple: scores["A"]=[12,15], meilleur=15.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 7
- Capacité mobilisée : P-HIST-01.
- Donnée utilisée : Critères: exactitude, tests, lisibilité, oral. Scores 3/4, 2/4, 3/4, 1/4.
- Résultat attendu : Oral est prioritaire avec 1/4, puis tests 2/4. L’action suivante: préparer une démonstration guidée et ajouter deux tests limites.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 8
- Capacité mobilisée : P-HIST-01.
- Donnée utilisée : Projet carnet de scores.
- Résultat attendu : Conclusion attendue: le programme ajoute, recherche et trie les scores ; les tests couvrent liste vide et doublons ; limite restante: pas d’interface graphique ni gestion multi-utilisateur.
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
| Fiche | P14_fiche_cours_synthese_projet_oral.md | needs_review |
| Séance | P14-S1 | progression existante |
| Évaluation | P14_evaluation_synthese_projet_oral.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans le dossier Documents_DRIVE avant création.
- Aucun fichier Drive n’a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
