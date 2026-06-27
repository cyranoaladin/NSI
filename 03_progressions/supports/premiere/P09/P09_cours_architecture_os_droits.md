---
title: "P09 - cours - architecture, système et droits Unix"
level: "premiere"
sequence_id: "P09"
document_type: "cours"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "architecture, système et droits Unix"
notion: "architecture, système et droits Unix"
private_data: false
official_program:
  capacities:
    - "P-ARCH-01A"
    - "P-ARCH-01B"
    - "P-ARCH-03A"
    - "P-ARCH-03B"
    - "P-ARCH-03C"
---

# P09 - Cours - architecture, système et droits Unix

## Objectifs spécifiques
- Identifier les données utiles de la situation : ls -l mesures.csv -> -rw-r----- 1 prof nsi 1240 mesures.csv ; utilisateur eleve hors groupe nsi.
- Employer le vocabulaire : processeur, mémoire, stockage, processus, PID, système de fichiers.
- Produire une trace, une table, une valeur ou un pseudo-code vérifiable.

## Capacités officielles
- P-ARCH-01A.
- P-ARCH-01B.
- P-ARCH-03A.
- P-ARCH-03B.
- P-ARCH-03C.

## Situation-problème
ls -l mesures.csv -> -rw-r----- 1 prof nsi 1240 mesures.csv ; utilisateur eleve hors groupe nsi

## À savoir
- processeur.
- mémoire.
- stockage.
- processus.
- PID.
- système de fichiers.
- chmod.
- permission denied.

## Méthodes
- distinguer mémoire vive et stockage.
- identifier PID et processus.
- lire rwx pour propriétaire groupe autres.
- calculer chmod 640 et droit x dossier.

## Exemples corrigés
### Exemple corrigé 1
- Donnée : `ls -l mesures.csv -> -rw-r----- 1 prof nsi 1240 mesures.csv ; utilisateur eleve hors groupe nsi`.
- Méthode : distinguer mémoire vive et stockage.
- Résultat attendu : -rw-r----- -> propriétaire rw, groupe r, autres aucun droit.
- Contrôle : capacité P-ARCH-01A et cas limite `fichier absent`.
### Exemple corrigé 2
- Donnée : `ls -l mesures.csv -> -rw-r----- 1 prof nsi 1240 mesures.csv ; utilisateur eleve hors groupe nsi`.
- Méthode : identifier PID et processus.
- Résultat attendu : chmod 640 mesures.csv donne rw-r-----.
- Contrôle : capacité P-ARCH-01B et cas limite `droit x manquant sur dossier`.
### Exemple corrigé 3
- Donnée : `ls -l mesures.csv -> -rw-r----- 1 prof nsi 1240 mesures.csv ; utilisateur eleve hors groupe nsi`.
- Méthode : lire rwx pour propriétaire groupe autres.
- Résultat attendu : PID 2314 python collecte.py est un processus.
- Contrôle : capacité P-ARCH-03A et cas limite `chmod 777 trop permissif`.
### Exemple corrigé 4
- Donnée : `ls -l mesures.csv -> -rw-r----- 1 prof nsi 1240 mesures.csv ; utilisateur eleve hors groupe nsi`.
- Méthode : calculer chmod 640 et droit x dossier.
- Résultat attendu : sans x sur dossier, lecture du fichier impossible.
- Contrôle : capacité P-ARCH-03B et cas limite `fichier absent`.

## Cas limites
- fichier absent.
- droit x manquant sur dossier.
- chmod 777 trop permissif.

## Erreurs fréquentes
- confondre mémoire et disque.
- oublier x sur dossier.
- donner tous les droits.

## Exercices intégrés
1. Identifier les données utiles dans `ls -l mesures.csv -> -rw-r----- 1 prof nsi 1240 mesures.csv ; utilisateur eleve hors groupe nsi`.
2. Appliquer : distinguer mémoire vive et stockage.
3. Appliquer : identifier PID et processus.
4. Décider le cas limite `fichier absent`.

## Critères de réussite observables
- Une capacité parmi P-ARCH-01A, P-ARCH-01B, P-ARCH-03A, P-ARCH-03B, P-ARCH-03C est citée et utilisée.
- Le résultat attendu est explicite : -rw-r----- -> propriétaire rw, groupe r, autres aucun droit.
- Le cas limite `droit x manquant sur dossier` est tranché.

## Lien avec la progression
- Séance : P09-S1 à P09-S4.
- TD : `P09_TD_architecture_os_droits.md`.
- TP : `P09_tp_architecture_os_droits.md`.
- Évaluation : `P09_evaluation_architecture_os_droits.md`.

## Renforcement explicatif ciblé

Ce cours doit être lu comme une progression sur architecture, système et droits. La notion ne se réduit pas à une liste de mots : on part d'une situation observable, on nomme les objets manipulés, puis on applique une méthode vérifiable sur un cas limité avant de généraliser.

### Savoir disciplinaire
- Vocabulaire à maîtriser : processeur, mémoire vive, stockage, processus, système de fichiers, chmod, permission denied.
- Capacités reliées : P-ARCH-01A, P-ARCH-01B, P-ARCH-03A, P-ARCH-03B, P-ARCH-03C.
- Le savoir attendu consiste à expliquer le rôle de chaque objet avant de l'utiliser dans un exercice.

### Savoir-faire et méthodes opérationnelles
- calculer une permission Unix en lecture/écriture/exécution.
- expliquer pourquoi un processus ne peut pas lire un fichier.
- relier une erreur permission denied au propriétaire et au groupe.

### Erreurs fréquentes spécifiques
- Un élève peut confondre mémoire vive et stockage persistant ; la correction consiste à reprendre la définition puis à refaire la trace sur un exemple minimal.
- Un élève peut oublier le bit exécution sur un script ; la correction consiste à isoler le cas limite avant de recommencer le calcul ou le raisonnement.
- Un élève peut attribuer une permission au mauvais groupe ; la correction consiste à vérifier le résultat avec une donnée différente.

### Cas limites à contrôler
- Cas minimal : une donnée vide, un seul élément, une route absente ou une structure sans enfant selon la notion.
- Cas ambigu : doublon, égalité, absence de correspondance ou choix local non optimal.

### Synthèse savoir / savoir-faire / méthode
- Savoir : définir précisément les objets de architecture, système et droits.
- Savoir-faire : appliquer une méthode contrôlable à une donnée explicite.
- Méthode : annoncer la donnée, exécuter les étapes dans l'ordre, puis vérifier le résultat par un cas limite.
