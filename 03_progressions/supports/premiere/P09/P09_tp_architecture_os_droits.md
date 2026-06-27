---
title: "P09 - TP papier - architecture, système d’exploitation, droits"
level: "premiere"
sequence_id: "P09"
document_type: "tp_papier"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Architecture matérielle et systèmes"
notion: "architecture, système d’exploitation, droits"
objectifs:
  - "identifier la donnée de référence"
  - "appliquer la méthode disciplinaire"
  - "produire un résultat vérifiable"
  - "contrôler un cas limite"
private_data: false
official_program:
  capacities:
    - "P-ARCH-01A"
    - "P-ARCH-01B"
    - "P-ARCH-03A"
    - "P-ARCH-03B"
---

# P09 - TP papier - architecture, système d’exploitation, droits

## Statut du TP
Ce support est un TP papier : aucune ressource Python n’est attendue dans cette passe pour P09. Le livrable est une trace manuscrite ou Markdown avec données, méthode, résultat et contrôle du cas limite.

## Donnée fournie
`droits initiaux -rw-r--r--; commande visée chmod u+x projet.py; résultat -rwxr--r--`

## Travail demandé
1. Recopier la donnée utile sans l’altérer.
2. Appliquer la méthode principale : distinguer processeur, mémoire, stockage et périphériques.
3. Vérifier le résultat : seul le propriétaire gagne x ; le groupe et les autres gardent lecture seule ; l’OS contrôle l’accès au fichier.
4. Tester un cas limite explicitement.

## Barème associé
- 2 points : donnée de départ correctement identifiée.
- 3 points : méthode appliquée dans le bon ordre.
- 3 points : résultat final exact.
- 2 points : cas limite justifié.

## Corrigé question par question
### Corrigé question 1
Résultat attendu : la donnée utile est `droits initiaux -rw-r--r--; commande visée chmod u+x projet.py; résultat -rwxr--r--`.
### Corrigé question 2
Résultat attendu : le fichier `projet.py` est une donnée stockée ; le système d'exploitation applique la commande `chmod u+x` et modifie seulement les droits du propriétaire.
### Corrigé question 3
Résultat attendu : après `chmod u+x projet.py`, les droits valent `-rwxr--r--`; seul le propriétaire gagne `x`, le groupe et les autres gardent lecture seule, et l’OS contrôle l’accès au fichier.
### Corrigé question 4
Résultat attendu : avec `chmod go-r projet.py`, le résultat devient `-rwx------` si le propriétaire avait déjà `rwx`; groupe et autres perdent la lecture.

## Liens
- TD lié : `P09_TD_architecture_os_droits.md`.
- Évaluation liée : `P09_evaluation_architecture_os_droits.md`.
