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
- O1 : appliquer les méthodes de la fiche à une donnée différente.
- O2 : distinguer lecture d'information, production et justification.
- O3 : traiter au moins un cas limite sans le masquer.
- O4 : préparer une correction exploitable en séance.

## Capacités officielles
- T-LANG-01A
- T-LANG-01B
- T-LANG-01C

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T15/T15_fiche_cours_calculabilite_arret.md`.
- Séance liée : `T15-S1` dans la progression annuelle.
- Statut : support créé en `needs_review`, non validé pédagogiquement et non publiable.

## Situation de travail
un analyseur imaginaire prétend décider pour tout programme Python si l’exécution termine.

## Données de référence
Programmes : boucle_finie décrémente n, boucle_infinie while True, programme diagonal qui inverse la réponse d’un prédicteur halt(p,x).

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée et vocabulaire.
- Standard : exercices 3 à 6, production écrite avec contrôle.
- Approfondissement : exercices 7 et 8, comparaison de démarches et généralisation.

## Exercices
### Exercice 1 - Lire un programme simple et décider s’il termine pour une entrée donnée
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-LANG-01A.
- Données : Programmes : boucle_finie décrémente n, boucle_infinie while True, programme diagonal qui inverse la réponse d’un prédicteur halt(p,x).
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de lire un programme simple et décider s’il termine pour une entrée donnée.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 2 - Analyser une boucle infinie évidente
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-LANG-01B.
- Données : Programmes : boucle_finie décrémente n, boucle_infinie while True, programme diagonal qui inverse la réponse d’un prédicteur halt(p,x).
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de analyser une boucle infinie évidente.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 3 - Écrire un prédicteur limité à une famille finie de programmes
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-LANG-01C.
- Données : Programmes : boucle_finie décrémente n, boucle_infinie while True, programme diagonal qui inverse la réponse d’un prédicteur halt(p,x).
- Consigne : Produis une réponse opérationnelle pour écrire un prédicteur limité à une famille finie de programmes, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 4 - Produire le programme diagonal de contradiction
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-LANG-01A.
- Données : Programmes : boucle_finie décrémente n, boucle_infinie while True, programme diagonal qui inverse la réponse d’un prédicteur halt(p,x).
- Consigne : Produis une réponse opérationnelle pour produire le programme diagonal de contradiction, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 5 - Traiter le cas limite entrée qui change la terminaison
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : T-LANG-01B.
- Données : Programmes : boucle_finie décrémente n, boucle_infinie while True, programme diagonal qui inverse la réponse d’un prédicteur halt(p,x).
- Consigne : Traite le cas limite demandé pour traiter le cas limite entrée qui change la terminaison et précise la convention retenue.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 6 - Justifier que le problème général de l’arrêt n’a pas d’algorithme total
- Type : justification.
- Niveau : standard.
- Capacité officielle : T-LANG-01C.
- Données : Programmes : boucle_finie décrémente n, boucle_infinie while True, programme diagonal qui inverse la réponse d’un prédicteur halt(p,x).
- Consigne : Justifie pourquoi la méthode utilisée pour justifier que le problème général de l’arrêt n’a pas d’algorithme total est correcte dans ce contexte.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 7 - Distinguer preuve pour un programme et décision pour tous les programmes
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : T-LANG-01A.
- Données : Programmes : boucle_finie décrémente n, boucle_infinie while True, programme diagonal qui inverse la réponse d’un prédicteur halt(p,x).
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de distinguer preuve pour un programme et décision pour tous les programmes.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 8 - Expliquer pourquoi tester longtemps ne prouve pas la non-terminaison
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : T-LANG-01B.
- Données : Programmes : boucle_finie décrémente n, boucle_infinie while True, programme diagonal qui inverse la réponse d’un prédicteur halt(p,x).
- Consigne : Produis une réponse opérationnelle pour expliquer pourquoi tester longtemps ne prouve pas la non-terminaison, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : T-LANG-01A.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T15 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « lire un programme simple et décider s’il termine pour une entrée donnée » en utilisant le vocabulaire calculabilité arrêt.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 2
- Capacité mobilisée : T-LANG-01B.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T15 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « analyser une boucle infinie évidente » en utilisant le vocabulaire calculabilité arrêt.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 3
- Capacité mobilisée : T-LANG-01C.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T15 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « écrire un prédicteur limité à une famille finie de programmes » en utilisant le vocabulaire calculabilité arrêt.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 4
- Capacité mobilisée : T-LANG-01A.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T15 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « produire le programme diagonal de contradiction » en utilisant le vocabulaire calculabilité arrêt.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 5
- Capacité mobilisée : T-LANG-01B.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T15 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « traiter le cas limite entrée qui change la terminaison » en utilisant le vocabulaire calculabilité arrêt.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 6
- Capacité mobilisée : T-LANG-01C.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T15 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « justifier que le problème général de l’arrêt n’a pas d’algorithme total » en utilisant le vocabulaire calculabilité arrêt.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 7
- Capacité mobilisée : T-LANG-01A.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T15 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « distinguer preuve pour un programme et décision pour tous les programmes » en utilisant le vocabulaire calculabilité arrêt.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 8
- Capacité mobilisée : T-LANG-01B.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T15 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « expliquer pourquoi tester longtemps ne prouve pas la non-terminaison » en utilisant le vocabulaire calculabilité arrêt.
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
| Fiche | T15_fiche_cours_calculabilite_arret.md | needs_review |
| Séance | T15-S1 | progression existante |
| Évaluation | T15_evaluation_calculabilite_arret.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans `/home/alaeddine/Documents/NSI/Documents_DRIVE` avant création.
- Aucun fichier Drive n'a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
