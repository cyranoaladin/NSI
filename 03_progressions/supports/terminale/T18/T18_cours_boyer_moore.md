---
title: "T18 - cours - Boyer-Moore"
level: "terminale"
sequence_id: "T18"
document_type: "cours"
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

# T18 - Cours - Boyer-Moore

## Objectifs spécifiques
- Identifier les données utiles de la situation : texte="BANANAS", motif="ANA", table mauvais caractère A->2, N->1.
- Employer le vocabulaire : motif, texte, table du mauvais caractère, comparaison droite à gauche, décalage, trace complète.
- Produire une trace, une table, une valeur ou un pseudo-code vérifiable.

## Capacités officielles
- T-ALGO-05.

## Situation-problème
texte="BANANAS", motif="ANA", table mauvais caractère A->2, N->1

## À savoir
- motif.
- texte.
- table du mauvais caractère.
- comparaison droite à gauche.
- décalage.
- trace complète.
- pseudo-code.
- motif trouvé.

## Méthodes
- prétraiter dernière position de chaque caractère.
- comparer depuis la droite.
- calculer max(1, j - dernière_position).
- comparer avec recherche naïve.

## Exemples corrigés
### Exemple corrigé 1
- Donnée : `texte="BANANAS", motif="ANA", table mauvais caractère A->2, N->1`.
- Méthode : prétraiter dernière position de chaque caractère.
- Résultat attendu : table : A->2, N->1.
- Contrôle : capacité T-ALGO-05 et cas limite `motif absent`.
### Exemple corrigé 2
- Donnée : `texte="BANANAS", motif="ANA", table mauvais caractère A->2, N->1`.
- Méthode : comparer depuis la droite.
- Résultat attendu : alignement 0 : N comparé à A -> décalage 1.
- Contrôle : capacité T-ALGO-05 et cas limite `motif plus long que texte`.
### Exemple corrigé 3
- Donnée : `texte="BANANAS", motif="ANA", table mauvais caractère A->2, N->1`.
- Méthode : calculer max(1, j - dernière_position).
- Résultat attendu : alignement 1 : ANA trouvé.
- Contrôle : capacité T-ALGO-05 et cas limite `caractère absent du motif`.
### Exemple corrigé 4
- Donnée : `texte="BANANAS", motif="ANA", table mauvais caractère A->2, N->1`.
- Méthode : comparer avec recherche naïve.
- Résultat attendu : motif XYZ absent.
- Contrôle : capacité T-ALGO-05 et cas limite `motif absent`.

## Cas limites
- motif absent.
- motif plus long que texte.
- caractère absent du motif.

## Erreurs fréquentes
- comparaison gauche à droite.
- décalage nul.
- caractère absent oublié.

## Exercices intégrés
1. Identifier les données utiles dans `texte="BANANAS", motif="ANA", table mauvais caractère A->2, N->1`.
2. Appliquer : prétraiter dernière position de chaque caractère.
3. Appliquer : comparer depuis la droite.
4. Décider le cas limite `motif absent`.

## Critères de réussite observables
- Une capacité parmi T-ALGO-05 est citée et utilisée.
- Le résultat attendu est explicite : table : A->2, N->1.
- Le cas limite `motif plus long que texte` est tranché.

## Lien avec la progression
- Séance : T18-S1 à T18-S4.
- TD : `T18_TD_boyer_moore.md`.
- TP : `T18_tp_boyer_moore.md`.
- Évaluation : `T18_evaluation_boyer_moore.md`.
