---
title: "T10 - TD - SQL INSERT UPDATE DELETE"
level: "terminale"
sequence_id: "T10"
document_type: "td"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Bases de données"
notion: "SQL INSERT UPDATE DELETE"
objectifs:
  - "travailler SQL INSERT UPDATE DELETE sur des données explicites"
  - "produire une réponse justifiée et contrôlée"
  - "identifier les cas limites"
  - "corriger les erreurs fréquentes du chapitre"
private_data: false
official_program:
  capacities:
    - "T-BDD-03F"
    - "T-BDD-03G"
    - "T-BDD-03H"
---
# T10 - TD - SQL INSERT UPDATE DELETE

## Objectifs
- O1 : appliquer les méthodes de la fiche à une donnée différente.
- O2 : distinguer lecture d'information, production et justification.
- O3 : traiter au moins un cas limite sans le masquer.
- O4 : préparer une correction exploitable en séance.

## Capacités officielles
- T-BDD-03F
- T-BDD-03G
- T-BDD-03H

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T10/T10_fiche_cours_sql_insert_update_delete.md`.
- Séance liée : `T10-S1` dans la progression annuelle.
- Statut : support créé en `needs_review`, non validé pédagogiquement et non publiable.

## Situation de travail
une table Projet(id_projet, titre, etat) doit être modifiée en gardant une vérification SELECT après chaque requête.

## Données de référence
Avant : Projet(1,"Site","en cours"), Projet(2,"Robot","test"), Projet(3,"Jeu","archive").

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée et vocabulaire.
- Standard : exercices 3 à 6, production écrite avec contrôle.
- Approfondissement : exercices 7 et 8, comparaison de démarches et généralisation.

## Exercices
### Exercice 1 - Lire l’état initial d’une table avant modification
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-BDD-03F.
- Données : Avant : Projet(1,"Site","en cours"), Projet(2,"Robot","test"), Projet(3,"Jeu","archive").
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de lire l’état initial d’une table avant modification.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 2 - Identifier la ligne visée par une clé primaire
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-BDD-03G.
- Données : Avant : Projet(1,"Site","en cours"), Projet(2,"Robot","test"), Projet(3,"Jeu","archive").
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de identifier la ligne visée par une clé primaire.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 3 - Écrire un insert pour ajouter projet(4,"data","idée")
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-BDD-03H.
- Données : Avant : Projet(1,"Site","en cours"), Projet(2,"Robot","test"), Projet(3,"Jeu","archive").
- Consigne : Produis une réponse opérationnelle pour écrire un INSERT pour ajouter Projet(4,"Data","idée"), avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 4 - Écrire un update ciblé qui passe le projet 2 à validé
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-BDD-03F.
- Données : Avant : Projet(1,"Site","en cours"), Projet(2,"Robot","test"), Projet(3,"Jeu","archive").
- Consigne : Produis une réponse opérationnelle pour écrire un UPDATE ciblé qui passe le projet 2 à validé, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 5 - Traiter le cas limite update sans where
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : T-BDD-03G.
- Données : Avant : Projet(1,"Site","en cours"), Projet(2,"Robot","test"), Projet(3,"Jeu","archive").
- Consigne : Traite le cas limite demandé pour traiter le cas limite UPDATE sans WHERE et précise la convention retenue.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 6 - Justifier le danger d’un delete trop large
- Type : justification.
- Niveau : standard.
- Capacité officielle : T-BDD-03H.
- Données : Avant : Projet(1,"Site","en cours"), Projet(2,"Robot","test"), Projet(3,"Jeu","archive").
- Consigne : Justifie pourquoi la méthode utilisée pour justifier le danger d’un DELETE trop large est correcte dans ce contexte.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 7 - Écrire un delete ciblé sur le projet 3
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : T-BDD-03F.
- Données : Avant : Projet(1,"Site","en cours"), Projet(2,"Robot","test"), Projet(3,"Jeu","archive").
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de écrire un DELETE ciblé sur le projet 3.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 8 - Vérifier chaque modification par select
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : T-BDD-03G.
- Données : Avant : Projet(1,"Site","en cours"), Projet(2,"Robot","test"), Projet(3,"Jeu","archive").
- Consigne : Produis une réponse opérationnelle pour vérifier chaque modification par SELECT, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : T-BDD-03F.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T10 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « lire l’état initial d’une table avant modification » en utilisant le vocabulaire SQL INSERT UPDATE DELETE.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 2
- Capacité mobilisée : T-BDD-03G.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T10 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « identifier la ligne visée par une clé primaire » en utilisant le vocabulaire SQL INSERT UPDATE DELETE.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 3
- Capacité mobilisée : T-BDD-03H.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T10 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « écrire un INSERT pour ajouter Projet(4,"Data","idée") » en utilisant le vocabulaire SQL INSERT UPDATE DELETE.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 4
- Capacité mobilisée : T-BDD-03F.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T10 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « écrire un UPDATE ciblé qui passe le projet 2 à validé » en utilisant le vocabulaire SQL INSERT UPDATE DELETE.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 5
- Capacité mobilisée : T-BDD-03G.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T10 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « traiter le cas limite UPDATE sans WHERE » en utilisant le vocabulaire SQL INSERT UPDATE DELETE.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 6
- Capacité mobilisée : T-BDD-03H.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T10 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « justifier le danger d’un DELETE trop large » en utilisant le vocabulaire SQL INSERT UPDATE DELETE.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 7
- Capacité mobilisée : T-BDD-03F.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T10 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « écrire un DELETE ciblé sur le projet 3 » en utilisant le vocabulaire SQL INSERT UPDATE DELETE.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 8
- Capacité mobilisée : T-BDD-03G.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T10 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « vérifier chaque modification par SELECT » en utilisant le vocabulaire SQL INSERT UPDATE DELETE.
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
| Fiche | T10_fiche_cours_sql_insert_update_delete.md | needs_review |
| Séance | T10-S1 | progression existante |
| Évaluation | T10_evaluation_sql_insert_update_delete.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans `/home/alaeddine/Documents/NSI/Documents_DRIVE` avant création.
- Aucun fichier Drive n'a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
