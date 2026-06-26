---
title: "P02 - Fiche cours - Booléens et tables de vérité"
level: "premiere"
sequence_id: "P02"
document_type: "fiche_cours"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Représentation machine"
notion: "booléens"
official_program:
  capacities:
    - "P-DATA-BASE-04"
private_data: false
---
# P02 - Fiche cours - Booléens et tables de vérité

## À savoir
- Capacités travaillées dans la fiche : P-DATA-BASE-04.
- Un booléen vaut vrai ou faux.
- `and`, `or` et `not` construisent des expressions logiques.
- Une table de vérité énumère toutes les valeurs possibles des variables.
- Deux expressions sont équivalentes si leurs colonnes finales coïncident.

## Méthodes
1. Lister les variables puis prévoir 2^n lignes.
2. Calculer les sous-expressions dans des colonnes intermédiaires.
3. Appliquer `not` avant `and`, puis `or`, sauf parenthèses.
4. Comparer les colonnes finales pour justifier une simplification.

## Exemples corrigés
### Exemple corrigé 1
`a and not b` est vrai seulement si a est vrai et b faux.
### Exemple corrigé 2
`(a and b) or (a and not b)` a la même table finale que `a`.

## Erreurs fréquentes
- Oublier une combinaison : recompter les 2^n lignes.
- Appliquer `not` à une expression trop large : ajouter des parenthèses.
- Confondre `or` inclusif et exclusif : tester le cas vrai/vrai.

## Cas limites
- Avec trois variables, la table contient huit lignes.
- Une expression constante peut ne dépendre d’aucune variable.
- Une comparaison Python comme `x < 3` produit un booléen.

## Mini-exercices
### Mini-exercice 1
Dresser la table de `a or b`.
### Mini-exercice 2
Évaluer `not True and False`.
### Mini-exercice 3
Tester la loi `not(a and b)` sur deux lignes.
### Mini-exercice 4
Calculer `5 > 2 and 2 == 3`.

## Réponses rapides
1. `a or b` est faux seulement pour faux/faux.
2. Le résultat est False.
3. Elle correspond à `not a or not b`.
4. Le résultat est False.

## À retenir
- Pour booléens, commencer par reconnaître la situation exacte.
- Une méthode de P02 doit être accompagnée d’un exemple numérique ou textuel.
- Les capacités P-DATA-BASE-04 restent au statut de travail tant que la revue humaine manque.
- La fiche prépare la révision de booléens sans produire à elle seule une preuve de couverture annuelle.
- Un cas limite explicite est obligatoire avant toute conclusion sur booleens.

## Lien avec la progression
- Séances : P02-S1 et P02-S2 lorsque le chapitre est découpé en plusieurs temps.
- TD lié : P02_TD_booleens.md, à produire ou relire dans le registre de supports.
- TP lié : P02_TP_booleens.py si la progression prévoit une manipulation programmée.
- Évaluation ou projet lié : contrôle court du chapitre P02 ou livrable associé.
- Dossier de progression : 03_progressions/fiches_cours/premiere/P02/.

## Auto-évaluation
- Je sais expliquer booléens sans lire la fiche.
- Je sais refaire les exemples de P02 avec des données différentes.
- Je sais identifier l’erreur fréquente la plus probable pour booléens.
- Je sais choisir un cas limite de booléens avant de répondre.
- Je sais relier la fiche P02 sur booléens à une séance, un TD ou un TP du chapitre.
