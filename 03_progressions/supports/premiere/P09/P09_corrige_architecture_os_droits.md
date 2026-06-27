---
title: "P09 - Corrigé - architecture, système d’exploitation, droits"
level: "premiere"
sequence_id: "P09"
document_type: "corrige"
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

# P09 - Corrigé - architecture, système d’exploitation, droits

## Réponse attendue principale
Donnée : `droits initiaux -rw-r--r--; commande visée chmod u+x projet.py; résultat -rwxr--r--`.
Étapes :
- distinguer processeur, mémoire, stockage et périphériques.
- repérer le rôle du système d’exploitation.
- interpréter r/w/x pour utilisateur, groupe, autres.
Résultat final : seul le propriétaire gagne x ; le groupe et les autres gardent lecture seule ; l’OS contrôle l’accès au fichier.

## Corrigé des exercices
### Exercice 1
La donnée de référence est recopiée, puis la première méthode est appliquée. Résultat : seul le propriétaire gagne x ; le groupe et les autres gardent lecture seule ; l’OS contrôle l’accès au fichier.
### Exercice 2
La variante doit conserver la structure du problème et produire un résultat recalculé.
### Exercice 3
Le cas limite est accepté seulement si la copie indique l’effet exact sur la méthode.
### Exercice 4
La capacité citée doit être reliée à une étape précise du raisonnement.
