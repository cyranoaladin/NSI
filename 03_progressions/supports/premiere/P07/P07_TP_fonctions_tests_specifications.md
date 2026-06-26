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
## Déroulé opérationnel détaillé
1. écrire `prix_ttc(ht, taux)` avec retour arrondi à deux décimales.
2. refuser un prix hors taxe négatif par `ValueError`.
3. refuser un taux négatif ou supérieur à 1.
4. séparer calcul, validation et tests dans trois fonctions courtes.
5. documenter précondition et postcondition dans la docstring.
6. exécuter les tests sans modifier le fichier de tests attendu.

## Tests vérifiables attendus
- Test 1 : `prix_ttc(80, 0.20) == 96.0`.
- Test 2 : `prix_ttc(0, 0.20) == 0.0`.
- Test 3 : `prix_ttc(19.99, 0.055) == 21.09`.
- Test 4 : `prix_ttc(-5, 0.20)` lève `ValueError`.
- Test 5 : `prix_ttc(10, -0.1)` lève `ValueError`.
- Test 6 : `prix_ttc(10, 1.5)` lève `ValueError`.

## Cas limites à documenter
- Cas limite : montant nul.
- Cas limite : arrondi décimal.
- Cas limite : taux nul.
- Cas limite : taux maximal 1.
- Cas limite : entrée négative.
- Cas limite : type non numérique.

## Plan de correction professeur
- Vérifier que le programme se lance dans un répertoire temporaire propre.
- Lire les fonctions avant les tests pour repérer un retour constant ou hardcodé.
- Exécuter les tests nominaux puis les tests limites.
- Ajouter un test invalide avant toute correction manuelle.
- Comparer la sortie obtenue avec le résultat attendu écrit dans ce TP.
- Refuser une solution qui supprime le cas limite au lieu de le traiter.
- Noter séparément exactitude, robustesse, lisibilité et justification.

## Grille de vérification élève
- [ ] le fichier demandé existe avec le bon nom.
- [ ] le starter n’a pas été remplacé par une constante.
- [ ] chaque fonction possède une docstring ou un commentaire de contrat.
- [ ] les tests nominaux passent.
- [ ] les tests limites passent.
- [ ] les entrées invalides sont refusées explicitement.
- [ ] le livrable ne dépend pas d’un chemin absolu local.
- [ ] la réponse cite la capacité travaillée.

## Différenciation opérationnelle
- Socle : compléter les fonctions dans l’ordre des tests fournis.
- Standard : ajouter deux tests personnels avant de demander la validation.
- Approfondissement : proposer une variante de donnée et expliquer pourquoi les tests restent pertinents.
- Aide autorisée : rappel de syntaxe, sans fournir le corps complet de la fonction.
- Aide interdite : donner directement le résultat attendu comme unique retour de fonction.

## Livrable final contrôlable
- Livrable : `P07_solution_fonctions_tests_specifications.py` et sortie texte de six assertions..
- Le professeur peut vérifier le livrable sans accès au Drive distant.
- Toute source locale éventuellement utilisée doit être tracée dans `support_source_trace.yml`.
