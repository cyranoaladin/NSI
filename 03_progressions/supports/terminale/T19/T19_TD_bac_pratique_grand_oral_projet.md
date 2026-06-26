---
title: "T19 - TD - bac pratique grand oral projet"
level: "terminale"
sequence_id: "T19"
document_type: "td"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Synthèse"
notion: "bac pratique grand oral projet"
objectifs:
  - "travailler bac pratique grand oral projet sur des données explicites"
  - "produire une réponse justifiée et contrôlée"
  - "identifier les cas limites"
  - "corriger les erreurs fréquentes du chapitre"
private_data: false
official_program:
  capacities:
    - "T-LANG-05"
---

# T19 - TD - bac pratique grand oral projet

## Objectifs
- Lire une donnée disciplinaire précise avant de répondre.
- Produire une méthode vérifiable et un résultat contrôlable.
- Traiter un cas limite sans le transformer en généralité.
- Relier chaque correction à une erreur fréquente observable.

## Capacités officielles
- T-LANG-05

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T19/T19_fiche_cours_bac_pratique_grand_oral_projet.md`.
- Séance liée : `T19-S1` dans la progression annuelle.
- Statut : support `needs_review`, non validé et non publiable.

## Situation de travail
Préparation finale: exercice pratique Python, analyse de complexité et oral de projet.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée.
- Standard : exercices 3 à 6, production écrite et justification.
- Approfondissement : exercices 7 et 8, transfert ou comparaison.

## Exercices
### Exercice 1 - Lire un sujet pratique
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-LANG-05.
- Données : Écrire occurrence(valeurs, x) qui compte x dans valeurs.
- Consigne : Identifier entrée/sortie.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 2 - Analyser un test
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-LANG-05.
- Données : assert occurrence([1,2,1],1)==2 ; assert occurrence([],3)==0.
- Consigne : Dire les cas couverts.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 3 - Écrire la fonction
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-LANG-05.
- Données : valeurs=[4,4,2], x=4.
- Consigne : Donner code.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 4 - Préparer explication orale
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-LANG-05.
- Données : Fonction occurrence.
- Consigne : Plan en 45 secondes.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 5 - Entrée vide
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : T-LANG-05.
- Données : occurrence([],5).
- Consigne : Donner résultat.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 6 - Justifier complexité
- Type : justification.
- Niveau : standard.
- Capacité officielle : T-LANG-05.
- Données : liste longueur n.
- Consigne : Donner ordre.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 7 - Évaluer une réponse orale
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : T-LANG-05.
- Données : Un élève donne code mais aucun test ni complexité.
- Consigne : Identifier manque.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 8 - Relier projet et programme
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : T-LANG-05.
- Données : Projet: moteur de recherche de mots.
- Consigne : Faire le lien.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : T-LANG-05.
- Donnée utilisée : Écrire occurrence(valeurs, x) qui compte x dans valeurs.
- Résultat attendu : Entrée: liste valeurs et cible x. Sortie: entier nombre d’occurrences. Exemple [1,2,1],1 -> 2.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 2
- Capacité mobilisée : T-LANG-05.
- Donnée utilisée : assert occurrence([1,2,1],1)==2 ; assert occurrence([],3)==0.
- Résultat attendu : Cas nominal avec doublon et cas limite liste vide.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 3
- Capacité mobilisée : T-LANG-05.
- Donnée utilisée : valeurs=[4,4,2], x=4.
- Résultat attendu : def occurrence(valeurs,x): c=0 ; for v in valeurs: if v==x: c+=1 ; return c. Résultat 2.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 4
- Capacité mobilisée : T-LANG-05.
- Donnée utilisée : Fonction occurrence.
- Résultat attendu : Dire contrat, boucle et invariant c compte les occurrences déjà lues, puis complexité O(n).
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 5
- Capacité mobilisée : T-LANG-05.
- Donnée utilisée : occurrence([],5).
- Résultat attendu : La boucle ne s’exécute pas ; c reste 0 ; résultat 0.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 6
- Capacité mobilisée : T-LANG-05.
- Donnée utilisée : liste longueur n.
- Résultat attendu : Chaque élément est comparé une fois à x ; temps O(n), mémoire O(1).
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 7
- Capacité mobilisée : T-LANG-05.
- Donnée utilisée : Un élève donne code mais aucun test ni complexité.
- Résultat attendu : Il manque au moins un test nominal, un test limite et l’analyse O(n). La réponse n’est pas complète pour le bac.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 8
- Capacité mobilisée : T-LANG-05.
- Donnée utilisée : Projet: moteur de recherche de mots.
- Résultat attendu : Capacités mobilisées: parcours de chaîne/liste, dictionnaire d’index, tests unitaires, complexité de recherche. Donner une donnée exemple: texte "nsi nsi bac" -> index {"nsi":[0,1],"bac":[2]}.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.

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
| Fiche | T19_fiche_cours_bac_pratique_grand_oral_projet.md | needs_review |
| Séance | T19-S1 | progression existante |
| Évaluation | T19_evaluation_bac_pratique_grand_oral_projet.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans le dossier Documents_DRIVE avant création.
- Aucun fichier Drive n’a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
