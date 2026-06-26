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
## Déroulé opérationnel détaillé
1. modéliser un graphe non orienté par dictionnaire de listes.
2. convertir ce graphe en matrice d’adjacence.
3. vérifier la symétrie de la matrice.
4. calculer le degré de chaque sommet.
5. détecter une arête absente.
6. comparer coût mémoire liste/matrice sur un petit exemple.

## Tests vérifiables attendus
- Test 1 : graphe A-B, A-C, B-D donne degré A=2.
- Test 2 : la matrice contient `1` en A,B et B,A.
- Test 3 : la diagonale vaut 0 sans boucle.
- Test 4 : arête C-D absente renvoie `False`.
- Test 5 : sommet isolé E a degré 0.
- Test 6 : conversion conserve l’ordre des sommets annoncé.

## Cas limites à documenter
- Cas limite : sommet isolé.
- Cas limite : graphe vide.
- Cas limite : arête dupliquée.
- Cas limite : boucle A-A.
- Cas limite : sommet inconnu.
- Cas limite : graphe orienté non accepté.

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
- Livrable : `T07_solution_graphes.py` et tableau liste/matrice rempli..
- Le professeur peut vérifier le livrable sans accès au Drive distant.
- Toute source locale éventuellement utilisée doit être tracée dans `support_source_trace.yml`.
