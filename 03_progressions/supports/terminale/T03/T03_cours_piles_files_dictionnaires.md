---
title: "T03 - Cours - Piles, files et dictionnaires"
level: "terminale"
sequence_id: "T03"
document_type: "cours"
status: "needs_review"
version: "0.3.0"
source: "BO 2019 ; ressource locale candidate : Documents_DRIVE/2_NSI/Formation TOULOUSE/BLOC4/TD EIL - TAD - 2019-2020.pdf"
theme: "Structures linéaires"
notion: "LIFO, FIFO, dictionnaire d’index"
objectifs:
  - "Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation."
  - "Objectif O2 - Appliquer une méthode explicite sur un exemple guidé."
  - "Objectif O3 - Justifier le résultat obtenu sur un cas nouveau."
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente."
private_data: false
official_program:
  capacities:
    - "T-STRUCT-03A"
    - "T-STRUCT-03B"
    - "T-STRUCT-03C"
---


# T03 - Cours - Piles, files et dictionnaires

## Objectifs spécifiques
- Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation.
- Objectif O2 - Appliquer une méthode explicite sur un exemple guidé.
- Objectif O3 - Justifier le résultat obtenu sur un cas nouveau.
- Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente.

## Capacités officielles atomiques
- T-STRUCT-03A
- T-STRUCT-03B
- T-STRUCT-03C

## Prérequis
- Lire une consigne technique sans confondre donnée, méthode et résultat.
- Écrire une réponse sous forme de phrases courtes et vérifiables.
- Utiliser Python en distinguant expression, valeur, variable et affichage.
- Conserver une trace de calcul ou de raisonnement exploitable pour la révision.

## Séance(s) correspondante(s)
- T03-S1 à T03-S6 : ce support est rattaché aux séances indiquées dans la progression.

## Situation-problème concrète
une application doit gérer un historique d’annulation et une file d’attente de requêtes. La tâche consiste à traiter LIFO, FIFO, dictionnaire d’index sans réponse intuitive non vérifiée.

## Activité d’entrée
1. Lire la situation : une application doit gérer un historique d’annulation et une file d’attente de requêtes.
2. Isoler la donnée de départ : suite d’opérations sur collection linéaire.
3. Prédire individuellement le résultat de l’exemple `empiler A, empiler B, dépiler`.
4. Comparer deux stratégies et noter la divergence précise.
5. Appliquer la méthode retenue : choisir LIFO ou FIFO selon l’ordre de sortie attendu.
6. Contrôler avec le résultat de référence : B sort avant A pour une pile ; A sort avant B pour une file.
7. Tester le cas limite suivant : dépiler ou défiler une structure vide.
8. Rédiger une phrase qui relie donnée, méthode, résultat et contrôle.

## Définitions et formalisation
- Définition D1 : la notion centrale est LIFO, FIFO, dictionnaire d’index.
- Définition D2 : une donnée est une information manipulée avant transformation.
- Définition D3 : une représentation est une convention permettant d’agir sur cette donnée.
- Définition D4 : une preuve courte explique pourquoi la méthode aboutit au résultat.
- Définition D5 : un cas limite est un exemple volontairement petit, extrême ou ambigu.
- Exemple de référence : `empiler A, empiler B, dépiler`.
- Résultat de référence : B sort avant A pour une pile ; A sort avant B pour une file.
- Méthode de référence : choisir LIFO ou FIFO selon l’ordre de sortie attendu.
- Cas limite à surveiller : dépiler ou défiler une structure vide.

