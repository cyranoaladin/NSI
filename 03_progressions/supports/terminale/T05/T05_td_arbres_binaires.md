---
title: "T05 - Td - Arbres binaires"
level: "terminale"
sequence_id: "T05"
document_type: "td"
status: "needs_review"
version: "0.4.1"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Arbres et algorithmes"
notion: "arbre binaire, racine, feuille, parcours"
objectifs:
  - "Objectif O1 - Identifier précisément la représentation ou la structure en jeu"
  - "Objectif O2 - Appliquer une méthode disciplinaire complète"
  - "Objectif O3 - Justifier le résultat sur un cas différent"
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur observée"
private_data: false
official_program:
  capacities:
    - "T-STRUCT-04A"
---

# T05 - TD - Arbres binaires

## Objectifs spécifiques
- Objectif O1 - Identifier précisément la représentation ou la structure en jeu.
- Objectif O2 - Appliquer une méthode disciplinaire complète.
- Objectif O3 - Justifier le résultat sur un cas différent.
- Objectif O4 - Contrôler un cas limite et corriger une erreur observée.

## Capacités officielles atomiques
- T-STRUCT-04A

## Prérequis
- Reconnaître une consigne liée à arbre binaire.
- Distinguer donnée, méthode et conclusion dans le thème Arbres et algorithmes.
- Rédiger une justification courte en utilisant le vocabulaire du programme.
- Contrôler une réponse par un cas limite ou un contre-exemple explicite.

## Séance(s) correspondante(s)
- T05-S1 à T05-S7 : support rattaché aux séances prêtes de la progression.

## Situation-problème concrète
Une expression arithmétique est représentée par un arbre dont les feuilles sont des valeurs et les nœuds internes des opérateurs.

## Activité d’entrée
1. Repérer racine, fils gauche et fils droit.
2. Calculer la hauteur d’un arbre réduit à une feuille.
3. Lister un parcours préfixe.
4. Évaluer une expression simple.

