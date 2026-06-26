---
title: "T10 - Fiche cours - SQL : INSERT, UPDATE, DELETE"
level: "terminale"
sequence_id: "T10"
document_type: "fiche_cours"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "SQL"
notion: "requêtes de modification"
official_program:
  capacities:
    - "T-BDD-03F"
    - "T-BDD-03G"
    - "T-BDD-03H"
private_data: false
---
# T10 - Fiche cours - SQL : INSERT, UPDATE, DELETE

## À savoir
- Capacités travaillées dans la fiche : T-BDD-03F, T-BDD-03G, T-BDD-03H.
- La notion “modification SQL” sert à ajouter, modifier ou supprimer des lignes.
- Le vocabulaire de requêtes de modification doit être employé avec des données concrètes propres au chapitre T10.
- La capacité associée à requêtes de modification se travaille par lecture, manipulation et justification dans T10.
- Une réponse sur requêtes de modification distingue la situation étudiée, la méthode choisie, le résultat et le contrôle.

## Méthodes
1. vérifier le WHERE par SELECT avant modification.
2. Écrire un exemple minimal de requêtes de modification avant de traiter le cas général du chapitre T10.
3. Identifier le cas limite de requêtes de modification qui peut faire échouer la méthode.
4. Relier la conclusion de requêtes de modification à une opération ou une propriété observable.

## Exemples corrigés
### Exemple corrigé 1
UPDATE Livre SET annee=2025 WHERE id=1.
### Exemple corrigé 2
On reprend le premier exemple avec une donnée différente et on contrôle explicitement la conclusion pour requêtes de modification.

## Erreurs fréquentes
- UPDATE sans WHERE touche trop de lignes : corriger avec un contre-exemple court.
- Donner seulement le résultat en requêtes de modification : ajouter une ligne qui nomme la méthode utilisée.
- Oublier le cas limite de requêtes de modification : le tester avant d’écrire la conclusion.

## Cas limites
- Cas vide ou minimal pour modification SQL.
- Donnée invalide ou absente dans une situation de requêtes de modification.
- Situation de requêtes de modification où deux réponses semblent possibles et exigent une convention explicite.

## Mini-exercices
### Mini-exercice 1
Définir modification SQL en une phrase précise.
### Mini-exercice 2
Appliquer la méthode à un petit exemple de modification SQL.
### Mini-exercice 3
Repérer une erreur fréquente dans une réponse proposée sur requêtes de modification.
### Mini-exercice 4
Citer le cas limite à vérifier en priorité pour requêtes de modification.

## Réponses rapides
1. modification SQL doit être défini avec son rôle, pas seulement son nom.
2. La réponse sur requêtes de modification doit montrer les étapes utiles.
3. L’erreur de requêtes de modification se repère en testant l’hypothèse oubliée.
4. Le cas vide ou minimal est souvent le premier contrôle pour requêtes de modification.

## À retenir
- Pour requêtes de modification, commencer par reconnaître la situation exacte.
- Une méthode de T10 doit être accompagnée d’un exemple numérique ou textuel.
- Les capacités T-BDD-03F, T-BDD-03G, T-BDD-03H restent au statut de travail tant que la revue humaine manque.
- La fiche prépare la révision de requêtes de modification sans produire à elle seule une preuve de couverture annuelle.
- Un cas limite explicite est obligatoire avant toute conclusion sur requêtes_de_modification.

## Lien avec la progression
- Séances : T10-S1 et T10-S2 lorsque le chapitre est découpé en plusieurs temps.
- TD lié : T10_TD_requêtes_de_modification.md, à produire ou relire dans le registre de supports.
- TP lié : T10_TP_requêtes_de_modification.py si la progression prévoit une manipulation programmée.
- Évaluation ou projet lié : contrôle court du chapitre T10 ou livrable associé.
- Dossier de progression : 03_progressions/fiches_cours/terminale/T10/.

## Auto-évaluation
- Je sais expliquer requêtes de modification sans lire la fiche.
- Je sais refaire les exemples de T10 avec des données différentes.
- Je sais identifier l’erreur fréquente la plus probable pour requêtes de modification.
- Je sais choisir un cas limite de requêtes de modification avant de répondre.
- Je sais relier la fiche T10 sur requêtes de modification à une séance, un TD ou un TP du chapitre.
