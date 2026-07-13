---
title: "T13 - trace - chiffrement et HTTPS"
level: "terminale"
sequence_id: "T13"
document_type: "trace"
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

# T13 - Trace - chiffrement et HTTPS

## Trace courte
- Donnée : `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test`.
- Vocabulaire : chiffrement symétrique, chiffrement asymétrique, clé publique, clé privée, certificat.
- Étape 1 : protéger Ksession par asymétrique.
- Étape 2 : utiliser symétrique pour données.
- Résultat de référence : à déterminer (quel type de chiffrement protège les données échangées ?).

## Cas limites à mémoriser
- certificat expiré.
- clé publique non vérifiée.
- HTTP sans TLS.

## Erreurs fréquentes
- clé publique supposée secrète.
- asymétrique utilisé partout.
- certificat ignoré.

## Critères de réussite observables
- Capacité : T-ARCH-04A.
- Résultat final : vérifier que la clé de session est protégée avant transmission.
- Cas limite : certificat expiré.

## Repères enseignant — résultats attendus
- Résultat de référence : message chiffré avec Ksession.
- Résultat final : Ksession chiffrée avec Kpub serveur.
