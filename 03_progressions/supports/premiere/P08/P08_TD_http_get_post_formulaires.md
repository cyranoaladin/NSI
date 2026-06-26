---
title: "P08 - TD - HTTP, GET, POST et formulaires"
level: "premiere"
sequence_id: "P08"
document_type: "td"
status: "needs_review"
version: "0.2.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Interactions sur le Web"
notion: "requêtes HTTP et formulaires"
objectifs:
  - "repérer méthode, URL, paramètres et corps"
  - "justifier GET pour une recherche partageable"
  - "justifier POST pour une donnée sensible"
  - "identifier le risque de mot de passe dans l’URL"
private_data: false
official_program:
  capacities:
    - "P-IHM-03A"
    - "P-IHM-03B"
    - "P-IHM-03C"
    - "P-IHM-04A"
    - "P-IHM-04B"
    - "P-IHM-04C"
---

# P08 - TD - HTTP, GET, POST et formulaires

## Objectifs
- O1 : repérer méthode, URL, paramètres et corps.
- O2 : justifier GET pour une recherche partageable.
- O3 : justifier POST pour une donnée sensible.
- O4 : identifier le risque de mot de passe dans l’URL.

## Capacités officielles
- P-IHM-03A
- P-IHM-03B
- P-IHM-03C
- P-IHM-04A
- P-IHM-04B
- P-IHM-04C

## Situation de travail
Un formulaire de recherche envoie un mot-clé public en GET, tandis qu’un formulaire de connexion doit envoyer les identifiants en POST.

## Données de référence
`GET /search?q=nsi puis POST /login avec champs utilisateur et mot_de_passe`

## Exercices
### Exercice 1
- Objectif travaillé : O1.
- Capacité officielle : P-IHM-03A.
- Énoncé : À partir de la donnée de référence, repérer méthode, URL, paramètres et corps et écrire la justification.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 2
- Objectif travaillé : O2.
- Capacité officielle : P-IHM-03B.
- Énoncé : Modifier une valeur de la donnée puis justifier GET pour une recherche partageable sans changer la méthode.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 3
- Objectif travaillé : O3.
- Capacité officielle : P-IHM-03C.
- Énoncé : Construire un contre-exemple qui montre pourquoi il faut justifier POST pour une donnée sensible.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 4
- Objectif travaillé : O4.
- Capacité officielle : P-IHM-04A.
- Énoncé : Analyser l'erreur fréquente « mettre un mot de passe dans une URL GET » et la corriger.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 5
- Objectif travaillé : O1.
- Capacité officielle : P-IHM-04B.
- Énoncé : Comparer deux solutions d'élèves : l'une applique repérer méthode, URL, paramètres et corps, l'autre conclut directement.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 6
- Objectif travaillé : O2.
- Capacité officielle : P-IHM-04C.
- Énoncé : Traiter le cas limite associé à « confondre code de statut et méthode HTTP » avec une donnée minimale.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 7
- Objectif travaillé : O3.
- Capacité officielle : P-IHM-03A.
- Énoncé : Rédiger une trace courte expliquant identifier le risque de mot de passe dans l’URL.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 8
- Objectif travaillé : O4.
- Capacité officielle : P-IHM-03B.
- Énoncé : Comparer `GET /login?user=ada&password=secret` et un formulaire `POST /login` dont le corps contient `user=ada&password=secret`.
- Production attendue : méthode `POST` retenue pour le mot de passe, car la chaîne sensible n’apparaît pas dans l’URL ; contrôle par lecture de l’adresse affichée.
- Critère de réussite : la conclusion est vérifiable par un pair.

## Corrigé indicatif
### Corrigé exercice 1
- Méthode : isoler la donnée, appliquer l’objectif O1, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « repérer méthode, URL, paramètres et corps » et citer P-IHM-03A.
- Contrôle : rejeter la solution si elle contient l’erreur « mettre un mot de passe dans une URL GET ».
### Corrigé exercice 2
- Méthode : isoler la donnée, appliquer l’objectif O2, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « justifier GET pour une recherche partageable » et citer P-IHM-03B.
- Contrôle : rejeter la solution si elle contient l’erreur « confondre code de statut et méthode HTTP ».
### Corrigé exercice 3
- Méthode : isoler la donnée, appliquer l’objectif O3, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « justifier POST pour une donnée sensible » et citer P-IHM-03C.
- Contrôle : rejeter la solution si elle contient l’erreur « croire que POST chiffre automatiquement ».
### Corrigé exercice 4
- Méthode : isoler la donnée, appliquer l’objectif O4, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « identifier le risque de mot de passe dans l’URL » et citer P-IHM-04A.
- Contrôle : rejeter la solution si elle contient l’erreur « oublier le nom des champs du formulaire ».
### Corrigé exercice 5
- Méthode : isoler la donnée, appliquer l’objectif O1, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « repérer méthode, URL, paramètres et corps » et citer P-IHM-04B.
- Contrôle : rejeter la solution si elle contient l’erreur « mettre un mot de passe dans une URL GET ».
### Corrigé exercice 6
- Méthode : isoler la donnée, appliquer l’objectif O2, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « justifier GET pour une recherche partageable » et citer P-IHM-04C.
- Contrôle : rejeter la solution si elle contient l’erreur « confondre code de statut et méthode HTTP ».
### Corrigé exercice 7
- Méthode : isoler la donnée, appliquer l’objectif O3, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « justifier POST pour une donnée sensible » et citer P-IHM-03A.
- Contrôle : rejeter la solution si elle contient l’erreur « croire que POST chiffre automatiquement ».
### Corrigé exercice 8
- Méthode : isoler la donnée, appliquer l’objectif O4, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « identifier le risque de mot de passe dans l’URL » et citer P-IHM-03B.
- Contrôle : rejeter la solution si elle contient l’erreur « oublier le nom des champs du formulaire ».

## Erreurs fréquentes et remédiation
- EF1 : mettre un mot de passe dans une URL GET. Remédiation : refaire l’exercice 1 avec la donnée modifiée par le professeur.
- EF2 : confondre code de statut et méthode HTTP. Remédiation : refaire l’exercice 2 avec la donnée modifiée par le professeur.
- EF3 : croire que POST chiffre automatiquement. Remédiation : refaire l’exercice 3 avec la donnée modifiée par le professeur.
- EF4 : oublier le nom des champs du formulaire. Remédiation : refaire l’exercice 4 avec la donnée modifiée par le professeur.

## Différenciation
- Socle : exercices 1 à 4 avec étapes visibles.
- Standard : exercices 1 à 6 avec justification complète.
- Expert : exercices 7 et 8 avec nouvelle donnée et contrôle autonome.
