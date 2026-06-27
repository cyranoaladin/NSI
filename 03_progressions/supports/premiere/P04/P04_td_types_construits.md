---
title: "P04 - Td - Types construits"
level: "premiere"
sequence_id: "P04"
document_type: "td"
status: "needs_review"
version: "0.4.1"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Tuples, listes, dictionnaires"
notion: "tuple, liste, dictionnaire, mutabilité"
objectifs:
  - "Objectif O1 - Identifier précisément la représentation ou la structure en jeu"
  - "Objectif O2 - Appliquer une méthode disciplinaire complète"
  - "Objectif O3 - Justifier le résultat sur un cas différent"
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur observée"
private_data: false
official_program:
  capacities:
    - "P-DATA-CONSTR-02A"
---

# P04 - TD - Types construits

## Objectifs spécifiques
- Objectif O1 - Identifier précisément la représentation ou la structure en jeu.
- Objectif O2 - Appliquer une méthode disciplinaire complète.
- Objectif O3 - Justifier le résultat sur un cas différent.
- Objectif O4 - Contrôler un cas limite et corriger une erreur observée.

## Capacités officielles atomiques
- P-DATA-CONSTR-02A

## Prérequis
- Reconnaître une consigne liée à tuple.
- Distinguer donnée, méthode et conclusion dans le thème Tuples, listes, dictionnaires.
- Rédiger une justification courte en utilisant le vocabulaire du programme.
- Contrôler une réponse par un cas limite ou un contre-exemple explicite.

## Séance(s) correspondante(s)
- P04-S1 à P04-S7 : support rattaché aux séances prêtes de la progression.

## Situation-problème concrète
Une station météo stocke des coordonnées fixes, des relevés horaires modifiables et des mesures accessibles par nom.

## Activité d’entrée
1. Identifier ce qui doit rester immuable dans un tuple.
2. Modifier une liste de températures.
3. Lire une clé dans un dictionnaire de station.
4. Décrire ce qui se passe avec une liste vide.

