---
title: "P08 - TD - HTML, CSS et DOM"
level: "premiere"
sequence_id: "P08"
document_type: "td"
status: "needs_review"
version: "0.2.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Interactions sur le Web"
notion: "HTML, CSS, DOM et événement"
objectifs:
  - "identifier balise, attribut id et classe CSS"
  - "sélectionner un élément du DOM"
  - "associer un événement clic"
  - "contrôler que seul t2 change de classe"
private_data: false
official_program:
  capacities:
    - "P-IHM-01A"
    - "P-IHM-01B"
    - "P-IHM-02"
    - "P-IHM-03A"
---

# P08 - TD - HTML, CSS et DOM

## Objectifs
- O1 : identifier balise, attribut id et classe CSS.
- O2 : sélectionner un élément du DOM.
- O3 : associer un événement clic.
- O4 : contrôler que seul t2 change de classe.

## Capacités officielles
- P-IHM-01A
- P-IHM-01B
- P-IHM-02
- P-IHM-03A

## Situation de travail
Une page locale affiche une liste de tâches ; un bouton doit ajouter la classe CSS termine à l’élément choisi sans modifier le texte des autres éléments.

## Données de référence
`<ul><li id="t1">Réviser</li><li id="t2">Tester</li></ul>`

## Exercices
### Exercice 1
- Objectif travaillé : O1.
- Capacité officielle : P-IHM-01A.
- Énoncé : À partir de la donnée de référence, identifier balise, attribut id et classe CSS et écrire la justification.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 2
- Objectif travaillé : O2.
- Capacité officielle : P-IHM-01B.
- Énoncé : Modifier une valeur de la donnée puis sélectionner un élément du DOM sans changer la méthode.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 3
- Objectif travaillé : O3.
- Capacité officielle : P-IHM-02.
- Énoncé : Construire un contre-exemple qui montre pourquoi il faut associer un événement clic.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 4
- Objectif travaillé : O4.
- Capacité officielle : P-IHM-03A.
- Énoncé : Analyser l'erreur fréquente « confondre HTML et CSS » et la corriger.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 5
- Objectif travaillé : O1.
- Capacité officielle : P-IHM-01A.
- Énoncé : Comparer deux solutions d'élèves : l'une applique identifier balise, attribut id et classe CSS, l'autre conclut directement.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 6
- Objectif travaillé : O2.
- Capacité officielle : P-IHM-01B.
- Énoncé : Traiter le cas limite associé à « modifier tous les li avec un sélecteur trop large » avec une donnée minimale.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 7
- Objectif travaillé : O3.
- Capacité officielle : P-IHM-02.
- Énoncé : Rédiger une trace courte expliquant contrôler que seul t2 change de classe.
- Production attendue : réponse structurée avec donnée, méthode, résultat et contrôle.
- Critère de réussite : la conclusion est vérifiable par un pair.
### Exercice 8
- Objectif travaillé : O4.
- Capacité officielle : P-IHM-03A.
- Énoncé : À partir du fragment `<p id="alerte" class="info">OK</p>`, prévoir l’effet de `document.querySelector("#alerte").classList.replace("info", "danger")`.
- Production attendue : résultat `class="danger"` sur le seul paragraphe d’identifiant `alerte`, avec contrôle qu’aucun autre noeud n’est modifié.
- Critère de réussite : la conclusion est vérifiable par un pair.

## Corrigé indicatif
### Corrigé exercice 1
- Méthode : isoler la donnée, appliquer l’objectif O1, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « identifier balise, attribut id et classe CSS » et citer P-IHM-01A.
- Contrôle : rejeter la solution si elle contient l’erreur « confondre HTML et CSS ».
### Corrigé exercice 2
- Méthode : isoler la donnée, appliquer l’objectif O2, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « sélectionner un élément du DOM » et citer P-IHM-01B.
- Contrôle : rejeter la solution si elle contient l’erreur « modifier tous les li avec un sélecteur trop large ».
### Corrigé exercice 3
- Méthode : isoler la donnée, appliquer l’objectif O3, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « associer un événement clic » et citer P-IHM-02.
- Contrôle : rejeter la solution si elle contient l’erreur « écrire du style en dur sans classe ».
### Corrigé exercice 4
- Méthode : isoler la donnée, appliquer l’objectif O4, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « contrôler que seul t2 change de classe » et citer P-IHM-03A.
- Contrôle : rejeter la solution si elle contient l’erreur « oublier que le DOM est l’arbre manipulé par JavaScript ».
### Corrigé exercice 5
- Méthode : isoler la donnée, appliquer l’objectif O1, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « identifier balise, attribut id et classe CSS » et citer P-IHM-01A.
- Contrôle : rejeter la solution si elle contient l’erreur « confondre HTML et CSS ».
### Corrigé exercice 6
- Méthode : isoler la donnée, appliquer l’objectif O2, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « sélectionner un élément du DOM » et citer P-IHM-01B.
- Contrôle : rejeter la solution si elle contient l’erreur « modifier tous les li avec un sélecteur trop large ».
### Corrigé exercice 7
- Méthode : isoler la donnée, appliquer l’objectif O3, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « associer un événement clic » et citer P-IHM-02.
- Contrôle : rejeter la solution si elle contient l’erreur « écrire du style en dur sans classe ».
### Corrigé exercice 8
- Méthode : isoler la donnée, appliquer l’objectif O4, puis vérifier le résultat sur le cas limite demandé.
- Résultat : la réponse doit mentionner explicitement « contrôler que seul t2 change de classe » et citer P-IHM-03A.
- Contrôle : rejeter la solution si elle contient l’erreur « oublier que le DOM est l’arbre manipulé par JavaScript ».

## Erreurs fréquentes et remédiation
- EF1 : confondre HTML et CSS. Remédiation : refaire l’exercice 1 avec la donnée modifiée par le professeur.
- EF2 : modifier tous les li avec un sélecteur trop large. Remédiation : refaire l’exercice 2 avec la donnée modifiée par le professeur.
- EF3 : écrire du style en dur sans classe. Remédiation : refaire l’exercice 3 avec la donnée modifiée par le professeur.
- EF4 : oublier que le DOM est l’arbre manipulé par JavaScript. Remédiation : refaire l’exercice 4 avec la donnée modifiée par le professeur.

## Différenciation
- Socle : exercices 1 à 4 avec étapes visibles.
- Standard : exercices 1 à 6 avec justification complète.
- Expert : exercices 7 et 8 avec nouvelle donnée et contrôle autonome.
