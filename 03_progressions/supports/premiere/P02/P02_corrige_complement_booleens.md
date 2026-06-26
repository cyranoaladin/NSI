---
title: "P02 - corrigé - Complément à deux et tables de vérité"
level: "premiere"
sequence_id: "P02"
document_type: "corrige"
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

# P02 - corrigé - Complément à deux et tables de vérité

## Objectifs
- Comprendre la notion : entiers relatifs, débordement, booléens.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : P-DATA-BASE-02A, P-DATA-BASE-02B, P-DATA-BASE-04.

## Capacités officielles
- P-DATA-BASE-02A
- P-DATA-BASE-02B
- P-DATA-BASE-04
## Réponse attendue
La correction vérifie la taille du registre, le bit de signe, le calcul de débordement et les quatre lignes de la table de vérité.

## Exemple
Sur 8 bits, `-7` se code par `256-7=249`, donc `11111001`. Pour décoder `11111001`, le bit de poids fort vaut 1, donc on calcule `249-256=-7`.

## Exercices corrigés
Encoder `5`, `-1` et `-8` sur 8 bits, puis dresser la table de vérité de `(a and b) or (a and not b)`.

## Corrigé détaillé
Une copie complète contient la méthode, le résultat et une phrase de contrôle. Les variantes sont acceptées si elles respectent la capacité officielle et ne changent pas le contrat demandé.

## Barème indicatif
- Méthode explicite : 40 %.
- Résultat correct : 30 %.
- Justification ou test : 20 %.
- Présentation lisible : 10 %.

## Erreurs fréquentes
- Résultat juste mais non justifié.
- Confusion de vocabulaire.
- Absence de vérification.

## Remédiation
Reprendre la question avec une donnée plus simple et faire nommer l'erreur corrigée.

## Différenciation
Socle : correction guidée. Standard : correction autonome. Approfondissement : proposer une variante acceptable et la justifier.

## Statut de revue
Document réel de première tranche, non publié et non validé. Une revue humaine indépendante reste nécessaire avant toute promotion de statut.
