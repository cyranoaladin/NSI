---
title: "P01 - Fiche cours - Conversions entre bases"
level: "premiere"
sequence_id: "P01"
document_type: "fiche_cours"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Représentation des entiers"
notion: "conversions"
official_program:
  capacities:
    - "P-DATA-BASE-01"
private_data: false
---
# P01 - Fiche cours - Conversions entre bases

## À savoir
- Capacités travaillées dans la fiche : P-DATA-BASE-01.
- Convertir change l’écriture d’un entier sans changer sa valeur.
- Les divisions successives donnent les chiffres du dernier reste vers le premier.
- La lecture positionnelle additionne les poids des bits actifs.
- Un contrôle inverse permet de repérer une erreur d’ordre ou de reste.

## Méthodes
1. Diviser par la base et noter quotient et reste dans deux colonnes.
2. Lire les restes du bas vers le haut.
3. Pour le binaire vers décimal, additionner seulement les poids associés à 1.
4. Reconvertir le résultat pour vérifier la valeur obtenue.

## Exemples corrigés
### Exemple corrigé 1
45 / 2 donne les restes 1, 0, 1, 1, 0, 1 ; lus à l’envers : 101101₂.
### Exemple corrigé 2
2D₁₆ vaut 2×16 + 13 = 45₁₀.

## Erreurs fréquentes
- Lire les restes dans l’ordre du calcul : flécher la remontée.
- Confondre quotient et reste : séparer les colonnes.
- Écrire 13 comme chiffre hexadécimal : remplacer par D.

## Cas limites
- La conversion de 0 s’arrête immédiatement.
- 64 donne 1000000₂ avec un seul bit actif.
- 63 donne 111111₂, juste avant une puissance de deux.

## Mini-exercices
### Mini-exercice 1
Convertir 19₁₀ en binaire.
### Mini-exercice 2
Convertir 100110₂ en décimal.
### Mini-exercice 3
Convertir 7B₁₆ en décimal.
### Mini-exercice 4
Vérifier que 11111₂ vaut 31.

## Réponses rapides
1. 19₁₀ = 10011₂.
2. 100110₂ = 38.
3. 7B₁₆ = 123.
4. 16 + 8 + 4 + 2 + 1 = 31.

## À retenir
- Pour conversions, commencer par reconnaître la situation exacte.
- Une méthode de P01 doit être accompagnée d’un exemple numérique ou textuel.
- Les capacités P-DATA-BASE-01 restent au statut de travail tant que la revue humaine manque.
- La fiche prépare la révision de conversions sans produire à elle seule une preuve de couverture annuelle.
- Un cas limite explicite est obligatoire avant toute conclusion sur conversions.

## Lien avec la progression
- Séances : P01-S1 et P01-S2 lorsque le chapitre est découpé en plusieurs temps.
- TD lié : P01_TD_conversions.md, à produire ou relire dans le registre de supports.
- TP lié : P01_TP_conversions.py si la progression prévoit une manipulation programmée.
- Évaluation ou projet lié : contrôle court du chapitre P01 ou livrable associé.
- Dossier de progression : 03_progressions/fiches_cours/premiere/P01/.

## Auto-évaluation
- Je sais expliquer conversions sans lire la fiche.
- Je sais refaire les exemples de P01 avec des données différentes.
- Je sais identifier l’erreur fréquente la plus probable pour conversions.
- Je sais choisir un cas limite de conversions avant de répondre.
- Je sais relier la fiche P01 sur conversions à une séance, un TD ou un TP du chapitre.
