---
title: "P02 - Fiche cours - Complément à deux"
level: "premiere"
sequence_id: "P02"
document_type: "fiche_cours"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Représentation machine"
notion: "complément à deux"
official_program:
  capacities:
    - "P-DATA-BASE-02A"
    - "P-DATA-BASE-02B"
private_data: false
---
# P02 - Fiche cours - Complément à deux

## À savoir
- Capacités travaillées dans la fiche : P-DATA-BASE-02A, P-DATA-BASE-02B.
- Le complément à deux représente des entiers relatifs sur une taille fixée.
- Sur n bits, la plage est de -2^(n-1) à 2^(n-1)-1.
- Le bit de poids fort indique une valeur négative quand il vaut 1.
- La même écriture binaire peut changer de sens si la taille ou la convention change.

## Méthodes
1. Écrire d’abord la taille du registre.
2. Pour coder -x, coder x, inverser les bits puis ajouter 1.
3. Pour décoder un mot négatif, soustraire 2^n à sa valeur non signée.
4. Tester un dépassement après addition de deux nombres de même signe.

## Exemples corrigés
### Exemple corrigé 1
Sur 4 bits, -6 : 0110, inversion 1001, ajout 1, donc 1010.
### Exemple corrigé 2
1101 sur 4 bits vaut 13 - 16 = -3.

## Erreurs fréquentes
- Oublier la taille : toujours écrire “sur 4 bits” ou “sur 8 bits”.
- Garder une retenue hors registre : supprimer ce qui dépasse n bits.
- Croire que +8 existe sur 4 bits signés : rappeler la borne +7.

## Cas limites
- Sur 4 bits, -8 existe et +8 n’existe pas.
- 0000 code 0, sans double zéro négatif.
- 7 + 1 déborde sur 4 bits signés.

## Mini-exercices
### Mini-exercice 1
Donner la plage sur 5 bits.
### Mini-exercice 2
Coder -5 sur 4 bits.
### Mini-exercice 3
Décoder 1001 sur 4 bits.
### Mini-exercice 4
Dire si 6 + 3 tient sur 4 bits signés.

## Réponses rapides
1. De -16 à 15.
2. 1011.
3. 1001 vaut -7.
4. Non, 9 dépasse +7.

## À retenir
- Pour complément à deux, commencer par reconnaître la situation exacte.
- Une méthode de P02 doit être accompagnée d’un exemple numérique ou textuel.
- Les capacités P-DATA-BASE-02A, P-DATA-BASE-02B restent au statut de travail tant que la revue humaine manque.
- La fiche prépare la révision de complément à deux sans produire à elle seule une preuve de couverture annuelle.
- Un cas limite explicite est obligatoire avant toute conclusion sur complement_a_deux.

## Lien avec la progression
- Séances : P02-S1 et P02-S2 lorsque le chapitre est découpé en plusieurs temps.
- TD lié : P02_TD_complement_a_deux.md, à produire ou relire dans le registre de supports.
- TP lié : P02_TP_complement_a_deux.py si la progression prévoit une manipulation programmée.
- Évaluation ou projet lié : contrôle court du chapitre P02 ou livrable associé.
- Dossier de progression : 03_progressions/fiches_cours/premiere/P02/.

## Auto-évaluation
- Je sais expliquer complément à deux sans lire la fiche.
- Je sais refaire les exemples de P02 avec des données différentes.
- Je sais identifier l’erreur fréquente la plus probable pour complément à deux.
- Je sais choisir un cas limite de complément à deux avant de répondre.
- Je sais relier la fiche P02 sur complément à deux à une séance, un TD ou un TP du chapitre.
