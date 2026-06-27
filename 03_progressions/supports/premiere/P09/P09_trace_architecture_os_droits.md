---
title: "P09 - Trace écrite - architecture, système d’exploitation, droits"
level: "premiere"
sequence_id: "P09"
document_type: "trace"
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

# P09 - Trace écrite - architecture, système d’exploitation, droits

## À retenir
- Situation : Un fichier projet.py doit être rendu exécutable seulement par son propriétaire dans un système multi-utilisateur.
- Donnée de référence : `droits initiaux -rw-r--r--; commande visée chmod u+x projet.py; résultat -rwxr--r--`.
- Résultat de référence : seul le propriétaire gagne x ; le groupe et les autres gardent lecture seule ; l’OS contrôle l’accès au fichier.

## Méthode courte
- distinguer processeur, mémoire, stockage et périphériques.
- repérer le rôle du système d’exploitation.
- interpréter r/w/x pour utilisateur, groupe, autres.

## Exemple minimal corrigé
Entrée : `droits initiaux -rw-r--r--; commande visée chmod u+x projet.py; résultat -rwxr--r--`.
Sortie attendue : seul le propriétaire gagne x ; le groupe et les autres gardent lecture seule ; l’OS contrôle l’accès au fichier.

## Point de vigilance
Le résultat doit être calculable à partir de la donnée, sans phrase de validation vague.

## Lien séance
- Séance P09-S1 : découverte et exemple.
- Séance P09-S2 : exercices et correction.
