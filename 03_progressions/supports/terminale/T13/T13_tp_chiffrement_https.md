---
title: "T13 - tp_papier - chiffrement et HTTPS"
level: "terminale"
sequence_id: "T13"
document_type: "tp_papier"
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

# T13 - TP - chiffrement et HTTPS

## Statut du TP
TP papier : ce support n attend aucune ressource Python ; le livrable est une trace écrite vérifiable.

## Donnée fournie
`Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test`

## Travail demandé
1. Préparer la donnée et nommer les champs utiles.
2. Réaliser : protéger Ksession par asymétrique.
3. Réaliser : utiliser symétrique pour données.
4. Tester le cas limite `certificat expiré`.
5. Produire une trace qui explicite quelle clé protège les données applicatives et pourquoi.

## Barème associé
- 2 points : donnée préparée.
- 3 points : méthode principale.
- 3 points : justification vérifiable du chiffrement symétrique des données applicatives.
- 2 points : cas limite `certificat expiré`.

## Corrigé question par question
### Corrigé question 1
Résultat attendu : `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test`.
### Corrigé question 2
Résultat attendu : message applicatif chiffré avec `Ksession`, par exemple `C = Enc_Ksession("GET /")`.
### Corrigé question 3
Résultat attendu : `Ksession` est chiffrée avec `Kpub_serveur`, puis seul le serveur la déchiffre avec `Kpriv_serveur`.
### Corrigé question 4
Résultat attendu : `certificat expiré` traité sans ambiguïté.

## Liens
- TD lié : `T13_TD_chiffrement_https.md`.
- Évaluation liée : `T13_evaluation_chiffrement_https.md`.

## Cas limites travaillés
- certificat expiré.
- clé publique non vérifiée.
- HTTP sans TLS.

## Erreurs fréquentes
- clé publique supposée secrète.
- asymétrique utilisé partout.
- certificat ignoré.

## Critères de réussite observables
- La donnée de départ est recopiée exactement.
- La trace ou le pseudo-code identifie la clé qui protège les données applicatives.
- Au moins un cas limite de la section précédente est décidé.
