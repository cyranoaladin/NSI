---
title: "T17 - TD - programmation dynamique"
level: "terminale"
sequence_id: "T17"
document_type: "td"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Algorithmique"
notion: "programmation dynamique"
objectifs:
  - "travailler programmation dynamique sur des données explicites"
  - "produire une réponse justifiée et contrôlée"
  - "identifier les cas limites"
  - "corriger les erreurs fréquentes du chapitre"
private_data: false
official_program:
  capacities:
    - "T-ALGO-04"
---

# T17 - TD - programmation dynamique

## Objectifs
- Lire une donnée disciplinaire précise avant de répondre.
- Produire une méthode vérifiable et un résultat contrôlable.
- Traiter un cas limite sans le transformer en généralité.
- Relier chaque correction à une erreur fréquente observable.

## Capacités officielles
- T-ALGO-04

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T17/T17_fiche_cours_programmation_dynamique.md`.
- Séance liée : `T17-S1` dans la progression annuelle.
- Statut : support `needs_review`, non validé et non publiable.

## Situation de travail
On résout un problème de nombre de chemins dans une grille 3 x 3 puis un rendu de monnaie minimal.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée.
- Standard : exercices 3 à 6, production écrite et justification.
- Approfondissement : exercices 7 et 8, transfert ou comparaison.

## Exercices
### Exercice 1 - Définir un état
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-ALGO-04.
- Données : Grille 3x3, déplacements droite ou bas.
- Consigne : Définir dp[i][j].
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 2 - Remplir les bords
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-ALGO-04.
- Données : dp sur grille 3x3.
- Consigne : Donner première ligne et première colonne.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 3 - Écrire la récurrence
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-ALGO-04.
- Données : Case intérieure (i,j).
- Consigne : Donner relation.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 4 - Remplir le tableau 3x3
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-ALGO-04.
- Données : Grille 3x3.
- Consigne : Donner la table.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 5 - Grille 1x1
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : T-ALGO-04.
- Données : Départ égale arrivée.
- Consigne : Donner dp.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 6 - Comparer récursion et tabulation
- Type : justification.
- Niveau : standard.
- Capacité officielle : T-ALGO-04.
- Données : Calcul chemins(4,4).
- Consigne : Expliquer les doublons.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 7 - Rendu de monnaie dynamique
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : T-ALGO-04.
- Données : pièces [1,3,4], montant 6.
- Consigne : Donner dp[0..6].
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 8 - Écrire pseudo-code tabulation
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : T-ALGO-04.
- Données : pièces [1,3,4], montant M.
- Consigne : Produire pseudo-code.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : T-ALGO-04.
- Donnée utilisée : Grille 3x3, déplacements droite ou bas.
- Résultat attendu : dp[i][j] = nombre de chemins depuis (0,0) vers la case (i,j).
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 2
- Capacité mobilisée : T-ALGO-04.
- Donnée utilisée : dp sur grille 3x3.
- Résultat attendu : dp[0][j]=1 et dp[i][0]=1 car un seul chemin en ligne droite. Bords: 1,1,1.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 3
- Capacité mobilisée : T-ALGO-04.
- Donnée utilisée : Case intérieure (i,j).
- Résultat attendu : dp[i][j] = dp[i-1][j] + dp[i][j-1]. Pour (1,1): 1+1=2.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 4
- Capacité mobilisée : T-ALGO-04.
- Donnée utilisée : Grille 3x3.
- Résultat attendu : Table dp: ligne0 [1,1,1], ligne1 [1,2,3], ligne2 [1,3,6]. Il y a 6 chemins vers (2,2).
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 5
- Capacité mobilisée : T-ALGO-04.
- Donnée utilisée : Départ égale arrivée.
- Résultat attendu : dp[0][0]=1 : il existe un chemin vide. Ne pas renvoyer 0.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 6
- Capacité mobilisée : T-ALGO-04.
- Donnée utilisée : Calcul chemins(4,4).
- Résultat attendu : La récursion naïve recalcule chemins(2,2) plusieurs fois ; la tabulation calcule chaque état une seule fois, donc O(n*m).
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 7
- Capacité mobilisée : T-ALGO-04.
- Donnée utilisée : pièces [1,3,4], montant 6.
- Résultat attendu : dp: [0,1,2,1,1,2,2]. Pour 6, optimal 3+3 donc 2 pièces.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 8
- Capacité mobilisée : T-ALGO-04.
- Donnée utilisée : pièces [1,3,4], montant M.
- Résultat attendu : dp[0]=0 ; dp[a]=inf ; pour a de 1 à M, pour p dans pièces si a>=p: dp[a]=min(dp[a],1+dp[a-p]).
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
| Fiche | T17_fiche_cours_programmation_dynamique.md | needs_review |
| Séance | T17-S1 | progression existante |
| Évaluation | T17_evaluation_programmation_dynamique.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans le dossier Documents_DRIVE avant création.
- Aucun fichier Drive n’a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
