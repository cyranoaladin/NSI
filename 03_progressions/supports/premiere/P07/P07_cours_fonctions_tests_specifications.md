---
title: "P07 - cours - fonctions, tests et spécifications"
level: "premiere"
sequence_id: "P07"
document_type: "cours"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "fonctions, tests et spécifications"
notion: "fonctions, tests et spécifications"
private_data: false
official_program:
  capacities:
    - "P-LANG-01"
    - "P-LANG-02"
    - "P-LANG-03A"
    - "P-LANG-03B"
    - "P-LANG-03C"
    - "P-LANG-04"
    - "P-LANG-05"
---

# P07 - Cours - fonctions, tests et spécifications

## Objectifs spécifiques
- Identifier les données utiles de la situation : prix_ht=80.0, taux=0.20 -> 96.0 ; prix_ht=-5.0 -> ValueError.
- Employer le vocabulaire : signature, précondition, postcondition, assertion, test unitaire, test limite.
- Produire une trace, une table, une valeur ou un pseudo-code vérifiable.

## Capacités officielles
- P-LANG-01.
- P-LANG-02.
- P-LANG-03A.
- P-LANG-03B.
- P-LANG-03C.
- P-LANG-04.
- P-LANG-05.

## Situation-problème
prix_ht=80.0, taux=0.20 -> 96.0 ; prix_ht=-5.0 -> ValueError

## À savoir
- signature.
- précondition.
- postcondition.
- assertion.
- test unitaire.
- test limite.
- erreur de type.
- fonction pure.

## Méthodes
- écrire def prix_ttc(prix_ht: float, taux: float) -> float.
- poser prix_ht >= 0 et taux >= 0.
- vérifier résultat >= prix_ht.
- écrire tests nominal, limite et invalide.

## Exemples corrigés
### Exemple corrigé 1
- Donnée : `prix_ht=80.0, taux=0.20 -> 96.0 ; prix_ht=-5.0 -> ValueError`.
- Méthode : écrire def prix_ttc(prix_ht: float, taux: float) -> float.
- Résultat attendu : signature complète de prix_ttc.
- Contrôle : capacité P-LANG-01 et cas limite `prix_ht=0`.
### Exemple corrigé 2
- Donnée : `prix_ht=80.0, taux=0.20 -> 96.0 ; prix_ht=-5.0 -> ValueError`.
- Méthode : poser prix_ht >= 0 et taux >= 0.
- Résultat attendu : prix_ttc(80,0.20) -> 96.0.
- Contrôle : capacité P-LANG-02 et cas limite `taux=0`.
### Exemple corrigé 3
- Donnée : `prix_ht=80.0, taux=0.20 -> 96.0 ; prix_ht=-5.0 -> ValueError`.
- Méthode : vérifier résultat >= prix_ht.
- Résultat attendu : prix_ttc(-5,0.20) -> ValueError.
- Contrôle : capacité P-LANG-03A et cas limite `type chaîne "80"`.
### Exemple corrigé 4
- Donnée : `prix_ht=80.0, taux=0.20 -> 96.0 ; prix_ht=-5.0 -> ValueError`.
- Méthode : écrire tests nominal, limite et invalide.
- Résultat attendu : taux=0 -> résultat 80.0.
- Contrôle : capacité P-LANG-03B et cas limite `prix_ht=0`.

## Cas limites
- prix_ht=0.
- taux=0.
- type chaîne "80".

## Erreurs fréquentes
- test unique non suffisant.
- précondition absente.
- effet de bord global.

## Exercices intégrés
1. Identifier les données utiles dans `prix_ht=80.0, taux=0.20 -> 96.0 ; prix_ht=-5.0 -> ValueError`.
2. Appliquer : écrire def prix_ttc(prix_ht: float, taux: float) -> float.
3. Appliquer : poser prix_ht >= 0 et taux >= 0.
4. Décider le cas limite `prix_ht=0`.

## Critères de réussite observables
- Une capacité parmi P-LANG-01, P-LANG-02, P-LANG-03A, P-LANG-03B, P-LANG-03C, P-LANG-04, P-LANG-05 est citée et utilisée.
- Le résultat attendu est explicite : signature complète de prix_ttc.
- Le cas limite `taux=0` est tranché.

## Lien avec la progression
- Séance : P07-S1 à P07-S4.
- TD : `P07_TD_fonctions_tests_specifications.md`.
- TP : `P07_tp_fonctions_tests_specifications.md`.
- Évaluation : `P07_evaluation_fonctions_tests_specifications.md`.

## Renforcement explicatif ciblé

Ce cours doit être lu comme une progression sur fonctions et tests. La notion ne se réduit pas à une liste de mots : on part d'une situation observable, on nomme les objets manipulés, puis on applique une méthode vérifiable sur un cas limité avant de généraliser.

### Savoir disciplinaire
- Vocabulaire à maîtriser : signature, précondition, postcondition, assertion, test unitaire, effet de bord.
- Capacités reliées : P-LANG-01, P-LANG-02, P-LANG-03A, P-LANG-03B, P-LANG-03C, P-LANG-04, P-LANG-05.
- Le savoir attendu consiste à expliquer le rôle de chaque objet avant de l'utiliser dans un exercice.

### Savoir-faire et méthodes opérationnelles
- vérifier une signature avant d’écrire le corps de la fonction.
- tester une valeur limite avant une valeur ordinaire.
- isoler une fonction pure d’une procédure qui modifie une liste.

### Erreurs fréquentes spécifiques
- Un élève peut confondre précondition et test de sortie ; la correction consiste à reprendre la définition puis à refaire la trace sur un exemple minimal.
- Un élève peut oublier le cas liste vide dans une moyenne ; la correction consiste à isoler le cas limite avant de recommencer le calcul ou le raisonnement.
- Un élève peut mélanger valeur renvoyée et affichage avec print ; la correction consiste à vérifier le résultat avec une donnée différente.

### Cas limites à contrôler
- Cas minimal : une donnée vide, un seul élément, une route absente ou une structure sans enfant selon la notion.
- Cas ambigu : doublon, égalité, absence de correspondance ou choix local non optimal.

### Synthèse savoir / savoir-faire / méthode
- Savoir : définir précisément les objets de fonctions et tests.
- Savoir-faire : appliquer une méthode contrôlable à une donnée explicite.
- Méthode : annoncer la donnée, exécuter les étapes dans l'ordre, puis vérifier le résultat par un cas limite.
