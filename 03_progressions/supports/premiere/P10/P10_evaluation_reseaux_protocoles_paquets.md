---
title: "P10 - Évaluation - protocoles et paquets"
level: "premiere"
sequence_id: "P10"
document_type: "evaluation"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Réseaux"
notion: "protocoles et paquets"
objectifs:
  - "évaluer la compréhension de la fiche"
  - "vérifier la capacité à produire une réponse justifiée"
  - "identifier les erreurs fréquentes"
  - "préparer une remédiation ciblée"
private_data: false
official_program:
  capacities:
    - "P-ARCH-02A"
    - "P-ARCH-02B"
    - "P-ARCH-02C"
    - "P-ARCH-04A"
    - "P-ARCH-04B"
---

# P10 - Évaluation - protocoles et paquets

## Durée et matériel autorisé
- Durée : 25 minutes.
- Matériel autorisé : fiche personnelle, sans accès réseau ni corrigé.
- Statut : évaluation `needs_review`, non validée et non publiable.

## Capacités évaluées
- P-ARCH-02A
- P-ARCH-02B
- P-ARCH-02C
- P-ARCH-04A
- P-ARCH-04B

## Fiche liée
- Fiche liée : `03_progressions/fiches_cours/premiere/P10/P10_fiche_cours_reseaux_protocoles_paquets.md`.
- Séance liée : `P10-S1`.
- TD lié : `P10_TD_reseaux_protocoles_paquets.md`.

## Consignes
Répondre directement sur copie. Chaque réponse doit montrer la donnée utilisée, la méthode et un contrôle rapide.

## Questions
### Question 1 - Identifier les champs d’un paquet IPv4
- Capacité : P-ARCH-02A.
- Données : Paquet A: src=192.168.1.20, dst=172.16.0.8, protocole=TCP, port source=50214, port destination=443, TTL=4.
- Consigne : Relever source, destination, protocole, port serveur et TTL.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 2 - Distinguer adresses MAC et adresses IP
- Capacité : P-ARCH-02B.
- Données : Trame Ethernet: MAC src=08:00:27:AA:10:01, MAC dst=08:00:27:BB:20:01 ; paquet IP: src=192.168.1.20, dst=172.16.0.8.
- Consigne : Dire quels champs changent à chaque saut et quels champs restent de bout en bout.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 3 - Dérouler un protocole à bit alterné
- Capacité : P-ARCH-02C.
- Données : M0(bit=0) reçu et ACK0 renvoyé ; M1(bit=1) est perdu ; l’émetteur retransmet M1 après timeout.
- Consigne : Écrire la séquence émission, perte, retransmission, ACK.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 4 - Produire un pseudo-code de passerelle
- Capacité : P-ARCH-04A.
- Données : Réseau local 192.168.1.0/24 ; passerelle 192.168.1.1 ; destination 192.168.1.34 puis destination 172.16.0.8.
- Consigne : Écrire la décision locale/passerelle.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.

## Barème
- Question 1: 1 point identification de la donnée, 1 point méthode, 1 point résultat exact, 1 point contrôle.
- Question 2: 1 point vocabulaire précis, 1 point méthode, 1 point résultat, 1 point justification.
- Question 3: 1 point modélisation, 1 point production correcte, 1 point test du résultat, 1 point lisibilité.
- Question 4: 1 point cas traité, 1 point résultat, 1 point justification, 1 point erreur fréquente évitée.
- Total : 16 points, conversion sur 20 après relecture pédagogique.

## Corrigé professeur
### Corrigé question 1
- Capacité évaluée : P-ARCH-02A.
- Donnée utilisée : Paquet A: src=192.168.1.20, dst=172.16.0.8, protocole=TCP, port source=50214, port destination=443, TTL=4.
- Réponse attendue : Source IP 192.168.1.20 ; destination IP 172.16.0.8 ; protocole TCP ; port serveur 443 ; TTL initial 4. Le paquet part du capteur vers le serveur HTTPS.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 2
- Capacité évaluée : P-ARCH-02B.
- Donnée utilisée : Trame Ethernet: MAC src=08:00:27:AA:10:01, MAC dst=08:00:27:BB:20:01 ; paquet IP: src=192.168.1.20, dst=172.16.0.8.
- Réponse attendue : Les adresses MAC changent à chaque liaison locale ; les IP source/destination restent 192.168.1.20 et 172.16.0.8 de bout en bout, sauf mécanisme particulier non étudié ici.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 3
- Capacité évaluée : P-ARCH-02C.
- Donnée utilisée : M0(bit=0) reçu et ACK0 renvoyé ; M1(bit=1) est perdu ; l’émetteur retransmet M1 après timeout.
- Réponse attendue : Séquence: envoyer M0(bit 0) -> recevoir ACK0 -> envoyer M1(bit 1) -> perte de M1 -> timeout -> retransmettre M1(bit 1) -> réception M1 -> renvoyer ACK1 -> l’émetteur passe au bit 0.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 4
- Capacité évaluée : P-ARCH-04A.
- Donnée utilisée : Réseau local 192.168.1.0/24 ; passerelle 192.168.1.1 ; destination 192.168.1.34 puis destination 172.16.0.8.
- Réponse attendue : Pseudo-code: si dst commence par 192.168.1. alors envoyer directement sur le LAN ; sinon envoyer à 192.168.1.1. Donc 192.168.1.34 est local, 172.16.0.8 passe par la passerelle.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.

## Critères de réussite
- Les capacités officielles sont reliées à une action observable.
- Le résultat attendu peut être comparé à une valeur, une table, une trace ou un pseudo-code.
- Le cas limite ou le contrôle demandé apparaît explicitement.
- Le vocabulaire disciplinaire est utilisé dans le contexte de la donnée.

## Version aménagée et indications d’aménagement
- Version aménagée : conserver les mêmes questions mais fournir la donnée surlignée et un tableau méthode / résultat / contrôle.
- Aménagement temps : ajouter 10 minutes si l’élève doit recopier les données.
- Aide autorisée : liste des verbes d’action, sans résultat numérique ni requête complète.

## Erreurs fréquentes et remédiation
- EF1 : réponse sans donnée citée ; remédiation : refaire la question 1 avec les valeurs encadrées.
- EF2 : méthode correcte mais résultat non contrôlé ; remédiation : ajouter une ligne de vérification.
- EF3 : confusion entre vocabulaire et preuve ; remédiation : demander une phrase « parce que ».
- EF4 : oubli du cas limite ; remédiation : reprendre le TD associé, exercice 5.

## Source et traçabilité
- Recherche locale effectuée dans le dossier Documents_DRIVE avant création.
- Aucun fichier Drive n’a été repris directement dans cette évaluation.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