## Objectif O1 - Appropriation guidée
- Capacité officielle travaillée : T-STRUCT-03A.
- Question directrice : comment traiter LIFO, FIFO, dictionnaire d’index dans une situation vérifiable ?
- Donnée étudiée : suite d’opérations sur collection linéaire.
- Étape 1 : reformuler la consigne avec les mots de la capacité T-STRUCT-03A.
- Étape 2 : appliquer la méthode `choisir LIFO ou FIFO selon l’ordre de sortie attendu` sans sauter d’étape.
- Étape 3 : obtenir le résultat contrôlé `B sort avant A pour une pile ; A sort avant B pour une file` ou expliquer l’écart.
- Étape 4 : tester le cas limite `dépiler ou défiler une structure vide`.
- Étape 5 : écrire une justification de deux phrases.
- Exemple corrigé 1 : sur `empiler A, empiler B, dépiler`, on obtient `B sort avant A pour une pile ; A sort avant B pour une file` car choisir LIFO ou FIFO selon l’ordre de sortie attendu.
- Contre-exemple : une valeur finale isolée ne prouve pas la compétence.
- Question flash : quel mot de vocabulaire permet de justifier le choix de méthode ?
- Vérification : modifier une donnée seulement et prévoir l’effet avant de tester.
- Trace attendue : une ligne de calcul ou un état intermédiaire, puis une phrase de conclusion.
- Point de vigilance : ne pas changer de représentation au milieu du raisonnement.
- Socle : recopier la méthode sur le même exemple avec une donnée voisine.
- Standard : résoudre un exemple nouveau en autonomie.
- Expert : concevoir un cas limite et prédire l’échec ou la réussite.
- Critère de réussite : donnée, méthode, résultat et contrôle sont visibles.

## Objectif O2 - Appropriation guidée
- Capacité officielle travaillée : T-STRUCT-03B.
- Question directrice : comment traiter LIFO, FIFO, dictionnaire d’index dans une situation vérifiable ?
- Donnée étudiée : suite d’opérations sur collection linéaire.
- Étape 1 : reformuler la consigne avec les mots de la capacité T-STRUCT-03B.
- Étape 2 : appliquer la méthode `choisir LIFO ou FIFO selon l’ordre de sortie attendu` sans sauter d’étape.
- Étape 3 : obtenir le résultat contrôlé `B sort avant A pour une pile ; A sort avant B pour une file` ou expliquer l’écart.
- Étape 4 : tester le cas limite `dépiler ou défiler une structure vide`.
- Étape 5 : écrire une justification de deux phrases.
- Exemple corrigé 2 : sur `empiler A, empiler B, dépiler`, on obtient `B sort avant A pour une pile ; A sort avant B pour une file` car choisir LIFO ou FIFO selon l’ordre de sortie attendu.
- Contre-exemple : une valeur finale isolée ne prouve pas la compétence.
- Question flash : quel mot de vocabulaire permet de justifier le choix de méthode ?
- Vérification : modifier une donnée seulement et prévoir l’effet avant de tester.
- Trace attendue : une ligne de calcul ou un état intermédiaire, puis une phrase de conclusion.
- Point de vigilance : ne pas changer de représentation au milieu du raisonnement.
- Socle : recopier la méthode sur le même exemple avec une donnée voisine.
- Standard : résoudre un exemple nouveau en autonomie.
- Expert : concevoir un cas limite et prédire l’échec ou la réussite.
- Critère de réussite : donnée, méthode, résultat et contrôle sont visibles.

## Objectif O3 - Appropriation guidée
- Capacité officielle travaillée : T-STRUCT-03C.
- Question directrice : comment traiter LIFO, FIFO, dictionnaire d’index dans une situation vérifiable ?
- Donnée étudiée : suite d’opérations sur collection linéaire.
- Étape 1 : reformuler la consigne avec les mots de la capacité T-STRUCT-03C.
- Étape 2 : appliquer la méthode `choisir LIFO ou FIFO selon l’ordre de sortie attendu` sans sauter d’étape.
- Étape 3 : obtenir le résultat contrôlé `B sort avant A pour une pile ; A sort avant B pour une file` ou expliquer l’écart.
- Étape 4 : tester le cas limite `dépiler ou défiler une structure vide`.
- Étape 5 : écrire une justification de deux phrases.
- Exemple corrigé 3 : sur `empiler A, empiler B, dépiler`, on obtient `B sort avant A pour une pile ; A sort avant B pour une file` car choisir LIFO ou FIFO selon l’ordre de sortie attendu.
- Contre-exemple : une valeur finale isolée ne prouve pas la compétence.
- Question flash : quel mot de vocabulaire permet de justifier le choix de méthode ?
- Vérification : modifier une donnée seulement et prévoir l’effet avant de tester.
- Trace attendue : une ligne de calcul ou un état intermédiaire, puis une phrase de conclusion.
- Point de vigilance : ne pas changer de représentation au milieu du raisonnement.
- Socle : recopier la méthode sur le même exemple avec une donnée voisine.
- Standard : résoudre un exemple nouveau en autonomie.
- Expert : concevoir un cas limite et prédire l’échec ou la réussite.
- Critère de réussite : donnée, méthode, résultat et contrôle sont visibles.

