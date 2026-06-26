---
title: "T02 - trace - Classes Python et état d’objet"
level: "terminale"
sequence_id: "T02"
document_type: "trace"
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

# T02 - trace - Classes Python et état d’objet

## Objectifs
- Comprendre la notion : classe, attribut, méthode, invariant.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : T-STRUCT-02A, T-STRUCT-02B, T-LANG-04A.

## Capacités officielles
- T-STRUCT-02A
- T-STRUCT-02B
- T-LANG-04A
## Notions essentielles
Cette trace fixe les définitions et les gestes à refaire sans le support de cours.

## Exemple
Dans une classe `Compteur`, l'attribut `_valeur` stocke l'état. La méthode `incrementer` modifie cet état, tandis que `valeur` permet de le lire sans l'exposer directement.

## Méthode à savoir refaire
1. Nommer la convention.
2. Écrire l'entrée et la sortie attendue.
3. Justifier chaque transformation.
4. Vérifier par calcul inverse, test ou table complète.

## Exercices
Écrire une classe `CompteurBorne` avec une valeur initiale, une méthode `incrementer`, une méthode `reset` et un test qui vérifie que la valeur ne dépasse pas une borne.

## Corrigé
La correction accepte plusieurs noms d'attributs si l'interface est claire et si le test vérifie la borne après plusieurs appels.

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
