---
title: "P13 - td - dichotomie, glouton et k-NN"
level: "premiere"
sequence_id: "P13"
document_type: "td"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "dichotomie, glouton et k-NN"
notion: "dichotomie, glouton et k-NN"
private_data: false
official_program:
  capacities:
    - "P-ALGO-03"
    - "P-ALGO-04"
    - "P-ALGO-05"
---

# P13 - TD - dichotomie, glouton et k-NN

## Objectifs
- Travailler dichotomie, variant droite-gauche, glouton, choix local, k-NN.
- Produire neuf réponses vérifiables avec données explicites.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2.
- Standard : exercices 3 à 6.
- Approfondissement : exercices 7, 8 et 9.

## Exercices
### Exercice 1
- Type : lecture/analyse.
- Capacité officielle : P-ALGO-04.
- Données : `tableau=[4,9,18,23,37,41], cible=37 ; pièces=[10,5,2,1], montant=28 ; voisins=[rouge:1.2, bleu:2.0, rouge:2.4]`. ; jeu_exercice=alpha
- Consigne : calculer milieu puis réduire intervalle ; traiter aussi `cible absente` si nécessaire.
- Réponse attendue : milieux 18 puis 37 -> trouvé indice 4.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `cible absente`.
### Exercice 2
- Type : production/écriture.
- Capacité officielle : P-ALGO-04.
- Données : `tableau=[4,9,18,23,37,41], cible=37 ; pièces=[10,5,2,1], montant=28 ; voisins=[rouge:1.2, bleu:2.0, rouge:2.4]`. ; jeu_exercice=beta
- Consigne : montrer que droite-gauche diminue ; traiter aussi `cible absente` si nécessaire.
- Réponse attendue : le variant V = droite − gauche + 1 décroît de 6 à 3 → terminaison (cible trouvée).
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `cible absente`.
### Exercice 3
- Type : production/écriture.
- Capacité officielle : P-ALGO-05.
- Données : `tableau=[4,9,18,23,37,41], cible=37 ; pièces=[10,5,2,1], montant=28 ; voisins=[rouge:1.2, bleu:2.0, rouge:2.4]`. ; jeu_exercice=gamma
- Consigne : prendre la plus grande pièce possible ; traiter aussi `pièce 1 absente` si nécessaire.
- Réponse attendue : 28 = 10+10+5+2+1 (5 pièces).
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `pièce 1 absente`.
### Exercice 4
- Type : cas limite.
- Capacité officielle : P-ALGO-03.
- Données : `tableau=[4,9,18,23,37,41], cible=37 ; pièces=[10,5,2,1], montant=28 ; voisins=[rouge:1.2, bleu:2.0, rouge:2.4]`. ; jeu_exercice=delta
- Consigne : voter parmi k=3 voisins ; traiter aussi `égalité de vote` si nécessaire.
- Réponse attendue : rouge 2 voix vs bleu 1 → classe rouge.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `égalité de vote`.
### Exercice 5
- Type : justification.
- Capacité officielle : P-ALGO-04.
- Données : `tableau=[4,9,18,23,37,41], cible=37 ; pièces=[10,5,2,1], montant=28 ; voisins=[rouge:1.2, bleu:2.0, rouge:2.4]`. ; jeu_exercice=epsilon
- Consigne : montrer que le variant droite-gauche diminue ; traiter aussi `cible absente` si nécessaire.
- Réponse attendue : le variant V = droite − gauche + 1 décroît de 6 à 3 → terminaison (cible trouvée).
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `cible absente`.
### Exercice 6
- Type : lecture/analyse.
- Capacité officielle : P-ALGO-05.
- Données : `tableau=[4,9,18,23,37,41], cible=37 ; pièces=[10,5,2,1], montant=28 ; voisins=[rouge:1.2, bleu:2.0, rouge:2.4]`. ; jeu_exercice=zeta
- Consigne : prendre la plus grande pièce possible ; traiter aussi `pièce 1 absente` si nécessaire.
- Réponse attendue : 28 = 10+10+5+2+1 (5 pièces).
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `pièce 1 absente`.
### Exercice 7
- Type : production/écriture.
- Capacité officielle : P-ALGO-03.
- Données : `tableau=[4,9,18,23,37,41], cible=37 ; pièces=[10,5,2,1], montant=28 ; voisins=[rouge:1.2, bleu:2.0, rouge:2.4]`. ; jeu_exercice=eta
- Consigne : voter parmi les k plus proches voisins ; traiter aussi `égalité de vote` si nécessaire.
- Réponse attendue : rouge 2 voix vs bleu 1 → classe rouge.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `égalité de vote`.
### Exercice 8
- Type : justification.
- Capacité officielle : P-ALGO-04.
- Données : `tableau=[4,9,18,23,37,41], cible=23`. ; jeu_exercice=theta
- Consigne : montrer que le variant droite-gauche décroît à chaque étape sur ces données ; conclure sur la terminaison ; traiter aussi `cible absente` si nécessaire.
- Réponse attendue : le variant V = droite − gauche + 1 décroît de 6 à 3 puis 1 → terminaison prouvée (cible trouvée).
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `cible absente`.