## Objectif O4 - Appropriation guidée
- Capacité officielle travaillée : T-STRUCT-03A.
- Question directrice : comment traiter LIFO, FIFO, dictionnaire d’index dans une situation vérifiable ?
- Donnée étudiée : suite d’opérations sur collection linéaire.
- Étape 1 : reformuler la consigne avec les mots de la capacité T-STRUCT-03A.
- Étape 2 : appliquer la méthode `choisir LIFO ou FIFO selon l’ordre de sortie attendu` sans sauter d’étape.
- Étape 3 : obtenir le résultat contrôlé `B sort avant A pour une pile ; A sort avant B pour une file` ou expliquer l’écart.
- Étape 4 : tester le cas limite `dépiler ou défiler une structure vide`.
- Étape 5 : écrire une justification de deux phrases.
- Exemple corrigé 4 : sur `empiler A, empiler B, dépiler`, on obtient `B sort avant A pour une pile ; A sort avant B pour une file` car choisir LIFO ou FIFO selon l’ordre de sortie attendu.
- Contre-exemple : une valeur finale isolée ne prouve pas la compétence.
- Question flash : quel mot de vocabulaire permet de justifier le choix de méthode ?
- Vérification : modifier une donnée seulement et prévoir l’effet avant de tester.
- Trace attendue : une ligne de calcul ou un état intermédiaire, puis une phrase de conclusion.
- Point de vigilance : ne pas changer de représentation au milieu du raisonnement.
- Socle : recopier la méthode sur le même exemple avec une donnée voisine.
- Standard : résoudre un exemple nouveau en autonomie.
- Expert : concevoir un cas limite et prédire l’échec ou la réussite.
- Critère de réussite : donnée, méthode, résultat et contrôle sont visibles.

## Exercices numérotés
- Exercice 1 : traiter LIFO, FIFO, dictionnaire d’index pour l’objectif O1 et la capacité T-STRUCT-03A, puis écrire un contrôle explicite.
- Exercice 2 : traiter LIFO, FIFO, dictionnaire d’index pour l’objectif O2 et la capacité T-STRUCT-03B, puis écrire un contrôle explicite.
- Exercice 3 : traiter LIFO, FIFO, dictionnaire d’index pour l’objectif O3 et la capacité T-STRUCT-03C, puis écrire un contrôle explicite.
- Exercice 4 : traiter LIFO, FIFO, dictionnaire d’index pour l’objectif O4 et la capacité T-STRUCT-03A, puis écrire un contrôle explicite.
- Exercice 5 : traiter LIFO, FIFO, dictionnaire d’index pour l’objectif O1 et la capacité T-STRUCT-03B, puis écrire un contrôle explicite.
- Exercice 6 : traiter LIFO, FIFO, dictionnaire d’index pour l’objectif O2 et la capacité T-STRUCT-03C, puis écrire un contrôle explicite.
- Exercice 7 : traiter LIFO, FIFO, dictionnaire d’index pour l’objectif O3 et la capacité T-STRUCT-03A, puis écrire un contrôle explicite.
- Exercice 8 : traiter LIFO, FIFO, dictionnaire d’index pour l’objectif O4 et la capacité T-STRUCT-03B, puis écrire un contrôle explicite.

