---
title: "P03 - Cours - Texte Unicode et nombres réels"
level: "premiere"
sequence_id: "P03"
document_type: "cours"
status: "needs_review"
version: "0.3.0"
source: "BO 2019 ; ressource locale candidate : Documents_DRIVE/2_NSI/Programmes et textes officiels/0_Programmes.pdf"
theme: "Données textuelles et approximation"
notion: "Unicode, UTF-8, flottants"
objectifs:
  - "Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation."
  - "Objectif O2 - Appliquer une méthode explicite sur un exemple guidé."
  - "Objectif O3 - Justifier le résultat obtenu sur un cas nouveau."
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente."
private_data: false
official_program:
  capacities:
    - "P-DATA-BASE-05A"
    - "P-DATA-BASE-05B"
    - "P-DATA-BASE-03"
---


# P03 - Cours - Texte Unicode et nombres réels

## Objectifs spécifiques
- Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation.
- Objectif O2 - Appliquer une méthode explicite sur un exemple guidé.
- Objectif O3 - Justifier le résultat obtenu sur un cas nouveau.
- Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente.

## Capacités officielles atomiques
- P-DATA-BASE-05A
- P-DATA-BASE-05B
- P-DATA-BASE-03

## Prérequis
- Lire une consigne technique sans confondre donnée, méthode et résultat.
- Écrire une réponse sous forme de phrases courtes et vérifiables.
- Utiliser Python en distinguant expression, valeur, variable et affichage.
- Conserver une trace de calcul ou de raisonnement exploitable pour la révision.

## Séance(s) correspondante(s)
- P03-S1 à P03-S5 : ce support est rattaché aux séances indiquées dans la progression.

## Situation-problème concrète
un formulaire accepte des accents mais un export binaire doit compter caractères, octets et valeurs approchées. La tâche consiste à traiter Unicode, UTF-8, flottants sans réponse intuitive non vérifiée.

## Activité d’entrée
1. Lire la situation : un formulaire accepte des accents mais un export binaire doit compter caractères, octets et valeurs approchées.
2. Isoler la donnée de départ : chaîne Unicode et calcul décimal représenté en binaire.
3. Prédire individuellement le résultat de l’exemple `Aé et 0.1 + 0.2`.
4. Comparer deux stratégies et noter la divergence précise.
5. Appliquer la méthode retenue : distinguer point de code, encodage, octets et approximation machine.
6. Contrôler avec le résultat de référence : 2 caractères, 3 octets, somme flottante non exactement égale à 0.3.
7. Tester le cas limite suivant : caractère hors ASCII ou comparaison directe de flottants.
8. Rédiger une phrase qui relie donnée, méthode, résultat et contrôle.

## Définitions et formalisation
- Définition D1 : la notion centrale est Unicode, UTF-8, flottants.
- Définition D2 : une donnée est une information manipulée avant transformation.
- Définition D3 : une représentation est une convention permettant d’agir sur cette donnée.
- Définition D4 : une preuve courte explique pourquoi la méthode aboutit au résultat.
- Définition D5 : un cas limite est un exemple volontairement petit, extrême ou ambigu.
- Exemple de référence : `Aé et 0.1 + 0.2`.
- Résultat de référence : 2 caractères, 3 octets, somme flottante non exactement égale à 0.3.
- Méthode de référence : distinguer point de code, encodage, octets et approximation machine.
- Cas limite à surveiller : caractère hors ASCII ou comparaison directe de flottants.

