---
title: "T01 - TP - Interfaces de structures abstraites"
level: "terminale"
sequence_id: "T01"
document_type: "tp"
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

# T01 - TP - Interfaces de structures abstraites

## Objectifs
- Comprendre la notion : interface, implémentation, pile et file.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : T-STRUCT-01A, T-STRUCT-01B, T-STRUCT-01C.

## Capacités officielles
- T-STRUCT-01A
- T-STRUCT-01B
- T-STRUCT-01C
## Fichiers et environnement
Le travail peut être réalisé dans un fichier Python local ou dans le carnet de bord selon la salle disponible.

## Exemple
Une pile expose `push`, `pop`, `is_empty`. Qu'elle utilise une liste Python ou une liste chaînée ne doit pas modifier le code utilisateur.

## Travail demandé
- Lire l'énoncé et repérer l'entrée, la sortie et les cas limites.
- Écrire ou compléter une fonction courte.
- Prévoir deux tests ordinaires et un test de bord.
- Copier la sortie des tests dans le carnet.

## Exercices
Classer `push`, `_items`, `pop`, `len(_items)` et `is_empty` selon interface ou implémentation, puis justifier chaque choix.

## Corrigé
Les opérations publiques appartiennent à l'interface. `_items` et `len(_items)` révèlent le choix interne et ne doivent pas apparaître dans le code client.

## Tests minimaux
Un test ordinaire, un test limite et un test d'erreur contrôlée doivent être écrits ou expliqués.

## Erreurs fréquentes
- Tester seulement le cas donné dans l'énoncé.
- Modifier l'interface demandée au lieu de corriger l'implémentation.
- Ne pas noter la sortie obtenue.

## Remédiation
Fournir une fonction presque complète et demander d'ajouter seulement les tests manquants.

## Différenciation
Socle : squelette guidé. Standard : fonction et tests. Approfondissement : ajout d'un test qui échoue avant correction.

## Statut de revue
Document réel de première tranche, non publié et non validé. Une revue humaine indépendante reste nécessaire avant toute promotion de statut.
