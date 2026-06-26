---
title: "P00 - TP - Diagnostic Python et carnet de bord"
level: "premiere"
sequence_id: "P00"
document_type: "tp"
status: "needs_review"
version: "0.1.0"
source: "BO 2019 ; source possible Drive : Documents_DRIVE/1_1ères NSI/1_Rentrée/2_Introduction_NSI.pdf"
theme: "Rentrée et méthode de travail"
notion: "diagnostic Python, lecture de consignes, carnet de bord"
objectifs: ["Travailler la capacité ciblée", "Produire une trace vérifiable", "Identifier les erreurs fréquentes"]
private_data: false
official_program:
  capacities: ["P-HIST-01", "P-LANG-01"]
---

# P00 - TP - Diagnostic Python et carnet de bord

## Objectifs
- Comprendre la notion : diagnostic Python, lecture de consignes, carnet de bord.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : P-HIST-01, P-LANG-01.

## Capacités officielles
- P-HIST-01
- P-LANG-01
## Fichiers et environnement
Le travail peut être réalisé dans un fichier Python local ou dans le carnet de bord selon la salle disponible.

## Exemple
On lit le programme `x = 3; x = x + 2; print(x)`. La réponse attendue est `5`, mais la justification doit préciser que la deuxième affectation remplace l'ancienne valeur de `x`.

## Travail demandé
- Lire l'énoncé et repérer l'entrée, la sortie et les cas limites.
- Écrire ou compléter une fonction courte.
- Prévoir deux tests ordinaires et un test de bord.
- Copier la sortie des tests dans le carnet.

## Exercices
Lire trois fragments Python courts, prédire la sortie, exécuter si possible, puis noter dans le carnet l'écart entre prédiction et sortie réelle.

## Corrigé
Une réponse est correcte si elle distingue valeur initiale, nouvelle affectation et affichage. L'erreur la plus fréquente consiste à lire `=` comme une égalité mathématique permanente.

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
