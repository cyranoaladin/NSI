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
# P13 - TD - dichotomie glouton k-NN

## Objectifs
- O1 : appliquer les méthodes de la fiche à une donnée différente.
- O2 : distinguer lecture d'information, production et justification.
- O3 : traiter au moins un cas limite sans le masquer.
- O4 : préparer une correction exploitable en séance.

## Capacités officielles
- P-ALGO-03
- P-ALGO-04
- P-ALGO-05

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/premiere/P13/P13_fiche_cours_dichotomie_glouton_knn.md`.
- Séance liée : `P13-S1` dans la progression annuelle.
- Statut : support créé en `needs_review`, non validé pédagogiquement et non publiable.

## Situation de travail
un moteur de recherche simplifié combine une recherche dichotomique, un choix glouton de pièces et un classement par plus proches voisins.

## Données de référence
Liste triée M = [4, 9, 15, 18, 23, 31, 42], somme 30 avec pièces [1, 4, 6, 10], points A(1,1), B(2,3), C(5,4), D(6,1), requête Q(3,2).

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée et vocabulaire.
- Standard : exercices 3 à 6, production écrite avec contrôle.
- Approfondissement : exercices 7 et 8, comparaison de démarches et généralisation.

## Exercices
### Exercice 1 - Tracer la dichotomie pour chercher 23 dans m
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : P-ALGO-03.
- Données : Liste triée M = [4, 9, 15, 18, 23, 31, 42], somme 30 avec pièces [1, 4, 6, 10], points A(1,1), B(2,3), C(5,4), D(6,1), requête Q(3,2).
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de tracer la dichotomie pour chercher 23 dans M.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 2 - Détecter l’échec de la dichotomie pour 20
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : P-ALGO-04.
- Données : Liste triée M = [4, 9, 15, 18, 23, 31, 42], somme 30 avec pièces [1, 4, 6, 10], points A(1,1), B(2,3), C(5,4), D(6,1), requête Q(3,2).
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de détecter l’échec de la dichotomie pour 20.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 3 - Écrire l’algorithme glouton pour rendre 30 avec les pièces proposées
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : P-ALGO-05.
- Données : Liste triée M = [4, 9, 15, 18, 23, 31, 42], somme 30 avec pièces [1, 4, 6, 10], points A(1,1), B(2,3), C(5,4), D(6,1), requête Q(3,2).
- Consigne : Produis une réponse opérationnelle pour écrire l’algorithme glouton pour rendre 30 avec les pièces proposées, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 4 - Construire un contre-exemple où un glouton n’est pas optimal
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : P-ALGO-03.
- Données : Liste triée M = [4, 9, 15, 18, 23, 31, 42], somme 30 avec pièces [1, 4, 6, 10], points A(1,1), B(2,3), C(5,4), D(6,1), requête Q(3,2).
- Consigne : Produis une réponse opérationnelle pour construire un contre-exemple où un glouton n’est pas optimal, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 5 - Traiter le cas limite liste vide ou k supérieur au nombre de points
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : P-ALGO-04.
- Données : Liste triée M = [4, 9, 15, 18, 23, 31, 42], somme 30 avec pièces [1, 4, 6, 10], points A(1,1), B(2,3), C(5,4), D(6,1), requête Q(3,2).
- Consigne : Traite le cas limite demandé pour traiter le cas limite liste vide ou k supérieur au nombre de points et précise la convention retenue.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 6 - Justifier la réduction d’intervalle en dichotomie
- Type : justification.
- Niveau : standard.
- Capacité officielle : P-ALGO-05.
- Données : Liste triée M = [4, 9, 15, 18, 23, 31, 42], somme 30 avec pièces [1, 4, 6, 10], points A(1,1), B(2,3), C(5,4), D(6,1), requête Q(3,2).
- Consigne : Justifie pourquoi la méthode utilisée pour justifier la réduction d’intervalle en dichotomie est correcte dans ce contexte.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 7 - Calculer les distances pour les deux plus proches voisins de q
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : P-ALGO-03.
- Données : Liste triée M = [4, 9, 15, 18, 23, 31, 42], somme 30 avec pièces [1, 4, 6, 10], points A(1,1), B(2,3), C(5,4), D(6,1), requête Q(3,2).
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de calculer les distances pour les deux plus proches voisins de Q.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 8 - Comparer solution exacte et heuristique gloutonne
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : P-ALGO-04.
- Données : Liste triée M = [4, 9, 15, 18, 23, 31, 42], somme 30 avec pièces [1, 4, 6, 10], points A(1,1), B(2,3), C(5,4), D(6,1), requête Q(3,2).
- Consigne : Produis une réponse opérationnelle pour comparer solution exacte et heuristique gloutonne, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : P-ALGO-03.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P13 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « tracer la dichotomie pour chercher 23 dans M » en utilisant le vocabulaire dichotomie glouton k-NN.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 2
- Capacité mobilisée : P-ALGO-04.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P13 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « détecter l’échec de la dichotomie pour 20 » en utilisant le vocabulaire dichotomie glouton k-NN.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 3
- Capacité mobilisée : P-ALGO-05.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P13 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « écrire l’algorithme glouton pour rendre 30 avec les pièces proposées » en utilisant le vocabulaire dichotomie glouton k-NN.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 4
- Capacité mobilisée : P-ALGO-03.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P13 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « construire un contre-exemple où un glouton n’est pas optimal » en utilisant le vocabulaire dichotomie glouton k-NN.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 5
- Capacité mobilisée : P-ALGO-04.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P13 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « traiter le cas limite liste vide ou k supérieur au nombre de points » en utilisant le vocabulaire dichotomie glouton k-NN.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 6
- Capacité mobilisée : P-ALGO-05.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P13 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « justifier la réduction d’intervalle en dichotomie » en utilisant le vocabulaire dichotomie glouton k-NN.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 7
- Capacité mobilisée : P-ALGO-03.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P13 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « calculer les distances pour les deux plus proches voisins de Q » en utilisant le vocabulaire dichotomie glouton k-NN.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 8
- Capacité mobilisée : P-ALGO-04.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P13 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « comparer solution exacte et heuristique gloutonne » en utilisant le vocabulaire dichotomie glouton k-NN.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.

## Erreurs fréquentes
- EF1 : recopier une définition sans l'appliquer à la donnée ; remédiation : entourer les valeurs utilisées avant d'écrire.
- EF2 : produire un résultat sans contrôle ; remédiation : ajouter une ligne « vérification » à chaque réponse.
- EF3 : confondre cas nominal et cas limite ; remédiation : refaire l'exercice 5 avec une donnée minimale.
- EF4 : citer la capacité officielle sans méthode ; remédiation : associer chaque capacité à une action observable.

## Différenciation
- Socle : fournir la donnée annotée et demander une phrase de conclusion.
- Standard : demander la méthode complète et le contrôle écrit.
- Approfondissement : demander une variante de donnée et une comparaison de deux démarches.

## Lien avec la progression
| Élément | Référence | Statut |
|---|---|---|
| Fiche | P13_fiche_cours_dichotomie_glouton_knn.md | needs_review |
| Séance | P13-S1 | progression existante |
| Évaluation | P13_evaluation_dichotomie_glouton_knn.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans `/home/alaeddine/Documents/NSI/Documents_DRIVE` avant création.
- Aucun fichier Drive n'a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
