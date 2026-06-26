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
