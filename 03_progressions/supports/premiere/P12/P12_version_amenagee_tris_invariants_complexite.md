---
title: "P12 - version_amenagee - tris, invariants et complexité"
level: "premiere"
sequence_id: "P12"
document_type: "version_amenagee"
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

# P12 - Version aménagée - tris, invariants et complexité

## Aides intégrées
- Donnée fournie : `temps=[42,17,23,17,9]`.
- Mots utiles : tri par insertion, tri par sélection, invariant, variant, coût quadratique.
- Méthode guidée : insérer la clé dans la partie gauche triée puis chercher le minimum du suffixe.

## Exercice guidé
1. Recopier la donnée utile.
2. Choisir la capacité : P-ALGO-02A ou P-ALGO-02B.
3. Compléter le résultat : insertion après i=1 -> [17,42,23,17,9].
4. Cocher le cas limite : liste vide.

## Réponses rapides
- Réponse 1 : insertion après i=1 -> [17,42,23,17,9].
- Réponse 2 : sélection place 9 en tête.
- Réponse 3 : invariant : indices < i triés.
