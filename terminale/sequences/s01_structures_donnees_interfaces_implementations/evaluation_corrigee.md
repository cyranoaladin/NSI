---
title: "Évaluation corrigée - structures de données"
niveau: terminale
source: "Prototype interne"
status: needs_review
version: "0.4.0"
notion: "évaluation corrigée"
objectifs: "Document professeur substantiel à relire avant usage."
sequence: s01_structures_donnees_interfaces_implementations
private_data: false
---

# Évaluation corrigée - structures de données

## Conditions

- Durée : 55 minutes, ou 75 minutes pour la version aménagée.
- Matériel autorisé : fiche rappel fournie par le professeur, sans corrigé.
- Compétences évaluées : comprendre, appliquer, programmer ou analyser, justifier, communiquer.
- Document professeur uniquement : ne pas exporter vers les élèves.

## Correction complète et barème

### Question 1

- Énoncé professeur : Décris l’interface minimale d’une file..
- Correction : Une file fournit créer, enfiler, défiler, tester si vide, éventuellement consulter le premier..
- Justification attendue : L’interface décrit les opérations visibles sans imposer la représentation interne..
- Barème : 1 pt opérations, 1 pt FIFO, 1 pt abstraction, 1 pt vocabulaire..
- Erreur à surveiller : Décrire une liste Python au lieu de l’interface..
- Remédiation après correction : Cacher l’implémentation et raisonner seulement sur les opérations..

### Question 2

- Énoncé professeur : Écris le début d’une classe Pile avec un attribut interne..
- Correction : Une classe initialise par exemple self._donnees = [] et expose empiler/depiler..
- Justification attendue : La classe regroupe état et méthodes ; l’attribut interne n’est pas l’interface..
- Barème : 1 pt __init__, 1 pt attribut, 1 pt méthode, 1 pt cas vide..
- Erreur à surveiller : Utiliser une variable globale..
- Remédiation après correction : Tracer deux objets distincts et leurs états..

### Question 3

- Énoncé professeur : Choisis pile, file ou dictionnaire pour retrouver rapidement un élève fictif par identifiant..
- Correction : Un dictionnaire convient si l’identifiant est la clé..
- Justification attendue : L’accès par clé correspond au besoin ; pile et file imposent un ordre de retrait..
- Barème : 1 pt choix, 1 pt justification, 1 pt contre-exemple, 1 pt limite..
- Erreur à surveiller : Choisir une file car les données arrivent dans un ordre..
- Remédiation après correction : Faire lister les opérations dominantes..

### Question 4

- Énoncé professeur : Modélise trois villes et deux routes par un graphe..
- Correction : Les villes sont sommets, les routes sont arêtes ; la représentation peut être liste ou matrice..
- Justification attendue : Un graphe modélise des relations entre objets..
- Barème : 1 pt sommets, 1 pt arêtes, 1 pt orientation ou non, 1 pt représentation..
- Erreur à surveiller : Confondre arête et sommet..
- Remédiation après correction : Faire dessiner puis traduire en liste..

### Question 5

- Énoncé professeur : Explique le rôle d’une file dans un parcours en largeur..
- Correction : La file conserve les sommets découverts dans l’ordre FIFO, ce qui visite par distance croissante en nombre d’arêtes..
- Justification attendue : BFS dépend de FIFO pour traiter les couches successives..
- Barème : 1 pt file, 1 pt FIFO, 1 pt sommets visités, 1 pt limite..
- Erreur à surveiller : Utiliser une pile et décrire DFS..
- Remédiation après correction : Comparer deux traces sur le même graphe..

## Version aménagée liée

La version aménagée est décrite dans `version_amenagee.md` et conserve les objectifs.

## Grille liée

La grille de compétences est décrite dans `grille_competences.md`.
