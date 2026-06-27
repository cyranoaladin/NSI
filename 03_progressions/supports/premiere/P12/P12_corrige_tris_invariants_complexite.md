---
title: "P12 - corrige - tris, invariants et complexité"
level: "premiere"
sequence_id: "P12"
document_type: "corrige"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "tris, invariants et complexité"
notion: "tris, invariants et complexité"
private_data: false
official_program:
  capacities:
    - "P-ALGO-02A"
    - "P-ALGO-02B"
    - "P-ALGO-02C"
    - "P-ALGO-02D"
---

# P12 - Corrigé - tris, invariants et complexité

## Corrigé du TD
### Exercice 1
- Réponse attendue : insertion après i=1 -> [17,42,23,17,9].
- Méthode : insérer la clé dans la partie gauche triée.
- Cas limite : liste vide.
### Exercice 2
- Réponse attendue : sélection place 9 en tête.
- Méthode : chercher le minimum du suffixe.
- Cas limite : liste déjà triée.
### Exercice 3
- Réponse attendue : invariant : indices < i triés.
- Méthode : écrire invariant gauche triée.
- Cas limite : doublons 17.
### Exercice 4
- Réponse attendue : pire cas quadratique.
- Méthode : compter comparaisons intuitives.
- Cas limite : liste vide.
### Exercice 5
- Réponse attendue : insertion après i=1 -> [17,42,23,17,9].
- Méthode : insérer la clé dans la partie gauche triée.
- Cas limite : liste déjà triée.
### Exercice 6
- Réponse attendue : sélection place 9 en tête.
- Méthode : chercher le minimum du suffixe.
- Cas limite : doublons 17.
### Exercice 7
- Réponse attendue : invariant : indices < i triés.
- Méthode : écrire invariant gauche triée.
- Cas limite : liste vide.
### Exercice 8
- Réponse attendue : pire cas quadratique.
- Méthode : compter comparaisons intuitives.
- Cas limite : liste déjà triée.

## Corrigé du TP
- Donnée : `temps=[42,17,23,17,9]`.
- Résultat principal : insertion après i=1 -> [17,42,23,17,9].
- Résultat secondaire : sélection place 9 en tête.

## Corrigé de l évaluation
- Question 1 : insertion après i=1 -> [17,42,23,17,9].
- Question 2 : sélection place 9 en tête.
- Question 3 : invariant : indices < i triés.
- Question 4 : pire cas quadratique.