## Exemples corrigés précis
### Exemple corrigé 1 - tuple de coordonnées
- Donnée étudiée : `(36.8, 10.2)`.
- Méthode : lire sans modifier et nommer latitude puis longitude.
- Résultat obtenu : coordonnées conservées.
- Contrôle : le cas limite « tentative de modification interdite » est vérifié séparément.
### Exemple corrigé 2 - liste de relevés
- Donnée étudiée : `[18, 20, 19]`.
- Méthode : parcourir les valeurs et calculer une moyenne.
- Résultat obtenu : `19`.
- Contrôle : le cas limite « liste vide » est vérifié séparément.
### Exemple corrigé 3 - dictionnaire
- Donnée étudiée : `{"temperature": 21, "vent": 12}`.
- Méthode : tester la présence de la clé avant lecture.
- Résultat obtenu : `21` pour `temperature`.
- Contrôle : le cas limite « clé absente » est vérifié séparément.
### Exemple corrigé 4 - copie de liste
- Donnée étudiée : `[[1], [2]]`.
- Méthode : distinguer copie superficielle et copie indépendante.
- Résultat obtenu : modification locale contrôlée.
- Contrôle : le cas limite « liste imbriquée » est vérifié séparément.
## Exercices numérotés
### Exercice 1
- Objectif travaillé : O1.
- Capacité officielle : P-DATA-CONSTR-02A.
- Énoncé disciplinaire : résoudre tuple de coordonnées avec `(36.8, 10.2)`.
- Production attendue : coordonnées conservées.
- Contrainte de contrôle : faire apparaître le contrôle « tentative de modification interdite ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 2
- Objectif travaillé : O2.
- Capacité officielle : P-DATA-CONSTR-02A.
- Énoncé disciplinaire : expliquer liste de relevés à partir de `[18, 20, 19]`.
- Production attendue : `19`.
- Contrainte de contrôle : rédiger la méthode avant le résultat.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 3
- Objectif travaillé : O3.
- Capacité officielle : P-DATA-CONSTR-02A.
- Énoncé disciplinaire : comparer dictionnaire avec `{"temperature": 21, "vent": 12}`.
- Production attendue : `21` pour `temperature`.
- Contrainte de contrôle : comparer avec le cas « clé absente ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 4
- Objectif travaillé : O4.
- Capacité officielle : P-DATA-CONSTR-02A.
- Énoncé disciplinaire : corriger copie de liste pour `[[1], [2]]`.
- Production attendue : modification locale contrôlée.
- Contrainte de contrôle : corriger l’erreur « Copier une liste imbriquée seulement au premier niveau. ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 5
- Objectif travaillé : O1.
- Capacité officielle : P-DATA-CONSTR-02A.
- Énoncé disciplinaire : tester un cas limite lié à tentative de modification interdite.
- Production attendue : le comportement de tuple de coordonnées est contrôlé.
- Contrainte de contrôle : nommer la donnée minimale et la conclusion.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 6
- Objectif travaillé : O2.
- Capacité officielle : P-DATA-CONSTR-02A.
- Énoncé disciplinaire : classer deux méthodes possibles pour liste de relevés.
- Production attendue : la méthode robuste est choisie et justifiée.
- Contrainte de contrôle : identifier pourquoi « Parcourir les indices quand les valeurs suffisent. » est une erreur.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 7
- Objectif travaillé : O3.
- Capacité officielle : P-DATA-CONSTR-02A.
- Énoncé disciplinaire : justifier un transfert qui utilise dictionnaire avec une donnée nouvelle.
- Production attendue : la justification reste valable sur le nouveau cas.
- Contrainte de contrôle : inclure une étape calculable par un pair.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 8
- Objectif travaillé : O4.
- Capacité officielle : P-DATA-CONSTR-02A.
- Énoncé disciplinaire : étendre un énoncé volontairement erroné sur copie de liste.
- Production attendue : l’erreur est localisée puis réparée.
- Contrainte de contrôle : proposer une activité corrective inspirée de « Modifier une sous-liste et observer l’effet sur la copie. ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
## Corrigé
### Corrigé exercice 1
- Méthode : identifier `(36.8, 10.2)`, appliquer la méthode « lire sans modifier et nommer latitude puis longitude », puis écrire coordonnées conservées.
- Résultat : coordonnées conservées.
- Contrôle : faire apparaître le contrôle « tentative de modification interdite ».
- Erreur traitée : EF1 - Modifier un tuple comme une liste.
### Corrigé exercice 2
- Méthode : expliciter chaque étape de parcourir les valeurs et calculer une moyenne avant de conclure par `19`.
- Résultat : `19`.
- Contrôle : rédiger la méthode avant le résultat.
- Erreur traitée : EF2 - Parcourir les indices quand les valeurs suffisent.
### Corrigé exercice 3
- Méthode : comparer la donnée avec le cas limite « clé absente » et valider `21` pour `temperature`.
- Résultat : `21` pour `temperature`.
- Contrôle : comparer avec le cas « clé absente ».
- Erreur traitée : EF3 - Accéder à une clé sans vérifier sa présence.
### Corrigé exercice 4
- Méthode : isoler l’erreur fréquente « Copier une liste imbriquée seulement au premier niveau. » puis reprendre la procédure correcte.
- Résultat : modification locale contrôlée.
- Contrôle : corriger l’erreur « Copier une liste imbriquée seulement au premier niveau. ».
- Erreur traitée : EF4 - Copier une liste imbriquée seulement au premier niveau.
### Corrigé exercice 5
- Méthode : identifier `(36.8, 10.2)`, appliquer la méthode « lire sans modifier et nommer latitude puis longitude », puis écrire coordonnées conservées.
- Résultat : le comportement de tuple de coordonnées est contrôlé.
- Contrôle : nommer la donnée minimale et la conclusion.
- Erreur traitée : EF1 - Modifier un tuple comme une liste.
### Corrigé exercice 6
- Méthode : expliciter chaque étape de parcourir les valeurs et calculer une moyenne avant de conclure par `19`.
- Résultat : la méthode robuste est choisie et justifiée.
- Contrôle : identifier pourquoi « Parcourir les indices quand les valeurs suffisent. » est une erreur.
- Erreur traitée : EF2 - Parcourir les indices quand les valeurs suffisent.
### Corrigé exercice 7
- Méthode : comparer la donnée avec le cas limite « clé absente » et valider `21` pour `temperature`.
- Résultat : la justification reste valable sur le nouveau cas.
- Contrôle : inclure une étape calculable par un pair.
- Erreur traitée : EF3 - Accéder à une clé sans vérifier sa présence.
### Corrigé exercice 8
- Méthode : isoler l’erreur fréquente « Copier une liste imbriquée seulement au premier niveau. » puis reprendre la procédure correcte.
- Résultat : l’erreur est localisée puis réparée.
- Contrôle : proposer une activité corrective inspirée de « Modifier une sous-liste et observer l’effet sur la copie. ».
- Erreur traitée : EF4 - Copier une liste imbriquée seulement au premier niveau.
## Erreurs fréquentes
- Erreur fréquente EF1 - Modifier un tuple comme une liste.
- Erreur fréquente EF2 - Parcourir les indices quand les valeurs suffisent.
- Erreur fréquente EF3 - Accéder à une clé sans vérifier sa présence.
- Erreur fréquente EF4 - Copier une liste imbriquée seulement au premier niveau.

