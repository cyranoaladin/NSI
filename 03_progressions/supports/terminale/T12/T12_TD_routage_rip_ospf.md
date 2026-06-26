---
title: "T12 - TD - routage RIP OSPF"
level: "terminale"
sequence_id: "T12"
document_type: "td"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Réseaux"
notion: "routage RIP OSPF"
objectifs:
  - "travailler routage RIP OSPF sur des données explicites"
  - "produire une réponse justifiée et contrôlée"
  - "identifier les cas limites"
  - "corriger les erreurs fréquentes du chapitre"
private_data: false
official_program:
  capacities:
    - "T-ARCH-03"
---
# T12 - TD - routage RIP OSPF

## Objectifs
- O1 : appliquer les méthodes de la fiche à une donnée différente.
- O2 : distinguer lecture d'information, production et justification.
- O3 : traiter au moins un cas limite sans le masquer.
- O4 : préparer une correction exploitable en séance.

## Capacités officielles
- T-ARCH-03

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T12/T12_fiche_cours_routage_rip_ospf.md`.
- Séance liée : `T12-S1` dans la progression annuelle.
- Statut : support créé en `needs_review`, non validé pédagogiquement et non publiable.

## Situation de travail
quatre routeurs R1, R2, R3, R4 doivent choisir une route entre un protocole à vecteur de distance et un protocole à état de liens.

## Données de référence
Liens : R1-R2 coût 1, R2-R4 coût 5, R1-R3 coût 2, R3-R4 coût 2, R2-R3 coût 1 ; destination réseau D derrière R4.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée et vocabulaire.
- Standard : exercices 3 à 6, production écrite avec contrôle.
- Approfondissement : exercices 7 et 8, comparaison de démarches et généralisation.

## Exercices
### Exercice 1 - Lire une table de routage locale et repérer le prochain saut
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-ARCH-03.
- Données : Liens : R1-R2 coût 1, R2-R4 coût 5, R1-R3 coût 2, R3-R4 coût 2, R2-R3 coût 1 ; destination réseau D derrière R4.
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de lire une table de routage locale et repérer le prochain saut.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 2 - Analyser une annonce rip en nombre de sauts
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-ARCH-03.
- Données : Liens : R1-R2 coût 1, R2-R4 coût 5, R1-R3 coût 2, R3-R4 coût 2, R2-R3 coût 1 ; destination réseau D derrière R4.
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de analyser une annonce RIP en nombre de sauts.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 3 - Produire le meilleur chemin par coût total
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-ARCH-03.
- Données : Liens : R1-R2 coût 1, R2-R4 coût 5, R1-R3 coût 2, R3-R4 coût 2, R2-R3 coût 1 ; destination réseau D derrière R4.
- Consigne : Produis une réponse opérationnelle pour produire le meilleur chemin par coût total, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 4 - Écrire une mise à jour de table après panne r2-r4
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-ARCH-03.
- Données : Liens : R1-R2 coût 1, R2-R4 coût 5, R1-R3 coût 2, R3-R4 coût 2, R2-R3 coût 1 ; destination réseau D derrière R4.
- Consigne : Produis une réponse opérationnelle pour écrire une mise à jour de table après panne R2-R4, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 5 - Traiter le cas limite d’une boucle de routage temporaire
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : T-ARCH-03.
- Données : Liens : R1-R2 coût 1, R2-R4 coût 5, R1-R3 coût 2, R3-R4 coût 2, R2-R3 coût 1 ; destination réseau D derrière R4.
- Consigne : Traite le cas limite demandé pour traiter le cas limite d’une boucle de routage temporaire et précise la convention retenue.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 6 - Justifier la différence rip nombre de sauts et ospf coût
- Type : justification.
- Niveau : standard.
- Capacité officielle : T-ARCH-03.
- Données : Liens : R1-R2 coût 1, R2-R4 coût 5, R1-R3 coût 2, R3-R4 coût 2, R2-R3 coût 1 ; destination réseau D derrière R4.
- Consigne : Justifie pourquoi la méthode utilisée pour justifier la différence RIP nombre de sauts et OSPF coût est correcte dans ce contexte.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 7 - Appliquer dijkstra sur le graphe r1 à r4
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : T-ARCH-03.
- Données : Liens : R1-R2 coût 1, R2-R4 coût 5, R1-R3 coût 2, R3-R4 coût 2, R2-R3 coût 1 ; destination réseau D derrière R4.
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de appliquer Dijkstra sur le graphe R1 à R4.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 8 - Comparer convergence lente et état de liens diffusé
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : T-ARCH-03.
- Données : Liens : R1-R2 coût 1, R2-R4 coût 5, R1-R3 coût 2, R3-R4 coût 2, R2-R3 coût 1 ; destination réseau D derrière R4.
- Consigne : Produis une réponse opérationnelle pour comparer convergence lente et état de liens diffusé, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : T-ARCH-03.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T12 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « lire une table de routage locale et repérer le prochain saut » en utilisant le vocabulaire routage RIP OSPF.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 2
- Capacité mobilisée : T-ARCH-03.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T12 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « analyser une annonce RIP en nombre de sauts » en utilisant le vocabulaire routage RIP OSPF.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 3
- Capacité mobilisée : T-ARCH-03.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T12 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « produire le meilleur chemin par coût total » en utilisant le vocabulaire routage RIP OSPF.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 4
- Capacité mobilisée : T-ARCH-03.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T12 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « écrire une mise à jour de table après panne R2-R4 » en utilisant le vocabulaire routage RIP OSPF.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 5
- Capacité mobilisée : T-ARCH-03.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T12 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « traiter le cas limite d’une boucle de routage temporaire » en utilisant le vocabulaire routage RIP OSPF.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 6
- Capacité mobilisée : T-ARCH-03.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T12 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « justifier la différence RIP nombre de sauts et OSPF coût » en utilisant le vocabulaire routage RIP OSPF.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 7
- Capacité mobilisée : T-ARCH-03.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T12 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « appliquer Dijkstra sur le graphe R1 à R4 » en utilisant le vocabulaire routage RIP OSPF.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 8
- Capacité mobilisée : T-ARCH-03.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T12 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « comparer convergence lente et état de liens diffusé » en utilisant le vocabulaire routage RIP OSPF.
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
| Fiche | T12_fiche_cours_routage_rip_ospf.md | needs_review |
| Séance | T12-S1 | progression existante |
| Évaluation | T12_evaluation_routage_rip_ospf.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans `/home/alaeddine/Documents/NSI/Documents_DRIVE` avant création.
- Aucun fichier Drive n'a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
