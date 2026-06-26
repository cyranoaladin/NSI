---
title: "T02 - barème - Classes Python et état d’objet"
level: "terminale"
sequence_id: "T02"
document_type: "bareme"
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

# T02 - barème - Classes Python et état d’objet

## Objectifs
- Comprendre la notion : classe, attribut, méthode, invariant.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : T-STRUCT-02A, T-STRUCT-02B, T-LANG-04A.

## Capacités officielles
- T-STRUCT-02A
- T-STRUCT-02B
- T-LANG-04A
## Barème
La note courte est ramenée à 10 points.

## Exemple
Dans une classe `Compteur`, l'attribut `_valeur` stocke l'état. La méthode `incrementer` modifie cet état, tandis que `valeur` permet de le lire sans l'exposer directement.

## Exercices évalués
Écrire une classe `CompteurBorne` avec une valeur initiale, une méthode `incrementer`, une méthode `reset` et un test qui vérifie que la valeur ne dépasse pas une borne.

## Corrigé
La correction accepte plusieurs noms d'attributs si l'interface est claire et si le test vérifie la borne après plusieurs appels.

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
