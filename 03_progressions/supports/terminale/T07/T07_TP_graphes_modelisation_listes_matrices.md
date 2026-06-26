---
title: "T07 - TP - Graphes : modélisation, listes et matrices"
level: "terminale"
sequence_id: "T07"
document_type: "tp"
status: "needs_review"
version: "0.2.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Graphes"
notion: "sommets, arêtes, matrice et liste d’adjacence"
objectifs:
  - "dessiner le graphe non orienté"
  - "écrire la liste d’adjacence"
  - "construire la matrice 4 x 4"
  - "comparer accès à un voisin et test d’adjacence"
private_data: false
official_program:
  capacities:
    - "T-STRUCT-05A"
    - "T-STRUCT-05B"
    - "T-STRUCT-05C"
    - "T-STRUCT-05D"
---

# T07 - TP - Graphes : modélisation, listes et matrices

## Objectif technique
On modélise un réseau de salles A, B, C, D avec couloirs A-B, A-C, B-D. Il faut choisir une représentation et justifier ses coûts.

## Consigne technique détaillée
- dessiner le graphe non orienté.
- écrire la liste d’adjacence.
- construire la matrice 4 x 4.
- comparer accès à un voisin et test d’adjacence.

## Starter code
```python
def verifier_graphes_modelisation_listes_matrices(donnee):
    """À compléter : renvoyer une structure vérifiable, pas un texte hardcodé."""
    raise NotImplementedError("à compléter par l’élève")
```

## Tests attendus
- Test nominal : donnée de référence acceptée et résultat exact.
- Test limite : donnée vide ou minimale traitée selon la convention.
- Test invalide : donnée incohérente refusée avec exception ou message explicite.

## Exemple d’exécution
- Entrée : `S = {A, B, C, D}, E = {(A,B), (A,C), (B,D)}`.
- Sortie attendue : structure contrôlable par assertions, pas phrase libre.

## Livrable vérifiable
- Un fichier `T07_solution_graphes_modelisation_listes_matrices.py` avec au moins trois tests personnels.
- Une capture texte des tests exécutés.

## Cas limite
- Cas à discuter : confondre sommet et arête.

## Corrigé professeur séparé
- Le corrigé professeur doit être conservé séparément et ne pas être cité comme document élève.

## Critères de réussite
- Le code ne retourne pas une constante unique.
- Les tests distinguent cas nominal, cas limite et entrée invalide.
- La justification relie le résultat à une capacité officielle.
