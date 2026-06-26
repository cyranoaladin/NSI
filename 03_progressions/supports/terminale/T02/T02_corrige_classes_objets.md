---
title: "T02 - corrigé - Classes Python et état d’objet"
level: "terminale"
sequence_id: "T02"
document_type: "corrige"
status: "needs_review"
version: "0.1.0"
source: "BO 2019 ; source possible Drive : Documents_DRIVE/2_Tles NSI/2_Projet1_TAD et POO/5_Cours_POO.odt"
theme: "Structures de données"
notion: "classe, attribut, méthode, invariant"
objectifs: ["Travailler la capacité ciblée", "Produire une trace vérifiable", "Identifier les erreurs fréquentes"]
private_data: false
official_program:
  capacities: ["T-STRUCT-02A", "T-STRUCT-02B", "T-LANG-04A"]
---

# T02 - corrigé - Classes Python et état d’objet

## Objectifs
- Comprendre la notion : classe, attribut, méthode, invariant.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : T-STRUCT-02A, T-STRUCT-02B, T-LANG-04A.

## Capacités officielles
- T-STRUCT-02A
- T-STRUCT-02B
- T-LANG-04A
## Réponse attendue
La correction accepte plusieurs noms d'attributs si l'interface est claire et si le test vérifie la borne après plusieurs appels.

## Exemple
Dans une classe `Compteur`, l'attribut `_valeur` stocke l'état. La méthode `incrementer` modifie cet état, tandis que `valeur` permet de le lire sans l'exposer directement.

## Exercices corrigés
Écrire une classe `CompteurBorne` avec une valeur initiale, une méthode `incrementer`, une méthode `reset` et un test qui vérifie que la valeur ne dépasse pas une borne.

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
