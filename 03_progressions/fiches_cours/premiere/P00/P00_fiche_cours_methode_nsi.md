---
title: "P00 - Fiche cours - Méthode NSI, diagnostic et carnet de bord"
level: "premiere"
sequence_id: "P00"
document_type: "fiche_cours"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Rentrée et méthode"
notion: "méthode NSI"
official_program:
  capacities:
    - "P-HIST-01"
    - "P-LANG-01"
private_data: false
---
# P00 - Fiche cours - Méthode NSI, diagnostic et carnet de bord

## À savoir
- Capacités travaillées dans la fiche : P-HIST-01, P-LANG-01.
- La NSI demande de relier une idée, un programme et une preuve par l’exemple.
- Un test décrit une entrée, un résultat attendu et le comportement réellement observé.
- Une trace de variables permet de comprendre une boucle avant de modifier le code.
- Un repère historique explique pourquoi une technique informatique a été inventée.

## Méthodes
1. Écrire les entrées et sorties avant le programme.
2. Tracer au moins un exemple court à la main.
3. Tester un cas normal, un cas limite et un cas refusé.
4. Conserver dans le carnet de bord la cause d’une erreur corrigée.

## Exemples corrigés
### Exemple corrigé 1
Pour `s = 0` puis `for x in [2, 5, 1]: s = s + x`, la trace donne 2, 7, 8.
### Exemple corrigé 2
Pour `est_pair`, les tests 0, 7 et -4 couvrent zéro, impair et entier négatif autorisé.

## Erreurs fréquentes
- Coder sans exemple préalable : imposer un exemple papier avant le clavier.
- Confondre syntaxe et logique : lire le message Python puis comparer avec l’attendu.
- Corriger trois lignes à la fois : relancer un test après chaque modification ciblée.

## Cas limites
- Liste vide pour une fonction de parcours.
- Variable non initialisée avant une boucle.
- Donnée personnelle à remplacer par une donnée fictive.

## Mini-exercices
### Mini-exercice 1
Tracer la valeur de `s` dans une boucle de somme.
### Mini-exercice 2
Proposer trois tests pour `est_pair(n)`.
### Mini-exercice 3
Associer machine programmable, réseau et langage à un besoin.
### Mini-exercice 4
Expliquer pourquoi une donnée réelle d’élève est interdite dans un support.

## Réponses rapides
1. La somme évolue selon les valeurs rencontrées.
2. 0 vrai, 7 faux, -4 vrai si les négatifs sont acceptés.
3. Calculer automatiquement, échanger, décrire une procédure.
4. Elle peut identifier une personne et bloque la publication.

## À retenir
- Pour méthode NSI, commencer par reconnaître la situation exacte.
- Une méthode de P00 doit être accompagnée d’un exemple numérique ou textuel.
- Les capacités P-HIST-01, P-LANG-01 restent au statut de travail tant que la revue humaine manque.
- La fiche prépare la révision de méthode NSI sans produire à elle seule une preuve de couverture annuelle.
- Un cas limite explicite est obligatoire avant toute conclusion sur methode_NSI.

## Lien avec la progression
- Séances : P00-S1 et P00-S2 lorsque le chapitre est découpé en plusieurs temps.
- TD lié : P00_TD_methode_NSI.md, à produire ou relire dans le registre de supports.
- TP lié : P00_TP_methode_NSI.py si la progression prévoit une manipulation programmée.
- Évaluation ou projet lié : contrôle court du chapitre P00 ou livrable associé.
- Dossier de progression : 03_progressions/fiches_cours/premiere/P00/.

## Auto-évaluation
- Je sais expliquer méthode NSI sans lire la fiche.
- Je sais refaire les exemples de P00 avec des données différentes.
- Je sais identifier l’erreur fréquente la plus probable pour méthode NSI.
- Je sais choisir un cas limite de méthode NSI avant de répondre.
- Je sais relier la fiche P00 sur méthode NSI à une séance, un TD ou un TP du chapitre.
