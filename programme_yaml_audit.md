# Audit du YAML programme NSI

## Source auditée

Fichier : `00_programmes_officiels/programme_nsi_2019.yaml`.

Références : annexes officielles NSI Première et Terminale publiées au Bulletin officiel.

## Comptage actuel

Première :

- Rubriques : 8.
- Contenus : 31.
- Capacités déclarées : 53.
- Entrées YAML : 31.

Terminale :

- Rubriques : 6.
- Contenus : 23.
- Capacités déclarées : 48.
- Entrées YAML : 23.

## Écarts constatés

Plusieurs identifiants regroupent encore plusieurs capacités attendues.

Un identifiant ne correspond donc pas toujours à une capacité indivisible.

Exemples Première :

- `P-DATA-CONSTR-02` regroupe plusieurs actions sur tableaux.
- `P-IHM-03` regroupe plusieurs aspects client-serveur.
- `P-ARCH-03` regroupe commandes, droits et processus.
- `P-ALGO-02` regroupe insertion et sélection.

Exemples Terminale :

- `T-STRUCT-01` regroupe interface, implémentation et coût.
- `T-STRUCT-03` regroupe listes, piles, files, dictionnaires, index et clés.
- `T-BDD-03` regroupe plusieurs formes SQL.
- `T-ALGO-01` regroupe arbres binaires et ABR.
- `T-ALGO-02` regroupe BFS, DFS et plus courts chemins.

## Risque

La couverture peut rester trop large si une preuve partielle est attachée à un identifiant agrégé.

Une capacité de compréhension ne doit pas être fusionnée avec une capacité de programmation.

Une rubrique ne doit pas être utilisée comme capacité.

Un contenu ne doit pas être utilisé comme preuve d'activité.

## Recommandation

Créer des sous-identifiants pour les contenus contenant plusieurs capacités.

Exemples :

- `T-ALGO-02a` : parcours en largeur.
- `T-ALGO-02b` : parcours en profondeur.
- `T-ALGO-02c` : plus court chemin dans un graphe non pondéré.
- `P-TABLE-03a` : recherche dans une table.
- `P-TABLE-03b` : tri selon une colonne.
- `P-TABLE-04a` : fusion de tables.
- `P-TABLE-04b` : gestion des doublons ou incohérences.

## Décision

Le YAML est utilisable comme référentiel de prototype.

Il ne doit pas être utilisé seul pour déclarer une couverture fiable du programme.
