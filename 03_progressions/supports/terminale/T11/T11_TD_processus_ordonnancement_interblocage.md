---
title: "T11 - TD - processus ordonnancement interblocage"
level: "terminale"
sequence_id: "T11"
document_type: "td"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Architecture"
notion: "processus ordonnancement interblocage"
objectifs:
  - "travailler processus ordonnancement interblocage sur des données explicites"
  - "produire une réponse justifiée et contrôlée"
  - "identifier les cas limites"
  - "corriger les erreurs fréquentes du chapitre"
private_data: false
official_program:
  capacities:
    - "T-ARCH-01"
    - "T-ARCH-02A"
    - "T-ARCH-02B"
    - "T-ARCH-02C"
---

# T11 - TD - processus ordonnancement interblocage

## Objectifs
- Lire une donnée disciplinaire précise avant de répondre.
- Produire une méthode vérifiable et un résultat contrôlable.
- Traiter un cas limite sans le transformer en généralité.
- Relier chaque correction à une erreur fréquente observable.

## Capacités officielles
- T-ARCH-01
- T-ARCH-02A
- T-ARCH-02B
- T-ARCH-02C

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T11/T11_fiche_cours_processus_ordonnancement_interblocage.md`.
- Séance liée : `T11-S1` dans la progression annuelle.
- Statut : support `needs_review`, non validé et non publiable.

## Situation de travail
Trois processus P1, P2, P3 se partagent CPU, imprimante R1 et fichier R2.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée.
- Standard : exercices 3 à 6, production écrite et justification.
- Approfondissement : exercices 7 et 8, transfert ou comparaison.

## Exercices
### Exercice 1 - Tracer FCFS
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-ARCH-01.
- Données : P1 arrivée 0 durée 3 ; P2 arrivée 1 durée 2 ; P3 arrivée 2 durée 1.
- Consigne : Donner le diagramme.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 2 - Tracer Round Robin quantum 1
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-ARCH-02A.
- Données : P1 durée 3, P2 durée 2, arrivées toutes à 0.
- Consigne : Donner la séquence CPU.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 3 - Calculer temps de séjour
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-ARCH-02B.
- Données : Données FCFS de l’exercice 1.
- Consigne : Calculer turnaround.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 4 - Écrire un pseudo-code ordonnanceur simple
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-ARCH-02C.
- Données : File prête [P1,P2,P3].
- Consigne : Produire pseudo-code FCFS.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 5 - Processus bloqué en E/S
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : T-ARCH-01.
- Données : P1 demande imprimante occupée de t=2 à t=5.
- Consigne : Dire son état.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 6 - Justifier un interblocage
- Type : justification.
- Niveau : standard.
- Capacité officielle : T-ARCH-02A.
- Données : P1 détient R1 et attend R2 ; P2 détient R2 et attend R1.
- Consigne : Montrer le cycle.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 7 - Comparer équité
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : T-ARCH-02B.
- Données : P1 durée 10, P2 durée 1, P3 durée 1.
- Consigne : Comparer FCFS et RR.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.
### Exercice 8 - Prévenir interblocage
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : T-ARCH-02C.
- Données : Ressources R1,R2.
- Consigne : Proposer une règle.
- Production attendue : une réponse structurée en donnée, méthode, résultat et contrôle.
- Critère de réussite : un pair peut vérifier le résultat à partir de la donnée.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : T-ARCH-01.
- Donnée utilisée : P1 arrivée 0 durée 3 ; P2 arrivée 1 durée 2 ; P3 arrivée 2 durée 1.
- Résultat attendu : FCFS: P1 de 0 à 3, P2 de 3 à 5, P3 de 5 à 6. Attentes: P1=0, P2=2, P3=3.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 2
- Capacité mobilisée : T-ARCH-02A.
- Donnée utilisée : P1 durée 3, P2 durée 2, arrivées toutes à 0.
- Résultat attendu : RR q=1: P1(0-1), P2(1-2), P1(2-3), P2(3-4), P1(4-5). Fin P2=4, P1=5.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 3
- Capacité mobilisée : T-ARCH-02B.
- Donnée utilisée : Données FCFS de l’exercice 1.
- Résultat attendu : Séjour = fin - arrivée: P1=3-0=3, P2=5-1=4, P3=6-2=4.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 4
- Capacité mobilisée : T-ARCH-02C.
- Donnée utilisée : File prête [P1,P2,P3].
- Résultat attendu : tant que file non vide: p=defiler(); exécuter p jusqu’à fin; enregistrer temps_fin[p]. La file conserve l’ordre d’arrivée.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 5
- Capacité mobilisée : T-ARCH-01.
- Donnée utilisée : P1 demande imprimante occupée de t=2 à t=5.
- Résultat attendu : P1 quitte l’état élu et passe bloqué jusqu’à libération de l’imprimante ; le CPU peut être donné à un autre processus.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 6
- Capacité mobilisée : T-ARCH-02A.
- Donnée utilisée : P1 détient R1 et attend R2 ; P2 détient R2 et attend R1.
- Résultat attendu : Graphe: P1 -> R2 -> P2 -> R1 -> P1. Cycle avec ressources non préemptibles : interblocage possible.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 7
- Capacité mobilisée : T-ARCH-02B.
- Donnée utilisée : P1 durée 10, P2 durée 1, P3 durée 1.
- Résultat attendu : FCFS retarde P2/P3 jusqu’à t=10 si P1 commence ; RR q=1 permet à P2 et P3 de finir tôt, mais ajoute des commutations.
- Contrôle : comparer la réponse avec la donnée de départ et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 8
- Capacité mobilisée : T-ARCH-02C.
- Donnée utilisée : Ressources R1,R2.
- Résultat attendu : Imposer un ordre global: toujours demander R1 avant R2. Alors aucun cycle P1/R2/P2/R1 ne peut se former.
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
| Fiche | T11_fiche_cours_processus_ordonnancement_interblocage.md | needs_review |
| Séance | T11-S1 | progression existante |
| Évaluation | T11_evaluation_processus_ordonnancement_interblocage.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans le dossier Documents_DRIVE avant création.
- Aucun fichier Drive n’a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
