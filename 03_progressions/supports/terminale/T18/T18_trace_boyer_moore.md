---
title: "T18 - trace - Boyer-Moore"
level: "terminale"
sequence_id: "T18"
document_type: "trace"
tp_mode: "papier"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Boyer-Moore"
notion: "Boyer-Moore"
private_data: false
official_program:
  capacities:
    - "T-ALGO-05"
---

# T18 - Trace - Boyer-Moore

## Trace courte
- Donnée : `texte="BANANAS", motif="ANA", table mauvais caractère A->2, N->1`.
- Vocabulaire : motif, texte, table du mauvais caractère, comparaison droite à gauche, décalage.
- Étape 1 : prétraiter dernière position de chaque caractère.
- Étape 2 : comparer depuis la droite.
- Résultat de référence : table : A->2, N->1.

## Cas limites à mémoriser
- motif absent.
- motif plus long que texte.
- caractère absent du motif.

## Erreurs fréquentes
- comparaison gauche à droite.
- décalage nul.
- caractère absent oublié.

## Critères de réussite observables
- Capacité : T-ALGO-05.
- Résultat final : alignement 0 : N comparé à A -> décalage 1.
- Cas limite : motif absent.

## Table de trace TP papier Boyer-Moore
Ce document est une trace de TP papier : aucune ressource Python n est attendu.

| Alignement | Fenêtre du texte | Comparaison de droite à gauche | Mauvais caractère | Décalage calculé | Décision |
|---|---|---|---|---|---|
| 0 | `BAN` face à `ANA` | `N` du texte comparé à `A` du motif | `N` dernière position 1 | `max(1, 2-1)=1` | décaler de 1 |
| 1 | `ANA` face à `ANA` | `A`, puis `N`, puis `A` correspondent | aucun | 0 | motif trouvé à l indice 1 |
| 4 | `NAS` face à `ANA` | `S` comparé à `A` | `S` absent du motif | `max(1, 2-(-1))=3` | sortie du texte, motif absent après indice 1 |

## Pseudo-code papier
1. Construire `dernier = {"A": 2, "N": 1}` pour le motif `ANA`.
2. Placer le motif sous le texte `BANANAS` à l alignement `i`.
3. Comparer `motif[j]` et `texte[i+j]` en partant de `j = len(motif)-1`.
4. Si une différence apparaît, calculer `decalage = max(1, j - dernier.get(caractere, -1))`.
5. Si `j < 0`, le motif est trouvé à l indice `i`.

## Barème associé
- 2 points : table du mauvais caractère `A->2`, `N->1`.
- 3 points : comparaisons droite-gauche de l alignement 0.
- 3 points : alignement 1 et indice trouvé `1`.
- 2 points : cas motif absent `XYZ` ou caractère absent du motif.

## Corrigé question par question
### Corrigé question 1
Résultat attendu : table du mauvais caractère `{"A": 2, "N": 1}` pour le motif `ANA`.
- Table du mauvais caractère : `A -> 2`, `N -> 1`.
### Corrigé question 2
Résultat attendu : alignement `0`, comparaison `N` contre `A`, mauvais caractère `N`, Décalage calculé `max(1, 2-1)=1`.
- Alignement 0 : `N` est comparé à `A`, mauvais caractère `N`, décalage `1`.
### Corrigé question 3
Résultat attendu : alignement `1`, comparaisons `A/N/A`, motif `ANA` trouvé à l indice `1`.
- Alignement 1 : `ANA` correspond, motif trouvé à l indice `1`.
### Corrigé question 4
Résultat attendu : motif absent `XYZ`, caractère absent traité par `dernier.get(c, -1)` et décalage `j + 1`.
- Motif absent `XYZ` : un caractère absent du motif impose un décalage au moins égal à `j + 1`.

## Liens TD et évaluation
- TD lié : `T18_TD_boyer_moore.md`.
- Évaluation liée : `T18_evaluation_boyer_moore.md`.
- Aucune ressource Python n est attendue pour ce TP papier.
