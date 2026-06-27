---
title: "T16 - TD - diviser pour régner tri fusion"
level: "terminale"
sequence_id: "T16"
document_type: "td"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Algorithmique"
notion: "diviser pour régner tri fusion"
objectifs:
  - "travailler diviser pour régner tri fusion sur des données explicites"
  - "produire une réponse justifiée et contrôlée"
  - "identifier les cas limites"
  - "corriger les erreurs fréquentes du chapitre"
private_data: false
official_program:
  capacities:
    - "T-ALGO-03"
---

# T16 - TD - diviser pour régner tri fusion

## Objectifs
- Lire une donnée disciplinaire précise avant de répondre.
- Produire une méthode vérifiable et un résultat contrôlable.
- Traiter un cas limite sans le transformer en généralité.
- Relier chaque correction à une erreur fréquente observable.

## Capacités officielles
- T-ALGO-03

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T16/T16_fiche_cours_diviser_pour_regner_tri_fusion.md`.
- Séance liée : `T16-S1` dans la progression annuelle.
- Statut : support `needs_review`, non validé et non publiable.

## Situation de travail
On applique le tri fusion à des listes de temps de calcul.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée.
- Standard : exercices 3 à 6, production écrite et justification.
- Approfondissement : exercices 7 et 8, transfert ou comparaison.

## Exercices
### Exercice 1 - Découper une liste
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-ALGO-03.
- Données : [8,3,5,1,9,2].
- Consigne : Donner les deux moitiés.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 2 - Fusionner deux listes triées
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-ALGO-03.
- Données : [2,5,8] et [1,3,9].
- Consigne : Donner la fusion.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 3 - Écrire pseudo-code fusion
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-ALGO-03.
- Données : g=[2,8], d=[1,5].
- Consigne : Produire pseudo-code.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 4 - Tracer tri fusion complet
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-ALGO-03.
- Données : [4,1,3,2].
- Consigne : Donner étapes.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 5 - Liste vide ou singleton
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : T-ALGO-03.
- Données : [] et [7].
- Consigne : Dire le résultat.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 6 - Justifier complexité
- Type : justification.
- Niveau : standard.
- Capacité officielle : T-ALGO-03.
- Données : n éléments, découpe en deux et fusion linéaire.
- Consigne : Donner ordre.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 7 - Comparer à tri insertion
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : T-ALGO-03.
- Données : n=1024.
- Consigne : Ordres de grandeur.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 8 - Garantir stabilité
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : T-ALGO-03.
- Données : Deux éléments égaux 5a et 5b.
- Consigne : Donner règle.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : T-ALGO-03.
- Donnée utilisée : [8,3,5,1,9,2].
- Résultat attendu : Moitié gauche [8,3,5], moitié droite [1,9,2]. On continue jusqu’aux listes de taille 1.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 2
- Capacité mobilisée : T-ALGO-03.
- Donnée utilisée : [2,5,8] et [1,3,9].
- Résultat attendu : Comparer têtes: 1, puis 2, puis 3, puis 5, puis 8, puis 9. Résultat [1,2,3,5,8,9].
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 3
- Capacité mobilisée : T-ALGO-03.
- Donnée utilisée : g=[2,8], d=[1,5].
- Résultat attendu : i=j=0 ; tant que i<len(g) et j<len(d), prendre le plus petit ; ajouter le reste. Résultat [1,2,5,8].
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 4
- Capacité mobilisée : T-ALGO-03.
- Donnée utilisée : [4,1,3,2].
- Résultat attendu : Découpe [4,1]|[3,2], puis [4],[1],[3],[2]. Fusions [1,4], [2,3], puis [1,2,3,4].
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 5
- Capacité mobilisée : T-ALGO-03.
- Donnée utilisée : [] et [7].
- Résultat attendu : Le tri fusion renvoie [] pour liste vide et [7] pour singleton : ce sont des cas de base sans fusion.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 6
- Capacité mobilisée : T-ALGO-03.
- Donnée utilisée : n éléments, découpe en deux et fusion linéaire.
- Résultat attendu : Il y a log2(n) niveaux de découpe et chaque niveau fusionne n éléments. Complexité O(n log n).
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 7
- Capacité mobilisée : T-ALGO-03.
- Donnée utilisée : n=1024.
- Résultat attendu : Tri fusion: 1024*10 environ 10240 opérations ; insertion pire cas environ 1024^2 = 1 048 576.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 8
- Capacité mobilisée : T-ALGO-03.
- Donnée utilisée : Deux éléments égaux 5a et 5b.
- Résultat attendu : Lors d’une égalité, prendre l’élément de la liste gauche en premier. L’ordre 5a avant 5b est conservé.
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
| Fiche | T16_fiche_cours_diviser_pour_regner_tri_fusion.md | needs_review |
| Séance | T16-S1 | progression existante |
| Évaluation | T16_evaluation_diviser_pour_regner_tri_fusion.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans le dossier Documents_DRIVE avant création.
- Aucun fichier Drive n’a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
