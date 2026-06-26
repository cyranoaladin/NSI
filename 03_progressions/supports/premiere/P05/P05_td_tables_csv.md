---
title: "P05 - Td - Tables CSV et requêtes simples"
level: "premiere"
sequence_id: "P05"
document_type: "td"
status: "needs_review"
version: "0.3.0"
source: "BO 2019 ; ressource locale candidate : Documents_DRIVE/1_1ères NSI/3_Bloc3_TdDeT/Evaluation/T.P_TdDeT.docx"
theme: "Traitement de tables"
notion: "CSV, dictionnaire ligne, sélection, projection"
objectifs:
  - "Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation."
  - "Objectif O2 - Appliquer une méthode explicite sur un exemple guidé."
  - "Objectif O3 - Justifier le résultat obtenu sur un cas nouveau."
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente."
private_data: false
official_program:
  capacities:
    - "P-TABLE-01"
    - "P-TABLE-02"
---


# P05 - Td - Tables CSV et requêtes simples

## Objectifs spécifiques
- Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation.
- Objectif O2 - Appliquer une méthode explicite sur un exemple guidé.
- Objectif O3 - Justifier le résultat obtenu sur un cas nouveau.
- Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente.

## Capacités officielles atomiques
- P-TABLE-01
- P-TABLE-02

## Prérequis
- Lire une consigne technique sans confondre donnée, méthode et résultat.
- Écrire une réponse sous forme de phrases courtes et vérifiables.
- Utiliser Python en distinguant expression, valeur, variable et affichage.
- Conserver une trace de calcul ou de raisonnement exploitable pour la révision.

## Séance(s) correspondante(s)
- P05-S1 à P05-S6 : ce support est rattaché aux séances indiquées dans la progression.

## Situation-problème concrète
une association reçoit un fichier CSV de réservations et veut filtrer les lignes incohérentes. La tâche consiste à traiter CSV, dictionnaire ligne, sélection, projection sans réponse intuitive non vérifiée.

## Activité d’entrée
1. Lire la situation : une association reçoit un fichier CSV de réservations et veut filtrer les lignes incohérentes.
2. Isoler la donnée de départ : table structurée en lignes et colonnes.
3. Prédire individuellement le résultat de l’exemple `nom;age;ville avec trois enregistrements`.
4. Comparer deux stratégies et noter la divergence précise.
5. Appliquer la méthode retenue : lire l’en-tête, convertir les champs utiles, filtrer puis agréger.
6. Contrôler avec le résultat de référence : liste de dictionnaires filtrée puis moyenne calculée.
7. Tester le cas limite suivant : champ vide, séparateur inattendu ou nombre invalide.
8. Rédiger une phrase qui relie donnée, méthode, résultat et contrôle.

## Exemple corrigé précis
- Exemple : `nom;age;ville avec trois enregistrements`.
- Méthode : lire l’en-tête, convertir les champs utiles, filtrer puis agréger.
- Résultat : liste de dictionnaires filtrée puis moyenne calculée.
- Justification : chaque étape transforme une donnée identifiable.

## Exercices numérotés
### Exercice 1
- Objectif travaillé : O1.
- Capacité officielle : P-TABLE-01.
- Énoncé : résoudre une variante de `nom;age;ville avec trois enregistrements` en changeant une donnée contrôlée.
- Travail demandé : appliquer lire l’en-tête, convertir les champs utiles, filtrer puis agréger, puis rédiger le contrôle.
- Contrainte : citer le cas limite `champ vide, séparateur inattendu ou nombre invalide` si la méthode peut échouer.
- Production attendue : réponse en trois lignes, méthode, résultat, vérification.
- Critère de réussite : aucun résultat n’est donné sans justification.

### Exercice 2
- Objectif travaillé : O2.
- Capacité officielle : P-TABLE-02.
- Énoncé : résoudre une variante de `nom;age;ville avec trois enregistrements` en changeant une donnée contrôlée.
- Travail demandé : appliquer lire l’en-tête, convertir les champs utiles, filtrer puis agréger, puis rédiger le contrôle.
- Contrainte : citer le cas limite `champ vide, séparateur inattendu ou nombre invalide` si la méthode peut échouer.
- Production attendue : réponse en trois lignes, méthode, résultat, vérification.
- Critère de réussite : aucun résultat n’est donné sans justification.

