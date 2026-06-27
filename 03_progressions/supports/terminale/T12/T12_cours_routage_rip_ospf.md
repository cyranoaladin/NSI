---
title: "T12 - cours - routage RIP et OSPF"
level: "terminale"
sequence_id: "T12"
document_type: "cours"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "routage RIP et OSPF"
notion: "routage RIP et OSPF"
private_data: false
official_program:
  capacities:
    - "T-ARCH-03"
---

# T12 - Cours - routage RIP et OSPF

## Objectifs spécifiques
- Identifier les données utiles de la situation : RIP A-B-D=2 sauts, A-C-D=2 sauts ; OSPF A-B=5, B-D=5, A-C=2, C-D=9.
- Employer le vocabulaire : route, RIP, nombre de sauts, OSPF, coût, table de routage.
- Produire une trace, une table, une valeur ou un pseudo-code vérifiable.

## Capacités officielles
- T-ARCH-03.

## Situation-problème
RIP A-B-D=2 sauts, A-C-D=2 sauts ; OSPF A-B=5, B-D=5, A-C=2, C-D=9

## À savoir
- route.
- RIP.
- nombre de sauts.
- OSPF.
- coût.
- table de routage.
- chemin minimal.
- égalité de coût.

## Méthodes
- compter sauts RIP.
- additionner coûts OSPF.
- choisir route en égalité documentée.
- recalculer après panne.

## Exemples corrigés
### Exemple corrigé 1
- Donnée : `RIP A-B-D=2 sauts, A-C-D=2 sauts ; OSPF A-B=5, B-D=5, A-C=2, C-D=9`.
- Méthode : compter sauts RIP.
- Résultat attendu : RIP : A-B-D et A-C-D ont 2 sauts.
- Contrôle : capacité T-ARCH-03 et cas limite `égalité exacte`.
### Exemple corrigé 2
- Donnée : `RIP A-B-D=2 sauts, A-C-D=2 sauts ; OSPF A-B=5, B-D=5, A-C=2, C-D=9`.
- Méthode : additionner coûts OSPF.
- Résultat attendu : OSPF : A-B-D coût 10, A-C-D coût 11.
- Contrôle : capacité T-ARCH-03 et cas limite `lien indisponible`.
### Exemple corrigé 3
- Donnée : `RIP A-B-D=2 sauts, A-C-D=2 sauts ; OSPF A-B=5, B-D=5, A-C=2, C-D=9`.
- Méthode : choisir route en égalité documentée.
- Résultat attendu : panne B-D -> A-C-D coût 11.
- Contrôle : capacité T-ARCH-03 et cas limite `route inconnue`.
### Exemple corrigé 4
- Donnée : `RIP A-B-D=2 sauts, A-C-D=2 sauts ; OSPF A-B=5, B-D=5, A-C=2, C-D=9`.
- Méthode : recalculer après panne.
- Résultat attendu : route inconnue -> rejet ou défaut.
- Contrôle : capacité T-ARCH-03 et cas limite `égalité exacte`.

## Cas limites
- égalité exacte.
- lien indisponible.
- route inconnue.

## Erreurs fréquentes
- sauts et coûts mélangés.
- choix visuel.
- panne non recalculée.

## Exercices intégrés
1. Identifier les données utiles dans `RIP A-B-D=2 sauts, A-C-D=2 sauts ; OSPF A-B=5, B-D=5, A-C=2, C-D=9`.
2. Appliquer : compter sauts RIP.
3. Appliquer : additionner coûts OSPF.
4. Décider le cas limite `égalité exacte`.

## Critères de réussite observables
- Une capacité parmi T-ARCH-03 est citée et utilisée.
- Le résultat attendu est explicite : RIP : A-B-D et A-C-D ont 2 sauts.
- Le cas limite `lien indisponible` est tranché.

## Lien avec la progression
- Séance : T12-S1 à T12-S4.
- TD : `T12_TD_routage_rip_ospf.md`.
- TP : `T12_tp_routage_rip_ospf.md`.
- Évaluation : `T12_evaluation_routage_rip_ospf.md`.
