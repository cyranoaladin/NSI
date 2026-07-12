---
title: "T05 - TD - Mesures et parcours d'arbres complément"
level: "terminale"
sequence_id: "T05"
document_type: "td"
status: "needs_review"
version: "0.4.1"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Arbres et algorithmes"
notion: "arbre binaire, taille, hauteur, feuilles, parcours en largeur, file"
objectifs:
  - "Objectif O1 - Identifier précisément la représentation ou la structure en jeu"
  - "Objectif O2 - Appliquer une méthode disciplinaire complète"
  - "Objectif O3 - Justifier le résultat sur un cas différent"
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur observée"
private_data: false
official_program:
  capacities:
    - "T-STRUCT-04B"
    - "T-ALGO-01A"
    - "T-ALGO-01B"
    - "T-ALGO-01D"
---

# T05 - TD - Mesures et parcours d'arbres complément

## Capacités officielles atomiques

- T-STRUCT-04B : Évaluer quelques mesures des arbres binaires (taille, hauteur, feuilles). « Taille, hauteur et feuilles. »
- T-ALGO-01A : Calculer la taille d’un arbre. « Structure récursive adaptée. »
- T-ALGO-01B : Calculer la hauteur d’un arbre. « Cas arbre vide : hauteur conventionnelle -1 (ou 0 selon la convention). »
- T-ALGO-01D : Parcourir un arbre en largeur d'abord. « Lien avec file. »

## Arbre de référence (rappel)

```
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
```

Taille = 9, hauteur = 3, feuilles = {1, 4, 7, 13}, BFS = [8, 3, 10, 1, 6, 14, 4, 7, 13].

---

## Exercice 1 — Mesures sur papier (T-STRUCT-04B)

Soit l'arbre binaire A1 suivant :

```
        20
       /  \
      15    25
     / \   /
    12  18 22
   /      \
  9       23
```

**1.a)** Déterminer la taille de A1.

**1.b)** Déterminer la hauteur de A1. Préciser le plus long chemin.

**1.c)** Lister toutes les feuilles de A1.

**1.d)** Cas limite : donner la taille, la hauteur et les feuilles d’un arbre vide. Donner la taille, la hauteur et les feuilles d’un arbre réduit à une seule feuille de valeur 42.

---

## Exercice 2 — Calcul récursif de la taille (T-ALGO-01A)

Soit l'arbre binaire A2 suivant :

```
      5
     / \
    2   7
   /   / \
  1   6   9
         /
        8
```

**2.a)** Écrire la formule récursive de la taille. Préciser le cas de base.

**2.b)** Dérouler l’exécution de `taille(5)` sur A2. Montrer l'arbre des appels récursifs et le résultat de chaque appel.

**2.c)** Quel est le variant utilisé pour prouver la terminaison de l'algorithme ? Justifier que ce variant décroît strictement et atteint le cas de base.

**2.d)** On considère un arbre A3 réduit au seul noeud 42. Vérifier que `taille(42)` renvoie 1 en déroulant l'algorithme.

---

## Exercice 3 — Calcul récursif de la hauteur (T-ALGO-01B)

Soit l'arbre binaire A4 suivant :

```
        30
       /
      20
     /  \
    10   25
   /
  5
```

**3.a)** Quelle convention adopte-t-on pour la hauteur d’un arbre vide ? Justifier ce choix.

**3.b)** Écrire la formule récursive de la hauteur. Préciser le cas de base.

**3.c)** Dérouler l’exécution de `hauteur(30)` sur A4. Détailler chaque appel récursif.

**3.d)** Vérifier le résultat en identifiant le plus long chemin dans A4 et en comptant les arêtes.

**3.e)** Donner un arbre de hauteur 0 et un arbre de hauteur 1. Vérifier avec la formule récursive.

---

## Exercice 4 — Parcours en largeur d'abord (T-ALGO-01D)

Soit l'arbre binaire A5 suivant :

```
         1
        / \
       2   3
      / \   \
     4   5   6
    /       / \
   7       8   9
```

**4.a)** Expliquer pourquoi le parcours BFS nécessite une file et non une pile.

**4.b)** Dérouler le parcours BFS de A5. Compléter le tableau :

| Étape | File (avant défilement) | Noeud traité | Résultat partiel |
|-------|------------------------|--------------|-----------------|
| 1 | | | |
| 2 | | | |
| ... | | | |

**4.c)** Donner le résultat final du parcours BFS de A5.

**4.d)** On suppose que l'on remplace la file par une pile (LIFO : on dépile au lieu de défiler). Dérouler le parcours obtenu sur A5. Est-ce un parcours en largeur ? Quel type de parcours obtient-on ?

**4.e)** Quel est le résultat du parcours BFS d’un arbre vide ? D'un arbre à un seul noeud ?


## Objectifs


## Prérequis


## Situation-problème

Un biologiste modélise un arbre phylogénétique et doit calculer le nombre d'espèces (taille), la profondeur maximale (hauteur) et lister les espèces terminales (feuilles). Comment parcourir l'arbre ?

## Activité d’entrée

Dessiner un arbre binaire de 7 noeuds, compter ses feuilles et mesurer sa hauteur à la main avant de programmer.

## Exemple

Construction collective d'un arbre binaire de 5 noeuds et calcul de sa taille, hauteur et parcours en largeur.

## Exercices

Exercices de calcul de mesures et de parcours sur des arbres binaires variés.

## Corrigé

Les corrigés détaillés sont dans T05_corrige_arbres_mesures_parcours_complement.md.

## Erreurs fréquentes

- EF1 : oublier le cas de l'arbre vide dans la fonction récursive (retourner 0 ou -1).
- EF2 : confondre hauteur et profondeur d'un noeud dans l'arbre.
- EF3 : utiliser une liste au lieu d'une file (deque) pour le parcours en largeur.


## Remédiation

Exercice de remédiation : tracer l'exécution de taille() sur un arbre de 3 noeuds en notant chaque appel récursif.

## Différenciation

- Socle : exercices de base.
- Standard : exercices complets.
- Expert : exercice d'approfondissement.

## Critères de réussite

- Critère de réussite : taille() et hauteur() retournent les valeurs correctes sur l'arbre exemple.
- Critère de validation : le parcours en largeur utilise une file et produit l'ordre attendu.
- Observable : la preuve de terminaison identifie le variant de boucle.


## Séance(s) correspondante(s)

Séance dédiée.

### Exercice 1

Exercice complémentaire de consolidation.

### Exercice 2

Exercice complémentaire de consolidation.

### Exercice 3

Exercice complémentaire de consolidation.

### Exercice 4

Exercice complémentaire de consolidation.

### Exercice 5

Exercice complémentaire de consolidation.

### Exercice 6

Exercice complémentaire de consolidation.

### Exercice 7

Exercice complémentaire de consolidation.

### Exercice 8

Exercice complémentaire de consolidation.

