---
title: "T14 - cours - modularité, API, paradigmes et bugs"
level: "terminale"
sequence_id: "T14"
document_type: "cours"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "modularité, API, paradigmes et bugs"
notion: "modularité, API, paradigmes et bugs"
private_data: false
official_program:
  capacities:
    - "T-LANG-03A"
    - "T-LANG-03B"
    - "T-LANG-03C"
    - "T-LANG-04A"
    - "T-LANG-04B"
    - "T-LANG-05"
---

# T14 - Cours - modularité, API, paradigmes et bugs

## Objectifs spécifiques
- Identifier les données utiles de la situation : meteo.py expose moyenne_temperature(releves) ; releves=[{ville:Sfax,temperature:31},{ville:Tunis,temperature:29}].
- Employer le vocabulaire : API, documentation, module, paradigme impératif, paradigme fonctionnel, objet.
- Produire une trace, une table, une valeur ou un pseudo-code vérifiable.

## Capacités officielles
- T-LANG-03A.
- T-LANG-03B.
- T-LANG-03C.
- T-LANG-04A.
- T-LANG-04B.
- T-LANG-05.

## Situation-problème
meteo.py expose moyenne_temperature(releves) ; releves=[{ville:Sfax,temperature:31},{ville:Tunis,temperature:29}]

## À savoir
- API.
- documentation.
- module.
- paradigme impératif.
- paradigme fonctionnel.
- objet.
- bug de typage.
- effet de bord.

## Méthodes
- définir fonction publique documentée.
- séparer module et script principal.
- choisir paradigme selon tâche.
- écrire un test révélant un bug.

## Exemples corrigés
### Exemple corrigé 1
- Donnée : `meteo.py expose moyenne_temperature(releves) ; releves=[{ville:Sfax,temperature:31},{ville:Tunis,temperature:29}]`.
- Méthode : définir fonction publique documentée.
- Résultat attendu : moyenne_temperature(releves) -> 30.0.
- Contrôle : capacité T-LANG-03A et cas limite `liste vide`.
### Exemple corrigé 2
- Donnée : `meteo.py expose moyenne_temperature(releves) ; releves=[{ville:Sfax,temperature:31},{ville:Tunis,temperature:29}]`.
- Méthode : séparer module et script principal.
- Résultat attendu : from meteo import moyenne_temperature.
- Contrôle : capacité T-LANG-03B et cas limite `clé temperature absente`.
### Exemple corrigé 3
- Donnée : `meteo.py expose moyenne_temperature(releves) ; releves=[{ville:Sfax,temperature:31},{ville:Tunis,temperature:29}]`.
- Méthode : choisir paradigme selon tâche.
- Résultat attendu : temperature="31" refusée ou convertie.
- Contrôle : capacité T-LANG-03C et cas limite `type chaîne`.
### Exemple corrigé 4
- Donnée : `meteo.py expose moyenne_temperature(releves) ; releves=[{ville:Sfax,temperature:31},{ville:Tunis,temperature:29}]`.
- Méthode : écrire un test révélant un bug.
- Résultat attendu : liste vide -> ValueError.
- Contrôle : capacité T-LANG-04A et cas limite `liste vide`.

## Cas limites
- liste vide.
- clé temperature absente.
- type chaîne.

## Erreurs fréquentes
- import avec effet de bord.
- API sans docstring.
- bug corrigé sans test.

## Exercices intégrés
1. Identifier les données utiles dans `meteo.py expose moyenne_temperature(releves) ; releves=[{ville:Sfax,temperature:31},{ville:Tunis,temperature:29}]`.
2. Appliquer : définir fonction publique documentée.
3. Appliquer : séparer module et script principal.
4. Décider le cas limite `liste vide`.

## Critères de réussite observables
- Une capacité parmi T-LANG-03A, T-LANG-03B, T-LANG-03C, T-LANG-04A, T-LANG-04B, T-LANG-05 est citée et utilisée.
- Le résultat attendu est explicite : moyenne_temperature(releves) -> 30.0.
- Le cas limite `clé temperature absente` est tranché.

## Lien avec la progression
- Séance : T14-S1 à T14-S4.
- TD : `T14_TD_modularite_api_paradigmes_bugs.md`.
- TP : `T14_tp_modularite_api_paradigmes_bugs.md`.
- Évaluation : `T14_evaluation_modularite_api_paradigmes_bugs.md`.

## Renforcement explicatif ciblé

Ce cours doit être lu comme une progression sur modularité, API et bugs. La notion ne se réduit pas à une liste de mots : on part d'une situation observable, on nomme les objets manipulés, puis on applique une méthode vérifiable sur un cas limité avant de généraliser.

### Savoir disciplinaire
- Vocabulaire à maîtriser : module, interface, contrat, API, exception, test de régression, effet de bord.
- Capacités reliées : T-LANG-03A, T-LANG-03B, T-LANG-03C, T-LANG-04A, T-LANG-04B, T-LANG-05.
- Le savoir attendu consiste à expliquer le rôle de chaque objet avant de l'utiliser dans un exercice.

### Savoir-faire et méthodes opérationnelles
- définir une interface minimale avant l’implémentation.
- écrire un test qui reproduit un bug.
- isoler une dépendance dans un module.

### Erreurs fréquentes spécifiques
- Un élève peut modifier une API sans mettre à jour ses appels ; la correction consiste à reprendre la définition puis à refaire la trace sur un exemple minimal.
- Un élève peut masquer une exception utile ; la correction consiste à isoler le cas limite avant de recommencer le calcul ou le raisonnement.
- Un élève peut corriger un bug sans test de régression ; la correction consiste à vérifier le résultat avec une donnée différente.

### Cas limites à contrôler
- Cas minimal : une donnée vide, un seul élément, une route absente ou une structure sans enfant selon la notion.
- Cas ambigu : doublon, égalité, absence de correspondance ou choix local non optimal.

### Synthèse savoir / savoir-faire / méthode
- Savoir : définir précisément les objets de modularité, API et bugs.
- Savoir-faire : appliquer une méthode contrôlable à une donnée explicite.
- Méthode : annoncer la donnée, exécuter les étapes dans l'ordre, puis vérifier le résultat par un cas limite.
