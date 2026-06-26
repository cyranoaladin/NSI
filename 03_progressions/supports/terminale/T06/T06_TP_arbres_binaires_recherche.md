---
title: "T06 - TP - Arbres binaires de recherche"
level: "terminale"
sequence_id: "T06"
document_type: "tp"
status: "needs_review"
version: "0.2.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Structures de données"
notion: "recherche et insertion dans un ABR"
objectifs:
  - "suivre les comparaisons depuis la racine"
  - "justifier le chemin vers 6"
  - "placer 7 à droite de 6"
  - "repérer le cas dégénéré d’insertions triées"
private_data: false
official_program:
  capacities:
    - "T-ALGO-01E"
    - "T-ALGO-01F"
---

# T06 - TP - Arbres binaires de recherche

## Objectif technique
Un ABR contient les clés 8, 3, 10, 1, 6. On recherche 6 puis on insère 7 en conservant l’invariant gauche < racine < droite.

## Consigne technique détaillée
- suivre les comparaisons depuis la racine.
- justifier le chemin vers 6.
- placer 7 à droite de 6.
- repérer le cas dégénéré d’insertions triées.

## Starter code
```python
def verifier_arbres_binaires_recherche(donnee):
    """À compléter : renvoyer une structure vérifiable, pas un texte hardcodé."""
    raise NotImplementedError("à compléter par l’élève")
```

## Tests attendus
- Test nominal : donnée de référence acceptée et résultat exact.
- Test limite : donnée vide ou minimale traitée selon la convention.
- Test invalide : donnée incohérente refusée avec exception ou message explicite.

## Exemple d’exécution
- Entrée : `racine 8 ; gauche 3 avec enfants 1 et 6 ; droite 10`.
- Sortie attendue : structure contrôlable par assertions, pas phrase libre.

## Livrable vérifiable
- Un fichier `T06_solution_arbres_binaires_recherche.py` avec au moins trois tests personnels.
- Une capture texte des tests exécutés.

## Cas limite
- Cas à discuter : oublier l’invariant après insertion.

## Corrigé professeur séparé
- Le corrigé professeur doit être conservé séparément et ne pas être cité comme document élève.

## Critères de réussite
- Le code ne retourne pas une constante unique.
- Les tests distinguent cas nominal, cas limite et entrée invalide.
- La justification relie le résultat à une capacité officielle.
