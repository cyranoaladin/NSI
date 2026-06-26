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
- O1 : appliquer les méthodes de la fiche à une donnée différente.
- O2 : distinguer lecture d'information, production et justification.
- O3 : traiter au moins un cas limite sans le masquer.
- O4 : préparer une correction exploitable en séance.

## Capacités officielles
- T-ALGO-04

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T17/T17_fiche_cours_programmation_dynamique.md`.
- Séance liée : `T17-S1` dans la progression annuelle.
- Statut : support créé en `needs_review`, non validé pédagogiquement et non publiable.

## Situation de travail
un robot avance sur une ligne et cherche le coût minimal pour atteindre la case 6 en mémorisant les sous-problèmes.

## Données de référence
Coûts cases = [0, 2, 5, 1, 4, 3, 6], transitions possibles +1 ou +2, valeur fib(6) à comparer avec une version récursive naïve.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée et vocabulaire.
- Standard : exercices 3 à 6, production écrite avec contrôle.
- Approfondissement : exercices 7 et 8, comparaison de démarches et généralisation.

## Exercices
### Exercice 1 - Lire une table de mémoïsation partiellement remplie
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-ALGO-04.
- Données : Coûts cases = [0, 2, 5, 1, 4, 3, 6], transitions possibles +1 ou +2, valeur fib(6) à comparer avec une version récursive naïve.
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de lire une table de mémoïsation partiellement remplie.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 2 - Analyser le recouvrement de sous-problèmes sur fibonacci
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-ALGO-04.
- Données : Coûts cases = [0, 2, 5, 1, 4, 3, 6], transitions possibles +1 ou +2, valeur fib(6) à comparer avec une version récursive naïve.
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de analyser le recouvrement de sous-problèmes sur Fibonacci.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 3 - Écrire une récurrence de coût minimal
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-ALGO-04.
- Données : Coûts cases = [0, 2, 5, 1, 4, 3, 6], transitions possibles +1 ou +2, valeur fib(6) à comparer avec une version récursive naïve.
- Consigne : Produis une réponse opérationnelle pour écrire une récurrence de coût minimal, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 4 - Remplir une table de programmation dynamique de gauche à droite
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-ALGO-04.
- Données : Coûts cases = [0, 2, 5, 1, 4, 3, 6], transitions possibles +1 ou +2, valeur fib(6) à comparer avec une version récursive naïve.
- Consigne : Produis une réponse opérationnelle pour remplir une table de programmation dynamique de gauche à droite, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 5 - Traiter le cas limite objectif 0 ou coût absent
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : T-ALGO-04.
- Données : Coûts cases = [0, 2, 5, 1, 4, 3, 6], transitions possibles +1 ou +2, valeur fib(6) à comparer avec une version récursive naïve.
- Consigne : Traite le cas limite demandé pour traiter le cas limite objectif 0 ou coût absent et précise la convention retenue.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 6 - Justifier ordre de calcul et dépendances
- Type : justification.
- Niveau : standard.
- Capacité officielle : T-ALGO-04.
- Données : Coûts cases = [0, 2, 5, 1, 4, 3, 6], transitions possibles +1 ou +2, valeur fib(6) à comparer avec une version récursive naïve.
- Consigne : Justifie pourquoi la méthode utilisée pour justifier ordre de calcul et dépendances est correcte dans ce contexte.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 7 - Repérer une recomputation inutile
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : T-ALGO-04.
- Données : Coûts cases = [0, 2, 5, 1, 4, 3, 6], transitions possibles +1 ou +2, valeur fib(6) à comparer avec une version récursive naïve.
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de repérer une recomputation inutile.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 8 - Comparer mémoïsation top-down et tabulation bottom-up
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : T-ALGO-04.
- Données : Coûts cases = [0, 2, 5, 1, 4, 3, 6], transitions possibles +1 ou +2, valeur fib(6) à comparer avec une version récursive naïve.
- Consigne : Produis une réponse opérationnelle pour comparer mémoïsation top-down et tabulation bottom-up, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : T-ALGO-04.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T17 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « lire une table de mémoïsation partiellement remplie » en utilisant le vocabulaire programmation dynamique.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 2
- Capacité mobilisée : T-ALGO-04.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T17 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « analyser le recouvrement de sous-problèmes sur Fibonacci » en utilisant le vocabulaire programmation dynamique.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 3
- Capacité mobilisée : T-ALGO-04.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T17 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « écrire une récurrence de coût minimal » en utilisant le vocabulaire programmation dynamique.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 4
- Capacité mobilisée : T-ALGO-04.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T17 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « remplir une table de programmation dynamique de gauche à droite » en utilisant le vocabulaire programmation dynamique.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 5
- Capacité mobilisée : T-ALGO-04.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T17 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « traiter le cas limite objectif 0 ou coût absent » en utilisant le vocabulaire programmation dynamique.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 6
- Capacité mobilisée : T-ALGO-04.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T17 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « justifier ordre de calcul et dépendances » en utilisant le vocabulaire programmation dynamique.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 7
- Capacité mobilisée : T-ALGO-04.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T17 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « repérer une recomputation inutile » en utilisant le vocabulaire programmation dynamique.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 8
- Capacité mobilisée : T-ALGO-04.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T17 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « comparer mémoïsation top-down et tabulation bottom-up » en utilisant le vocabulaire programmation dynamique.
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
| Fiche | T17_fiche_cours_programmation_dynamique.md | needs_review |
| Séance | T17-S1 | progression existante |
| Évaluation | T17_evaluation_programmation_dynamique.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans `/home/alaeddine/Documents/NSI/Documents_DRIVE` avant création.
- Aucun fichier Drive n'a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
