---
title: "T09 - TD - Bases relationnelles, clés et contraintes"
level: "terminale"
sequence_id: "T09"
document_type: "td"
status: "needs_review"
version: "0.2.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Bases de données"
notion: "tables, clés primaires, clés étrangères, contraintes"
objectifs:
  - "identifier la clé primaire de chaque table"
  - "repérer la clé étrangère Note.id_eleve"
  - "signaler une référence vers un élève absent"
  - "distinguer contrainte de domaine et contrainte de référence"
private_data: false
official_program:
  capacities:
    - "T-BDD-01A"
    - "T-BDD-01B"
    - "T-BDD-01C"
    - "T-BDD-02"
---

# T09 - TD - Bases relationnelles, clés et contraintes

## Objectifs
- O1 : identifier la clé primaire de chaque table.
- O2 : repérer la clé étrangère Note.id_eleve.
- O3 : signaler une référence vers un élève absent.
- O4 : distinguer contrainte de domaine et contrainte de référence.

## Capacités officielles
- T-BDD-01A
- T-BDD-01B
- T-BDD-01C
- T-BDD-02

## Situation de travail
Un lycée modélise Eleve(id_eleve, nom, classe) et Note(id_note, id_eleve, matiere, note). Il faut identifier clés et contraintes.

## Données de référence
`Eleve(1, "E2", "1G1"), Note(10, 1, "NSI", 15), Note(11, 9, "NSI", 12)`

## Exercices
### Exercice 1
- Objectif travaillé : O1.
- Capacité officielle : T-BDD-01A.
- Énoncé : À partir de la donnée de référence, identifier la clé primaire de chaque table et écrire la justification.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 2
- Objectif travaillé : O2.
- Capacité officielle : T-BDD-01B.
- Énoncé : Modifier une valeur de la donnée puis repérer la clé étrangère Note.id_eleve sans changer la méthode.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 3
- Objectif travaillé : O3.
- Capacité officielle : T-BDD-01C.
- Énoncé : Construire un contre-exemple qui montre pourquoi il faut signaler une référence vers un élève absent.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 4
- Objectif travaillé : O4.
- Capacité officielle : T-BDD-02.
- Énoncé : Analyser l'erreur fréquente « utiliser le nom comme clé primaire » et la corriger.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 5
- Objectif travaillé : O1.
- Capacité officielle : T-BDD-01A.
- Énoncé : Comparer deux solutions d'élèves : l'une applique identifier la clé primaire de chaque table, l'autre conclut directement.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 6
- Objectif travaillé : O2.
- Capacité officielle : T-BDD-01B.
- Énoncé : Traiter le cas limite associé à « accepter une note hors 0..20 » avec une donnée minimale.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 7
- Objectif travaillé : O3.
- Capacité officielle : T-BDD-01C.
- Énoncé : Rédiger une trace courte expliquant distinguer contrainte de domaine et contrainte de référence.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 8
- Objectif travaillé : O4.
- Capacité officielle : T-BDD-02.
- Énoncé : Créer une nouvelle donnée de test et vérifier que la méthode reste valable.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.

## Corrigé indicatif
### Corrigé exercice 1
- Méthode : isoler la donnée, appliquer l’objectif O1, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « identifier la clé primaire de chaque table » et citer T-BDD-01A.
- Contrôle : rejeter la solution si elle contient l’erreur « utiliser le nom comme clé primaire ».
### Corrigé exercice 2
- Méthode : isoler la donnée, appliquer l’objectif O2, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « repérer la clé étrangère Note.id_eleve » et citer T-BDD-01B.
- Contrôle : rejeter la solution si elle contient l’erreur « accepter une note hors 0..20 ».
### Corrigé exercice 3
- Méthode : isoler la donnée, appliquer l’objectif O3, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « signaler une référence vers un élève absent » et citer T-BDD-01C.
- Contrôle : rejeter la solution si elle contient l’erreur « insérer une note pour un élève absent ».
### Corrigé exercice 4
- Méthode : isoler la donnée, appliquer l’objectif O4, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « distinguer contrainte de domaine et contrainte de référence » et citer T-BDD-02.
- Contrôle : rejeter la solution si elle contient l’erreur « confondre clé primaire et clé étrangère ».
### Corrigé exercice 5
- Méthode : isoler la donnée, appliquer l’objectif O1, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « identifier la clé primaire de chaque table » et citer T-BDD-01A.
- Contrôle : rejeter la solution si elle contient l’erreur « utiliser le nom comme clé primaire ».
### Corrigé exercice 6
- Méthode : isoler la donnée, appliquer l’objectif O2, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « repérer la clé étrangère Note.id_eleve » et citer T-BDD-01B.
- Contrôle : rejeter la solution si elle contient l’erreur « accepter une note hors 0..20 ».
### Corrigé exercice 7
- Méthode : isoler la donnée, appliquer l’objectif O3, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « signaler une référence vers un élève absent » et citer T-BDD-01C.
- Contrôle : rejeter la solution si elle contient l’erreur « insérer une note pour un élève absent ».
### Corrigé exercice 8
- Méthode : isoler la donnée, appliquer l’objectif O4, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « distinguer contrainte de domaine et contrainte de référence » et citer T-BDD-02.
- Contrôle : rejeter la solution si elle contient l’erreur « confondre clé primaire et clé étrangère ».

## Erreurs fréquentes et remédiation
- EF1 : utiliser le nom comme clé primaire. Remédiation : refaire l’exercice 1 avec la donnée modifiée par le professeur.
- EF2 : accepter une note hors 0..20. Remédiation : refaire l’exercice 2 avec la donnée modifiée par le professeur.
- EF3 : insérer une note pour un élève absent. Remédiation : refaire l’exercice 3 avec la donnée modifiée par le professeur.
- EF4 : confondre clé primaire et clé étrangère. Remédiation : refaire l’exercice 4 avec la donnée modifiée par le professeur.

## Différenciation
- Socle : exercices 1 à 4 avec étapes visibles.
- Standard : exercices 1 à 6 avec justification complète.
- Expert : exercices 7 et 8 avec nouvelle donnée et contrôle autonome.
