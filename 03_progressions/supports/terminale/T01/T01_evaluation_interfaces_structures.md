---
title: "T01 - évaluation courte - Interfaces de structures abstraites"
level: "terminale"
sequence_id: "T01"
document_type: "evaluation"
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

# T01 - évaluation courte - Interfaces de structures abstraites

## Objectifs
- Comprendre la notion : interface, implémentation, pile et file.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : T-STRUCT-01A, T-STRUCT-01B, T-STRUCT-01C.

## Capacités officielles
- T-STRUCT-01A
- T-STRUCT-01B
- T-STRUCT-01C
## Durée et consignes
Durée conseillée : 20 minutes. Répondre sans document, sauf consigne contraire du professeur.

## Exemple
Une pile expose `push`, `pop`, `is_empty`. Qu'elle utilise une liste Python ou une liste chaînée ne doit pas modifier le code utilisateur.

## Exercices
1. Restituer la définition ou la convention utilisée.
2. Résoudre un cas d'application directe.
3. Justifier une réponse d'élève.
4. Proposer un test, une vérification ou un cas limite.

## Corrigé
Les opérations publiques appartiennent à l'interface. `_items` et `len(_items)` révèlent le choix interne et ne doivent pas apparaître dans le code client.

## Critères de réussite
La réponse doit être courte, lisible et vérifiable. Le résultat seul ne suffit pas pour obtenir tous les points.

## Erreurs fréquentes
- Omettre la justification.
- Répondre avec une convention différente de celle demandée.
- Ne pas traiter le cas limite.

## Remédiation
Après correction, refaire la question 2 avec une donnée voisine et écrire la phrase de justification.

## Différenciation
Version standard : quatre questions. Version aménagée : mêmes capacités avec étapes intermédiaires et espace de réponse structuré.

## Statut de revue
Document réel de première tranche, non publié et non validé. Une revue humaine indépendante reste nécessaire avant toute promotion de statut.
