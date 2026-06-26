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
- O1 : appliquer les méthodes de la fiche à une donnée différente.
- O2 : distinguer lecture d'information, production et justification.
- O3 : traiter au moins un cas limite sans le masquer.
- O4 : préparer une correction exploitable en séance.

## Capacités officielles
- T-ALGO-03

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T16/T16_fiche_cours_diviser_pour_regner_tri_fusion.md`.
- Séance liée : `T16-S1` dans la progression annuelle.
- Statut : support créé en `needs_review`, non validé pédagogiquement et non publiable.

## Situation de travail
une liste [8, 3, 7, 2, 9, 1] est triée par découpage récursif puis fusion contrôlée.

## Données de référence
Liste L = [8, 3, 7, 2, 9, 1], sous-listes [3,8] et [1,2,7,9], cas vide [].

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée et vocabulaire.
- Standard : exercices 3 à 6, production écrite avec contrôle.
- Approfondissement : exercices 7 et 8, comparaison de démarches et généralisation.

## Exercices
### Exercice 1 - Lire l’arbre d’appels récursifs du tri fusion
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-ALGO-03.
- Données : Liste L = [8, 3, 7, 2, 9, 1], sous-listes [3,8] et [1,2,7,9], cas vide [].
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de lire l’arbre d’appels récursifs du tri fusion.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 2 - Analyser une fusion de deux listes déjà triées
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-ALGO-03.
- Données : Liste L = [8, 3, 7, 2, 9, 1], sous-listes [3,8] et [1,2,7,9], cas vide [].
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de analyser une fusion de deux listes déjà triées.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 3 - Écrire la fonction fusion avec deux indices
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-ALGO-03.
- Données : Liste L = [8, 3, 7, 2, 9, 1], sous-listes [3,8] et [1,2,7,9], cas vide [].
- Consigne : Produis une réponse opérationnelle pour écrire la fonction fusion avec deux indices, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 4 - Écrire le schéma diviser, résoudre, combiner
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-ALGO-03.
- Données : Liste L = [8, 3, 7, 2, 9, 1], sous-listes [3,8] et [1,2,7,9], cas vide [].
- Consigne : Produis une réponse opérationnelle pour écrire le schéma diviser, résoudre, combiner, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 5 - Traiter le cas limite liste vide ou un seul élément
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : T-ALGO-03.
- Données : Liste L = [8, 3, 7, 2, 9, 1], sous-listes [3,8] et [1,2,7,9], cas vide [].
- Consigne : Traite le cas limite demandé pour traiter le cas limite liste vide ou un seul élément et précise la convention retenue.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 6 - Justifier la terminaison par diminution de taille
- Type : justification.
- Niveau : standard.
- Capacité officielle : T-ALGO-03.
- Données : Liste L = [8, 3, 7, 2, 9, 1], sous-listes [3,8] et [1,2,7,9], cas vide [].
- Consigne : Justifie pourquoi la méthode utilisée pour justifier la terminaison par diminution de taille est correcte dans ce contexte.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 7 - Compter le nombre de niveaux de division
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : T-ALGO-03.
- Données : Liste L = [8, 3, 7, 2, 9, 1], sous-listes [3,8] et [1,2,7,9], cas vide [].
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de compter le nombre de niveaux de division.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 8 - Comparer tri fusion et tri insertion sur grande liste
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : T-ALGO-03.
- Données : Liste L = [8, 3, 7, 2, 9, 1], sous-listes [3,8] et [1,2,7,9], cas vide [].
- Consigne : Produis une réponse opérationnelle pour comparer tri fusion et tri insertion sur grande liste, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : T-ALGO-03.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T16 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « lire l’arbre d’appels récursifs du tri fusion » en utilisant le vocabulaire diviser pour régner tri fusion.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 2
- Capacité mobilisée : T-ALGO-03.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T16 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « analyser une fusion de deux listes déjà triées » en utilisant le vocabulaire diviser pour régner tri fusion.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 3
- Capacité mobilisée : T-ALGO-03.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T16 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « écrire la fonction fusion avec deux indices » en utilisant le vocabulaire diviser pour régner tri fusion.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 4
- Capacité mobilisée : T-ALGO-03.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T16 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « écrire le schéma diviser, résoudre, combiner » en utilisant le vocabulaire diviser pour régner tri fusion.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 5
- Capacité mobilisée : T-ALGO-03.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T16 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « traiter le cas limite liste vide ou un seul élément » en utilisant le vocabulaire diviser pour régner tri fusion.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 6
- Capacité mobilisée : T-ALGO-03.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T16 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « justifier la terminaison par diminution de taille » en utilisant le vocabulaire diviser pour régner tri fusion.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 7
- Capacité mobilisée : T-ALGO-03.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T16 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « compter le nombre de niveaux de division » en utilisant le vocabulaire diviser pour régner tri fusion.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 8
- Capacité mobilisée : T-ALGO-03.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T16 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « comparer tri fusion et tri insertion sur grande liste » en utilisant le vocabulaire diviser pour régner tri fusion.
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
| Fiche | T16_fiche_cours_diviser_pour_regner_tri_fusion.md | needs_review |
| Séance | T16-S1 | progression existante |
| Évaluation | T16_evaluation_diviser_pour_regner_tri_fusion.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans `/home/alaeddine/Documents/NSI/Documents_DRIVE` avant création.
- Aucun fichier Drive n'a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
