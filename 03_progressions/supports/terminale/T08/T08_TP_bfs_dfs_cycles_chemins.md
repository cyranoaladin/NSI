---
title: "T08 - TP - Parcours BFS, DFS, cycles et chemins"
level: "terminale"
sequence_id: "T08"
document_type: "tp"
status: "needs_review"
version: "0.2.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Algorithmes sur graphes"
notion: "parcours en largeur, profondeur, chemins, cycles"
objectifs:
  - "exécuter BFS avec file"
  - "exécuter DFS avec pile ou récursion"
  - "reconstruire un chemin par prédécesseurs"
  - "détecter un cycle en évitant le parent"
private_data: false
official_program:
  capacities:
    - "T-ALGO-02A"
    - "T-ALGO-02B"
    - "T-ALGO-02C"
    - "T-ALGO-02D"
---

# T08 - TP - Parcours BFS, DFS, cycles et chemins

## Objectif technique
Dans un graphe de salles, on cherche le plus petit nombre de couloirs depuis A vers D et on compare BFS avec DFS.

## Consigne technique détaillée
- exécuter BFS avec file.
- exécuter DFS avec pile ou récursion.
- reconstruire un chemin par prédécesseurs.
- détecter un cycle en évitant le parent.

## Starter code
```python
def verifier_bfs_dfs_cycles_chemins(donnee):
    """À compléter : renvoyer une structure vérifiable, pas un texte hardcodé."""
    raise NotImplementedError("à compléter par l’élève")
```

## Tests attendus
- Test nominal : donnée de référence acceptée et résultat exact.
- Test limite : donnée vide ou minimale traitée selon la convention.
- Test invalide : donnée incohérente refusée avec exception ou message explicite.

## Exemple d’exécution
- Entrée : `A: B,C ; B: A,D ; C: A,D ; D: B,C,E ; E: D`.
- Sortie attendue : structure contrôlable par assertions, pas phrase libre.

## Livrable vérifiable
- Un fichier `T08_solution_bfs_dfs_cycles_chemins.py` avec au moins trois tests personnels.
- Une capture texte des tests exécutés.

## Cas limite
- Cas à discuter : croire que DFS donne toujours un plus court chemin.

## Corrigé professeur séparé
- Le corrigé professeur doit être conservé séparément et ne pas être cité comme document élève.

## Critères de réussite
- Le code ne retourne pas une constante unique.
- Les tests distinguent cas nominal, cas limite et entrée invalide.
- La justification relie le résultat à une capacité officielle.
## Déroulé opérationnel détaillé
1. implémenter BFS avec file explicite.
2. implémenter DFS avec pile ou récursion contrôlée.
3. reconstruire un chemin parent depuis BFS.
4. détecter un cycle dans un graphe non orienté.
5. comparer ordre de visite BFS/DFS.
6. tester un graphe non connexe.

## Tests vérifiables attendus
- Test 1 : BFS depuis A visite A puis ses voisins B,C.
- Test 2 : chemin A vers E reconstruit `A-B-D-E` ou chemin équivalent minimal.
- Test 3 : DFS atteint tous les sommets de la composante.
- Test 4 : cycle A-B-C-A détecté.
- Test 5 : graphe arbre ne signale pas de cycle.
- Test 6 : sommet F isolé reste non visité depuis A.

## Cas limites à documenter
- Cas limite : graphe vide.
- Cas limite : sommet départ absent.
- Cas limite : cycle de longueur 3.
- Cas limite : composante isolée.
- Cas limite : voisin déjà visité.
- Cas limite : chemin impossible.

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
- Livrable : `T08_solution_parcours_graphes.py` avec sorties BFS, DFS, chemin et cycle..
- Le professeur peut vérifier le livrable sans accès au Drive distant.
- Toute source locale éventuellement utilisée doit être tracée dans `support_source_trace.yml`.
