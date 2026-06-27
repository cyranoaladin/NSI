---
title: "P10 - tp_papier - réseaux, protocoles et paquets"
level: "premiere"
sequence_id: "P10"
document_type: "tp_papier"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "réseaux, protocoles et paquets"
notion: "réseaux, protocoles et paquets"
private_data: false
official_program:
  capacities:
    - "P-ARCH-02A"
    - "P-ARCH-02B"
    - "P-ARCH-02C"
    - "P-ARCH-04A"
    - "P-ARCH-04B"
---

# P10 - TP - réseaux, protocoles et paquets

## Statut du TP
TP papier : ce support n attend aucune ressource Python ; le livrable est une trace écrite vérifiable.

## Donnée fournie
`src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24`

## Travail demandé
1. Préparer la donnée et nommer les champs utiles.
2. Réaliser : identifier champs de bout en bout.
3. Réaliser : distinguer MAC et IP.
4. Tester le cas limite `TTL devient 0`.
5. Produire le livrable : src=192.168.1.20 dst=172.16.0.8 TCP port 443 TTL 4.

## Barème associé
- 2 points : donnée préparée.
- 3 points : méthode principale.
- 3 points : résultat `src=192.168.1.20 dst=172.16.0.8 TCP port 443 TTL 4`.
- 2 points : cas limite `TTL devient 0`.

## Corrigé question par question
### Corrigé question 1
Résultat attendu : `src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24`.
### Corrigé question 2
Résultat attendu : src=192.168.1.20 dst=172.16.0.8 TCP port 443 TTL 4.
### Corrigé question 3
Résultat attendu : MAC change à chaque saut, IP reste de bout en bout.
### Corrigé question 4
Résultat attendu : `TTL devient 0` traité sans ambiguïté.

## Liens
- TD lié : `P10_TD_reseaux_protocoles_paquets.md`.
- Évaluation liée : `P10_evaluation_reseaux_protocoles_paquets.md`.

## Cas limites travaillés
- TTL devient 0.
- destination locale 192.168.1.34.
- ACK43 dupliqué.

## Erreurs fréquentes
- confondre MAC et IP.
- TTL pris pour une durée.
- réémettre un paquet TTL 0.

## Critères de réussite observables
- La donnée de départ est recopiée exactement.
- La trace ou le pseudo-code conduit à `src=192.168.1.20 dst=172.16.0.8 TCP port 443 TTL 4`.
- Au moins un cas limite de la section précédente est décidé.

