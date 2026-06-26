---
title: "T01 - cours - Interfaces de structures abstraites"
level: "terminale"
sequence_id: "T01"
document_type: "cours"
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

# T01 - cours - Interfaces de structures abstraites

## Objectifs
- Comprendre la notion : interface, implémentation, pile et file.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : T-STRUCT-01A, T-STRUCT-01B, T-STRUCT-01C.

## Capacités officielles
- T-STRUCT-01A
- T-STRUCT-01B
- T-STRUCT-01C
## Situation-problème
Un programme utilisateur veut ajouter et retirer des éléments sans dépendre de la représentation interne. La séance distingue les opérations promises par l'interface et les choix d'implémentation.

## Déroulé proposé
1. Question flash individuelle sur la notion.
2. Mise en commun des critères de réussite.
3. Exemple guidé au tableau avec verbalisation de la méthode.
4. Exercice court réalisé seul puis comparé en binôme.
5. Synthèse écrite dans la trace.

## Exemple
Une pile expose `push`, `pop`, `is_empty`. Qu'elle utilise une liste Python ou une liste chaînée ne doit pas modifier le code utilisateur.

## Méthode
- Identifier la donnée manipulée et la convention utilisée.
- Écrire les étapes intermédiaires, pas seulement le résultat.
- Vérifier la réponse avec une méthode inverse ou un test simple.

## Exercices
Classer `push`, `_items`, `pop`, `len(_items)` et `is_empty` selon interface ou implémentation, puis justifier chaque choix.

## Corrigé
Les opérations publiques appartiennent à l'interface. `_items` et `len(_items)` révèlent le choix interne et ne doivent pas apparaître dans le code client.

## Erreurs fréquentes
- Donner un résultat sans convention ou sans taille de registre.
- Confondre écriture et valeur représentée.
- Tester seulement un cas ordinaire et oublier un cas limite.

## Remédiation
Reprendre un exemple plus petit, faire verbaliser la convention, puis demander une vérification par la méthode inverse.

## Différenciation
Socle : un exemple guidé et une grille de méthode. Standard : trois exercices autonomes. Approfondissement : produire un contre-exemple ou un test de bord.

## Statut de revue
Document réel de première tranche, non publié et non validé. Une revue humaine indépendante reste nécessaire avant toute promotion de statut.
