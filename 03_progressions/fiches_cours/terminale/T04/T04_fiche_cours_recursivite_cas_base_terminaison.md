---
title: "T04 - Fiche cours - Récursivité, cas de base et terminaison"
level: "terminale"
sequence_id: "T04"
document_type: "fiche_cours"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Récursivité"
notion: "récursivité"
official_program:
  capacities:
    - "T-LANG-02A"
    - "T-LANG-02B"
private_data: false
---
# T04 - Fiche cours - Récursivité, cas de base et terminaison

## À savoir
- Capacités travaillées dans la fiche : T-LANG-02A, T-LANG-02B.
- La notion “récursivité” sert à résoudre par appels plus petits.
- Le vocabulaire de récursivité doit être employé avec des données concrètes propres au chapitre T04.
- La capacité associée à récursivité se travaille par lecture, manipulation et justification dans T04.
- Une réponse sur récursivité distingue la situation étudiée, la méthode choisie, le résultat et le contrôle.

## Méthodes
1. écrire cas de base et diminution.
2. Écrire un exemple minimal de récursivité avant de traiter le cas général du chapitre T04.
3. Identifier le cas limite de récursivité qui peut faire échouer la méthode.
4. Relier la conclusion de récursivité à une opération ou une propriété observable.

## Exemples corrigés
### Exemple corrigé 1
fact(3) appelle fact(2).
### Exemple corrigé 2
On change les données de l’exemple précédent et on vérifie que le raisonnement sur récursivité donne encore une conclusion contrôlable.

## Erreurs fréquentes
- un appel avec même argument ne termine pas : corriger avec un contre-exemple court.
- Donner seulement le résultat en récursivité : ajouter une ligne qui nomme la méthode utilisée.
- Oublier le cas limite de récursivité : le tester avant d’écrire la conclusion.

## Cas limites
- Cas vide ou minimal pour récursivité.
- Donnée invalide ou absente dans une situation de récursivité.
- Situation de récursivité où deux réponses semblent possibles et exigent une convention explicite.

## Mini-exercices
### Mini-exercice 1
Définir récursivité en une phrase précise.
### Mini-exercice 2
Appliquer la méthode à un petit exemple de récursivité.
### Mini-exercice 3
Repérer une erreur fréquente dans une réponse proposée sur récursivité.
### Mini-exercice 4
Citer le cas limite à vérifier en priorité pour récursivité.

## Réponses rapides
1. récursivité doit être défini avec son rôle, pas seulement son nom.
2. La réponse sur récursivité doit montrer les étapes utiles.
3. L’erreur de récursivité se repère en testant l’hypothèse oubliée.
4. Le cas vide ou minimal est souvent le premier contrôle pour récursivité.

## À retenir
- Pour récursivité, commencer par reconnaître la situation exacte.
- Une méthode de T04 doit être accompagnée d’un exemple numérique ou textuel.
- Les capacités T-LANG-02A, T-LANG-02B restent au statut de travail tant que la revue humaine manque.
- La fiche prépare la révision de récursivité sans produire à elle seule une preuve de couverture annuelle.
- Un cas limite explicite est obligatoire avant toute conclusion sur recursivite.

## Lien avec la progression
- Séances : T04-S1 et T04-S2 lorsque le chapitre est découpé en plusieurs temps.
- TD lié : T04_TD_recursivite.md, à produire ou relire dans le registre de supports.
- TP lié : T04_TP_recursivite.py si la progression prévoit une manipulation programmée.
- Évaluation ou projet lié : contrôle court du chapitre T04 ou livrable associé.
- Dossier de progression : 03_progressions/fiches_cours/terminale/T04/.

## Auto-évaluation
- Je sais expliquer récursivité sans lire la fiche.
- Je sais refaire les exemples de T04 avec des données différentes.
- Je sais identifier l’erreur fréquente la plus probable pour récursivité.
- Je sais choisir un cas limite de récursivité avant de répondre.
- Je sais relier la fiche T04 sur récursivité à une séance, un TD ou un TP du chapitre.
