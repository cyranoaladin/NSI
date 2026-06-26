---
title: "T08 - TD - Parcours BFS, DFS, cycles et chemins"
level: "terminale"
sequence_id: "T08"
document_type: "td"
status: "needs_review"
version: "0.2.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Algorithmes sur graphes"
notion: "parcours en largeur, profondeur, chemins, cycles"
objectifs:
  - "exécuter BFS avec file"
  - "exécuter DFS avec pile ou récursion"
  - "reconstruire un chemin par prédécesseurs"
  - "détecter un cycle en évitant le parent"
private_data: false
official_program:
  capacities:
    - "T-ALGO-02A"
    - "T-ALGO-02B"
    - "T-ALGO-02C"
    - "T-ALGO-02D"
---

# T08 - TD - Parcours BFS, DFS, cycles et chemins

## Objectifs
- O1 : exécuter BFS avec file.
- O2 : exécuter DFS avec pile ou récursion.
- O3 : reconstruire un chemin par prédécesseurs.
- O4 : détecter un cycle en évitant le parent.

## Capacités officielles
- T-ALGO-02A
- T-ALGO-02B
- T-ALGO-02C
- T-ALGO-02D

## Situation de travail
Dans un graphe de salles, on cherche le plus petit nombre de couloirs depuis A vers D et on compare BFS avec DFS.

## Données de référence
`A: B,C ; B: A,D ; C: A,D ; D: B,C,E ; E: D`

## Exercices
### Exercice 1
- Objectif travaillé : O1.
- Capacité officielle : T-ALGO-02A.
- Énoncé : À partir de la donnée de référence, exécuter BFS avec file et écrire la justification.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 2
- Objectif travaillé : O2.
- Capacité officielle : T-ALGO-02B.
- Énoncé : Modifier une valeur de la donnée puis exécuter DFS avec pile ou récursion sans changer la méthode.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 3
- Objectif travaillé : O3.
- Capacité officielle : T-ALGO-02C.
- Énoncé : Construire un contre-exemple qui montre pourquoi il faut reconstruire un chemin par prédécesseurs.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 4
- Objectif travaillé : O4.
- Capacité officielle : T-ALGO-02D.
- Énoncé : Analyser l'erreur fréquente « marquer un sommet trop tard » et la corriger.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 5
- Objectif travaillé : O1.
- Capacité officielle : T-ALGO-02A.
- Énoncé : Comparer deux solutions d'élèves : l'une applique exécuter BFS avec file, l'autre conclut directement.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 6
- Objectif travaillé : O2.
- Capacité officielle : T-ALGO-02B.
- Énoncé : Traiter le cas limite associé à « croire que DFS donne toujours un plus court chemin » avec une donnée minimale.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 7
- Objectif travaillé : O3.
- Capacité officielle : T-ALGO-02C.
- Énoncé : Rédiger une trace courte expliquant détecter un cycle en évitant le parent.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 8
- Objectif travaillé : O4.
- Capacité officielle : T-ALGO-02D.
- Énoncé : Créer une nouvelle donnée de test et vérifier que la méthode reste valable.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.

## Corrigé indicatif
### Corrigé exercice 1
- Méthode : isoler la donnée, appliquer l’objectif O1, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « exécuter BFS avec file » et citer T-ALGO-02A.
- Contrôle : rejeter la solution si elle contient l’erreur « marquer un sommet trop tard ».
### Corrigé exercice 2
- Méthode : isoler la donnée, appliquer l’objectif O2, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « exécuter DFS avec pile ou récursion » et citer T-ALGO-02B.
- Contrôle : rejeter la solution si elle contient l’erreur « croire que DFS donne toujours un plus court chemin ».
### Corrigé exercice 3
- Méthode : isoler la donnée, appliquer l’objectif O3, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « reconstruire un chemin par prédécesseurs » et citer T-ALGO-02C.
- Contrôle : rejeter la solution si elle contient l’erreur « oublier les prédécesseurs ».
### Corrigé exercice 4
- Méthode : isoler la donnée, appliquer l’objectif O4, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « détecter un cycle en évitant le parent » et citer T-ALGO-02D.
- Contrôle : rejeter la solution si elle contient l’erreur « confondre cycle et simple retour vers le parent ».
### Corrigé exercice 5
- Méthode : isoler la donnée, appliquer l’objectif O1, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « exécuter BFS avec file » et citer T-ALGO-02A.
- Contrôle : rejeter la solution si elle contient l’erreur « marquer un sommet trop tard ».
### Corrigé exercice 6
- Méthode : isoler la donnée, appliquer l’objectif O2, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « exécuter DFS avec pile ou récursion » et citer T-ALGO-02B.
- Contrôle : rejeter la solution si elle contient l’erreur « croire que DFS donne toujours un plus court chemin ».
### Corrigé exercice 7
- Méthode : isoler la donnée, appliquer l’objectif O3, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « reconstruire un chemin par prédécesseurs » et citer T-ALGO-02C.
- Contrôle : rejeter la solution si elle contient l’erreur « oublier les prédécesseurs ».
### Corrigé exercice 8
- Méthode : isoler la donnée, appliquer l’objectif O4, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « détecter un cycle en évitant le parent » et citer T-ALGO-02D.
- Contrôle : rejeter la solution si elle contient l’erreur « confondre cycle et simple retour vers le parent ».

## Erreurs fréquentes et remédiation
- EF1 : marquer un sommet trop tard. Remédiation : refaire l’exercice 1 avec la donnée modifiée par le professeur.
- EF2 : croire que DFS donne toujours un plus court chemin. Remédiation : refaire l’exercice 2 avec la donnée modifiée par le professeur.
- EF3 : oublier les prédécesseurs. Remédiation : refaire l’exercice 3 avec la donnée modifiée par le professeur.
- EF4 : confondre cycle et simple retour vers le parent. Remédiation : refaire l’exercice 4 avec la donnée modifiée par le professeur.

## Différenciation
- Socle : exercices 1 à 4 avec étapes visibles.
- Standard : exercices 1 à 6 avec justification complète.
- Expert : exercices 7 et 8 avec nouvelle donnée et contrôle autonome.
