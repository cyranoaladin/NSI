---
title: "Évaluation corrigée - représentation des données"
niveau: premiere
source: "Prototype interne"
status: needs_review
version: "0.4.0"
notion: "évaluation corrigée"
objectifs: "Document professeur substantiel à relire avant usage."
sequence: s01_representation_donnees
private_data: false
---

# Évaluation corrigée - représentation des données

## Conditions

- Durée : 55 minutes, ou 75 minutes pour la version aménagée.
- Matériel autorisé : fiche rappel fournie par le professeur, sans corrigé.
- Compétences évaluées : comprendre, appliquer, programmer ou analyser, justifier, communiquer.
- Document professeur uniquement : ne pas exporter vers les élèves.

## Correction complète et barème

### Question 1

- Énoncé professeur : Convertis 45 en base 2 puis en base 16 en indiquant les étapes..
- Correction : 45 = 32 + 8 + 4 + 1, donc 101101 en base 2 et 2D en base 16..
- Justification attendue : La décomposition en puissances de 2 permet de contrôler les bits à 1..
- Barème : 1 pt décomposition, 1 pt binaire, 1 pt hexadécimal, 1 pt justification..
- Erreur à surveiller : Lire les restes dans le mauvais sens ou confondre 13 et D..
- Remédiation après correction : Reprendre avec 13 puis 45 et faire grouper les bits par paquets de quatre..

### Question 2

- Énoncé professeur : Encode -3 sur 4 bits en complément à deux..
- Correction : 3 vaut 0011 ; inversion 1100 ; ajout de 1 : 1101..
- Justification attendue : Sur 4 bits, 1101 représente -3 car 13 - 16 = -3..
- Barème : 1 pt positif, 1 pt inversion, 1 pt ajout, 1 pt vérification..
- Erreur à surveiller : Oublier la taille fixe ou obtenir 101 sans compléter à 4 bits..
- Remédiation après correction : Faire écrire toute la table des valeurs de -8 à 7..

### Question 3

- Énoncé professeur : Dresse la table de vérité de non A ou B..
- Correction : La seule ligne fausse est A vrai et B faux..
- Justification attendue : non A ou B correspond à une implication A vers B..
- Barème : 1 pt colonnes, 1 pt non A, 1 pt résultat, 1 pt phrase..
- Erreur à surveiller : Appliquer la négation à toute l’expression..
- Remédiation après correction : Séparer sous-expression puis expression finale..

### Question 4

- Énoncé professeur : Explique pourquoi un caractère accentué peut occuper plus d’un octet selon l’encodage..
- Correction : Unicode définit des points de code ; l’encodage choisi décrit comment les stocker en octets..
- Justification attendue : La distinction caractère, point de code et octets évite les confusions..
- Barème : 1 pt Unicode, 1 pt encodage, 1 pt exemple, 1 pt limite..
- Erreur à surveiller : Dire que Unicode est seulement une police..
- Remédiation après correction : Comparer caractère affiché et suite d’octets..

### Question 5

- Énoncé professeur : Propose deux tests pour une fonction de conversion de base..
- Correction : Tester zéro et une valeur avec lettre hexadécimale, par exemple 0 et 45..
- Justification attendue : Les tests doivent couvrir cas simple et cas limite ou ambigu..
- Barème : 1 pt cas standard, 1 pt cas limite, 1 pt résultat attendu, 1 pt justification..
- Erreur à surveiller : Tester seulement des valeurs déjà vues sans résultat attendu..
- Remédiation après correction : Faire écrire entrée, sortie attendue, raison du test..

## Version aménagée liée

La version aménagée est décrite dans `version_amenagee.md` et conserve les objectifs.

## Grille liée

La grille de compétences est décrite dans `grille_competences.md`.
