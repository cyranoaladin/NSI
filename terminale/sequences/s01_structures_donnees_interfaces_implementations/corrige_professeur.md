---
title: "Corrigé professeur - structures de données"
niveau: terminale
source: "Prototype interne"
status: needs_review
version: "0.4.0"
notion: "corrigé professeur"
objectifs: "Document professeur substantiel à relire avant usage."
sequence: s01_structures_donnees_interfaces_implementations
private_data: false
---

# Corrigé professeur - structures de données

## Statut

Document professeur uniquement. Il reste en `needs_review` et ne doit pas être exporté dans une version élève.

## Méthode de correction

Chaque exercice est corrigé selon huit éléments : réponse attendue, justification, barème, variante acceptable, erreurs fréquentes, remédiation, critère de réussite et capacité officielle associée.

## Exercice 1 - Interface de structure

- Capacité officielle associée : T-STRUCT-01A.
- Réponse attendue : Une file fournit créer, enfiler, défiler, tester si vide, éventuellement consulter le premier..
- Justification : L’interface décrit les opérations visibles sans imposer la représentation interne..
- Barème question par question : 1 pt opérations, 1 pt FIFO, 1 pt abstraction, 1 pt vocabulaire..
- Variante acceptable : Noms anglais acceptés si les rôles sont expliqués..
- Erreurs fréquentes : Décrire une liste Python au lieu de l’interface..
- Remédiation : Cacher l’implémentation et raisonner seulement sur les opérations..
- Critère de réussite : L’élève distingue usage et représentation..

## Exercice 2 - Classe Python

- Capacité officielle associée : T-STRUCT-02A.
- Réponse attendue : Une classe initialise par exemple self._donnees = [] et expose empiler/depiler..
- Justification : La classe regroupe état et méthodes ; l’attribut interne n’est pas l’interface..
- Barème question par question : 1 pt __init__, 1 pt attribut, 1 pt méthode, 1 pt cas vide..
- Variante acceptable : collections.deque accepté si justifié..
- Erreurs fréquentes : Utiliser une variable globale..
- Remédiation : Tracer deux objets distincts et leurs états..
- Critère de réussite : Deux piles peuvent évoluer séparément..

## Exercice 3 - Choix de structure

- Capacité officielle associée : T-STRUCT-03B.
- Réponse attendue : Un dictionnaire convient si l’identifiant est la clé..
- Justification : L’accès par clé correspond au besoin ; pile et file imposent un ordre de retrait..
- Barème question par question : 1 pt choix, 1 pt justification, 1 pt contre-exemple, 1 pt limite..
- Variante acceptable : Table indexée acceptée si un index explicite est construit..
- Erreurs fréquentes : Choisir une file car les données arrivent dans un ordre..
- Remédiation : Faire lister les opérations dominantes..
- Critère de réussite : Le choix répond à la question posée..

## Exercice 4 - Graphe

- Capacité officielle associée : T-STRUCT-05A.
- Réponse attendue : Les villes sont sommets, les routes sont arêtes ; la représentation peut être liste ou matrice..
- Justification : Un graphe modélise des relations entre objets..
- Barème question par question : 1 pt sommets, 1 pt arêtes, 1 pt orientation ou non, 1 pt représentation..
- Variante acceptable : Graphe orienté accepté si le sens des routes est explicitement justifié..
- Erreurs fréquentes : Confondre arête et sommet..
- Remédiation : Faire dessiner puis traduire en liste..
- Critère de réussite : La représentation permet de retrouver les voisins..

## Exercice 5 - Parcours application

- Capacité officielle associée : T-ALGO-02A.
- Réponse attendue : La file conserve les sommets découverts dans l’ordre FIFO, ce qui visite par distance croissante en nombre d’arêtes..
- Justification : BFS dépend de FIFO pour traiter les couches successives..
- Barème question par question : 1 pt file, 1 pt FIFO, 1 pt sommets visités, 1 pt limite..
- Variante acceptable : Explication avec dessin acceptée..
- Erreurs fréquentes : Utiliser une pile et décrire DFS..
- Remédiation : Comparer deux traces sur le même graphe..
- Critère de réussite : L’ordre de visite est justifié..

## Décision

Le corrigé n'est pas publié. Une revue pédagogique et scientifique reste nécessaire avant utilisation large.
