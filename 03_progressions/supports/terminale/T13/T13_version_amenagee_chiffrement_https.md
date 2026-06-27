---
title: "T13 - version_amenagee - chiffrement et HTTPS"
level: "terminale"
sequence_id: "T13"
document_type: "version_amenagee"
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

# T13 - Version aménagée - chiffrement et HTTPS

## Aides intégrées
- Donnée fournie : `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test`.
- Mots utiles : chiffrement symétrique, chiffrement asymétrique, clé publique, clé privée, certificat.
- Méthode guidée : protéger Ksession par asymétrique puis utiliser symétrique pour données.

## Exercice guidé
1. Recopier la donnée utile.
2. Choisir la capacité : T-ARCH-04A ou T-ARCH-04B.
3. Compléter le résultat : message chiffré avec Ksession.
4. Cocher le cas limite : certificat expiré.

## Réponses rapides
- Réponse 1 : message chiffré avec Ksession.
- Réponse 2 : Ksession chiffrée avec Kpub serveur.
- Réponse 3 : Autorité-Test signe serveur.example.
