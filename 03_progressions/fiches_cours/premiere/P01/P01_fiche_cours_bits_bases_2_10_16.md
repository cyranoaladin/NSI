---
title: "P01 - Fiche cours - Bits et bases 2, 10, 16"
level: "premiere"
sequence_id: "P01"
document_type: "fiche_cours"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Représentation des entiers"
notion: "bits et bases"
official_program:
  capacities:
    - "P-DATA-BASE-01"
private_data: false
---
# P01 - Fiche cours - Bits et bases 2, 10, 16

## À savoir
- Capacités travaillées dans la fiche : P-DATA-BASE-01.
- Un bit vaut 0 ou 1 et prend sa valeur grâce à sa position.
- En base 2 les poids sont 1, 2, 4, 8 ; en base 16 ils sont 1, 16, 256.
- Quatre bits correspondent exactement à un chiffre hexadécimal.
- 45 en base dix, 101101 en base deux et 2D en base seize désignent la même quantité.

## Méthodes
1. Écrire les poids sous les chiffres avant de calculer.
2. Vérifier que chaque symbole appartient à la base.
3. Grouper le binaire par paquets de quatre pour passer en hexadécimal.
4. Contrôler l’ordre de grandeur avec la puissance de deux la plus proche.

## Exemples corrigés
### Exemple corrigé 1
101101₂ vaut 32 + 8 + 4 + 1 = 45₁₀.
### Exemple corrigé 2
11101010₂ se groupe en 1110 1010, donc EA₁₆.

## Erreurs fréquentes
- Lire un mot binaire comme un nombre décimal : revenir aux poids.
- Écrire le chiffre 2 dans une base deux : contrôler l’alphabet.
- Ajouter les zéros de regroupement à droite : les ajouter à gauche seulement.

## Cas limites
- 0 garde l’écriture 0.
- 1 garde l’écriture 1 dans les bases usuelles.
- 255 correspond à 11111111₂ et FF₁₆.

## Mini-exercices
### Mini-exercice 1
Calculer 11001₂ en base dix.
### Mini-exercice 2
Dire si 1201₂ est valide.
### Mini-exercice 3
Convertir 10101111₂ en hexadécimal.
### Mini-exercice 4
Encadrer 73 entre deux puissances de deux.

## Réponses rapides
1. 11001₂ = 25.
2. Non, le symbole 2 est interdit.
3. 10101111₂ = AF₁₆.
4. 64 <= 73 < 128.

## À retenir
- Pour bits et bases, commencer par reconnaître la situation exacte.
- Une méthode de P01 doit être accompagnée d’un exemple numérique ou textuel.
- Les capacités P-DATA-BASE-01 restent au statut de travail tant que la revue humaine manque.
- La fiche prépare la révision de bits et bases sans produire à elle seule une preuve de couverture annuelle.
- Un cas limite explicite est obligatoire avant toute conclusion sur bits_et_bases.

## Lien avec la progression
- Séances : P01-S1 et P01-S2 lorsque le chapitre est découpé en plusieurs temps.
- TD lié : P01_TD_bits_et_bases.md, à produire ou relire dans le registre de supports.
- TP lié : P01_TP_bits_et_bases.py si la progression prévoit une manipulation programmée.
- Évaluation ou projet lié : contrôle court du chapitre P01 ou livrable associé.
- Dossier de progression : 03_progressions/fiches_cours/premiere/P01/.

## Auto-évaluation
- Je sais expliquer bits et bases sans lire la fiche.
- Je sais refaire les exemples de P01 avec des données différentes.
- Je sais identifier l’erreur fréquente la plus probable pour bits et bases.
- Je sais choisir un cas limite de bits et bases avant de répondre.
- Je sais relier la fiche P01 sur bits et bases à une séance, un TD ou un TP du chapitre.
