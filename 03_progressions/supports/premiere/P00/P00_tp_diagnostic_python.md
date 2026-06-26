---
title: "P00 - Tp - Diagnostic Python et carnet de bord"
level: "premiere"
sequence_id: "P00"
document_type: "tp"
status: "needs_review"
version: "0.3.0"
source: "BO 2019 ; ressource locale candidate : Documents_DRIVE/1_1ères NSI/1_Rentrée/2_Introduction_NSI.pdf"
theme: "Rentrée et méthode"
notion: "affectation, expression, trace, test"
objectifs:
  - "Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation."
  - "Objectif O2 - Appliquer une méthode explicite sur un exemple guidé."
  - "Objectif O3 - Justifier le résultat obtenu sur un cas nouveau."
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente."
private_data: false
official_program:
  capacities:
    - "P-HIST-01"
    - "P-LANG-01"
---


# P00 - Tp - Diagnostic Python et carnet de bord

## Objectifs spécifiques
- Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation.
- Objectif O2 - Appliquer une méthode explicite sur un exemple guidé.
- Objectif O3 - Justifier le résultat obtenu sur un cas nouveau.
- Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente.

## Capacités officielles atomiques
- P-HIST-01
- P-LANG-01

## Prérequis
- Lire une consigne technique sans confondre donnée, méthode et résultat.
- Écrire une réponse sous forme de phrases courtes et vérifiables.
- Utiliser Python en distinguant expression, valeur, variable et affichage.
- Conserver une trace de calcul ou de raisonnement exploitable pour la révision.

## Séance(s) correspondante(s)
- P00-S1 à P00-S4 : ce support est rattaché aux séances indiquées dans la progression.

## Situation-problème concrète
une classe de Première démarre avec des habitudes Python inégales et doit produire une trace vérifiable. La tâche consiste à traiter affectation, expression, trace, test sans réponse intuitive non vérifiée.

## Activité d’entrée
1. Lire la situation : une classe de Première démarre avec des habitudes Python inégales et doit produire une trace vérifiable.
2. Isoler la donnée de départ : variable x initialisée à 3 puis réaffectée.
3. Prédire individuellement le résultat de l’exemple `x = 3 ; x = x + 2 ; print(x)`.
4. Comparer deux stratégies et noter la divergence précise.
5. Appliquer la méthode retenue : suivre l’état de la variable après chaque affectation.
6. Contrôler avec le résultat de référence : 5.
7. Tester le cas limite suivant : réaffectation avec zéro ou valeur négative.
8. Rédiger une phrase qui relie donnée, méthode, résultat et contrôle.

## Consigne technique détaillée
- Mission : écrire un analyseur très simple de traces d’affectation.
- Starter code : `03_progressions/supports/premiere/P00/code/P00_starter_diagnostic_python.py`.
- Tests attendus : `03_progressions/supports/premiere/P00/code/P00_tests_attendus_diagnostic_python.py`.
- Corrigé professeur séparé : `03_progressions/supports/premiere/P00/code/P00_corrige_professeur_diagnostic_python.py`.
- Fonction principale à compléter ou contrôler : `predict_trace(steps)`.
- Exemple d’entrée : `[("x", 3), ("x", 5)]`.
- Exemple d’exécution : l’exemple de référence `x = 3 ; x = x + 2 ; print(x)` conduit à `5`.
- Cas limite : réaffectation avec zéro ou valeur négative.
- Livrable vérifiable : fichier Python exécutable et capture textuelle des tests attendus.

## Tests attendus
- Test 1 : cas nominal issu de l’exemple du cours.
- Test 2 : cas limite annoncé dans la trace.
- Test 3 : entrée invalide ou ambiguë, avec comportement documenté.
- Test 4 : non-régression sur une variante numérique ou structurelle.

## Exemple corrigé précis
- On appelle `predict_trace([("x", 3), ("x", 5)])`.
- La fonction doit appliquer suivre l’état de la variable après chaque affectation.
- Le résultat contrôlé est `5` ou une structure portant cette information.
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
- Corrigé exercice 1 : le test vérifie suivre l’état de la variable après chaque affectation et couvre EF1.
- Corrigé exercice 2 : le test vérifie suivre l’état de la variable après chaque affectation et couvre EF2.
- Corrigé exercice 3 : le test vérifie suivre l’état de la variable après chaque affectation et couvre EF3.
- Corrigé exercice 4 : le test vérifie suivre l’état de la variable après chaque affectation et couvre EF4.
- Corrigé exercice 5 : le test vérifie suivre l’état de la variable après chaque affectation et couvre EF1.
- Corrigé exercice 6 : le test vérifie suivre l’état de la variable après chaque affectation et couvre EF2.
- Corrigé exercice 7 : le test vérifie suivre l’état de la variable après chaque affectation et couvre EF3.
- Corrigé exercice 8 : le test vérifie suivre l’état de la variable après chaque affectation et couvre EF4.

## Erreurs fréquentes
- Erreur fréquente EF1 - répondre seulement par `5` sans écrire la méthode.
- Erreur fréquente EF2 - appliquer suivre l’état de la variable après chaque affectation dans le mauvais ordre.
- Erreur fréquente EF3 - oublier le cas limite : réaffectation avec zéro ou valeur négative.
- Erreur fréquente EF4 - citer une capacité officielle sans la relier à une production observable.

## Remédiation ciblée
- Activité corrective EF1 : reprendre l’exemple en imposant quatre colonnes, donnée, opération, résultat, contrôle.
- Activité corrective EF2 : refaire la méthode avec des étapes numérotées et une vérification à chaque étape.
- Activité corrective EF3 : construire deux variantes du cas limite `réaffectation avec zéro ou valeur négative` et comparer les sorties.
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
