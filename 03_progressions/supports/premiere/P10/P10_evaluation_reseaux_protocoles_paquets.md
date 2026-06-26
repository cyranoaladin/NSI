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
- Matériel autorisé : fiche de cours personnelle, sans accès réseau ni correction.
- Statut : évaluation créée en `needs_review`, non publiée et non validée.

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
Répondre directement sur copie. Chaque réponse doit citer la donnée utilisée, la méthode et un contrôle rapide.

## Questions
### Question 1 - Identifier source, destination, protocole et ttl dans un paquet ip
- Capacité : P-ARCH-02A.
- Données : Trace réseau : A(src=192.168.1.20,dst=172.16.0.8,proto=TCP,seq=42,ack=17,ttl=4), B(src=172.16.0.8,dst=192.168.1.20,proto=TCP,seq=17,ack=43,ttl=3), trame perdue seq=43 puis retransmission avec bit alterné 1.
- Consigne : répondre à la tâche « identifier source, destination, protocole et TTL dans un paquet IP » avec méthode, résultat et contrôle.
- Format attendu : réponse courte mais justifiée, avec notation ou pseudo-code si nécessaire.
### Question 2 - Expliquer encapsulation ethernet/ip/tcp sans mélanger adresse mac et adresse ip
- Capacité : P-ARCH-02B.
- Données : Trace réseau : A(src=192.168.1.20,dst=172.16.0.8,proto=TCP,seq=42,ack=17,ttl=4), B(src=172.16.0.8,dst=192.168.1.20,proto=TCP,seq=17,ack=43,ttl=3), trame perdue seq=43 puis retransmission avec bit alterné 1.
- Consigne : répondre à la tâche « expliquer encapsulation Ethernet/IP/TCP sans mélanger adresse MAC et adresse IP » avec méthode, résultat et contrôle.
- Format attendu : réponse courte mais justifiée, avec notation ou pseudo-code si nécessaire.
### Question 3 - Écrire la simulation d’un protocole à bit alterné après perte de trame
- Capacité : P-ARCH-02C.
- Données : Trace réseau : A(src=192.168.1.20,dst=172.16.0.8,proto=TCP,seq=42,ack=17,ttl=4), B(src=172.16.0.8,dst=192.168.1.20,proto=TCP,seq=17,ack=43,ttl=3), trame perdue seq=43 puis retransmission avec bit alterné 1.
- Consigne : répondre à la tâche « écrire la simulation d’un protocole à bit alterné après perte de trame » avec méthode, résultat et contrôle.
- Format attendu : réponse courte mais justifiée, avec notation ou pseudo-code si nécessaire.
### Question 4 - Définir les messages capteur, accusé de réception et commande actionneur
- Capacité : P-ARCH-04A.
- Données : Trace réseau : A(src=192.168.1.20,dst=172.16.0.8,proto=TCP,seq=42,ack=17,ttl=4), B(src=172.16.0.8,dst=192.168.1.20,proto=TCP,seq=17,ack=43,ttl=3), trame perdue seq=43 puis retransmission avec bit alterné 1.
- Consigne : répondre à la tâche « définir les messages capteur, accusé de réception et commande actionneur » avec méthode, résultat et contrôle.
- Format attendu : réponse courte mais justifiée, avec notation ou pseudo-code si nécessaire.

## Barème
- Question 1: 2 points méthode, 1 point résultat, 1 point contrôle ou justification.
- Question 2: 2 points méthode, 1 point résultat, 1 point contrôle ou justification.
- Question 3: 2 points méthode, 1 point résultat, 1 point contrôle ou justification.
- Question 4: 2 points méthode, 1 point résultat, 1 point contrôle ou justification.
- Total : 16 points convertibles sur 20 après relecture pédagogique.

## Corrigé professeur
### Corrigé question 1
- Capacité évaluée : P-ARCH-02A.
- Réponse attendue : la solution explicite « identifier source, destination, protocole et TTL dans un paquet IP » à partir des données fournies.
- Justification : les étapes doivent permettre de retrouver le résultat sans deviner.
- Point de vigilance : une conclusion isolée sans contrôle perd les points de méthode.
### Corrigé question 2
- Capacité évaluée : P-ARCH-02B.
- Réponse attendue : la solution explicite « expliquer encapsulation Ethernet/IP/TCP sans mélanger adresse MAC et adresse IP » à partir des données fournies.
- Justification : les étapes doivent permettre de retrouver le résultat sans deviner.
- Point de vigilance : une conclusion isolée sans contrôle perd les points de méthode.
### Corrigé question 3
- Capacité évaluée : P-ARCH-02C.
- Réponse attendue : la solution explicite « écrire la simulation d’un protocole à bit alterné après perte de trame » à partir des données fournies.
- Justification : les étapes doivent permettre de retrouver le résultat sans deviner.
- Point de vigilance : une conclusion isolée sans contrôle perd les points de méthode.
### Corrigé question 4
- Capacité évaluée : P-ARCH-04A.
- Réponse attendue : la solution explicite « définir les messages capteur, accusé de réception et commande actionneur » à partir des données fournies.
- Justification : les étapes doivent permettre de retrouver le résultat sans deviner.
- Point de vigilance : une conclusion isolée sans contrôle perd les points de méthode.

## Critères de réussite
- Les capacités officielles sont reliées à une action observable.
- La réponse ne se limite pas à un mot-clé de la fiche.
- Le cas limite ou le contrôle demandé apparaît explicitement.
- Le vocabulaire disciplinaire est utilisé dans le contexte de la donnée.

## Version aménagée et indications d’aménagement
- Version aménagée : conserver les mêmes questions mais fournir la donnée surlignée et un espace « méthode / résultat / contrôle ».
- Aménagement temps : ajouter 10 minutes si l'élève doit recopier la donnée.
- Aide autorisée : liste des verbes d'action, sans résultat numérique ni requête complète.

## Erreurs fréquentes et remédiation
- EF1 : réponse sans donnée citée ; remédiation : refaire la question 1 avec les valeurs encadrées.
- EF2 : méthode correcte mais résultat non contrôlé ; remédiation : ajouter une ligne de vérification.
- EF3 : confusion entre vocabulaire et preuve ; remédiation : demander une phrase « parce que ».
- EF4 : oubli du cas limite ; remédiation : reprendre le TD associé, exercice 5.

## Source et traçabilité
- Recherche locale effectuée dans `/home/alaeddine/Documents/NSI/Documents_DRIVE` avant création.
- Aucun fichier Drive n'a été repris directement dans cette évaluation.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
