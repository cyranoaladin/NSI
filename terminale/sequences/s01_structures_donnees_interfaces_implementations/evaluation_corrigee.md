---
title: "Évaluation corrigée - structures de données"
niveau: terminale
source: "Prototype interne"
status: needs_review
version: "0.5.0"
notion: "évaluation corrigée"
objectifs: "Document professeur exploitable en prototype, à relire avant usage."
sequence: s01_structures_donnees_interfaces_implementations
private_data: false
---

# Évaluation corrigée - structures de données

**Document professeur uniquement.** Durée standard : 55 minutes. Matériel : fiche rappel sans corrigé.

## Sujet corrigé

### Question 1

- Énoncé : Décris l’interface minimale d’une file.
- Correction complète : créer, enfiler, défiler, est_vide, éventuellement premier.
- Justification attendue : L’interface liste les opérations visibles.
- Barème : 2.5 points.
- Erreur fréquente à surveiller : décrire la liste interne
- Remédiation : cacher l’implémentation et ne garder que les opérations

### Question 2

- Énoncé : Explique interface vs implémentation.
- Correction complète : L’interface décrit quoi faire ; l’implémentation décrit comment c’est stocké.
- Justification attendue : Deux implémentations peuvent partager la même interface.
- Barème : 2.5 points.
- Erreur fréquente à surveiller : assimiler interface à classe Python
- Remédiation : comparer deux codes avec mêmes méthodes

### Question 3

- Énoncé : Écris le squelette d’une classe Pile.
- Correction complète : `__init__` initialise un attribut, puis méthodes empiler/depiler.
- Justification attendue : La classe regroupe état et opérations.
- Barème : 2.5 points.
- Erreur fréquente à surveiller : utiliser une variable globale
- Remédiation : créer deux piles et tracer les états

### Question 4

- Énoncé : Choisis une structure pour retrouver par clé.
- Correction complète : Un dictionnaire convient.
- Justification attendue : La recherche se fait par clé.
- Barème : 2.5 points.
- Erreur fréquente à surveiller : choisir une file par ordre d’arrivée
- Remédiation : lister les opérations dominantes

### Question 5

- Énoncé : Compare recherche dans liste et dictionnaire.
- Correction complète : Liste : parcours ; dictionnaire : accès par clé.
- Justification attendue : Les opérations caractéristiques diffèrent.
- Barème : 2.5 points.
- Erreur fréquente à surveiller : chercher une valeur comme une clé
- Remédiation : faire écrire clé -> valeur

### Question 6

- Énoncé : Modélise villes et routes.
- Correction complète : Villes = sommets, routes = arêtes.
- Justification attendue : Le graphe représente des relations.
- Barème : 2.5 points.
- Erreur fréquente à surveiller : confondre sommet et arête
- Remédiation : dessiner puis convertir

### Question 7

- Énoncé : Explique une matrice d’adjacence.
- Correction complète : Case i,j indique présence d’une arête.
- Justification attendue : La matrice encode toutes les paires de sommets.
- Barème : 2.5 points.
- Erreur fréquente à surveiller : matrice non carrée
- Remédiation : repartir de la liste des sommets

### Question 8

- Énoncé : Pourquoi BFS utilise une file ?
- Correction complète : La file traite les sommets découverts en FIFO.
- Justification attendue : Cela visite par couches de distance.
- Barème : 2.5 points.
- Erreur fréquente à surveiller : utiliser une pile et décrire DFS
- Remédiation : comparer pile et file sur le même graphe

