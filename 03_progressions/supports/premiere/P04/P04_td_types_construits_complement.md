---
title: "P04 - TD - Types construits complément"
level: "premiere"
sequence_id: "P04"
document_type: "td"
status: "needs_review"
version: "0.4.1"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Tuples, listes, dictionnaires"
notion: "p-uplet, compréhension, matrice, dictionnaire, itération"
objectifs:
  - "Objectif O1 - Identifier précisément la représentation ou la structure en jeu"
  - "Objectif O2 - Appliquer une méthode disciplinaire complète"
  - "Objectif O3 - Justifier le résultat sur un cas différent"
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur observée"
private_data: false
official_program:
  capacities:
    - "P-DATA-CONSTR-01"
    - "P-DATA-CONSTR-02B"
    - "P-DATA-CONSTR-02C"
    - "P-DATA-CONSTR-03A"
    - "P-DATA-CONSTR-03B"
    - "P-DATA-CONSTR-03C"
---

# P04 - Travaux dirigés - Types construits complément

## Capacités officielles atomiques
- P-DATA-CONSTR-01 : Écrire une fonction renvoyant un p-uplet de valeurs
- P-DATA-CONSTR-02B : Construire un tableau par compréhension
- P-DATA-CONSTR-02C : Utiliser des tableaux de tableaux pour représenter des matrices
- P-DATA-CONSTR-03A : Construire une entrée de dictionnaire
- P-DATA-CONSTR-03B : Itérer sur les éléments d’un dictionnaire

---

## Exercice 1 - Fonction renvoyant un p-uplet (P-DATA-CONSTR-01)

On considère la fonction suivante :

```python
def analyser_notes(notes):
    mini = notes[0]
    maxi = notes[0]
    somme = 0
    for n in notes:
        if n < mini:
            mini = n
        if n > maxi:
            maxi = n
        somme = somme + n
    moyenne = somme / len(notes)
    return mini, maxi, moyenne
```

**Question 1a.** Donner le type de la valeur renvoyée par `analyser_notes([12, 8, 15, 10])`.

**Question 1b.** Déterminer les valeurs de `a`, `b` et `c` après l’exécution de :

```python
a, b, c = analyser_notes([12, 8, 15, 10])
```

**Question 1c.** Écrire sur papier une fonction `extremes(a, b)` qui renvoie le tuple `(plus_petit, plus_grand)` de deux nombres `a` et `b`.

**Question 1d.** Que se passe-t-il si on appelle `analyser_notes([])` ? Quelle précondition faudrait-il vérifier ?

---

## Exercice 2 - Tableau par compréhension (P-DATA-CONSTR-02B)

**Question 2a.** Déterminer le contenu de chaque liste :

```python
L1 = [x ** 2 for x in range(10)]
L2 = [k * 3 for k in range(1, 6)]
L3 = [c.upper() for c in "python"]
```

**Question 2b.** Déterminer le contenu de la liste avec filtre :

```python
L4 = [n for n in range(1, 21) if n % 3 == 0]
```

**Question 2c.** Écrire sur papier une compréhension qui produit la liste des cubes des entiers de 1 à 8, soit `[1, 8, 27, 64, 125, 216, 343, 512]`.

**Question 2d.** On donne `temperatures = [15.5, 22.0, 18.3, -1.0, 30.2]`. Écrire une compréhension qui ne garde que les températures strictement positives.

**Question 2e.** Que produit `[0 for _ in range(0)]` ? Justifier.

---

## Exercice 3 - Matrices comme tableaux de tableaux (P-DATA-CONSTR-02C)

On donne la matrice suivante :

```python
M = [
    [5, 3, 8],
    [1, 7, 4],
    [9, 2, 6],
]
```

**Question 3a.** Donner la valeur de `M[0][2]`, `M[1][1]` et `M[2][0]`.

**Question 3b.** Combien de lignes et de colonnes possède `M` ? Écrire les expressions Python qui donnent ces valeurs.

**Question 3c.** Écrire sur papier la trace d'exécution (valeurs de `i`, `j` et `total`) de la fonction suivante appliquée à `M` :

