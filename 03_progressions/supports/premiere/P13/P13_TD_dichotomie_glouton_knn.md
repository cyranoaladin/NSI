---
title: "P13 - TD - dichotomie glouton k-NN"
level: "premiere"
sequence_id: "P13"
document_type: "td"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Algorithmique"
notion: "dichotomie glouton k-NN"
objectifs:
  - "travailler dichotomie glouton k-NN sur des données explicites"
  - "produire une réponse justifiée et contrôlée"
  - "identifier les cas limites"
  - "corriger les erreurs fréquentes du chapitre"
private_data: false
official_program:
  capacities:
    - "P-ALGO-03"
    - "P-ALGO-04"
    - "P-ALGO-05"
---

# P13 - TD - dichotomie glouton knn

## Objectifs
- Lire une donnée disciplinaire précise avant de répondre.
- Produire une méthode vérifiable et un résultat contrôlable.
- Traiter un cas limite sans le transformer en généralité.
- Relier chaque correction à une erreur fréquente observable.

## Capacités officielles
- P-ALGO-03
- P-ALGO-04
- P-ALGO-05

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/premiere/P13/P13_fiche_cours_dichotomie_glouton_knn.md`.
- Séance liée : `P13-S1` dans la progression annuelle.
- Statut : support `needs_review`, non validé et non publiable.

## Situation de travail
On choisit des algorithmes pour rechercher une valeur, rendre la monnaie et classer un point.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée.
- Standard : exercices 3 à 6, production écrite et justification.
- Approfondissement : exercices 7 et 8, transfert ou comparaison.

## Exercices
### Exercice 1 - Tracer une recherche dichotomique
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : P-ALGO-03.
- Données : tableau trié [3,8,12,19,27,31], cible=19.
- Consigne : Donner les bornes et milieux successifs.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 2 - Repérer la condition de tri
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : P-ALGO-04.
- Données : tableau [4,9,2,11], cible=2.
- Consigne : Dire si la dichotomie est applicable.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 3 - Écrire un glouton de monnaie
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : P-ALGO-05.
- Données : pièces [50,20,10,5,2,1], montant=87.
- Consigne : Donner les pièces choisies.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 4 - Calculer un k-NN
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : P-ALGO-03.
- Données : Points A(0,0) rouge, B(2,0) rouge, C(0,3) bleu ; point X(1,1), k=3.
- Consigne : Calculer les distances carrées et la classe.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 5 - Dichotomie sur tableau vide
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : P-ALGO-04.
- Données : tableau [], cible=5.
- Consigne : Donner la réponse et éviter l’erreur d’indice.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 6 - Justifier le choix glouton
- Type : justification.
- Niveau : standard.
- Capacité officielle : P-ALGO-05.
- Données : Système de pièces [4,3,1], montant=6.
- Consigne : Montrer que le glouton peut échouer.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 7 - Comparer linéaire et dichotomique
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : P-ALGO-03.
- Données : n=64 éléments triés.
- Consigne : Donner le nombre maximal d’étapes dichotomiques.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 8 - Gérer égalité en k-NN
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : P-ALGO-04.
- Données : Voisins: rouge, bleu, bleu, rouge avec k=4.
- Consigne : Proposer une règle explicite.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : P-ALGO-03.
- Donnée utilisée : tableau trié [3,8,12,19,27,31], cible=19.
- Résultat attendu : g=0,d=5,m=2,val=12 -> cible à droite ; g=3,d=5,m=4,val=27 -> cible à gauche ; g=3,d=3,m=3,val=19 -> trouvé indice 3.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 2
- Capacité mobilisée : P-ALGO-04.
- Donnée utilisée : tableau [4,9,2,11], cible=2.
- Résultat attendu : Non, le tableau n’est pas trié. Une dichotomie pourrait éliminer la mauvaise moitié. Il faut trier ou utiliser une recherche séquentielle.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 3
- Capacité mobilisée : P-ALGO-05.
- Donnée utilisée : pièces [50,20,10,5,2,1], montant=87.
- Résultat attendu : Choix glouton: 50 reste 37 ; 20 reste 17 ; 10 reste 7 ; 5 reste 2 ; 2 reste 0. Réponse [50,20,10,5,2].
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 4
- Capacité mobilisée : P-ALGO-03.
- Donnée utilisée : Points A(0,0) rouge, B(2,0) rouge, C(0,3) bleu ; point X(1,1), k=3.
- Résultat attendu : d2(A)=2, d2(B)=2, d2(C)=5. Les 3 voisins contiennent 2 rouges et 1 bleu ; X est classé rouge.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 5
- Capacité mobilisée : P-ALGO-04.
- Donnée utilisée : tableau [], cible=5.
- Résultat attendu : g=0,d=-1 donc la boucle ne démarre pas. Résultat: absent, par exemple -1 ou None selon le contrat.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 6
- Capacité mobilisée : P-ALGO-05.
- Donnée utilisée : Système de pièces [4,3,1], montant=6.
- Résultat attendu : Glouton prend 4 puis 1 puis 1 -> 3 pièces. Solution optimale: 3+3 -> 2 pièces. Le glouton n’est pas toujours optimal.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 7
- Capacité mobilisée : P-ALGO-03.
- Donnée utilisée : n=64 éléments triés.
- Résultat attendu : On divise par 2 à chaque étape ; 64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1. Au plus 7 tests environ, contre 64 en linéaire.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 8
- Capacité mobilisée : P-ALGO-04.
- Donnée utilisée : Voisins: rouge, bleu, bleu, rouge avec k=4.
- Résultat attendu : Égalité 2 rouges / 2 bleus. Règle possible: diminuer k à 3 avec les plus proches ou choisir la classe du voisin le plus proche. La règle doit être annoncée avant le calcul.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.

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
| Fiche | P13_fiche_cours_dichotomie_glouton_knn.md | needs_review |
| Séance | P13-S1 | progression existante |
| Évaluation | P13_evaluation_dichotomie_glouton_knn.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans le dossier Documents_DRIVE avant création.
- Aucun fichier Drive n’a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
