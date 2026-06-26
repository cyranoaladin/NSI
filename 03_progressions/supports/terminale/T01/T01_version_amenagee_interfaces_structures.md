---
title: "T01 - version aménagée - Interfaces de structures abstraites"
level: "terminale"
sequence_id: "T01"
document_type: "version_amenagee"
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

# T01 - version aménagée - Interfaces de structures abstraites

## Objectifs
- Comprendre la notion : interface, implémentation, pile et file.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : T-STRUCT-01A, T-STRUCT-01B, T-STRUCT-01C.

## Capacités officielles
- T-STRUCT-01A
- T-STRUCT-01B
- T-STRUCT-01C
## Principe
Cette version conserve les mêmes capacités officielles mais réduit la charge de lecture.

## Exemple
Une pile expose `push`, `pop`, `is_empty`. Qu'elle utilise une liste Python ou une liste chaînée ne doit pas modifier le code utilisateur.

## Exercices
1. Question guidée avec étapes numérotées.
2. Application directe avec tableau de réponse.
3. Justification courte à choisir parmi deux formulations.

## Corrigé
Les opérations publiques appartiennent à l'interface. `_items` et `len(_items)` révèlent le choix interne et ne doivent pas apparaître dans le code client.

## Aides intégrées
Les mots importants sont rappelés dans l'énoncé et les emplacements de calcul sont séparés.

## Erreurs fréquentes
- Lire trop vite la convention.
- Oublier de remplir une étape intermédiaire.

## Remédiation
Faire relire la consigne, surligner l'entrée et la sortie, puis reprendre l'étape manquante.

## Différenciation
Socle : version aménagée. Standard : évaluation courte ordinaire. Approfondissement : question bonus sans pénaliser le socle.

## Statut de revue
Document réel de première tranche, non publié et non validé. Une revue humaine indépendante reste nécessaire avant toute promotion de statut.
