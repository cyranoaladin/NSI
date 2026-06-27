---
title: "T13 - evaluation - chiffrement et HTTPS"
level: "terminale"
sequence_id: "T13"
document_type: "evaluation"
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

# T13 - Évaluation - chiffrement et HTTPS

## Modalités
- Durée : 30 minutes.
- Matériel autorisé : fiche de cours.
- Capacités évaluées : T-ARCH-04A, T-ARCH-04B.

## Questions
### Question 1
- Capacité officielle : T-ARCH-04A.
- Énoncé : à partir de `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test`, protéger Ksession par asymétrique.
- Réponse attendue : message chiffré avec Ksession.
- Barème : 1 point donnée, 1 point méthode, 1 point résultat, 1 point justification sur `certificat expiré`.
### Question 2
- Capacité officielle : T-ARCH-04B.
- Énoncé : à partir de `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test`, utiliser symétrique pour données.
- Réponse attendue : Ksession chiffrée avec Kpub serveur.
- Barème : 1 point donnée, 1 point méthode, 1 point résultat, 1 point justification sur `clé publique non vérifiée`.
### Question 3
- Capacité officielle : T-ARCH-04A.
- Énoncé : à partir de `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test`, vérifier certificat.
- Réponse attendue : Autorité-Test signe serveur.example.
- Barème : 1 point donnée, 1 point méthode, 1 point résultat, 1 point justification sur `HTTP sans TLS`.
### Question 4
- Capacité officielle : T-ARCH-04B.
- Énoncé : à partir de `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test`, distinguer confidentialité et authenticité.
- Réponse attendue : HTTP sans TLS ne protège pas.
- Barème : 1 point donnée, 1 point méthode, 1 point résultat, 1 point justification sur `certificat expiré`.

## Corrigé question par question
### Corrigé question 1
- Résultat attendu : message chiffré avec Ksession.
- Critère spécifique : protéger Ksession par asymétrique et éviter `clé publique supposée secrète`.
### Corrigé question 2
- Résultat attendu : Ksession chiffrée avec Kpub serveur.
- Critère spécifique : utiliser symétrique pour données et éviter `asymétrique utilisé partout`.
### Corrigé question 3
- Résultat attendu : Autorité-Test signe serveur.example.
- Critère spécifique : vérifier certificat et éviter `certificat ignoré`.
### Corrigé question 4
- Résultat attendu : HTTP sans TLS ne protège pas.
- Critère spécifique : distinguer confidentialité et authenticité et éviter `clé publique supposée secrète`.

## Erreurs fréquentes et remédiation
- clé publique supposée secrète.
- asymétrique utilisé partout.
- certificat ignoré.

## Cas limites travaillés
- certificat expiré.
- clé publique non vérifiée.
- HTTP sans TLS.

## Critères de réussite observables
- La donnée de départ est recopiée exactement.
- La trace ou le pseudo-code conduit à `message chiffré avec Ksession`.
- Au moins un cas limite de la section précédente est décidé.



## Barème question par question
- question 1: 1 point donnée exacte, 1 point méthode liée à la capacité, 1 point résultat vérifiable, 1 point justification du cas limite.
- question 2: 1 point donnée exacte, 1 point méthode liée à la capacité, 1 point résultat vérifiable, 1 point justification du cas limite.
- question 3: 1 point donnée exacte, 1 point méthode liée à la capacité, 1 point résultat vérifiable, 1 point justification du cas limite.
- question 4: 1 point donnée exacte, 1 point méthode liée à la capacité, 1 point résultat vérifiable, 1 point justification du cas limite.

## Fiche liée
- Fiche liée : fiche de cours T13 sur `chiffrement_https`.

## Aménagement
- Version aménagée : `T13_version_amenagee_chiffrement_https.md` ; consignes découpées et barème conservé.
