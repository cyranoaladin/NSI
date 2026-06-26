---
title: "P12 - Fiche cours - Tris, invariants et complexité"
level: "premiere"
sequence_id: "P12"
document_type: "fiche_cours"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Algorithmique"
notion: "tris"
official_program:
  capacities:
    - "P-ALGO-02A"
    - "P-ALGO-02B"
    - "P-ALGO-02C"
    - "P-ALGO-02D"
private_data: false
---
# P12 - Fiche cours - Tris, invariants et complexité

## À savoir
- Capacités travaillées dans la fiche : P-ALGO-02A, P-ALGO-02B, P-ALGO-02C, P-ALGO-02D.
- La notion “tri simple” sert à réordonner selon une relation.
- Le vocabulaire de tris doit être employé avec des données concrètes propres au chapitre P12.
- La capacité associée à tris se travaille par lecture, manipulation et justification dans P12.
- Une réponse sur tris distingue la situation étudiée, la méthode choisie, le résultat et le contrôle.

## Méthodes
1. formuler l’invariant de la partie déjà triée.
2. Écrire un exemple minimal de tris avant de traiter le cas général du chapitre P12.
3. Identifier le cas limite de tris qui peut faire échouer la méthode.
4. Relier la conclusion de tris à une opération ou une propriété observable.

## Exemples corrigés
### Exemple corrigé 1
insertion de 3 dans [1,4] donne [1,3,4].
### Exemple corrigé 2
On reprend le premier exemple avec une donnée différente et on contrôle explicitement la conclusion pour tris.

## Erreurs fréquentes
- un tri n’est pas seulement une recherche de minimum : corriger avec un contre-exemple court.
- Donner seulement le résultat en tris : ajouter une ligne qui nomme la méthode utilisée.
- Oublier le cas limite de tris : le tester avant d’écrire la conclusion.

## Cas limites
- Cas vide ou minimal pour tri simple.
- Donnée invalide ou absente dans une situation de tris.
- Situation de tris où deux réponses semblent possibles et exigent une convention explicite.

## Mini-exercices
### Mini-exercice 1
Définir tri simple en une phrase précise.
### Mini-exercice 2
Appliquer la méthode à un petit exemple de tri simple.
### Mini-exercice 3
Repérer une erreur fréquente dans une réponse proposée sur tris.
### Mini-exercice 4
Citer le cas limite à vérifier en priorité pour tris.

## Réponses rapides
1. tri simple doit être défini avec son rôle, pas seulement son nom.
2. La réponse sur tris doit montrer les étapes utiles.
3. L’erreur de tris se repère en testant l’hypothèse oubliée.
4. Le cas vide ou minimal est souvent le premier contrôle pour tris.

## À retenir
- Pour tris, commencer par reconnaître la situation exacte.
- Une méthode de P12 doit être accompagnée d’un exemple numérique ou textuel.
- Les capacités P-ALGO-02A, P-ALGO-02B, P-ALGO-02C, P-ALGO-02D restent au statut de travail tant que la revue humaine manque.
- La fiche prépare la révision de tris sans produire à elle seule une preuve de couverture annuelle.
- Un cas limite explicite est obligatoire avant toute conclusion sur tris.

## Lien avec la progression
- Séances : P12-S1 et P12-S2 lorsque le chapitre est découpé en plusieurs temps.
- TD lié : P12_TD_tris.md, à produire ou relire dans le registre de supports.
- TP lié : P12_TP_tris.py si la progression prévoit une manipulation programmée.
- Évaluation ou projet lié : contrôle court du chapitre P12 ou livrable associé.
- Dossier de progression : 03_progressions/fiches_cours/premiere/P12/.

## Auto-évaluation
- Je sais expliquer tris sans lire la fiche.
- Je sais refaire les exemples de P12 avec des données différentes.
- Je sais identifier l’erreur fréquente la plus probable pour tris.
- Je sais choisir un cas limite de tris avant de répondre.
- Je sais relier la fiche P12 sur tris à une séance, un TD ou un TP du chapitre.