### Exercice 3
- Objectif travaillé : O3.
- Capacité officielle : P-TABLE-01.
- Énoncé : résoudre une variante de `nom;age;ville avec trois enregistrements` en changeant une donnée contrôlée.
- Travail demandé : appliquer lire l’en-tête, convertir les champs utiles, filtrer puis agréger, puis rédiger le contrôle.
- Contrainte : citer le cas limite `champ vide, séparateur inattendu ou nombre invalide` si la méthode peut échouer.
- Production attendue : réponse en trois lignes, méthode, résultat, vérification.
- Critère de réussite : aucun résultat n’est donné sans justification.

### Exercice 4
- Objectif travaillé : O4.
- Capacité officielle : P-TABLE-02.
- Énoncé : résoudre une variante de `nom;age;ville avec trois enregistrements` en changeant une donnée contrôlée.
- Travail demandé : appliquer lire l’en-tête, convertir les champs utiles, filtrer puis agréger, puis rédiger le contrôle.
- Contrainte : citer le cas limite `champ vide, séparateur inattendu ou nombre invalide` si la méthode peut échouer.
- Production attendue : réponse en trois lignes, méthode, résultat, vérification.
- Critère de réussite : aucun résultat n’est donné sans justification.

### Exercice 5
- Objectif travaillé : O1.
- Capacité officielle : P-TABLE-01.
- Énoncé : résoudre une variante de `nom;age;ville avec trois enregistrements` en changeant une donnée contrôlée.
- Travail demandé : appliquer lire l’en-tête, convertir les champs utiles, filtrer puis agréger, puis rédiger le contrôle.
- Contrainte : citer le cas limite `champ vide, séparateur inattendu ou nombre invalide` si la méthode peut échouer.
- Production attendue : réponse en trois lignes, méthode, résultat, vérification.
- Critère de réussite : aucun résultat n’est donné sans justification.

### Exercice 6
- Objectif travaillé : O2.
- Capacité officielle : P-TABLE-02.
- Énoncé : résoudre une variante de `nom;age;ville avec trois enregistrements` en changeant une donnée contrôlée.
- Travail demandé : appliquer lire l’en-tête, convertir les champs utiles, filtrer puis agréger, puis rédiger le contrôle.
- Contrainte : citer le cas limite `champ vide, séparateur inattendu ou nombre invalide` si la méthode peut échouer.
- Production attendue : réponse en trois lignes, méthode, résultat, vérification.
- Critère de réussite : aucun résultat n’est donné sans justification.

### Exercice 7
- Objectif travaillé : O3.
- Capacité officielle : P-TABLE-01.
- Énoncé : résoudre une variante de `nom;age;ville avec trois enregistrements` en changeant une donnée contrôlée.
- Travail demandé : appliquer lire l’en-tête, convertir les champs utiles, filtrer puis agréger, puis rédiger le contrôle.
- Contrainte : citer le cas limite `champ vide, séparateur inattendu ou nombre invalide` si la méthode peut échouer.
- Production attendue : réponse en trois lignes, méthode, résultat, vérification.
- Critère de réussite : aucun résultat n’est donné sans justification.

### Exercice 8
- Objectif travaillé : O4.
- Capacité officielle : P-TABLE-02.
- Énoncé : résoudre une variante de `nom;age;ville avec trois enregistrements` en changeant une donnée contrôlée.
- Travail demandé : appliquer lire l’en-tête, convertir les champs utiles, filtrer puis agréger, puis rédiger le contrôle.
- Contrainte : citer le cas limite `champ vide, séparateur inattendu ou nombre invalide` si la méthode peut échouer.
- Production attendue : réponse en trois lignes, méthode, résultat, vérification.
- Critère de réussite : aucun résultat n’est donné sans justification.

## Corrigé
### Corrigé exercice 1
- On repère d’abord table structurée en lignes et colonnes.
- On applique ensuite lire l’en-tête, convertir les champs utiles, filtrer puis agréger.
- Le résultat attendu est `liste de dictionnaires filtrée puis moyenne calculée` pour l’exemple de référence ou une valeur cohérente pour la variante.
- L’erreur EF1 est évitée car la vérification est écrite.

