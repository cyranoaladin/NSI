---
title: "T01 - Trace - Interfaces de structures abstraites"
level: "terminale"
sequence_id: "T01"
document_type: "trace"
status: "needs_review"
version: "0.3.0"
source: "BO 2019 ; ressource locale candidate : Documents_DRIVE/2_NSI/Formation TOULOUSE/BLOC4/Cours EIL - TAD - 2019-2020.pdf"
theme: "Structures de données"
notion: "interface, opération, coût"
objectifs:
  - "Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation."
  - "Objectif O2 - Appliquer une méthode explicite sur un exemple guidé."
  - "Objectif O3 - Justifier le résultat obtenu sur un cas nouveau."
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente."
private_data: false
official_program:
  capacities:
    - "T-STRUCT-01A"
    - "T-STRUCT-01B"
    - "T-STRUCT-01C"
---


# T01 - Trace - Interfaces de structures abstraites

## Objectifs spécifiques
- Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation.
- Objectif O2 - Appliquer une méthode explicite sur un exemple guidé.
- Objectif O3 - Justifier le résultat obtenu sur un cas nouveau.
- Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente.

## Capacités officielles atomiques
- T-STRUCT-01A
- T-STRUCT-01B
- T-STRUCT-01C

## Prérequis
- Lire une consigne technique sans confondre donnée, méthode et résultat.
- Écrire une réponse sous forme de phrases courtes et vérifiables.
- Utiliser Python en distinguant expression, valeur, variable et affichage.
- Conserver une trace de calcul ou de raisonnement exploitable pour la révision.

## Séance(s) correspondante(s)
- T01-S1 à T01-S5 : ce support est rattaché aux séances indiquées dans la progression.

## Situation-problème concrète
un même service peut être décrit par ses opérations avant de choisir l’implémentation Python. La tâche consiste à traiter interface, opération, coût sans réponse intuitive non vérifiée.

## Activité d’entrée
1. Lire la situation : un même service peut être décrit par ses opérations avant de choisir l’implémentation Python.
2. Isoler la donnée de départ : ensemble d’opérations observables.
3. Prédire individuellement le résultat de l’exemple `sac avec ajouter, retirer, est_vide`.
4. Comparer deux stratégies et noter la divergence précise.
5. Appliquer la méthode retenue : nommer les opérations, les préconditions et les effets sans dépendre du stockage.
6. Contrôler avec le résultat de référence : interface séparée de la représentation interne.
7. Tester le cas limite suivant : confondre interface et liste Python concrète.
8. Rédiger une phrase qui relie donnée, méthode, résultat et contrôle.

## Trace synthétique structurée
- Notion : interface, opération, coût.
- Exemple mémorisé : `sac avec ajouter, retirer, est_vide`.
- Résultat contrôlé : interface séparée de la représentation interne.
- Méthode courte : nommer les opérations, les préconditions et les effets sans dépendre du stockage.
- Cas limite à écrire dans la marge : confondre interface et liste Python concrète.

## Exemple corrigé précis
- Donnée : ensemble d’opérations observables.
- Calcul ou raisonnement : nommer les opérations, les préconditions et les effets sans dépendre du stockage.
- Conclusion : le résultat contrôlé est `interface séparée de la représentation interne`.
- Justification : la méthode respecte la représentation annoncée en début de réponse.

## Exercices numérotés
- Exercice 1 : écrire une trace de quatre lignes pour l’objectif O1.
- Exercice 2 : écrire une trace de quatre lignes pour l’objectif O2.
- Exercice 3 : écrire une trace de quatre lignes pour l’objectif O3.
- Exercice 4 : écrire une trace de quatre lignes pour l’objectif O4.
- Exercice 5 : écrire une trace de quatre lignes pour l’objectif O1.
- Exercice 6 : écrire une trace de quatre lignes pour l’objectif O2.
- Exercice 7 : écrire une trace de quatre lignes pour l’objectif O3.
- Exercice 8 : écrire une trace de quatre lignes pour l’objectif O4.

## Corrigé
- Corrigé exercice 1 : la trace contient donnée, opération, résultat `interface séparée de la représentation interne` et contrôle EF1.
- Corrigé exercice 2 : la trace contient donnée, opération, résultat `interface séparée de la représentation interne` et contrôle EF2.
- Corrigé exercice 3 : la trace contient donnée, opération, résultat `interface séparée de la représentation interne` et contrôle EF3.
- Corrigé exercice 4 : la trace contient donnée, opération, résultat `interface séparée de la représentation interne` et contrôle EF4.
- Corrigé exercice 5 : la trace contient donnée, opération, résultat `interface séparée de la représentation interne` et contrôle EF1.
- Corrigé exercice 6 : la trace contient donnée, opération, résultat `interface séparée de la représentation interne` et contrôle EF2.
- Corrigé exercice 7 : la trace contient donnée, opération, résultat `interface séparée de la représentation interne` et contrôle EF3.
- Corrigé exercice 8 : la trace contient donnée, opération, résultat `interface séparée de la représentation interne` et contrôle EF4.

## Erreurs fréquentes
- Erreur fréquente EF1 - répondre seulement par `interface séparée de la représentation interne` sans écrire la méthode.
- Erreur fréquente EF2 - appliquer nommer les opérations, les préconditions et les effets sans dépendre du stockage dans le mauvais ordre.
- Erreur fréquente EF3 - oublier le cas limite : confondre interface et liste Python concrète.
- Erreur fréquente EF4 - citer une capacité officielle sans la relier à une production observable.

## Remédiation ciblée
- Activité corrective EF1 : reprendre l’exemple en imposant quatre colonnes, donnée, opération, résultat, contrôle.
- Activité corrective EF2 : refaire la méthode avec des étapes numérotées et une vérification à chaque étape.
- Activité corrective EF3 : construire deux variantes du cas limite `confondre interface et liste Python concrète` et comparer les sorties.
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

## Relecture de la trace
- La trace ne contient pas de phrase vague : chaque ligne sert à refaire la méthode.
- Les capacités officielles restent visibles dans le titre ou dans la marge.
- Les critères de réussite sont cochés après le TD et avant le TP.
