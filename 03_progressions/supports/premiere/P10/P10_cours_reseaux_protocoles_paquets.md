---
title: "P10 - cours - réseaux, protocoles et paquets"
level: "premiere"
sequence_id: "P10"
document_type: "cours"
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

# P10 - Cours - réseaux, protocoles et paquets

## Objectifs spécifiques
- Identifier les données utiles de la situation : src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24.
- Employer le vocabulaire : IP source, IP destination, MAC locale, TCP, port 443, TTL.
- Produire une trace, une table, une valeur ou un pseudo-code vérifiable.

## Capacités officielles
- P-ARCH-02A.
- P-ARCH-02B.
- P-ARCH-02C.
- P-ARCH-04A.
- P-ARCH-04B.

## Situation-problème
src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24

## À savoir
- IP source.
- IP destination.
- MAC locale.
- TCP.
- port 443.
- TTL.
- bit alterné.
- passerelle.

## Méthodes
- identifier champs de bout en bout.
- distinguer MAC et IP.
- dérouler M0 ACK0 M1 perdu retransmission ACK1.
- décrémenter TTL avant retransmission.

## Exemples corrigés
### Exemple corrigé 1
- Donnée : `src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24`.
- Méthode : identifier champs de bout en bout.
- Résultat attendu : src=192.168.1.20 dst=172.16.0.8 TCP port 443 TTL 4.
- Contrôle : capacité P-ARCH-02A et cas limite `TTL devient 0`.
### Exemple corrigé 2
- Donnée : `src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24`.
- Méthode : distinguer MAC et IP.
- Résultat attendu : MAC change à chaque saut, IP reste de bout en bout.
- Décision locale/passerelle : si `dst` appartient au préfixe `192.168.1.0/24`, l’hôte résout la MAC locale ; sinon il envoie le paquet à la passerelle.
- Contrôle : capacité P-ARCH-02B et cas limite `destination locale 192.168.1.34`.
### Exemple corrigé 3
- Donnée : `src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24`.
- Méthode : dérouler M0 ACK0 M1 perdu retransmission ACK1.
- Résultat attendu : M0 -> ACK0 -> M1 perdu -> M1 retransmis -> ACK1.
- Contrôle : capacité P-ARCH-02C et cas limite `ACK43 dupliqué`.
### Exemple corrigé 4
- Donnée : `src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24`.
- Méthode : décrémenter TTL avant retransmission.
- Résultat attendu : TTL=1 devient 0 et le paquet est détruit.
- Contrôle : capacité P-ARCH-04A et cas limite `TTL devient 0`.

## Cas limites
- TTL devient 0.
- destination locale 192.168.1.34.
- ACK43 dupliqué.

## Erreurs fréquentes
- confondre MAC et IP.
- TTL pris pour une durée.
- réémettre un paquet TTL 0.

## Exercices intégrés
1. Identifier les données utiles dans `src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24`.
2. Appliquer : identifier champs de bout en bout.
3. Appliquer : distinguer MAC et IP.
4. Décider le cas limite `TTL devient 0`.

## Critères de réussite observables
- Une capacité parmi P-ARCH-02A, P-ARCH-02B, P-ARCH-02C, P-ARCH-04A, P-ARCH-04B est citée et utilisée.
- Le résultat attendu est explicite : src=192.168.1.20 dst=172.16.0.8 TCP port 443 TTL 4.
- Le cas limite `destination locale 192.168.1.34` est tranché.

## Lien avec la progression
- Séance : P10-S1 à P10-S4.
- TD : `P10_TD_reseaux_protocoles_paquets.md`.
- TP : `P10_tp_reseaux_protocoles_paquets.md`.
- Évaluation : `P10_evaluation_reseaux_protocoles_paquets.md`.

## Renforcement explicatif ciblé

Ce cours doit être lu comme une progression sur réseaux, protocoles et paquets. La notion ne se réduit pas à une liste de mots : on part d'une situation observable, on nomme les objets manipulés, puis on applique une méthode vérifiable sur un cas limité avant de généraliser.

### Savoir disciplinaire
- Vocabulaire à maîtriser : adresse IP, adresse MAC, passerelle, TTL, paquet, protocole, port, routage.
- Capacités reliées : P-ARCH-02A, P-ARCH-02B, P-ARCH-02C, P-ARCH-04A, P-ARCH-04B.
- Le savoir attendu consiste à expliquer le rôle de chaque objet avant de l'utiliser dans un exercice.

### Savoir-faire et méthodes opérationnelles
- décrémenter le TTL à chaque routeur traversé.
- choisir la passerelle quand l’adresse de destination n’est pas locale.
- distinguer IP de bout en bout et MAC locale.

### Erreurs fréquentes spécifiques
- Un élève peut confondre MAC et IP ; la correction consiste à reprendre la définition puis à refaire la trace sur un exemple minimal.
- Un élève peut oublier de supprimer un paquet dont le TTL devient 0 ; la correction consiste à isoler le cas limite avant de recommencer le calcul ou le raisonnement.
- Un élève peut choisir une route sans comparer les préfixes ; la correction consiste à vérifier le résultat avec une donnée différente.

### Cas limites à contrôler
- Cas minimal : une donnée vide, un seul élément, une route absente ou une structure sans enfant selon la notion.
- Cas ambigu : doublon, égalité, absence de correspondance ou choix local non optimal.

### Synthèse savoir / savoir-faire / méthode
- Savoir : définir précisément les objets de réseaux, protocoles et paquets.
- Savoir-faire : appliquer une méthode contrôlable à une donnée explicite.
- Méthode : annoncer la donnée, exécuter les étapes dans l'ordre, puis vérifier le résultat par un cas limite.
