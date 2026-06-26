---
title: "P03 - Corrige - Texte Unicode et nombres réels"
level: "premiere"
sequence_id: "P03"
document_type: "corrige"
status: "needs_review"
version: "0.3.0"
source: "BO 2019 ; ressource locale candidate : Documents_DRIVE/2_NSI/Programmes et textes officiels/0_Programmes.pdf"
theme: "Données textuelles et approximation"
notion: "Unicode, UTF-8, flottants"
objectifs:
  - "Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation."
  - "Objectif O2 - Appliquer une méthode explicite sur un exemple guidé."
  - "Objectif O3 - Justifier le résultat obtenu sur un cas nouveau."
  - "Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente."
private_data: false
official_program:
  capacities:
    - "P-DATA-BASE-05A"
    - "P-DATA-BASE-05B"
    - "P-DATA-BASE-03"
---


# P03 - Corrige - Texte Unicode et nombres réels

## Objectifs spécifiques
- Objectif O1 - Identifier les données et le vocabulaire opératoire de la situation.
- Objectif O2 - Appliquer une méthode explicite sur un exemple guidé.
- Objectif O3 - Justifier le résultat obtenu sur un cas nouveau.
- Objectif O4 - Contrôler un cas limite et corriger une erreur fréquente.

## Capacités officielles atomiques
- P-DATA-BASE-05A
- P-DATA-BASE-05B
- P-DATA-BASE-03

## Prérequis
- Lire une consigne technique sans confondre donnée, méthode et résultat.
- Écrire une réponse sous forme de phrases courtes et vérifiables.
- Utiliser Python en distinguant expression, valeur, variable et affichage.
- Conserver une trace de calcul ou de raisonnement exploitable pour la révision.

## Séance(s) correspondante(s)
- P03-S1 à P03-S5 : ce support est rattaché aux séances indiquées dans la progression.

## Situation-problème concrète
un formulaire accepte des accents mais un export binaire doit compter caractères, octets et valeurs approchées. La tâche consiste à traiter Unicode, UTF-8, flottants sans réponse intuitive non vérifiée.

## Activité d’entrée
1. Lire la situation : un formulaire accepte des accents mais un export binaire doit compter caractères, octets et valeurs approchées.
2. Isoler la donnée de départ : chaîne Unicode et calcul décimal représenté en binaire.
3. Prédire individuellement le résultat de l’exemple `Aé et 0.1 + 0.2`.
4. Comparer deux stratégies et noter la divergence précise.
5. Appliquer la méthode retenue : distinguer point de code, encodage, octets et approximation machine.
6. Contrôler avec le résultat de référence : 2 caractères, 3 octets, somme flottante non exactement égale à 0.3.
7. Tester le cas limite suivant : caractère hors ASCII ou comparaison directe de flottants.
8. Rédiger une phrase qui relie donnée, méthode, résultat et contrôle.

## Exemple corrigé précis
- Exemple : `Aé et 0.1 + 0.2`.
- Correction : distinguer point de code, encodage, octets et approximation machine.
- Résultat : 2 caractères, 3 octets, somme flottante non exactement égale à 0.3.
- Justification : le raisonnement est lisible et relié à une capacité officielle.

## Exercices numérotés
- Les exercices 1 à 8 du TD sont repris ci-dessous pour rendre la correspondance vérifiable.

### Corrigé exercice 1
- Objectif : O1.
- Capacité : P-DATA-BASE-05A.
- Donnée traitée : chaîne Unicode et calcul décimal représenté en binaire.
- Méthode correcte : distinguer point de code, encodage, octets et approximation machine.
- Résultat de référence : `2 caractères, 3 octets, somme flottante non exactement égale à 0.3`.
- Contrôle : comparer la sortie à la représentation attendue et expliquer l’écart éventuel.
- Erreur fréquente évitée : EF1.
- Remédiation : Activité corrective EF1 si la méthode n’est pas justifiée.

### Corrigé exercice 2
- Objectif : O2.
- Capacité : P-DATA-BASE-05B.
- Donnée traitée : chaîne Unicode et calcul décimal représenté en binaire.
- Méthode correcte : distinguer point de code, encodage, octets et approximation machine.
- Résultat de référence : `2 caractères, 3 octets, somme flottante non exactement égale à 0.3`.
- Contrôle : comparer la sortie à la représentation attendue et expliquer l’écart éventuel.
- Erreur fréquente évitée : EF2.
- Remédiation : Activité corrective EF2 si la méthode n’est pas justifiée.

