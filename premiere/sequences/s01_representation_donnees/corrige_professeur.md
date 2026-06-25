---
title: "Corrigé professeur - représentation des données"
niveau: premiere
source: "Prototype interne"
status: needs_review
version: "0.4.0"
notion: "corrigé professeur"
objectifs: "Document professeur substantiel à relire avant usage."
sequence: s01_representation_donnees
private_data: false
---

# Corrigé professeur - représentation des données

## Statut

Document professeur uniquement. Il reste en `needs_review` et ne doit pas être exporté dans une version élève.

## Méthode de correction

Chaque exercice est corrigé selon huit éléments : réponse attendue, justification, barème, variante acceptable, erreurs fréquentes, remédiation, critère de réussite et capacité officielle associée.

## Exercice 1 - Conversion base 2/10/16

- Capacité officielle associée : P-DATA-BASE-01.
- Réponse attendue : 45 = 32 + 8 + 4 + 1, donc 101101 en base 2 et 2D en base 16..
- Justification : La décomposition en puissances de 2 permet de contrôler les bits à 1..
- Barème question par question : 1 pt décomposition, 1 pt binaire, 1 pt hexadécimal, 1 pt justification..
- Variante acceptable : Conversion par divisions successives acceptée si les restes sont dans le bon ordre..
- Erreurs fréquentes : Lire les restes dans le mauvais sens ou confondre 13 et D..
- Remédiation : Reprendre avec 13 puis 45 et faire grouper les bits par paquets de quatre..
- Critère de réussite : La valeur convertie reste la même dans les trois écritures..

## Exercice 2 - Complément à deux

- Capacité officielle associée : P-DATA-BASE-02BB.
- Réponse attendue : 3 vaut 0011 ; inversion 1100 ; ajout de 1 : 1101..
- Justification : Sur 4 bits, 1101 représente -3 car 13 - 16 = -3..
- Barème question par question : 1 pt positif, 1 pt inversion, 1 pt ajout, 1 pt vérification..
- Variante acceptable : Méthode par 16 - 3 = 13 acceptée..
- Erreurs fréquentes : Oublier la taille fixe ou obtenir 101 sans compléter à 4 bits..
- Remédiation : Faire écrire toute la table des valeurs de -8 à 7..
- Critère de réussite : L’élève vérifie la valeur représentée..

## Exercice 3 - Booléens

- Capacité officielle associée : P-DATA-BASE-04.
- Réponse attendue : La seule ligne fausse est A vrai et B faux..
- Justification : non A ou B correspond à une implication A vers B..
- Barème question par question : 1 pt colonnes, 1 pt non A, 1 pt résultat, 1 pt phrase..
- Variante acceptable : Table avec 0/1 acceptée si la correspondance est claire..
- Erreurs fréquentes : Appliquer la négation à toute l’expression..
- Remédiation : Séparer sous-expression puis expression finale..
- Critère de réussite : Les quatre lignes sont traitées..

## Exercice 4 - Texte Unicode

- Capacité officielle associée : P-DATA-BASE-05AA.
- Réponse attendue : Unicode définit des points de code ; l’encodage choisi décrit comment les stocker en octets..
- Justification : La distinction caractère, point de code et octets évite les confusions..
- Barème question par question : 1 pt Unicode, 1 pt encodage, 1 pt exemple, 1 pt limite..
- Variante acceptable : Exemple avec un caractère non latin accepté..
- Erreurs fréquentes : Dire que Unicode est seulement une police..
- Remédiation : Comparer caractère affiché et suite d’octets..
- Critère de réussite : L’élève distingue symbole et représentation..

## Exercice 5 - Tests Python

- Capacité officielle associée : P-LANG-04.
- Réponse attendue : Tester zéro et une valeur avec lettre hexadécimale, par exemple 0 et 45..
- Justification : Les tests doivent couvrir cas simple et cas limite ou ambigu..
- Barème question par question : 1 pt cas standard, 1 pt cas limite, 1 pt résultat attendu, 1 pt justification..
- Variante acceptable : Un test d’erreur sur chiffre invalide est accepté..
- Erreurs fréquentes : Tester seulement des valeurs déjà vues sans résultat attendu..
- Remédiation : Faire écrire entrée, sortie attendue, raison du test..
- Critère de réussite : Chaque test peut être exécuté et interprété..

## Décision

Le corrigé n'est pas publié. Une revue pédagogique et scientifique reste nécessaire avant utilisation large.
