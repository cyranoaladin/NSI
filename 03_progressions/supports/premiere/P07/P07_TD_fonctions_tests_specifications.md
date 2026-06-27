---
title: "P07 - TD - Fonctions, spécifications et tests"
level: "premiere"
sequence_id: "P07"
document_type: "td"
status: "needs_review"
version: "0.2.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Langage Python"
notion: "fonctions, paramètres, assertions, tests"
objectifs:
  - "écrire la signature et le rôle des paramètres"
  - "formuler précondition et postcondition"
  - "ajouter une assertion sur le prix négatif"
  - "tester cas nominal, zéro et entrée invalide"
private_data: false
official_program:
  capacities:
    - "P-LANG-01"
    - "P-LANG-02"
    - "P-LANG-03A"
    - "P-LANG-03B"
    - "P-LANG-03C"
    - "P-LANG-04"
    - "P-LANG-05"
---

# P07 - TD - Fonctions, spécifications et tests

## Objectifs
- O1 : écrire la signature et le rôle des paramètres.
- O2 : formuler précondition et postcondition.
- O3 : ajouter une assertion sur le prix négatif.
- O4 : tester cas nominal, zéro et entrée invalide.

## Capacités officielles
- P-LANG-01
- P-LANG-02
- P-LANG-03A
- P-LANG-03B
- P-LANG-03C
- P-LANG-04
- P-LANG-05

## Situation de travail
On veut écrire une fonction prix_ttc(ht, taux) utilisable dans plusieurs exercices, avec contrat, tests nominaux et tests d’erreur.

## Données de référence
`prix_ttc(80, 0.20), prix_ttc(0, 0.20), prix_ttc(-5, 0.20)`

## Exercices
### Exercice 1
- Objectif travaillé : O1.
- Capacité officielle : P-LANG-01.
- Énoncé : À partir de la donnée de référence, écrire la signature et le rôle des paramètres et écrire la justification.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 2
- Objectif travaillé : O2.
- Capacité officielle : P-LANG-02.
- Énoncé : Modifier une valeur de la donnée puis formuler précondition et postcondition sans changer la méthode.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 3
- Objectif travaillé : O3.
- Capacité officielle : P-LANG-03A.
- Énoncé : Construire un contre-exemple qui montre pourquoi il faut ajouter une assertion sur le prix négatif.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 4
- Objectif travaillé : O4.
- Capacité officielle : P-LANG-03B.
- Énoncé : Analyser l'erreur fréquente « écrire un print au lieu de return » et la corriger.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 5
- Objectif travaillé : O1.
- Capacité officielle : P-LANG-03C.
- Énoncé : Comparer deux solutions d'élèves : l'une applique écrire la signature et le rôle des paramètres, l'autre conclut directement.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 6
- Objectif travaillé : O2.
- Capacité officielle : P-LANG-04.
- Énoncé : Traiter le cas limite associé à « oublier le cas limite ht=0 » avec une donnée minimale.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 7
- Objectif travaillé : O3.
- Capacité officielle : P-LANG-05.
- Énoncé : Rédiger une trace courte expliquant tester cas nominal, zéro et entrée invalide.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 8
- Objectif travaillé : O4.
- Capacité officielle : P-LANG-01.
- Énoncé : Construire un cas de test numérique ou textuel inédit et vérifier que la méthode reste valable.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.

## Corrigé indicatif
### Corrigé exercice 1
- Méthode : isoler la donnée, appliquer l’objectif O1, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « écrire la signature et le rôle des paramètres » et citer P-LANG-01.
- Contrôle : rejeter la solution si elle contient l’erreur « écrire un print au lieu de return ».
### Corrigé exercice 2
- Méthode : isoler la donnée, appliquer l’objectif O2, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « formuler précondition et postcondition » et citer P-LANG-02.
- Contrôle : rejeter la solution si elle contient l’erreur « oublier le cas limite ht=0 ».
### Corrigé exercice 3
- Méthode : isoler la donnée, appliquer l’objectif O3, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « ajouter une assertion sur le prix négatif » et citer P-LANG-03A.
- Contrôle : rejeter la solution si elle contient l’erreur « tester seulement la valeur 80 ».
### Corrigé exercice 4
- Méthode : isoler la donnée, appliquer l’objectif O4, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « tester cas nominal, zéro et entrée invalide » et citer P-LANG-03B.
- Contrôle : rejeter la solution si elle contient l’erreur « modifier une variable globale depuis la fonction ».
### Corrigé exercice 5
- Méthode : isoler la donnée, appliquer l’objectif O1, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « écrire la signature et le rôle des paramètres » et citer P-LANG-03C.
- Contrôle : rejeter la solution si elle contient l’erreur « écrire un print au lieu de return ».
### Corrigé exercice 6
- Méthode : isoler la donnée, appliquer l’objectif O2, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « formuler précondition et postcondition » et citer P-LANG-04.
- Contrôle : rejeter la solution si elle contient l’erreur « oublier le cas limite ht=0 ».
### Corrigé exercice 7
- Méthode : isoler la donnée, appliquer l’objectif O3, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « ajouter une assertion sur le prix négatif » et citer P-LANG-05.
- Contrôle : rejeter la solution si elle contient l’erreur « tester seulement la valeur 80 ».
### Corrigé exercice 8
- Méthode : isoler la donnée, appliquer l’objectif O4, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « tester cas nominal, zéro et entrée invalide » et citer P-LANG-01.
- Contrôle : rejeter la solution si elle contient l’erreur « modifier une variable globale depuis la fonction ».

## Erreurs fréquentes et remédiation
- EF1 : écrire un print au lieu de return. Remédiation : refaire l’exercice 1 avec la donnée modifiée par le professeur.
- EF2 : oublier le cas limite ht=0. Remédiation : refaire l’exercice 2 avec la donnée modifiée par le professeur.
- EF3 : tester seulement la valeur 80. Remédiation : refaire l’exercice 3 avec la donnée modifiée par le professeur.
- EF4 : modifier une variable globale depuis la fonction. Remédiation : refaire l’exercice 4 avec la donnée modifiée par le professeur.

## Différenciation
- Socle : exercices 1 à 4 avec étapes visibles.
- Standard : exercices 1 à 6 avec justification complète.
- Expert : exercices 7 et 8 avec nouvelle donnée et contrôle autonome.
