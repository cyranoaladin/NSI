---
title: "P06 - TD - Tables : recherche, tri et fusion"
level: "premiere"
sequence_id: "P06"
document_type: "td"
status: "needs_review"
version: "0.2.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Traitement de tables"
notion: "recherche, tri, fusion de tables"
objectifs:
  - "rechercher la première ligne où id vaut 17"
  - "trier les lignes par nom puis par atelier"
  - "fusionner avec une table de présences par identifiant"
  - "signaler le doublon id=17 au lieu de l’écraser"
private_data: false
official_program:
  capacities:
    - "P-TABLE-03"
    - "P-TABLE-04"
---

# P06 - TD - Tables : recherche, tri et fusion

## Objectifs
- O1 : rechercher la première ligne où id vaut 17.
- O2 : trier les lignes par nom puis par atelier.
- O3 : fusionner avec une table de présences par identifiant.
- O4 : signaler le doublon id=17 au lieu de l’écraser.

## Capacités officielles
- P-TABLE-03
- P-TABLE-04

## Situation de travail
Une association dispose de deux fichiers : inscriptions aux ateliers et résultats de présence. Il faut retrouver une ligne, trier par nom puis fusionner deux tables avec la clé adherent.

## Données de référence
`inscriptions = [{"id": 17, "nom": "E1", "atelier": "robot"}, {"id": 4, "nom": "E2", "atelier": "web"}, {"id": 17, "nom": "E1", "atelier": "python"}]`

## Exercices
### Exercice 1
- Objectif travaillé : O1.
- Capacité officielle : P-TABLE-03.
- Énoncé : À partir de la donnée de référence, rechercher la première ligne où id vaut 17 et écrire la justification.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 2
- Objectif travaillé : O2.
- Capacité officielle : P-TABLE-04.
- Énoncé : Modifier une valeur de la donnée puis trier les lignes par nom puis par atelier sans changer la méthode.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 3
- Objectif travaillé : O3.
- Capacité officielle : P-TABLE-03.
- Énoncé : Construire un contre-exemple qui montre pourquoi il faut fusionner avec une table de présences par identifiant.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 4
- Objectif travaillé : O4.
- Capacité officielle : P-TABLE-04.
- Énoncé : Analyser l'erreur fréquente « utiliser la position de ligne comme clé stable » et la corriger.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 5
- Objectif travaillé : O1.
- Capacité officielle : P-TABLE-03.
- Énoncé : Comparer deux solutions d'élèves : l'une applique rechercher la première ligne où id vaut 17, l'autre conclut directement.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 6
- Objectif travaillé : O2.
- Capacité officielle : P-TABLE-04.
- Énoncé : Traiter le cas limite associé à « supprimer silencieusement un doublon » avec une donnée minimale.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 7
- Objectif travaillé : O3.
- Capacité officielle : P-TABLE-03.
- Énoncé : Rédiger une trace courte expliquant signaler le doublon id=17 au lieu de l’écraser.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 8
- Objectif travaillé : O4.
- Capacité officielle : P-TABLE-04.
- Énoncé : Construire un cas de test numérique ou textuel inédit et vérifier que la méthode reste valable.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.

## Corrigé indicatif
### Corrigé exercice 1
- Méthode : isoler la donnée, appliquer l’objectif O1, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « rechercher la première ligne où id vaut 17 » et citer P-TABLE-03.
- Contrôle : rejeter la solution si elle contient l’erreur « utiliser la position de ligne comme clé stable ».
### Corrigé exercice 2
- Méthode : isoler la donnée, appliquer l’objectif O2, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « trier les lignes par nom puis par atelier » et citer P-TABLE-04.
- Contrôle : rejeter la solution si elle contient l’erreur « supprimer silencieusement un doublon ».
### Corrigé exercice 3
- Méthode : isoler la donnée, appliquer l’objectif O3, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « fusionner avec une table de présences par identifiant » et citer P-TABLE-03.
- Contrôle : rejeter la solution si elle contient l’erreur « trier des nombres stockés comme chaînes ».
### Corrigé exercice 4
- Méthode : isoler la donnée, appliquer l’objectif O4, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « signaler le doublon id=17 au lieu de l’écraser » et citer P-TABLE-04.
- Contrôle : rejeter la solution si elle contient l’erreur « fusionner deux tables sans vérifier les clés absentes ».
### Corrigé exercice 5
- Méthode : isoler la donnée, appliquer l’objectif O1, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « rechercher la première ligne où id vaut 17 » et citer P-TABLE-03.
- Contrôle : rejeter la solution si elle contient l’erreur « utiliser la position de ligne comme clé stable ».
### Corrigé exercice 6
- Méthode : isoler la donnée, appliquer l’objectif O2, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « trier les lignes par nom puis par atelier » et citer P-TABLE-04.
- Contrôle : rejeter la solution si elle contient l’erreur « supprimer silencieusement un doublon ».
### Corrigé exercice 7
- Méthode : isoler la donnée, appliquer l’objectif O3, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « fusionner avec une table de présences par identifiant » et citer P-TABLE-03.
- Contrôle : rejeter la solution si elle contient l’erreur « trier des nombres stockés comme chaînes ».
### Corrigé exercice 8
- Méthode : isoler la donnée, appliquer l’objectif O4, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « signaler le doublon id=17 au lieu de l’écraser » et citer P-TABLE-04.
- Contrôle : rejeter la solution si elle contient l’erreur « fusionner deux tables sans vérifier les clés absentes ».

## Erreurs fréquentes et remédiation
- EF1 : utiliser la position de ligne comme clé stable. Remédiation : refaire l’exercice 1 avec la donnée modifiée par le professeur.
- EF2 : supprimer silencieusement un doublon. Remédiation : refaire l’exercice 2 avec la donnée modifiée par le professeur.
- EF3 : trier des nombres stockés comme chaînes. Remédiation : refaire l’exercice 3 avec la donnée modifiée par le professeur.
- EF4 : fusionner deux tables sans vérifier les clés absentes. Remédiation : refaire l’exercice 4 avec la donnée modifiée par le professeur.

## Différenciation
- Socle : exercices 1 à 4 avec étapes visibles.
- Standard : exercices 1 à 6 avec justification complète.
- Expert : exercices 7 et 8 avec nouvelle donnée et contrôle autonome.