## Corrigés complets des exercices du cours
- Corrigé exercice 1 : identifier suite d’opérations sur collection linéaire, appliquer choisir LIFO ou FIFO selon l’ordre de sortie attendu, annoncer B sort avant A pour une pile ; A sort avant B pour une file, puis vérifier EF1.
- Corrigé exercice 2 : identifier suite d’opérations sur collection linéaire, appliquer choisir LIFO ou FIFO selon l’ordre de sortie attendu, annoncer B sort avant A pour une pile ; A sort avant B pour une file, puis vérifier EF2.
- Corrigé exercice 3 : identifier suite d’opérations sur collection linéaire, appliquer choisir LIFO ou FIFO selon l’ordre de sortie attendu, annoncer B sort avant A pour une pile ; A sort avant B pour une file, puis vérifier EF3.
- Corrigé exercice 4 : identifier suite d’opérations sur collection linéaire, appliquer choisir LIFO ou FIFO selon l’ordre de sortie attendu, annoncer B sort avant A pour une pile ; A sort avant B pour une file, puis vérifier EF4.
- Corrigé exercice 5 : identifier suite d’opérations sur collection linéaire, appliquer choisir LIFO ou FIFO selon l’ordre de sortie attendu, annoncer B sort avant A pour une pile ; A sort avant B pour une file, puis vérifier EF1.
- Corrigé exercice 6 : identifier suite d’opérations sur collection linéaire, appliquer choisir LIFO ou FIFO selon l’ordre de sortie attendu, annoncer B sort avant A pour une pile ; A sort avant B pour une file, puis vérifier EF2.
- Corrigé exercice 7 : identifier suite d’opérations sur collection linéaire, appliquer choisir LIFO ou FIFO selon l’ordre de sortie attendu, annoncer B sort avant A pour une pile ; A sort avant B pour une file, puis vérifier EF3.
- Corrigé exercice 8 : identifier suite d’opérations sur collection linéaire, appliquer choisir LIFO ou FIFO selon l’ordre de sortie attendu, annoncer B sort avant A pour une pile ; A sort avant B pour une file, puis vérifier EF4.

## Erreurs fréquentes
- Erreur fréquente EF1 - répondre seulement par `B sort avant A pour une pile ; A sort avant B pour une file` sans écrire la méthode.
- Erreur fréquente EF2 - appliquer choisir LIFO ou FIFO selon l’ordre de sortie attendu dans le mauvais ordre.
- Erreur fréquente EF3 - oublier le cas limite : dépiler ou défiler une structure vide.
- Erreur fréquente EF4 - citer une capacité officielle sans la relier à une production observable.

## Remédiation ciblée
- Activité corrective EF1 : reprendre l’exemple en imposant quatre colonnes, donnée, opération, résultat, contrôle.
- Activité corrective EF2 : refaire la méthode avec des étapes numérotées et une vérification à chaque étape.
- Activité corrective EF3 : construire deux variantes du cas limite `dépiler ou défiler une structure vide` et comparer les sorties.
- Activité corrective EF4 : associer chaque phrase de réponse à une capacité officielle citée en début de copie.

## Différenciation
- Socle : la méthode est fournie sous forme de tableau à compléter.
- Standard : l’élève choisit la méthode et rédige la justification complète.
- Expert : l’élève crée un contre-exemple ou un cas limite et explique l’échec attendu.

## Critères de réussite
- Les objectifs O1 à O4 apparaissent dans la production ou dans la correction.
- Au moins une capacité officielle est reliée à une question traitée.
- Le résultat est accompagné d’une méthode et d’un contrôle.
- Les erreurs fréquentes sont nommées et corrigées par une activité de remédiation.

## Synthèse à retenir
- Un document NSI utile relie toujours notion, capacité, méthode, résultat et contrôle.
- La trace doit pouvoir être relue une semaine plus tard sans ajouter d’information orale.
- La correction sert à comprendre l’erreur, pas seulement à vérifier une valeur finale.

## Consolidation de fin de cours
- Question de consolidation 1 : réécrire l’objectif O1 avec les mots de la situation-problème.
- Question de consolidation 2 : associer chaque donnée de l’exemple à une étape de méthode.
- Question de consolidation 3 : produire une vérification indépendante du résultat annoncé.
- Question de consolidation 4 : nommer l’erreur fréquente la plus probable et sa remédiation.
- Question de consolidation 5 : indiquer la capacité officielle mobilisée par la dernière étape.
- Question de consolidation 6 : expliquer pourquoi le cas limite ne peut pas être ignoré.
- Question de consolidation 7 : rédiger une phrase de synthèse utilisable dans la trace écrite.
- Question de consolidation 8 : préparer une question pour le TD en conservant le même objectif.
- Critère final : le cours peut être relu sans support oral supplémentaire.
