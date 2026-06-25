---
title: "Corrigé - S01 Représentation des données"
level: "premiere"
sequence_id: "s01_representation_donnees"
document_type: "corrige"
status: "needs_review"
version: "0.2.0"
source: "BO spécial n°1 du 22 janvier 2019"
theme: "Représentation des données"
notion: "corrections et justifications"
duration: "1 h"
difficulty: "standard"
private_data: false
official_program:
  level: "premiere"
  rubrique: "Représentation des données"
  content: "Correction des activités"
  capacities:
    - id: "P-DATA-BASE-01"
      label: "Changer de base."
      evidence: [{section: "Réponse attendue - TD", file: "premiere/sequences/s01_representation_donnees/corrige.md", anchor: "#réponse-attendue-td", type: "corrige"}]
    - id: "P-DATA-BASE-02B"
      label: "Utiliser le complément à deux."
      evidence: [{section: "Réponse attendue - TD", file: "premiere/sequences/s01_representation_donnees/corrige.md", anchor: "#réponse-attendue-td", type: "corrige"}]
    - id: "P-DATA-BASE-04"
      label: "Tables de vérité."
      evidence: [{section: "Réponse attendue - TD", file: "premiere/sequences/s01_representation_donnees/corrige.md", anchor: "#réponse-attendue-td", type: "corrige"}]
    - id: "P-DATA-BASE-05A"
      label: "Encodage de texte."
      evidence: [{section: "Réponse attendue - TD", file: "premiere/sequences/s01_representation_donnees/corrige.md", anchor: "#réponse-attendue-td", type: "corrige"}]
    - id: "P-DATA-CONSTR-01"
      label: "Tuples."
      evidence: [{section: "Réponse attendue - TD", file: "premiere/sequences/s01_representation_donnees/corrige.md", anchor: "#réponse-attendue-td", type: "corrige"}]
    - id: "P-DATA-CONSTR-02A"
      label: "Listes."
      evidence: [{section: "Réponse attendue - TD", file: "premiere/sequences/s01_representation_donnees/corrige.md", anchor: "#réponse-attendue-td", type: "corrige"}]
    - id: "P-DATA-CONSTR-03A"
      label: "Dictionnaires."
      evidence: [{section: "Réponse attendue - TD", file: "premiere/sequences/s01_representation_donnees/corrige.md", anchor: "#réponse-attendue-td", type: "corrige"}]
    - id: "P-LANG-04"
      label: "Jeux de tests."
      evidence: [{section: "Code testé", file: "premiere/sequences/s01_representation_donnees/corrige.md", anchor: "#code-testé", type: "corrige"}]
prerequisites: ["TD et TP S01"]
learning_objectives: ["Expliquer les réponses attendues et les variantes acceptables."]
assessment: {formative: true, summative: false}
last_review: {pedagogy: "", science: "", technical: ""}
---

# Corrigé - S01

## Réponse attendue - TD

### Exercice 1

`18₁₀ = 10010₂`.
`31₁₀ = 11111₂`.
`42₁₀ = 101010₂`.
`1010₂ = 10₁₀`.
`1111₂ = 15₁₀`.
`100000₂ = 32₁₀`.
`2A₁₆ = 42₁₀`.
`FF₁₆ = 255₁₀`.
Justification : développer avec les puissances ou relire les restes des divisions.

### Exercice 2

Sur 8 bits sans signe, l'intervalle est `0` à `255`.
`255` est représentable.
`256` ne l'est pas.
`128` est représentable.
`0` est représentable.
`255₁₀ = 11111111₂ = FF₁₆`.
Deux chiffres hexadécimaux suffisent car chaque chiffre représente 4 bits.

### Exercice 3

`5` sur 8 bits : `00000101`.
`-1` sur 8 bits : `11111111`.
`-7` sur 8 bits : `11111001`.
`-128` sur 8 bits : `10000000`.
`00000101` se décode en `5`.
`11111111` se décode en `255 - 256 = -1`.
`11111001` se décode en `249 - 256 = -7`.
`10000000` se décode en `128 - 256 = -128`.
Sur 4 bits, l'intervalle est `-8` à `7`.
Donc `-9` est hors intervalle.

### Exercice 4

Pour `and`, seul le cas `True, True` donne `True`.
Pour `or`, tous les cas sauf `False, False` donnent `True`.
Pour `a and not b`, seul `a=True, b=False` donne `True`.
Le xor donne `True` quand exactement une entrée est vraie.

### Exercice 5

`65` et `233` sont des points de code.
`"A"` est représenté sur un octet en UTF-8.
`"é"` est représenté sur deux octets en UTF-8.
Le nombre de caractères ne suffit donc pas à déduire le nombre d'octets.

### Exercice 6

```python
def milieu(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
```
La compréhension `[t + 1 for t in temperatures]` convient.
Le tuple regroupe deux coordonnées liées.
Il évite de retourner deux valeurs séparées sans relation explicite.

### Exercice 7

Résultat attendu : `{"A": 3, "B": 2, "C": 1}`.
La clé de plus grand effectif est `"A"`.
Un dictionnaire est adapté car l'accès par choix est central.
Une liste suffit si l'on conserve seulement l'ordre brut des votes.

### Exercice 8

Positions successives : liste.
Coordonnées fixes : tuple.
Stock par référence : dictionnaire.
Pixels ligne par ligne : liste de listes.
Fiche courte avec champs nommés : dictionnaire.
Une autre réponse est acceptable si elle est justifiée par les opérations attendues.

### Exercice 9

`mystere(6)` renvoie `"110"`.
Le cas limite non géré est `n = 0`.
Correction minimale : renvoyer `"0"` si `n == 0`.
Tests attendus : `mystere(0)`, `mystere(1)`, `mystere(6)`.

### Exercice 10

La liste de tuples impose un parcours pour retrouver un identifiant.
Un dictionnaire `identifiant -> nom` est plus adapté.
Transformation :
```python
annuaire = {identifiant: nom for identifiant, nom in utilisateurs}
```
Test possible : vérifier que `annuaire["u2"]` renvoie le nom attendu.

## Justification

Les conversions doivent être justifiées par les puissances de la base.
Le complément à deux doit toujours indiquer le nombre de bits.
Les tables de vérité doivent couvrir tous les cas.
Le choix liste, tuple ou dictionnaire doit citer l'opération principale.
Un test doit relier une entrée à une sortie attendue.

## Variante acceptable

Pour le milieu, une solution qui décompose `x1, y1 = p1` est acceptée.
Pour le comptage de votes, une boucle avec `if choix not in effectifs` est acceptée.
Pour le choix de représentation, plusieurs réponses sont acceptées si la justification est solide.
Pour les tests, les noms de fonctions peuvent différer si les entrées et sorties sont vérifiables.

## Erreurs fréquentes

- Oublier `n = 0` dans la conversion.
- Lire `11111111` sans convention.
- Oublier que `FF₁₆` vaut `255`.
- Confondre clé et valeur dans un dictionnaire.
- Donner seulement une structure sans justification.

## Barème

- Conversions de base : 4 points.
- Complément à deux : 4 points.
- Booléens et texte : 3 points.
- Structures Python : 5 points.
- Analyse de code et tests : 4 points.

## Code testé

Les fonctions de référence sont dans `python/representation_tools.py`.
Les tests sont dans `tests/test_representation_tools.py`.
La commande de contrôle est `python scripts/run_python_tests.py`.
Les tests vérifient conversions, complément à deux, Unicode et choix de conteneur.
