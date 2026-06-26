---
title: "T13 - Évaluation - chiffrement HTTPS"
level: "terminale"
sequence_id: "T13"
document_type: "evaluation"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Sécurité"
notion: "chiffrement HTTPS"
objectifs:
  - "évaluer la compréhension de la fiche"
  - "vérifier la capacité à produire une réponse justifiée"
  - "identifier les erreurs fréquentes"
  - "préparer une remédiation ciblée"
private_data: false
official_program:
  capacities:
    - "T-ARCH-04A"
    - "T-ARCH-04B"
---

# T13 - Évaluation - chiffrement HTTPS

## Durée et matériel autorisé
- Durée : 25 minutes.
- Matériel autorisé : fiche personnelle, sans accès réseau ni corrigé.
- Statut : évaluation `needs_review`, non validée et non publiable.

## Capacités évaluées
- T-ARCH-04A
- T-ARCH-04B

## Fiche liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T13/T13_fiche_cours_chiffrement_https.md`.
- Séance liée : `T13-S1`.
- TD lié : `T13_TD_chiffrement_https.md`.

## Consignes
Répondre directement sur copie. Chaque réponse doit montrer la donnée utilisée, la méthode et un contrôle rapide.

## Questions
### Question 1 - Distinguer chiffrement symétrique/asymétrique
- Capacité : T-ARCH-04A.
- Données : Clé publique serveur Kpub, clé privée Kpriv, clé de session Ks.
- Consigne : Associer les rôles.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 2 - Lire un certificat
- Capacité : T-ARCH-04B.
- Données : Certificat: sujet serveur.example, émetteur CA-NSI, validité 2026-01-01 à 2027-01-01.
- Consigne : Dire ce qui est vérifié.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 3 - Dérouler un handshake simplifié
- Capacité : T-ARCH-04A.
- Données : Client propose suites ; serveur envoie certificat ; secret de session établi.
- Consigne : Écrire les étapes.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.
### Question 4 - Calculer un haché jouet
- Capacité : T-ARCH-04B.
- Données : h(m)=somme codes ASCII mod 10, message "AB".
- Consigne : Calculer h.
- Format attendu : réponse courte, justifiée, avec tableau, requête, pseudo-code ou trace si nécessaire.

## Barème
- Question 1: 1 point identification de la donnée, 1 point méthode, 1 point résultat exact, 1 point contrôle.
- Question 2: 1 point vocabulaire précis, 1 point méthode, 1 point résultat, 1 point justification.
- Question 3: 1 point modélisation, 1 point production correcte, 1 point test du résultat, 1 point lisibilité.
- Question 4: 1 point cas traité, 1 point résultat, 1 point justification, 1 point erreur fréquente évitée.
- Total : 16 points, conversion sur 20 après relecture pédagogique.

## Corrigé professeur
### Corrigé question 1
- Capacité évaluée : T-ARCH-04A.
- Donnée utilisée : Clé publique serveur Kpub, clé privée Kpriv, clé de session Ks.
- Réponse attendue : Kpub/Kpriv servent à authentifier/établir le secret ; Ks sert ensuite au chiffrement symétrique rapide des données.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 2
- Capacité évaluée : T-ARCH-04B.
- Donnée utilisée : Certificat: sujet serveur.example, émetteur CA-NSI, validité 2026-01-01 à 2027-01-01.
- Réponse attendue : Le navigateur vérifie le nom serveur.example, la période de validité et la signature par une autorité de confiance CA-NSI.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 3
- Capacité évaluée : T-ARCH-04A.
- Donnée utilisée : Client propose suites ; serveur envoie certificat ; secret de session établi.
- Réponse attendue : 1 ClientHello ; 2 ServerHello+certificat ; 3 vérification certificat ; 4 établissement Ks ; 5 données chiffrées avec Ks.
- Points attribués : les points du barème correspondent à des éléments observables dans cette réponse, pas à une intention supposée.
- Erreur fréquente liée : résultat donné sans citer la donnée ou sans contrôle.
### Corrigé question 4
- Capacité évaluée : T-ARCH-04B.
- Donnée utilisée : h(m)=somme codes ASCII mod 10, message "AB".
- Réponse attendue : ASCII A=65, B=66, somme=131, 131 mod 10 = 1. Ce haché jouet n’est pas cryptographiquement sûr.
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
