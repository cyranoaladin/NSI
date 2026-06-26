---
title: "P03 - Fiche cours - Texte, ASCII et Unicode"
level: "premiere"
sequence_id: "P03"
document_type: "fiche_cours"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Données textuelles"
notion: "Unicode"
official_program:
  capacities:
    - "P-DATA-BASE-05A"
    - "P-DATA-BASE-05B"
private_data: false
---
# P03 - Fiche cours - Texte, ASCII et Unicode

## À savoir
- Capacités travaillées dans la fiche : P-DATA-BASE-05A, P-DATA-BASE-05B.
- Un caractère est une unité de texte, distincte des octets stockés.
- Unicode attribue un point de code abstrait aux caractères.
- UTF-8 encode un point de code avec un à plusieurs octets.
- ASCII ne couvre que 128 caractères et ne suffit pas aux textes accentués ou multilingues.

## Méthodes
1. Séparer caractère, point de code et octets.
2. Utiliser `ord` pour observer un point de code.
3. Utiliser `.encode("utf-8")` pour observer les octets.
4. Préciser l’encodage lors de la lecture et de l’écriture de fichiers.

## Exemples corrigés
### Exemple corrigé 1
`ord("A")` vaut 65 alors que `ord("é")` vaut 233.
### Exemple corrigé 2
`"é".encode("utf-8")` produit C3 A9, donc deux octets.

## Erreurs fréquentes
- Confondre longueur de chaîne et nombre d’octets : comparer `len(s)` et `len(s.encode())`.
- Ouvrir un fichier avec l’encodage implicite : écrire `encoding="utf-8"`.
- Présenter Unicode comme un fichier : distinguer répertoire et encodage.

## Cas limites
- La chaîne vide contient zéro caractère.
- Un accent peut occuper deux octets en UTF-8.
- Un octet invalide peut provoquer une erreur de décodage.

## Mini-exercices
### Mini-exercice 1
Donner le point de code de `A`.
### Mini-exercice 2
Dire combien d’octets UTF-8 contient `Aé`.
### Mini-exercice 3
Expliquer l’affichage `Ã©`.
### Mini-exercice 4
Écrire l’ouverture UTF-8 d’un fichier.

## Réponses rapides
1. `A` a le point de code 65.
2. `Aé` contient trois octets.
3. Les octets UTF-8 ont été lus avec un mauvais encodage.
4. `open(nom, encoding="utf-8")`.

## À retenir
- Pour Unicode, commencer par reconnaître la situation exacte.
- Une méthode de P03 doit être accompagnée d’un exemple numérique ou textuel.
- Les capacités P-DATA-BASE-05A, P-DATA-BASE-05B restent au statut de travail tant que la revue humaine manque.
- La fiche prépare la révision de Unicode sans produire à elle seule une preuve de couverture annuelle.
- Un cas limite explicite est obligatoire avant toute conclusion sur Unicode.

## Lien avec la progression
- Séances : P03-S1 et P03-S2 lorsque le chapitre est découpé en plusieurs temps.
- TD lié : P03_TD_Unicode.md, à produire ou relire dans le registre de supports.
- TP lié : P03_TP_Unicode.py si la progression prévoit une manipulation programmée.
- Évaluation ou projet lié : contrôle court du chapitre P03 ou livrable associé.
- Dossier de progression : 03_progressions/fiches_cours/premiere/P03/.

## Auto-évaluation
- Je sais expliquer Unicode sans lire la fiche.
- Je sais refaire les exemples de P03 avec des données différentes.
- Je sais identifier l’erreur fréquente la plus probable pour Unicode.
- Je sais choisir un cas limite de Unicode avant de répondre.
- Je sais relier la fiche P03 sur Unicode à une séance, un TD ou un TP du chapitre.
