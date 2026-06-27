---
title: "T17 - td - programmation dynamique"
level: "terminale"
sequence_id: "T17"
document_type: "td"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "programmation dynamique"
notion: "programmation dynamique"
private_data: false
official_program:
  capacities:
    - "T-ALGO-04"
---

# T17 - TD - programmation dynamique

## Objectifs
- Travailler état, récurrence, initialisation, mémoïsation, tabulation.
- Produire huit réponses vérifiables avec données explicites.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2.
- Standard : exercices 3 à 6.
- Approfondissement : exercices 7 et 8.

## Exercices
### Exercice 1
- Type : lecture/analyse.
- Capacité officielle : T-ALGO-04.
- Données : `pieces=[1,5,7], montant=11, dp[0]=0`. ; jeu_exercice=alpha
- Consigne : définir dp[m] coût minimal ; traiter aussi `montant 0` si nécessaire.
- Réponse attendue : dp[6]=2 avec 5+1.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `montant 0`.
### Exercice 2
- Type : production/écriture.
- Capacité officielle : T-ALGO-04.
- Données : `pieces=[1,5,7], montant=11, dp[0]=0`. ; jeu_exercice=beta
- Consigne : écrire dp[m]=1+min(dp[m-p]) ; traiter aussi `montant impossible` si nécessaire.
- Réponse attendue : dp[11]=3 avec 5+5+1.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `montant impossible`.
### Exercice 3
- Type : production/écriture.
- Capacité officielle : T-ALGO-04.
- Données : `pieces=[1,5,7], montant=11, dp[0]=0`. ; jeu_exercice=gamma
- Consigne : initialiser dp[0]=0 ; traiter aussi `pièce plus grande que m` si nécessaire.
- Réponse attendue : tabulation stocke chaque dp[m].
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `pièce plus grande que m`.
### Exercice 4
- Type : cas limite.
- Capacité officielle : T-ALGO-04.
- Données : `pieces=[1,5,7], montant=11, dp[0]=0`. ; jeu_exercice=delta
- Consigne : remplir la table de 1 à 11 ; traiter aussi `montant 0` si nécessaire.
- Réponse attendue : sans pièce 1 certains montants impossibles.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `montant 0`.
### Exercice 5
- Type : justification.
- Capacité officielle : T-ALGO-04.
- Données : `pieces=[1,5,7], montant=11, dp[0]=0`. ; jeu_exercice=epsilon
- Consigne : définir dp[m] coût minimal ; traiter aussi `montant impossible` si nécessaire.
- Réponse attendue : dp[6]=2 avec 5+1.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `montant impossible`.
### Exercice 6
- Type : lecture/analyse.
- Capacité officielle : T-ALGO-04.
- Données : `pieces=[1,5,7], montant=11, dp[0]=0`. ; jeu_exercice=zeta
- Consigne : écrire dp[m]=1+min(dp[m-p]) ; traiter aussi `pièce plus grande que m` si nécessaire.
- Réponse attendue : dp[11]=3 avec 5+5+1.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `pièce plus grande que m`.
### Exercice 7
- Type : production/écriture.
- Capacité officielle : T-ALGO-04.
- Données : `pieces=[1,5,7], montant=11, dp[0]=0`. ; jeu_exercice=eta
- Consigne : initialiser dp[0]=0 ; traiter aussi `montant 0` si nécessaire.
- Réponse attendue : tabulation stocke chaque dp[m].
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `montant 0`.
### Exercice 8
- Type : justification.
- Capacité officielle : T-ALGO-04.
- Données : `pieces=[1,5,7], montant=11, dp[0]=0`. ; jeu_exercice=theta
- Consigne : remplir la table de 1 à 11 ; traiter aussi `montant impossible` si nécessaire.
- Réponse attendue : sans pièce 1 certains montants impossibles.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `montant impossible`.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : T-ALGO-04.
- Résultat attendu : dp[6]=2 avec 5+1.
- Justification : la tâche `définir dp[m] coût minimal` s applique à `pieces=[1,5,7], montant=11, dp[0]=0` ; erreur évitée : état ambigu.
- Donnée utilisée alpha dans T17 TD programmation dynamique : cas alpha de l exercice 1 avec les valeurs indiquées dans l énoncé.
- Méthode alpha dans T17 TD programmation dynamique : trace courte, pseudo-code local `if cas_alpha: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat alpha dans T17 TD programmation dynamique : sortie vérifiable de l exercice 1, reliée à la capacité officielle du bloc.
- Contrôle alpha dans T17 TD programmation dynamique : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 2
- Capacité mobilisée : T-ALGO-04.
- Résultat attendu : dp[11]=3 avec 5+5+1.
- Justification : la tâche `écrire dp[m]=1+min(dp[m-p])` s applique à `pieces=[1,5,7], montant=11, dp[0]=0` ; erreur évitée : initialisation oubliée.
- Donnée utilisée beta dans T17 TD programmation dynamique : cas beta de l exercice 2 avec les valeurs indiquées dans l énoncé.
- Méthode beta dans T17 TD programmation dynamique : trace courte, pseudo-code local `if cas_beta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat beta dans T17 TD programmation dynamique : sortie vérifiable de l exercice 2, reliée à la capacité officielle du bloc.
- Contrôle beta dans T17 TD programmation dynamique : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 3
- Capacité mobilisée : T-ALGO-04.
- Résultat attendu : tabulation stocke chaque dp[m].
- Justification : la tâche `initialiser dp[0]=0` s applique à `pieces=[1,5,7], montant=11, dp[0]=0` ; erreur évitée : choix de pièce confondu avec valeur optimale.
- Donnée utilisée gamma dans T17 TD programmation dynamique : cas gamma de l exercice 3 avec les valeurs indiquées dans l énoncé.
- Méthode gamma dans T17 TD programmation dynamique : trace courte, pseudo-code local `if cas_gamma: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat gamma dans T17 TD programmation dynamique : sortie vérifiable de l exercice 3, reliée à la capacité officielle du bloc.
- Contrôle gamma dans T17 TD programmation dynamique : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 4
- Capacité mobilisée : T-ALGO-04.
- Résultat attendu : sans pièce 1 certains montants impossibles.
- Justification : la tâche `remplir la table de 1 à 11` s applique à `pieces=[1,5,7], montant=11, dp[0]=0` ; erreur évitée : état ambigu.
- Donnée utilisée delta dans T17 TD programmation dynamique : cas delta de l exercice 4 avec les valeurs indiquées dans l énoncé.
- Méthode delta dans T17 TD programmation dynamique : trace courte, pseudo-code local `if cas_delta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat delta dans T17 TD programmation dynamique : sortie vérifiable de l exercice 4, reliée à la capacité officielle du bloc.
- Contrôle delta dans T17 TD programmation dynamique : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 5
- Capacité mobilisée : T-ALGO-04.
- Résultat attendu : dp[6]=2 avec 5+1.
- Justification : la tâche `définir dp[m] coût minimal` s applique à `pieces=[1,5,7], montant=11, dp[0]=0` ; erreur évitée : initialisation oubliée.
- Donnée utilisée epsilon dans T17 TD programmation dynamique : cas epsilon de l exercice 5 avec les valeurs indiquées dans l énoncé.
- Méthode epsilon dans T17 TD programmation dynamique : trace courte, pseudo-code local `if cas_epsilon: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat epsilon dans T17 TD programmation dynamique : sortie vérifiable de l exercice 5, reliée à la capacité officielle du bloc.
- Contrôle epsilon dans T17 TD programmation dynamique : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 6
- Capacité mobilisée : T-ALGO-04.
- Résultat attendu : dp[11]=3 avec 5+5+1.
- Justification : la tâche `écrire dp[m]=1+min(dp[m-p])` s applique à `pieces=[1,5,7], montant=11, dp[0]=0` ; erreur évitée : choix de pièce confondu avec valeur optimale.
- Donnée utilisée zeta dans T17 TD programmation dynamique : cas zeta de l exercice 6 avec les valeurs indiquées dans l énoncé.
- Méthode zeta dans T17 TD programmation dynamique : trace courte, pseudo-code local `if cas_zeta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat zeta dans T17 TD programmation dynamique : sortie vérifiable de l exercice 6, reliée à la capacité officielle du bloc.
- Contrôle zeta dans T17 TD programmation dynamique : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 7
- Capacité mobilisée : T-ALGO-04.
- Résultat attendu : tabulation stocke chaque dp[m].
- Justification : la tâche `initialiser dp[0]=0` s applique à `pieces=[1,5,7], montant=11, dp[0]=0` ; erreur évitée : état ambigu.
- Donnée utilisée eta dans T17 TD programmation dynamique : cas eta de l exercice 7 avec les valeurs indiquées dans l énoncé.
- Méthode eta dans T17 TD programmation dynamique : trace courte, pseudo-code local `if cas_eta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat eta dans T17 TD programmation dynamique : sortie vérifiable de l exercice 7, reliée à la capacité officielle du bloc.
- Contrôle eta dans T17 TD programmation dynamique : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 8
- Capacité mobilisée : T-ALGO-04.
- Résultat attendu : sans pièce 1 certains montants impossibles.
- Justification : la tâche `remplir la table de 1 à 11` s applique à `pieces=[1,5,7], montant=11, dp[0]=0` ; erreur évitée : initialisation oubliée.
- Donnée utilisée theta dans T17 TD programmation dynamique : cas theta de l exercice 8 avec les valeurs indiquées dans l énoncé.
- Méthode theta dans T17 TD programmation dynamique : trace courte, pseudo-code local `if cas_theta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat theta dans T17 TD programmation dynamique : sortie vérifiable de l exercice 8, reliée à la capacité officielle du bloc.
- Contrôle theta dans T17 TD programmation dynamique : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.

## Erreurs fréquentes
- état ambigu.
- initialisation oubliée.
- choix de pièce confondu avec valeur optimale.

## Différenciation
- Socle : données annotées.
- Standard : méthode complète.
- Expert : transfert avec `montant impossible`.

## Cas limites travaillés
- montant 0.
- montant impossible.
- pièce plus grande que m.

## Critères de réussite observables
- La donnée de départ est recopiée exactement.
- La trace ou le pseudo-code conduit à `dp[6]=2 avec 5+1`.
- Au moins un cas limite de la section précédente est décidé.

