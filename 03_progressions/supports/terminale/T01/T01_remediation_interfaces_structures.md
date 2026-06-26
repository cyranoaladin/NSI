---
title: "T01 - fiche remédiation - Interfaces de structures abstraites"
level: "terminale"
sequence_id: "T01"
document_type: "remediation"
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

# T01 - fiche remédiation - Interfaces de structures abstraites

## Objectifs
- Comprendre la notion : interface, implémentation, pile et file.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : T-STRUCT-01A, T-STRUCT-01B, T-STRUCT-01C.

## Capacités officielles
- T-STRUCT-01A
- T-STRUCT-01B
- T-STRUCT-01C
## Diagnostic rapide
La remédiation commence par une question courte qui cible l'erreur la plus fréquente.

## Exemple
Une pile expose `push`, `pop`, `is_empty`. Qu'elle utilise une liste Python ou une liste chaînée ne doit pas modifier le code utilisateur.

## Exercices
1. Refaire le cas guidé avec une valeur plus petite.
2. Compléter une justification à trous.
3. Résoudre un cas voisin sans aide.

## Corrigé
Les opérations publiques appartiennent à l'interface. `_items` et `len(_items)` révèlent le choix interne et ne doivent pas apparaître dans le code client.

## Erreurs fréquentes
- Ne pas nommer la convention.
- Sauter une étape de méthode.
- Croire qu'un seul exemple suffit à prouver une règle.

## Remédiation
L'élève doit verbaliser l'erreur initiale, corriger sa démarche, puis noter une règle personnelle de vigilance.

## Différenciation
Socle : justification à trous. Standard : cas voisin. Approfondissement : création d'un piège et de sa correction.

## Statut de revue
Document réel de première tranche, non publié et non validé. Une revue humaine indépendante reste nécessaire avant toute promotion de statut.
