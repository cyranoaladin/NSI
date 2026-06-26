---
title: "T14 - Fiche cours - Modularité, API, paradigmes et bugs"
level: "terminale"
sequence_id: "T14"
document_type: "fiche_cours"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Langages"
notion: "modularité API"
official_program:
  capacities:
    - "T-LANG-03A"
    - "T-LANG-03B"
    - "T-LANG-03C"
    - "T-LANG-04A"
    - "T-LANG-04B"
    - "T-LANG-05"
private_data: false
---
# T14 - Fiche cours - Modularité, API, paradigmes et bugs

## À savoir
- Capacités travaillées dans la fiche : T-LANG-03A, T-LANG-03B, T-LANG-03C, T-LANG-04A, T-LANG-04B, T-LANG-05.
- La notion “modularité” sert à découper un programme en API testables.
- Le vocabulaire de modularité API doit être employé avec des données concrètes propres au chapitre T14.
- La capacité associée à modularité API se travaille par lecture, manipulation et justification dans T14.
- Une réponse sur modularité API distingue la situation étudiée, la méthode choisie, le résultat et le contrôle.

## Méthodes
1. réduire un bug à un exemple minimal.
2. Écrire un exemple minimal de modularité API avant de traiter le cas général du chapitre T14.
3. Identifier le cas limite de modularité API qui peut faire échouer la méthode.
4. Relier la conclusion de modularité API à une opération ou une propriété observable.

## Exemples corrigés
### Exemple corrigé 1
un module stats expose moyenne.
### Exemple corrigé 2
On reprend le premier exemple avec une donnée différente et on contrôle explicitement la conclusion pour modularité API.

## Erreurs fréquentes
- corriger sans test favorise les retours de bug : corriger avec un contre-exemple court.
- Donner seulement le résultat en modularité API : ajouter une ligne qui nomme la méthode utilisée.
- Oublier le cas limite de modularité API : le tester avant d’écrire la conclusion.

## Cas limites
- Cas vide ou minimal pour modularité.
- Donnée invalide ou absente dans une situation de modularité API.
- Situation de modularité API où deux réponses semblent possibles et exigent une convention explicite.

## Mini-exercices
### Mini-exercice 1
Définir modularité en une phrase précise.
### Mini-exercice 2
Appliquer la méthode à un petit exemple de modularité.
### Mini-exercice 3
Repérer une erreur fréquente dans une réponse proposée sur modularité API.
### Mini-exercice 4
Citer le cas limite à vérifier en priorité pour modularité API.

## Réponses rapides
1. modularité doit être défini avec son rôle, pas seulement son nom.
2. La réponse sur modularité API doit montrer les étapes utiles.
3. L’erreur de modularité API se repère en testant l’hypothèse oubliée.
4. Le cas vide ou minimal est souvent le premier contrôle pour modularité API.

## À retenir
- Pour modularité API, commencer par reconnaître la situation exacte.
- Une méthode de T14 doit être accompagnée d’un exemple numérique ou textuel.
- Les capacités T-LANG-03A, T-LANG-03B, T-LANG-03C, T-LANG-04A, T-LANG-04B, T-LANG-05 restent au statut de travail tant que la revue humaine manque.
- La fiche prépare la révision de modularité API sans produire à elle seule une preuve de couverture annuelle.
- Un cas limite explicite est obligatoire avant toute conclusion sur modularite_API.

## Lien avec la progression
- Séances : T14-S1 et T14-S2 lorsque le chapitre est découpé en plusieurs temps.
- TD lié : T14_TD_modularite_API.md, à produire ou relire dans le registre de supports.
- TP lié : T14_TP_modularite_API.py si la progression prévoit une manipulation programmée.
- Évaluation ou projet lié : contrôle court du chapitre T14 ou livrable associé.
- Dossier de progression : 03_progressions/fiches_cours/terminale/T14/.

## Auto-évaluation
- Je sais expliquer modularité API sans lire la fiche.
- Je sais refaire les exemples de T14 avec des données différentes.
- Je sais identifier l’erreur fréquente la plus probable pour modularité API.
- Je sais choisir un cas limite de modularité API avant de répondre.
- Je sais relier la fiche T14 sur modularité API à une séance, un TD ou un TP du chapitre.
