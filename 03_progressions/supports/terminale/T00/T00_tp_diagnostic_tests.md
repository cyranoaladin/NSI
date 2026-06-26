---
title: "T00 - TP - Diagnostic Terminale, tests et complexité simple"
level: "terminale"
sequence_id: "T00"
document_type: "tp"
status: "needs_review"
version: "0.1.0"
source: "BO 2019 ; source possible Drive : Documents_DRIVE/2_Tles NSI/1_Révisions_Python/Révisions_python.odt"
theme: "Rentrée Terminale"
notion: "révisions Python, tests, estimation de coût"
objectifs: ["Travailler la capacité ciblée", "Produire une trace vérifiable", "Identifier les erreurs fréquentes"]
private_data: false
official_program:
  capacities: ["T-HIST-01A", "T-HIST-01B", "T-LANG-03A", "T-LANG-05"]
---

# T00 - TP - Diagnostic Terminale, tests et complexité simple

## Objectifs
- Comprendre la notion : révisions Python, tests, estimation de coût.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : T-HIST-01A, T-HIST-01B, T-LANG-03A, T-LANG-05.

## Capacités officielles
- T-HIST-01A
- T-HIST-01B
- T-LANG-03A
- T-LANG-05
## Fichiers et environnement
Le travail peut être réalisé dans un fichier Python local ou dans le carnet de bord selon la salle disponible.

## Exemple
La fonction qui additionne les éléments d'une liste vide doit renvoyer `0`. Ce cas limite est plus informatif qu'un seul test avec `[1,2,3]`.

## Travail demandé
- Lire l'énoncé et repérer l'entrée, la sortie et les cas limites.
- Écrire ou compléter une fonction courte.
- Prévoir deux tests ordinaires et un test de bord.
- Copier la sortie des tests dans le carnet.

## Exercices
Proposer trois tests pour une fonction `maximum`, dont une liste d'un élément, une liste de nombres négatifs et une liste contenant plusieurs fois le maximum.

## Corrigé
Une réponse complète associe chaque test à l'erreur ciblée : oubli du cas vide, initialisation à zéro ou confusion entre valeur et indice.

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
