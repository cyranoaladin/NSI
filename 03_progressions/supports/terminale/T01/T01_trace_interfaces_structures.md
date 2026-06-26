---
title: "T01 - trace - Interfaces de structures abstraites"
level: "terminale"
sequence_id: "T01"
document_type: "trace"
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

# T01 - trace - Interfaces de structures abstraites

## Objectifs
- Comprendre la notion : interface, implémentation, pile et file.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : T-STRUCT-01A, T-STRUCT-01B, T-STRUCT-01C.

## Capacités officielles
- T-STRUCT-01A
- T-STRUCT-01B
- T-STRUCT-01C
## Notions essentielles
Cette trace fixe les définitions et les gestes à refaire sans le support de cours.

## Exemple
Une pile expose `push`, `pop`, `is_empty`. Qu'elle utilise une liste Python ou une liste chaînée ne doit pas modifier le code utilisateur.

## Méthode à savoir refaire
1. Nommer la convention.
2. Écrire l'entrée et la sortie attendue.
3. Justifier chaque transformation.
4. Vérifier par calcul inverse, test ou table complète.

## Exercices
Classer `push`, `_items`, `pop`, `len(_items)` et `is_empty` selon interface ou implémentation, puis justifier chaque choix.

## Corrigé
Les opérations publiques appartiennent à l'interface. `_items` et `len(_items)` révèlent le choix interne et ne doivent pas apparaître dans le code client.

## Erreurs fréquentes
- Recopier un résultat sans justification.
- Oublier le cas limite demandé.
- Utiliser un vocabulaire imprécis.

## Remédiation
Relire la méthode, refaire l'exemple avec une valeur voisine, puis écrire une phrase de justification complète.

## Différenciation
Socle : méthode en quatre étapes. Standard : exercice voisin. Approfondissement : inventer une question qui piège une erreur fréquente.

## Statut de revue
Document réel de première tranche, non publié et non validé. Une revue humaine indépendante reste nécessaire avant toute promotion de statut.