## Objectif O1 - Appropriation guidée
- Capacité officielle travaillée : P-DATA-BASE-05A.
- Question directrice : comment traiter Unicode, UTF-8, flottants dans une situation vérifiable ?
- Donnée étudiée : chaîne Unicode et calcul décimal représenté en binaire.
- Étape 1 : reformuler la consigne avec les mots de la capacité P-DATA-BASE-05A.
- Étape 2 : appliquer la méthode `distinguer point de code, encodage, octets et approximation machine` sans sauter d’étape.
- Étape 3 : obtenir le résultat contrôlé `2 caractères, 3 octets, somme flottante non exactement égale à 0.3` ou expliquer l’écart.
- Étape 4 : tester le cas limite `caractère hors ASCII ou comparaison directe de flottants`.
- Étape 5 : écrire une justification de deux phrases.
- Exemple corrigé 1 : sur `Aé et 0.1 + 0.2`, on obtient `2 caractères, 3 octets, somme flottante non exactement égale à 0.3` car distinguer point de code, encodage, octets et approximation machine.
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
- Capacité officielle travaillée : P-DATA-BASE-05B.
- Question directrice : comment traiter Unicode, UTF-8, flottants dans une situation vérifiable ?
- Donnée étudiée : chaîne Unicode et calcul décimal représenté en binaire.
- Étape 1 : reformuler la consigne avec les mots de la capacité P-DATA-BASE-05B.
- Étape 2 : appliquer la méthode `distinguer point de code, encodage, octets et approximation machine` sans sauter d’étape.
- Étape 3 : obtenir le résultat contrôlé `2 caractères, 3 octets, somme flottante non exactement égale à 0.3` ou expliquer l’écart.
- Étape 4 : tester le cas limite `caractère hors ASCII ou comparaison directe de flottants`.
- Étape 5 : écrire une justification de deux phrases.
- Exemple corrigé 2 : sur `Aé et 0.1 + 0.2`, on obtient `2 caractères, 3 octets, somme flottante non exactement égale à 0.3` car distinguer point de code, encodage, octets et approximation machine.
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
- Capacité officielle travaillée : P-DATA-BASE-03.
- Question directrice : comment traiter Unicode, UTF-8, flottants dans une situation vérifiable ?
- Donnée étudiée : chaîne Unicode et calcul décimal représenté en binaire.
- Étape 1 : reformuler la consigne avec les mots de la capacité P-DATA-BASE-03.
- Étape 2 : appliquer la méthode `distinguer point de code, encodage, octets et approximation machine` sans sauter d’étape.
- Étape 3 : obtenir le résultat contrôlé `2 caractères, 3 octets, somme flottante non exactement égale à 0.3` ou expliquer l’écart.
- Étape 4 : tester le cas limite `caractère hors ASCII ou comparaison directe de flottants`.
- Étape 5 : écrire une justification de deux phrases.
- Exemple corrigé 3 : sur `Aé et 0.1 + 0.2`, on obtient `2 caractères, 3 octets, somme flottante non exactement égale à 0.3` car distinguer point de code, encodage, octets et approximation machine.
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
- Capacité officielle travaillée : P-DATA-BASE-05A.
- Question directrice : comment traiter Unicode, UTF-8, flottants dans une situation vérifiable ?
- Donnée étudiée : chaîne Unicode et calcul décimal représenté en binaire.
- Étape 1 : reformuler la consigne avec les mots de la capacité P-DATA-BASE-05A.
- Étape 2 : appliquer la méthode `distinguer point de code, encodage, octets et approximation machine` sans sauter d’étape.
- Étape 3 : obtenir le résultat contrôlé `2 caractères, 3 octets, somme flottante non exactement égale à 0.3` ou expliquer l’écart.
- Étape 4 : tester le cas limite `caractère hors ASCII ou comparaison directe de flottants`.
- Étape 5 : écrire une justification de deux phrases.
- Exemple corrigé 4 : sur `Aé et 0.1 + 0.2`, on obtient `2 caractères, 3 octets, somme flottante non exactement égale à 0.3` car distinguer point de code, encodage, octets et approximation machine.
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
- Exercice 1 : traiter Unicode, UTF-8, flottants pour l’objectif O1 et la capacité P-DATA-BASE-05A, puis écrire un contrôle explicite.
- Exercice 2 : traiter Unicode, UTF-8, flottants pour l’objectif O2 et la capacité P-DATA-BASE-05B, puis écrire un contrôle explicite.
- Exercice 3 : traiter Unicode, UTF-8, flottants pour l’objectif O3 et la capacité P-DATA-BASE-03, puis écrire un contrôle explicite.
- Exercice 4 : traiter Unicode, UTF-8, flottants pour l’objectif O4 et la capacité P-DATA-BASE-05A, puis écrire un contrôle explicite.
- Exercice 5 : traiter Unicode, UTF-8, flottants pour l’objectif O1 et la capacité P-DATA-BASE-05B, puis écrire un contrôle explicite.
- Exercice 6 : traiter Unicode, UTF-8, flottants pour l’objectif O2 et la capacité P-DATA-BASE-03, puis écrire un contrôle explicite.
- Exercice 7 : traiter Unicode, UTF-8, flottants pour l’objectif O3 et la capacité P-DATA-BASE-05A, puis écrire un contrôle explicite.
- Exercice 8 : traiter Unicode, UTF-8, flottants pour l’objectif O4 et la capacité P-DATA-BASE-05B, puis écrire un contrôle explicite.

