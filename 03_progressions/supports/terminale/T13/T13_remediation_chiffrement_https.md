---
title: "T13 - remediation - chiffrement et HTTPS"
level: "terminale"
sequence_id: "T13"
document_type: "remediation"
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

# T13 - Remédiation - chiffrement et HTTPS

## Diagnostic
- clé publique supposée secrète.
- asymétrique utilisé partout.
- certificat ignoré.

## Activités correctives
1. Annoter `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test`.
2. Refaire la tâche `protéger Ksession par asymétrique` et comparer avec `message chiffré avec Ksession`.
3. Traiter le cas limite `certificat expiré`.
4. Relier la réponse à T-ARCH-04A.

## Critères de sortie
- Donnée exacte.
- Résultat final explicite.
- Cas limite décidé.
