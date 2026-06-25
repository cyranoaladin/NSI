---
title: "Évaluation corrigée - représentation des données"
niveau: premiere
source: "Prototype interne"
status: needs_review
version: "0.5.0"
notion: "évaluation corrigée"
objectifs: "Document professeur exploitable en prototype, à relire avant usage."
sequence: s01_representation_donnees
private_data: false
---

# Évaluation corrigée - représentation des données

**Document professeur uniquement.** Durée standard : 55 minutes. Matériel : fiche rappel sans corrigé.

## Sujet corrigé

### Question 1

- Énoncé : Convertis 45 en base 2 puis en base 16.
- Correction complète : 45 = 101101 en base 2 et 2D en base 16.
- Justification attendue : Décomposition en puissances de deux puis groupement par quatre bits.
- Barème : 2.5 points.
- Erreur fréquente à surveiller : restes lus dans le mauvais ordre
- Remédiation : reprendre un exemple à deux chiffres puis vérifier en base 10

### Question 2

- Énoncé : Combien de bits faut-il pour écrire 255 puis 256 ?
- Correction complète : 255 nécessite 8 bits ; 256 nécessite 9 bits.
- Justification attendue : 8 bits codent de 0 à 255, donc 256 dépasse cette plage.
- Barème : 2.5 points.
- Erreur fréquente à surveiller : confondre nombre de valeurs et plus grande valeur
- Remédiation : faire écrire les intervalles 0..2^n-1

### Question 3

- Énoncé : Encode -3 sur 4 bits.
- Correction complète : 1101.
- Justification attendue : 3 vaut 0011, inversion 1100, ajout de 1 : 1101.
- Barème : 2.5 points.
- Erreur fréquente à surveiller : oublier la taille fixe
- Remédiation : dresser la table sur 4 bits

### Question 4

- Énoncé : Dresse la table de vérité de non A ou B.
- Correction complète : Seule la ligne A vrai et B faux est fausse.
- Justification attendue : La négation porte seulement sur A.
- Barème : 2.5 points.
- Erreur fréquente à surveiller : nier toute l’expression
- Remédiation : séparer les colonnes A, B, non A, résultat

### Question 5

- Énoncé : Explique l’intérêt d’Unicode.
- Correction complète : Unicode fournit un répertoire commun de caractères au-delà d’ASCII.
- Justification attendue : Il évite de limiter les textes aux caractères latins simples.
- Barème : 2.5 points.
- Erreur fréquente à surveiller : confondre caractère et police
- Remédiation : comparer symbole affiché et code stocké

### Question 6

- Énoncé : Écris une fonction renvoyant quotient et reste.
- Correction complète : Une fonction peut retourner `(q, r)`.
- Justification attendue : Un p-uplet regroupe plusieurs valeurs de retour.
- Barème : 2.5 points.
- Erreur fréquente à surveiller : modifier une variable globale
- Remédiation : faire tracer entrée et sortie

### Question 7

- Énoncé : Corrige une erreur d’indice dans une liste de trois valeurs.
- Correction complète : Les indices valides sont 0, 1 et 2.
- Justification attendue : L’indexation Python commence à zéro.
- Barème : 2.5 points.
- Erreur fréquente à surveiller : utiliser l’indice 3
- Remédiation : dessiner cases et indices

### Question 8

- Énoncé : Propose deux tests pour une fonction de conversion.
- Correction complète : Tester 0 et une valeur avec lettre hexadécimale, par exemple 45.
- Justification attendue : Les tests couvrent cas limite et cas standard.
- Barème : 2.5 points.
- Erreur fréquente à surveiller : donner une entrée sans sortie attendue
- Remédiation : imposer entrée, sortie, raison

