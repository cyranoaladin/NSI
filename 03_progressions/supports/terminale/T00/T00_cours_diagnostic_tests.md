---
title: "T00 - cours - Diagnostic Terminale, tests et complexité simple"
level: "terminale"
sequence_id: "T00"
document_type: "cours"
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

# T00 - cours - Diagnostic Terminale, tests et complexité simple

## Objectifs
- Comprendre la notion : révisions Python, tests, estimation de coût.
- Produire une réponse vérifiable et exploitable en classe.
- Relier le travail aux capacités officielles : T-HIST-01A, T-HIST-01B, T-LANG-03A, T-LANG-05.

## Capacités officielles
- T-HIST-01A
- T-HIST-01B
- T-LANG-03A
- T-LANG-05
## Situation-problème
Avant d'aborder les structures abstraites, il faut vérifier que les élèves savent lire une fonction, prévoir un test et repérer une boucle dont le coût augmente avec la taille des données.

## Déroulé proposé
1. Question flash individuelle sur la notion.
2. Mise en commun des critères de réussite.
3. Exemple guidé au tableau avec verbalisation de la méthode.
4. Exercice court réalisé seul puis comparé en binôme.
5. Synthèse écrite dans la trace.

## Exemple
La fonction qui additionne les éléments d'une liste vide doit renvoyer `0`. Ce cas limite est plus informatif qu'un seul test avec `[1,2,3]`.

## Méthode
- Identifier la donnée manipulée et la convention utilisée.
- Écrire les étapes intermédiaires, pas seulement le résultat.
- Vérifier la réponse avec une méthode inverse ou un test simple.

## Exercices
Proposer trois tests pour une fonction `maximum`, dont une liste d'un élément, une liste de nombres négatifs et une liste contenant plusieurs fois le maximum.

## Corrigé
Une réponse complète associe chaque test à l'erreur ciblée : oubli du cas vide, initialisation à zéro ou confusion entre valeur et indice.

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
