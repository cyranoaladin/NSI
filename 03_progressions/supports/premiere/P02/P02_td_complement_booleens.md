---
title: "P02 - Td - Complément à deux et booléens"
level: "premiere"
sequence_id: "P02"
document_type: "td"
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


# P02 - Td - Complément à deux et booléens

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

## Exemple corrigé précis
- Exemple : `-23 sur 8 bits et (a and b) or (a and not b)`.
- Méthode : inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé.
- Résultat : 11101001 et simplification en a.
- Justification : chaque étape transforme une donnée identifiable.

## Exercices numérotés
### Exercice 1
- Objectif travaillé : O1.
- Capacité officielle : P-DATA-BASE-02A.
- Énoncé : résoudre une variante de `-23 sur 8 bits et (a and b) or (a and not b)` en changeant une donnée contrôlée.
- Travail demandé : appliquer inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé, puis rédiger le contrôle.
- Contrainte : citer le cas limite `140 impossible sur 8 bits signés` si la méthode peut échouer.
- Production attendue : réponse en trois lignes, méthode, résultat, vérification.
- Critère de réussite : aucun résultat n’est donné sans justification.

### Exercice 2
- Objectif travaillé : O2.
- Capacité officielle : P-DATA-BASE-02B.
- Énoncé : résoudre une variante de `-23 sur 8 bits et (a and b) or (a and not b)` en changeant une donnée contrôlée.
- Travail demandé : appliquer inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé, puis rédiger le contrôle.
- Contrainte : citer le cas limite `140 impossible sur 8 bits signés` si la méthode peut échouer.
- Production attendue : réponse en trois lignes, méthode, résultat, vérification.
- Critère de réussite : aucun résultat n’est donné sans justification.

### Exercice 3
- Objectif travaillé : O3.
- Capacité officielle : P-DATA-BASE-04.
- Énoncé : résoudre une variante de `-23 sur 8 bits et (a and b) or (a and not b)` en changeant une donnée contrôlée.
- Travail demandé : appliquer inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé, puis rédiger le contrôle.
- Contrainte : citer le cas limite `140 impossible sur 8 bits signés` si la méthode peut échouer.
- Production attendue : réponse en trois lignes, méthode, résultat, vérification.
- Critère de réussite : aucun résultat n’est donné sans justification.

### Exercice 4
- Objectif travaillé : O4.
- Capacité officielle : P-DATA-BASE-02A.
- Énoncé : résoudre une variante de `-23 sur 8 bits et (a and b) or (a and not b)` en changeant une donnée contrôlée.
- Travail demandé : appliquer inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé, puis rédiger le contrôle.
- Contrainte : citer le cas limite `140 impossible sur 8 bits signés` si la méthode peut échouer.
- Production attendue : réponse en trois lignes, méthode, résultat, vérification.
- Critère de réussite : aucun résultat n’est donné sans justification.

### Exercice 5
- Objectif travaillé : O1.
- Capacité officielle : P-DATA-BASE-02B.
- Énoncé : résoudre une variante de `-23 sur 8 bits et (a and b) or (a and not b)` en changeant une donnée contrôlée.
- Travail demandé : appliquer inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé, puis rédiger le contrôle.
- Contrainte : citer le cas limite `140 impossible sur 8 bits signés` si la méthode peut échouer.
- Production attendue : réponse en trois lignes, méthode, résultat, vérification.
- Critère de réussite : aucun résultat n’est donné sans justification.

### Exercice 6
- Objectif travaillé : O2.
- Capacité officielle : P-DATA-BASE-04.
- Énoncé : résoudre une variante de `-23 sur 8 bits et (a and b) or (a and not b)` en changeant une donnée contrôlée.
- Travail demandé : appliquer inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé, puis rédiger le contrôle.
- Contrainte : citer le cas limite `140 impossible sur 8 bits signés` si la méthode peut échouer.
- Production attendue : réponse en trois lignes, méthode, résultat, vérification.
- Critère de réussite : aucun résultat n’est donné sans justification.

