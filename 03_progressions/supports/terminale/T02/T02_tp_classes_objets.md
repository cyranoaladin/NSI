---
title: "T02 - TP - Classes Python et état d’objet"
level: "terminale"
sequence_id: "T02"
document_type: "tp"
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

# T02 - TP - Classes Python et état d’objet

## Objectifs
- Comprendre la notion : classe, attribut, méthode, invariant.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : T-STRUCT-02A, T-STRUCT-02B, T-LANG-04A.

## Capacités officielles
- T-STRUCT-02A
- T-STRUCT-02B
- T-LANG-04A
## Fichiers et environnement
Le travail peut être réalisé dans un fichier Python local ou dans le carnet de bord selon la salle disponible.

## Exemple
Dans une classe `Compteur`, l'attribut `_valeur` stocke l'état. La méthode `incrementer` modifie cet état, tandis que `valeur` permet de le lire sans l'exposer directement.

## Travail demandé
- Lire l'énoncé et repérer l'entrée, la sortie et les cas limites.
- Écrire ou compléter une fonction courte.
- Prévoir deux tests ordinaires et un test de bord.
- Copier la sortie des tests dans le carnet.

## Exercices
Écrire une classe `CompteurBorne` avec une valeur initiale, une méthode `incrementer`, une méthode `reset` et un test qui vérifie que la valeur ne dépasse pas une borne.

## Corrigé
La correction accepte plusieurs noms d'attributs si l'interface est claire et si le test vérifie la borne après plusieurs appels.

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
