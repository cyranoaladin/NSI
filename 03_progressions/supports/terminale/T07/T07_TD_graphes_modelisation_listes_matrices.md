---
title: "T07 - TD - Graphes : modélisation, listes et matrices"
level: "terminale"
sequence_id: "T07"
document_type: "td"
status: "needs_review"
version: "0.2.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Graphes"
notion: "sommets, arêtes, matrice et liste d’adjacence"
objectifs:
  - "dessiner le graphe non orienté"
  - "écrire la liste d’adjacence"
  - "construire la matrice 4 x 4"
  - "comparer accès à un voisin et test d’adjacence"
private_data: false
official_program:
  capacities:
    - "T-STRUCT-05A"
    - "T-STRUCT-05B"
    - "T-STRUCT-05C"
    - "T-STRUCT-05D"
---

# T07 - TD - Graphes : modélisation, listes et matrices

## Objectifs
- O1 : dessiner le graphe non orienté.
- O2 : écrire la liste d’adjacence.
- O3 : construire la matrice 4 x 4.
- O4 : comparer accès à un voisin et test d’adjacence.

## Capacités officielles
- T-STRUCT-05A
- T-STRUCT-05B
- T-STRUCT-05C
- T-STRUCT-05D

## Situation de travail
On modélise un réseau de salles A, B, C, D avec couloirs A-B, A-C, B-D. Il faut choisir une représentation et justifier ses coûts.

## Données de référence
`S = {A, B, C, D}, E = {(A,B), (A,C), (B,D)}`

## Exercices
### Exercice 1
- Objectif travaillé : O1.
- Capacité officielle : T-STRUCT-05A.
- Énoncé : À partir de la donnée de référence, dessiner le graphe non orienté et écrire la justification.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 2
- Objectif travaillé : O2.
- Capacité officielle : T-STRUCT-05B.
- Énoncé : Modifier une valeur de la donnée puis écrire la liste d’adjacence sans changer la méthode.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 3
- Objectif travaillé : O3.
- Capacité officielle : T-STRUCT-05C.
- Énoncé : Construire un contre-exemple qui montre pourquoi il faut construire la matrice 4 x 4.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 4
- Objectif travaillé : O4.
- Capacité officielle : T-STRUCT-05D.
- Énoncé : Analyser l'erreur fréquente « oublier la symétrie en non orienté » et la corriger.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 5
- Objectif travaillé : O1.
- Capacité officielle : T-STRUCT-05A.
- Énoncé : Comparer deux solutions d'élèves : l'une applique dessiner le graphe non orienté, l'autre conclut directement.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 6
- Objectif travaillé : O2.
- Capacité officielle : T-STRUCT-05B.
- Énoncé : Traiter le cas limite associé à « confondre sommet et arête » avec une donnée minimale.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 7
- Objectif travaillé : O3.
- Capacité officielle : T-STRUCT-05C.
- Énoncé : Rédiger une trace courte expliquant comparer accès à un voisin et test d’adjacence.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 8
- Objectif travaillé : O4.
- Capacité officielle : T-STRUCT-05D.
- Énoncé : Pour le graphe non orienté d’arêtes `(A,B)`, `(A,C)`, `(B,D)`, écrire la liste d’adjacence puis dire si `C` et `D` sont adjacents.
- Production attendue : `A:[B,C]`, `B:[A,D]`, `C:[A]`, `D:[B]`; résultat `C` et `D` non adjacents, contrôle par absence de `D` dans la liste de `C`.
- Critère de réussite : la conclusion est vérifiable par un pair.

## Corrigé indicatif
### Corrigé exercice 1
- Méthode : isoler la donnée, appliquer l’objectif O1, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « dessiner le graphe non orienté » et citer T-STRUCT-05A.
- Contrôle : rejeter la solution si elle contient l’erreur « oublier la symétrie en non orienté ».
### Corrigé exercice 2
- Méthode : isoler la donnée, appliquer l’objectif O2, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « écrire la liste d’adjacence » et citer T-STRUCT-05B.
- Contrôle : rejeter la solution si elle contient l’erreur « confondre sommet et arête ».
### Corrigé exercice 3
- Méthode : isoler la donnée, appliquer l’objectif O3, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « construire la matrice 4 x 4 » et citer T-STRUCT-05C.
- Contrôle : rejeter la solution si elle contient l’erreur « mettre des doublons dans la liste ».
### Corrigé exercice 4
- Méthode : isoler la donnée, appliquer l’objectif O4, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « comparer accès à un voisin et test d’adjacence » et citer T-STRUCT-05D.
- Contrôle : rejeter la solution si elle contient l’erreur « choisir une matrice sans discuter la densité ».
### Corrigé exercice 5
- Méthode : isoler la donnée, appliquer l’objectif O1, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « dessiner le graphe non orienté » et citer T-STRUCT-05A.
- Contrôle : rejeter la solution si elle contient l’erreur « oublier la symétrie en non orienté ».
### Corrigé exercice 6
- Méthode : isoler la donnée, appliquer l’objectif O2, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « écrire la liste d’adjacence » et citer T-STRUCT-05B.
- Contrôle : rejeter la solution si elle contient l’erreur « confondre sommet et arête ».
### Corrigé exercice 7
- Méthode : isoler la donnée, appliquer l’objectif O3, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « construire la matrice 4 x 4 » et citer T-STRUCT-05C.
- Contrôle : rejeter la solution si elle contient l’erreur « mettre des doublons dans la liste ».
### Corrigé exercice 8
- Méthode : isoler la donnée, appliquer l’objectif O4, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « comparer accès à un voisin et test d’adjacence » et citer T-STRUCT-05D.
- Contrôle : rejeter la solution si elle contient l’erreur « choisir une matrice sans discuter la densité ».

## Erreurs fréquentes et remédiation
- EF1 : oublier la symétrie en non orienté. Remédiation : refaire l’exercice 1 avec la donnée modifiée par le professeur.
- EF2 : confondre sommet et arête. Remédiation : refaire l’exercice 2 avec la donnée modifiée par le professeur.
- EF3 : mettre des doublons dans la liste. Remédiation : refaire l’exercice 3 avec la donnée modifiée par le professeur.
- EF4 : choisir une matrice sans discuter la densité. Remédiation : refaire l’exercice 4 avec la donnée modifiée par le professeur.

## Différenciation
- Socle : exercices 1 à 4 avec étapes visibles.
- Standard : exercices 1 à 6 avec justification complète.
- Expert : exercices 7 et 8 avec nouvelle donnée et contrôle autonome.
