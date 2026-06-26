---
title: "P09 - TD - Architecture, système et droits"
level: "premiere"
sequence_id: "P09"
document_type: "td"
status: "needs_review"
version: "0.2.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Architecture matérielle et systèmes"
notion: "chemins, processus, permissions"
objectifs:
  - "distinguer chemin absolu et relatif"
  - "interpréter r, w, x pour propriétaire/groupe/autres"
  - "proposer chmod u+x scripts/run.sh"
  - "expliquer l’erreur Permission denied"
private_data: false
official_program:
  capacities:
    - "P-ARCH-01A"
    - "P-ARCH-01B"
    - "P-ARCH-03A"
    - "P-ARCH-03B"
    - "P-ARCH-03C"
---

# P09 - TD - Architecture, système et droits

## Objectifs
- O1 : distinguer chemin absolu et relatif.
- O2 : interpréter r, w, x pour propriétaire/groupe/autres.
- O3 : proposer chmod u+x scripts/run.sh.
- O4 : expliquer l’erreur Permission denied.

## Capacités officielles
- P-ARCH-01A
- P-ARCH-01B
- P-ARCH-03A
- P-ARCH-03B
- P-ARCH-03C

## Situation de travail
Un projet Python contient app.py, data/notes.csv et scripts/run.sh. Il faut choisir les bons chemins et expliquer pourquoi run.sh n’est pas exécutable.

## Données de référence
`ls -l : -rw-r--r-- app.py, -rw-r----- data/notes.csv, -rw-r--r-- scripts/run.sh`

## Exercices
### Exercice 1
- Objectif travaillé : O1.
- Capacité officielle : P-ARCH-01A.
- Énoncé : À partir de la donnée de référence, distinguer chemin absolu et relatif et écrire la justification.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 2
- Objectif travaillé : O2.
- Capacité officielle : P-ARCH-01B.
- Énoncé : Modifier une valeur de la donnée puis interpréter r, w, x pour propriétaire/groupe/autres sans changer la méthode.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 3
- Objectif travaillé : O3.
- Capacité officielle : P-ARCH-03A.
- Énoncé : Construire un contre-exemple qui montre pourquoi il faut proposer chmod u+x scripts/run.sh.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 4
- Objectif travaillé : O4.
- Capacité officielle : P-ARCH-03B.
- Énoncé : Analyser l'erreur fréquente « confondre lecture et exécution » et la corriger.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 5
- Objectif travaillé : O1.
- Capacité officielle : P-ARCH-03C.
- Énoncé : Comparer deux solutions d'élèves : l'une applique distinguer chemin absolu et relatif, l'autre conclut directement.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 6
- Objectif travaillé : O2.
- Capacité officielle : P-ARCH-01A.
- Énoncé : Traiter le cas limite associé à « utiliser un chemin valable seulement dans son dossier courant » avec une donnée minimale.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 7
- Objectif travaillé : O3.
- Capacité officielle : P-ARCH-01B.
- Énoncé : Rédiger une trace courte expliquant expliquer l’erreur Permission denied.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 8
- Objectif travaillé : O4.
- Capacité officielle : P-ARCH-03A.
- Énoncé : Créer une nouvelle donnée de test et vérifier que la méthode reste valable.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.

## Corrigé indicatif
### Corrigé exercice 1
- Méthode : isoler la donnée, appliquer l’objectif O1, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « distinguer chemin absolu et relatif » et citer P-ARCH-01A.
- Contrôle : rejeter la solution si elle contient l’erreur « confondre lecture et exécution ».
### Corrigé exercice 2
- Méthode : isoler la donnée, appliquer l’objectif O2, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « interpréter r, w, x pour propriétaire/groupe/autres » et citer P-ARCH-01B.
- Contrôle : rejeter la solution si elle contient l’erreur « utiliser un chemin valable seulement dans son dossier courant ».
### Corrigé exercice 3
- Méthode : isoler la donnée, appliquer l’objectif O3, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « proposer chmod u+x scripts/run.sh » et citer P-ARCH-03A.
- Contrôle : rejeter la solution si elle contient l’erreur « donner tous les droits avec chmod 777 ».
### Corrigé exercice 4
- Méthode : isoler la donnée, appliquer l’objectif O4, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « expliquer l’erreur Permission denied » et citer P-ARCH-03B.
- Contrôle : rejeter la solution si elle contient l’erreur « oublier le rôle du système d’exploitation ».
### Corrigé exercice 5
- Méthode : isoler la donnée, appliquer l’objectif O1, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « distinguer chemin absolu et relatif » et citer P-ARCH-03C.
- Contrôle : rejeter la solution si elle contient l’erreur « confondre lecture et exécution ».
### Corrigé exercice 6
- Méthode : isoler la donnée, appliquer l’objectif O2, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « interpréter r, w, x pour propriétaire/groupe/autres » et citer P-ARCH-01A.
- Contrôle : rejeter la solution si elle contient l’erreur « utiliser un chemin valable seulement dans son dossier courant ».
### Corrigé exercice 7
- Méthode : isoler la donnée, appliquer l’objectif O3, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « proposer chmod u+x scripts/run.sh » et citer P-ARCH-01B.
- Contrôle : rejeter la solution si elle contient l’erreur « donner tous les droits avec chmod 777 ».
### Corrigé exercice 8
- Méthode : isoler la donnée, appliquer l’objectif O4, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « expliquer l’erreur Permission denied » et citer P-ARCH-03A.
- Contrôle : rejeter la solution si elle contient l’erreur « oublier le rôle du système d’exploitation ».

## Erreurs fréquentes et remédiation
- EF1 : confondre lecture et exécution. Remédiation : refaire l’exercice 1 avec la donnée modifiée par le professeur.
- EF2 : utiliser un chemin valable seulement dans son dossier courant. Remédiation : refaire l’exercice 2 avec la donnée modifiée par le professeur.
- EF3 : donner tous les droits avec chmod 777. Remédiation : refaire l’exercice 3 avec la donnée modifiée par le professeur.
- EF4 : oublier le rôle du système d’exploitation. Remédiation : refaire l’exercice 4 avec la donnée modifiée par le professeur.

## Différenciation
- Socle : exercices 1 à 4 avec étapes visibles.
- Standard : exercices 1 à 6 avec justification complète.
- Expert : exercices 7 et 8 avec nouvelle donnée et contrôle autonome.