## Corrigés complets des exercices du cours
- Corrigé exercice 1 : identifier chaîne Unicode et calcul décimal représenté en binaire, appliquer distinguer point de code, encodage, octets et approximation machine, annoncer 2 caractères, 3 octets, somme flottante non exactement égale à 0.3, puis vérifier EF1.
- Corrigé exercice 2 : identifier chaîne Unicode et calcul décimal représenté en binaire, appliquer distinguer point de code, encodage, octets et approximation machine, annoncer 2 caractères, 3 octets, somme flottante non exactement égale à 0.3, puis vérifier EF2.
- Corrigé exercice 3 : identifier chaîne Unicode et calcul décimal représenté en binaire, appliquer distinguer point de code, encodage, octets et approximation machine, annoncer 2 caractères, 3 octets, somme flottante non exactement égale à 0.3, puis vérifier EF3.
- Corrigé exercice 4 : identifier chaîne Unicode et calcul décimal représenté en binaire, appliquer distinguer point de code, encodage, octets et approximation machine, annoncer 2 caractères, 3 octets, somme flottante non exactement égale à 0.3, puis vérifier EF4.
- Corrigé exercice 5 : identifier chaîne Unicode et calcul décimal représenté en binaire, appliquer distinguer point de code, encodage, octets et approximation machine, annoncer 2 caractères, 3 octets, somme flottante non exactement égale à 0.3, puis vérifier EF1.
- Corrigé exercice 6 : identifier chaîne Unicode et calcul décimal représenté en binaire, appliquer distinguer point de code, encodage, octets et approximation machine, annoncer 2 caractères, 3 octets, somme flottante non exactement égale à 0.3, puis vérifier EF2.
- Corrigé exercice 7 : identifier chaîne Unicode et calcul décimal représenté en binaire, appliquer distinguer point de code, encodage, octets et approximation machine, annoncer 2 caractères, 3 octets, somme flottante non exactement égale à 0.3, puis vérifier EF3.
- Corrigé exercice 8 : identifier chaîne Unicode et calcul décimal représenté en binaire, appliquer distinguer point de code, encodage, octets et approximation machine, annoncer 2 caractères, 3 octets, somme flottante non exactement égale à 0.3, puis vérifier EF4.

## Erreurs fréquentes
- Erreur fréquente EF1 - répondre seulement par `2 caractères, 3 octets, somme flottante non exactement égale à 0.3` sans écrire la méthode.
- Erreur fréquente EF2 - appliquer distinguer point de code, encodage, octets et approximation machine dans le mauvais ordre.
- Erreur fréquente EF3 - oublier le cas limite : caractère hors ASCII ou comparaison directe de flottants.
- Erreur fréquente EF4 - citer une capacité officielle sans la relier à une production observable.

## Remédiation ciblée
- Activité corrective EF1 : reprendre l’exemple en imposant quatre colonnes, donnée, opération, résultat, contrôle.
- Activité corrective EF2 : refaire la méthode avec des étapes numérotées et une vérification à chaque étape.
- Activité corrective EF3 : construire deux variantes du cas limite `caractère hors ASCII ou comparaison directe de flottants` et comparer les sorties.
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
