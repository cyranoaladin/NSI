---
title: "T10 - Fiche cours - SQL : SELECT, WHERE, JOIN"
level: "terminale"
sequence_id: "T10"
document_type: "fiche_cours"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "SQL"
notion: "requêtes de lecture"
official_program:
  capacities:
    - "T-BDD-03A"
    - "T-BDD-03B"
    - "T-BDD-03C"
    - "T-BDD-03D"
    - "T-BDD-03E"
private_data: false
---
# T10 - Fiche cours - SQL : SELECT, WHERE, JOIN

## À savoir
- Capacités travaillées dans la fiche : T-BDD-03A, T-BDD-03B, T-BDD-03C, T-BDD-03D, T-BDD-03E.
- La notion “requête SELECT” sert à filtrer et relier des tables.
- Le vocabulaire de requêtes de lecture doit être employé avec des données concrètes propres au chapitre T10.
- La capacité associée à requêtes de lecture se travaille par lecture, manipulation et justification dans T10.
- Une réponse sur requêtes de lecture distingue la situation étudiée, la méthode choisie, le résultat et le contrôle.

## Méthodes
1. écrire FROM, WHERE puis colonnes utiles.
2. Écrire un exemple minimal de requêtes de lecture avant de traiter le cas général du chapitre T10.
3. Identifier le cas limite de requêtes de lecture qui peut faire échouer la méthode.
4. Relier la conclusion de requêtes de lecture à une opération ou une propriété observable.

## Exemples corrigés
### Exemple corrigé 1
SELECT nom FROM Eleve filtre une classe.
### Exemple corrigé 2
On reprend le premier exemple avec une donnée différente et on contrôle explicitement la conclusion pour requêtes de lecture.

## Erreurs fréquentes
- une jointure sans condition multiplie les lignes : corriger avec un contre-exemple court.
- Donner seulement le résultat en requêtes de lecture : ajouter une ligne qui nomme la méthode utilisée.
- Oublier le cas limite de requêtes de lecture : le tester avant d’écrire la conclusion.

## Cas limites
- Cas vide ou minimal pour requête SELECT.
- Donnée invalide ou absente dans une situation de requêtes de lecture.
- Situation de requêtes de lecture où deux réponses semblent possibles et exigent une convention explicite.

## Mini-exercices
### Mini-exercice 1
Définir requête SELECT en une phrase précise.
### Mini-exercice 2
Appliquer la méthode à un petit exemple de requête SELECT.
### Mini-exercice 3
Repérer une erreur fréquente dans une réponse proposée sur requêtes de lecture.
### Mini-exercice 4
Citer le cas limite à vérifier en priorité pour requêtes de lecture.

## Réponses rapides
1. requête SELECT doit être défini avec son rôle, pas seulement son nom.
2. La réponse sur requêtes de lecture doit montrer les étapes utiles.
3. L’erreur de requêtes de lecture se repère en testant l’hypothèse oubliée.
4. Le cas vide ou minimal est souvent le premier contrôle pour requêtes de lecture.

## À retenir
- Pour requêtes de lecture, commencer par reconnaître la situation exacte.
- Une méthode de T10 doit être accompagnée d’un exemple numérique ou textuel.
- Les capacités T-BDD-03A, T-BDD-03B, T-BDD-03C, T-BDD-03D, T-BDD-03E restent au statut de travail tant que la revue humaine manque.
- La fiche prépare la révision de requêtes de lecture sans produire à elle seule une preuve de couverture annuelle.
- Un cas limite explicite est obligatoire avant toute conclusion sur requêtes_de_lecture.

## Lien avec la progression
- Séances : T10-S1 et T10-S2 lorsque le chapitre est découpé en plusieurs temps.
- TD lié : T10_TD_requêtes_de_lecture.md, à produire ou relire dans le registre de supports.
- TP lié : T10_TP_requêtes_de_lecture.py si la progression prévoit une manipulation programmée.
- Évaluation ou projet lié : contrôle court du chapitre T10 ou livrable associé.
- Dossier de progression : 03_progressions/fiches_cours/terminale/T10/.

## Auto-évaluation
- Je sais expliquer requêtes de lecture sans lire la fiche.
- Je sais refaire les exemples de T10 avec des données différentes.
- Je sais identifier l’erreur fréquente la plus probable pour requêtes de lecture.
- Je sais choisir un cas limite de requêtes de lecture avant de répondre.
- Je sais relier la fiche T10 sur requêtes de lecture à une séance, un TD ou un TP du chapitre.