### Corrigé exercice 3
- Objectif : O3.
- Capacité : P-DATA-BASE-03.
- Donnée traitée : chaîne Unicode et calcul décimal représenté en binaire.
- Méthode correcte : distinguer point de code, encodage, octets et approximation machine.
- Résultat de référence : `2 caractères, 3 octets, somme flottante non exactement égale à 0.3`.
- Contrôle : comparer la sortie à la représentation attendue et expliquer l’écart éventuel.
- Erreur fréquente évitée : EF3.
- Remédiation : Activité corrective EF3 si la méthode n’est pas justifiée.

### Corrigé exercice 4
- Objectif : O4.
- Capacité : P-DATA-BASE-05A.
- Donnée traitée : chaîne Unicode et calcul décimal représenté en binaire.
- Méthode correcte : distinguer point de code, encodage, octets et approximation machine.
- Résultat de référence : `2 caractères, 3 octets, somme flottante non exactement égale à 0.3`.
- Contrôle : comparer la sortie à la représentation attendue et expliquer l’écart éventuel.
- Erreur fréquente évitée : EF4.
- Remédiation : Activité corrective EF4 si la méthode n’est pas justifiée.

### Corrigé exercice 5
- Objectif : O1.
- Capacité : P-DATA-BASE-05B.
- Donnée traitée : chaîne Unicode et calcul décimal représenté en binaire.
- Méthode correcte : distinguer point de code, encodage, octets et approximation machine.
- Résultat de référence : `2 caractères, 3 octets, somme flottante non exactement égale à 0.3`.
- Contrôle : comparer la sortie à la représentation attendue et expliquer l’écart éventuel.
- Erreur fréquente évitée : EF1.
- Remédiation : Activité corrective EF1 si la méthode n’est pas justifiée.

### Corrigé exercice 6
- Objectif : O2.
- Capacité : P-DATA-BASE-03.
- Donnée traitée : chaîne Unicode et calcul décimal représenté en binaire.
- Méthode correcte : distinguer point de code, encodage, octets et approximation machine.
- Résultat de référence : `2 caractères, 3 octets, somme flottante non exactement égale à 0.3`.
- Contrôle : comparer la sortie à la représentation attendue et expliquer l’écart éventuel.
- Erreur fréquente évitée : EF2.
- Remédiation : Activité corrective EF2 si la méthode n’est pas justifiée.

### Corrigé exercice 7
- Objectif : O3.
- Capacité : P-DATA-BASE-05A.
- Donnée traitée : chaîne Unicode et calcul décimal représenté en binaire.
- Méthode correcte : distinguer point de code, encodage, octets et approximation machine.
- Résultat de référence : `2 caractères, 3 octets, somme flottante non exactement égale à 0.3`.
- Contrôle : comparer la sortie à la représentation attendue et expliquer l’écart éventuel.
- Erreur fréquente évitée : EF3.
- Remédiation : Activité corrective EF3 si la méthode n’est pas justifiée.

### Corrigé exercice 8
- Objectif : O4.
- Capacité : P-DATA-BASE-05B.
- Donnée traitée : chaîne Unicode et calcul décimal représenté en binaire.
- Méthode correcte : distinguer point de code, encodage, octets et approximation machine.
- Résultat de référence : `2 caractères, 3 octets, somme flottante non exactement égale à 0.3`.
- Contrôle : comparer la sortie à la représentation attendue et expliquer l’écart éventuel.
- Erreur fréquente évitée : EF4.
- Remédiation : Activité corrective EF4 si la méthode n’est pas justifiée.

## Barème de correction
- Méthode explicite : 4 points.
- Résultat correct : 3 points.
- Justification reliée à la capacité : 2 points.
- Contrôle ou cas limite : 1 point.

## Erreurs fréquentes
- Erreur fréquente EF1 - répondre seulement par `2 caractères, 3 octets, somme flottante non exactement égale à 0.3` sans écrire la méthode.
- Erreur fréquente EF2 - appliquer distinguer point de code, encodage, octets et approximation machine dans le mauvais ordre.
- Erreur fréquente EF3 - oublier le cas limite : caractère hors ASCII ou comparaison directe de flottants.
- Erreur fréquente EF4 - citer une capacité officielle sans la relier à une production observable.

## Remédiation ciblée
- Activité corrective EF1 : reprendre l’exemple en imposant quatre colonnes, donnée, opération, résultat, contrôle.
- Activité corrective EF2 : refaire la méthode avec des étapes numérotées et une vérification à chaque étape.
- Activité corrective EF3 : construire deux variantes du cas limite `caractère hors ASCII ou comparaison directe de flottants` et comparer les sorties.
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

