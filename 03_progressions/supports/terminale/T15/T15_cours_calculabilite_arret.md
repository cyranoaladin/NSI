---
title: "T15 - cours - calculabilité, programme comme donnée et arrêt"
level: "terminale"
sequence_id: "T15"
document_type: "cours"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "calculabilité, programme comme donnée et arrêt"
notion: "calculabilité, programme comme donnée et arrêt"
private_data: false
official_program:
  capacities:
    - "T-LANG-01A"
    - "T-LANG-01B"
    - "T-LANG-01C"
---

# T15 - Cours - calculabilité, programme comme donnée et arrêt

## Objectifs spécifiques
- Identifier les données utiles de la situation : arrete(P,x) prétend répondre True si P(x) termine ; Q appelle arrete(Q,Q).
- Employer le vocabulaire : programme comme donnée, interpréteur, calculabilité, langage indépendant, problème de l arrêt, contradiction.
- Produire une trace, une table, une valeur ou un pseudo-code vérifiable.

## Capacités officielles
- T-LANG-01A.
- T-LANG-01B.
- T-LANG-01C.

## Situation-problème
arrete(P,x) prétend répondre True si P(x) termine ; Q appelle arrete(Q,Q)

## À savoir
- programme comme donnée.
- interpréteur.
- calculabilité.
- langage indépendant.
- problème de l arrêt.
- contradiction.

## Méthodes
- encoder un programme comme texte.
- raisonner indépendamment de Python.
- poser un oracle hypothétique.
- construire un programme contradictoire.

## Exemples corrigés
### Exemple corrigé 1
- Donnée : `arrete(P,x) prétend répondre True si P(x) termine ; Q appelle arrete(Q,Q)`.
- Méthode : encoder un programme comme texte.
- Résultat attendu : source="print(1)" est une donnée.
- Contrôle : capacité T-LANG-01A et cas limite `programme très long mais fini`.
### Exemple corrigé 2
- Donnée : `arrete(P,x) prétend répondre True si P(x) termine ; Q appelle arrete(Q,Q)`.
- Méthode : raisonner indépendamment de Python.
- Résultat attendu : arrete(P,x) renvoie True ou False.
- Contrôle : capacité T-LANG-01B et cas limite `langage différent`.
### Exemple corrigé 3
- Donnée : `arrete(P,x) prétend répondre True si P(x) termine ; Q appelle arrete(Q,Q)`.
- Méthode : poser un oracle hypothétique.
- Résultat attendu : Q boucle si arrete(Q,Q) dit True.
- Contrôle : capacité T-LANG-01C et cas limite `entrée absente`.
### Exemple corrigé 4
- Donnée : `arrete(P,x) prétend répondre True si P(x) termine ; Q appelle arrete(Q,Q)`.
- Méthode : construire un programme contradictoire.
- Résultat attendu : contradiction donc oracle impossible.
- Contrôle : capacité T-LANG-01A et cas limite `programme très long mais fini`.

## Cas limites
- programme très long mais fini.
- langage différent.
- entrée absente.

## Erreurs fréquentes
- non connu confondu avec impossible.
- tests finis comme preuve.
- contradiction oubliée.

## Exercices intégrés
1. Identifier les données utiles dans `arrete(P,x) prétend répondre True si P(x) termine ; Q appelle arrete(Q,Q)`.
2. Appliquer : encoder un programme comme texte.
3. Appliquer : raisonner indépendamment de Python.
4. Décider le cas limite `programme très long mais fini`.

## Critères de réussite observables
- Une capacité parmi T-LANG-01A, T-LANG-01B, T-LANG-01C est citée et utilisée.
- Le résultat attendu est explicite : source="print(1)" est une donnée.
- Le cas limite `langage différent` est tranché.

## Lien avec la progression
- Séance : T15-S1 à T15-S4.
- TD : `T15_TD_calculabilite_arret.md`.
- TP : `T15_tp_calculabilite_arret.md`.
- Évaluation : `T15_evaluation_calculabilite_arret.md`.
