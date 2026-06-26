---
title: "T01 - corrigé - Interfaces de structures abstraites"
level: "terminale"
sequence_id: "T01"
document_type: "corrige"
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

# T01 - corrigé - Interfaces de structures abstraites

## Objectifs
- Comprendre la notion : interface, implémentation, pile et file.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : T-STRUCT-01A, T-STRUCT-01B, T-STRUCT-01C.

## Capacités officielles
- T-STRUCT-01A
- T-STRUCT-01B
- T-STRUCT-01C
## Réponse attendue
Les opérations publiques appartiennent à l'interface. `_items` et `len(_items)` révèlent le choix interne et ne doivent pas apparaître dans le code client.

## Exemple
Une pile expose `push`, `pop`, `is_empty`. Qu'elle utilise une liste Python ou une liste chaînée ne doit pas modifier le code utilisateur.

## Exercices corrigés
Classer `push`, `_items`, `pop`, `len(_items)` et `is_empty` selon interface ou implémentation, puis justifier chaque choix.

## Corrigé détaillé
Une copie complète contient la méthode, le résultat et une phrase de contrôle. Les variantes sont acceptées si elles respectent la capacité officielle et ne changent pas le contrat demandé.

## Barème indicatif
- Méthode explicite : 40 %.
- Résultat correct : 30 %.
- Justification ou test : 20 %.
- Présentation lisible : 10 %.

## Erreurs fréquentes
- Résultat juste mais non justifié.
- Confusion de vocabulaire.
- Absence de vérification.

## Remédiation
Reprendre la question avec une donnée plus simple et faire nommer l'erreur corrigée.

## Différenciation
Socle : correction guidée. Standard : correction autonome. Approfondissement : proposer une variante acceptable et la justifier.

## Statut de revue
Document réel de première tranche, non publié et non validé. Une revue humaine indépendante reste nécessaire avant toute promotion de statut.
