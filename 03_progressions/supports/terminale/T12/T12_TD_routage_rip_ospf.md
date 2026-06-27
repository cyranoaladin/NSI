---
title: "T12 - TD - routage RIP OSPF"
level: "terminale"
sequence_id: "T12"
document_type: "td"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Réseaux"
notion: "routage RIP OSPF"
objectifs:
  - "travailler routage RIP OSPF sur des données explicites"
  - "produire une réponse justifiée et contrôlée"
  - "identifier les cas limites"
  - "corriger les erreurs fréquentes du chapitre"
private_data: false
official_program:
  capacities:
    - "T-ARCH-03"
---

# T12 - TD - routage RIP OSPF

## Objectifs
- Lire une donnée disciplinaire précise avant de répondre.
- Produire une méthode vérifiable et un résultat contrôlable.
- Traiter un cas limite sans le transformer en généralité.
- Relier chaque correction à une erreur fréquente observable.

## Capacités officielles
- T-ARCH-03

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T12/T12_fiche_cours_routage_rip_ospf.md`.
- Séance liée : `T12-S1` dans la progression annuelle.
- Statut : support `needs_review`, non validé et non publiable.

## Situation de travail
Topologie: R1-R2 coût1, R2-R3 coût1, R1-R3 coût4, R3-R4 coût2.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée.
- Standard : exercices 3 à 6, production écrite et justification.
- Approfondissement : exercices 7 et 8, transfert ou comparaison.

## Exercices
### Exercice 1 - Lire une table de routage
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-ARCH-03.
- Données : R1 connaît R2 coût1, R3 coût4 direct, R4 via R3 coût6.
- Consigne : Identifier la meilleure route vers R3.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 2 - Calculer métrique RIP
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-ARCH-03.
- Données : R1 vers R4 via R2 puis R3, 3 sauts.
- Consigne : Donner métrique.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 3 - Appliquer Dijkstra OSPF
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-ARCH-03.
- Données : Coûts: R1-R2=1, R2-R3=1, R1-R3=4, R3-R4=2.
- Consigne : Donner distances depuis R1.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 4 - Écrire une entrée de table
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-ARCH-03.
- Données : Destination réseau 10.4.0.0/24 derrière R4.
- Consigne : Donner next-hop depuis R1.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 5 - Lien R2-R3 coupé
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : T-ARCH-03.
- Données : Après coupure, R1-R3 direct coût4 existe.
- Consigne : Recalculer R1 vers R4.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 6 - Comparer RIP et OSPF
- Type : justification.
- Niveau : standard.
- Capacité officielle : T-ARCH-03.
- Données : Chemin A 2 sauts coût 100, chemin B 3 sauts coût 3.
- Consigne : Dire protocole choisi.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 7 - Détecter boucle temporaire
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : T-ARCH-03.
- Données : R1 croit R4 via R2, R2 croit R4 via R1.
- Consigne : Expliquer le risque.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 8 - Pseudo-code de next-hop
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : T-ARCH-03.
- Données : Distances candidates vers R4: via R2 coût4, via R3 coût6.
- Consigne : Écrire la sélection.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : T-ARCH-03.
- Donnée utilisée : R1 connaît R2 coût1, R3 coût4 direct, R4 via R3 coût6.
- Résultat attendu : Meilleure route R1->R2->R3 coût 2 si R2 annonce R3 à 1 ; elle bat le lien direct coût 4.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 2
- Capacité mobilisée : T-ARCH-03.
- Donnée utilisée : R1 vers R4 via R2 puis R3, 3 sauts.
- Résultat attendu : En RIP, la métrique est le nombre de sauts: R1->R2, R2->R3, R3->R4 donc 3.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 3
- Capacité mobilisée : T-ARCH-03.
- Donnée utilisée : Coûts: R1-R2=1, R2-R3=1, R1-R3=4, R3-R4=2.
- Résultat attendu : D(R1)=0, D(R2)=1, D(R3)=2 via R2, D(R4)=4 via R2 puis R3.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 4
- Capacité mobilisée : T-ARCH-03.
- Donnée utilisée : Destination réseau 10.4.0.0/24 derrière R4.
- Résultat attendu : Entrée: destination 10.4.0.0/24, next-hop R2, coût OSPF 4. Le chemin calculé est R1-R2-R3-R4.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 5
- Capacité mobilisée : T-ARCH-03.
- Donnée utilisée : Après coupure, R1-R3 direct coût4 existe.
- Résultat attendu : Chemin devient R1-R3-R4 coût 4+2=6. La route via R2 n’est plus valide.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 6
- Capacité mobilisée : T-ARCH-03.
- Donnée utilisée : Chemin A 2 sauts coût 100, chemin B 3 sauts coût 3.
- Résultat attendu : RIP préfère A car 2 sauts < 3. OSPF préfère B car coût total 3 < 100.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 7
- Capacité mobilisée : T-ARCH-03.
- Donnée utilisée : R1 croit R4 via R2, R2 croit R4 via R1.
- Résultat attendu : Les paquets peuvent alterner R1/R2 jusqu’à TTL=0. Les protocoles utilisent temporisateurs et annonces pour corriger.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 8
- Capacité mobilisée : T-ARCH-03.
- Donnée utilisée : Distances candidates vers R4: via R2 coût4, via R3 coût6.
- Résultat attendu : min_cost=inf; pour voisin, coût=c_lien + annonce[voisin][R4]; garder voisin minimal. Résultat next-hop R2 coût4.
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
| Fiche | T12_fiche_cours_routage_rip_ospf.md | needs_review |
| Séance | T12-S1 | progression existante |
| Évaluation | T12_evaluation_routage_rip_ospf.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans le dossier Documents_DRIVE avant création.
- Aucun fichier Drive n’a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.
