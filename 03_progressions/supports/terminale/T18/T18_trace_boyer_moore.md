---
title: "T18 - Trace - Boyer-Moore"
level: "terminale"
sequence_id: "T18"
document_type: "trace"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Recherche textuelle"
notion: "Boyer-Moore, mauvais caractère, trace d'exécution"
official_program:
  capacities:
    - "T-ALGO-05"
private_data: false
tp_mode: "papier"
---
# T18 - TP papier et trace Boyer-Moore

## Statut du support
Ce document est un TP papier : aucune ressource Python élève n’est attendue pour T18 dans cette passe. Le travail demandé est la construction manuelle de la table du mauvais caractère, la trace des alignements, le calcul des décalages et la justification du résultat.

## Liens avec les autres supports
- TD lié : `T18_TD_boyer_moore.md`, exercices sur table du mauvais caractère, trace et comparaison avec la recherche naïve.
- Évaluation liée : `T18_evaluation_boyer_moore.md`, questions sur motif trouvé, motif absent, pseudo-code et justification du décalage.

## Données de référence
- Texte : `CABAABABA`
- Motif : `ABA`
- Objectif : trouver la première occurrence du motif dans le texte avec la règle du mauvais caractère.

## Table du mauvais caractère

| Caractère du motif | Dernier indice dans `ABA` |
|---|---:|
| `A` | 2 |
| `B` | 1 |
| autre caractère | -1 |

## Trace complète - motif trouvé

| Alignement | Fenêtre du texte | Comparaison de droite à gauche | Mauvais caractère | Décalage calculé | Résultat |
|---:|---|---|---|---:|---|
| 0 | `CAB` | `A` du motif contre `B` du texte : échec à l'indice texte 2 | `B`, dernier indice 1 | `max(1, 2 - 1) = 1` | décaler d'une case |
| 1 | `ABA` | `A=A`, puis `B=B`, puis `A=A` | aucun | 0 | motif trouvé à l'indice 1 |

## Trace complète - motif absent

| Alignement | Fenêtre du texte | Comparaison de droite à gauche | Mauvais caractère | Décalage calculé | Résultat |
|---:|---|---|---|---:|---|
| 0 | `CCC` | `A` du motif contre `C` du texte : échec à l'indice texte 2 | `C`, absent du motif | `max(1, 2 - (-1)) = 3` | décaler de trois cases |
| 3 | `CCC` | `A` du motif contre `C` du texte : échec à l'indice texte 5 | `C`, absent du motif | `3` | fin sans occurrence |

## Pseudo-code

```text
construire derniere_position pour chaque caractère du motif
i = 0
tant que i <= len(texte) - len(motif):
    j = len(motif) - 1
    tant que j >= 0 et motif[j] == texte[i+j]:
        j = j - 1
    si j < 0:
        renvoyer i
    mauvais = texte[i+j]
    i = i + max(1, j - derniere_position.get(mauvais, -1))
renvoyer -1
```

## Comparaison avec la recherche naïve
- Recherche naïve sur `CABAABABA` et `ABA` : essayer les alignements 0 puis 1, avec des comparaisons de gauche à droite.
- Boyer-Moore mauvais caractère : à l'alignement 0, la comparaison commence à droite, voit `B` contre `A`, puis calcule directement un décalage de 1.
- Cas absent `CCCCCC` avec motif `ABA` : le mauvais caractère `C` absent du motif donne un décalage de 3 au lieu de tester chaque position.

## Critère de réussite
La trace est correcte si elle contient le texte, le motif, la table du mauvais caractère, chaque alignement, le mauvais caractère observé, le décalage calculé et le résultat final.

## Barème associé
- 2 points : table du mauvais caractère correcte pour `ABA` (`A -> 2`, `B -> 1`, autre caractère `-1`).
- 3 points : trace motif trouvé complète, avec alignement 0, mauvais caractère `B`, décalage 1, puis occurrence à l’indice 1.
- 2 points : trace motif absent complète sur `CCCCCC`, avec décalage 3 et conclusion `-1`.
- 2 points : pseudo-code cohérent avec comparaison de droite à gauche et règle `max(1, j - dernière_position)`.
- 1 point : comparaison claire avec la recherche naïve.

## Corrigé question par question
### Corrigé question 1
Pour le motif `ABA`, la table du mauvais caractère est `A -> 2`, `B -> 1`, et tout autre caractère vaut `-1`.

### Corrigé question 2
Sur `CABAABABA`, l’alignement 0 compare le `A` final du motif avec `B` dans le texte, calcule `max(1, 2 - 1) = 1`, puis l’alignement 1 vérifie `A=A`, `B=B`, `A=A`. Résultat attendu : motif trouvé à l’indice `1`, avec la trace `alignement 0 -> décalage 1 -> alignement 1`.

### Corrigé question 3
Sur `CCCCCC`, le caractère `C` est absent du motif. Le décalage vaut `max(1, 2 - (-1)) = 3`; après deux alignements, aucune occurrence n’est trouvée. Résultat : `-1`.

### Corrigé question 4
Résultat attendu : la recherche naïve teste les alignements `0, 1, 2, ...` de gauche à droite, alors que Boyer-Moore compare le motif par la droite et calcule un décalage. Sur `CCCCCC` avec motif `ABA`, la trace donne `alignement 0 -> décalage 3 -> alignement 3 -> résultat -1`, donc deux alignements au lieu de tester chaque position.
