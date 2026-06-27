---
title: "T14 - TD - modularité API paradigmes bugs"
level: "terminale"
sequence_id: "T14"
document_type: "td"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Langages"
notion: "modularité API paradigmes bugs"
objectifs:
  - "travailler modularité API paradigmes bugs sur des données explicites"
  - "produire une réponse justifiée et contrôlée"
  - "identifier les cas limites"
  - "corriger les erreurs fréquentes du chapitre"
private_data: false
official_program:
  capacities:
    - "T-LANG-03A"
    - "T-LANG-03B"
    - "T-LANG-03C"
    - "T-LANG-04A"
    - "T-LANG-04B"
    - "T-LANG-05"
---

# T14 - TD - modularité API paradigmes bugs

## Objectifs
- Lire une donnée disciplinaire précise avant de répondre.
- Produire une méthode vérifiable et un résultat contrôlable.
- Traiter un cas limite sans le transformer en généralité.
- Relier chaque correction à une erreur fréquente observable.

## Capacités officielles
- T-LANG-03A
- T-LANG-03B
- T-LANG-03C
- T-LANG-04A
- T-LANG-04B
- T-LANG-05

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T14/T14_fiche_cours_modularite_api_paradigmes_bugs.md`.
- Séance liée : `T14-S1` dans la progression annuelle.
- Statut : support `needs_review`, non validé et non publiable.

## Situation de travail
On transforme un script monolithique de notes en module testable.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée.
- Standard : exercices 3 à 6, production écrite et justification.
- Approfondissement : exercices 7 et 8, transfert ou comparaison.

## Exercices
### Exercice 1 - Identifier une API
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-LANG-03A.
- Données : Module notes.py expose moyenne(notes) et mediane(notes).
- Consigne : Dire ce qui appartient à l’API.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 2 - Lire une trace d’erreur
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-LANG-03B.
- Données : TypeError: unsupported operand type(s) for +: int and str dans somme += note.
- Consigne : Identifier la cause.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 3 - Écrire une fonction pure
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-LANG-03C.
- Données : notes=[10,14,16].
- Consigne : Coder moyenne sans effet de bord.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 4 - Ajouter un test unitaire
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-LANG-04A.
- Données : moyenne([10,20]) doit valoir 15.
- Consigne : Écrire un assert.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 5 - Contrat liste vide
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : T-LANG-04B.
- Données : moyenne([]).
- Consigne : Choisir une gestion.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 6 - Justifier la modularité
- Type : justification.
- Niveau : standard.
- Capacité officielle : T-LANG-05.
- Données : Script avec lecture fichier, calcul et affichage mélangés.
- Consigne : Expliquer le découpage.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 7 - Comparer paradigmes
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : T-LANG-03A.
- Données : Calculer les carrés de [1,2,3].
- Consigne : Donner version impérative et fonctionnelle.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 8 - Déboguer mutation non voulue
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : T-LANG-03B.
- Données : fonction ajoute_zero(l) fait l.append(0).
- Consigne : Proposer correction.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : T-LANG-03A.
- Donnée utilisée : Module notes.py expose moyenne(notes) et mediane(notes).
- Résultat attendu : Les signatures moyenne(notes) et mediane(notes), leur contrat d’entrée/sortie et exceptions appartiennent à l’API ; les variables internes non.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 2
- Capacité mobilisée : T-LANG-03B.
- Donnée utilisée : TypeError: unsupported operand type(s) for +: int and str dans somme += note.
- Résultat attendu : Une note est une chaîne comme "12" au lieu d’un entier/float. Il faut convertir ou valider l’entrée.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 3
- Capacité mobilisée : T-LANG-03C.
- Donnée utilisée : notes=[10,14,16].
- Résultat attendu : def moyenne(notes): return sum(notes)/len(notes). Pour [10,14,16], résultat 40/3 environ 13.33 ; la liste n’est pas modifiée.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 4
- Capacité mobilisée : T-LANG-04A.
- Donnée utilisée : moyenne([10,20]) doit valoir 15.
- Résultat attendu : assert moyenne([10,20]) == 15. On ajoute aussi le cas vide selon contrat, par exemple pytest.raises(ValueError).
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 5
- Capacité mobilisée : T-LANG-04B.
- Donnée utilisée : moyenne([]).
- Résultat attendu : Contrat retenu: lever ValueError("liste vide"). Cela évite division par zéro silencieuse.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 6
- Capacité mobilisée : T-LANG-05.
- Donnée utilisée : Script avec lecture fichier, calcul et affichage mélangés.
- Résultat attendu : Séparer lire_csv, moyenne, afficher_resultat permet de tester moyenne sans fichier et de changer l’affichage sans toucher le calcul.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 7
- Capacité mobilisée : T-LANG-03A.
- Donnée utilisée : Calculer les carrés de [1,2,3].
- Résultat attendu : Impératif: boucle append. Fonctionnel: list(map(lambda x: x*x, valeurs)) ou compréhension [x*x for x in valeurs]. Résultat [1,4,9].
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 8
- Capacité mobilisée : T-LANG-03B.
- Donnée utilisée : fonction ajoute_zero(l) fait l.append(0).
- Résultat attendu : Retourner une nouvelle liste: return l + [0]. Ainsi l’entrée originale [1,2] reste [1,2], sortie [1,2,0].
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.

## Erreurs fréquentes
- EF1 : répondre par un mot-clé sans citer la donnée ; remédiation : entourer les valeurs utiles avant de rédiger.
- EF2 : donner un résultat sans méthode ; remédiation : imposer une ligne méthode puis une ligne résultat.
- EF3 : oublier le cas limite ; remédiation : refaire l’exercice 5 avec la donnée minimale.
- EF4 : confondre justification et paraphrase ; remédiation : écrire une phrase qui relie donnée, règle et conclusion.

## Remédiation ciblée
- Reprendre deux exercices en ne gardant que les données numériques ou symboliques.
- Faire corriger une réponse incomplète par un binôme avec une grille donnée/méthode/résultat/contrôle.
- Produire une variante courte avec une donnée changée et vérifier que la méthode reste valable.

## Différenciation
- Socle : fournir les données annotées et demander seulement le résultat contrôlé.
- Standard : demander méthode complète, résultat et contrôle écrit.
- Approfondissement : demander une variante de la donnée et une comparaison de deux démarches.

## Lien avec la progression
| Élément | Référence | Statut |
|---|---|---|
| Fiche | T14_fiche_cours_modularite_api_paradigmes_bugs.md | needs_review |
| Séance | T14-S1 | progression existante |
| Évaluation | T14_evaluation_modularite_api_paradigmes_bugs.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans le dossier Documents_DRIVE avant création.
- Aucun fichier Drive n’a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
