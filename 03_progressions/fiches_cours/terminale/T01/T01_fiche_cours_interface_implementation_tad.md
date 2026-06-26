---
title: "T01 - Fiche cours - Interface, implémentation et TAD"
level: "terminale"
sequence_id: "T01"
document_type: "fiche_cours"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Structures abstraites"
notion: "TAD"
official_program:
  capacities:
    - "T-STRUCT-01A"
    - "T-STRUCT-01B"
    - "T-STRUCT-01C"
private_data: false
---
# T01 - Fiche cours - Interface, implémentation et TAD

## À savoir
- Capacités travaillées dans la fiche : T-STRUCT-01A, T-STRUCT-01B, T-STRUCT-01C.
- La notion “type abstrait” sert à séparer interface et représentation.
- Le vocabulaire de TAD doit être employé avec des données concrètes propres au chapitre T01.
- La capacité associée à TAD se travaille par lecture, manipulation et justification dans T01.
- Une réponse sur TAD distingue la situation étudiée, la méthode choisie, le résultat et le contrôle.

## Méthodes
1. lister opérations et invariants.
2. Écrire un exemple minimal de TAD avant de traiter le cas général du chapitre T01.
3. Identifier le cas limite de TAD qui peut faire échouer la méthode.
4. Relier la conclusion de TAD à une opération ou une propriété observable.

## Exemples corrigés
### Exemple corrigé 1
une pile offre empiler et depiler.
### Exemple corrigé 2
On reprend le premier exemple avec une donnée différente et on contrôle explicitement la conclusion pour TAD.

## Erreurs fréquentes
- l’implémentation n’est pas le contrat : corriger avec un contre-exemple court.
- Donner seulement le résultat en TAD : ajouter une ligne qui nomme la méthode utilisée.
- Oublier le cas limite de TAD : le tester avant d’écrire la conclusion.

## Cas limites
- Cas vide ou minimal pour type abstrait.
- Donnée invalide ou absente dans une situation de TAD.
- Situation de TAD où deux réponses semblent possibles et exigent une convention explicite.

## Mini-exercices
### Mini-exercice 1
Définir type abstrait en une phrase précise.
### Mini-exercice 2
Appliquer la méthode à un petit exemple de type abstrait.
### Mini-exercice 3
Repérer une erreur fréquente dans une réponse proposée sur TAD.
### Mini-exercice 4
Citer le cas limite à vérifier en priorité pour TAD.

## Réponses rapides
1. type abstrait doit être défini avec son rôle, pas seulement son nom.
2. La réponse sur TAD doit montrer les étapes utiles.
3. L’erreur de TAD se repère en testant l’hypothèse oubliée.
4. Le cas vide ou minimal est souvent le premier contrôle pour TAD.

## À retenir
- Pour TAD, commencer par reconnaître la situation exacte.
- Une méthode de T01 doit être accompagnée d’un exemple numérique ou textuel.
- Les capacités T-STRUCT-01A, T-STRUCT-01B, T-STRUCT-01C restent au statut de travail tant que la revue humaine manque.
- La fiche prépare la révision de TAD sans produire à elle seule une preuve de couverture annuelle.
- Un cas limite explicite est obligatoire avant toute conclusion sur TAD.

## Lien avec la progression
- Séances : T01-S1 et T01-S2 lorsque le chapitre est découpé en plusieurs temps.
- TD lié : T01_TD_TAD.md, à produire ou relire dans le registre de supports.
- TP lié : T01_TP_TAD.py si la progression prévoit une manipulation programmée.
- Évaluation ou projet lié : contrôle court du chapitre T01 ou livrable associé.
- Dossier de progression : 03_progressions/fiches_cours/terminale/T01/.

## Auto-évaluation
- Je sais expliquer TAD sans lire la fiche.
- Je sais refaire les exemples de T01 avec des données différentes.
- Je sais identifier l’erreur fréquente la plus probable pour TAD.
- Je sais choisir un cas limite de TAD avant de répondre.
- Je sais relier la fiche T01 sur TAD à une séance, un TD ou un TP du chapitre.
