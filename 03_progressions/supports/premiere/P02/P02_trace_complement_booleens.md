---
title: "P02 - trace - Complément à deux et tables de vérité"
level: "premiere"
sequence_id: "P02"
document_type: "trace"
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

# P02 - trace - Complément à deux et tables de vérité

## Objectifs
- Comprendre la notion : entiers relatifs, débordement, booléens.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : P-DATA-BASE-02A, P-DATA-BASE-02B, P-DATA-BASE-04.

## Capacités officielles
- P-DATA-BASE-02A
- P-DATA-BASE-02B
- P-DATA-BASE-04
## Notions essentielles
Cette trace fixe les définitions et les gestes à refaire sans le support de cours.

## Exemple
Sur 8 bits, `-7` se code par `256-7=249`, donc `11111001`. Pour décoder `11111001`, le bit de poids fort vaut 1, donc on calcule `249-256=-7`.

## Méthode à savoir refaire
1. Nommer la convention.
2. Écrire l'entrée et la sortie attendue.
3. Justifier chaque transformation.
4. Vérifier par calcul inverse, test ou table complète.

## Exercices
Encoder `5`, `-1` et `-8` sur 8 bits, puis dresser la table de vérité de `(a and b) or (a and not b)`.

## Corrigé
La correction vérifie la taille du registre, le bit de signe, le calcul de débordement et les quatre lignes de la table de vérité.

## Erreurs fréquentes
- Recopier un résultat sans justification.
- Oublier le cas limite demandé.
- Utiliser un vocabulaire imprécis.

## Remédiation
Relire la méthode, refaire l'exemple avec une valeur voisine, puis écrire une phrase de justification complète.

## Différenciation
Socle : méthode en quatre étapes. Standard : exercice voisin. Approfondissement : inventer une question qui piège une erreur fréquente.

## Statut de revue
Document réel de première tranche, non publié et non validé. Une revue humaine indépendante reste nécessaire avant toute promotion de statut.
