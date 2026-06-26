---
title: "T01 - TD - Interfaces de structures abstraites"
level: "terminale"
sequence_id: "T01"
document_type: "td"
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

# T01 - TD - Interfaces de structures abstraites

## Objectifs
- Comprendre la notion : interface, implémentation, pile et file.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : T-STRUCT-01A, T-STRUCT-01B, T-STRUCT-01C.

## Capacités officielles
- T-STRUCT-01A
- T-STRUCT-01B
- T-STRUCT-01C
## Consignes
Répondre sur feuille ou cahier. Chaque réponse doit contenir une justification courte.

## Exemple
Une pile expose `push`, `pop`, `is_empty`. Qu'elle utilise une liste Python ou une liste chaînée ne doit pas modifier le code utilisateur.

## Exercices
1. Question socle : reprendre l'exemple avec une valeur voisine.
2. Question standard : résoudre le cas nouveau et expliquer la méthode.
3. Question standard : comparer deux réponses d'élèves et choisir la plus solide.
4. Question approfondissement : produire un cas limite et sa correction.

## Corrigé
Les opérations publiques appartiennent à l'interface. `_items` et `len(_items)` révèlent le choix interne et ne doivent pas apparaître dans le code client.

## Justification attendue
La correction doit faire apparaître les étapes, le vocabulaire de la capacité et une vérification.

## Erreurs fréquentes
- Répondre par intuition sans preuve.
- Mélanger deux conventions.
- Ne pas vérifier la cohérence du résultat.

## Remédiation
Faire traiter seulement les questions 1 et 2, puis demander une verbalisation orale avant l'écrit.

## Différenciation
Socle : questions 1 et 2. Standard : questions 1 à 3. Approfondissement : question 4 et production d'une variante.

## Statut de revue
Document réel de première tranche, non publié et non validé. Une revue humaine indépendante reste nécessaire avant toute promotion de statut.
