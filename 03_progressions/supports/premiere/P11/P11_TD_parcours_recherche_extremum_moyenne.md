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
- O1 : appliquer les méthodes de la fiche à une donnée différente.
- O2 : distinguer lecture d'information, production et justification.
- O3 : traiter au moins un cas limite sans le masquer.
- O4 : préparer une correction exploitable en séance.

## Capacités officielles
- P-ALGO-01A
- P-ALGO-01B

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/premiere/P11/P11_fiche_cours_parcours_recherche_extremum_moyenne.md`.
- Séance liée : `P11-S1` dans la progression annuelle.
- Statut : support créé en `needs_review`, non validé pédagogiquement et non publiable.

## Situation de travail
une station météo fournit les températures [18, 21, 19, 21, 17, 22, 20] et il faut produire occurrence, maximum et moyenne contrôlée.

## Données de référence
Tableau T = [18, 21, 19, 21, 17, 22, 20], seuil = 20, tableau U = [-3, -7, -2, -5], tableau V = [].

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée et vocabulaire.
- Standard : exercices 3 à 6, production écrite avec contrôle.
- Approfondissement : exercices 7 et 8, comparaison de démarches et généralisation.

## Exercices
### Exercice 1 - Compter les occurrences de 21 par parcours complet
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : P-ALGO-01A.
- Données : Tableau T = [18, 21, 19, 21, 17, 22, 20], seuil = 20, tableau U = [-3, -7, -2, -5], tableau V = [].
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de compter les occurrences de 21 par parcours complet.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 2 - Rechercher le premier indice où une valeur dépasse le seuil 20
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : P-ALGO-01B.
- Données : Tableau T = [18, 21, 19, 21, 17, 22, 20], seuil = 20, tableau U = [-3, -7, -2, -5], tableau V = [].
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de rechercher le premier indice où une valeur dépasse le seuil 20.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 3 - Écrire une fonction maximum qui accepte des valeurs négatives
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : P-ALGO-01A.
- Données : Tableau T = [18, 21, 19, 21, 17, 22, 20], seuil = 20, tableau U = [-3, -7, -2, -5], tableau V = [].
- Consigne : Produis une réponse opérationnelle pour écrire une fonction maximum qui accepte des valeurs négatives, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 4 - Écrire une fonction moyenne qui refuse le tableau vide
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : P-ALGO-01B.
- Données : Tableau T = [18, 21, 19, 21, 17, 22, 20], seuil = 20, tableau U = [-3, -7, -2, -5], tableau V = [].
- Consigne : Produis une réponse opérationnelle pour écrire une fonction moyenne qui refuse le tableau vide, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 5 - Traiter explicitement le cas limite tableau vide
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : P-ALGO-01A.
- Données : Tableau T = [18, 21, 19, 21, 17, 22, 20], seuil = 20, tableau U = [-3, -7, -2, -5], tableau V = [].
- Consigne : Traite le cas limite demandé pour traiter explicitement le cas limite tableau vide et précise la convention retenue.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 6 - Justifier l’invariant maximum courant après chaque itération
- Type : justification.
- Niveau : standard.
- Capacité officielle : P-ALGO-01B.
- Données : Tableau T = [18, 21, 19, 21, 17, 22, 20], seuil = 20, tableau U = [-3, -7, -2, -5], tableau V = [].
- Consigne : Justifie pourquoi la méthode utilisée pour justifier l’invariant maximum courant après chaque itération est correcte dans ce contexte.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 7 - Analyser une solution qui initialise le maximum à 0
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : P-ALGO-01A.
- Données : Tableau T = [18, 21, 19, 21, 17, 22, 20], seuil = 20, tableau U = [-3, -7, -2, -5], tableau V = [].
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de analyser une solution qui initialise le maximum à 0.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 8 - Produire un jeu de tests pour occurrence, extremum et moyenne
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : P-ALGO-01B.
- Données : Tableau T = [18, 21, 19, 21, 17, 22, 20], seuil = 20, tableau U = [-3, -7, -2, -5], tableau V = [].
- Consigne : Produis une réponse opérationnelle pour produire un jeu de tests pour occurrence, extremum et moyenne, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : P-ALGO-01A.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P11 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « compter les occurrences de 21 par parcours complet » en utilisant le vocabulaire parcours recherche extremum moyenne.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 2
- Capacité mobilisée : P-ALGO-01B.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P11 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « rechercher le premier indice où une valeur dépasse le seuil 20 » en utilisant le vocabulaire parcours recherche extremum moyenne.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 3
- Capacité mobilisée : P-ALGO-01A.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P11 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « écrire une fonction maximum qui accepte des valeurs négatives » en utilisant le vocabulaire parcours recherche extremum moyenne.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 4
- Capacité mobilisée : P-ALGO-01B.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P11 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « écrire une fonction moyenne qui refuse le tableau vide » en utilisant le vocabulaire parcours recherche extremum moyenne.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 5
- Capacité mobilisée : P-ALGO-01A.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P11 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « traiter explicitement le cas limite tableau vide » en utilisant le vocabulaire parcours recherche extremum moyenne.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 6
- Capacité mobilisée : P-ALGO-01B.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P11 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « justifier l’invariant maximum courant après chaque itération » en utilisant le vocabulaire parcours recherche extremum moyenne.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 7
- Capacité mobilisée : P-ALGO-01A.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P11 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « analyser une solution qui initialise le maximum à 0 » en utilisant le vocabulaire parcours recherche extremum moyenne.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 8
- Capacité mobilisée : P-ALGO-01B.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P11 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « produire un jeu de tests pour occurrence, extremum et moyenne » en utilisant le vocabulaire parcours recherche extremum moyenne.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.

## Erreurs fréquentes
- EF1 : recopier une définition sans l'appliquer à la donnée ; remédiation : entourer les valeurs utilisées avant d'écrire.
- EF2 : produire un résultat sans contrôle ; remédiation : ajouter une ligne « vérification » à chaque réponse.
- EF3 : confondre cas nominal et cas limite ; remédiation : refaire l'exercice 5 avec une donnée minimale.
- EF4 : citer la capacité officielle sans méthode ; remédiation : associer chaque capacité à une action observable.

## Différenciation
- Socle : fournir la donnée annotée et demander une phrase de conclusion.
- Standard : demander la méthode complète et le contrôle écrit.
- Approfondissement : demander une variante de donnée et une comparaison de deux démarches.

## Lien avec la progression
| Élément | Référence | Statut |
|---|---|---|
| Fiche | P11_fiche_cours_parcours_recherche_extremum_moyenne.md | needs_review |
| Séance | P11-S1 | progression existante |
| Évaluation | P11_evaluation_parcours_recherche_extremum_moyenne.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans `/home/alaeddine/Documents/NSI/Documents_DRIVE` avant création.
- Aucun fichier Drive n'a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
