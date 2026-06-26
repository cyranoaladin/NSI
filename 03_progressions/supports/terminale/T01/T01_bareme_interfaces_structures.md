---
title: "T01 - barème - Interfaces de structures abstraites"
level: "terminale"
sequence_id: "T01"
document_type: "bareme"
status: "needs_review"
version: "0.1.0"
source: "BO 2019 ; source possible Drive : Documents_DRIVE/2_Tles NSI/2_Projet1_TAD et POO/1_TD1_Structure de données abstraite.odt"
theme: "Structures de données"
notion: "interface, implémentation, pile et file"
objectifs: ["Travailler la capacité ciblée", "Produire une trace vérifiable", "Identifier les erreurs fréquentes"]
private_data: false
official_program:
  capacities: ["T-STRUCT-01A", "T-STRUCT-01B", "T-STRUCT-01C"]
---

# T01 - barème - Interfaces de structures abstraites

## Objectifs
- Comprendre la notion : interface, implémentation, pile et file.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : T-STRUCT-01A, T-STRUCT-01B, T-STRUCT-01C.

## Capacités officielles
- T-STRUCT-01A
- T-STRUCT-01B
- T-STRUCT-01C
## Barème
La note courte est ramenée à 10 points.

## Exemple
Une pile expose `push`, `pop`, `is_empty`. Qu'elle utilise une liste Python ou une liste chaînée ne doit pas modifier le code utilisateur.

## Exercices évalués
Classer `push`, `_items`, `pop`, `len(_items)` et `is_empty` selon interface ou implémentation, puis justifier chaque choix.

## Corrigé
Les opérations publiques appartiennent à l'interface. `_items` et `len(_items)` révèlent le choix interne et ne doivent pas apparaître dans le code client.

## Répartition
- Question 1 : 2 points pour le vocabulaire exact.
- Question 2 : 3 points pour la méthode et le résultat.
- Question 3 : 3 points pour l'analyse et la justification.
- Question 4 : 2 points pour le test ou le cas limite.

## Erreurs fréquentes
- Accorder tous les points à un résultat non justifié.
- Ne pas distinguer erreur mineure de méthode et erreur de convention.

## Remédiation
Identifier la ligne du barème perdue, puis refaire uniquement la compétence concernée.

## Différenciation
Aménagement : accorder les points de méthode dès que les étapes sont correctement ordonnées, même si une erreur de calcul isolée apparaît.

## Statut de revue
Document réel de première tranche, non publié et non validé. Une revue humaine indépendante reste nécessaire avant toute promotion de statut.
