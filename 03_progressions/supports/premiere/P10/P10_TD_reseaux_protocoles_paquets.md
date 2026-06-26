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
- O1 : appliquer les méthodes de la fiche à une donnée différente.
- O2 : distinguer lecture d'information, production et justification.
- O3 : traiter au moins un cas limite sans le masquer.
- O4 : préparer une correction exploitable en séance.

## Capacités officielles
- P-ARCH-02A
- P-ARCH-02B
- P-ARCH-02C
- P-ARCH-04A
- P-ARCH-04B

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/premiere/P10/P10_fiche_cours_reseaux_protocoles_paquets.md`.
- Séance liée : `P10-S1` dans la progression annuelle.
- Statut : support créé en `needs_review`, non validé pédagogiquement et non publiable.

## Situation de travail
une mini-application de capteur envoie des mesures depuis 192.168.1.20 vers un serveur 172.16.0.8 en passant par une passerelle.

## Données de référence
Trace réseau : A(src=192.168.1.20,dst=172.16.0.8,proto=TCP,seq=42,ack=17,ttl=4), B(src=172.16.0.8,dst=192.168.1.20,proto=TCP,seq=17,ack=43,ttl=3), trame perdue seq=43 puis retransmission avec bit alterné 1.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée et vocabulaire.
- Standard : exercices 3 à 6, production écrite avec contrôle.
- Approfondissement : exercices 7 et 8, comparaison de démarches et généralisation.

## Exercices
### Exercice 1 - Identifier source, destination, protocole et ttl dans un paquet ip
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : P-ARCH-02A.
- Données : Trace réseau : A(src=192.168.1.20,dst=172.16.0.8,proto=TCP,seq=42,ack=17,ttl=4), B(src=172.16.0.8,dst=192.168.1.20,proto=TCP,seq=17,ack=43,ttl=3), trame perdue seq=43 puis retransmission avec bit alterné 1.
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de identifier source, destination, protocole et TTL dans un paquet IP.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 2 - Expliquer encapsulation ethernet/ip/tcp sans mélanger adresse mac et adresse ip
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : P-ARCH-02B.
- Données : Trace réseau : A(src=192.168.1.20,dst=172.16.0.8,proto=TCP,seq=42,ack=17,ttl=4), B(src=172.16.0.8,dst=192.168.1.20,proto=TCP,seq=17,ack=43,ttl=3), trame perdue seq=43 puis retransmission avec bit alterné 1.
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de expliquer encapsulation Ethernet/IP/TCP sans mélanger adresse MAC et adresse IP.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 3 - Écrire la simulation d’un protocole à bit alterné après perte de trame
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : P-ARCH-02C.
- Données : Trace réseau : A(src=192.168.1.20,dst=172.16.0.8,proto=TCP,seq=42,ack=17,ttl=4), B(src=172.16.0.8,dst=192.168.1.20,proto=TCP,seq=17,ack=43,ttl=3), trame perdue seq=43 puis retransmission avec bit alterné 1.
- Consigne : Produis une réponse opérationnelle pour écrire la simulation d’un protocole à bit alterné après perte de trame, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 4 - Définir les messages capteur, accusé de réception et commande actionneur
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : P-ARCH-04A.
- Données : Trace réseau : A(src=192.168.1.20,dst=172.16.0.8,proto=TCP,seq=42,ack=17,ttl=4), B(src=172.16.0.8,dst=192.168.1.20,proto=TCP,seq=17,ack=43,ttl=3), trame perdue seq=43 puis retransmission avec bit alterné 1.
- Consigne : Produis une réponse opérationnelle pour définir les messages capteur, accusé de réception et commande actionneur, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 5 - Traiter le cas limite ttl=0 et destination dans le même sous-réseau
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : P-ARCH-04B.
- Données : Trace réseau : A(src=192.168.1.20,dst=172.16.0.8,proto=TCP,seq=42,ack=17,ttl=4), B(src=172.16.0.8,dst=192.168.1.20,proto=TCP,seq=17,ack=43,ttl=3), trame perdue seq=43 puis retransmission avec bit alterné 1.
- Consigne : Traite le cas limite demandé pour traiter le cas limite TTL=0 et destination dans le même sous-réseau et précise la convention retenue.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 6 - Justifier pourquoi un protocole impose format et ordre des messages
- Type : justification.
- Niveau : standard.
- Capacité officielle : P-ARCH-02A.
- Données : Trace réseau : A(src=192.168.1.20,dst=172.16.0.8,proto=TCP,seq=42,ack=17,ttl=4), B(src=172.16.0.8,dst=192.168.1.20,proto=TCP,seq=17,ack=43,ttl=3), trame perdue seq=43 puis retransmission avec bit alterné 1.
- Consigne : Justifie pourquoi la méthode utilisée pour justifier pourquoi un protocole impose format et ordre des messages est correcte dans ce contexte.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 7 - Analyser une trace avec accusé de réception dupliqué
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : P-ARCH-02B.
- Données : Trace réseau : A(src=192.168.1.20,dst=172.16.0.8,proto=TCP,seq=42,ack=17,ttl=4), B(src=172.16.0.8,dst=192.168.1.20,proto=TCP,seq=17,ack=43,ttl=3), trame perdue seq=43 puis retransmission avec bit alterné 1.
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de analyser une trace avec accusé de réception dupliqué.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 8 - Proposer un pseudo-code de décision passerelle ou livraison locale
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : P-ARCH-02C.
- Données : Trace réseau : A(src=192.168.1.20,dst=172.16.0.8,proto=TCP,seq=42,ack=17,ttl=4), B(src=172.16.0.8,dst=192.168.1.20,proto=TCP,seq=17,ack=43,ttl=3), trame perdue seq=43 puis retransmission avec bit alterné 1.
- Consigne : Produis une réponse opérationnelle pour proposer un pseudo-code de décision passerelle ou livraison locale, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : P-ARCH-02A.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P10 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « identifier source, destination, protocole et TTL dans un paquet IP » en utilisant le vocabulaire protocoles et paquets.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 2
- Capacité mobilisée : P-ARCH-02B.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P10 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « expliquer encapsulation Ethernet/IP/TCP sans mélanger adresse MAC et adresse IP » en utilisant le vocabulaire protocoles et paquets.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 3
- Capacité mobilisée : P-ARCH-02C.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P10 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « écrire la simulation d’un protocole à bit alterné après perte de trame » en utilisant le vocabulaire protocoles et paquets.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 4
- Capacité mobilisée : P-ARCH-04A.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P10 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « définir les messages capteur, accusé de réception et commande actionneur » en utilisant le vocabulaire protocoles et paquets.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 5
- Capacité mobilisée : P-ARCH-04B.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P10 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « traiter le cas limite TTL=0 et destination dans le même sous-réseau » en utilisant le vocabulaire protocoles et paquets.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 6
- Capacité mobilisée : P-ARCH-02A.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P10 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « justifier pourquoi un protocole impose format et ordre des messages » en utilisant le vocabulaire protocoles et paquets.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 7
- Capacité mobilisée : P-ARCH-02B.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P10 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « analyser une trace avec accusé de réception dupliqué » en utilisant le vocabulaire protocoles et paquets.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 8
- Capacité mobilisée : P-ARCH-02C.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P10 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « proposer un pseudo-code de décision passerelle ou livraison locale » en utilisant le vocabulaire protocoles et paquets.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.

## Erreurs fréquentes
- EF1 : recopier une définition sans l'appliquer à la donnée ; remédiation : entourer les valeurs utilisées avant d'écrire.
- EF2 : produire un résultat sans contrôle ; remédiation : ajouter une ligne « vérification » à chaque réponse.
- EF3 : confondre cas nominal et cas limite ; remédiation : refaire l'exercice 5 avec une donnée minimale.
- EF4 : citer la capacité officielle sans méthode ; remédiation : associer chaque capacité à une action observable.

## Différenciation
- Socle : fournir la donnée annotée et demander une phrase de conclusion.
- Standard : demander la méthode complète et le contrôle écrit.
- Approfondissement : demander une variante de donnée et une comparaison de deux démarches.

## Lien avec la progression
| Élément | Référence | Statut |
|---|---|---|
| Fiche | P10_fiche_cours_reseaux_protocoles_paquets.md | needs_review |
| Séance | P10-S1 | progression existante |
| Évaluation | P10_evaluation_reseaux_protocoles_paquets.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans `/home/alaeddine/Documents/NSI/Documents_DRIVE` avant création.
- Aucun fichier Drive n'a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
