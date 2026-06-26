---
title: "P06 - EVALUATION - Tables : recherche, tri et fusion"
level: "premiere"
sequence_id: "P06"
document_type: "evaluation"
status: "needs_review"
version: "0.2.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Traitement de tables"
notion: "recherche, tri, fusion de tables"
objectifs:
  - "rechercher la première ligne où id vaut 17"
  - "trier les lignes par nom puis par atelier"
  - "fusionner avec une table de présences par identifiant"
  - "signaler le doublon id=17 au lieu de l’écraser"
private_data: false
official_program:
  capacities:
    - "P-TABLE-03"
    - "P-TABLE-04"
---

# P06 - Évaluation courte - Tables : recherche, tri et fusion

## Objectifs évalués
- O1 : rechercher la première ligne où id vaut 17.
- O2 : trier les lignes par nom puis par atelier.
- O3 : fusionner avec une table de présences par identifiant.
- O4 : signaler le doublon id=17 au lieu de l’écraser.

## Capacités officielles
- P-TABLE-03
- P-TABLE-04

## Questions
### Question 1
- Capacité : P-TABLE-03.
- Énoncé : avec `inscriptions = [{"id": 17, "nom": "E1", "atelier": "robot"}, {"id": 4, "nom": "E2", "atelier": "web"}, {"id": 17, "nom": "E1", "atelier": "python"}]`, rechercher la première ligne où id vaut 17.
- Réponse attendue : méthode explicite, résultat contrôlé et vocabulaire du chapitre P06.
- Critère de réussite : l’erreur « utiliser la position de ligne comme clé stable » est évitée ou corrigée.
### Question 2
- Capacité : P-TABLE-04.
- Énoncé : avec `inscriptions = [{"id": 17, "nom": "E1", "atelier": "robot"}, {"id": 4, "nom": "E2", "atelier": "web"}, {"id": 17, "nom": "E1", "atelier": "python"}]`, trier les lignes par nom puis par atelier.
- Réponse attendue : méthode explicite, résultat contrôlé et vocabulaire du chapitre P06.
- Critère de réussite : l’erreur « supprimer silencieusement un doublon » est évitée ou corrigée.
### Question 3
- Capacité : P-TABLE-03.
- Énoncé : avec `inscriptions = [{"id": 17, "nom": "E1", "atelier": "robot"}, {"id": 4, "nom": "E2", "atelier": "web"}, {"id": 17, "nom": "E1", "atelier": "python"}]`, fusionner avec une table de présences par identifiant.
- Réponse attendue : méthode explicite, résultat contrôlé et vocabulaire du chapitre P06.
- Critère de réussite : l’erreur « trier des nombres stockés comme chaînes » est évitée ou corrigée.
### Question 4
- Capacité : P-TABLE-04.
- Énoncé : avec `inscriptions = [{"id": 17, "nom": "E1", "atelier": "robot"}, {"id": 4, "nom": "E2", "atelier": "web"}, {"id": 17, "nom": "E1", "atelier": "python"}]`, signaler le doublon id=17 au lieu de l’écraser.
- Réponse attendue : méthode explicite, résultat contrôlé et vocabulaire du chapitre P06.
- Critère de réussite : l’erreur « fusionner deux tables sans vérifier les clés absentes » est évitée ou corrigée.

## Barème
- Question 1 : 2 points méthode, 1 point résultat, 1 point contrôle du cas limite.
- Question 2 : 2 points méthode, 1 point résultat, 1 point contrôle du cas limite.
- Question 3 : 2 points méthode, 1 point résultat, 1 point contrôle du cas limite.
- Question 4 : 2 points méthode, 1 point résultat, 1 point contrôle du cas limite.

## Corrigé
### Corrigé question 1
- Démarche : rechercher la première ligne où id vaut 17.
- Résultat attendu : une conclusion compatible avec `inscriptions = [{"id": 17, "nom": "E1", "atelier": "robot"}, {"id": 4, "nom": "E2", "atelier": "web"}, {"id": 17, "nom": "E1", "atelier": "python"}]`.
- Justification : le contrôle explicite empêche l’erreur « utiliser la position de ligne comme clé stable ».
### Corrigé question 2
- Démarche : trier les lignes par nom puis par atelier.
- Résultat attendu : une conclusion compatible avec `inscriptions = [{"id": 17, "nom": "E1", "atelier": "robot"}, {"id": 4, "nom": "E2", "atelier": "web"}, {"id": 17, "nom": "E1", "atelier": "python"}]`.
- Justification : le contrôle explicite empêche l’erreur « supprimer silencieusement un doublon ».
### Corrigé question 3
- Démarche : fusionner avec une table de présences par identifiant.
- Résultat attendu : une conclusion compatible avec `inscriptions = [{"id": 17, "nom": "E1", "atelier": "robot"}, {"id": 4, "nom": "E2", "atelier": "web"}, {"id": 17, "nom": "E1", "atelier": "python"}]`.
- Justification : le contrôle explicite empêche l’erreur « trier des nombres stockés comme chaînes ».
### Corrigé question 4
- Démarche : signaler le doublon id=17 au lieu de l’écraser.
- Résultat attendu : une conclusion compatible avec `inscriptions = [{"id": 17, "nom": "E1", "atelier": "robot"}, {"id": 4, "nom": "E2", "atelier": "web"}, {"id": 17, "nom": "E1", "atelier": "python"}]`.
- Justification : le contrôle explicite empêche l’erreur « fusionner deux tables sans vérifier les clés absentes ».

## Critères de réussite
- Les capacités officielles sont citées dans les réponses.
- Chaque question contient donnée, méthode, résultat et contrôle.
- Le vocabulaire disciplinaire est utilisé sans remplacer la justification.
- Le barème reste indicatif tant que la ressource est en needs_review.

## Modalités de passation
- Durée : 25 minutes.
- Matériel autorisé : fiche personnelle, sans corrigé ni accès réseau.
- Capacités évaluées :
- P-TABLE-03
- P-TABLE-04
- P-TABLE-03
- P-TABLE-04

## Fiche liée et aménagement
- Fiche liée : fiche de cours opérationnelle de la séquence P06, statut `needs_review`.
- Séance liée : `P06-S1` dans la progression annuelle.
- Version aménagée : même sujet avec données surlignées et tableau méthode / résultat / contrôle.
- Remédiation : reprendre la question la moins réussie avec une donnée plus courte puis faire verbaliser la méthode.
## Erreurs fréquentes
- EF1 : répondre sans citer la donnée utilisée ; correction : encadrer la donnée avant de rédiger.
- EF2 : donner un résultat sans méthode ; correction : séparer méthode, résultat et contrôle.
- EF3 : oublier le cas limite ; correction : refaire une question avec une donnée minimale.

