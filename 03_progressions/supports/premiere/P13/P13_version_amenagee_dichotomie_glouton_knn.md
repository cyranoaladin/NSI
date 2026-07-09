---
title: "P13 - version_amenagee - dichotomie, glouton et k-NN"
level: "premiere"
sequence_id: "P13"
document_type: "version_amenagee"
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

# P13 - Version aménagée - dichotomie, glouton et k-NN

## Aides intégrées
- Donnée fournie : `tableau=[4,9,18,23,37,41], cible=37 ; pièces=[10,5,2,1], montant=28 ; voisins=[rouge:1.2, bleu:2.0, rouge:2.4]`.
- Mots utiles : dichotomie, variant droite-gauche, glouton, choix local, k-NN.
- Méthode guidée : calculer milieu puis réduire intervalle puis montrer que droite-gauche diminue.

## Bloc 1 — Dichotomie et variant (P-ALGO-04)
1. Recopier la donnée utile : `tableau=[4,9,18,23,37,41], cible=37`.
2. Calculer milieu puis réduire intervalle → milieux 18 puis 37 → trouvé indice 4.
3. Montrer que le variant V = droite − gauche + 1 décroît de 6 à 3 → terminaison.
4. Cas limite : cible absente (ex. 38) → V décroît 6→3→1→0.

## Bloc 2 — Glouton (P-ALGO-05)
1. Recopier la donnée utile : `pièces=[10,5,2,1], montant=28`.
2. Prendre la plus grande pièce possible → 28 = 10+10+5+2+1 (5 pièces).
3. Cas limite : pièce 1 absente → le glouton peut échouer.

## Bloc 3 — k-NN (P-ALGO-03)
1. Recopier la donnée utile : `voisins=[rouge:1.2, bleu:2.0, rouge:2.4], k=3`.
2. Voter parmi les 3 plus proches → rouge 2 voix vs bleu 1 → classe rouge.
3. Cas limite : k pair → égalité de vote possible.

## Réponses rapides
- Réponse 1 (P-ALGO-04) : milieux 18 puis 37 -> trouvé indice 4 ; variant V décroît de 6 à 3.
- Réponse 2 (P-ALGO-05) : 28 = 10+10+5+2+1 (5 pièces).
- Réponse 3 (P-ALGO-03) : rouge 2 voix vs bleu 1 → classe rouge.
