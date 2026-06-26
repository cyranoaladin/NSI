---
title: "P02 - Cours - Complément à deux et booléens"
level: "premiere"
sequence_id: "P02"
document_type: "cours"
status: "needs_review"
version: "0.3.0"
source: "BO 2019 ; ressource locale candidate : Documents_DRIVE/2_NSI/Programmes et textes officiels/0_Programmes.pdf"
theme: "Représentation machine"
notion: "entiers signés, débordement, expressions booléennes"
objectifs:
  - "Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation."
  - "Objectif O2 - Appliquer une méthode explicite sur un exemple guidé."
  - "Objectif O3 - Justifier le résultat obtenu sur un cas nouveau."
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente."
private_data: false
official_program:
  capacities:
    - "P-DATA-BASE-02A"
    - "P-DATA-BASE-02B"
    - "P-DATA-BASE-04"
---


# P02 - Cours - Complément à deux et booléens

## Objectifs spécifiques
- Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation.
- Objectif O2 - Appliquer une méthode explicite sur un exemple guidé.
- Objectif O3 - Justifier le résultat obtenu sur un cas nouveau.
- Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente.

## Capacités officielles atomiques
- P-DATA-BASE-02A
- P-DATA-BASE-02B
- P-DATA-BASE-04

## Prérequis
- Lire une consigne technique sans confondre donnée, méthode et résultat.
- Écrire une réponse sous forme de phrases courtes et vérifiables.
- Utiliser Python en distinguant expression, valeur, variable et affichage.
- Conserver une trace de calcul ou de raisonnement exploitable pour la révision.

## Séance(s) correspondante(s)
- P02-S1 à P02-S5 : ce support est rattaché aux séances indiquées dans la progression.

## Situation-problème concrète
un capteur renvoie un octet qui peut représenter une température négative ou un indicateur booléen. La tâche consiste à traiter entiers signés, débordement, expressions booléennes sans réponse intuitive non vérifiée.

## Activité d’entrée
1. Lire la situation : un capteur renvoie un octet qui peut représenter une température négative ou un indicateur booléen.
2. Isoler la donnée de départ : mot binaire de 8 bits et deux variables booléennes.
3. Prédire individuellement le résultat de l’exemple `-23 sur 8 bits et (a and b) or (a and not b)`.
4. Comparer deux stratégies et noter la divergence précise.
5. Appliquer la méthode retenue : inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé.
6. Contrôler avec le résultat de référence : 11101001 et simplification en a.
7. Tester le cas limite suivant : 140 impossible sur 8 bits signés.
8. Rédiger une phrase qui relie donnée, méthode, résultat et contrôle.

## Définitions et formalisation
- Définition D1 : la notion centrale est entiers signés, débordement, expressions booléennes.
- Définition D2 : une donnée est une information manipulée avant transformation.
- Définition D3 : une représentation est une convention permettant d’agir sur cette donnée.
- Définition D4 : une preuve courte explique pourquoi la méthode aboutit au résultat.
- Définition D5 : un cas limite est un exemple volontairement petit, extrême ou ambigu.
- Exemple de référence : `-23 sur 8 bits et (a and b) or (a and not b)`.
- Résultat de référence : 11101001 et simplification en a.
- Méthode de référence : inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé.
- Cas limite à surveiller : 140 impossible sur 8 bits signés.

