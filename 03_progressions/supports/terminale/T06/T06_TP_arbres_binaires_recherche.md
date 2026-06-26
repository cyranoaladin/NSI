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
## Déroulé opérationnel détaillé
1. implémenter un nœud avec `valeur`, `gauche`, `droite`.
2. écrire `inserer(racine, valeur)` sans casser l’ordre ABR.
3. écrire `contient(racine, valeur)` avec parcours guidé.
4. écrire `minimum(racine)`.
5. produire un parcours infixe pour vérifier le tri.
6. documenter la convention sur les doublons.

## Tests vérifiables attendus
- Test 1 : insertion 8,3,10,1,6 produit infixe `[1,3,6,8,10]`.
- Test 2 : `contient(r, 6)` renvoie `True`.
- Test 3 : `contient(r, 7)` renvoie `False`.
- Test 4 : `minimum(r)` renvoie 1.
- Test 5 : arbre vide traité par `None` ou exception documentée.
- Test 6 : doublon 6 refusé ou rangé selon convention écrite.

## Cas limites à documenter
- Cas limite : arbre vide.
- Cas limite : valeur déjà présente.
- Cas limite : arbre dégénéré croissant.
- Cas limite : minimum sur singleton.
- Cas limite : recherche absente.
- Cas limite : valeurs négatives.

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
- Livrable : `T06_solution_abr.py` avec fonctions et tests exécutables..
- Le professeur peut vérifier le livrable sans accès au Drive distant.
- Toute source locale éventuellement utilisée doit être tracée dans `support_source_trace.yml`.
