---
title: "T13 - corrige - chiffrement et HTTPS"
level: "terminale"
sequence_id: "T13"
document_type: "corrige"
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

# T13 - Corrigé - chiffrement et HTTPS

## Corrigé du TD
### Exercice 1
- Réponse attendue : message chiffré avec Ksession.
- Méthode : protéger Ksession par asymétrique.
- Cas limite : certificat expiré.
### Exercice 2
- Réponse attendue : Ksession chiffrée avec Kpub serveur.
- Méthode : utiliser symétrique pour données.
- Cas limite : clé publique non vérifiée.
### Exercice 3
- Réponse attendue : Autorité-Test signe serveur.example.
- Méthode : vérifier certificat.
- Cas limite : HTTP sans TLS.
### Exercice 4
- Réponse attendue : HTTP sans TLS ne protège pas.
- Méthode : distinguer confidentialité et authenticité.
- Cas limite : certificat expiré.
### Exercice 5
- Réponse attendue : message chiffré avec Ksession.
- Méthode : protéger Ksession par asymétrique.
- Cas limite : clé publique non vérifiée.
### Exercice 6
- Réponse attendue : Ksession chiffrée avec Kpub serveur.
- Méthode : utiliser symétrique pour données.
- Cas limite : HTTP sans TLS.
### Exercice 7
- Réponse attendue : Autorité-Test signe serveur.example.
- Méthode : vérifier certificat.
- Cas limite : certificat expiré.
### Exercice 8
- Réponse attendue : HTTP sans TLS ne protège pas.
- Méthode : distinguer confidentialité et authenticité.
- Cas limite : clé publique non vérifiée.

## Corrigé du TP
- Donnée : `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test`.
- Résultat principal : message chiffré avec Ksession.
- Résultat secondaire : Ksession chiffrée avec Kpub serveur.

## Corrigé de l évaluation
- Question 1 : message chiffré avec Ksession.
- Question 2 : Ksession chiffrée avec Kpub serveur.
- Question 3 : Autorité-Test signe serveur.example.
- Question 4 : HTTP sans TLS ne protège pas.
