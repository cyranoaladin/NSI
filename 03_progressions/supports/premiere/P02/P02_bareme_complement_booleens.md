---
title: "P02 - barème - Complément à deux et tables de vérité"
level: "premiere"
sequence_id: "P02"
document_type: "bareme"
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

# P02 - barème - Complément à deux et tables de vérité

## Objectifs
- Comprendre la notion : entiers relatifs, débordement, booléens.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : P-DATA-BASE-02A, P-DATA-BASE-02B, P-DATA-BASE-04.

## Capacités officielles
- P-DATA-BASE-02A
- P-DATA-BASE-02B
- P-DATA-BASE-04
## Barème
La note courte est ramenée à 10 points.

## Exemple
Sur 8 bits, `-7` se code par `256-7=249`, donc `11111001`. Pour décoder `11111001`, le bit de poids fort vaut 1, donc on calcule `249-256=-7`.

## Exercices évalués
Encoder `5`, `-1` et `-8` sur 8 bits, puis dresser la table de vérité de `(a and b) or (a and not b)`.

## Corrigé
La correction vérifie la taille du registre, le bit de signe, le calcul de débordement et les quatre lignes de la table de vérité.

## Répartition
- Question 1 : 2 points pour le vocabulaire exact.
- Question 2 : 3 points pour la méthode et le résultat.
- Question 3 : 3 points pour l'analyse et la justification.
- Question 4 : 2 points pour le test ou le cas limite.

## Erreurs fréquentes
- Accorder tous les points à un résultat non justifié.
- Ne pas distinguer erreur mineure de méthode et erreur de convention.

## Remédiation
Identifier la ligne du barème perdue, puis refaire uniquement la compétence concernée.

## Différenciation
Aménagement : accorder les points de méthode dès que les étapes sont correctement ordonnées, même si une erreur de calcul isolée apparaît.

## Statut de revue
Document réel de première tranche, non publié et non validé. Une revue humaine indépendante reste nécessaire avant toute promotion de statut.
