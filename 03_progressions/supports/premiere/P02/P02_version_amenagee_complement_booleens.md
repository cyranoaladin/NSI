---
title: "P02 - version aménagée - Complément à deux et tables de vérité"
level: "premiere"
sequence_id: "P02"
document_type: "version_amenagee"
status: "needs_review"
version: "0.1.0"
source: "BO 2019 ; source possible Drive : Documents_DRIVE/Algo_Premiere/Complément.pdf"
theme: "Représentation des données"
notion: "entiers relatifs, débordement, booléens"
objectifs: ["Travailler la capacité ciblée", "Produire une trace vérifiable", "Identifier les erreurs fréquentes"]
private_data: false
official_program:
  capacities: ["P-DATA-BASE-02A", "P-DATA-BASE-02B", "P-DATA-BASE-04"]
---

# P02 - version aménagée - Complément à deux et tables de vérité

## Objectifs
- Comprendre la notion : entiers relatifs, débordement, booléens.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : P-DATA-BASE-02A, P-DATA-BASE-02B, P-DATA-BASE-04.

## Capacités officielles
- P-DATA-BASE-02A
- P-DATA-BASE-02B
- P-DATA-BASE-04
## Principe
Cette version conserve les mêmes capacités officielles mais réduit la charge de lecture.

## Exemple
Sur 8 bits, `-7` se code par `256-7=249`, donc `11111001`. Pour décoder `11111001`, le bit de poids fort vaut 1, donc on calcule `249-256=-7`.

## Exercices
1. Question guidée avec étapes numérotées.
2. Application directe avec tableau de réponse.
3. Justification courte à choisir parmi deux formulations.

## Corrigé
La correction vérifie la taille du registre, le bit de signe, le calcul de débordement et les quatre lignes de la table de vérité.

## Aides intégrées
Les mots importants sont rappelés dans l'énoncé et les emplacements de calcul sont séparés.

## Erreurs fréquentes
- Lire trop vite la convention.
- Oublier de remplir une étape intermédiaire.

## Remédiation
Faire relire la consigne, surligner l'entrée et la sortie, puis reprendre l'étape manquante.

## Différenciation
Socle : version aménagée. Standard : évaluation courte ordinaire. Approfondissement : question bonus sans pénaliser le socle.

## Statut de revue
Document réel de première tranche, non publié et non validé. Une revue humaine indépendante reste nécessaire avant toute promotion de statut.
