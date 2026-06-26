---
title: "T11 - TD - processus ordonnancement interblocage"
level: "terminale"
sequence_id: "T11"
document_type: "td"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Architecture"
notion: "processus ordonnancement interblocage"
objectifs:
  - "travailler processus ordonnancement interblocage sur des données explicites"
  - "produire une réponse justifiée et contrôlée"
  - "identifier les cas limites"
  - "corriger les erreurs fréquentes du chapitre"
private_data: false
official_program:
  capacities:
    - "T-ARCH-01"
    - "T-ARCH-02A"
    - "T-ARCH-02B"
    - "T-ARCH-02C"
---
# T11 - TD - processus ordonnancement interblocage

## Objectifs
- O1 : appliquer les méthodes de la fiche à une donnée différente.
- O2 : distinguer lecture d'information, production et justification.
- O3 : traiter au moins un cas limite sans le masquer.
- O4 : préparer une correction exploitable en séance.

## Capacités officielles
- T-ARCH-01
- T-ARCH-02A
- T-ARCH-02B
- T-ARCH-02C

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T11/T11_fiche_cours_processus_ordonnancement_interblocage.md`.
- Séance liée : `T11-S1` dans la progression annuelle.
- Statut : support créé en `needs_review`, non validé pédagogiquement et non publiable.

## Situation de travail
trois processus P1, P2, P3 partagent CPU, imprimante et fichier verrouillé, avec risque d’attente circulaire.

## Données de référence
P1 demande imprimante puis fichier, P2 demande fichier puis imprimante, P3 calcule 4 unités CPU ; quantum = 2.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée et vocabulaire.
- Standard : exercices 3 à 6, production écrite avec contrôle.
- Approfondissement : exercices 7 et 8, comparaison de démarches et généralisation.

## Exercices
### Exercice 1 - Lire un état prêt, élu, bloqué dans une table de processus
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-ARCH-01.
- Données : P1 demande imprimante puis fichier, P2 demande fichier puis imprimante, P3 calcule 4 unités CPU ; quantum = 2.
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de lire un état prêt, élu, bloqué dans une table de processus.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 2 - Analyser un diagramme d’ordonnancement round-robin
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-ARCH-02A.
- Données : P1 demande imprimante puis fichier, P2 demande fichier puis imprimante, P3 calcule 4 unités CPU ; quantum = 2.
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de analyser un diagramme d’ordonnancement round-robin.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 3 - Produire la file des processus après deux quanta
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-ARCH-02B.
- Données : P1 demande imprimante puis fichier, P2 demande fichier puis imprimante, P3 calcule 4 unités CPU ; quantum = 2.
- Consigne : Produis une réponse opérationnelle pour produire la file des processus après deux quanta, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 4 - Écrire une stratégie pour éviter l’attente circulaire
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-ARCH-02C.
- Données : P1 demande imprimante puis fichier, P2 demande fichier puis imprimante, P3 calcule 4 unités CPU ; quantum = 2.
- Consigne : Produis une réponse opérationnelle pour écrire une stratégie pour éviter l’attente circulaire, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 5 - Traiter le cas limite d’un processus qui ne rend jamais une ressource
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : T-ARCH-01.
- Données : P1 demande imprimante puis fichier, P2 demande fichier puis imprimante, P3 calcule 4 unités CPU ; quantum = 2.
- Consigne : Traite le cas limite demandé pour traiter le cas limite d’un processus qui ne rend jamais une ressource et précise la convention retenue.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 6 - Justifier les quatre conditions d’interblocage
- Type : justification.
- Niveau : standard.
- Capacité officielle : T-ARCH-02A.
- Données : P1 demande imprimante puis fichier, P2 demande fichier puis imprimante, P3 calcule 4 unités CPU ; quantum = 2.
- Consigne : Justifie pourquoi la méthode utilisée pour justifier les quatre conditions d’interblocage est correcte dans ce contexte.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 7 - Repérer une famine dans un planning prioritaire
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : T-ARCH-02B.
- Données : P1 demande imprimante puis fichier, P2 demande fichier puis imprimante, P3 calcule 4 unités CPU ; quantum = 2.
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de repérer une famine dans un planning prioritaire.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 8 - Comparer ordonnancement équitable et priorité stricte
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : T-ARCH-02C.
- Données : P1 demande imprimante puis fichier, P2 demande fichier puis imprimante, P3 calcule 4 unités CPU ; quantum = 2.
- Consigne : Produis une réponse opérationnelle pour comparer ordonnancement équitable et priorité stricte, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : T-ARCH-01.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T11 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « lire un état prêt, élu, bloqué dans une table de processus » en utilisant le vocabulaire processus ordonnancement interblocage.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 2
- Capacité mobilisée : T-ARCH-02A.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T11 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « analyser un diagramme d’ordonnancement round-robin » en utilisant le vocabulaire processus ordonnancement interblocage.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 3
- Capacité mobilisée : T-ARCH-02B.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T11 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « produire la file des processus après deux quanta » en utilisant le vocabulaire processus ordonnancement interblocage.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 4
- Capacité mobilisée : T-ARCH-02C.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T11 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « écrire une stratégie pour éviter l’attente circulaire » en utilisant le vocabulaire processus ordonnancement interblocage.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 5
- Capacité mobilisée : T-ARCH-01.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T11 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « traiter le cas limite d’un processus qui ne rend jamais une ressource » en utilisant le vocabulaire processus ordonnancement interblocage.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 6
- Capacité mobilisée : T-ARCH-02A.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T11 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « justifier les quatre conditions d’interblocage » en utilisant le vocabulaire processus ordonnancement interblocage.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 7
- Capacité mobilisée : T-ARCH-02B.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T11 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « repérer une famine dans un planning prioritaire » en utilisant le vocabulaire processus ordonnancement interblocage.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 8
- Capacité mobilisée : T-ARCH-02C.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T11 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « comparer ordonnancement équitable et priorité stricte » en utilisant le vocabulaire processus ordonnancement interblocage.
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
| Fiche | T11_fiche_cours_processus_ordonnancement_interblocage.md | needs_review |
| Séance | T11-S1 | progression existante |
| Évaluation | T11_evaluation_processus_ordonnancement_interblocage.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans `/home/alaeddine/Documents/NSI/Documents_DRIVE` avant création.
- Aucun fichier Drive n'a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
