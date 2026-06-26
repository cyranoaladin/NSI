---
title: "P10 - TD - protocoles et paquets"
level: "premiere"
sequence_id: "P10"
document_type: "td"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Réseaux"
notion: "protocoles et paquets"
objectifs:
  - "travailler protocoles et paquets sur des données explicites"
  - "produire une réponse justifiée et contrôlée"
  - "identifier les cas limites"
  - "corriger les erreurs fréquentes du chapitre"
private_data: false
official_program:
  capacities:
    - "P-ARCH-02A"
    - "P-ARCH-02B"
    - "P-ARCH-02C"
    - "P-ARCH-04A"
    - "P-ARCH-04B"
---

# P10 - TD - protocoles et paquets

## Objectifs
- Lire une donnée disciplinaire précise avant de répondre.
- Produire une méthode vérifiable et un résultat contrôlable.
- Traiter un cas limite sans le transformer en généralité.
- Relier chaque correction à une erreur fréquente observable.

## Capacités officielles
- P-ARCH-02A
- P-ARCH-02B
- P-ARCH-02C
- P-ARCH-04A
- P-ARCH-04B

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/premiere/P10/P10_fiche_cours_reseaux_protocoles_paquets.md`.
- Séance liée : `P10-S1` dans la progression annuelle.
- Statut : support `needs_review`, non validé et non publiable.

## Situation de travail
Une station de capteurs envoie une mesure depuis 192.168.1.20 vers 172.16.0.8 via la passerelle 192.168.1.1.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée.
- Standard : exercices 3 à 6, production écrite et justification.
- Approfondissement : exercices 7 et 8, transfert ou comparaison.

## Exercices
### Exercice 1 - Identifier les champs d’un paquet IPv4
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : P-ARCH-02A.
- Données : Paquet A: src=192.168.1.20, dst=172.16.0.8, protocole=TCP, port source=50214, port destination=443, TTL=4.
- Consigne : Relever source, destination, protocole, port serveur et TTL.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 2 - Distinguer adresses MAC et adresses IP
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : P-ARCH-02B.
- Données : Trame Ethernet: MAC src=08:00:27:AA:10:01, MAC dst=08:00:27:BB:20:01 ; paquet IP: src=192.168.1.20, dst=172.16.0.8.
- Consigne : Dire quels champs changent à chaque saut et quels champs restent de bout en bout.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 3 - Dérouler un protocole à bit alterné
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : P-ARCH-02C.
- Données : M0(bit=0) reçu et ACK0 renvoyé ; M1(bit=1) est perdu ; l’émetteur retransmet M1 après timeout.
- Consigne : Écrire la séquence émission, perte, retransmission, ACK.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 4 - Produire un pseudo-code de passerelle
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : P-ARCH-04A.
- Données : Réseau local 192.168.1.0/24 ; passerelle 192.168.1.1 ; destination 192.168.1.34 puis destination 172.16.0.8.
- Consigne : Écrire la décision locale/passerelle.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 5 - Traiter TTL égal à 0
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : P-ARCH-04B.
- Données : Un routeur reçoit un paquet IP avec TTL=1 vers 172.16.0.8. Il décrémente avant retransmission.
- Consigne : Dire ce qui arrive au paquet.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 6 - Justifier le rôle d’un protocole
- Type : justification.
- Niveau : standard.
- Capacité officielle : P-ARCH-02A.
- Données : Deux capteurs envoient température et humidité ; le serveur attend ordre: TYPE;ID;VALEUR;HORODATAGE.
- Consigne : Expliquer pourquoi format et ordre sont obligatoires.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 7 - Analyser un ACK dupliqué
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : P-ARCH-02B.
- Données : Trace TCP: seq=42 len=1, ACK43 ; puis seq=43 perdu ; le récepteur renvoie deux fois ACK43.
- Consigne : Interpréter ACK43 dupliqué.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 8 - Définir les messages capteur/actionneur
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : P-ARCH-02C.
- Données : Capteur C7, température 19.8 °C, actionneur chauffage ON, timestamp 10:15:03.
- Consigne : Proposer deux messages textuels cohérents.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : P-ARCH-02A.
- Donnée utilisée : Paquet A: src=192.168.1.20, dst=172.16.0.8, protocole=TCP, port source=50214, port destination=443, TTL=4.
- Résultat attendu : Source IP 192.168.1.20 ; destination IP 172.16.0.8 ; protocole TCP ; port serveur 443 ; TTL initial 4. Le paquet part du capteur vers le serveur HTTPS.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 2
- Capacité mobilisée : P-ARCH-02B.
- Donnée utilisée : Trame Ethernet: MAC src=08:00:27:AA:10:01, MAC dst=08:00:27:BB:20:01 ; paquet IP: src=192.168.1.20, dst=172.16.0.8.
- Résultat attendu : Les adresses MAC changent à chaque liaison locale ; les IP source/destination restent 192.168.1.20 et 172.16.0.8 de bout en bout, sauf mécanisme particulier non étudié ici.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 3
- Capacité mobilisée : P-ARCH-02C.
- Donnée utilisée : M0(bit=0) reçu et ACK0 renvoyé ; M1(bit=1) est perdu ; l’émetteur retransmet M1 après timeout.
- Résultat attendu : Séquence: envoyer M0(bit 0) -> recevoir ACK0 -> envoyer M1(bit 1) -> perte de M1 -> timeout -> retransmettre M1(bit 1) -> réception M1 -> renvoyer ACK1 -> l’émetteur passe au bit 0.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 4
- Capacité mobilisée : P-ARCH-04A.
- Donnée utilisée : Réseau local 192.168.1.0/24 ; passerelle 192.168.1.1 ; destination 192.168.1.34 puis destination 172.16.0.8.
- Résultat attendu : Pseudo-code: si dst commence par 192.168.1. alors envoyer directement sur le LAN ; sinon envoyer à 192.168.1.1. Donc 192.168.1.34 est local, 172.16.0.8 passe par la passerelle.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 5
- Capacité mobilisée : P-ARCH-04B.
- Donnée utilisée : Un routeur reçoit un paquet IP avec TTL=1 vers 172.16.0.8. Il décrémente avant retransmission.
- Résultat attendu : Le routeur calcule TTL=0. Il ne retransmet pas le paquet ; il le détruit et peut renvoyer un message ICMP Time Exceeded à la source.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 6
- Capacité mobilisée : P-ARCH-02A.
- Donnée utilisée : Deux capteurs envoient température et humidité ; le serveur attend ordre: TYPE;ID;VALEUR;HORODATAGE.
- Résultat attendu : Sans ordre commun, 23.5 peut être lu comme ID ou valeur. Le protocole fixe les champs TYPE, ID, VALEUR, HORODATAGE afin que le destinataire parse chaque message sans ambiguïté.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 7
- Capacité mobilisée : P-ARCH-02B.
- Donnée utilisée : Trace TCP: seq=42 len=1, ACK43 ; puis seq=43 perdu ; le récepteur renvoie deux fois ACK43.
- Résultat attendu : ACK43 signifie « j’attends l’octet ou segment 43 ». Deux ACK43 indiquent que le segment 43 manque encore ; ils déclenchent une retransmission possible.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 8
- Capacité mobilisée : P-ARCH-02C.
- Donnée utilisée : Capteur C7, température 19.8 °C, actionneur chauffage ON, timestamp 10:15:03.
- Résultat attendu : Mesure: MESURE;C7;TEMP;19.8;10:15:03. Commande: COMMANDE;CHAUFFAGE;ON;10:15:05. Les champs permettent type, cible, valeur et date.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.

## Erreurs fréquentes
- EF1 : répondre par un mot-clé sans citer la donnée ; remédiation : entourer les valeurs utiles avant de rédiger.
- EF2 : donner un résultat sans méthode ; remédiation : imposer une ligne méthode puis une ligne résultat.
- EF3 : oublier le cas limite ; remédiation : refaire l’exercice 5 avec la donnée minimale.
- EF4 : confondre justification et paraphrase ; remédiation : écrire une phrase qui relie donnée, règle et conclusion.

## Remédiation ciblée
- Reprendre deux exercices en ne gardant que les données numériques ou symboliques.
- Faire corriger une réponse incomplète par un binôme avec une grille donnée/méthode/résultat/contrôle.
- Produire une variante courte avec une donnée changée et vérifier que la méthode reste valable.

## Différenciation
- Socle : fournir les données annotées et demander seulement le résultat contrôlé.
- Standard : demander méthode complète, résultat et contrôle écrit.
- Approfondissement : demander une variante de la donnée et une comparaison de deux démarches.

## Lien avec la progression
| Élément | Référence | Statut |
|---|---|---|
| Fiche | P10_fiche_cours_reseaux_protocoles_paquets.md | needs_review |
| Séance | P10-S1 | progression existante |
| Évaluation | P10_evaluation_reseaux_protocoles_paquets.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans le dossier Documents_DRIVE avant création.
- Aucun fichier Drive n’a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
