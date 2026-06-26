---
title: "P07 - TP - Fonctions, spécifications et tests"
level: "premiere"
sequence_id: "P07"
document_type: "tp"
status: "needs_review"
version: "0.2.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Langage Python"
notion: "fonctions, paramètres, assertions, tests"
objectifs:
  - "écrire la signature et le rôle des paramètres"
  - "formuler précondition et postcondition"
  - "ajouter une assertion sur le prix négatif"
  - "tester cas nominal, zéro et entrée invalide"
private_data: false
official_program:
  capacities:
    - "P-LANG-01"
    - "P-LANG-02"
    - "P-LANG-03A"
    - "P-LANG-03B"
    - "P-LANG-03C"
    - "P-LANG-04"
    - "P-LANG-05"
---

# P07 - TP - Fonctions, spécifications et tests

## Objectif technique
On veut écrire une fonction prix_ttc(ht, taux) utilisable dans plusieurs exercices, avec contrat, tests nominaux et tests d’erreur.

## Consigne technique détaillée
- écrire la signature et le rôle des paramètres.
- formuler précondition et postcondition.
- ajouter une assertion sur le prix négatif.
- tester cas nominal, zéro et entrée invalide.

## Starter code
```python
def verifier_fonctions_tests_specifications(donnee):
    """À compléter : renvoyer une structure vérifiable, pas un texte hardcodé."""
    raise NotImplementedError("à compléter par l’élève")
```

## Tests attendus
- Test nominal : donnée de référence acceptée et résultat exact.
- Test limite : donnée vide ou minimale traitée selon la convention.
- Test invalide : donnée incohérente refusée avec exception ou message explicite.

## Exemple d’exécution
- Entrée : `prix_ttc(80, 0.20), prix_ttc(0, 0.20), prix_ttc(-5, 0.20)`.
- Sortie attendue : structure contrôlable par assertions, pas phrase libre.

## Livrable vérifiable
- Un fichier `P07_solution_fonctions_tests_specifications.py` avec au moins trois tests personnels.
- Une capture texte des tests exécutés.

## Cas limite
- Cas à discuter : oublier le cas limite ht=0.

## Corrigé professeur séparé
- Le corrigé professeur doit être conservé séparément et ne pas être cité comme document élève.

## Critères de réussite
- Le code ne retourne pas une constante unique.
- Les tests distinguent cas nominal, cas limite et entrée invalide.
- La justification relie le résultat à une capacité officielle.
