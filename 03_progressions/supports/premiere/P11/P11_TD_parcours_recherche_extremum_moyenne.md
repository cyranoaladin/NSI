---
title: "P11 - TD - parcours recherche extremum moyenne"
level: "premiere"
sequence_id: "P11"
document_type: "td"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Algorithmique"
notion: "parcours recherche extremum moyenne"
objectifs:
  - "travailler parcours recherche extremum moyenne sur des données explicites"
  - "produire une réponse justifiée et contrôlée"
  - "identifier les cas limites"
  - "corriger les erreurs fréquentes du chapitre"
private_data: false
official_program:
  capacities:
    - "P-ALGO-01A"
    - "P-ALGO-01B"
---

# P11 - TD - parcours recherche extremum moyenne

## Objectifs
- Lire une donnée disciplinaire précise avant de répondre.
- Produire une méthode vérifiable et un résultat contrôlable.
- Traiter un cas limite sans le transformer en généralité.
- Relier chaque correction à une erreur fréquente observable.

## Capacités officielles
- P-ALGO-01A
- P-ALGO-01B

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/premiere/P11/P11_fiche_cours_parcours_recherche_extremum_moyenne.md`.
- Séance liée : `P11-S1` dans la progression annuelle.
- Statut : support `needs_review`, non validé et non publiable.

## Situation de travail
On analyse des listes de mesures anonymisées produites par un capteur de luminosité.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée.
- Standard : exercices 3 à 6, production écrite et justification.
- Approfondissement : exercices 7 et 8, transfert ou comparaison.

## Exercices
### Exercice 1 - Tracer une recherche séquentielle
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : P-ALGO-01A.
- Données : liste = [12, 7, 19, 7, 3], valeur cherchée = 7.
- Consigne : Donner les indices lus jusqu’à la première occurrence.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 2 - Calculer un maximum avec trace
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : P-ALGO-01B.
- Données : mesures = [4, 11, 6, 11, 2].
- Consigne : Donner la valeur de max après chaque élément.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 3 - Écrire un parcours de moyenne
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : P-ALGO-01A.
- Données : notes = [8, 12, 15, 5].
- Consigne : Écrire un pseudo-code qui renvoie la moyenne.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 4 - Écrire une recherche avec booléen
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : P-ALGO-01B.
- Données : mots = ["NSI", "maths", "SI"], cible="physique".
- Consigne : Produire un algorithme qui renvoie True ou False.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 5 - Traiter la liste vide
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : P-ALGO-01A.
- Données : valeurs = [].
- Consigne : Dire quoi renvoyer pour moyenne et maximum.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 6 - Justifier la complexité
- Type : justification.
- Niveau : standard.
- Capacité officielle : P-ALGO-01B.
- Données : liste de longueur n, recherche séquentielle d’une valeur absente.
- Consigne : Justifier le nombre de comparaisons.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 7 - Comparer deux parcours
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : P-ALGO-01A.
- Données : liste = [5, 1, 9, 2]. Méthode A calcule max puis moyenne en deux boucles ; méthode B fait les deux dans une boucle.
- Consigne : Comparer résultats et nombre de lectures.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 8 - Retourner l’indice du minimum
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : P-ALGO-01B.
- Données : liste = [6, 4, 4, 9].
- Consigne : Écrire la règle en cas d’égalité.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : P-ALGO-01A.
- Donnée utilisée : liste = [12, 7, 19, 7, 3], valeur cherchée = 7.
- Résultat attendu : On lit indice 0 -> 12, puis indice 1 -> 7. La première occurrence est à l’indice 1 ; on peut arrêter la recherche.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 2
- Capacité mobilisée : P-ALGO-01B.
- Donnée utilisée : mesures = [4, 11, 6, 11, 2].
- Résultat attendu : Trace max: départ 4 ; après 11 -> 11 ; après 6 -> 11 ; après 11 -> 11 ; après 2 -> 11. Maximum final 11.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 3
- Capacité mobilisée : P-ALGO-01A.
- Donnée utilisée : notes = [8, 12, 15, 5].
- Résultat attendu : Pseudo-code: somme=0 ; pour x dans notes: somme=somme+x ; moyenne=somme/len(notes). Ici somme=40, len=4, moyenne=10.0.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 4
- Capacité mobilisée : P-ALGO-01B.
- Donnée utilisée : mots = ["NSI", "maths", "SI"], cible="physique".
- Résultat attendu : trouve=False ; pour mot dans mots: si mot==cible alors trouve=True. Aucune égalité trouvée ; résultat False.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 5
- Capacité mobilisée : P-ALGO-01A.
- Donnée utilisée : valeurs = [].
- Résultat attendu : Moyenne et maximum ne sont pas définis sur une liste vide. La fonction doit lever ValueError ou renvoyer None selon le contrat choisi ; elle ne doit pas diviser par 0.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 6
- Capacité mobilisée : P-ALGO-01B.
- Donnée utilisée : liste de longueur n, recherche séquentielle d’une valeur absente.
- Résultat attendu : Si la valeur est absente, tous les éléments sont testés une fois. Il y a n comparaisons, donc une complexité linéaire O(n).
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 7
- Capacité mobilisée : P-ALGO-01A.
- Donnée utilisée : liste = [5, 1, 9, 2]. Méthode A calcule max puis moyenne en deux boucles ; méthode B fait les deux dans une boucle.
- Résultat attendu : Les deux donnent max=9 et moyenne=17/4=4.25. A lit 8 éléments au total ; B lit 4 éléments, donc B est préférable sans changer le résultat.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 8
- Capacité mobilisée : P-ALGO-01B.
- Donnée utilisée : liste = [6, 4, 4, 9].
- Résultat attendu : Pseudo-code: indice_min=0 ; pour i de 1 à 3, si liste[i] < liste[indice_min], remplacer. Avec égalité stricte, résultat indice 1, première occurrence du minimum 4.
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
| Fiche | P11_fiche_cours_parcours_recherche_extremum_moyenne.md | needs_review |
| Séance | P11-S1 | progression existante |
| Évaluation | P11_evaluation_parcours_recherche_extremum_moyenne.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans le dossier Documents_DRIVE avant création.
- Aucun fichier Drive n’a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
