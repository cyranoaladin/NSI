---
title: "T10 - td - SQL SELECT, JOIN, INSERT, UPDATE et DELETE"
level: "terminale"
sequence_id: "T10"
document_type: "td"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "SQL SELECT, JOIN, INSERT, UPDATE et DELETE"
notion: "SQL SELECT, JOIN, INSERT, UPDATE et DELETE"
private_data: false
official_program:
  capacities:
    - "T-BDD-03A"
    - "T-BDD-03B"
    - "T-BDD-03C"
    - "T-BDD-03D"
    - "T-BDD-03E"
    - "T-BDD-03F"
    - "T-BDD-03G"
    - "T-BDD-03H"
---

# T10 - TD - SQL SELECT, JOIN, INSERT, UPDATE et DELETE

## Objectifs
- Travailler SELECT, FROM, WHERE, JOIN, ORDER BY.
- Produire huit réponses vérifiables avec données explicites.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2.
- Standard : exercices 3 à 6.
- Approfondissement : exercices 7 et 8.

## Exercices
### Exercice 1
- Type : lecture/analyse.
- Capacité officielle : T-BDD-03A.
- Données : `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)`. ; jeu_exercice=alpha
- Consigne : projeter nom et classe ; traiter aussi `JOIN sans ON` si nécessaire.
- Réponse attendue : SELECT nom FROM Eleve ORDER BY nom -> Ada, Linus.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `JOIN sans ON`.
### Exercice 2
- Type : production/écriture.
- Capacité officielle : T-BDD-03B.
- Données : `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)`. ; jeu_exercice=beta
- Consigne : filtrer note >= 15 ; traiter aussi `UPDATE sans WHERE` si nécessaire.
- Réponse attendue : JOIN -> Ada 17, Linus 13.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `UPDATE sans WHERE`.
### Exercice 3
- Type : production/écriture.
- Capacité officielle : T-BDD-03C.
- Données : `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)`. ; jeu_exercice=gamma
- Consigne : joindre Eleve.id_eleve = Note.id_eleve ; traiter aussi `DELETE sans WHERE` si nécessaire.
- Réponse attendue : UPDATE id_note=10 -> Ada 18.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `DELETE sans WHERE`.
### Exercice 4
- Type : cas limite.
- Capacité officielle : T-BDD-03D.
- Données : `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)`. ; jeu_exercice=delta
- Consigne : vérifier modification par SELECT ; traiter aussi `JOIN sans ON` si nécessaire.
- Réponse attendue : DELETE WHERE id_note=11 retire Linus.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `JOIN sans ON`.
### Exercice 5
- Type : justification.
- Capacité officielle : T-BDD-03E.
- Données : `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)`. ; jeu_exercice=epsilon
- Consigne : projeter nom et classe ; traiter aussi `UPDATE sans WHERE` si nécessaire.
- Réponse attendue : SELECT nom FROM Eleve ORDER BY nom -> Ada, Linus.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `UPDATE sans WHERE`.
### Exercice 6
- Type : lecture/analyse.
- Capacité officielle : T-BDD-03F.
- Données : `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)`. ; jeu_exercice=zeta
- Consigne : filtrer note >= 15 ; traiter aussi `DELETE sans WHERE` si nécessaire.
- Réponse attendue : JOIN -> Ada 17, Linus 13.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `DELETE sans WHERE`.
### Exercice 7
- Type : production/écriture.
- Capacité officielle : T-BDD-03G.
- Données : `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)`. ; jeu_exercice=eta
- Consigne : joindre Eleve.id_eleve = Note.id_eleve ; traiter aussi `JOIN sans ON` si nécessaire.
- Réponse attendue : UPDATE id_note=10 -> Ada 18.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `JOIN sans ON`.
### Exercice 8
- Type : justification.
- Capacité officielle : T-BDD-03H.
- Données : `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)`. ; jeu_exercice=theta
- Consigne : vérifier modification par SELECT ; traiter aussi `UPDATE sans WHERE` si nécessaire.
- Réponse attendue : DELETE WHERE id_note=11 retire Linus.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `UPDATE sans WHERE`.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : T-BDD-03A.
- Résultat attendu : SELECT nom FROM Eleve ORDER BY nom -> Ada, Linus.
- Justification : la tâche `projeter nom et classe` s applique à `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)` ; erreur évitée : condition de jointure oubliée.
- Donnée utilisée alpha dans T10 TD sql insert update delete : cas alpha de l exercice 1 avec les valeurs indiquées dans l énoncé.
- Méthode alpha dans T10 TD sql insert update delete : trace courte, pseudo-code local `if cas_alpha: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat alpha dans T10 TD sql insert update delete : sortie vérifiable de l exercice 1, reliée à la capacité officielle du bloc.
- Contrôle alpha dans T10 TD sql insert update delete : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 2
- Capacité mobilisée : T-BDD-03B.
- Résultat attendu : JOIN -> Ada 17, Linus 13.
- Justification : la tâche `filtrer note >= 15` s applique à `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)` ; erreur évitée : WHERE confondu avec ORDER BY.
- Donnée utilisée beta dans T10 TD sql insert update delete : cas beta de l exercice 2 avec les valeurs indiquées dans l énoncé.
- Méthode beta dans T10 TD sql insert update delete : trace courte, pseudo-code local `if cas_beta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat beta dans T10 TD sql insert update delete : sortie vérifiable de l exercice 2, reliée à la capacité officielle du bloc.
- Contrôle beta dans T10 TD sql insert update delete : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 3
- Capacité mobilisée : T-BDD-03C.
- Résultat attendu : UPDATE id_note=10 -> Ada 18.
- Justification : la tâche `joindre Eleve.id_eleve = Note.id_eleve` s applique à `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)` ; erreur évitée : WHERE omis dans UPDATE.
- Donnée utilisée gamma dans T10 TD sql insert update delete : cas gamma de l exercice 3 avec les valeurs indiquées dans l énoncé.
- Méthode gamma dans T10 TD sql insert update delete : trace courte, pseudo-code local `if cas_gamma: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat gamma dans T10 TD sql insert update delete : sortie vérifiable de l exercice 3, reliée à la capacité officielle du bloc.
- Contrôle gamma dans T10 TD sql insert update delete : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 4
- Capacité mobilisée : T-BDD-03D.
- Résultat attendu : DELETE WHERE id_note=11 retire Linus.
- Justification : la tâche `vérifier modification par SELECT` s applique à `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)` ; erreur évitée : condition de jointure oubliée.
- Donnée utilisée delta dans T10 TD sql insert update delete : cas delta de l exercice 4 avec les valeurs indiquées dans l énoncé.
- Méthode delta dans T10 TD sql insert update delete : trace courte, pseudo-code local `if cas_delta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat delta dans T10 TD sql insert update delete : sortie vérifiable de l exercice 4, reliée à la capacité officielle du bloc.
- Contrôle delta dans T10 TD sql insert update delete : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 5
- Capacité mobilisée : T-BDD-03E.
- Résultat attendu : SELECT nom FROM Eleve ORDER BY nom -> Ada, Linus.
- Justification : la tâche `projeter nom et classe` s applique à `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)` ; erreur évitée : WHERE confondu avec ORDER BY.
- Donnée utilisée epsilon dans T10 TD sql insert update delete : cas epsilon de l exercice 5 avec les valeurs indiquées dans l énoncé.
- Méthode epsilon dans T10 TD sql insert update delete : trace courte, pseudo-code local `if cas_epsilon: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat epsilon dans T10 TD sql insert update delete : sortie vérifiable de l exercice 5, reliée à la capacité officielle du bloc.
- Contrôle epsilon dans T10 TD sql insert update delete : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 6
- Capacité mobilisée : T-BDD-03F.
- Résultat attendu : JOIN -> Ada 17, Linus 13.
- Justification : la tâche `filtrer note >= 15` s applique à `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)` ; erreur évitée : WHERE omis dans UPDATE.
- Donnée utilisée zeta dans T10 TD sql insert update delete : cas zeta de l exercice 6 avec les valeurs indiquées dans l énoncé.
- Méthode zeta dans T10 TD sql insert update delete : trace courte, pseudo-code local `if cas_zeta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat zeta dans T10 TD sql insert update delete : sortie vérifiable de l exercice 6, reliée à la capacité officielle du bloc.
- Contrôle zeta dans T10 TD sql insert update delete : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 7
- Capacité mobilisée : T-BDD-03G.
- Résultat attendu : UPDATE id_note=10 -> Ada 18.
- Justification : la tâche `joindre Eleve.id_eleve = Note.id_eleve` s applique à `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)` ; erreur évitée : condition de jointure oubliée.
- Donnée utilisée eta dans T10 TD sql insert update delete : cas eta de l exercice 7 avec les valeurs indiquées dans l énoncé.
- Méthode eta dans T10 TD sql insert update delete : trace courte, pseudo-code local `if cas_eta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat eta dans T10 TD sql insert update delete : sortie vérifiable de l exercice 7, reliée à la capacité officielle du bloc.
- Contrôle eta dans T10 TD sql insert update delete : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 8
- Capacité mobilisée : T-BDD-03H.
- Résultat attendu : DELETE WHERE id_note=11 retire Linus.
- Justification : la tâche `vérifier modification par SELECT` s applique à `Eleve(1,Ada,T1), Eleve(2,Linus,T2) ; Note(10,1,NSI,17), Note(11,2,NSI,13)` ; erreur évitée : WHERE confondu avec ORDER BY.
- Donnée utilisée theta dans T10 TD sql insert update delete : cas theta de l exercice 8 avec les valeurs indiquées dans l énoncé.
- Méthode theta dans T10 TD sql insert update delete : trace courte, pseudo-code local `if cas_theta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat theta dans T10 TD sql insert update delete : sortie vérifiable de l exercice 8, reliée à la capacité officielle du bloc.
- Contrôle theta dans T10 TD sql insert update delete : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.

## Erreurs fréquentes
- condition de jointure oubliée.
- WHERE confondu avec ORDER BY.
- WHERE omis dans UPDATE.

## Différenciation
- Socle : données annotées.
- Standard : méthode complète.
- Expert : transfert avec `UPDATE sans WHERE`.

## Cas limites travaillés
- JOIN sans ON.
- UPDATE sans WHERE.
- DELETE sans WHERE.

## Critères de réussite observables
- La donnée de départ est recopiée exactement.
- La trace ou le pseudo-code conduit à `SELECT nom FROM Eleve ORDER BY nom -> Ada, Linus`.
- Au moins un cas limite de la section précédente est décidé.

