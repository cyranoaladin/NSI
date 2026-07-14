---
title: "T13 - cours - chiffrement et HTTPS"
level: "terminale"
sequence_id: "T13"
document_type: "cours"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "chiffrement et HTTPS"
notion: "chiffrement et HTTPS"
private_data: false
official_program:
  capacities:
    - "T-ARCH-04A"
    - "T-ARCH-04B"
---

# T13 - Cours - chiffrement et HTTPS

## Objectifs spécifiques
- Identifier les données utiles de la situation : Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test.
- Employer le vocabulaire : chiffrement symétrique, chiffrement asymétrique, clé publique, clé privée, certificat, échange de clé.
- Produire une trace, une table, une valeur ou un pseudo-code vérifiable.

## Capacités officielles
- T-ARCH-04A.
- T-ARCH-04B.

## Situation-problème
Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test

## À savoir
- chiffrement symétrique.
- chiffrement asymétrique.
- clé publique.
- clé privée.
- certificat.
- échange de clé.
- HTTPS.
- authenticité.

## Méthodes
- protéger Ksession par asymétrique.
- utiliser symétrique pour données.
- vérifier certificat.
- distinguer confidentialité et authenticité.

## Exemples corrigés
### Exemple corrigé 1
- Donnée : `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test`.
- Méthode : protéger Ksession par asymétrique.
- Résultat attendu : message chiffré avec Ksession.
- Contrôle : capacité T-ARCH-04A et cas limite `certificat expiré`.
### Exemple corrigé 2
- Donnée : `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test`.
- Méthode : utiliser symétrique pour données.
- Résultat attendu : Ksession chiffrée avec Kpub serveur.
- Contrôle : capacité T-ARCH-04B et cas limite `clé publique non vérifiée`.
### Exemple corrigé 3
- Donnée : `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test`.
- Méthode : vérifier certificat.
- Résultat attendu : Autorité-Test signe serveur.example.
- Contrôle : capacité T-ARCH-04A et cas limite `HTTP sans TLS`.
### Exemple corrigé 4
- Donnée : `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test`.
- Méthode : distinguer confidentialité et authenticité.
- Résultat attendu : HTTP sans TLS ne protège pas.
- Contrôle : capacité T-ARCH-04B et cas limite `certificat expiré`.

## Cas limites
- certificat expiré.
- clé publique non vérifiée.
- HTTP sans TLS.

## Erreurs fréquentes
- clé publique supposée secrète.
- asymétrique utilisé partout.
- certificat ignoré.

## Exercices intégrés
1. Identifier les données utiles dans `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test`.
2. Appliquer : protéger Ksession par asymétrique.
3. Appliquer : utiliser symétrique pour données.
4. Décider le cas limite `certificat expiré`.

## Critères de réussite observables
- Une capacité parmi T-ARCH-04A, T-ARCH-04B est citée et utilisée.
- Le résultat formulé explicite la protection des données applicatives sans confondre les rôles des clés.
- Le cas limite `clé publique non vérifiée` est tranché.

## Lien avec la progression
- Séance : T13-S1 à T13-S4.
- TD : `T13_TD_chiffrement_https.md`.
- TP : `T13_tp_chiffrement_https.md`.
- Évaluation : `T13_evaluation_chiffrement_https.md`.

## Renforcement explicatif ciblé

Ce cours doit être lu comme une progression sur chiffrement et HTTPS. La notion ne se réduit pas à une liste de mots : on part d'une situation observable, on nomme les objets manipulés, puis on applique une méthode vérifiable sur un cas limité avant de généraliser.

### Savoir disciplinaire
- Vocabulaire à maîtriser : clé publique, clé privée, certificat, TLS, port 443, empreinte, autorité de certification.
- Capacités reliées : T-ARCH-04A, T-ARCH-04B.
- Le savoir attendu consiste à expliquer le rôle de chaque objet avant de l'utiliser dans un exercice.

### Savoir-faire et méthodes opérationnelles
- expliquer le rôle du certificat serveur.
- distinguer chiffrement symétrique et asymétrique.
- repérer le port 443 dans un échange HTTPS.

### Erreurs fréquentes spécifiques
- Un élève peut confondre hachage et chiffrement ; la correction consiste à reprendre la définition puis à refaire la trace sur un exemple minimal.
- Un élève peut faire transiter une clé privée ; la correction consiste à isoler le cas limite avant de recommencer le calcul ou le raisonnement.
- Un élève peut croire que HTTPS cache le nom du site à tous les niveaux ; la correction consiste à vérifier le résultat avec une donnée différente.

### Cas limites à contrôler
- Cas minimal : une donnée vide, un seul élément, une route absente ou une structure sans enfant selon la notion.
- Cas ambigu : doublon, égalité, absence de correspondance ou choix local non optimal.

### Synthèse savoir / savoir-faire / méthode
- Savoir : définir précisément les objets de chiffrement et HTTPS.
- Savoir-faire : appliquer une méthode contrôlable à une donnée explicite.
- Méthode : annoncer la donnée, exécuter les étapes dans l'ordre, puis vérifier le résultat par un cas limite.
