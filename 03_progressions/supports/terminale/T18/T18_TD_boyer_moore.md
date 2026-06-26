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
- Lire une donnée disciplinaire précise avant de répondre.
- Produire une méthode vérifiable et un résultat contrôlable.
- Traiter un cas limite sans le transformer en généralité.
- Relier chaque correction à une erreur fréquente observable.

## Capacités officielles
- T-ALGO-05

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T18/T18_fiche_cours_boyer_moore.md`.
- Séance liée : `T18-S1` dans la progression annuelle.
- Statut : support `needs_review`, non validé et non publiable.

## Situation de travail
On recherche le motif ABA dans le texte CABAABABA.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée.
- Standard : exercices 3 à 6, production écrite et justification.
- Approfondissement : exercices 7 et 8, transfert ou comparaison.

## Exercices
### Exercice 1 - Construire table mauvais caractère
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-ALGO-05.
- Données : motif ABA.
- Consigne : Donner derniers indices.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 2 - Comparer depuis la droite
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-ALGO-05.
- Données : texte CABAABABA, motif ABA aligné au début.
- Consigne : Donner première comparaison.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 3 - Tracer la première occurrence
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-ALGO-05.
- Données : texte CABAABABA, motif ABA.
- Consigne : Donner indice trouvé.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 4 - Écrire pseudo-code simplifié
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-ALGO-05.
- Données : motif m, texte t.
- Consigne : Produire boucle.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 5 - Motif plus long que texte
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : T-ALGO-05.
- Données : texte AB, motif ABA.
- Consigne : Donner résultat.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 6 - Justifier saut minimal 1
- Type : justification.
- Niveau : standard.
- Capacité officielle : T-ALGO-05.
- Données : Mismatch sur caractère absent du motif.
- Consigne : Expliquer.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 7 - Comparer naïf et Boyer-Moore
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : T-ALGO-05.
- Données : texte AAAAAAB, motif AAAB.
- Consigne : Expliquer avantage.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 8 - Gérer motif vide
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : T-ALGO-05.
- Données : motif "".
- Consigne : Proposer contrat.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : T-ALGO-05.
- Donnée utilisée : motif ABA.
- Résultat attendu : A apparaît aux indices 0 et 2, donc dernier indice A=2 ; B=1 ; autre caractère -> -1.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 2
- Capacité mobilisée : T-ALGO-05.
- Donnée utilisée : texte CABAABABA, motif ABA aligné au début.
- Résultat attendu : On compare motif[2]=A avec texte[2]=B : mismatch B. Dernier B dans motif à 1, décalage max(1,2-1)=1.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 3
- Capacité mobilisée : T-ALGO-05.
- Donnée utilisée : texte CABAABABA, motif ABA.
- Résultat attendu : Après décalage 1, alignement texte[1:4]=ABA. Comparaisons droite à gauche A=A, B=B, A=A. Occurrence trouvée à l’indice 1.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 4
- Capacité mobilisée : T-ALGO-05.
- Donnée utilisée : motif m, texte t.
- Résultat attendu : i=0 ; tant que i<=n-p: comparer j=p-1 vers 0 ; si j<0 retourner i ; sinon i += max(1, j-last[t[i+j]]).
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 5
- Capacité mobilisée : T-ALGO-05.
- Donnée utilisée : texte AB, motif ABA.
- Résultat attendu : Aucun alignement possible car len(motif)=3 > len(texte)=2. Résultat -1 ou None selon contrat.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 6
- Capacité mobilisée : T-ALGO-05.
- Donnée utilisée : Mismatch sur caractère absent du motif.
- Résultat attendu : Si last[c]=-1 et mismatch à j=2, décalage j-(-1)=3. max(1,...) évite aussi un décalage nul dans tous les cas.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 7
- Capacité mobilisée : T-ALGO-05.
- Donnée utilisée : texte AAAAAAB, motif AAAB.
- Résultat attendu : La comparaison depuis la droite voit vite B attendu contre A et décale selon mauvais caractère, évitant plusieurs essais naïfs.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 8
- Capacité mobilisée : T-ALGO-05.
- Donnée utilisée : motif "".
- Résultat attendu : Contrat explicite: motif vide trouvé à l’indice 0, ou bien ValueError. Le TD choisit indice 0 et le teste.
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
| Fiche | T18_fiche_cours_boyer_moore.md | needs_review |
| Séance | T18-S1 | progression existante |
| Évaluation | T18_evaluation_boyer_moore.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans le dossier Documents_DRIVE avant création.
- Aucun fichier Drive n’a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
