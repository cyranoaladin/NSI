---
title: "T02 - Td - Classes et objets"
level: "terminale"
sequence_id: "T02"
document_type: "td"
status: "needs_review"
version: "0.4.1"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Programmation orientée objet"
notion: "classe, attribut, méthode, invariant"
objectifs:
  - "Objectif O1 - Identifier précisément la représentation ou la structure en jeu"
  - "Objectif O2 - Appliquer une méthode disciplinaire complète"
  - "Objectif O3 - Justifier le résultat sur un cas différent"
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur observée"
private_data: false
official_program:
  capacities:
    - "T-STRUCT-02A"
---

# T02 - TD - Classes et objets

## Objectifs spécifiques
- Objectif O1 - Identifier précisément la représentation ou la structure en jeu.
- Objectif O2 - Appliquer une méthode disciplinaire complète.
- Objectif O3 - Justifier le résultat sur un cas différent.
- Objectif O4 - Contrôler un cas limite et corriger une erreur observée.

## Capacités officielles atomiques
- T-STRUCT-02A

## Prérequis
- Reconnaître une consigne liée à classe.
- Distinguer donnée, méthode et conclusion dans le thème Programmation orientée objet.
- Rédiger une justification courte en utilisant le vocabulaire du programme.
- Contrôler une réponse par un cas limite ou un contre-exemple explicite.

## Séance(s) correspondante(s)
- T02-S1 à T02-S5 : support rattaché aux séances prêtes de la progression.

## Situation-problème concrète
Une application de gestion de comptes doit garantir qu’aucune opération ne crée un solde incohérent.

## Activité d’entrée
1. Identifier attributs et méthodes d’un compte.
2. Écrire l’invariant `solde >= 0`.
3. Prévoir un dépôt puis un retrait.
4. Décider quoi faire si le retrait dépasse le solde.

