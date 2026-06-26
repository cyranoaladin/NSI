---
title: "P12 - TD - tris invariants complexité"
level: "premiere"
sequence_id: "P12"
document_type: "td"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Algorithmique"
notion: "tris invariants complexité"
objectifs:
  - "travailler tris invariants complexité sur des données explicites"
  - "produire une réponse justifiée et contrôlée"
  - "identifier les cas limites"
  - "corriger les erreurs fréquentes du chapitre"
private_data: false
official_program:
  capacities:
    - "P-ALGO-02A"
    - "P-ALGO-02B"
    - "P-ALGO-02C"
    - "P-ALGO-02D"
---
# P12 - TD - tris invariants complexité

## Objectifs
- O1 : appliquer les méthodes de la fiche à une donnée différente.
- O2 : distinguer lecture d'information, production et justification.
- O3 : traiter au moins un cas limite sans le masquer.
- O4 : préparer une correction exploitable en séance.

## Capacités officielles
- P-ALGO-02A
- P-ALGO-02B
- P-ALGO-02C
- P-ALGO-02D

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/premiere/P12/P12_fiche_cours_tris_invariants_complexite.md`.
- Séance liée : `P12-S1` dans la progression annuelle.
- Statut : support créé en `needs_review`, non validé pédagogiquement et non publiable.

## Situation de travail
une liste de temps de course [42, 37, 51, 37, 46] doit être triée en conservant les doublons et en expliquant l’invariant.

## Données de référence
Liste L = [42, 37, 51, 37, 46], liste déjà triée A = [3, 5, 8], liste inversée B = [9, 7, 4, 1].

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée et vocabulaire.
- Standard : exercices 3 à 6, production écrite avec contrôle.
- Approfondissement : exercices 7 et 8, comparaison de démarches et généralisation.

## Exercices
### Exercice 1 - Tracer le tri par insertion sur les deux premières insertions
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : P-ALGO-02A.
- Données : Liste L = [42, 37, 51, 37, 46], liste déjà triée A = [3, 5, 8], liste inversée B = [9, 7, 4, 1].
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de tracer le tri par insertion sur les deux premières insertions.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 2 - Tracer le tri par sélection en indiquant l’indice du minimum
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : P-ALGO-02B.
- Données : Liste L = [42, 37, 51, 37, 46], liste déjà triée A = [3, 5, 8], liste inversée B = [9, 7, 4, 1].
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de tracer le tri par sélection en indiquant l’indice du minimum.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 3 - Écrire le pseudo-code du décalage dans le tri par insertion
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : P-ALGO-02C.
- Données : Liste L = [42, 37, 51, 37, 46], liste déjà triée A = [3, 5, 8], liste inversée B = [9, 7, 4, 1].
- Consigne : Produis une réponse opérationnelle pour écrire le pseudo-code du décalage dans le tri par insertion, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 4 - Écrire le pseudo-code de l’échange dans le tri par sélection
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : P-ALGO-02D.
- Données : Liste L = [42, 37, 51, 37, 46], liste déjà triée A = [3, 5, 8], liste inversée B = [9, 7, 4, 1].
- Consigne : Produis une réponse opérationnelle pour écrire le pseudo-code de l’échange dans le tri par sélection, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 5 - Traiter le cas limite liste vide et liste avec doublons
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : P-ALGO-02A.
- Données : Liste L = [42, 37, 51, 37, 46], liste déjà triée A = [3, 5, 8], liste inversée B = [9, 7, 4, 1].
- Consigne : Traite le cas limite demandé pour traiter le cas limite liste vide et liste avec doublons et précise la convention retenue.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 6 - Justifier l’invariant de la partie triée pour insertion
- Type : justification.
- Niveau : standard.
- Capacité officielle : P-ALGO-02B.
- Données : Liste L = [42, 37, 51, 37, 46], liste déjà triée A = [3, 5, 8], liste inversée B = [9, 7, 4, 1].
- Consigne : Justifie pourquoi la méthode utilisée pour justifier l’invariant de la partie triée pour insertion est correcte dans ce contexte.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 7 - Comparer le nombre de comparaisons sur liste inversée
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : P-ALGO-02C.
- Données : Liste L = [42, 37, 51, 37, 46], liste déjà triée A = [3, 5, 8], liste inversée B = [9, 7, 4, 1].
- Consigne : Lis la donnée, surligne l'information utile puis rédige l'analyse qui permet de comparer le nombre de comparaisons sur liste inversée.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.
### Exercice 8 - Expliquer pourquoi le coût reste quadratique au pire cas
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : P-ALGO-02D.
- Données : Liste L = [42, 37, 51, 37, 46], liste déjà triée A = [3, 5, 8], liste inversée B = [9, 7, 4, 1].
- Consigne : Produis une réponse opérationnelle pour expliquer pourquoi le coût reste quadratique au pire cas, avec pseudo-code, requête ou schéma si le thème l'exige.
- Production attendue : une réponse structurée en donnée, méthode, résultat, contrôle.
- Critère de réussite : le résultat peut être vérifié sans demander l'intention de l'élève.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : P-ALGO-02A.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P12 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « tracer le tri par insertion sur les deux premières insertions » en utilisant le vocabulaire tris invariants complexité.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 2
- Capacité mobilisée : P-ALGO-02B.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P12 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « tracer le tri par sélection en indiquant l’indice du minimum » en utilisant le vocabulaire tris invariants complexité.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 3
- Capacité mobilisée : P-ALGO-02C.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P12 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « écrire le pseudo-code du décalage dans le tri par insertion » en utilisant le vocabulaire tris invariants complexité.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 4
- Capacité mobilisée : P-ALGO-02D.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P12 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « écrire le pseudo-code de l’échange dans le tri par sélection » en utilisant le vocabulaire tris invariants complexité.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 5
- Capacité mobilisée : P-ALGO-02A.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P12 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « traiter le cas limite liste vide et liste avec doublons » en utilisant le vocabulaire tris invariants complexité.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 6
- Capacité mobilisée : P-ALGO-02B.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P12 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « justifier l’invariant de la partie triée pour insertion » en utilisant le vocabulaire tris invariants complexité.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 7
- Capacité mobilisée : P-ALGO-02C.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P12 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « comparer le nombre de comparaisons sur liste inversée » en utilisant le vocabulaire tris invariants complexité.
- Contrôle : une réponse sans donnée citée, sans étape intermédiaire ou sans cas limite n'est pas complète.
### Corrigé exercice 8
- Capacité mobilisée : P-ALGO-02D.
- Démarche : partir de la donnée fournie, isoler les grandeurs utiles, appliquer la méthode du chapitre P12 puis contrôler le résultat.
- Résultat indicatif : l'élève doit obtenir une conclusion explicite sur « expliquer pourquoi le coût reste quadratique au pire cas » en utilisant le vocabulaire tris invariants complexité.
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
| Fiche | P12_fiche_cours_tris_invariants_complexite.md | needs_review |
| Séance | P12-S1 | progression existante |
| Évaluation | P12_evaluation_tris_invariants_complexite.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans `/home/alaeddine/Documents/NSI/Documents_DRIVE` avant création.
- Aucun fichier Drive n'a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
