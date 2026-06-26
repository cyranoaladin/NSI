---
title: "P02 - TD - Complément à deux et tables de vérité"
level: "premiere"
sequence_id: "P02"
document_type: "td"
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

# P02 - TD - Complément à deux et tables de vérité

## Objectifs
- Comprendre la notion : entiers relatifs, débordement, booléens.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : P-DATA-BASE-02A, P-DATA-BASE-02B, P-DATA-BASE-04.

## Capacités officielles
- P-DATA-BASE-02A
- P-DATA-BASE-02B
- P-DATA-BASE-04
## Consignes
Répondre sur feuille ou cahier. Chaque réponse doit contenir une justification courte.

## Exemple
Sur 8 bits, `-7` se code par `256-7=249`, donc `11111001`. Pour décoder `11111001`, le bit de poids fort vaut 1, donc on calcule `249-256=-7`.

## Exercices
1. Question socle : reprendre l'exemple avec une valeur voisine.
2. Question standard : résoudre le cas nouveau et expliquer la méthode.
3. Question standard : comparer deux réponses d'élèves et choisir la plus solide.
4. Question approfondissement : produire un cas limite et sa correction.

## Corrigé
La correction vérifie la taille du registre, le bit de signe, le calcul de débordement et les quatre lignes de la table de vérité.

## Justification attendue
La correction doit faire apparaître les étapes, le vocabulaire de la capacité et une vérification.

## Erreurs fréquentes
- Répondre par intuition sans preuve.
- Mélanger deux conventions.
- Ne pas vérifier la cohérence du résultat.

## Remédiation
Faire traiter seulement les questions 1 et 2, puis demander une verbalisation orale avant l'écrit.

## Différenciation
Socle : questions 1 et 2. Standard : questions 1 à 3. Approfondissement : question 4 et production d'une variante.

## Statut de revue
Document réel de première tranche, non publié et non validé. Une revue humaine indépendante reste nécessaire avant toute promotion de statut.
