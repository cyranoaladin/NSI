---
title: "T18 - TD - Boyer-Moore"
level: "terminale"
sequence_id: "T18"
document_type: "td"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Algorithmique"
notion: "Boyer-Moore"
objectifs:
  - "travailler Boyer-Moore sur des données explicites"
  - "produire une réponse justifiée et contrôlée"
  - "identifier les cas limites"
  - "corriger les erreurs fréquentes du chapitre"
private_data: false
official_program:
  capacities:
    - "T-ALGO-05"
---
# T18 - TD - Boyer-Moore

## Objectifs
- O1 : appliquer les méthodes de la fiche à une donnée différente.
- O2 : distinguer lecture d'information, production et justification.
- O3 : traiter au moins un cas limite sans le masquer.
- O4 : préparer une correction exploitable en séance.

## Capacités officielles
- T-ALGO-05

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T18/T18_fiche_cours_boyer_moore.md`.
- Séance liée : `T18-S1` dans la progression annuelle.
- Statut : support créé en `needs_review`, non validé pédagogiquement et non publiable.

## Situation de travail
on cherche le motif "INFO" dans le texte "NSI-INFORMATIQUE" avec une table de mauvais caractère simplifiée.

## Données de référence
Texte = NSI-INFORMATIQUE, motif = INFO, table décalage : I->3, N->2, F->1, O->4, autre->4.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée et vocabulaire.
- Standard : exercices 3 à 6, production écrite avec contrôle.
- Approfondissement : exercices 7 et 8, comparaison de démarches et généralisation.

## Exercices
### Exercice 1 - Lire l’alignement texte-motif au premier essai
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-ALGO-05.
- Données : Texte = NSI-INFORMATIQUE, motif = INFO, table décalage : I->3, N->2, F->1, O->4, autre->4.
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de lire l’alignement texte-motif au premier essai.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 2 - Analyser une comparaison de droite à gauche
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-ALGO-05.
- Données : Texte = NSI-INFORMATIQUE, motif = INFO, table décalage : I->3, N->2, F->1, O->4, autre->4.
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de analyser une comparaison de droite à gauche.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 3 - Produire la table de décalage du motif info
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-ALGO-05.
- Données : Texte = NSI-INFORMATIQUE, motif = INFO, table décalage : I->3, N->2, F->1, O->4, autre->4.
- Consigne : Produis une réponse opérationnelle pour produire la table de décalage du motif INFO, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 4 - Écrire les décalages successifs jusqu’à occurrence
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-ALGO-05.
- Données : Texte = NSI-INFORMATIQUE, motif = INFO, table décalage : I->3, N->2, F->1, O->4, autre->4.
- Consigne : Produis une réponse opérationnelle pour écrire les décalages successifs jusqu’à occurrence, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 5 - Traiter le cas limite motif plus long que le texte
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : T-ALGO-05.
- Données : Texte = NSI-INFORMATIQUE, motif = INFO, table décalage : I->3, N->2, F->1, O->4, autre->4.
- Consigne : Traite le cas limite demandé pour traiter le cas limite motif plus long que le texte et précise la convention retenue.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 6 - Justifier pourquoi le décalage ne saute pas une occurrence possible
- Type : justification.
- Niveau : standard.
- Capacité officielle : T-ALGO-05.
- Données : Texte = NSI-INFORMATIQUE, motif = INFO, table décalage : I->3, N->2, F->1, O->4, autre->4.
- Consigne : Justifie pourquoi la méthode utilisée pour justifier pourquoi le décalage ne saute pas une occurrence possible est correcte dans ce contexte.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 7 - Comparer recherche naïve et boyer-moore sur le même texte
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : T-ALGO-05.
- Données : Texte = NSI-INFORMATIQUE, motif = INFO, table décalage : I->3, N->2, F->1, O->4, autre->4.
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de comparer recherche naïve et Boyer-Moore sur le même texte.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 8 - Repérer une erreur de table qui décale de 0
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : T-ALGO-05.
- Données : Texte = NSI-INFORMATIQUE, motif = INFO, table décalage : I->3, N->2, F->1, O->4, autre->4.
- Consigne : Produis une réponse opérationnelle pour repérer une erreur de table qui décale de 0, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : T-ALGO-05.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T18 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « lire l’alignement texte-motif au premier essai » en utilisant le vocabulaire Boyer-Moore.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 2
- Capacité mobilisée : T-ALGO-05.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T18 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « analyser une comparaison de droite à gauche » en utilisant le vocabulaire Boyer-Moore.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 3
- Capacité mobilisée : T-ALGO-05.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T18 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « produire la table de décalage du motif INFO » en utilisant le vocabulaire Boyer-Moore.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 4
- Capacité mobilisée : T-ALGO-05.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T18 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « écrire les décalages successifs jusqu’à occurrence » en utilisant le vocabulaire Boyer-Moore.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 5
- Capacité mobilisée : T-ALGO-05.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T18 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « traiter le cas limite motif plus long que le texte » en utilisant le vocabulaire Boyer-Moore.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 6
- Capacité mobilisée : T-ALGO-05.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T18 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « justifier pourquoi le décalage ne saute pas une occurrence possible » en utilisant le vocabulaire Boyer-Moore.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 7
- Capacité mobilisée : T-ALGO-05.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T18 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « comparer recherche naïve et Boyer-Moore sur le même texte » en utilisant le vocabulaire Boyer-Moore.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 8
- Capacité mobilisée : T-ALGO-05.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre T18 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « repérer une erreur de table qui décale de 0 » en utilisant le vocabulaire Boyer-Moore.
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
| Fiche | T18_fiche_cours_boyer_moore.md | needs_review |
| Séance | T18-S1 | progression existante |
| Évaluation | T18_evaluation_boyer_moore.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans `/home/alaeddine/Documents/NSI/Documents_DRIVE` avant création.
- Aucun fichier Drive n'a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
