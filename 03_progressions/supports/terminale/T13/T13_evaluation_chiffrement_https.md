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
- Matériel autorisé : fiche de cours personnelle, sans accès réseau ni correction.
- Statut : évaluation créée en `needs_review`, non publiée et non validée.

## Capacités évaluées
- T-ARCH-04A
- T-ARCH-04B

## Fiche liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T13/T13_fiche_cours_chiffrement_https.md`.
- Séance liée : `T13-S1`.
- TD lié : `T13_TD_chiffrement_https.md`.

## Consignes
Répondre directement sur copie. Chaque réponse doit citer la donnée utilisée, la méthode et un contrôle rapide.

## Questions
### Question 1 - Lire le rôle des clés publique, privée et de session
- Capacité : T-ARCH-04A.
- Données : Client C, serveur S, certificat de S, clé publique KpubS, clé privée KprivS, clé de session Ks, message m = "GET /note".
- Consigne : répondre à la tâche « lire le rôle des clés publique, privée et de session » avec méthode, résultat et contrôle.
- Format attendu : réponse courte mais justifiée, avec notation ou pseudo-code si nécessaire.
### Question 2 - Analyser une étape de vérification de certificat
- Capacité : T-ARCH-04B.
- Données : Client C, serveur S, certificat de S, clé publique KpubS, clé privée KprivS, clé de session Ks, message m = "GET /note".
- Consigne : répondre à la tâche « analyser une étape de vérification de certificat » avec méthode, résultat et contrôle.
- Format attendu : réponse courte mais justifiée, avec notation ou pseudo-code si nécessaire.
### Question 3 - Produire un schéma d’échange de clé de session
- Capacité : T-ARCH-04A.
- Données : Client C, serveur S, certificat de S, clé publique KpubS, clé privée KprivS, clé de session Ks, message m = "GET /note".
- Consigne : répondre à la tâche « produire un schéma d’échange de clé de session » avec méthode, résultat et contrôle.
- Format attendu : réponse courte mais justifiée, avec notation ou pseudo-code si nécessaire.
### Question 4 - Écrire ce qui est chiffré en symétrique après négociation
- Capacité : T-ARCH-04B.
- Données : Client C, serveur S, certificat de S, clé publique KpubS, clé privée KprivS, clé de session Ks, message m = "GET /note".
- Consigne : répondre à la tâche « écrire ce qui est chiffré en symétrique après négociation » avec méthode, résultat et contrôle.
- Format attendu : réponse courte mais justifiée, avec notation ou pseudo-code si nécessaire.

## Barème
- Question 1: 2 points méthode, 1 point résultat, 1 point contrôle ou justification.
- Question 2: 2 points méthode, 1 point résultat, 1 point contrôle ou justification.
- Question 3: 2 points méthode, 1 point résultat, 1 point contrôle ou justification.
- Question 4: 2 points méthode, 1 point résultat, 1 point contrôle ou justification.
- Total : 16 points convertibles sur 20 après relecture pédagogique.

## Corrigé professeur
### Corrigé question 1
- Capacité évaluée : T-ARCH-04A.
- Réponse attendue : la solution explicite « lire le rôle des clés publique, privée et de session » à partir des données fournies.
- Justification : les étapes doivent permettre de retrouver le résultat sans deviner.
- Point de vigilance : une conclusion isolée sans contrôle perd les points de méthode.
### Corrigé question 2
- Capacité évaluée : T-ARCH-04B.
- Réponse attendue : la solution explicite « analyser une étape de vérification de certificat » à partir des données fournies.
- Justification : les étapes doivent permettre de retrouver le résultat sans deviner.
- Point de vigilance : une conclusion isolée sans contrôle perd les points de méthode.
### Corrigé question 3
- Capacité évaluée : T-ARCH-04A.
- Réponse attendue : la solution explicite « produire un schéma d’échange de clé de session » à partir des données fournies.
- Justification : les étapes doivent permettre de retrouver le résultat sans deviner.
- Point de vigilance : une conclusion isolée sans contrôle perd les points de méthode.
### Corrigé question 4
- Capacité évaluée : T-ARCH-04B.
- Réponse attendue : la solution explicite « écrire ce qui est chiffré en symétrique après négociation » à partir des données fournies.
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
