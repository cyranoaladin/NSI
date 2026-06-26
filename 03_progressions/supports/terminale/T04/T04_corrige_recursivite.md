---
title: "T04 - Corrige - Récursivité contrôlée"
level: "terminale"
sequence_id: "T04"
document_type: "corrige"
status: "needs_review"
version: "0.3.0"
source: "BO 2019 ; ressource locale candidate : Documents_DRIVE/2_NSI/Formation TOULOUSE/BLOC5/PolyBloc5.pdf"
theme: "Langage et preuve"
notion: "cas de base, appel récursif, terminaison"
objectifs:
  - "Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation."
  - "Objectif O2 - Appliquer une méthode explicite sur un exemple guidé."
  - "Objectif O3 - Justifier le résultat obtenu sur un cas nouveau."
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente."
private_data: false
official_program:
  capacities:
    - "T-LANG-02A"
    - "T-LANG-02B"
---


# T04 - Corrige - Récursivité contrôlée

## Objectifs spécifiques
- Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation.
- Objectif O2 - Appliquer une méthode explicite sur un exemple guidé.
- Objectif O3 - Justifier le résultat obtenu sur un cas nouveau.
- Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente.

## Capacités officielles atomiques
- T-LANG-02A
- T-LANG-02B

## Prérequis
- Lire une consigne technique sans confondre donnée, méthode et résultat.
- Écrire une réponse sous forme de phrases courtes et vérifiables.
- Utiliser Python en distinguant expression, valeur, variable et affichage.
- Conserver une trace de calcul ou de raisonnement exploitable pour la révision.

## Séance(s) correspondante(s)
- T04-S1 à T04-S5 : ce support est rattaché aux séances indiquées dans la progression.

## Situation-problème concrète
un calcul naturel se définit par réduction du problème mais risque de ne jamais s’arrêter. La tâche consiste à traiter cas de base, appel récursif, terminaison sans réponse intuitive non vérifiée.

## Activité d’entrée
1. Lire la situation : un calcul naturel se définit par réduction du problème mais risque de ne jamais s’arrêter.
2. Isoler la donnée de départ : entier naturel réduit à chaque appel.
3. Prédire individuellement le résultat de l’exemple `factorielle(5)`.
4. Comparer deux stratégies et noter la divergence précise.
5. Appliquer la méthode retenue : identifier cas de base, relation de récurrence et variant décroissant.
6. Contrôler avec le résultat de référence : 120 avec cas de base factorielle(0)=1.
7. Tester le cas limite suivant : appel récursif sans diminution ou profondeur excessive.
8. Rédiger une phrase qui relie donnée, méthode, résultat et contrôle.

## Exemple corrigé précis
- Exemple : `factorielle(5)`.
- Correction : identifier cas de base, relation de récurrence et variant décroissant.
- Résultat : 120 avec cas de base factorielle(0)=1.
- Justification : le raisonnement est lisible et relié à une capacité officielle.

## Exercices numérotés
- Les exercices 1 à 8 du TD sont repris ci-dessous pour rendre la correspondance vérifiable.

### Corrigé exercice 1
- Objectif : O1.
- Capacité : T-LANG-02A.
- Donnée traitée : entier naturel réduit à chaque appel.
- Méthode correcte : identifier cas de base, relation de récurrence et variant décroissant.
- Résultat de référence : `120 avec cas de base factorielle(0)=1`.
- Contrôle : comparer la sortie à la représentation attendue et expliquer l’écart éventuel.
- Erreur fréquente évitée : EF1.
- Remédiation : Activité corrective EF1 si la méthode n’est pas justifiée.

### Corrigé exercice 2
- Objectif : O2.
- Capacité : T-LANG-02B.
- Donnée traitée : entier naturel réduit à chaque appel.
- Méthode correcte : identifier cas de base, relation de récurrence et variant décroissant.
- Résultat de référence : `120 avec cas de base factorielle(0)=1`.
- Contrôle : comparer la sortie à la représentation attendue et expliquer l’écart éventuel.
- Erreur fréquente évitée : EF2.
- Remédiation : Activité corrective EF2 si la méthode n’est pas justifiée.

