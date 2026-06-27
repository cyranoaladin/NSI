---
title: "P09 - EVALUATION - Architecture, système et droits"
level: "premiere"
sequence_id: "P09"
document_type: "evaluation"
status: "needs_review"
version: "0.2.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Architecture matérielle et systèmes"
notion: "chemins, processus, permissions"
objectifs:
  - "distinguer chemin absolu et relatif"
  - "interpréter r, w, x pour propriétaire/groupe/autres"
  - "proposer chmod u+x scripts/run.sh"
  - "expliquer l’erreur Permission denied"
private_data: false
official_program:
  capacities:
    - "P-ARCH-01A"
    - "P-ARCH-01B"
    - "P-ARCH-03A"
    - "P-ARCH-03B"
    - "P-ARCH-03C"
---

# P09 - Évaluation courte - Architecture, système et droits

## Objectifs évalués
- O1 : distinguer chemin absolu et relatif.
- O2 : interpréter r, w, x pour propriétaire/groupe/autres.
- O3 : proposer chmod u+x scripts/run.sh.
- O4 : expliquer l’erreur Permission denied.

## Capacités officielles
- P-ARCH-01A
- P-ARCH-01B
- P-ARCH-03A
- P-ARCH-03B
- P-ARCH-03C

## Questions
### Question 1
- Capacité : P-ARCH-01A.
- Énoncé : avec `ls -l : -rw-r--r-- app.py, -rw-r----- data/notes.csv, -rw-r--r-- scripts/run.sh`, distinguer chemin absolu et relatif.
- Réponse attendue : méthode explicite, résultat contrôlé et vocabulaire du chapitre P09.
- Critère de réussite : l’erreur « confondre lecture et exécution » est évitée ou corrigée.
### Question 2
- Capacité : P-ARCH-01B.
- Énoncé : avec `ls -l : -rw-r--r-- app.py, -rw-r----- data/notes.csv, -rw-r--r-- scripts/run.sh`, interpréter r, w, x pour propriétaire/groupe/autres.
- Réponse attendue : méthode explicite, résultat contrôlé et vocabulaire du chapitre P09.
- Critère de réussite : l’erreur « utiliser un chemin valable seulement dans son dossier courant » est évitée ou corrigée.
### Question 3
- Capacité : P-ARCH-03A.
- Énoncé : avec `ls -l : -rw-r--r-- app.py, -rw-r----- data/notes.csv, -rw-r--r-- scripts/run.sh`, proposer chmod u+x scripts/run.sh.
- Réponse attendue : méthode explicite, résultat contrôlé et vocabulaire du chapitre P09.
- Critère de réussite : l’erreur « donner tous les droits avec chmod 777 » est évitée ou corrigée.
### Question 4
- Capacité : P-ARCH-03B.
- Énoncé : avec `ls -l : -rw-r--r-- app.py, -rw-r----- data/notes.csv, -rw-r--r-- scripts/run.sh`, expliquer l’erreur Permission denied.
- Réponse attendue : méthode explicite, résultat contrôlé et vocabulaire du chapitre P09.
- Critère de réussite : l’erreur « oublier le rôle du système d’exploitation » est évitée ou corrigée.

## Barème
- Question 1 : 2 points méthode, 1 point résultat, 1 point contrôle du cas limite.
- Question 2 : 2 points méthode, 1 point résultat, 1 point contrôle du cas limite.
- Question 3 : 2 points méthode, 1 point résultat, 1 point contrôle du cas limite.
- Question 4 : 2 points méthode, 1 point résultat, 1 point contrôle du cas limite.

## Corrigé
### Corrigé question 1
- Démarche : distinguer chemin absolu et relatif.
- Résultat attendu : une conclusion justifiée par les valeurs obtenues avec `ls -l : -rw-r--r-- app.py, -rw-r----- data/notes.csv, -rw-r--r-- scripts/run.sh`.
- Justification : le contrôle explicite empêche l’erreur « confondre lecture et exécution ».
### Corrigé question 2
- Démarche : interpréter r, w, x pour propriétaire/groupe/autres.
- Résultat attendu : une conclusion justifiée par les valeurs obtenues avec `ls -l : -rw-r--r-- app.py, -rw-r----- data/notes.csv, -rw-r--r-- scripts/run.sh`.
- Justification : le contrôle explicite empêche l’erreur « utiliser un chemin valable seulement dans son dossier courant ».
### Corrigé question 3
- Démarche : proposer chmod u+x scripts/run.sh.
- Résultat attendu : une conclusion justifiée par les valeurs obtenues avec `ls -l : -rw-r--r-- app.py, -rw-r----- data/notes.csv, -rw-r--r-- scripts/run.sh`.
- Justification : le contrôle explicite empêche l’erreur « donner tous les droits avec chmod 777 ».
### Corrigé question 4
- Démarche : expliquer l’erreur Permission denied.
- Résultat attendu : une conclusion justifiée par les valeurs obtenues avec `ls -l : -rw-r--r-- app.py, -rw-r----- data/notes.csv, -rw-r--r-- scripts/run.sh`.
- Justification : le contrôle explicite empêche l’erreur « oublier le rôle du système d’exploitation ».

## Critères de réussite
- Les capacités officielles sont citées dans les réponses.
- Chaque question contient donnée, méthode, résultat et contrôle.
- Le vocabulaire disciplinaire est utilisé sans remplacer la justification.
- Le barème reste indicatif tant que la ressource est en needs_review.

## Modalités de passation
- Durée : 25 minutes.
- Matériel autorisé : fiche personnelle, sans corrigé ni accès réseau.
- Capacités évaluées :
- P-ARCH-01A
- P-ARCH-01B
- P-ARCH-03A
- P-ARCH-03B
- P-ARCH-03C

## Fiche liée et aménagement
- Fiche liée : fiche de cours opérationnelle de la séquence P09, statut `needs_review`.
- Séance liée : `P09-S1` dans la progression annuelle.
- Version aménagée : même sujet avec données surlignées et tableau méthode / résultat / contrôle.
- Remédiation : reprendre la question la moins réussie avec une donnée plus courte puis faire verbaliser la méthode.
## Erreurs fréquentes
- EF1 : répondre sans citer la donnée utilisée ; correction : encadrer la donnée avant de rédiger.
- EF2 : donner un résultat sans méthode ; correction : séparer méthode, résultat et contrôle.
- EF3 : oublier le cas limite ; correction : refaire une question avec une donnée minimale.

