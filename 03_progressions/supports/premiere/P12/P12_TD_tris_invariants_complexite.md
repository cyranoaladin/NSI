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
- Lire une donnée disciplinaire précise avant de répondre.
- Produire une méthode vérifiable et un résultat contrôlable.
- Traiter un cas limite sans le transformer en généralité.
- Relier chaque correction à une erreur fréquente observable.

## Capacités officielles
- P-ALGO-02A
- P-ALGO-02B
- P-ALGO-02C
- P-ALGO-02D

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/premiere/P12/P12_fiche_cours_tris_invariants_complexite.md`.
- Séance liée : `P12-S1` dans la progression annuelle.
- Statut : support `needs_review`, non validé et non publiable.

## Situation de travail
On trie des séries de temps de réponse collectées pendant un TP réseau.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée.
- Standard : exercices 3 à 6, production écrite et justification.
- Approfondissement : exercices 7 et 8, transfert ou comparaison.

## Exercices
### Exercice 1 - Tracer un tri par insertion
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : P-ALGO-02A.
- Données : liste initiale [5, 2, 4, 1].
- Consigne : Donner les états après chaque insertion.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 2 - Reconnaître un invariant
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : P-ALGO-02B.
- Données : Dans le tri par insertion, après l’étape i, le préfixe de longueur i+1 est trié.
- Consigne : Vérifier l’invariant après l’insertion de 4 dans [5,2,4,1].
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 3 - Écrire un tri par sélection
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : P-ALGO-02C.
- Données : liste [3, 1, 4, 2].
- Consigne : Donner pseudo-code et premier échange.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 4 - Compter les comparaisons
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : P-ALGO-02D.
- Données : tri par sélection sur n=5 éléments.
- Consigne : Calculer le nombre de comparaisons.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 5 - Trier une liste déjà triée
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : P-ALGO-02A.
- Données : liste [1, 2, 3, 4].
- Consigne : Comparer insertion et sélection.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 6 - Justifier la terminaison
- Type : justification.
- Niveau : standard.
- Capacité officielle : P-ALGO-02B.
- Données : Boucle pour i allant de 1 à n-1 dans insertion.
- Consigne : Dire pourquoi l’algorithme termine.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 7 - Comparer complexités
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : P-ALGO-02C.
- Données : n=1000, tri quadratique versus tri en n log2 n.
- Consigne : Donner les ordres de grandeur.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 8 - Détecter une erreur d’invariant
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : P-ALGO-02D.
- Données : Un élève écrit: “après chaque échange, toute la liste est triée”.
- Consigne : Corriger l’invariant.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : P-ALGO-02A.
- Donnée utilisée : liste initiale [5, 2, 4, 1].
- Résultat attendu : États: [5,2,4,1] ; insérer 2 -> [2,5,4,1] ; insérer 4 -> [2,4,5,1] ; insérer 1 -> [1,2,4,5].
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 2
- Capacité mobilisée : P-ALGO-02B.
- Donnée utilisée : Dans le tri par insertion, après l’étape i, le préfixe de longueur i+1 est trié.
- Résultat attendu : Après insertion de 4, le préfixe [2,4,5] est trié. L’invariant est vrai pour i=2 ; le suffixe [1] n’est pas encore traité.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 3
- Capacité mobilisée : P-ALGO-02C.
- Donnée utilisée : liste [3, 1, 4, 2].
- Résultat attendu : Pseudo-code: pour i, chercher j_min dans i..n-1 puis échanger. Pour i=0, minimum 1 à j=1, échange -> [1,3,4,2].
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 4
- Capacité mobilisée : P-ALGO-02D.
- Donnée utilisée : tri par sélection sur n=5 éléments.
- Résultat attendu : Comparaisons: 4+3+2+1=10. Formule n(n-1)/2 = 5*4/2 = 10.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 5
- Capacité mobilisée : P-ALGO-02A.
- Donnée utilisée : liste [1, 2, 3, 4].
- Résultat attendu : Insertion ne décale aucun élément et reste très rapide ; sélection effectue quand même 6 comparaisons pour n=4. Le résultat reste [1,2,3,4].
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 6
- Capacité mobilisée : P-ALGO-02B.
- Donnée utilisée : Boucle pour i allant de 1 à n-1 dans insertion.
- Résultat attendu : i augmente d’une unité et n est fini. La boucle interne décale j vers la gauche ; j diminue jusqu’à 0 au plus. Les deux boucles terminent.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 7
- Capacité mobilisée : P-ALGO-02C.
- Donnée utilisée : n=1000, tri quadratique versus tri en n log2 n.
- Résultat attendu : n^2 = 1 000 000 opérations ; n log2 n environ 1000*10=10 000. L’écart justifie un tri plus avancé pour grandes données.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 8
- Capacité mobilisée : P-ALGO-02D.
- Donnée utilisée : Un élève écrit: “après chaque échange, toute la liste est triée”.
- Résultat attendu : Invariant correct pour sélection: après l’itération i, les i+1 plus petits éléments sont placés au début et triés ; le suffixe peut rester non trié.
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
| Fiche | P12_fiche_cours_tris_invariants_complexite.md | needs_review |
| Séance | P12-S1 | progression existante |
| Évaluation | P12_evaluation_tris_invariants_complexite.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans le dossier Documents_DRIVE avant création.
- Aucun fichier Drive n’a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
