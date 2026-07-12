---
title: "T05 - barème - Mesures et parcours d'arbres complément"
level: "terminale"
sequence_id: "T05"
document_type: "bareme"
status: "needs_review"
version: "0.4.1"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Arbres et algorithmes"
notion: "arbre binaire, taille, hauteur, feuilles, parcours en largeur, file"
private_data: false
official_program:
  capacities:
    - "T-STRUCT-04B"
    - "T-ALGO-01A"
    - "T-ALGO-01B"
    - "T-ALGO-01D"
---

# T05 - Barème - Mesures et parcours d'arbres complément

## Barème question par question

### Barème question 1 — Mesures sur papier (T-STRUCT-04B) — 5 points
- 1.a) Taille et hauteur de B : 2 points (1 pt taille correcte = 9, 1 pt hauteur correcte = 3 avec chemin le plus long cité).
- 1.b) Feuilles de B : 2 points (1 pt liste complète {10, 35, 45, 80}, 1 pt aucun noeud interne inclus par erreur).
- 1.c) Arbre réduit au noeud 99 : 1 point (taille = 1, hauteur = 0, feuilles = {99}).

### Barème question 2 — Calcul récursif de la taille (T-ALGO-01A) — 5 points
- 2.a) Déroulement de taille(50) : 3 points (1 pt structure récursive posée, 1 pt au moins 3 niveaux détaillés, 1 pt résultat final = 9).
- 2.b) Variant de terminaison : 2 points (1 pt variant nommé = taille du sous-arbre, 1 pt justification de la terminaison en une phrase).

### Barème question 3 — Calcul récursif de la hauteur (T-ALGO-01B) — 5 points
- 3.a) Déroulement de hauteur(50) : 3 points (1 pt appels récursifs détaillés pour le sous-arbre gauche, 1 pt max identifié à chaque noeud, 1 pt résultat final = 3).
- 3.b) Convention hauteur arbre vide : 2 points (1 pt hauteur d'une feuille = 1 avec convention 0, 1 pt explication : convention -1 donne hauteur feuille = 0 qui correspond au nombre d'arêtes).

### Barème question 4 — Parcours en largeur (T-ALGO-01D) — 5 points
- 4.a) Déroulement BFS : 3 points (1 pt initialisation correcte de la file, 1 pt au moins 4 étapes complètes, 1 pt résultat final = [50, 30, 70, 20, 40, 80, 10, 35, 45]).
- 4.b) Structure de données : 1 point (file FIFO, pas une pile car l'ordre d'arrivée = ordre de traitement).
- 4.c) BFS sur arbre vide : 1 point (résultat = liste vide).

## Total : 20 points

## Critères de réussite observables
- La donnée de départ (arbre B) est recopiée exactement.
- Chaque question produit un résultat numérique ou une trace vérifiable.
- Au moins un cas limite (arbre vide, feuille seule, convention de hauteur) est tranché.

## Erreurs fréquentes
- Confondre taille et hauteur.
- Oublier les feuilles dans le dénombrement.
- Utiliser une pile au lieu d'une file pour le BFS.
- Convention de hauteur arbre vide mal appliquée.

## Cas limites travaillés
- Arbre réduit à un seul noeud.
- Arbre vide (taille 0, hauteur -1, BFS = []).
- Convention de hauteur 0 vs -1 pour l'arbre vide.
