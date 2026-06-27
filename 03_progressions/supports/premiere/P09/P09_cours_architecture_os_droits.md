---
title: "P09 - Cours - architecture, système d’exploitation, droits"
level: "premiere"
sequence_id: "P09"
document_type: "cours"
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

# P09 - Cours - architecture, système d’exploitation, droits

## Objectifs
- Lire la situation sans modifier les données.
- Appliquer une méthode explicitement liée aux capacités.
- Produire un résultat contrôlable.

## Capacités travaillées
- P-ARCH-01A
- P-ARCH-01B
- P-ARCH-03A
- P-ARCH-03B

## Situation-problème
Un fichier projet.py doit être rendu exécutable seulement par son propriétaire dans un système multi-utilisateur.

## Données de référence
`droits initiaux -rw-r--r--; commande visée chmod u+x projet.py; résultat -rwxr--r--`

## Méthodes disciplinaires
- distinguer processeur, mémoire, stockage et périphériques.
- repérer le rôle du système d’exploitation.
- interpréter r/w/x pour utilisateur, groupe, autres.

## Exemple corrigé 1
Donnée : `droits initiaux -rw-r--r--; commande visée chmod u+x projet.py; résultat -rwxr--r--`.
Méthode : distinguer processeur, mémoire, stockage et périphériques.
Résultat : seul le propriétaire gagne x ; le groupe et les autres gardent lecture seule ; l’OS contrôle l’accès au fichier.

## Exemple corrigé 2 - cas limite
On modifie une seule donnée pour tester le cas limite du chapitre. La correction attendue explique pourquoi la méthode reste valable ou pourquoi elle doit refuser l’entrée.

## Erreurs fréquentes
- Confondre une clé, un indice ou un état temporaire avec la donnée stable.
- Conclure sans écrire le résultat contrôlable.
- Oublier le cas vide, absent ou invalide.

## Exercices intégrés
1. Reprendre la donnée de référence et écrire toutes les étapes.
2. Modifier une valeur et prévoir le nouveau résultat.
3. Construire un cas limite et dire si la méthode accepte ou refuse.
4. Relier chaque étape à une capacité officielle.
