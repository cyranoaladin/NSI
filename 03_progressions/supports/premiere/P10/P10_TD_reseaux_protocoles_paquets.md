---
title: "P10 - td - réseaux, protocoles et paquets"
level: "premiere"
sequence_id: "P10"
document_type: "td"
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

# P10 - TD - réseaux, protocoles et paquets

## Objectifs
- Travailler IP source, IP destination, MAC locale, TCP, port 443.
- Produire huit réponses vérifiables avec données explicites.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2.
- Standard : exercices 3 à 6.
- Approfondissement : exercices 7 et 8.

## Exercices
### Exercice 1
- Type : lecture/analyse.
- Capacité officielle : P-ARCH-02A.
- Données : `src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24`. ; jeu_exercice=alpha
- Consigne : identifier champs de bout en bout ; traiter aussi `TTL devient 0` si nécessaire.
- Réponse attendue : src=192.168.1.20 dst=172.16.0.8 TCP port 443 TTL 4.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `TTL devient 0`.
### Exercice 2
- Type : production/écriture.
- Capacité officielle : P-ARCH-02B.
- Données : `src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24`. ; jeu_exercice=beta
- Consigne : distinguer MAC et IP ; traiter aussi `destination locale 192.168.1.34` si nécessaire.
- Réponse attendue : MAC change à chaque saut, IP reste de bout en bout.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `destination locale 192.168.1.34`.
### Exercice 3
- Type : production/écriture.
- Capacité officielle : P-ARCH-02C.
- Données : `src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24`. ; jeu_exercice=gamma
- Consigne : dérouler M0 ACK0 M1 perdu retransmission ACK1 ; traiter aussi `ACK43 dupliqué` si nécessaire.
- Réponse attendue : M0 -> ACK0 -> M1 perdu -> M1 retransmis -> ACK1.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `ACK43 dupliqué`.
### Exercice 4
- Type : cas limite.
- Capacité officielle : P-ARCH-04A.
- Données : `src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24`. ; jeu_exercice=delta
- Consigne : décrémenter TTL avant retransmission ; traiter aussi `TTL devient 0` si nécessaire.
- Réponse attendue : TTL=1 devient 0 et le paquet est détruit.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `TTL devient 0`.
### Exercice 5
- Type : justification.
- Capacité officielle : P-ARCH-04B.
- Données : `src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24`. ; jeu_exercice=epsilon
- Consigne : identifier champs de bout en bout ; traiter aussi `destination locale 192.168.1.34` si nécessaire.
- Réponse attendue : src=192.168.1.20 dst=172.16.0.8 TCP port 443 TTL 4.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `destination locale 192.168.1.34`.
### Exercice 6
- Type : lecture/analyse.
- Capacité officielle : P-ARCH-02A.
- Données : `src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24`. ; jeu_exercice=zeta
- Consigne : distinguer MAC et IP ; traiter aussi `ACK43 dupliqué` si nécessaire.
- Réponse attendue : MAC change à chaque saut, IP reste de bout en bout.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `ACK43 dupliqué`.
### Exercice 7
- Type : production/écriture.
- Capacité officielle : P-ARCH-02B.
- Données : `src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24`. ; jeu_exercice=eta
- Consigne : dérouler M0 ACK0 M1 perdu retransmission ACK1 ; traiter aussi `TTL devient 0` si nécessaire.
- Réponse attendue : M0 -> ACK0 -> M1 perdu -> M1 retransmis -> ACK1.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `TTL devient 0`.
### Exercice 8
- Type : justification.
- Capacité officielle : P-ARCH-02C.
- Données : `src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24`. ; jeu_exercice=theta
- Consigne : décrémenter TTL avant retransmission ; traiter aussi `destination locale 192.168.1.34` si nécessaire.
- Réponse attendue : TTL=1 devient 0 et le paquet est détruit.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `destination locale 192.168.1.34`.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : P-ARCH-02A.
- Résultat attendu : src=192.168.1.20 dst=172.16.0.8 TCP port 443 TTL 4.
- Justification : la tâche `identifier champs de bout en bout` s applique à `src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24` ; erreur évitée : confondre MAC et IP.
- Donnée utilisée alpha dans P10 TD reseaux protocoles paquets : cas alpha de l exercice 1 avec les valeurs indiquées dans l énoncé.
- Méthode alpha dans P10 TD reseaux protocoles paquets : trace courte, pseudo-code local `if cas_alpha: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat alpha dans P10 TD reseaux protocoles paquets : sortie vérifiable de l exercice 1, reliée à la capacité officielle du bloc.
- Contrôle alpha dans P10 TD reseaux protocoles paquets : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 2
- Capacité mobilisée : P-ARCH-02B.
- Résultat attendu : MAC change à chaque saut, IP reste de bout en bout.
- Justification : la tâche `distinguer MAC et IP` s applique à `src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24` ; erreur évitée : TTL pris pour une durée.
- Donnée utilisée beta dans P10 TD reseaux protocoles paquets : cas beta de l exercice 2 avec les valeurs indiquées dans l énoncé.
- Méthode beta dans P10 TD reseaux protocoles paquets : trace courte, pseudo-code local `if cas_beta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat beta dans P10 TD reseaux protocoles paquets : sortie vérifiable de l exercice 2, reliée à la capacité officielle du bloc.
- Contrôle beta dans P10 TD reseaux protocoles paquets : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 3
- Capacité mobilisée : P-ARCH-02C.
- Résultat attendu : M0 -> ACK0 -> M1 perdu -> M1 retransmis -> ACK1.
- Justification : la tâche `dérouler M0 ACK0 M1 perdu retransmission ACK1` s applique à `src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24` ; erreur évitée : réémettre un paquet TTL 0.
- Donnée utilisée gamma dans P10 TD reseaux protocoles paquets : cas gamma de l exercice 3 avec les valeurs indiquées dans l énoncé.
- Méthode gamma dans P10 TD reseaux protocoles paquets : trace courte, pseudo-code local `if cas_gamma: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat gamma dans P10 TD reseaux protocoles paquets : sortie vérifiable de l exercice 3, reliée à la capacité officielle du bloc.
- Contrôle gamma dans P10 TD reseaux protocoles paquets : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 4
- Capacité mobilisée : P-ARCH-04A.
- Résultat attendu : TTL=1 devient 0 et le paquet est détruit.
- Justification : la tâche `décrémenter TTL avant retransmission` s applique à `src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24` ; erreur évitée : confondre MAC et IP.
- Donnée utilisée delta dans P10 TD reseaux protocoles paquets : cas delta de l exercice 4 avec les valeurs indiquées dans l énoncé.
- Méthode delta dans P10 TD reseaux protocoles paquets : trace courte, pseudo-code local `if cas_delta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat delta dans P10 TD reseaux protocoles paquets : sortie vérifiable de l exercice 4, reliée à la capacité officielle du bloc.
- Contrôle delta dans P10 TD reseaux protocoles paquets : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 5
- Capacité mobilisée : P-ARCH-04B.
- Résultat attendu : src=192.168.1.20 dst=172.16.0.8 TCP port 443 TTL 4.
- Justification : la tâche `identifier champs de bout en bout` s applique à `src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24` ; erreur évitée : TTL pris pour une durée.
- Donnée utilisée epsilon dans P10 TD reseaux protocoles paquets : cas epsilon de l exercice 5 avec les valeurs indiquées dans l énoncé.
- Méthode epsilon dans P10 TD reseaux protocoles paquets : trace courte, pseudo-code local `if cas_epsilon: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat epsilon dans P10 TD reseaux protocoles paquets : sortie vérifiable de l exercice 5, reliée à la capacité officielle du bloc.
- Contrôle epsilon dans P10 TD reseaux protocoles paquets : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 6
- Capacité mobilisée : P-ARCH-02A.
- Résultat attendu : MAC change à chaque saut, IP reste de bout en bout.
- Justification : la tâche `distinguer MAC et IP` s applique à `src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24` ; erreur évitée : réémettre un paquet TTL 0.
- Donnée utilisée zeta dans P10 TD reseaux protocoles paquets : cas zeta de l exercice 6 avec les valeurs indiquées dans l énoncé.
- Méthode zeta dans P10 TD reseaux protocoles paquets : trace courte, pseudo-code local `if cas_zeta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat zeta dans P10 TD reseaux protocoles paquets : sortie vérifiable de l exercice 6, reliée à la capacité officielle du bloc.
- Contrôle zeta dans P10 TD reseaux protocoles paquets : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 7
- Capacité mobilisée : P-ARCH-02B.
- Résultat attendu : M0 -> ACK0 -> M1 perdu -> M1 retransmis -> ACK1.
- Justification : la tâche `dérouler M0 ACK0 M1 perdu retransmission ACK1` s applique à `src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24` ; erreur évitée : confondre MAC et IP.
- Donnée utilisée eta dans P10 TD reseaux protocoles paquets : cas eta de l exercice 7 avec les valeurs indiquées dans l énoncé.
- Méthode eta dans P10 TD reseaux protocoles paquets : trace courte, pseudo-code local `if cas_eta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat eta dans P10 TD reseaux protocoles paquets : sortie vérifiable de l exercice 7, reliée à la capacité officielle du bloc.
- Contrôle eta dans P10 TD reseaux protocoles paquets : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 8
- Capacité mobilisée : P-ARCH-02C.
- Résultat attendu : TTL=1 devient 0 et le paquet est détruit.
- Justification : la tâche `décrémenter TTL avant retransmission` s applique à `src=192.168.1.20, dst=172.16.0.8, TCP, port dst=443, TTL=4, LAN 192.168.1.0/24` ; erreur évitée : TTL pris pour une durée.
- Donnée utilisée theta dans P10 TD reseaux protocoles paquets : cas theta de l exercice 8 avec les valeurs indiquées dans l énoncé.
- Méthode theta dans P10 TD reseaux protocoles paquets : trace courte, pseudo-code local `if cas_theta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat theta dans P10 TD reseaux protocoles paquets : sortie vérifiable de l exercice 8, reliée à la capacité officielle du bloc.
- Contrôle theta dans P10 TD reseaux protocoles paquets : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.

## Erreurs fréquentes
- confondre MAC et IP.
- TTL pris pour une durée.
- réémettre un paquet TTL 0.

## Différenciation
- Socle : données annotées.
- Standard : méthode complète.
- Expert : transfert avec `destination locale 192.168.1.34`.

## Cas limites travaillés
- TTL devient 0.
- destination locale 192.168.1.34.
- ACK43 dupliqué.

## Critères de réussite observables
- La donnée de départ est recopiée exactement.
- La trace ou le pseudo-code conduit à `src=192.168.1.20 dst=172.16.0.8 TCP port 443 TTL 4`.
- Au moins un cas limite de la section précédente est décidé.

