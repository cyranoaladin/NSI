---
title: "P08 - Cours - HTML, CSS, DOM, HTTP GET/POST"
level: "premiere"
sequence_id: "P08"
document_type: "cours"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "IHM sur le Web"
notion: "HTML, CSS, DOM, HTTP GET/POST"
objectifs:
  - "identifier la donnée de référence"
  - "appliquer la méthode disciplinaire"
  - "produire un résultat vérifiable"
  - "contrôler un cas limite"
private_data: false
official_program:
  capacities:
    - "P-IHM-01A"
    - "P-IHM-01B"
    - "P-IHM-02"
    - "P-IHM-03A"
    - "P-IHM-03B"
    - "P-IHM-03C"
---

# P08 - Cours - HTML, CSS, DOM, HTTP GET/POST

## Objectifs
- Lire la situation sans modifier les données.
- Appliquer une méthode explicitement liée aux capacités.
- Produire un résultat contrôlable.

## Capacités travaillées
- P-IHM-01A
- P-IHM-01B
- P-IHM-02
- P-IHM-03A
- P-IHM-03B
- P-IHM-03C

## Situation-problème
Une page de réservation affiche un formulaire et met à jour une zone DOM après validation.

## Données de référence
`<form method="post" action="/reservation"><input name="nom"><button>Envoyer</button></form>`

## Méthodes disciplinaires
- séparer structure HTML, style CSS et comportement DOM.
- identifier méthode GET pour lecture et POST pour envoi.
- modifier textContent sans injecter de HTML non contrôlé.

## Exemple corrigé 1
Donnée : `<form method="post" action="/reservation"><input name="nom"><button>Envoyer</button></form>`.
Méthode : séparer structure HTML, style CSS et comportement DOM.
Résultat : le formulaire POST transporte nom=Ada ; le DOM affiche Réservation enregistrée pour Ada ; GET reste réservé à une URL consultable.

## Exemple corrigé 2 - cas limite
On modifie une seule donnée pour tester le cas limite du chapitre. La correction attendue explique pourquoi la méthode reste valable ou pourquoi elle doit refuser l’entrée.

## Erreurs fréquentes
- Confondre une clé, un indice ou un état temporaire avec la donnée stable.
- Conclure sans écrire le résultat contrôlable.
- Oublier le cas vide, absent ou invalide.

## Exercices intégrés
1. Reprendre la donnée de référence et écrire toutes les étapes.
2. Modifier une valeur et prévoir le nouveau résultat.
3. Construire un cas limite et dire si la méthode accepte ou refuse.
4. Relier chaque étape à une capacité officielle.
