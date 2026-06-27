---
title: "T15 - TD - calculabilité arrêt"
level: "terminale"
sequence_id: "T15"
document_type: "td"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Langages et calculabilité"
notion: "calculabilité arrêt"
objectifs:
  - "travailler calculabilité arrêt sur des données explicites"
  - "produire une réponse justifiée et contrôlée"
  - "identifier les cas limites"
  - "corriger les erreurs fréquentes du chapitre"
private_data: false
official_program:
  capacities:
    - "T-LANG-01A"
    - "T-LANG-01B"
    - "T-LANG-01C"
---

# T15 - TD - calculabilité arrêt

## Objectifs
- Lire une donnée disciplinaire précise avant de répondre.
- Produire une méthode vérifiable et un résultat contrôlable.
- Traiter un cas limite sans le transformer en généralité.
- Relier chaque correction à une erreur fréquente observable.

## Capacités officielles
- T-LANG-01A
- T-LANG-01B
- T-LANG-01C

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T15/T15_fiche_cours_calculabilite_arret.md`.
- Séance liée : `T15-S1` dans la progression annuelle.
- Statut : support `needs_review`, non validé et non publiable.

## Situation de travail
On classe des programmes selon terminaison observable et limites théoriques.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée.
- Standard : exercices 3 à 6, production écrite et justification.
- Approfondissement : exercices 7 et 8, transfert ou comparaison.

## Exercices
### Exercice 1 - Tracer une boucle terminante
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-LANG-01A.
- Données : n=3 ; while n>0: n=n-1.
- Consigne : Donner la trace.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 2 - Repérer une boucle infinie
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-LANG-01B.
- Données : while True: pass.
- Consigne : Dire ce qui manque pour terminer.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 3 - Écrire un variant
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-LANG-01C.
- Données : while n>0: n=n//2 pour n=10.
- Consigne : Donner variant et trace.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 4 - Construire un semi-décideur
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-LANG-01A.
- Données : Chercher si une valeur apparaît dans un flux infini.
- Consigne : Expliquer.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 5 - Entrée déjà au cas d’arrêt
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : T-LANG-01B.
- Données : n=0 pour while n>0.
- Consigne : Donner comportement.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 6 - Expliquer l’indécidabilité de l’arrêt
- Type : justification.
- Niveau : standard.
- Capacité officielle : T-LANG-01C.
- Données : Supposer un programme HALT(P,x).
- Consigne : Donner l’idée de contradiction.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 7 - Distinguer bug et limite théorique
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : T-LANG-01A.
- Données : Un test timeout après 2 secondes.
- Consigne : Peut-on conclure non-terminaison ?
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 8 - Classer trois programmes
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : T-LANG-01B.
- Données : A termine toujours, B boucle toujours, C dépend d’une conjecture.
- Consigne : Donner statut.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : T-LANG-01A.
- Donnée utilisée : n=3 ; while n>0: n=n-1.
- Résultat attendu : Trace n: 3 -> 2 -> 1 -> 0, puis condition n>0 fausse. Le programme termine.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 2
- Capacité mobilisée : T-LANG-01B.
- Donnée utilisée : while True: pass.
- Résultat attendu : Aucune variable ne rapproche d’un cas d’arrêt et la condition reste True. La boucle ne termine pas.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 3
- Capacité mobilisée : T-LANG-01C.
- Donnée utilisée : while n>0: n=n//2 pour n=10.
- Résultat attendu : Variant n entier naturel diminue: 10 -> 5 -> 2 -> 1 -> 0. Il assure la terminaison.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 4
- Capacité mobilisée : T-LANG-01A.
- Donnée utilisée : Chercher si une valeur apparaît dans un flux infini.
- Résultat attendu : On lit les valeurs une à une ; si cible trouvée, on répond oui. Si elle n’apparaît jamais, l’algorithme peut tourner sans répondre.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 5
- Capacité mobilisée : T-LANG-01B.
- Donnée utilisée : n=0 pour while n>0.
- Résultat attendu : La condition est fausse au départ ; zéro itération ; terminaison immédiate.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 6
- Capacité mobilisée : T-LANG-01C.
- Donnée utilisée : Supposer un programme HALT(P,x).
- Résultat attendu : Construire D(P): si HALT(P,P) répond oui alors boucler, sinon terminer. Exécuter D(D) contredit la réponse de HALT.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 7
- Capacité mobilisée : T-LANG-01A.
- Donnée utilisée : Un test timeout après 2 secondes.
- Résultat attendu : Non. Le programme peut terminer après 3 secondes. Le timeout est une observation pratique, pas une preuve générale.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 8
- Capacité mobilisée : T-LANG-01B.
- Donnée utilisée : A termine toujours, B boucle toujours, C dépend d’une conjecture.
- Résultat attendu : A décidable par preuve directe ; B non-terminaison prouvée par invariant True ; C peut être hors de portée sans preuve mathématique supplémentaire.
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
| Fiche | T15_fiche_cours_calculabilite_arret.md | needs_review |
| Séance | T15-S1 | progression existante |
| Évaluation | T15_evaluation_calculabilite_arret.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans le dossier Documents_DRIVE avant création.
- Aucun fichier Drive n’a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
