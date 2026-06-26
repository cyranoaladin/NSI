---
title: "T00 - Tp - Diagnostic Terminale et tests"
level: "terminale"
sequence_id: "T00"
document_type: "tp"
status: "needs_review"
version: "0.3.0"
source: "BO 2019 ; ressource locale candidate : Documents_DRIVE/2_Tles NSI/0_Ressources/liens_ressources.odt"
theme: "Reprise Python et qualité"
notion: "tests, modularité, invariants simples"
objectifs:
  - "Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation."
  - "Objectif O2 - Appliquer une méthode explicite sur un exemple guidé."
  - "Objectif O3 - Justifier le résultat obtenu sur un cas nouveau."
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente."
private_data: false
official_program:
  capacities:
    - "T-HIST-01A"
    - "T-HIST-01B"
    - "T-LANG-03A"
    - "T-LANG-05"
---


# T00 - Tp - Diagnostic Terminale et tests

## Objectifs spécifiques
- Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation.
- Objectif O2 - Appliquer une méthode explicite sur un exemple guidé.
- Objectif O3 - Justifier le résultat obtenu sur un cas nouveau.
- Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente.

## Capacités officielles atomiques
- T-HIST-01A
- T-HIST-01B
- T-LANG-03A
- T-LANG-05

## Prérequis
- Lire une consigne technique sans confondre donnée, méthode et résultat.
- Écrire une réponse sous forme de phrases courtes et vérifiables.
- Utiliser Python en distinguant expression, valeur, variable et affichage.
- Conserver une trace de calcul ou de raisonnement exploitable pour la révision.

## Séance(s) correspondante(s)
- T00-S1 à T00-S4 : ce support est rattaché aux séances indiquées dans la progression.

## Situation-problème concrète
un code repris de Première donne parfois le bon résultat mais ne possède aucun test explicite. La tâche consiste à traiter tests, modularité, invariants simples sans réponse intuitive non vérifiée.

## Activité d’entrée
1. Lire la situation : un code repris de Première donne parfois le bon résultat mais ne possède aucun test explicite.
2. Isoler la donnée de départ : liste de valeurs et contrat de fonction.
3. Prédire individuellement le résultat de l’exemple `fonction maximum([3, 8, 2])`.
4. Comparer deux stratégies et noter la divergence précise.
5. Appliquer la méthode retenue : isoler la fonction, écrire le contrat, tester cas nominal et cas limite.
6. Contrôler avec le résultat de référence : 8 avec test nominal, test limite et test d’erreur.
7. Tester le cas limite suivant : liste vide ou mutation inattendue.
8. Rédiger une phrase qui relie donnée, méthode, résultat et contrôle.

## Consigne technique détaillée
- Mission : organiser un module Python avec tests attendus et cas limites.
- Starter code : `03_progressions/supports/terminale/T00/code/T00_starter_diagnostic_tests.py`.
- Tests attendus : `03_progressions/supports/terminale/T00/code/T00_tests_attendus_diagnostic_tests.py`.
- Corrigé professeur séparé : `03_progressions/supports/terminale/T00/code/T00_corrige_professeur_diagnostic_tests.py`.
- Fonction principale à compléter ou contrôler : `maximum_controle(valeurs)`.
- Exemple d’entrée : `[3, 8, 2]`.
- Exemple d’exécution : l’exemple de référence `fonction maximum([3, 8, 2])` conduit à `8 avec test nominal, test limite et test d’erreur`.
- Cas limite : liste vide ou mutation inattendue.
- Livrable vérifiable : fichier Python exécutable et capture textuelle des tests attendus.

## Tests attendus
- Test 1 : cas nominal issu de l’exemple du cours.
- Test 2 : cas limite annoncé dans la trace.
- Test 3 : entrée invalide ou ambiguë, avec comportement documenté.
- Test 4 : non-régression sur une variante numérique ou structurelle.

## Exemple corrigé précis
- On appelle `maximum_controle([3, 8, 2])`.
- La fonction doit appliquer isoler la fonction, écrire le contrat, tester cas nominal et cas limite.
- Le résultat contrôlé est `8 avec test nominal, test limite et test d’erreur` ou une structure portant cette information.
- Le test attendu compare la sortie à une valeur connue plutôt qu’à une impression visuelle.

## Exercices numérotés
- Exercice 1 : ajouter un test ou une variante pour l’objectif O1 et expliquer le résultat.
- Exercice 2 : ajouter un test ou une variante pour l’objectif O2 et expliquer le résultat.
- Exercice 3 : ajouter un test ou une variante pour l’objectif O3 et expliquer le résultat.
- Exercice 4 : ajouter un test ou une variante pour l’objectif O4 et expliquer le résultat.
- Exercice 5 : ajouter un test ou une variante pour l’objectif O1 et expliquer le résultat.
- Exercice 6 : ajouter un test ou une variante pour l’objectif O2 et expliquer le résultat.
- Exercice 7 : ajouter un test ou une variante pour l’objectif O3 et expliquer le résultat.
- Exercice 8 : ajouter un test ou une variante pour l’objectif O4 et expliquer le résultat.

## Corrigé
- Corrigé exercice 1 : le test vérifie isoler la fonction, écrire le contrat, tester cas nominal et cas limite et couvre EF1.
- Corrigé exercice 2 : le test vérifie isoler la fonction, écrire le contrat, tester cas nominal et cas limite et couvre EF2.
- Corrigé exercice 3 : le test vérifie isoler la fonction, écrire le contrat, tester cas nominal et cas limite et couvre EF3.
- Corrigé exercice 4 : le test vérifie isoler la fonction, écrire le contrat, tester cas nominal et cas limite et couvre EF4.
- Corrigé exercice 5 : le test vérifie isoler la fonction, écrire le contrat, tester cas nominal et cas limite et couvre EF1.
- Corrigé exercice 6 : le test vérifie isoler la fonction, écrire le contrat, tester cas nominal et cas limite et couvre EF2.
- Corrigé exercice 7 : le test vérifie isoler la fonction, écrire le contrat, tester cas nominal et cas limite et couvre EF3.
- Corrigé exercice 8 : le test vérifie isoler la fonction, écrire le contrat, tester cas nominal et cas limite et couvre EF4.

## Erreurs fréquentes
- Erreur fréquente EF1 - répondre seulement par `8 avec test nominal, test limite et test d’erreur` sans écrire la méthode.
- Erreur fréquente EF2 - appliquer isoler la fonction, écrire le contrat, tester cas nominal et cas limite dans le mauvais ordre.
- Erreur fréquente EF3 - oublier le cas limite : liste vide ou mutation inattendue.
- Erreur fréquente EF4 - citer une capacité officielle sans la relier à une production observable.

## Remédiation ciblée
- Activité corrective EF1 : reprendre l’exemple en imposant quatre colonnes, donnée, opération, résultat, contrôle.
- Activité corrective EF2 : refaire la méthode avec des étapes numérotées et une vérification à chaque étape.
- Activité corrective EF3 : construire deux variantes du cas limite `liste vide ou mutation inattendue` et comparer les sorties.
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

## Livrable vérifiable
- Le fichier starter s’exécute avec Python 3 sans dépendance externe.
- Les tests attendus peuvent être lancés directement par `python fichier_tests.py`.
- Le corrigé professeur reste séparé du document élève et n’est pas cité comme support élève.