### Exercice 7
- Objectif travaillé : O3.
- Capacité officielle : P-DATA-BASE-02A.
- Énoncé : résoudre une variante de `-23 sur 8 bits et (a and b) or (a and not b)` en changeant une donnée contrôlée.
- Travail demandé : appliquer inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé, puis rédiger le contrôle.
- Contrainte : citer le cas limite `140 impossible sur 8 bits signés` si la méthode peut échouer.
- Production attendue : réponse en trois lignes, méthode, résultat, vérification.
- Critère de réussite : aucun résultat n’est donné sans justification.

### Exercice 8
- Objectif travaillé : O4.
- Capacité officielle : P-DATA-BASE-02B.
- Énoncé : résoudre une variante de `-23 sur 8 bits et (a and b) or (a and not b)` en changeant une donnée contrôlée.
- Travail demandé : appliquer inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé, puis rédiger le contrôle.
- Contrainte : citer le cas limite `140 impossible sur 8 bits signés` si la méthode peut échouer.
- Production attendue : réponse en trois lignes, méthode, résultat, vérification.
- Critère de réussite : aucun résultat n’est donné sans justification.

## Corrigé
### Corrigé exercice 1
- On repère d’abord mot binaire de 8 bits et deux variables booléennes.
- On applique ensuite inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé.
- Le résultat attendu est `11101001 et simplification en a` pour l’exemple de référence ou une valeur cohérente pour la variante.
- L’erreur EF1 est évitée car la vérification est écrite.

### Corrigé exercice 2
- On repère d’abord mot binaire de 8 bits et deux variables booléennes.
- On applique ensuite inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé.
- Le résultat attendu est `11101001 et simplification en a` pour l’exemple de référence ou une valeur cohérente pour la variante.
- L’erreur EF2 est évitée car la vérification est écrite.

### Corrigé exercice 3
- On repère d’abord mot binaire de 8 bits et deux variables booléennes.
- On applique ensuite inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé.
- Le résultat attendu est `11101001 et simplification en a` pour l’exemple de référence ou une valeur cohérente pour la variante.
- L’erreur EF3 est évitée car la vérification est écrite.

### Corrigé exercice 4
- On repère d’abord mot binaire de 8 bits et deux variables booléennes.
- On applique ensuite inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé.
- Le résultat attendu est `11101001 et simplification en a` pour l’exemple de référence ou une valeur cohérente pour la variante.
- L’erreur EF4 est évitée car la vérification est écrite.

### Corrigé exercice 5
- On repère d’abord mot binaire de 8 bits et deux variables booléennes.
- On applique ensuite inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé.
- Le résultat attendu est `11101001 et simplification en a` pour l’exemple de référence ou une valeur cohérente pour la variante.
- L’erreur EF1 est évitée car la vérification est écrite.

### Corrigé exercice 6
- On repère d’abord mot binaire de 8 bits et deux variables booléennes.
- On applique ensuite inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé.
- Le résultat attendu est `11101001 et simplification en a` pour l’exemple de référence ou une valeur cohérente pour la variante.
- L’erreur EF2 est évitée car la vérification est écrite.

### Corrigé exercice 7
- On repère d’abord mot binaire de 8 bits et deux variables booléennes.
- On applique ensuite inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé.
- Le résultat attendu est `11101001 et simplification en a` pour l’exemple de référence ou une valeur cohérente pour la variante.
- L’erreur EF3 est évitée car la vérification est écrite.

### Corrigé exercice 8
- On repère d’abord mot binaire de 8 bits et deux variables booléennes.
- On applique ensuite inverser les bits, ajouter 1, puis vérifier les bornes de l’intervalle signé.
- Le résultat attendu est `11101001 et simplification en a` pour l’exemple de référence ou une valeur cohérente pour la variante.
- L’erreur EF4 est évitée car la vérification est écrite.

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

