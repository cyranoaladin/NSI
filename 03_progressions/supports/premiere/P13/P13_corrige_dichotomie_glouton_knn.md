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
- Réponse attendue : milieux 18 puis 37 -> trouvé indice 4.
- Méthode : calculer milieu puis réduire intervalle.
- Cas limite : cible absente.
### Exercice 2
- Réponse attendue : 28 -> 10+10+5+2+1.
- Méthode : montrer que droite-gauche diminue.
- Cas limite : pièce 1 absente.
### Exercice 3
- Réponse attendue : rouge, bleu, rouge -> classe rouge.
- Méthode : prendre la plus grande pièce possible.
- Cas limite : égalité de vote.
### Exercice 4
- Réponse attendue : cible 40 absente -> non trouvé.
- Méthode : voter parmi k=3 voisins.
- Cas limite : cible absente.
### Exercice 5
- Réponse attendue : milieux 18 puis 37 -> trouvé indice 4.
- Méthode : calculer milieu puis réduire intervalle.
- Cas limite : pièce 1 absente.
### Exercice 6
- Réponse attendue : 28 -> 10+10+5+2+1.
- Méthode : montrer que droite-gauche diminue.
- Cas limite : égalité de vote.
### Exercice 7
- Réponse attendue : rouge, bleu, rouge -> classe rouge.
- Méthode : prendre la plus grande pièce possible.
- Cas limite : cible absente.
### Exercice 8
- Réponse attendue : cible 40 absente -> non trouvé.
- Méthode : voter parmi k=3 voisins.
- Cas limite : pièce 1 absente.

### Exercice 9
- Capacité mobilisée : P-ALGO-03.
- Réponse attendue : distances calculées, 3 plus proches = A(3,2) B(5,4) A(2,3), vote A=2 B=1, classe "A".
- Méthode : distance euclidienne, tri, vote majoritaire.
- Cas limite : k=2 avec égalité de vote → résultat indéterminé.

## Corrigé du TP
- Donnée : `tableau=[4,9,18,23,37,41], cible=37 ; pièces=[10,5,2,1], montant=28 ; voisins=[rouge:1.2, bleu:2.0, rouge:2.4]`.
- Résultat principal : milieux 18 puis 37 -> trouvé indice 4.
- Résultat secondaire : 28 -> 10+10+5+2+1.

## Corrigé de l évaluation
- Question 1 : milieux 18 puis 37 -> trouvé indice 4.
- Question 2 : 28 -> 10+10+5+2+1.
- Question 3 : rouge, bleu, rouge -> classe rouge.
- Question 4 : cible 40 absente -> non trouvé.