## Remédiation ciblée
- Activité corrective EF1 : Identifier mutabilité et usage avant d’écrire une affectation.
- Activité corrective EF2 : Écrire deux boucles, avec indices puis avec valeurs, et comparer.
- Activité corrective EF3 : Tester `cle in dictionnaire` avant la lecture.
- Activité corrective EF4 : Modifier une sous-liste et observer l’effet sur la copie.

## Différenciation
- Socle : traiter `(36.8, 10.2)` avec une fiche méthode fournie.
- Standard : traiter `[18, 20, 19]` en rédigeant la justification complète.
- Expert : inventer un cas limite lié à « clé absente » et expliquer le comportement attendu.

## Critères de réussite
- La capacité officielle est citée dans la copie.
- La méthode contient au moins une étape vérifiable par un pair.
- Le cas limite est discuté avec une donnée concrète.
- La correction explique quelle erreur fréquente est évitée.

## Complément d’exercices corrigés - types construits
### Exercice 9 - Milieu de deux coordonnées
- Données : `A = (0, 4)`, `B = (6, 10)`.
- Consigne : écrire la formule du milieu et préciser pourquoi un tuple convient.

### Exercice 10 - Liste mutable
- Données : `notes = [8, 12, 10]`.
- Consigne : remplacer la deuxième note par `14`, puis donner la liste.

### Exercice 11 - Liste de dictionnaires
- Données : `stations = [{"nom": "A", "temperature": 21}, {"nom": "B", "temperature": 18}, {"nom": "C", "temperature": 23}]`.
- Consigne : extraire les noms des stations dont la température est au moins `20`.

### Exercice 12 - Cas limites
- Données : `point = (2,)`, `station = {"temperature": 21}`, `notes = []`.
- Consigne : associer chaque donnée à l’erreur possible.

### Corrigé exercice 9
- Donnée utilisée : `A = (0, 4)` et `B = (6, 10)`.
- Méthode : appliquer la formule `((x_A+x_B)/2, (y_A+y_B)/2)`.
- Résultat attendu : le milieu vaut `((0+6)/2, (4+10)/2) = (3.0, 7.0)`.
- Contrôle : le résultat est un tuple de taille 2, adapté à une coordonnée fixe.

### Corrigé exercice 10
- Donnée utilisée : `notes = [8, 12, 10]`.
- Méthode : l’indice `1` désigne la deuxième case d’une liste mutable.
- Résultat attendu : après `notes[1] = 14`, la liste vaut `[8, 14, 10]`.
- Contrôle : la longueur reste `3`, seule la valeur de rang 2 change.

### Corrigé exercice 11
- Donnée utilisée : `stations = [{"nom": "A", "temperature": 21}, {"nom": "B", "temperature": 18}, {"nom": "C", "temperature": 23}]`.
- Méthode : parcourir la liste, lire la clé `temperature`, conserver les dictionnaires dont `temperature >= 20`, puis lire la clé `nom`.
- Résultat attendu : les noms extraits sont `["A", "C"]`.
- Contrôle : la station `"B"` est exclue car `18 < 20`.

### Corrigé exercice 12
- Donnée utilisée : `point = (2,)`, `station = {"temperature": 21}`, `notes = []`.
- Méthode : associer chaque donnée à son cas limite structurel.
- Résultat attendu : `point` a une mauvaise taille pour une coordonnée 2D ; `station["pression"]` provoquerait une clé absente ; `notes` ne permet pas de moyenne sans convention.
- Contrôle : chaque erreur est liée à un type différent : tuple, dictionnaire, liste.
