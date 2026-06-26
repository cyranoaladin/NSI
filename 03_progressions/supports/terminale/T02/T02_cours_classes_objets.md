---
title: "T02 - cours - Classes Python et état d’objet"
level: "terminale"
sequence_id: "T02"
document_type: "cours"
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

# T02 - cours - Classes Python et état d’objet

## Objectifs
- Comprendre la notion : classe, attribut, méthode, invariant.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : T-STRUCT-02A, T-STRUCT-02B, T-LANG-04A.

## Capacités officielles
- T-STRUCT-02A
- T-STRUCT-02B
- T-LANG-04A
## Situation-problème
Une structure comme une file conserve un état interne. La classe permet d'associer cet état aux méthodes qui le modifient, mais elle impose de préserver des invariants simples.

## Déroulé proposé
1. Question flash individuelle sur la notion.
2. Mise en commun des critères de réussite.
3. Exemple guidé au tableau avec verbalisation de la méthode.
4. Exercice court réalisé seul puis comparé en binôme.
5. Synthèse écrite dans la trace.

## Exemple
Dans une classe `Compteur`, l'attribut `_valeur` stocke l'état. La méthode `incrementer` modifie cet état, tandis que `valeur` permet de le lire sans l'exposer directement.

## Méthode
- Identifier la donnée manipulée et la convention utilisée.
- Écrire les étapes intermédiaires, pas seulement le résultat.
- Vérifier la réponse avec une méthode inverse ou un test simple.

## Exercices
Écrire une classe `CompteurBorne` avec une valeur initiale, une méthode `incrementer`, une méthode `reset` et un test qui vérifie que la valeur ne dépasse pas une borne.

## Corrigé
La correction accepte plusieurs noms d'attributs si l'interface est claire et si le test vérifie la borne après plusieurs appels.

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
