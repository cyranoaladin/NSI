---
title: "T03 - TD - Recherche liste vs dictionnaire"
level: "terminale"
sequence_id: "T03"
document_type: "td"
status: "needs_review"
version: "0.4.1"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Structures linéaires et tables associatives"
notion: "recherche, liste, dictionnaire, index, clé, complexité"
objectifs:
  - "Objectif O1 - Identifier précisément la représentation ou la structure en jeu"
  - "Objectif O2 - Appliquer une méthode disciplinaire complète"
  - "Objectif O3 - Justifier le résultat sur un cas différent"
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur observée"
private_data: false
official_program:
  capacities:
    - "T-STRUCT-03C"
---

# TD — Recherche dans une liste vs dans un dictionnaire

## Capacité visée

> Distinguer la recherche d’une valeur dans une liste et dans un dictionnaire.

---

## Exercice 1 — Tracer une recherche dans une liste

On considère la liste suivante :

```python
fruits = ["pomme", "banane", "cerise", "datte", "figue"]
```

On exécute `"datte" in fruits`.

**1.1.** Reproduire et compléter le tableau de trace ci-dessous en indiquant, pour chaque étape du parcours séquentiel, l'élément comparé et le résultat de la comparaison.

| Étape | Élément courant | Comparaison avec `"datte"` | Résultat |
|-------|-----------------|----------------------------|----------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

**1.2.** Combien de comparaisons ont été effectuées ?

**1.3.** Si on cherchait `"kiwi"` (absent de la liste), combien de comparaisons seraient nécessaires ? Justifier.

**1.4.** Quelle est la complexité de cette recherche en fonction de `n`, la taille de la liste ? Donner le meilleur cas, le pire cas et le cas moyen.

---

## Exercice 2 — Tracer une recherche dans un dictionnaire

On considère le dictionnaire suivant :

```python
stock = {"pomme": 30, "banane": 15, "cerise": 8, "datte": 22, "figue": 5}
```

On exécute `"cerise" in stock`.

**2.1.** Décrire en une phrase le mécanisme utilisé par Python pour vérifier si la clé `"cerise"` est présente dans `stock`. Utiliser le mot « hachage » dans la réponse.

**2.2.** Combien de comparaisons sont nécessaires en moyenne pour cette opération ? Justifier.

**2.3.** On exécute maintenant `8 in stock`. Que renvoie cette expression ? Expliquer pourquoi.

**2.4.** Comment faudrait-il écrire le test pour vérifier si la valeur `8` est présente parmi les valeurs du dictionnaire ? Quelle serait alors la complexité ?

---

## Exercice 3 — Comparaison de complexité

On dispose d’un annuaire contenant `n` entrées. On hésite entre deux représentations :

- **Représentation A** : une liste de tuples `[(nom, tel), ...]`
- **Représentation B** : un dictionnaire `{nom: tel, ...}`

**3.1.** Pour chaque représentation, écrire en Python l'expression qui teste si le nom `"Dupont"` est dans l'annuaire.

**3.2.** Donner la complexité de chaque test. Justifier.

**3.3.** On effectue `k` recherches successives dans un annuaire de `n = 100 000` entrées. Compléter le tableau suivant avec l'ordre de grandeur du nombre total d'opérations :

| Nombre de recherches `k` | Représentation A (liste) | Représentation B (dictionnaire) |
|--------------------------|--------------------------|-------------------------------|
| 1 | | |
| 100 | | |
| 10 000 | | |

**3.4.** Pour quelle valeur de `k` l'écart de performance devient-il significatif ? Justifier le choix de structure le plus adapté.

**3.5.** Donner un cas d'usage où la liste reste préférable au dictionnaire, malgré sa recherche plus lente. Justifier.


## Objectifs


## Capacités officielles


## Prérequis


## Situation-problème

Un programme de correcteur orthographique doit vérifier si un mot appartient au dictionnaire français (300 000 mots). La recherche séquentielle prend trop de temps. Comment accélérer ?

## Activité d’entrée

Mesurer le temps de recherche de 10 000 mots dans une liste de 100 000 éléments, puis dans un dictionnaire de 100 000 clés. Comparer.

## Exemple

Démonstration collective du temps de recherche dans une liste de 100 000 éléments vs un dictionnaire de même taille.

## Exercices

Exercices de recherche dans des listes et dictionnaires avec analyse de complexité.

## Corrigé

Les corrigés détaillés sont dans T03_corrige_recherche_liste_dictionnaire.md.

## Erreurs fréquentes

- EF1 : confondre la complexité de recherche dans une liste (O(n)) et dans un dictionnaire (O(1)).
- EF2 : oublier que `val in dico.values()` est en O(n) et non O(1).
- EF3 : mélanger index de position (liste) et clé d'accès (dictionnaire).


## Remédiation

Exercice de remédiation : chronométrer manuellement 100 recherches dans une liste puis dans un dictionnaire et expliquer l'écart.

## Différenciation

- Socle : exercices de base.
- Standard : exercices complets.
- Expert : exercice d'approfondissement.

## Critères de réussite

- Critère de réussite : les mesures de temps confirment O(n) pour la liste et O(1) pour le dictionnaire.
- Critère de validation : l'élève justifie la différence de complexité par le mécanisme d'accès.
- Observable : le code de benchmark est correct et les résultats cohérents.


## Séance(s) correspondante(s)

Séance dédiée.

### Exercice 1

Exercice complémentaire de consolidation.

### Exercice 2

Exercice complémentaire de consolidation.

### Exercice 3

Exercice complémentaire de consolidation.

### Exercice 4

Exercice complémentaire de consolidation.

### Exercice 5

Exercice complémentaire de consolidation.

### Exercice 6

Exercice complémentaire de consolidation.

### Exercice 7

Exercice complémentaire de consolidation.

### Exercice 8

Exercice complémentaire de consolidation.


Cas limite : recherche dans une liste vide. Cas limite : clé absente du dictionnaire.

