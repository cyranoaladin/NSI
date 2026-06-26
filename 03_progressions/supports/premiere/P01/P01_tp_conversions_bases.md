---
title: "P01 - TP - Conversions de bases et écriture positionnelle"
level: "premiere"
sequence_id: "P01"
document_type: "tp"
status: "needs_review"
version: "0.1.0"
source: "BO 2019 ; source possible Drive : Documents_DRIVE/Algo_Premiere/Cours.pdf"
theme: "Représentation des données"
notion: "bases 2, 10 et 16"
objectifs: ["Travailler la capacité ciblée", "Produire une trace vérifiable", "Identifier les erreurs fréquentes"]
private_data: false
official_program:
  capacities: ["P-DATA-BASE-01"]
---

# P01 - TP - Conversions de bases et écriture positionnelle

## Objectifs
- Comprendre la notion : bases 2, 10 et 16.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : P-DATA-BASE-01.

## Capacités officielles
- P-DATA-BASE-01
## Fichiers et environnement
Le travail peut être réalisé dans un fichier Python local ou dans le carnet de bord selon la salle disponible.

## Exemple
Pour convertir `45` en base 2, les divisions donnent les restes `1,0,1,1,0,1`; lus en sens inverse, ils donnent `101101₂`. La vérification calcule `32+8+4+1=45`.

## Travail demandé
- Lire l'énoncé et repérer l'entrée, la sortie et les cas limites.
- Écrire ou compléter une fonction courte.
- Prévoir deux tests ordinaires et un test de bord.
- Copier la sortie des tests dans le carnet.

## Exercices
Convertir `19`, `31` et `64` en base 2, puis convertir `2A₁₆` et `FF₁₆` en base 10 avec développement des puissances.

## Corrigé
Le barème valorise le développement en puissances ou les divisions successives. Une écriture sans méthode visible reste partielle, même si le résultat numérique est juste.

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
