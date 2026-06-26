---
title: "P00 - cours - Diagnostic Python et carnet de bord"
level: "premiere"
sequence_id: "P00"
document_type: "cours"
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

# P00 - cours - Diagnostic Python et carnet de bord

## Objectifs
- Comprendre la notion : diagnostic Python, lecture de consignes, carnet de bord.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : P-HIST-01, P-LANG-01.

## Capacités officielles
- P-HIST-01
- P-LANG-01
## Situation-problème
Une classe commence l'année avec des niveaux Python hétérogènes. La séance doit repérer les acquis sans classer les élèves, puis installer une méthode commune pour conserver les traces de tests, d'erreurs et de progrès.

## Déroulé proposé
1. Question flash individuelle sur la notion.
2. Mise en commun des critères de réussite.
3. Exemple guidé au tableau avec verbalisation de la méthode.
4. Exercice court réalisé seul puis comparé en binôme.
5. Synthèse écrite dans la trace.

## Exemple
On lit le programme `x = 3; x = x + 2; print(x)`. La réponse attendue est `5`, mais la justification doit préciser que la deuxième affectation remplace l'ancienne valeur de `x`.

## Méthode
- Identifier la donnée manipulée et la convention utilisée.
- Écrire les étapes intermédiaires, pas seulement le résultat.
- Vérifier la réponse avec une méthode inverse ou un test simple.

## Exercices
Lire trois fragments Python courts, prédire la sortie, exécuter si possible, puis noter dans le carnet l'écart entre prédiction et sortie réelle.

## Corrigé
Une réponse est correcte si elle distingue valeur initiale, nouvelle affectation et affichage. L'erreur la plus fréquente consiste à lire `=` comme une égalité mathématique permanente.

## Erreurs fréquentes
- Donner un résultat sans convention ou sans taille de registre.
- Confondre écriture et valeur représentée.
- Tester seulement un cas ordinaire et oublier un cas limite.

## Remédiation
Reprendre un exemple plus petit, faire verbaliser la convention, puis demander une vérification par la méthode inverse.

## Différenciation
Socle : un exemple guidé et une grille de méthode. Standard : trois exercices autonomes. Approfondissement : produire un contre-exemple ou un test de bord.

## Statut de revue
Document réel de première tranche, non publié et non validé. Une revue humaine indépendante reste nécessaire avant toute promotion de statut.