### Corrigé exercice 3
- Objectif : O3.
- Capacité : T-LANG-02A.
- Donnée traitée : entier naturel réduit à chaque appel.
- Méthode correcte : identifier cas de base, relation de récurrence et variant décroissant.
- Résultat de référence : `120 avec cas de base factorielle(0)=1`.
- Contrôle : comparer la sortie à la représentation attendue et expliquer l’écart éventuel.
- Erreur fréquente évitée : EF3.
- Remédiation : Activité corrective EF3 si la méthode n’est pas justifiée.

### Corrigé exercice 4
- Objectif : O4.
- Capacité : T-LANG-02B.
- Donnée traitée : entier naturel réduit à chaque appel.
- Méthode correcte : identifier cas de base, relation de récurrence et variant décroissant.
- Résultat de référence : `120 avec cas de base factorielle(0)=1`.
- Contrôle : comparer la sortie à la représentation attendue et expliquer l’écart éventuel.
- Erreur fréquente évitée : EF4.
- Remédiation : Activité corrective EF4 si la méthode n’est pas justifiée.

### Corrigé exercice 5
- Objectif : O1.
- Capacité : T-LANG-02A.
- Donnée traitée : entier naturel réduit à chaque appel.
- Méthode correcte : identifier cas de base, relation de récurrence et variant décroissant.
- Résultat de référence : `120 avec cas de base factorielle(0)=1`.
- Contrôle : comparer la sortie à la représentation attendue et expliquer l’écart éventuel.
- Erreur fréquente évitée : EF1.
- Remédiation : Activité corrective EF1 si la méthode n’est pas justifiée.

### Corrigé exercice 6
- Objectif : O2.
- Capacité : T-LANG-02B.
- Donnée traitée : entier naturel réduit à chaque appel.
- Méthode correcte : identifier cas de base, relation de récurrence et variant décroissant.
- Résultat de référence : `120 avec cas de base factorielle(0)=1`.
- Contrôle : comparer la sortie à la représentation attendue et expliquer l’écart éventuel.
- Erreur fréquente évitée : EF2.
- Remédiation : Activité corrective EF2 si la méthode n’est pas justifiée.

### Corrigé exercice 7
- Objectif : O3.
- Capacité : T-LANG-02A.
- Donnée traitée : entier naturel réduit à chaque appel.
- Méthode correcte : identifier cas de base, relation de récurrence et variant décroissant.
- Résultat de référence : `120 avec cas de base factorielle(0)=1`.
- Contrôle : comparer la sortie à la représentation attendue et expliquer l’écart éventuel.
- Erreur fréquente évitée : EF3.
- Remédiation : Activité corrective EF3 si la méthode n’est pas justifiée.

### Corrigé exercice 8
- Objectif : O4.
- Capacité : T-LANG-02B.
- Donnée traitée : entier naturel réduit à chaque appel.
- Méthode correcte : identifier cas de base, relation de récurrence et variant décroissant.
- Résultat de référence : `120 avec cas de base factorielle(0)=1`.
- Contrôle : comparer la sortie à la représentation attendue et expliquer l’écart éventuel.
- Erreur fréquente évitée : EF4.
- Remédiation : Activité corrective EF4 si la méthode n’est pas justifiée.

## Barème de correction
- Méthode explicite : 4 points.
- Résultat correct : 3 points.
- Justification reliée à la capacité : 2 points.
- Contrôle ou cas limite : 1 point.

## Erreurs fréquentes
- Erreur fréquente EF1 - répondre seulement par `120 avec cas de base factorielle(0)=1` sans écrire la méthode.
- Erreur fréquente EF2 - appliquer identifier cas de base, relation de récurrence et variant décroissant dans le mauvais ordre.
- Erreur fréquente EF3 - oublier le cas limite : appel récursif sans diminution ou profondeur excessive.
- Erreur fréquente EF4 - citer une capacité officielle sans la relier à une production observable.

## Remédiation ciblée
- Activité corrective EF1 : reprendre l’exemple en imposant quatre colonnes, donnée, opération, résultat, contrôle.
- Activité corrective EF2 : refaire la méthode avec des étapes numérotées et une vérification à chaque étape.
- Activité corrective EF3 : construire deux variantes du cas limite `appel récursif sans diminution ou profondeur excessive` et comparer les sorties.
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

