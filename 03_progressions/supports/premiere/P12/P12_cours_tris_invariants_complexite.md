---
title: "P12 - cours - tris, invariants et complexité"
level: "premiere"
sequence_id: "P12"
document_type: "cours"
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

# P12 - Cours - tris, invariants et complexité

## Objectifs spécifiques
- Identifier les données utiles de la situation : temps=[42,17,23,17,9].
- Employer le vocabulaire : tri par insertion, tri par sélection, invariant, variant, coût quadratique, stabilité.
- Produire une trace, une table, une valeur ou un pseudo-code vérifiable.

## Capacités officielles
- P-ALGO-02A.
- P-ALGO-02B.
- P-ALGO-02C.
- P-ALGO-02D.

## Situation-problème
temps=[42,17,23,17,9]

## À savoir
- tri par insertion.
- tri par sélection.
- invariant.
- variant.
- coût quadratique.
- stabilité.
- doublon 17.

## Méthodes
- insérer la clé dans la partie gauche triée.
- chercher le minimum du suffixe.
- écrire invariant gauche triée.
- compter comparaisons intuitives.

## Exemples corrigés
### Exemple corrigé 1
- Donnée : `temps=[42,17,23,17,9]`.
- Méthode : insérer la clé dans la partie gauche triée.
- Résultat attendu : insertion après i=1 -> [17,42,23,17,9].
- Contrôle : capacité P-ALGO-02A et cas limite `liste vide`.
### Exemple corrigé 2
- Donnée : `temps=[42,17,23,17,9]`.
- Méthode : chercher le minimum du suffixe.
- Résultat attendu : sélection place 9 en tête.
- Contrôle : capacité P-ALGO-02B et cas limite `liste déjà triée`.
### Exemple corrigé 3
- Donnée : `temps=[42,17,23,17,9]`.
- Méthode : écrire invariant gauche triée.
- Résultat attendu : invariant : indices < i triés.
- Contrôle : capacité P-ALGO-02C et cas limite `doublons 17`.
### Exemple corrigé 4
- Donnée : `temps=[42,17,23,17,9]`.
- Méthode : compter comparaisons intuitives.
- Résultat attendu : pire cas quadratique.
- Contrôle : capacité P-ALGO-02D et cas limite `liste vide`.

## Cas limites
- liste vide.
- liste déjà triée.
- doublons 17.

## Erreurs fréquentes
- invariant confondu avec résultat.
- décalage oublié.
- coût linéaire annoncé.

## Exercices intégrés
1. Identifier les données utiles dans `temps=[42,17,23,17,9]`.
2. Appliquer : insérer la clé dans la partie gauche triée.
3. Appliquer : chercher le minimum du suffixe.
4. Décider le cas limite `liste vide`.

## Critères de réussite observables
- Une capacité parmi P-ALGO-02A, P-ALGO-02B, P-ALGO-02C, P-ALGO-02D est citée et utilisée.
- Le résultat attendu est explicite : insertion après i=1 -> [17,42,23,17,9].
- Le cas limite `liste déjà triée` est tranché.

## Lien avec la progression
- Séance : P12-S1 à P12-S4.
- TD : `P12_TD_tris_invariants_complexite.md`.
- TP : `P12_tp_tris_invariants_complexite.md`.
- Évaluation : `P12_evaluation_tris_invariants_complexite.md`.