```python
def somme_diagonale(matrice):
    total = 0
    for i in range(len(matrice)):
        total = total + matrice[i][i]
    return total
```

**Question 3d.** On exécute le code suivant. Expliquer pourquoi le résultat est incorrect et proposer une correction.

```python
grille = [[0] * 3] * 3
grille[0][0] = 1
print(grille)
```

---

## Exercice 4 - Construire une entrée de dictionnaire (P-DATA-CONSTR-03A)

On souhaite stocker les métadonnées EXIF fictives d’une photographie.

**Question 4a.** Compléter le code pour construire le dictionnaire `photo` contenant les entrées suivantes : `"marque"` associée à `"Sony"`, `"modele"` associée à `"A7III"`, `"date_prise"` associée à `"2025-07-01"`, `"taille"` associée au tuple `(6000, 4000)`.

```python
photo = {}
photo[______] = ______
photo[______] = ______
photo[______] = ______
photo[______] = ______
```

**Question 4b.** Qu'affiche `photo["taille"]` ? De quel type est cette valeur ?

**Question 4c.** On exécute `photo["iso"] = 100` puis `photo["iso"] = 200`. Que contient `photo["iso"]` ? Expliquer.

**Question 4d.** Expliquer pourquoi le code suivant provoque une erreur :

```python
d = {}
d[[1, 2]] = "coordonnees"
```

---

## Exercice 5 - Itérer sur un dictionnaire (P-DATA-CONSTR-03B)

On donne le dictionnaire suivant :

```python
meteo = {
    "temperature": 22,
    "humidite": 65,
    "vent": 15,
    "pression": 1013,
}
```

**Question 5a.** Écrire ce qu'affiche chacun des trois blocs :

```python
# Bloc A
for cle in meteo:
    print(cle)

# Bloc B
for val in meteo.values():
    print(val)

# Bloc C
for cle, val in meteo.items():
    print(f"{cle} = {val}")
```

**Question 5b.** Écrire sur papier une boucle qui calcule la somme de toutes les valeurs du dictionnaire `meteo`.

**Question 5c.** Écrire sur papier une fonction `cles_superieures(d, seuil)` qui renvoie la liste des clés dont la valeur associée est strictement supérieure à `seuil`.

**Question 5d.** Que se passe-t-il si on itère sur un dictionnaire vide `{}` ? Justifier.


## Objectifs


## Prérequis


## Situation-problème

Un programme de gestion de notes doit stocker, pour chaque élève, son nom et ses notes dans différentes matières. Quelle structure de données choisir et comment organiser les accès ?

## Activité d’entrée

Écrire une fonction Python qui reçoit deux nombres et renvoie à la fois leur somme et leur produit. Tester avec print(resultat[0], resultat[1]).

## Exemple

Écriture collective d'une fonction coordonnees() renvoyant un tuple (x, y) et d'une compréhension [i**2 for i in range(5)].

## Exercices

Exercices de manipulation de tuples, listes en compréhension, matrices et dictionnaires.

## Corrigé

Les corrigés détaillés sont dans P04_corrige_types_construits_complement.md.

## Erreurs fréquentes

- EF1 : confondre tuple (immutable) et liste (mutable) lors du retour de fonction.
- EF2 : oublier les crochets dans une compréhension de liste.
- EF3 : accéder à une clé inexistante d'un dictionnaire sans utiliser get().


## Remédiation

Exercice de remédiation : écrire une fonction min_max qui renvoie le minimum et le maximum d'une liste sous forme de tuple.

## Différenciation

- Socle : exercices de base.
- Standard : exercices complets.
- Expert : exercice d'approfondissement.

## Critères de réussite

- Critère de réussite : la fonction renvoie un tuple vérifiable par déstructuration.
- Critère de validation : la compréhension de liste produit le résultat attendu.
- Observable : le dictionnaire est itéré avec keys(), values() et items() correctement.


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


Cas limite : liste vide passée en argument. Cas limite : clé absente du dictionnaire.

