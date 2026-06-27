---
title: "P09 - tp_papier - architecture, système et droits Unix"
level: "premiere"
sequence_id: "P09"
document_type: "tp_papier"
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

# P09 - TP - architecture, système et droits Unix

## Statut du TP
TP papier : ce support n attend aucune ressource Python ; le livrable est une trace écrite vérifiable.

## Donnée fournie
`ls -l mesures.csv -> -rw-r----- 1 prof nsi 1240 mesures.csv ; utilisateur eleve hors groupe nsi`

## Travail demandé
1. Préparer la donnée et nommer les champs utiles.
2. Réaliser : distinguer mémoire vive et stockage.
3. Réaliser : identifier PID et processus.
4. Tester le cas limite `fichier absent`.
5. Produire le livrable : -rw-r----- -> propriétaire rw, groupe r, autres aucun droit.

## Barème associé
- 2 points : donnée préparée.
- 3 points : méthode principale.
- 3 points : résultat `-rw-r----- -> propriétaire rw, groupe r, autres aucun droit`.
- 2 points : cas limite `fichier absent`.

## Corrigé question par question
### Corrigé question 1
Résultat attendu : `ls -l mesures.csv -> -rw-r----- 1 prof nsi 1240 mesures.csv ; utilisateur eleve hors groupe nsi`.
### Corrigé question 2
Résultat attendu : -rw-r----- -> propriétaire rw, groupe r, autres aucun droit.
### Corrigé question 3
Résultat attendu : chmod 640 mesures.csv donne rw-r-----.
### Corrigé question 4
Résultat attendu : `fichier absent` traité sans ambiguïté.

## Liens
- TD lié : `P09_TD_architecture_os_droits.md`.
- Évaluation liée : `P09_evaluation_architecture_os_droits.md`.

## Cas limites travaillés
- fichier absent.
- droit x manquant sur dossier.
- chmod 777 trop permissif.

## Erreurs fréquentes
- confondre mémoire et disque.
- oublier x sur dossier.
- donner tous les droits.

## Critères de réussite observables
- La donnée de départ est recopiée exactement.
- La trace ou le pseudo-code conduit à `-rw-r----- -> propriétaire rw, groupe r, autres aucun droit`.
- Au moins un cas limite de la section précédente est décidé.

