---
title: "P03 - Fiche cours - Flottants et approximations"
level: "premiere"
sequence_id: "P03"
document_type: "fiche_cours"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Représentation des réels"
notion: "flottants"
official_program:
  capacities:
    - "P-DATA-BASE-03"
private_data: false
---
# P03 - Fiche cours - Flottants et approximations

## À savoir
- Capacités travaillées dans la fiche : P-DATA-BASE-03.
- Un flottant représente une approximation d’un nombre réel.
- Certaines fractions décimales n’ont pas d’écriture binaire finie.
- Le programme ne demande pas le détail complet de la norme IEEE-754.
- Une égalité stricte entre résultats flottants peut être fragile.

## Méthodes
1. Afficher un résultat avec davantage de décimales pour observer l’approximation.
2. Comparer deux valeurs avec une tolérance.
3. Éviter d’arrondir à chaque étape intermédiaire.
4. Raisonner sur l’ordre de grandeur de l’erreur.

## Exemples corrigés
### Exemple corrigé 1
`0.1 + 0.2` peut donner `0.30000000000000004`.
### Exemple corrigé 2
`abs(x - 0.3) < 1e-9` teste une proximité raisonnable.

## Erreurs fréquentes
- Dire que la machine calcule faux : parler de représentation approchée.
- Tester `x == 0.3` après un calcul : utiliser une tolérance.
- Arrondir trop tôt : conserver les valeurs jusqu’à la fin.

## Cas limites
- 0,5 est représentable exactement en binaire.
- 0,1 ne l’est pas exactement.
- Ajouter un très petit flottant à un très grand peut ne rien changer visiblement.

## Mini-exercices
### Mini-exercice 1
Prévoir le risque de `0.1 + 0.2 == 0.3`.
### Mini-exercice 2
Écrire un test tolérant.
### Mini-exercice 3
Dire pourquoi 0,5 est particulier.
### Mini-exercice 4
Formuler une conclusion sur une approximation.

## Réponses rapides
1. Le test peut être faux.
2. `abs(x - 0.3) < 1e-9`.
3. 0,5 vaut 1/2.
4. Le résultat est approché mais contrôlable.

## À retenir
- Pour flottants, commencer par reconnaître la situation exacte.
- Une méthode de P03 doit être accompagnée d’un exemple numérique ou textuel.
- Les capacités P-DATA-BASE-03 restent au statut de travail tant que la revue humaine manque.
- La fiche prépare la révision de flottants sans produire à elle seule une preuve de couverture annuelle.
- Un cas limite explicite est obligatoire avant toute conclusion sur flottants.

## Lien avec la progression
- Séances : P03-S1 et P03-S2 lorsque le chapitre est découpé en plusieurs temps.
- TD lié : P03_TD_flottants.md, à produire ou relire dans le registre de supports.
- TP lié : P03_TP_flottants.py si la progression prévoit une manipulation programmée.
- Évaluation ou projet lié : contrôle court du chapitre P03 ou livrable associé.
- Dossier de progression : 03_progressions/fiches_cours/premiere/P03/.

## Auto-évaluation
- Je sais expliquer flottants sans lire la fiche.
- Je sais refaire les exemples de P03 avec des données différentes.
- Je sais identifier l’erreur fréquente la plus probable pour flottants.
- Je sais choisir un cas limite de flottants avant de répondre.
- Je sais relier la fiche P03 sur flottants à une séance, un TD ou un TP du chapitre.
