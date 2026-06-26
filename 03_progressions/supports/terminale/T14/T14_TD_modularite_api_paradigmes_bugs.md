---
title: "T14 - TD - modularité API paradigmes bugs"
level: "terminale"
sequence_id: "T14"
document_type: "td"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Langages"
notion: "modularité API paradigmes bugs"
objectifs:
  - "travailler modularité API paradigmes bugs sur des données explicites"
  - "produire une réponse justifiée et contrôlée"
  - "identifier les cas limites"
  - "corriger les erreurs fréquentes du chapitre"
private_data: false
official_program:
  capacities:
    - "T-LANG-03A"
    - "T-LANG-03B"
    - "T-LANG-03C"
    - "T-LANG-04A"
    - "T-LANG-04B"
    - "T-LANG-05"
---
# T14 - TD - modularité API paradigmes bugs

## Objectifs
- O1 : appliquer les méthodes de la fiche à une donnée différente.
- O2 : distinguer lecture d'information, production et justification.
- O3 : traiter au moins un cas limite sans le masquer.
- O4 : préparer une correction exploitable en séance.

## Capacités officielles
- T-LANG-03A
- T-LANG-03B
- T-LANG-03C
- T-LANG-04A
- T-LANG-04B
- T-LANG-05

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T14/T14_fiche_cours_modularite_api_paradigmes_bugs.md`.
- Séance liée : `T14-S1` dans la progression annuelle.
- Statut : support créé en `needs_review`, non validé pédagogiquement et non publiable.

## Situation de travail
un petit module météo expose charger_mesures, moyenne, alerte et une API documentée pour être réutilisée dans un projet.

## Données de référence
Module meteo.py : mesures horaires, seuil alerte 35, documentation de fonction, appel externe qui peut échouer.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée et vocabulaire.
- Standard : exercices 3 à 6, production écrite avec contrôle.
- Approfondissement : exercices 7 et 8, comparaison de démarches et généralisation.

## Exercices
### Exercice 1 - Lire une signature d’api et ses préconditions
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-LANG-03A.
- Données : Module meteo.py : mesures horaires, seuil alerte 35, documentation de fonction, appel externe qui peut échouer.
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de lire une signature d’API et ses préconditions.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 2 - Analyser une documentation pour repérer entrée, sortie, exception
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-LANG-03B.
- Données : Module meteo.py : mesures horaires, seuil alerte 35, documentation de fonction, appel externe qui peut échouer.
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de analyser une documentation pour repérer entrée, sortie, exception.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 3 - Écrire un module simple séparant lecture et calcul
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-LANG-03C.
- Données : Module meteo.py : mesures horaires, seuil alerte 35, documentation de fonction, appel externe qui peut échouer.
- Consigne : Produis une réponse opérationnelle pour écrire un module simple séparant lecture et calcul, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 4 - Écrire un test qui isole un bug de seuil
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-LANG-04A.
- Données : Module meteo.py : mesures horaires, seuil alerte 35, documentation de fonction, appel externe qui peut échouer.
- Consigne : Produis une réponse opérationnelle pour écrire un test qui isole un bug de seuil, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 5 - Traiter le cas limite service api indisponible
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : T-LANG-04B.
- Données : Module meteo.py : mesures horaires, seuil alerte 35, documentation de fonction, appel externe qui peut échouer.
- Consigne : Traite le cas limite demandé pour traiter le cas limite service API indisponible et précise la convention retenue.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 6 - Justifier le choix impératif, fonctionnel ou objet selon la tâche
- Type : justification.
- Niveau : standard.
- Capacité officielle : T-LANG-05.
- Données : Module meteo.py : mesures horaires, seuil alerte 35, documentation de fonction, appel externe qui peut échouer.
- Consigne : Justifie pourquoi la méthode utilisée pour justifier le choix impératif, fonctionnel ou objet selon la tâche est correcte dans ce contexte.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 7 - Repérer une dépendance globale qui rend le test fragile
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : T-LANG-03A.
- Données : Module meteo.py : mesures horaires, seuil alerte 35, documentation de fonction, appel externe qui peut échouer.
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de repérer une dépendance globale qui rend le test fragile.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 8 - Proposer une correction minimale documentée
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : T-LANG-03B.
- Données : Module meteo.py : mesures horaires, seuil alerte 35, documentation de fonction, appel externe qui peut échouer.
- Consigne : Produis une réponse opérationnelle pour proposer une correction minimale documentée, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : T-LANG-03A.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T14 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « lire une signature d’API et ses préconditions » en utilisant le vocabulaire modularité API paradigmes bugs.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 2
- Capacité mobilisée : T-LANG-03B.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T14 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « analyser une documentation pour repérer entrée, sortie, exception » en utilisant le vocabulaire modularité API paradigmes bugs.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 3
- Capacité mobilisée : T-LANG-03C.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T14 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « écrire un module simple séparant lecture et calcul » en utilisant le vocabulaire modularité API paradigmes bugs.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 4
- Capacité mobilisée : T-LANG-04A.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T14 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « écrire un test qui isole un bug de seuil » en utilisant le vocabulaire modularité API paradigmes bugs.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 5
- Capacité mobilisée : T-LANG-04B.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T14 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « traiter le cas limite service API indisponible » en utilisant le vocabulaire modularité API paradigmes bugs.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 6
- Capacité mobilisée : T-LANG-05.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T14 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « justifier le choix impératif, fonctionnel ou objet selon la tâche » en utilisant le vocabulaire modularité API paradigmes bugs.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 7
- Capacité mobilisée : T-LANG-03A.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T14 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « repérer une dépendance globale qui rend le test fragile » en utilisant le vocabulaire modularité API paradigmes bugs.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 8
- Capacité mobilisée : T-LANG-03B.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T14 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « proposer une correction minimale documentée » en utilisant le vocabulaire modularité API paradigmes bugs.
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
| Fiche | T14_fiche_cours_modularite_api_paradigmes_bugs.md | needs_review |
| Séance | T14-S1 | progression existante |
| Évaluation | T14_evaluation_modularite_api_paradigmes_bugs.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans `/home/alaeddine/Documents/NSI/Documents_DRIVE` avant création.
- Aucun fichier Drive n'a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