## Exemples corrigés précis
### Exemple corrigé 1 - arbre feuille
- Donnée étudiée : `7`.
- Méthode : reconnaître l’absence de fils.
- Résultat obtenu : hauteur 0.
- Contrôle : le cas limite « arbre vide » est vérifié séparément.
### Exemple corrigé 2 - hauteur
- Donnée étudiée : racine avec deux feuilles.
- Méthode : prendre 1 plus le maximum des hauteurs des sous-arbres.
- Résultat obtenu : hauteur 1.
- Contrôle : le cas limite « un seul fils » est vérifié séparément.
### Exemple corrigé 3 - parcours préfixe
- Donnée étudiée : `+ 2 3`.
- Méthode : visiter racine puis gauche puis droite.
- Résultat obtenu : `+, 2, 3`.
- Contrôle : le cas limite « nœud feuille » est vérifié séparément.
### Exemple corrigé 4 - évaluation
- Donnée étudiée : `(2 + 3) * 4`.
- Méthode : évaluer les sous-arbres avant l’opérateur parent.
- Résultat obtenu : `20`.
- Contrôle : le cas limite « division par zéro si opérateur `/` » est vérifié séparément.
## Exercices numérotés
### Exercice 1
- Objectif travaillé : O1.
- Capacité officielle : T-STRUCT-04A.
- Énoncé disciplinaire : résoudre arbre feuille avec `7`.
- Production attendue : hauteur 0.
- Contrainte de contrôle : faire apparaître le contrôle « arbre vide ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 2
- Objectif travaillé : O2.
- Capacité officielle : T-STRUCT-04A.
- Énoncé disciplinaire : expliquer hauteur à partir de racine avec deux feuilles.
- Production attendue : hauteur 1.
- Contrainte de contrôle : rédiger la méthode avant le résultat.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 3
- Objectif travaillé : O3.
- Capacité officielle : T-STRUCT-04A.
- Énoncé disciplinaire : comparer parcours préfixe avec `+ 2 3`.
- Production attendue : `+, 2, 3`.
- Contrainte de contrôle : comparer avec le cas « nœud feuille ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 4
- Objectif travaillé : O4.
- Capacité officielle : T-STRUCT-04A.
- Énoncé disciplinaire : corriger évaluation pour `(2 + 3) * 4`.
- Production attendue : `20`.
- Contrainte de contrôle : corriger l’erreur « Évaluer un opérateur avant ses opérandes. ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 5
- Objectif travaillé : O1.
- Capacité officielle : T-STRUCT-04A.
- Énoncé disciplinaire : tester un cas limite lié à arbre vide.
- Production attendue : le comportement de arbre feuille est contrôlé.
- Contrainte de contrôle : nommer la donnée minimale et la conclusion.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 6
- Objectif travaillé : O2.
- Capacité officielle : T-STRUCT-04A.
- Énoncé disciplinaire : classer deux méthodes possibles pour hauteur.
- Production attendue : la méthode robuste est choisie et justifiée.
- Contrainte de contrôle : identifier pourquoi « Oublier le cas arbre vide. » est une erreur.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 7
- Objectif travaillé : O3.
- Capacité officielle : T-STRUCT-04A.
- Énoncé disciplinaire : justifier un transfert qui utilise parcours préfixe avec une donnée nouvelle.
- Production attendue : la justification reste valable sur le nouveau cas.
- Contrainte de contrôle : inclure une étape calculable par un pair.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 8
- Objectif travaillé : O4.
- Capacité officielle : T-STRUCT-04A.
- Énoncé disciplinaire : étendre un énoncé volontairement erroné sur évaluation.
- Production attendue : l’erreur est localisée puis réparée.
- Contrainte de contrôle : proposer une activité corrective inspirée de « Remonter les valeurs depuis les feuilles vers la racine. ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
## Corrigé
### Corrigé exercice 1
- Méthode : identifier `7`, appliquer la méthode « reconnaître l’absence de fils », puis écrire hauteur 0.
- Résultat : hauteur 0.
- Contrôle : faire apparaître le contrôle « arbre vide ».
- Erreur traitée : EF1 - Confondre hauteur et nombre de nœuds.
### Corrigé exercice 2
- Méthode : expliciter chaque étape de prendre 1 plus le maximum des hauteurs des sous-arbres avant de conclure par hauteur 1.
- Résultat : hauteur 1.
- Contrôle : rédiger la méthode avant le résultat.
- Erreur traitée : EF2 - Oublier le cas arbre vide.
### Corrigé exercice 3
- Méthode : comparer la donnée avec le cas limite « nœud feuille » et valider `+, 2, 3`.
- Résultat : `+, 2, 3`.
- Contrôle : comparer avec le cas « nœud feuille ».
- Erreur traitée : EF3 - Mélanger parcours préfixe et infixe.
### Corrigé exercice 4
- Méthode : isoler l’erreur fréquente « Évaluer un opérateur avant ses opérandes. » puis reprendre la procédure correcte.
- Résultat : `20`.
- Contrôle : corriger l’erreur « Évaluer un opérateur avant ses opérandes. ».
- Erreur traitée : EF4 - Évaluer un opérateur avant ses opérandes.
### Corrigé exercice 5
- Méthode : identifier `7`, appliquer la méthode « reconnaître l’absence de fils », puis écrire hauteur 0.
- Résultat : le comportement de arbre feuille est contrôlé.
- Contrôle : nommer la donnée minimale et la conclusion.
- Erreur traitée : EF1 - Confondre hauteur et nombre de nœuds.
### Corrigé exercice 6
- Méthode : expliciter chaque étape de prendre 1 plus le maximum des hauteurs des sous-arbres avant de conclure par hauteur 1.
- Résultat : la méthode robuste est choisie et justifiée.
- Contrôle : identifier pourquoi « Oublier le cas arbre vide. » est une erreur.
- Erreur traitée : EF2 - Oublier le cas arbre vide.
### Corrigé exercice 7
- Méthode : comparer la donnée avec le cas limite « nœud feuille » et valider `+, 2, 3`.
- Résultat : la justification reste valable sur le nouveau cas.
- Contrôle : inclure une étape calculable par un pair.
- Erreur traitée : EF3 - Mélanger parcours préfixe et infixe.
### Corrigé exercice 8
- Méthode : isoler l’erreur fréquente « Évaluer un opérateur avant ses opérandes. » puis reprendre la procédure correcte.
- Résultat : l’erreur est localisée puis réparée.
- Contrôle : proposer une activité corrective inspirée de « Remonter les valeurs depuis les feuilles vers la racine. ».
- Erreur traitée : EF4 - Évaluer un opérateur avant ses opérandes.
## Erreurs fréquentes
- Erreur fréquente EF1 - Confondre hauteur et nombre de nœuds.
- Erreur fréquente EF2 - Oublier le cas arbre vide.
- Erreur fréquente EF3 - Mélanger parcours préfixe et infixe.
- Erreur fréquente EF4 - Évaluer un opérateur avant ses opérandes.

## Remédiation ciblée
- Activité corrective EF1 : Calculer séparément hauteur gauche et droite.
- Activité corrective EF2 : Décider une convention pour l’arbre vide puis l’appliquer partout.
- Activité corrective EF3 : Écrire l’ordre de visite au-dessus de chaque nœud.
- Activité corrective EF4 : Remonter les valeurs depuis les feuilles vers la racine.

## Différenciation
- Socle : traiter `7` avec une fiche méthode fournie.
- Standard : traiter racine avec deux feuilles en rédigeant la justification complète.
- Expert : inventer un cas limite lié à « nœud feuille » et expliquer le comportement attendu.

## Critères de réussite
- La capacité officielle est citée dans la copie.
- La méthode contient au moins une étape vérifiable par un pair.
- Le cas limite est discuté avec une donnée concrète.
- La correction explique quelle erreur fréquente est évitée.
