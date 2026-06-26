---
title: "P02 - fiche remédiation - Complément à deux et tables de vérité"
level: "premiere"
sequence_id: "P02"
document_type: "remediation"
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

# P02 - fiche remédiation - Complément à deux et tables de vérité

## Objectifs
- Comprendre la notion : entiers relatifs, débordement, booléens.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : P-DATA-BASE-02A, P-DATA-BASE-02B, P-DATA-BASE-04.

## Capacités officielles
- P-DATA-BASE-02A
- P-DATA-BASE-02B
- P-DATA-BASE-04
## Diagnostic rapide
La remédiation commence par une question courte qui cible l'erreur la plus fréquente.

## Exemple
Sur 8 bits, `-7` se code par `256-7=249`, donc `11111001`. Pour décoder `11111001`, le bit de poids fort vaut 1, donc on calcule `249-256=-7`.

## Exercices
1. Refaire le cas guidé avec une valeur plus petite.
2. Compléter une justification à trous.
3. Résoudre un cas voisin sans aide.

## Corrigé
La correction vérifie la taille du registre, le bit de signe, le calcul de débordement et les quatre lignes de la table de vérité.

## Erreurs fréquentes
- Ne pas nommer la convention.
- Sauter une étape de méthode.
- Croire qu'un seul exemple suffit à prouver une règle.

## Remédiation
L'élève doit verbaliser l'erreur initiale, corriger sa démarche, puis noter une règle personnelle de vigilance.

## Différenciation
Socle : justification à trous. Standard : cas voisin. Approfondissement : création d'un piège et de sa correction.

## Statut de revue
Document réel de première tranche, non publié et non validé. Une revue humaine indépendante reste nécessaire avant toute promotion de statut.
