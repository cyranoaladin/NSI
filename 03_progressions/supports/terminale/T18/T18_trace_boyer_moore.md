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
---
# T18 - Trace Boyer-Moore

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