## Exemples corrigés précis
### Exemple corrigé 1 - constructeur
- Donnée étudiée : `Compte("Ada", 20)`.
- Méthode : initialiser les attributs après validation.
- Résultat obtenu : propriétaire Ada, solde 20.
- Contrôle : le cas limite « solde initial négatif » est vérifié séparément.
### Exemple corrigé 2 - méthode dépôt
- Donnée étudiée : dépôt de 15.
- Méthode : vérifier le montant puis modifier le solde.
- Résultat obtenu : solde augmenté de 15.
- Contrôle : le cas limite « montant nul ou négatif » est vérifié séparément.
### Exemple corrigé 3 - méthode retrait
- Donnée étudiée : retrait de 7 sur solde 20.
- Méthode : contrôler disponibilité puis soustraire.
- Résultat obtenu : solde 13.
- Contrôle : le cas limite « retrait supérieur au solde » est vérifié séparément.
### Exemple corrigé 4 - représentation
- Donnée étudiée : `repr(compte)`.
- Méthode : exposer une chaîne utile sans révéler de données inutiles.
- Résultat obtenu : résumé lisible.
- Contrôle : le cas limite « nom vide » est vérifié séparément.
## Exercices numérotés
### Exercice 1
- Objectif travaillé : O1.
- Capacité officielle : T-STRUCT-02A.
- Énoncé disciplinaire : résoudre constructeur avec `Compte("Ada", 20)`.
- Production attendue : propriétaire Ada, solde 20.
- Contrainte de contrôle : faire apparaître le contrôle « solde initial négatif ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 2
- Objectif travaillé : O2.
- Capacité officielle : T-STRUCT-02A.
- Énoncé disciplinaire : expliquer méthode dépôt à partir de dépôt de 15.
- Production attendue : solde augmenté de 15.
- Contrainte de contrôle : rédiger la méthode avant le résultat.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 3
- Objectif travaillé : O3.
- Capacité officielle : T-STRUCT-02A.
- Énoncé disciplinaire : comparer méthode retrait avec retrait de 7 sur solde 20.
- Production attendue : solde 13.
- Contrainte de contrôle : comparer avec le cas « retrait supérieur au solde ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 4
- Objectif travaillé : O4.
- Capacité officielle : T-STRUCT-02A.
- Énoncé disciplinaire : corriger représentation pour `repr(compte)`.
- Production attendue : résumé lisible.
- Contrainte de contrôle : corriger l’erreur « Confondre classe et instance. ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 5
- Objectif travaillé : O1.
- Capacité officielle : T-STRUCT-02A.
- Énoncé disciplinaire : tester un cas limite lié à solde initial négatif.
- Production attendue : le comportement de constructeur est contrôlé.
- Contrainte de contrôle : nommer la donnée minimale et la conclusion.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 6
- Objectif travaillé : O2.
- Capacité officielle : T-STRUCT-02A.
- Énoncé disciplinaire : classer deux méthodes possibles pour méthode dépôt.
- Production attendue : la méthode robuste est choisie et justifiée.
- Contrainte de contrôle : identifier pourquoi « Oublier de maintenir l’invariant. » est une erreur.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 7
- Objectif travaillé : O3.
- Capacité officielle : T-STRUCT-02A.
- Énoncé disciplinaire : justifier un transfert qui utilise méthode retrait avec une donnée nouvelle.
- Production attendue : la justification reste valable sur le nouveau cas.
- Contrainte de contrôle : inclure une étape calculable par un pair.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 8
- Objectif travaillé : O4.
- Capacité officielle : T-STRUCT-02A.
- Énoncé disciplinaire : étendre un énoncé volontairement erroné sur représentation.
- Production attendue : l’erreur est localisée puis réparée.
- Contrainte de contrôle : proposer une activité corrective inspirée de « Colorer définition de classe, constructeur et instance. ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
## Corrigé
### Corrigé exercice 1
- Méthode : identifier `Compte("Ada", 20)`, appliquer la méthode « initialiser les attributs après validation », puis écrire propriétaire Ada, solde 20.
- Résultat : propriétaire Ada, solde 20.
- Contrôle : faire apparaître le contrôle « solde initial négatif ».
- Erreur traitée : EF1 - Modifier directement un attribut sans passer par la méthode.
### Corrigé exercice 2
- Méthode : expliciter chaque étape de vérifier le montant puis modifier le solde avant de conclure par solde augmenté de 15.
- Résultat : solde augmenté de 15.
- Contrôle : rédiger la méthode avant le résultat.
- Erreur traitée : EF2 - Oublier de maintenir l’invariant.
### Corrigé exercice 3
- Méthode : comparer la donnée avec le cas limite « retrait supérieur au solde » et valider solde 13.
- Résultat : solde 13.
- Contrôle : comparer avec le cas « retrait supérieur au solde ».
- Erreur traitée : EF3 - Utiliser une variable globale pour l’état de l’objet.
### Corrigé exercice 4
- Méthode : isoler l’erreur fréquente « Confondre classe et instance. » puis reprendre la procédure correcte.
- Résultat : résumé lisible.
- Contrôle : corriger l’erreur « Confondre classe et instance. ».
- Erreur traitée : EF4 - Confondre classe et instance.
### Corrigé exercice 5
- Méthode : identifier `Compte("Ada", 20)`, appliquer la méthode « initialiser les attributs après validation », puis écrire propriétaire Ada, solde 20.
- Résultat : le comportement de constructeur est contrôlé.
- Contrôle : nommer la donnée minimale et la conclusion.
- Erreur traitée : EF1 - Modifier directement un attribut sans passer par la méthode.
### Corrigé exercice 6
- Méthode : expliciter chaque étape de vérifier le montant puis modifier le solde avant de conclure par solde augmenté de 15.
- Résultat : la méthode robuste est choisie et justifiée.
- Contrôle : identifier pourquoi « Oublier de maintenir l’invariant. » est une erreur.
- Erreur traitée : EF2 - Oublier de maintenir l’invariant.
### Corrigé exercice 7
- Méthode : comparer la donnée avec le cas limite « retrait supérieur au solde » et valider solde 13.
- Résultat : la justification reste valable sur le nouveau cas.
- Contrôle : inclure une étape calculable par un pair.
- Erreur traitée : EF3 - Utiliser une variable globale pour l’état de l’objet.
### Corrigé exercice 8
- Méthode : isoler l’erreur fréquente « Confondre classe et instance. » puis reprendre la procédure correcte.
- Résultat : l’erreur est localisée puis réparée.
- Contrôle : proposer une activité corrective inspirée de « Colorer définition de classe, constructeur et instance. ».
- Erreur traitée : EF4 - Confondre classe et instance.
## Erreurs fréquentes
- Erreur fréquente EF1 - Modifier directement un attribut sans passer par la méthode.
- Erreur fréquente EF2 - Oublier de maintenir l’invariant.
- Erreur fréquente EF3 - Utiliser une variable globale pour l’état de l’objet.
- Erreur fréquente EF4 - Confondre classe et instance.

## Remédiation ciblée
- Activité corrective EF1 : Tracer l’état avant et après chaque méthode.
- Activité corrective EF2 : Écrire l’invariant en marge de chaque opération.
- Activité corrective EF3 : Créer deux comptes pour vérifier l’indépendance des états.
- Activité corrective EF4 : Colorer définition de classe, constructeur et instance.

## Différenciation
- Socle : traiter `Compte("Ada", 20)` avec une fiche méthode fournie.
- Standard : traiter dépôt de 15 en rédigeant la justification complète.
- Expert : inventer un cas limite lié à « retrait supérieur au solde » et expliquer le comportement attendu.

## Critères de réussite
- La capacité officielle est citée dans la copie.
- La méthode contient au moins une étape vérifiable par un pair.
- Le cas limite est discuté avec une donnée concrète.
- La correction explique quelle erreur fréquente est évitée.
