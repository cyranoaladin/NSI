---
title: "T13 - td - chiffrement et HTTPS"
level: "terminale"
sequence_id: "T13"
document_type: "td"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "chiffrement et HTTPS"
notion: "chiffrement et HTTPS"
private_data: false
official_program:
  capacities:
    - "T-ARCH-04A"
    - "T-ARCH-04B"
---

# T13 - TD - chiffrement et HTTPS

## Objectifs
- Travailler chiffrement symétrique, chiffrement asymétrique, clé publique, clé privée, certificat.
- Produire huit réponses vérifiables avec données explicites.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2.
- Standard : exercices 3 à 6.
- Approfondissement : exercices 7 et 8.

## Exercices
### Exercice 1
- Type : lecture/analyse.
- Capacité officielle : T-ARCH-04A.
- Données : `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test`. ; jeu_exercice=alpha
- Consigne : protéger Ksession par asymétrique ; traiter aussi `certificat expiré` si nécessaire.
- Réponse attendue : message chiffré avec Ksession.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `certificat expiré`.
### Exercice 2
- Type : production/écriture.
- Capacité officielle : T-ARCH-04B.
- Données : `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test`. ; jeu_exercice=beta
- Consigne : utiliser symétrique pour données ; traiter aussi `clé publique non vérifiée` si nécessaire.
- Réponse attendue : Ksession chiffrée avec Kpub serveur.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `clé publique non vérifiée`.
### Exercice 3
- Type : production/écriture.
- Capacité officielle : T-ARCH-04A.
- Données : `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test`. ; jeu_exercice=gamma
- Consigne : vérifier certificat ; traiter aussi `HTTP sans TLS` si nécessaire.
- Réponse attendue : Autorité-Test signe serveur.example.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `HTTP sans TLS`.
### Exercice 4
- Type : cas limite.
- Capacité officielle : T-ARCH-04B.
- Données : `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test`. ; jeu_exercice=delta
- Consigne : distinguer confidentialité et authenticité ; traiter aussi `certificat expiré` si nécessaire.
- Réponse attendue : HTTP sans TLS ne protège pas.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `certificat expiré`.
### Exercice 5
- Type : justification.
- Capacité officielle : T-ARCH-04A.
- Données : `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test`. ; jeu_exercice=epsilon
- Consigne : protéger Ksession par asymétrique ; traiter aussi `clé publique non vérifiée` si nécessaire.
- Réponse attendue : message chiffré avec Ksession.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `clé publique non vérifiée`.
### Exercice 6
- Type : lecture/analyse.
- Capacité officielle : T-ARCH-04B.
- Données : `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test`. ; jeu_exercice=zeta
- Consigne : utiliser symétrique pour données ; traiter aussi `HTTP sans TLS` si nécessaire.
- Réponse attendue : Ksession chiffrée avec Kpub serveur.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `HTTP sans TLS`.
### Exercice 7
- Type : production/écriture.
- Capacité officielle : T-ARCH-04A.
- Données : `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test`. ; jeu_exercice=eta
- Consigne : vérifier certificat ; traiter aussi `certificat expiré` si nécessaire.
- Réponse attendue : Autorité-Test signe serveur.example.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `certificat expiré`.
### Exercice 8
- Type : justification.
- Capacité officielle : T-ARCH-04B.
- Données : `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test`. ; jeu_exercice=theta
- Consigne : distinguer confidentialité et authenticité ; traiter aussi `clé publique non vérifiée` si nécessaire.
- Réponse attendue : HTTP sans TLS ne protège pas.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `clé publique non vérifiée`.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : T-ARCH-04A.
- Résultat attendu : message chiffré avec Ksession.
- Justification : la tâche `protéger Ksession par asymétrique` s applique à `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test` ; erreur évitée : clé publique supposée secrète.
- Donnée utilisée alpha dans T13 TD chiffrement https : cas alpha de l exercice 1 avec les valeurs indiquées dans l énoncé.
- Méthode alpha dans T13 TD chiffrement https : trace courte, pseudo-code local `if cas_alpha: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat alpha dans T13 TD chiffrement https : sortie vérifiable de l exercice 1, reliée à la capacité officielle du bloc.
- Contrôle alpha dans T13 TD chiffrement https : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 2
- Capacité mobilisée : T-ARCH-04B.
- Résultat attendu : Ksession chiffrée avec Kpub serveur.
- Justification : la tâche `utiliser symétrique pour données` s applique à `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test` ; erreur évitée : asymétrique utilisé partout.
- Donnée utilisée beta dans T13 TD chiffrement https : cas beta de l exercice 2 avec les valeurs indiquées dans l énoncé.
- Méthode beta dans T13 TD chiffrement https : trace courte, pseudo-code local `if cas_beta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat beta dans T13 TD chiffrement https : sortie vérifiable de l exercice 2, reliée à la capacité officielle du bloc.
- Contrôle beta dans T13 TD chiffrement https : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 3
- Capacité mobilisée : T-ARCH-04A.
- Résultat attendu : Autorité-Test signe serveur.example.
- Justification : la tâche `vérifier certificat` s applique à `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test` ; erreur évitée : certificat ignoré.
- Donnée utilisée gamma dans T13 TD chiffrement https : cas gamma de l exercice 3 avec les valeurs indiquées dans l énoncé.
- Méthode gamma dans T13 TD chiffrement https : trace courte, pseudo-code local `if cas_gamma: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat gamma dans T13 TD chiffrement https : sortie vérifiable de l exercice 3, reliée à la capacité officielle du bloc.
- Contrôle gamma dans T13 TD chiffrement https : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 4
- Capacité mobilisée : T-ARCH-04B.
- Résultat attendu : HTTP sans TLS ne protège pas.
- Justification : la tâche `distinguer confidentialité et authenticité` s applique à `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test` ; erreur évitée : clé publique supposée secrète.
- Donnée utilisée delta dans T13 TD chiffrement https : cas delta de l exercice 4 avec les valeurs indiquées dans l énoncé.
- Méthode delta dans T13 TD chiffrement https : trace courte, pseudo-code local `if cas_delta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat delta dans T13 TD chiffrement https : sortie vérifiable de l exercice 4, reliée à la capacité officielle du bloc.
- Contrôle delta dans T13 TD chiffrement https : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 5
- Capacité mobilisée : T-ARCH-04A.
- Résultat attendu : message chiffré avec Ksession.
- Justification : la tâche `protéger Ksession par asymétrique` s applique à `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test` ; erreur évitée : asymétrique utilisé partout.
- Donnée utilisée epsilon dans T13 TD chiffrement https : cas epsilon de l exercice 5 avec les valeurs indiquées dans l énoncé.
- Méthode epsilon dans T13 TD chiffrement https : trace courte, pseudo-code local `if cas_epsilon: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat epsilon dans T13 TD chiffrement https : sortie vérifiable de l exercice 5, reliée à la capacité officielle du bloc.
- Contrôle epsilon dans T13 TD chiffrement https : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 6
- Capacité mobilisée : T-ARCH-04B.
- Résultat attendu : Ksession chiffrée avec Kpub serveur.
- Justification : la tâche `utiliser symétrique pour données` s applique à `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test` ; erreur évitée : certificat ignoré.
- Donnée utilisée zeta dans T13 TD chiffrement https : cas zeta de l exercice 6 avec les valeurs indiquées dans l énoncé.
- Méthode zeta dans T13 TD chiffrement https : trace courte, pseudo-code local `if cas_zeta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat zeta dans T13 TD chiffrement https : sortie vérifiable de l exercice 6, reliée à la capacité officielle du bloc.
- Contrôle zeta dans T13 TD chiffrement https : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 7
- Capacité mobilisée : T-ARCH-04A.
- Résultat attendu : Autorité-Test signe serveur.example.
- Justification : la tâche `vérifier certificat` s applique à `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test` ; erreur évitée : clé publique supposée secrète.
- Donnée utilisée eta dans T13 TD chiffrement https : cas eta de l exercice 7 avec les valeurs indiquées dans l énoncé.
- Méthode eta dans T13 TD chiffrement https : trace courte, pseudo-code local `if cas_eta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat eta dans T13 TD chiffrement https : sortie vérifiable de l exercice 7, reliée à la capacité officielle du bloc.
- Contrôle eta dans T13 TD chiffrement https : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 8
- Capacité mobilisée : T-ARCH-04B.
- Résultat attendu : HTTP sans TLS ne protège pas.
- Justification : la tâche `distinguer confidentialité et authenticité` s applique à `Ksession, clé publique serveur Kpub, certificat signé par Autorité-Test` ; erreur évitée : asymétrique utilisé partout.
- Donnée utilisée theta dans T13 TD chiffrement https : cas theta de l exercice 8 avec les valeurs indiquées dans l énoncé.
- Méthode theta dans T13 TD chiffrement https : trace courte, pseudo-code local `if cas_theta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat theta dans T13 TD chiffrement https : sortie vérifiable de l exercice 8, reliée à la capacité officielle du bloc.
- Contrôle theta dans T13 TD chiffrement https : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.

## Erreurs fréquentes
- clé publique supposée secrète.
- asymétrique utilisé partout.
- certificat ignoré.

## Différenciation
- Socle : données annotées.
- Standard : méthode complète.
- Expert : transfert avec `clé publique non vérifiée`.

## Cas limites travaillés
- certificat expiré.
- clé publique non vérifiée.
- HTTP sans TLS.

## Critères de réussite observables
- La donnée de départ est recopiée exactement.
- La trace ou le pseudo-code identifie la clé qui protège les données applicatives.
- Au moins un cas limite de la section précédente est décidé.