### Exercice 9
- Type : production/écriture.
- Capacité officielle : P-ALGO-03.
- Données : données d'entraînement = [(2, 3, "A"), (5, 4, "B"), (1, 1, "A"), (8, 7, "B"), (3, 2, "A")]. Nouveau point = (4, 3). k = 3. ; jeu_exercice=iota
- Consigne : (9a) calculer la distance euclidienne entre le nouveau point et chaque point d'entraînement ; (9b) identifier les 3 plus proches voisins ; (9c) déterminer la classe prédite par vote majoritaire ; (9d) que se passe-t-il si k = 2 et les deux voisins sont de classes différentes ?
- Réponse attendue : distances calculées, 3 plus proches identifiés, classe prédite = "A", cas k=2 → égalité.
- Critère de réussite : distances correctes, tri vérifié, vote majoritaire explicite, cas d'égalité traité.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : P-ALGO-04.
- Résultat attendu : milieux 18 puis 37 -> trouvé indice 4.
- Justification : la tâche `calculer milieu puis réduire intervalle` s applique à `tableau=[4,9,18,23,37,41], cible=37 ; pièces=[10,5,2,1], montant=28 ; voisins=[rouge:1.2, bleu:2.0, rouge:2.4]` ; erreur évitée : dichotomie sur liste non triée.
- Donnée utilisée alpha dans P13 TD dichotomie glouton knn : cas alpha de l exercice 1 avec les valeurs indiquées dans l énoncé.
- Méthode alpha dans P13 TD dichotomie glouton knn : trace courte, pseudo-code local `if cas_alpha: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat alpha dans P13 TD dichotomie glouton knn : sortie vérifiable de l exercice 1, reliée à la capacité officielle du bloc.
- Contrôle alpha dans P13 TD dichotomie glouton knn : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 2
- Capacité mobilisée : P-ALGO-04.
- Résultat attendu : le variant V = droite − gauche + 1 décroît de 6 à 3 → terminaison (cible trouvée).
- Justification : la tâche `montrer que droite-gauche diminue` s applique à `tableau=[4,9,18,23,37,41], cible=37` ; erreur évitée : variant non identifié ou non décroissant.
- Donnée utilisée beta dans P13 TD dichotomie glouton knn : cas beta de l exercice 2 avec les valeurs indiquées dans l énoncé.
- Méthode beta dans P13 TD dichotomie glouton knn : trace courte, pseudo-code local `if cas_beta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat beta dans P13 TD dichotomie glouton knn : sortie vérifiable de l exercice 2, reliée à la capacité officielle du bloc.
- Contrôle beta dans P13 TD dichotomie glouton knn : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 3
- Capacité mobilisée : P-ALGO-05.
- Résultat attendu : 28 = 10+10+5+2+1 (5 pièces).
- Justification : la tâche `prendre la plus grande pièce possible` s applique à `pièces=[10,5,2,1], montant=28` ; erreur évitée : glouton supposé toujours optimal.
- Donnée utilisée gamma dans P13 TD dichotomie glouton knn : cas gamma de l exercice 3 avec les valeurs indiquées dans l énoncé.
- Méthode gamma dans P13 TD dichotomie glouton knn : trace courte, pseudo-code local `if cas_gamma: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat gamma dans P13 TD dichotomie glouton knn : sortie vérifiable de l exercice 3, reliée à la capacité officielle du bloc.
- Contrôle gamma dans P13 TD dichotomie glouton knn : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 4
- Capacité mobilisée : P-ALGO-03.
- Résultat attendu : rouge 2 voix vs bleu 1 → classe rouge.
- Justification : la tâche `voter parmi k=3 voisins` s applique à `voisins=[rouge:1.2, bleu:2.0, rouge:2.4]` ; erreur évitée : égalité k-NN non décidée.
- Donnée utilisée delta dans P13 TD dichotomie glouton knn : cas delta de l exercice 4 avec les valeurs indiquées dans l énoncé.
- Méthode delta dans P13 TD dichotomie glouton knn : trace courte, pseudo-code local `if cas_delta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat delta dans P13 TD dichotomie glouton knn : sortie vérifiable de l exercice 4, reliée à la capacité officielle du bloc.
- Contrôle delta dans P13 TD dichotomie glouton knn : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 5
- Capacité mobilisée : P-ALGO-04.
- Résultat attendu : le variant V = droite − gauche + 1 décroît de 6 à 3 → terminaison (cible trouvée).
- Justification : la tâche `montrer que le variant droite-gauche diminue` s applique à `tableau=[4,9,18,23,37,41], cible=37` ; erreur évitée : variant non identifié ou non décroissant.
- Donnée utilisée epsilon dans P13 TD dichotomie glouton knn : cas epsilon de l exercice 5 avec les valeurs indiquées dans l énoncé.
- Méthode epsilon dans P13 TD dichotomie glouton knn : trace courte, pseudo-code local `if cas_epsilon: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat epsilon dans P13 TD dichotomie glouton knn : sortie vérifiable de l exercice 5, reliée à la capacité officielle du bloc.
- Contrôle epsilon dans P13 TD dichotomie glouton knn : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 6
- Capacité mobilisée : P-ALGO-05.
- Résultat attendu : 28 = 10+10+5+2+1 (5 pièces).
- Justification : la tâche `prendre la plus grande pièce possible` s applique à `pièces=[10,5,2,1], montant=28` ; erreur évitée : glouton supposé toujours optimal.
- Donnée utilisée zeta dans P13 TD dichotomie glouton knn : cas zeta de l exercice 6 avec les valeurs indiquées dans l énoncé.
- Méthode zeta dans P13 TD dichotomie glouton knn : trace courte, pseudo-code local `if cas_zeta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat zeta dans P13 TD dichotomie glouton knn : sortie vérifiable de l exercice 6, reliée à la capacité officielle du bloc.
- Contrôle zeta dans P13 TD dichotomie glouton knn : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 7
- Capacité mobilisée : P-ALGO-03.
- Résultat attendu : rouge 2 voix vs bleu 1 → classe rouge.
- Justification : la tâche `voter parmi les k plus proches voisins` s applique à `voisins=[rouge:1.2, bleu:2.0, rouge:2.4]` ; erreur évitée : égalité k-NN non décidée.
- Donnée utilisée eta dans P13 TD dichotomie glouton knn : cas eta de l exercice 7 avec les valeurs indiquées dans l énoncé.
- Méthode eta dans P13 TD dichotomie glouton knn : trace courte, pseudo-code local `if cas_eta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat eta dans P13 TD dichotomie glouton knn : sortie vérifiable de l exercice 7, reliée à la capacité officielle du bloc.
- Contrôle eta dans P13 TD dichotomie glouton knn : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 8
- Capacité mobilisée : P-ALGO-04.
- Résultat attendu : le variant V = droite − gauche + 1 décroît de 6 à 3 puis 1 → terminaison prouvée (cible trouvée).
- Justification : la tâche `montrer que le variant droite-gauche décroît` s applique à `tableau=[4,9,18,23,37,41], cible=23` ; erreur évitée : variant non identifié ou non décroissant.
- Donnée utilisée theta dans P13 TD dichotomie glouton knn : cas theta de l exercice 8 avec les valeurs indiquées dans l énoncé.
- Méthode theta dans P13 TD dichotomie glouton knn : trace courte, pseudo-code local `if cas_theta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat theta dans P13 TD dichotomie glouton knn : sortie vérifiable de l exercice 8, reliée à la capacité officielle du bloc.
- Contrôle theta dans P13 TD dichotomie glouton knn : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.

