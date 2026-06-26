---
title: "T09 - EVALUATION - Bases relationnelles, clés et contraintes"
level: "terminale"
sequence_id: "T09"
document_type: "evaluation"
status: "needs_review"
version: "0.2.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Bases de données"
notion: "tables, clés primaires, clés étrangères, contraintes"
objectifs:
  - "identifier la clé primaire de chaque table"
  - "repérer la clé étrangère Note.id_eleve"
  - "signaler une référence vers un élève absent"
  - "distinguer contrainte de domaine et contrainte de référence"
private_data: false
official_program:
  capacities:
    - "T-BDD-01A"
    - "T-BDD-01B"
    - "T-BDD-01C"
    - "T-BDD-02"
---

# T09 - Évaluation courte - Bases relationnelles, clés et contraintes

## Objectifs évalués
- O1 : identifier la clé primaire de chaque table.
- O2 : repérer la clé étrangère Note.id_eleve.
- O3 : signaler une référence vers un élève absent.
- O4 : distinguer contrainte de domaine et contrainte de référence.

## Capacités officielles
- T-BDD-01A
- T-BDD-01B
- T-BDD-01C
- T-BDD-02

## Questions
### Question 1
- Capacité : T-BDD-01A.
- Énoncé : avec `Eleve(1, "E2", "1G1"), Note(10, 1, "NSI", 15), Note(11, 9, "NSI", 12)`, identifier la clé primaire de chaque table.
- Réponse attendue : méthode explicite, résultat contrôlé et vocabulaire du chapitre T09.
- Critère de réussite : l’erreur « utiliser le nom comme clé primaire » est évitée ou corrigée.
### Question 2
- Capacité : T-BDD-01B.
- Énoncé : avec `Eleve(1, "E2", "1G1"), Note(10, 1, "NSI", 15), Note(11, 9, "NSI", 12)`, repérer la clé étrangère Note.id_eleve.
- Réponse attendue : méthode explicite, résultat contrôlé et vocabulaire du chapitre T09.
- Critère de réussite : l’erreur « accepter une note hors 0..20 » est évitée ou corrigée.
### Question 3
- Capacité : T-BDD-01C.
- Énoncé : avec `Eleve(1, "E2", "1G1"), Note(10, 1, "NSI", 15), Note(11, 9, "NSI", 12)`, signaler une référence vers un élève absent.
- Réponse attendue : méthode explicite, résultat contrôlé et vocabulaire du chapitre T09.
- Critère de réussite : l’erreur « insérer une note pour un élève absent » est évitée ou corrigée.
### Question 4
- Capacité : T-BDD-02.
- Énoncé : avec `Eleve(1, "E2", "1G1"), Note(10, 1, "NSI", 15), Note(11, 9, "NSI", 12)`, distinguer contrainte de domaine et contrainte de référence.
- Réponse attendue : méthode explicite, résultat contrôlé et vocabulaire du chapitre T09.
- Critère de réussite : l’erreur « confondre clé primaire et clé étrangère » est évitée ou corrigée.

## Barème
- Question 1 : 2 points méthode, 1 point résultat, 1 point contrôle du cas limite.
- Question 2 : 2 points méthode, 1 point résultat, 1 point contrôle du cas limite.
- Question 3 : 2 points méthode, 1 point résultat, 1 point contrôle du cas limite.
- Question 4 : 2 points méthode, 1 point résultat, 1 point contrôle du cas limite.

## Corrigé
### Corrigé question 1
- Démarche : dans `Eleve(id_eleve, nom, classe)`, la valeur qui identifie une ligne est `id_eleve`; dans `Note(id_note, id_eleve, matiere, note)`, la valeur qui identifie une ligne de note est `id_note`.
- Résultat attendu : clés primaires `Eleve.id_eleve` et `Note.id_note`. Pour les lignes données, les identifiants primaires sont `1`, `10` et `11`.
- Justification : le nom `"E2"` n’est pas une clé primaire fiable, car deux élèves pourraient porter le même nom; l’identifiant numérique reste unique.
### Corrigé question 2
- Démarche : comparer `Note.id_eleve` aux valeurs existantes de `Eleve.id_eleve`.
- Résultat attendu : `Note.id_eleve` est une clé étrangère vers `Eleve.id_eleve`. La ligne `Note(10, 1, "NSI", 15)` est cohérente car `1` existe dans `Eleve`; la ligne `Note(11, 9, "NSI", 12)` pose problème car aucun `Eleve.id_eleve = 9` n’est fourni.
- Justification : la contrainte de référence porte sur l’existence de l’élève, pas sur la valeur de la note.
### Corrigé question 3
- Démarche : isoler chaque note et tester si son `id_eleve` est présent dans la table `Eleve`.
- Résultat attendu : la référence invalide est `Note(11, 9, "NSI", 12)`, car `9` ne correspond à aucun élève connu. Cette ligne doit être refusée ou mise en attente tant que l’élève `9` n’existe pas.
- Justification : accepter cette ligne créerait une note orpheline, impossible à rattacher à un élève.
### Corrigé question 4
- Démarche : classer les contraintes selon ce qu’elles vérifient.
- Résultat attendu : `0 <= note <= 20` est une contrainte de domaine sur l’attribut `Note.note`; `Note.id_eleve` doit appartenir aux valeurs de `Eleve.id_eleve` est une contrainte de référence. Dans les données, `15` et `12` respectent le domaine, mais `id_eleve=9` viole la référence.
- Justification : une même ligne peut respecter le domaine de la note tout en violant la clé étrangère.

## Critères de réussite
- Les capacités officielles sont citées dans les réponses.
- Chaque question contient donnée, méthode, résultat et contrôle.
- Le vocabulaire disciplinaire est utilisé sans remplacer la justification.
- Le barème reste indicatif tant que la ressource est en needs_review.

## Modalités de passation
- Durée : 25 minutes.
- Matériel autorisé : fiche personnelle, sans corrigé ni accès réseau.
- Capacités évaluées :
- T-BDD-01A
- T-BDD-01B
- T-BDD-01C
- T-BDD-02
- T-BDD-01A
- T-BDD-01B
- T-BDD-01C
- T-BDD-02

## Fiche liée et aménagement
- Fiche liée : fiche de cours opérationnelle de la séquence T09, statut `needs_review`.
- Séance liée : `T09-S1` dans la progression annuelle.
- Version aménagée : même sujet avec données surlignées et tableau méthode / résultat / contrôle.
- Remédiation : reprendre la question la moins réussie avec une donnée plus courte puis faire verbaliser la méthode.
## Erreurs fréquentes
- EF1 : répondre sans citer la donnée utilisée ; correction : encadrer la donnée avant de rédiger.
- EF2 : donner un résultat sans méthode ; correction : séparer méthode, résultat et contrôle.
- EF3 : oublier le cas limite ; correction : refaire une question avec une donnée minimale.
