---
title: "P04 - Tp - Types construits Python"
level: "premiere"
sequence_id: "P04"
document_type: "tp"
status: "needs_review"
version: "0.3.0"
source: "BO 2019 ; ressource locale candidate : Documents_DRIVE/9_NSI_2025-2026/1ère/Séq2_Types construits _partie1/Cours_Tuples_Listes_Elève.pdf"
theme: "Tuples, listes, dictionnaires"
notion: "tuple, liste, dictionnaire, parcours"
objectifs:
  - "Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation."
  - "Objectif O2 - Appliquer une méthode explicite sur un exemple guidé."
  - "Objectif O3 - Justifier le résultat obtenu sur un cas nouveau."
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente."
private_data: false
official_program:
  capacities:
    - "P-DATA-CONSTR-01"
    - "P-DATA-CONSTR-02A"
    - "P-DATA-CONSTR-02B"
    - "P-DATA-CONSTR-02C"
    - "P-DATA-CONSTR-02D"
    - "P-DATA-CONSTR-03A"
    - "P-DATA-CONSTR-03B"
    - "P-DATA-CONSTR-03C"
---


# P04 - Tp - Types construits Python

## Objectifs spécifiques
- Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation.
- Objectif O2 - Appliquer une méthode explicite sur un exemple guidé.
- Objectif O3 - Justifier le résultat obtenu sur un cas nouveau.
- Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente.

## Capacités officielles atomiques
- P-DATA-CONSTR-01
- P-DATA-CONSTR-02A
- P-DATA-CONSTR-02B
- P-DATA-CONSTR-02C
- P-DATA-CONSTR-02D
- P-DATA-CONSTR-03A
- P-DATA-CONSTR-03B
- P-DATA-CONSTR-03C

## Prérequis
- Lire une consigne technique sans confondre donnée, méthode et résultat.
- Écrire une réponse sous forme de phrases courtes et vérifiables.
- Utiliser Python en distinguant expression, valeur, variable et affichage.
- Conserver une trace de calcul ou de raisonnement exploitable pour la révision.

## Séance(s) correspondante(s)
- P04-S1 à P04-S7 : ce support est rattaché aux séances indiquées dans la progression.

## Situation-problème concrète
un relevé météo mélange coordonnées fixes, mesures modifiables et accès par nom de station. La tâche consiste à traiter tuple, liste, dictionnaire, parcours sans réponse intuitive non vérifiée.

## Activité d’entrée
1. Lire la situation : un relevé météo mélange coordonnées fixes, mesures modifiables et accès par nom de station.
2. Isoler la donnée de départ : collection ordonnée ou associée à des clés.
3. Prédire individuellement le résultat de l’exemple `coord=(43.6,1.4), mesures=[12,14,13], station={"nom":"A","temp":14}`.
4. Comparer deux stratégies et noter la divergence précise.
5. Appliquer la méthode retenue : choisir le conteneur selon mutabilité, ordre et accès attendu.
6. Contrôler avec le résultat de référence : tuple non modifié, liste mise à jour, dictionnaire consulté par clé.
7. Tester le cas limite suivant : copie de liste et clé absente.
8. Rédiger une phrase qui relie donnée, méthode, résultat et contrôle.

## Consigne technique détaillée
- Mission : manipuler des relevés météo dans listes et dictionnaires avec contrôles.
- Starter code : `03_progressions/supports/premiere/P04/code/P04_starter_types_construits.py`.
- Tests attendus : `03_progressions/supports/premiere/P04/code/P04_tests_attendus_types_construits.py`.
- Corrigé professeur séparé : `03_progressions/supports/premiere/P04/code/P04_corrige_professeur_types_construits.py`.
- Fonction principale à compléter ou contrôler : `resume_mesures(mesures)`.
- Exemple d’entrée : `[12, 14, 13]`.
- Exemple d’exécution : l’exemple de référence `coord=(43.6,1.4), mesures=[12,14,13], station={"nom":"A","temp":14}` conduit à `tuple non modifié, liste mise à jour, dictionnaire consulté par clé`.
- Cas limite : copie de liste et clé absente.
- Livrable vérifiable : fichier Python exécutable et capture textuelle des tests attendus.

## Tests attendus
- Test 1 : cas nominal issu de l’exemple du cours.
- Test 2 : cas limite annoncé dans la trace.
- Test 3 : entrée invalide ou ambiguë, avec comportement documenté.
- Test 4 : non-régression sur une variante numérique ou structurelle.

## Exemple corrigé précis
- On appelle `resume_mesures([12, 14, 13])`.
- La fonction doit appliquer choisir le conteneur selon mutabilité, ordre et accès attendu.
- Le résultat contrôlé est `tuple non modifié, liste mise à jour, dictionnaire consulté par clé` ou une structure portant cette information.
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
- Corrigé exercice 1 : le test vérifie choisir le conteneur selon mutabilité, ordre et accès attendu et couvre EF1.
- Corrigé exercice 2 : le test vérifie choisir le conteneur selon mutabilité, ordre et accès attendu et couvre EF2.
- Corrigé exercice 3 : le test vérifie choisir le conteneur selon mutabilité, ordre et accès attendu et couvre EF3.
- Corrigé exercice 4 : le test vérifie choisir le conteneur selon mutabilité, ordre et accès attendu et couvre EF4.
- Corrigé exercice 5 : le test vérifie choisir le conteneur selon mutabilité, ordre et accès attendu et couvre EF1.
- Corrigé exercice 6 : le test vérifie choisir le conteneur selon mutabilité, ordre et accès attendu et couvre EF2.
- Corrigé exercice 7 : le test vérifie choisir le conteneur selon mutabilité, ordre et accès attendu et couvre EF3.
- Corrigé exercice 8 : le test vérifie choisir le conteneur selon mutabilité, ordre et accès attendu et couvre EF4.

## Erreurs fréquentes
- Erreur fréquente EF1 - répondre seulement par `tuple non modifié, liste mise à jour, dictionnaire consulté par clé` sans écrire la méthode.
- Erreur fréquente EF2 - appliquer choisir le conteneur selon mutabilité, ordre et accès attendu dans le mauvais ordre.
- Erreur fréquente EF3 - oublier le cas limite : copie de liste et clé absente.
- Erreur fréquente EF4 - citer une capacité officielle sans la relier à une production observable.

## Remédiation ciblée
- Activité corrective EF1 : reprendre l’exemple en imposant quatre colonnes, donnée, opération, résultat, contrôle.
- Activité corrective EF2 : refaire la méthode avec des étapes numérotées et une vérification à chaque étape.
- Activité corrective EF3 : construire deux variantes du cas limite `copie de liste et clé absente` et comparer les sorties.
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
