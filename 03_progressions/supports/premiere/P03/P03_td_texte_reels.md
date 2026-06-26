---
title: "P03 - Td - Texte Unicode et nombres réels"
level: "premiere"
sequence_id: "P03"
document_type: "td"
status: "needs_review"
version: "0.4.1"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Données textuelles et approximation"
notion: "Unicode, UTF-8, octet, flottant"
objectifs:
  - "Objectif O1 - Identifier précisément la représentation ou la structure en jeu"
  - "Objectif O2 - Appliquer une méthode disciplinaire complète"
  - "Objectif O3 - Justifier le résultat sur un cas différent"
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur observée"
private_data: false
official_program:
  capacities:
    - "P-DATA-BASE-05A"
---

# P03 - TD - Texte Unicode et nombres réels

## Objectifs spécifiques
- Objectif O1 - Identifier précisément la représentation ou la structure en jeu.
- Objectif O2 - Appliquer une méthode disciplinaire complète.
- Objectif O3 - Justifier le résultat sur un cas différent.
- Objectif O4 - Contrôler un cas limite et corriger une erreur observée.

## Capacités officielles atomiques
- P-DATA-BASE-05A

## Prérequis
- Reconnaître une consigne liée à Unicode.
- Distinguer donnée, méthode et conclusion dans le thème Données textuelles et approximation.
- Rédiger une justification courte en utilisant le vocabulaire du programme.
- Contrôler une réponse par un cas limite ou un contre-exemple explicite.

## Séance(s) correspondante(s)
- P03-S1 à P03-S5 : support rattaché aux séances prêtes de la progression.

## Situation-problème concrète
Un formulaire international mélange accents, symboles monétaires et mesures décimales calculées par programme.

## Activité d’entrée
1. Comparer `A`, `é` et `€` selon caractères et octets.
2. Encoder `Aé` en UTF-8.
3. Observer `0.1 + 0.2` dans Python.
4. Décider quand utiliser une tolérance.

