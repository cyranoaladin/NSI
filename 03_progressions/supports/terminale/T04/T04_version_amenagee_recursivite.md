---
title: "T04 - Version Amenagee - Récursivité contrôlée"
level: "terminale"
sequence_id: "T04"
document_type: "version_amenagee"
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


# T04 - Version Amenagee - Récursivité contrôlée

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

## Version aménagée - Énoncé élève
- Situation : un calcul naturel se définit par réduction du problème mais risque de ne jamais s’arrêter.
- Donnée fournie : entier naturel réduit à chaque appel.
- Exemple de départ : `factorielle(5)`.
- Les étapes sont séparées pour réduire la charge de lecture.

## Aide intégrée
- Aide 1 : commence par recopier la donnée utile, ici entier naturel réduit à chaque appel.
- Aide 2 : applique seulement cette méthode : identifier cas de base, relation de récurrence et variant décroissant.
- Aide 3 : compare avec le résultat de référence `120 avec cas de base factorielle(0)=1`.
- Aide 4 : vérifie le cas limite `appel récursif sans diminution ou profondeur excessive`.

## Exemple corrigé précis
- Exemple guidé : `factorielle(5)`.
- Correction guidée : identifier cas de base, relation de récurrence et variant décroissant, donc `120 avec cas de base factorielle(0)=1`.

## Exercices numérotés
- Exercice 1 : compléter la phrase guidée pour l’objectif O1.
- Exercice 2 : compléter la phrase guidée pour l’objectif O2.
- Exercice 3 : compléter la phrase guidée pour l’objectif O3.
- Exercice 4 : compléter la phrase guidée pour l’objectif O4.
- Exercice 5 : compléter la phrase guidée pour l’objectif O1.
- Exercice 6 : compléter la phrase guidée pour l’objectif O2.
- Exercice 7 : compléter la phrase guidée pour l’objectif O3.
- Exercice 8 : compléter la phrase guidée pour l’objectif O4.

## Espace de réponse
- Réponse exercice 1 - Donnée : ____________________.
- Réponse exercice 1 - Méthode : ____________________.
- Réponse exercice 1 - Résultat : ____________________.
- Réponse exercice 1 - Contrôle : ____________________.
- Réponse exercice 2 - Donnée : ____________________.
- Réponse exercice 2 - Méthode : ____________________.
- Réponse exercice 2 - Résultat : ____________________.
- Réponse exercice 2 - Contrôle : ____________________.
- Réponse exercice 3 - Donnée : ____________________.
- Réponse exercice 3 - Méthode : ____________________.
- Réponse exercice 3 - Résultat : ____________________.
- Réponse exercice 3 - Contrôle : ____________________.
- Réponse exercice 4 - Donnée : ____________________.
- Réponse exercice 4 - Méthode : ____________________.
- Réponse exercice 4 - Résultat : ____________________.
- Réponse exercice 4 - Contrôle : ____________________.
- Réponse exercice 5 - Donnée : ____________________.
- Réponse exercice 5 - Méthode : ____________________.
- Réponse exercice 5 - Résultat : ____________________.
- Réponse exercice 5 - Contrôle : ____________________.
- Réponse exercice 6 - Donnée : ____________________.
- Réponse exercice 6 - Méthode : ____________________.
- Réponse exercice 6 - Résultat : ____________________.
- Réponse exercice 6 - Contrôle : ____________________.
- Réponse exercice 7 - Donnée : ____________________.
- Réponse exercice 7 - Méthode : ____________________.
- Réponse exercice 7 - Résultat : ____________________.
- Réponse exercice 7 - Contrôle : ____________________.
- Réponse exercice 8 - Donnée : ____________________.
- Réponse exercice 8 - Méthode : ____________________.
- Réponse exercice 8 - Résultat : ____________________.
- Réponse exercice 8 - Contrôle : ____________________.

## Corrigé
- Corrigé exercice 1 : donnée `entier naturel réduit à chaque appel`, méthode `identifier cas de base, relation de récurrence et variant décroissant`, résultat `120 avec cas de base factorielle(0)=1`, contrôle EF1.
- Corrigé exercice 2 : donnée `entier naturel réduit à chaque appel`, méthode `identifier cas de base, relation de récurrence et variant décroissant`, résultat `120 avec cas de base factorielle(0)=1`, contrôle EF2.
- Corrigé exercice 3 : donnée `entier naturel réduit à chaque appel`, méthode `identifier cas de base, relation de récurrence et variant décroissant`, résultat `120 avec cas de base factorielle(0)=1`, contrôle EF3.
- Corrigé exercice 4 : donnée `entier naturel réduit à chaque appel`, méthode `identifier cas de base, relation de récurrence et variant décroissant`, résultat `120 avec cas de base factorielle(0)=1`, contrôle EF4.
- Corrigé exercice 5 : donnée `entier naturel réduit à chaque appel`, méthode `identifier cas de base, relation de récurrence et variant décroissant`, résultat `120 avec cas de base factorielle(0)=1`, contrôle EF1.
- Corrigé exercice 6 : donnée `entier naturel réduit à chaque appel`, méthode `identifier cas de base, relation de récurrence et variant décroissant`, résultat `120 avec cas de base factorielle(0)=1`, contrôle EF2.
- Corrigé exercice 7 : donnée `entier naturel réduit à chaque appel`, méthode `identifier cas de base, relation de récurrence et variant décroissant`, résultat `120 avec cas de base factorielle(0)=1`, contrôle EF3.
- Corrigé exercice 8 : donnée `entier naturel réduit à chaque appel`, méthode `identifier cas de base, relation de récurrence et variant décroissant`, résultat `120 avec cas de base factorielle(0)=1`, contrôle EF4.

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

