---
title: "T06 - TD - Arbres binaires de recherche"
level: "terminale"
sequence_id: "T06"
document_type: "td"
status: "needs_review"
version: "0.2.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Structures de données"
notion: "recherche et insertion dans un ABR"
objectifs:
  - "suivre les comparaisons depuis la racine"
  - "justifier le chemin vers 6"
  - "placer 7 à droite de 6"
  - "repérer le cas dégénéré d’insertions triées"
private_data: false
official_program:
  capacities:
    - "T-ALGO-01E"
    - "T-ALGO-01F"
---

# T06 - TD - Arbres binaires de recherche

## Objectifs
- O1 : suivre les comparaisons depuis la racine.
- O2 : justifier le chemin vers 6.
- O3 : placer 7 à droite de 6.
- O4 : repérer le cas dégénéré d’insertions triées.

## Capacités officielles
- T-ALGO-01E
- T-ALGO-01F

## Situation de travail
Un ABR contient les clés 8, 3, 10, 1, 6. On recherche 6 puis on insère 7 en conservant l’invariant gauche < racine < droite.

## Données de référence
`racine 8 ; gauche 3 avec enfants 1 et 6 ; droite 10`

## Exercices
### Exercice 1
- Objectif travaillé : O1.
- Capacité officielle : T-ALGO-01E.
- Énoncé : À partir de la donnée de référence, suivre les comparaisons depuis la racine et écrire la justification.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 2
- Objectif travaillé : O2.
- Capacité officielle : T-ALGO-01F.
- Énoncé : Modifier une valeur de la donnée puis justifier le chemin vers 6 sans changer la méthode.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 3
- Objectif travaillé : O3.
- Capacité officielle : T-ALGO-01E.
- Énoncé : Construire un contre-exemple qui montre pourquoi il faut placer 7 à droite de 6.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 4
- Objectif travaillé : O4.
- Capacité officielle : T-ALGO-01F.
- Énoncé : Analyser l'erreur fréquente « parcourir tout l’arbre comme dans un arbre quelconque » et la corriger.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 5
- Objectif travaillé : O1.
- Capacité officielle : T-ALGO-01E.
- Énoncé : Comparer deux solutions d'élèves : l'une applique suivre les comparaisons depuis la racine, l'autre conclut directement.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 6
- Objectif travaillé : O2.
- Capacité officielle : T-ALGO-01F.
- Énoncé : Traiter le cas limite associé à « oublier l’invariant après insertion » avec une donnée minimale.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 7
- Objectif travaillé : O3.
- Capacité officielle : T-ALGO-01E.
- Énoncé : Rédiger une trace courte expliquant repérer le cas dégénéré d’insertions triées.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 8
- Objectif travaillé : O4.
- Capacité officielle : T-ALGO-01F.
- Énoncé : Créer une nouvelle donnée de test et vérifier que la méthode reste valable.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.

## Corrigé indicatif
### Corrigé exercice 1
- Méthode : isoler la donnée, appliquer l’objectif O1, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « suivre les comparaisons depuis la racine » et citer T-ALGO-01E.
- Contrôle : rejeter la solution si elle contient l’erreur « parcourir tout l’arbre comme dans un arbre quelconque ».
### Corrigé exercice 2
- Méthode : isoler la donnée, appliquer l’objectif O2, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « justifier le chemin vers 6 » et citer T-ALGO-01F.
- Contrôle : rejeter la solution si elle contient l’erreur « oublier l’invariant après insertion ».
### Corrigé exercice 3
- Méthode : isoler la donnée, appliquer l’objectif O3, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « placer 7 à droite de 6 » et citer T-ALGO-01E.
- Contrôle : rejeter la solution si elle contient l’erreur « placer une clé égale sans convention ».
### Corrigé exercice 4
- Méthode : isoler la donnée, appliquer l’objectif O4, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « repérer le cas dégénéré d’insertions triées » et citer T-ALGO-01F.
- Contrôle : rejeter la solution si elle contient l’erreur « annoncer une complexité logarithmique sans condition d’équilibre ».
### Corrigé exercice 5
- Méthode : isoler la donnée, appliquer l’objectif O1, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « suivre les comparaisons depuis la racine » et citer T-ALGO-01E.
- Contrôle : rejeter la solution si elle contient l’erreur « parcourir tout l’arbre comme dans un arbre quelconque ».
### Corrigé exercice 6
- Méthode : isoler la donnée, appliquer l’objectif O2, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « justifier le chemin vers 6 » et citer T-ALGO-01F.
- Contrôle : rejeter la solution si elle contient l’erreur « oublier l’invariant après insertion ».
### Corrigé exercice 7
- Méthode : isoler la donnée, appliquer l’objectif O3, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « placer 7 à droite de 6 » et citer T-ALGO-01E.
- Contrôle : rejeter la solution si elle contient l’erreur « placer une clé égale sans convention ».
### Corrigé exercice 8
- Méthode : isoler la donnée, appliquer l’objectif O4, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « repérer le cas dégénéré d’insertions triées » et citer T-ALGO-01F.
- Contrôle : rejeter la solution si elle contient l’erreur « annoncer une complexité logarithmique sans condition d’équilibre ».

## Erreurs fréquentes et remédiation
- EF1 : parcourir tout l’arbre comme dans un arbre quelconque. Remédiation : refaire l’exercice 1 avec la donnée modifiée par le professeur.
- EF2 : oublier l’invariant après insertion. Remédiation : refaire l’exercice 2 avec la donnée modifiée par le professeur.
- EF3 : placer une clé égale sans convention. Remédiation : refaire l’exercice 3 avec la donnée modifiée par le professeur.
- EF4 : annoncer une complexité logarithmique sans condition d’équilibre. Remédiation : refaire l’exercice 4 avec la donnée modifiée par le professeur.

## Différenciation
- Socle : exercices 1 à 4 avec étapes visibles.
- Standard : exercices 1 à 6 avec justification complète.
- Expert : exercices 7 et 8 avec nouvelle donnée et contrôle autonome.
