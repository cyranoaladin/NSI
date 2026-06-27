---
title: "T13 - bareme - chiffrement et HTTPS"
level: "terminale"
sequence_id: "T13"
document_type: "bareme"
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

# T13 - Barème - chiffrement et HTTPS

## TD
- 8 exercices : 1 point donnée, 1 point méthode, 1 point résultat, 1 point cas limite.

## TP
- 2 points donnée `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test`.
- 3 points tâche `protéger Ksession par asymétrique`.
- 3 points résultat `message chiffré avec Ksession`.
- 2 points cas limite `certificat expiré`.

## Évaluation question par question
- Question 1 : 4 points sur T-ARCH-04A avec résultat `message chiffré avec Ksession`.
- Question 2 : 4 points sur T-ARCH-04B avec résultat `Ksession chiffrée avec Kpub serveur`.
- Question 3 : 4 points sur T-ARCH-04A avec résultat `Autorité-Test signe serveur.example`.
- Question 4 : 4 points sur T-ARCH-04B avec résultat `HTTP sans TLS ne protège pas`.

## Critères observables
- Trace, table, valeur ou pseudo-code présent.
- Cas limite et erreur fréquente explicités.
