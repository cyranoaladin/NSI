---
title: "T08 - EVALUATION - Parcours BFS, DFS, cycles et chemins"
level: "terminale"
sequence_id: "T08"
document_type: "evaluation"
status: "needs_review"
version: "0.2.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Algorithmes sur graphes"
notion: "parcours en largeur, profondeur, chemins, cycles"
objectifs:
  - "exécuter BFS avec file"
  - "exécuter DFS avec pile ou récursion"
  - "reconstruire un chemin par prédécesseurs"
  - "détecter un cycle en évitant le parent"
private_data: false
official_program:
  capacities:
    - "T-ALGO-02A"
    - "T-ALGO-02B"
    - "T-ALGO-02C"
    - "T-ALGO-02D"
---

# T08 - Évaluation courte - Parcours BFS, DFS, cycles et chemins

## Objectifs évalués
- O1 : exécuter BFS avec file.
- O2 : exécuter DFS avec pile ou récursion.
- O3 : reconstruire un chemin par prédécesseurs.
- O4 : détecter un cycle en évitant le parent.

## Capacités officielles
- T-ALGO-02A
- T-ALGO-02B
- T-ALGO-02C
- T-ALGO-02D

## Questions
### Question 1
- Capacité : T-ALGO-02A.
- Énoncé : avec `A: B,C ; B: A,D ; C: A,D ; D: B,C,E ; E: D`, exécuter BFS avec file.
- Réponse attendue : méthode explicite, résultat contrôlé et vocabulaire du chapitre T08.
- Critère de réussite : l’erreur « marquer un sommet trop tard » est évitée ou corrigée.
### Question 2
- Capacité : T-ALGO-02B.
- Énoncé : avec `A: B,C ; B: A,D ; C: A,D ; D: B,C,E ; E: D`, exécuter DFS avec pile ou récursion.
- Réponse attendue : méthode explicite, résultat contrôlé et vocabulaire du chapitre T08.
- Critère de réussite : l’erreur « croire que DFS donne toujours un plus court chemin » est évitée ou corrigée.
### Question 3
- Capacité : T-ALGO-02C.
- Énoncé : avec `A: B,C ; B: A,D ; C: A,D ; D: B,C,E ; E: D`, reconstruire un chemin par prédécesseurs.
- Réponse attendue : méthode explicite, résultat contrôlé et vocabulaire du chapitre T08.
- Critère de réussite : l’erreur « oublier les prédécesseurs » est évitée ou corrigée.
### Question 4
- Capacité : T-ALGO-02D.
- Énoncé : avec `A: B,C ; B: A,D ; C: A,D ; D: B,C,E ; E: D`, détecter un cycle en évitant le parent.
- Réponse attendue : méthode explicite, résultat contrôlé et vocabulaire du chapitre T08.
- Critère de réussite : l’erreur « confondre cycle et simple retour vers le parent » est évitée ou corrigée.

## Barème
- Question 1 : 2 points méthode, 1 point résultat, 1 point contrôle du cas limite.
- Question 2 : 2 points méthode, 1 point résultat, 1 point contrôle du cas limite.
- Question 3 : 2 points méthode, 1 point résultat, 1 point contrôle du cas limite.
- Question 4 : 2 points méthode, 1 point résultat, 1 point contrôle du cas limite.

## Corrigé
### Corrigé question 1
- Démarche : exécuter BFS avec file.
- Résultat attendu : une conclusion compatible avec `A: B,C ; B: A,D ; C: A,D ; D: B,C,E ; E: D`.
- Justification : le contrôle explicite empêche l’erreur « marquer un sommet trop tard ».
### Corrigé question 2
- Démarche : exécuter DFS avec pile ou récursion.
- Résultat attendu : une conclusion compatible avec `A: B,C ; B: A,D ; C: A,D ; D: B,C,E ; E: D`.
- Justification : le contrôle explicite empêche l’erreur « croire que DFS donne toujours un plus court chemin ».
### Corrigé question 3
- Démarche : reconstruire un chemin par prédécesseurs.
- Résultat attendu : une conclusion compatible avec `A: B,C ; B: A,D ; C: A,D ; D: B,C,E ; E: D`.
- Justification : le contrôle explicite empêche l’erreur « oublier les prédécesseurs ».
### Corrigé question 4
- Démarche : détecter un cycle en évitant le parent.
- Résultat attendu : une conclusion compatible avec `A: B,C ; B: A,D ; C: A,D ; D: B,C,E ; E: D`.
- Justification : le contrôle explicite empêche l’erreur « confondre cycle et simple retour vers le parent ».

## Critères de réussite
- Les capacités officielles sont citées dans les réponses.
- Chaque question contient donnée, méthode, résultat et contrôle.
- Le vocabulaire disciplinaire est utilisé sans remplacer la justification.
- Le barème reste indicatif tant que la ressource est en needs_review.

## Modalités de passation
- Durée : 25 minutes.
- Matériel autorisé : fiche personnelle, sans corrigé ni accès réseau.
- Capacités évaluées :
- T-ALGO-02A
- T-ALGO-02B
- T-ALGO-02C
- T-ALGO-02D
- T-ALGO-02A
- T-ALGO-02B
- T-ALGO-02C
- T-ALGO-02D

## Fiche liée et aménagement
- Fiche liée : fiche de cours opérationnelle de la séquence T08, statut `needs_review`.
- Séance liée : `T08-S1` dans la progression annuelle.
- Version aménagée : même sujet avec données surlignées et tableau méthode / résultat / contrôle.
- Remédiation : reprendre la question la moins réussie avec une donnée plus courte puis faire verbaliser la méthode.
## Erreurs fréquentes
- EF1 : répondre sans citer la donnée utilisée ; correction : encadrer la donnée avant de rédiger.
- EF2 : donner un résultat sans méthode ; correction : séparer méthode, résultat et contrôle.
- EF3 : oublier le cas limite ; correction : refaire une question avec une donnée minimale.