## Objectif O1 - Appropriation guidée
- Capacité officielle travaillée : P-DATA-BASE-02A.
- Question directrice : comment traiter entiers signés, débordement, expressions booléennes dans une situation vérifiable ?
- Donnée étudiée : mot binaire de 8 bits et deux variables booléennes.
- Étape 1 : reformuler la consigne avec les mots de la capacité P-DATA-BASE-02A.
- Étape 2 : appliquer la méthode `inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé` sans sauter d’étape.
- Étape 3 : obtenir le résultat contrôlé `11101001 et simplification en a` ou expliquer l’écart.
- Étape 4 : tester le cas limite `140 impossible sur 8 bits signés`.
- Étape 5 : écrire une justification de deux phrases.
- Exemple corrigé 1 : sur `-23 sur 8 bits et (a and b) or (a and not b)`, on obtient `11101001 et simplification en a` car inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé.
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
- Capacité officielle travaillée : P-DATA-BASE-02B.
- Question directrice : comment traiter entiers signés, débordement, expressions booléennes dans une situation vérifiable ?
- Donnée étudiée : mot binaire de 8 bits et deux variables booléennes.
- Étape 1 : reformuler la consigne avec les mots de la capacité P-DATA-BASE-02B.
- Étape 2 : appliquer la méthode `inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé` sans sauter d’étape.
- Étape 3 : obtenir le résultat contrôlé `11101001 et simplification en a` ou expliquer l’écart.
- Étape 4 : tester le cas limite `140 impossible sur 8 bits signés`.
- Étape 5 : écrire une justification de deux phrases.
- Exemple corrigé 2 : sur `-23 sur 8 bits et (a and b) or (a and not b)`, on obtient `11101001 et simplification en a` car inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé.
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
- Capacité officielle travaillée : P-DATA-BASE-04.
- Question directrice : comment traiter entiers signés, débordement, expressions booléennes dans une situation vérifiable ?
- Donnée étudiée : mot binaire de 8 bits et deux variables booléennes.
- Étape 1 : reformuler la consigne avec les mots de la capacité P-DATA-BASE-04.
- Étape 2 : appliquer la méthode `inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé` sans sauter d’étape.
- Étape 3 : obtenir le résultat contrôlé `11101001 et simplification en a` ou expliquer l’écart.
- Étape 4 : tester le cas limite `140 impossible sur 8 bits signés`.
- Étape 5 : écrire une justification de deux phrases.
- Exemple corrigé 3 : sur `-23 sur 8 bits et (a and b) or (a and not b)`, on obtient `11101001 et simplification en a` car inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé.
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
- Capacité officielle travaillée : P-DATA-BASE-02A.
- Question directrice : comment traiter entiers signés, débordement, expressions booléennes dans une situation vérifiable ?
- Donnée étudiée : mot binaire de 8 bits et deux variables booléennes.
- Étape 1 : reformuler la consigne avec les mots de la capacité P-DATA-BASE-02A.
- Étape 2 : appliquer la méthode `inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé` sans sauter d’étape.
- Étape 3 : obtenir le résultat contrôlé `11101001 et simplification en a` ou expliquer l’écart.
- Étape 4 : tester le cas limite `140 impossible sur 8 bits signés`.
- Étape 5 : écrire une justification de deux phrases.
- Exemple corrigé 4 : sur `-23 sur 8 bits et (a and b) or (a and not b)`, on obtient `11101001 et simplification en a` car inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé.
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
- Exercice 1 : traiter entiers signés, débordement, expressions booléennes pour l’objectif O1 et la capacité P-DATA-BASE-02A, puis écrire un contrôle explicite.
- Exercice 2 : traiter entiers signés, débordement, expressions booléennes pour l’objectif O2 et la capacité P-DATA-BASE-02B, puis écrire un contrôle explicite.
- Exercice 3 : traiter entiers signés, débordement, expressions booléennes pour l’objectif O3 et la capacité P-DATA-BASE-04, puis écrire un contrôle explicite.
- Exercice 4 : traiter entiers signés, débordement, expressions booléennes pour l’objectif O4 et la capacité P-DATA-BASE-02A, puis écrire un contrôle explicite.
- Exercice 5 : traiter entiers signés, débordement, expressions booléennes pour l’objectif O1 et la capacité P-DATA-BASE-02B, puis écrire un contrôle explicite.
- Exercice 6 : traiter entiers signés, débordement, expressions booléennes pour l’objectif O2 et la capacité P-DATA-BASE-04, puis écrire un contrôle explicite.
- Exercice 7 : traiter entiers signés, débordement, expressions booléennes pour l’objectif O3 et la capacité P-DATA-BASE-02A, puis écrire un contrôle explicite.
- Exercice 8 : traiter entiers signés, débordement, expressions booléennes pour l’objectif O4 et la capacité P-DATA-BASE-02B, puis écrire un contrôle explicite.

## Corrigés complets des exercices du cours
- Corrigé exercice 1 : identifier mot binaire de 8 bits et deux variables booléennes, appliquer inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé, annoncer 11101001 et simplification en a, puis vérifier EF1.
- Corrigé exercice 2 : identifier mot binaire de 8 bits et deux variables booléennes, appliquer inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé, annoncer 11101001 et simplification en a, puis vérifier EF2.
- Corrigé exercice 3 : identifier mot binaire de 8 bits et deux variables booléennes, appliquer inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé, annoncer 11101001 et simplification en a, puis vérifier EF3.
- Corrigé exercice 4 : identifier mot binaire de 8 bits et deux variables booléennes, appliquer inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé, annoncer 11101001 et simplification en a, puis vérifier EF4.
- Corrigé exercice 5 : identifier mot binaire de 8 bits et deux variables booléennes, appliquer inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé, annoncer 11101001 et simplification en a, puis vérifier EF1.
- Corrigé exercice 6 : identifier mot binaire de 8 bits et deux variables booléennes, appliquer inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé, annoncer 11101001 et simplification en a, puis vérifier EF2.
- Corrigé exercice 7 : identifier mot binaire de 8 bits et deux variables booléennes, appliquer inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé, annoncer 11101001 et simplification en a, puis vérifier EF3.
- Corrigé exercice 8 : identifier mot binaire de 8 bits et deux variables booléennes, appliquer inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé, annoncer 11101001 et simplification en a, puis vérifier EF4.

## Erreurs fréquentes
- Erreur fréquente EF1 - répondre seulement par `11101001 et simplification en a` sans écrire la méthode.
- Erreur fréquente EF2 - appliquer inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé dans le mauvais ordre.
- Erreur fréquente EF3 - oublier le cas limite : 140 impossible sur 8 bits signés.
- Erreur fréquente EF4 - citer une capacité officielle sans la relier à une production observable.

## Remédiation ciblée
- Activité corrective EF1 : reprendre l’exemple en imposant quatre colonnes, donnée, opération, résultat, contrôle.
- Activité corrective EF2 : refaire la méthode avec des étapes numérotées et une vérification à chaque étape.
- Activité corrective EF3 : construire deux variantes du cas limite `140 impossible sur 8 bits signés` et comparer les sorties.
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
