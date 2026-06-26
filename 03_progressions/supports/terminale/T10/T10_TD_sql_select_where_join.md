---
title: "T10 - TD - SQL SELECT WHERE JOIN"
level: "terminale"
sequence_id: "T10"
document_type: "td"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Bases de données"
notion: "SQL SELECT WHERE JOIN"
objectifs:
  - "travailler SQL SELECT WHERE JOIN sur des données explicites"
  - "produire une réponse justifiée et contrôlée"
  - "identifier les cas limites"
  - "corriger les erreurs fréquentes du chapitre"
private_data: false
official_program:
  capacities:
    - "T-BDD-03A"
    - "T-BDD-03B"
    - "T-BDD-03C"
    - "T-BDD-03D"
    - "T-BDD-03E"
---
# T10 - TD - SQL SELECT WHERE JOIN

## Objectifs
- O1 : appliquer les méthodes de la fiche à une donnée différente.
- O2 : distinguer lecture d'information, production et justification.
- O3 : traiter au moins un cas limite sans le masquer.
- O4 : préparer une correction exploitable en séance.

## Capacités officielles
- T-BDD-03A
- T-BDD-03B
- T-BDD-03C
- T-BDD-03D
- T-BDD-03E

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T10/T10_fiche_cours_sql_select_where_join.md`.
- Séance liée : `T10-S1` dans la progression annuelle.
- Statut : support créé en `needs_review`, non validé pédagogiquement et non publiable.

## Situation de travail
un relevé de notes utilise Eleve(id_eleve, nom, classe) et Note(id_note, id_eleve, matiere, note).

## Données de référence
Eleve : (1,"E1","T1"), (2,"E2","T2"), (3,"E3","T1"). Note : (10,1,"NSI",15), (11,1,"Maths",13), (12,2,"NSI",9), (13,3,"NSI",18).

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée et vocabulaire.
- Standard : exercices 3 à 6, production écrite avec contrôle.
- Approfondissement : exercices 7 et 8, comparaison de démarches et généralisation.

## Exercices
### Exercice 1 - Lire les colonnes utiles dans un select simple
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-BDD-03A.
- Données : Eleve : (1,"E1","T1"), (2,"E2","T2"), (3,"E3","T1"). Note : (10,1,"NSI",15), (11,1,"Maths",13), (12,2,"NSI",9), (13,3,"NSI",18).
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de lire les colonnes utiles dans un SELECT simple.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 2 - Écrire un where qui filtre les élèves de t1
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-BDD-03B.
- Données : Eleve : (1,"E1","T1"), (2,"E2","T2"), (3,"E3","T1"). Note : (10,1,"NSI",15), (11,1,"Maths",13), (12,2,"NSI",9), (13,3,"NSI",18).
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de écrire un WHERE qui filtre les élèves de T1.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 3 - Produire une jointure eleve-note avec condition on
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-BDD-03C.
- Données : Eleve : (1,"E1","T1"), (2,"E2","T2"), (3,"E3","T1"). Note : (10,1,"NSI",15), (11,1,"Maths",13), (12,2,"NSI",9), (13,3,"NSI",18).
- Consigne : Produis une réponse opérationnelle pour produire une jointure Eleve-Note avec condition ON, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 4 - Écrire une requête triée par note décroissante
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-BDD-03D.
- Données : Eleve : (1,"E1","T1"), (2,"E2","T2"), (3,"E3","T1"). Note : (10,1,"NSI",15), (11,1,"Maths",13), (12,2,"NSI",9), (13,3,"NSI",18).
- Consigne : Produis une réponse opérationnelle pour écrire une requête triée par note décroissante, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 5 - Traiter le cas limite d’une jointure sans condition
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : T-BDD-03E.
- Données : Eleve : (1,"E1","T1"), (2,"E2","T2"), (3,"E3","T1"). Note : (10,1,"NSI",15), (11,1,"Maths",13), (12,2,"NSI",9), (13,3,"NSI",18).
- Consigne : Traite le cas limite demandé pour traiter le cas limite d’une jointure sans condition et précise la convention retenue.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 6 - Justifier la différence entre filtre sur classe et filtre sur matière
- Type : justification.
- Niveau : standard.
- Capacité officielle : T-BDD-03A.
- Données : Eleve : (1,"E1","T1"), (2,"E2","T2"), (3,"E3","T1"). Note : (10,1,"NSI",15), (11,1,"Maths",13), (12,2,"NSI",9), (13,3,"NSI",18).
- Consigne : Justifie pourquoi la méthode utilisée pour justifier la différence entre filtre sur classe et filtre sur matière est correcte dans ce contexte.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 7 - Analyser une requête qui duplique les lignes
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : T-BDD-03B.
- Données : Eleve : (1,"E1","T1"), (2,"E2","T2"), (3,"E3","T1"). Note : (10,1,"NSI",15), (11,1,"Maths",13), (12,2,"NSI",9), (13,3,"NSI",18).
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de analyser une requête qui duplique les lignes.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 8 - Écrire une requête complète nom, matière, note pour les notes au moins 14
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : T-BDD-03C.
- Données : Eleve : (1,"E1","T1"), (2,"E2","T2"), (3,"E3","T1"). Note : (10,1,"NSI",15), (11,1,"Maths",13), (12,2,"NSI",9), (13,3,"NSI",18).
- Consigne : Produis une réponse opérationnelle pour écrire une requête complète nom, matière, note pour les notes au moins 14, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : T-BDD-03A.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T10 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « lire les colonnes utiles dans un SELECT simple » en utilisant le vocabulaire SQL SELECT WHERE JOIN.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 2
- Capacité mobilisée : T-BDD-03B.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T10 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « écrire un WHERE qui filtre les élèves de T1 » en utilisant le vocabulaire SQL SELECT WHERE JOIN.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 3
- Capacité mobilisée : T-BDD-03C.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T10 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « produire une jointure Eleve-Note avec condition ON » en utilisant le vocabulaire SQL SELECT WHERE JOIN.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 4
- Capacité mobilisée : T-BDD-03D.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T10 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « écrire une requête triée par note décroissante » en utilisant le vocabulaire SQL SELECT WHERE JOIN.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 5
- Capacité mobilisée : T-BDD-03E.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T10 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « traiter le cas limite d’une jointure sans condition » en utilisant le vocabulaire SQL SELECT WHERE JOIN.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 6
- Capacité mobilisée : T-BDD-03A.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T10 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « justifier la différence entre filtre sur classe et filtre sur matière » en utilisant le vocabulaire SQL SELECT WHERE JOIN.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 7
- Capacité mobilisée : T-BDD-03B.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T10 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « analyser une requête qui duplique les lignes » en utilisant le vocabulaire SQL SELECT WHERE JOIN.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 8
- Capacité mobilisée : T-BDD-03C.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T10 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « écrire une requête complète nom, matière, note pour les notes au moins 14 » en utilisant le vocabulaire SQL SELECT WHERE JOIN.
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
| Fiche | T10_fiche_cours_sql_select_where_join.md | needs_review |
| Séance | T10-S1 | progression existante |
| Évaluation | T10_evaluation_sql_select_where_join.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans `/home/alaeddine/Documents/NSI/Documents_DRIVE` avant création.
- Aucun fichier Drive n'a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
