---
title: "P01 - cours - Conversions de bases et écriture positionnelle"
level: "premiere"
sequence_id: "P01"
document_type: "cours"
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

# P01 - cours - Conversions de bases et écriture positionnelle

## Objectifs
- Comprendre la notion : bases 2, 10 et 16.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : P-DATA-BASE-01.

## Capacités officielles
- P-DATA-BASE-01
## Situation-problème
Un identifiant de badge peut être affiché en décimal pour l'humain, en binaire pour la machine et en hexadécimal dans une documentation technique. Il faut reconnaître que la valeur reste la même quand l'écriture change.

## Déroulé proposé
1. Question flash individuelle sur la notion.
2. Mise en commun des critères de réussite.
3. Exemple guidé au tableau avec verbalisation de la méthode.
4. Exercice court réalisé seul puis comparé en binôme.
5. Synthèse écrite dans la trace.

## Exemple
Pour convertir `45` en base 2, les divisions donnent les restes `1,0,1,1,0,1`; lus en sens inverse, ils donnent `101101₂`. La vérification calcule `32+8+4+1=45`.

## Méthode
- Identifier la donnée manipulée et la convention utilisée.
- Écrire les étapes intermédiaires, pas seulement le résultat.
- Vérifier la réponse avec une méthode inverse ou un test simple.

## Exercices
Convertir `19`, `31` et `64` en base 2, puis convertir `2A₁₆` et `FF₁₆` en base 10 avec développement des puissances.

## Corrigé
Le barème valorise le développement en puissances ou les divisions successives. Une écriture sans méthode visible reste partielle, même si le résultat numérique est juste.

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
