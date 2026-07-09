---
title: "P13 - corrige - dichotomie, glouton et k-NN"
level: "premiere"
sequence_id: "P13"
document_type: "corrige"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "dichotomie, glouton et k-NN"
notion: "dichotomie, glouton et k-NN"
private_data: false
official_program:
  capacities:
    - "P-ALGO-03"
    - "P-ALGO-04"
    - "P-ALGO-05"
---

# P13 - Corrigé - dichotomie, glouton et k-NN

## Corrigé du TD
### Exercice 1
- Capacité mobilisée : P-ALGO-04.
- Réponse attendue : milieux 18 puis 37 -> trouvé indice 4.
- Méthode : calculer milieu puis réduire intervalle.
- Cas limite : cible absente.
### Exercice 2
- Capacité mobilisée : P-ALGO-04.
- Réponse attendue : le variant V = droite − gauche + 1 décroît de 6 à 3 sur tableau=[4,9,18,23,37,41], cible=37 → terminaison (cible trouvée).
- Méthode : montrer que V décroît strictement à chaque étape.
- Cas limite : cible absente (ex. 38) → V décroît 6→3→1→0, la boucle s'arrête sans trouver.
### Exercice 3
- Capacité mobilisée : P-ALGO-05.
- Réponse attendue : 28 = 10 + 10 + 5 + 2 + 1 (5 pièces, algorithme glouton avec pièces=[10,5,2,1]).
- Méthode : prendre la plus grande pièce possible à chaque étape.
- Cas limite : pièce 1 absente → le glouton peut échouer (ex. montant=3 avec pièces=[5,2]).
### Exercice 4
- Capacité mobilisée : P-ALGO-03.
- Réponse attendue : voisins=[rouge:1.2, bleu:2.0, rouge:2.4], k=3 → vote rouge=2, bleu=1 → classe rouge.
- Méthode : trier par distance, voter parmi les k plus proches.
- Cas limite : k pair → égalité de vote possible.
### Exercice 5
- Capacité mobilisée : P-ALGO-04.
- Réponse attendue : le variant V = droite − gauche + 1 décroît de 6 à 3 sur tableau=[4,9,18,23,37,41], cible=37 → terminaison (cible trouvée).
- Méthode : montrer que V décroît strictement à chaque étape.
- Cas limite : cible absente (ex. 38) → V décroît 6→3→1→0, la boucle s'arrête sans trouver.
### Exercice 6
- Capacité mobilisée : P-ALGO-05.
- Réponse attendue : 28 = 10 + 10 + 5 + 2 + 1 (5 pièces, algorithme glouton avec pièces=[10,5,2,1]).
- Méthode : prendre la plus grande pièce possible à chaque étape.
- Cas limite : pièce 1 absente → le glouton peut échouer (ex. montant=3 avec pièces=[5,2]).
### Exercice 7
- Capacité mobilisée : P-ALGO-03.
- Réponse attendue : voisins=[rouge:1.2, bleu:2.0, rouge:2.4], k=3 → vote rouge=2, bleu=1 → classe rouge.
- Méthode : trier par distance, voter parmi les k plus proches.
- Cas limite : k pair → égalité de vote possible.
### Exercice 8
- Capacité mobilisée : P-ALGO-04.
- Réponse attendue : le variant V = droite − gauche + 1 décroît de 6 à 3 puis 1 sur tableau=[4,9,18,23,37,41], cible=23 → terminaison prouvée (cible trouvée).
- Méthode : montrer que V décroît strictement à chaque étape.
- Cas limite : cible absente (ex. 38) → V décroît 6→3→1→0, la boucle s'arrête sans trouver.

### Exercice 9
- Capacité mobilisée : P-ALGO-03.
- Réponse attendue : distances calculées, 3 plus proches = A(3,2) B(5,4) A(2,3), vote A=2 B=1, classe "A".
- Méthode : distance euclidienne, tri, vote majoritaire.
- Cas limite : k=2 avec égalité de vote → résultat indéterminé.

## Corrigé du TP
- Donnée dichotomie : `tableau=[4,9,18,23,37,41], cible=37` → trouvé indice 4.
- Donnée glouton : `pièces=[10,5,2,1], montant=28` → 10+10+5+2+1 (5 pièces).
- Donnée k-NN : `voisins=[rouge:1.2, bleu:2.0, rouge:2.4], k=3` → classe rouge.

## Corrigé de l évaluation
- Question 1 : milieux 18 puis 37 -> trouvé indice 4.
- Question 2 : le variant V = droite − gauche + 1 décroît de 6 à 3 → terminaison (cible trouvée).
- Question 3 : 28 = 10 + 10 + 5 + 2 + 1 (5 pièces).
- Question 4 : rouge (2 voix) vs bleu (1) → classe rouge.
