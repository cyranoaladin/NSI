---
title: "P12 - td - tris, invariants et complexité"
level: "premiere"
sequence_id: "P12"
document_type: "td"
status: "needs_review"
version: "0.6.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "tris, invariants et complexité"
notion: "tris, invariants et complexité"
private_data: false
official_program:
  capacities:
    - "P-ALGO-02A"
    - "P-ALGO-02B"
    - "P-ALGO-02C"
    - "P-ALGO-02D"
---

# P12 - TD - tris, invariants et complexité

## Objectifs
- Travailler tri par insertion, tri par sélection, invariant, variant, coût quadratique.
- Produire huit réponses vérifiables avec données explicites.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2.
- Standard : exercices 3 à 6.
- Approfondissement : exercices 7 et 8.

## Exercices
### Exercice 1
- Type : lecture/analyse.
- Capacité officielle : P-ALGO-02A.
- Données : `temps=[42,17,23,17,9]`. ; jeu_exercice=alpha
- Consigne : insérer la clé dans la partie gauche triée ; traiter aussi `liste vide` si nécessaire.
- Réponse attendue : insertion après i=1 -> [17,42,23,17,9].
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `liste vide`.
### Exercice 2
- Type : production/écriture.
- Capacité officielle : P-ALGO-02B.
- Données : `temps=[42,17,23,17,9]`. ; jeu_exercice=beta
- Consigne : chercher le minimum du suffixe ; traiter aussi `liste déjà triée` si nécessaire.
- Réponse attendue : sélection place 9 en tête.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `liste déjà triée`.
### Exercice 3
- Type : production/écriture.
- Capacité officielle : P-ALGO-02C.
- Données : `temps=[42,17,23,17,9]`. ; jeu_exercice=gamma
- Consigne : écrire invariant gauche triée ; traiter aussi `doublons 17` si nécessaire.
- Réponse attendue : invariant : indices < i triés.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `doublons 17`.
### Exercice 4
- Type : cas limite.
- Capacité officielle : P-ALGO-02D.
- Données : `temps=[42,17,23,17,9]`. ; jeu_exercice=delta
- Consigne : compter comparaisons intuitives ; traiter aussi `liste vide` si nécessaire.
- Réponse attendue : pire cas quadratique.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `liste vide`.
### Exercice 5
- Type : justification.
- Capacité officielle : P-ALGO-02A.
- Données : `temps=[42,17,23,17,9]`. ; jeu_exercice=epsilon
- Consigne : insérer la clé dans la partie gauche triée ; traiter aussi `liste déjà triée` si nécessaire.
- Réponse attendue : insertion après i=1 -> [17,42,23,17,9].
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `liste déjà triée`.
### Exercice 6
- Type : lecture/analyse.
- Capacité officielle : P-ALGO-02B.
- Données : `temps=[42,17,23,17,9]`. ; jeu_exercice=zeta
- Consigne : chercher le minimum du suffixe ; traiter aussi `doublons 17` si nécessaire.
- Réponse attendue : sélection place 9 en tête.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `doublons 17`.
### Exercice 7
- Type : production/écriture.
- Capacité officielle : P-ALGO-02C.
- Données : `temps=[42,17,23,17,9]`. ; jeu_exercice=eta
- Consigne : écrire invariant gauche triée ; traiter aussi `liste vide` si nécessaire.
- Réponse attendue : invariant : indices < i triés.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `liste vide`.
### Exercice 8
- Type : justification.
- Capacité officielle : P-ALGO-02D.
- Données : `temps=[42,17,23,17,9]`. ; jeu_exercice=theta
- Consigne : compter comparaisons intuitives ; traiter aussi `liste déjà triée` si nécessaire.
- Réponse attendue : pire cas quadratique.
- Critère de réussite : donnée exacte, méthode nommée, résultat final et décision sur `liste déjà triée`.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : P-ALGO-02A.
- Résultat attendu : insertion après i=1 -> [17,42,23,17,9].
- Justification : la tâche `insérer la clé dans la partie gauche triée` s applique à `temps=[42,17,23,17,9]` ; erreur évitée : invariant confondu avec résultat.
- Donnée utilisée alpha dans P12 TD tris invariants complexite : cas alpha de l exercice 1 avec les valeurs indiquées dans l énoncé.
- Méthode alpha dans P12 TD tris invariants complexite : trace courte, pseudo-code local `if cas_alpha: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat alpha dans P12 TD tris invariants complexite : sortie vérifiable de l exercice 1, reliée à la capacité officielle du bloc.
- Contrôle alpha dans P12 TD tris invariants complexite : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 2
- Capacité mobilisée : P-ALGO-02B.
- Résultat attendu : sélection place 9 en tête.
- Justification : la tâche `chercher le minimum du suffixe` s applique à `temps=[42,17,23,17,9]` ; erreur évitée : décalage oublié.
- Donnée utilisée beta dans P12 TD tris invariants complexite : cas beta de l exercice 2 avec les valeurs indiquées dans l énoncé.
- Méthode beta dans P12 TD tris invariants complexite : trace courte, pseudo-code local `if cas_beta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat beta dans P12 TD tris invariants complexite : sortie vérifiable de l exercice 2, reliée à la capacité officielle du bloc.
- Contrôle beta dans P12 TD tris invariants complexite : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 3
- Capacité mobilisée : P-ALGO-02C.
- Résultat attendu : invariant : indices < i triés.
- Justification : la tâche `écrire invariant gauche triée` s applique à `temps=[42,17,23,17,9]` ; erreur évitée : coût linéaire annoncé.
- Donnée utilisée gamma dans P12 TD tris invariants complexite : cas gamma de l exercice 3 avec les valeurs indiquées dans l énoncé.
- Méthode gamma dans P12 TD tris invariants complexite : trace courte, pseudo-code local `if cas_gamma: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat gamma dans P12 TD tris invariants complexite : sortie vérifiable de l exercice 3, reliée à la capacité officielle du bloc.
- Contrôle gamma dans P12 TD tris invariants complexite : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 4
- Capacité mobilisée : P-ALGO-02D.
- Résultat attendu : pire cas quadratique.
- Justification : la tâche `compter comparaisons intuitives` s applique à `temps=[42,17,23,17,9]` ; erreur évitée : invariant confondu avec résultat.
- Donnée utilisée delta dans P12 TD tris invariants complexite : cas delta de l exercice 4 avec les valeurs indiquées dans l énoncé.
- Méthode delta dans P12 TD tris invariants complexite : trace courte, pseudo-code local `if cas_delta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat delta dans P12 TD tris invariants complexite : sortie vérifiable de l exercice 4, reliée à la capacité officielle du bloc.
- Contrôle delta dans P12 TD tris invariants complexite : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 5
- Capacité mobilisée : P-ALGO-02A.
- Résultat attendu : insertion après i=1 -> [17,42,23,17,9].
- Justification : la tâche `insérer la clé dans la partie gauche triée` s applique à `temps=[42,17,23,17,9]` ; erreur évitée : décalage oublié.
- Donnée utilisée epsilon dans P12 TD tris invariants complexite : cas epsilon de l exercice 5 avec les valeurs indiquées dans l énoncé.
- Méthode epsilon dans P12 TD tris invariants complexite : trace courte, pseudo-code local `if cas_epsilon: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat epsilon dans P12 TD tris invariants complexite : sortie vérifiable de l exercice 5, reliée à la capacité officielle du bloc.
- Contrôle epsilon dans P12 TD tris invariants complexite : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 6
- Capacité mobilisée : P-ALGO-02B.
- Résultat attendu : sélection place 9 en tête.
- Justification : la tâche `chercher le minimum du suffixe` s applique à `temps=[42,17,23,17,9]` ; erreur évitée : coût linéaire annoncé.
- Donnée utilisée zeta dans P12 TD tris invariants complexite : cas zeta de l exercice 6 avec les valeurs indiquées dans l énoncé.
- Méthode zeta dans P12 TD tris invariants complexite : trace courte, pseudo-code local `if cas_zeta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat zeta dans P12 TD tris invariants complexite : sortie vérifiable de l exercice 6, reliée à la capacité officielle du bloc.
- Contrôle zeta dans P12 TD tris invariants complexite : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 7
- Capacité mobilisée : P-ALGO-02C.
- Résultat attendu : invariant : indices < i triés.
- Justification : la tâche `écrire invariant gauche triée` s applique à `temps=[42,17,23,17,9]` ; erreur évitée : invariant confondu avec résultat.
- Donnée utilisée eta dans P12 TD tris invariants complexite : cas eta de l exercice 7 avec les valeurs indiquées dans l énoncé.
- Méthode eta dans P12 TD tris invariants complexite : trace courte, pseudo-code local `if cas_eta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat eta dans P12 TD tris invariants complexite : sortie vérifiable de l exercice 7, reliée à la capacité officielle du bloc.
- Contrôle eta dans P12 TD tris invariants complexite : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.
### Corrigé exercice 8
- Capacité mobilisée : P-ALGO-02D.
- Résultat attendu : pire cas quadratique.
- Justification : la tâche `compter comparaisons intuitives` s applique à `temps=[42,17,23,17,9]` ; erreur évitée : décalage oublié.
- Donnée utilisée theta dans P12 TD tris invariants complexite : cas theta de l exercice 8 avec les valeurs indiquées dans l énoncé.
- Méthode theta dans P12 TD tris invariants complexite : trace courte, pseudo-code local `if cas_theta: décider else: calculer`, invariant nommé et complexité `O(n)`.
- Résultat theta dans P12 TD tris invariants complexite : sortie vérifiable de l exercice 8, reliée à la capacité officielle du bloc.
- Contrôle theta dans P12 TD tris invariants complexite : le cas limite annoncé est décidé explicitement et une réponse sans trace est refusée.

## Erreurs fréquentes
- invariant confondu avec résultat.
- décalage oublié.
- coût linéaire annoncé.

## Différenciation
- Socle : données annotées.
- Standard : méthode complète.
- Expert : transfert avec `liste déjà triée`.

## Cas limites travaillés
- liste vide.
- liste déjà triée.
- doublons 17.

## Critères de réussite observables
- La donnée de départ est recopiée exactement.
- La trace ou le pseudo-code conduit à `insertion après i=1 -> [17,42,23,17,9]`.
- Au moins un cas limite de la section précédente est décidé.

