---
title: "T13 - TD - chiffrement HTTPS"
level: "terminale"
sequence_id: "T13"
document_type: "td"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Sécurité"
notion: "chiffrement HTTPS"
objectifs:
  - "travailler chiffrement HTTPS sur des données explicites"
  - "produire une réponse justifiée et contrôlée"
  - "identifier les cas limites"
  - "corriger les erreurs fréquentes du chapitre"
private_data: false
official_program:
  capacities:
    - "T-ARCH-04A"
    - "T-ARCH-04B"
---
# T13 - TD - chiffrement HTTPS

## Objectifs
- O1 : appliquer les méthodes de la fiche à une donnée différente.
- O2 : distinguer lecture d'information, production et justification.
- O3 : traiter au moins un cas limite sans le masquer.
- O4 : préparer une correction exploitable en séance.

## Capacités officielles
- T-ARCH-04A
- T-ARCH-04B

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T13/T13_fiche_cours_chiffrement_https.md`.
- Séance liée : `T13-S1` dans la progression annuelle.
- Statut : support créé en `needs_review`, non validé pédagogiquement et non publiable.

## Situation de travail
un navigateur établit une connexion HTTPS avec un serveur et doit obtenir une clé de session sans la transmettre en clair.

## Données de référence
Client C, serveur S, certificat de S, clé publique KpubS, clé privée KprivS, clé de session Ks, message m = "GET /note".

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée et vocabulaire.
- Standard : exercices 3 à 6, production écrite avec contrôle.
- Approfondissement : exercices 7 et 8, comparaison de démarches et généralisation.

## Exercices
### Exercice 1 - Lire le rôle des clés publique, privée et de session
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-ARCH-04A.
- Données : Client C, serveur S, certificat de S, clé publique KpubS, clé privée KprivS, clé de session Ks, message m = "GET /note".
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de lire le rôle des clés publique, privée et de session.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 2 - Analyser une étape de vérification de certificat
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-ARCH-04B.
- Données : Client C, serveur S, certificat de S, clé publique KpubS, clé privée KprivS, clé de session Ks, message m = "GET /note".
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de analyser une étape de vérification de certificat.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 3 - Produire un schéma d’échange de clé de session
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-ARCH-04A.
- Données : Client C, serveur S, certificat de S, clé publique KpubS, clé privée KprivS, clé de session Ks, message m = "GET /note".
- Consigne : Produis une réponse opérationnelle pour produire un schéma d’échange de clé de session, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 4 - Écrire ce qui est chiffré en symétrique après négociation
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-ARCH-04B.
- Données : Client C, serveur S, certificat de S, clé publique KpubS, clé privée KprivS, clé de session Ks, message m = "GET /note".
- Consigne : Produis une réponse opérationnelle pour écrire ce qui est chiffré en symétrique après négociation, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 5 - Traiter le cas limite certificat expiré ou nom de domaine différent
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : T-ARCH-04A.
- Données : Client C, serveur S, certificat de S, clé publique KpubS, clé privée KprivS, clé de session Ks, message m = "GET /note".
- Consigne : Traite le cas limite demandé pour traiter le cas limite certificat expiré ou nom de domaine différent et précise la convention retenue.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 6 - Justifier pourquoi le chiffrement asymétrique seul n’est pas utilisé pour tout le flux
- Type : justification.
- Niveau : standard.
- Capacité officielle : T-ARCH-04B.
- Données : Client C, serveur S, certificat de S, clé publique KpubS, clé privée KprivS, clé de session Ks, message m = "GET /note".
- Consigne : Justifie pourquoi la méthode utilisée pour justifier pourquoi le chiffrement asymétrique seul n’est pas utilisé pour tout le flux est correcte dans ce contexte.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 7 - Repérer une attaque homme du milieu sans vérification de certificat
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : T-ARCH-04A.
- Données : Client C, serveur S, certificat de S, clé publique KpubS, clé privée KprivS, clé de session Ks, message m = "GET /note".
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de repérer une attaque homme du milieu sans vérification de certificat.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 8 - Comparer confidentialité, authentification et intégrité
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : T-ARCH-04B.
- Données : Client C, serveur S, certificat de S, clé publique KpubS, clé privée KprivS, clé de session Ks, message m = "GET /note".
- Consigne : Produis une réponse opérationnelle pour comparer confidentialité, authentification et intégrité, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : T-ARCH-04A.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T13 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « lire le rôle des clés publique, privée et de session » en utilisant le vocabulaire chiffrement HTTPS.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 2
- Capacité mobilisée : T-ARCH-04B.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T13 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « analyser une étape de vérification de certificat » en utilisant le vocabulaire chiffrement HTTPS.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 3
- Capacité mobilisée : T-ARCH-04A.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T13 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « produire un schéma d’échange de clé de session » en utilisant le vocabulaire chiffrement HTTPS.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 4
- Capacité mobilisée : T-ARCH-04B.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T13 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « écrire ce qui est chiffré en symétrique après négociation » en utilisant le vocabulaire chiffrement HTTPS.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 5
- Capacité mobilisée : T-ARCH-04A.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T13 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « traiter le cas limite certificat expiré ou nom de domaine différent » en utilisant le vocabulaire chiffrement HTTPS.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 6
- Capacité mobilisée : T-ARCH-04B.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T13 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « justifier pourquoi le chiffrement asymétrique seul n’est pas utilisé pour tout le flux » en utilisant le vocabulaire chiffrement HTTPS.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 7
- Capacité mobilisée : T-ARCH-04A.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T13 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « repérer une attaque homme du milieu sans vérification de certificat » en utilisant le vocabulaire chiffrement HTTPS.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 8
- Capacité mobilisée : T-ARCH-04B.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T13 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « comparer confidentialité, authentification et intégrité » en utilisant le vocabulaire chiffrement HTTPS.
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
| Fiche | T13_fiche_cours_chiffrement_https.md | needs_review |
| Séance | T13-S1 | progression existante |
| Évaluation | T13_evaluation_chiffrement_https.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans `/home/alaeddine/Documents/NSI/Documents_DRIVE` avant création.
- Aucun fichier Drive n'a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