## Exemples corrigés précis
### Exemple corrigé 1 - ASCII simple
- Donnée étudiée : `A`.
- Méthode : lire le point de code U+0041 puis son octet UTF-8.
- Résultat obtenu : `41` en hexadécimal.
- Contrôle : le cas limite « caractère dans l’ASCII » est vérifié séparément.
### Exemple corrigé 2 - accent UTF-8
- Donnée étudiée : `é`.
- Méthode : distinguer un caractère et deux octets.
- Résultat obtenu : `c3 a9`.
- Contrôle : le cas limite « longueur en octets différente de la longueur en caractères » est vérifié séparément.
### Exemple corrigé 3 - chaîne mixte
- Donnée étudiée : `Aé`.
- Méthode : additionner les tailles UTF-8 de chaque caractère.
- Résultat obtenu : 2 caractères et 3 octets.
- Contrôle : le cas limite « chaîne vide » est vérifié séparément.
### Exemple corrigé 4 - flottant
- Donnée étudiée : `0.1 + 0.2`.
- Méthode : comparer avec une tolérance au lieu de `==`.
- Résultat obtenu : valeur proche de `0.3`.
- Contrôle : le cas limite « arrondi binaire » est vérifié séparément.
## Exercices numérotés
### Exercice 1
- Objectif travaillé : O1.
- Capacité officielle : P-DATA-BASE-05A.
- Énoncé disciplinaire : résoudre ASCII simple avec `A`.
- Production attendue : `41` en hexadécimal.
- Contrainte de contrôle : faire apparaître le contrôle « caractère dans l’ASCII ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 2
- Objectif travaillé : O2.
- Capacité officielle : P-DATA-BASE-05A.
- Énoncé disciplinaire : expliquer accent UTF-8 à partir de `é`.
- Production attendue : `c3 a9`.
- Contrainte de contrôle : rédiger la méthode avant le résultat.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 3
- Objectif travaillé : O3.
- Capacité officielle : P-DATA-BASE-05A.
- Énoncé disciplinaire : comparer chaîne mixte avec `Aé`.
- Production attendue : 2 caractères et 3 octets.
- Contrainte de contrôle : comparer avec le cas « chaîne vide ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 4
- Objectif travaillé : O4.
- Capacité officielle : P-DATA-BASE-05A.
- Énoncé disciplinaire : corriger flottant pour `0.1 + 0.2`.
- Production attendue : valeur proche de `0.3`.
- Contrainte de contrôle : corriger l’erreur « Confondre point de code et représentation binaire. ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 5
- Objectif travaillé : O1.
- Capacité officielle : P-DATA-BASE-05A.
- Énoncé disciplinaire : tester un cas limite lié à caractère dans l’ASCII.
- Production attendue : le comportement de ASCII simple est contrôlé.
- Contrainte de contrôle : nommer la donnée minimale et la conclusion.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 6
- Objectif travaillé : O2.
- Capacité officielle : P-DATA-BASE-05A.
- Énoncé disciplinaire : classer deux méthodes possibles pour accent UTF-8.
- Production attendue : la méthode robuste est choisie et justifiée.
- Contrainte de contrôle : identifier pourquoi « Croire que tout caractère occupe un octet. » est une erreur.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 7
- Objectif travaillé : O3.
- Capacité officielle : P-DATA-BASE-05A.
- Énoncé disciplinaire : justifier un transfert qui utilise chaîne mixte avec une donnée nouvelle.
- Production attendue : la justification reste valable sur le nouveau cas.
- Contrainte de contrôle : inclure une étape calculable par un pair.
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
### Exercice 8
- Objectif travaillé : O4.
- Capacité officielle : P-DATA-BASE-05A.
- Énoncé disciplinaire : étendre un énoncé volontairement erroné sur flottant.
- Production attendue : l’erreur est localisée puis réparée.
- Contrainte de contrôle : proposer une activité corrective inspirée de « Séparer nom du caractère et encodage effectif. ».
- Critère local : la réponse contient une donnée, une méthode, un résultat et une vérification.
## Corrigé
### Corrigé exercice 1
- Méthode : identifier `A`, appliquer la méthode « lire le point de code U+0041 puis son octet UTF-8 », puis écrire `41` en hexadécimal.
- Résultat : `41` en hexadécimal.
- Contrôle : faire apparaître le contrôle « caractère dans l’ASCII ».
- Erreur traitée : EF1 - Compter les caractères au lieu des octets en UTF-8.
### Corrigé exercice 2
- Méthode : expliciter chaque étape de distinguer un caractère et deux octets avant de conclure par `c3 a9`.
- Résultat : `c3 a9`.
- Contrôle : rédiger la méthode avant le résultat.
- Erreur traitée : EF2 - Croire que tout caractère occupe un octet.
### Corrigé exercice 3
- Méthode : comparer la donnée avec le cas limite « chaîne vide » et valider 2 caractères et 3 octets.
- Résultat : 2 caractères et 3 octets.
- Contrôle : comparer avec le cas « chaîne vide ».
- Erreur traitée : EF3 - Comparer deux flottants avec égalité stricte après calcul.
### Corrigé exercice 4
- Méthode : isoler l’erreur fréquente « Confondre point de code et représentation binaire. » puis reprendre la procédure correcte.
- Résultat : valeur proche de `0.3`.
- Contrôle : corriger l’erreur « Confondre point de code et représentation binaire. ».
- Erreur traitée : EF4 - Confondre point de code et représentation binaire.
### Corrigé exercice 5
- Méthode : identifier `A`, appliquer la méthode « lire le point de code U+0041 puis son octet UTF-8 », puis écrire `41` en hexadécimal.
- Résultat : le comportement de ASCII simple est contrôlé.
- Contrôle : nommer la donnée minimale et la conclusion.
- Erreur traitée : EF1 - Compter les caractères au lieu des octets en UTF-8.
### Corrigé exercice 6
- Méthode : expliciter chaque étape de distinguer un caractère et deux octets avant de conclure par `c3 a9`.
- Résultat : la méthode robuste est choisie et justifiée.
- Contrôle : identifier pourquoi « Croire que tout caractère occupe un octet. » est une erreur.
- Erreur traitée : EF2 - Croire que tout caractère occupe un octet.
### Corrigé exercice 7
- Méthode : comparer la donnée avec le cas limite « chaîne vide » et valider 2 caractères et 3 octets.
- Résultat : la justification reste valable sur le nouveau cas.
- Contrôle : inclure une étape calculable par un pair.
- Erreur traitée : EF3 - Comparer deux flottants avec égalité stricte après calcul.
### Corrigé exercice 8
- Méthode : isoler l’erreur fréquente « Confondre point de code et représentation binaire. » puis reprendre la procédure correcte.
- Résultat : l’erreur est localisée puis réparée.
- Contrôle : proposer une activité corrective inspirée de « Séparer nom du caractère et encodage effectif. ».
- Erreur traitée : EF4 - Confondre point de code et représentation binaire.
## Erreurs fréquentes
- Erreur fréquente EF1 - Compter les caractères au lieu des octets en UTF-8.
- Erreur fréquente EF2 - Croire que tout caractère occupe un octet.
- Erreur fréquente EF3 - Comparer deux flottants avec égalité stricte après calcul.
- Erreur fréquente EF4 - Confondre point de code et représentation binaire.

## Remédiation ciblée
- Activité corrective EF1 : Afficher la liste des octets avec `encode("utf-8")`.
- Activité corrective EF2 : Construire un tableau caractère, point de code, octets.
- Activité corrective EF3 : Utiliser une tolérance absolue et justifier son ordre de grandeur.
- Activité corrective EF4 : Séparer nom du caractère et encodage effectif.

## Différenciation
- Socle : traiter `A` avec une fiche méthode fournie.
- Standard : traiter `é` en rédigeant la justification complète.
- Expert : inventer un cas limite lié à « chaîne vide » et expliquer le comportement attendu.

## Critères de réussite
- La capacité officielle est citée dans la copie.
- La méthode contient au moins une étape vérifiable par un pair.
- Le cas limite est discuté avec une donnée concrète.
- La correction explique quelle erreur fréquente est évitée.