### Corrigé exercice 2
- On repère d’abord table structurée en lignes et colonnes.
- On applique ensuite lire l’en-tête, convertir les champs utiles, filtrer puis agréger.
- Le résultat attendu est `liste de dictionnaires filtrée puis moyenne calculée` pour l’exemple de référence ou une valeur cohérente pour la variante.
- L’erreur EF2 est évitée car la vérification est écrite.

### Corrigé exercice 3
- On repère d’abord table structurée en lignes et colonnes.
- On applique ensuite lire l’en-tête, convertir les champs utiles, filtrer puis agréger.
- Le résultat attendu est `liste de dictionnaires filtrée puis moyenne calculée` pour l’exemple de référence ou une valeur cohérente pour la variante.
- L’erreur EF3 est évitée car la vérification est écrite.

### Corrigé exercice 4
- On repère d’abord table structurée en lignes et colonnes.
- On applique ensuite lire l’en-tête, convertir les champs utiles, filtrer puis agréger.
- Le résultat attendu est `liste de dictionnaires filtrée puis moyenne calculée` pour l’exemple de référence ou une valeur cohérente pour la variante.
- L’erreur EF4 est évitée car la vérification est écrite.

### Corrigé exercice 5
- On repère d’abord table structurée en lignes et colonnes.
- On applique ensuite lire l’en-tête, convertir les champs utiles, filtrer puis agréger.
- Le résultat attendu est `liste de dictionnaires filtrée puis moyenne calculée` pour l’exemple de référence ou une valeur cohérente pour la variante.
- L’erreur EF1 est évitée car la vérification est écrite.

### Corrigé exercice 6
- On repère d’abord table structurée en lignes et colonnes.
- On applique ensuite lire l’en-tête, convertir les champs utiles, filtrer puis agréger.
- Le résultat attendu est `liste de dictionnaires filtrée puis moyenne calculée` pour l’exemple de référence ou une valeur cohérente pour la variante.
- L’erreur EF2 est évitée car la vérification est écrite.

### Corrigé exercice 7
- On repère d’abord table structurée en lignes et colonnes.
- On applique ensuite lire l’en-tête, convertir les champs utiles, filtrer puis agréger.
- Le résultat attendu est `liste de dictionnaires filtrée puis moyenne calculée` pour l’exemple de référence ou une valeur cohérente pour la variante.
- L’erreur EF3 est évitée car la vérification est écrite.

### Corrigé exercice 8
- On repère d’abord table structurée en lignes et colonnes.
- On applique ensuite lire l’en-tête, convertir les champs utiles, filtrer puis agréger.
- Le résultat attendu est `liste de dictionnaires filtrée puis moyenne calculée` pour l’exemple de référence ou une valeur cohérente pour la variante.
- L’erreur EF4 est évitée car la vérification est écrite.

## Erreurs fréquentes
- Erreur fréquente EF1 - répondre seulement par `liste de dictionnaires filtrée puis moyenne calculée` sans écrire la méthode.
- Erreur fréquente EF2 - appliquer lire l’en-tête, convertir les champs utiles, filtrer puis agréger dans le mauvais ordre.
- Erreur fréquente EF3 - oublier le cas limite : champ vide, séparateur inattendu ou nombre invalide.
- Erreur fréquente EF4 - citer une capacité officielle sans la relier à une production observable.

## Remédiation ciblée
- Activité corrective EF1 : reprendre l’exemple en imposant quatre colonnes, donnée, opération, résultat, contrôle.
- Activité corrective EF2 : refaire la méthode avec des étapes numérotées et une vérification à chaque étape.
- Activité corrective EF3 : construire deux variantes du cas limite `champ vide, séparateur inattendu ou nombre invalide` et comparer les sorties.
- Activité corrective EF4 : associer chaque phrase de réponse à une capacité officielle citée en début de copie.

## Différenciation
- Socle : la méthode est fournie sous forme de tableau à compléter.
- Standard : l’élève choisit la méthode et rédige la justification complète.
- Expert : l’élève crée un contre-exemple ou un cas limite et explique l’échec attendu.

## Critères de réussite
- Les objectifs O1 à O4 apparaissent dans la production ou dans la correction.
- Au moins une capacité officielle est reliée à une question traitée.
- Le résultat est accompagné d’une méthode et d’un contrôle.
- Les erreurs fréquentes sont nommées et corrigées par une activité de remédiation.

