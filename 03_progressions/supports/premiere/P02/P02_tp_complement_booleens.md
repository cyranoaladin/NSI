---
title: "P02 - TP - Complément à deux et tables de vérité"
level: "premiere"
sequence_id: "P02"
document_type: "tp"
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

# P02 - TP - Complément à deux et tables de vérité

## Objectifs
- Comprendre la notion : entiers relatifs, débordement, booléens.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : P-DATA-BASE-02A, P-DATA-BASE-02B, P-DATA-BASE-04.

## Capacités officielles
- P-DATA-BASE-02A
- P-DATA-BASE-02B
- P-DATA-BASE-04
## Fichiers et environnement
Le travail peut être réalisé dans un fichier Python local ou dans le carnet de bord selon la salle disponible.

## Exemple
Sur 8 bits, `-7` se code par `256-7=249`, donc `11111001`. Pour décoder `11111001`, le bit de poids fort vaut 1, donc on calcule `249-256=-7`.

## Travail demandé
- Lire l'énoncé et repérer l'entrée, la sortie et les cas limites.
- Écrire ou compléter une fonction courte.
- Prévoir deux tests ordinaires et un test de bord.
- Copier la sortie des tests dans le carnet.

## Exercices
Encoder `5`, `-1` et `-8` sur 8 bits, puis dresser la table de vérité de `(a and b) or (a and not b)`.

## Corrigé
La correction vérifie la taille du registre, le bit de signe, le calcul de débordement et les quatre lignes de la table de vérité.

## Tests minimaux
Un test ordinaire, un test limite et un test d'erreur contrôlée doivent être écrits ou expliqués.

## Erreurs fréquentes
- Tester seulement le cas donné dans l'énoncé.
- Modifier l'interface demandée au lieu de corriger l'implémentation.
- Ne pas noter la sortie obtenue.

## Remédiation
Fournir une fonction presque complète et demander d'ajouter seulement les tests manquants.

## Différenciation
Socle : squelette guidé. Standard : fonction et tests. Approfondissement : ajout d'un test qui échoue avant correction.

## Statut de revue
Document réel de première tranche, non publié et non validé. Une revue humaine indépendante reste nécessaire avant toute promotion de statut.