### Corrigé exercice 9
- Capacité mobilisée : P-ALGO-03.
- Résultat attendu : (9a) d(A(2,3))=2.00, d(B(5,4))=1.41, d(A(1,1))=3.61, d(B(8,7))=5.66, d(A(3,2))=1.41. (9b) 3 plus proches : A(3,2) d=1.41, B(5,4) d=1.41, A(2,3) d=2.00. (9c) Vote : A=2, B=1 → classe prédite = "A". (9d) k=2 : A(3,2) et B(5,4) à distance égale → égalité 1-1, résultat indéterminé.
- Justification : la tâche `classifier par k-NN` s'applique aux données d'entraînement avec distance euclidienne et vote majoritaire ; erreur évitée : égalité k-NN non décidée.
- Donnée utilisée iota dans P13 TD dichotomie glouton knn : cas iota de l'exercice 9 avec 5 points et k=3.
- Méthode iota dans P13 TD dichotomie glouton knn : calcul de distance euclidienne, tri, sélection des k plus proches, vote majoritaire.
- Résultat iota dans P13 TD dichotomie glouton knn : classe prédite "A" avec vote 2 contre 1.
- Contrôle iota dans P13 TD dichotomie glouton knn : le cas limite « k=2 avec égalité de vote » est traité explicitement.

## Erreurs fréquentes
- dichotomie sur liste non triée.
- glouton supposé toujours optimal.
- égalité k-NN non décidée.

## Différenciation
- Socle : données annotées.
- Standard : méthode complète.
- Expert : transfert avec `pièce 1 absente`.

## Cas limites travaillés
- cible absente.
- pièce 1 absente.
- égalité de vote.

## Critères de réussite observables
- La donnée de départ est recopiée exactement.
- La trace ou le pseudo-code conduit à `milieux 18 puis 37 -> trouvé indice 4`.
- Au moins un cas limite de la section précédente est décidé.

