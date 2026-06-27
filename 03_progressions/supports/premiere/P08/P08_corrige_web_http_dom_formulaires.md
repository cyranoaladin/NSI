---
title: "P08 - Corrigé - HTML, CSS, DOM, HTTP GET/POST"
level: "premiere"
sequence_id: "P08"
document_type: "corrige"
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

# P08 - Corrigé - HTML, CSS, DOM, HTTP GET/POST

## Réponse attendue principale
Donnée : `<form method="post" action="/reservation"><input name="nom"><button>Envoyer</button></form>`.
Étapes :
- séparer structure HTML, style CSS et comportement DOM.
- identifier méthode GET pour lecture et POST pour envoi.
- modifier textContent sans injecter de HTML non contrôlé.
Résultat final : le formulaire POST transporte nom=Ada ; le DOM affiche Réservation enregistrée pour Ada ; GET reste réservé à une URL consultable.

## Corrigé des exercices
### Exercice 1
La donnée de référence est recopiée, puis la première méthode est appliquée. Résultat : le formulaire POST transporte nom=Ada ; le DOM affiche Réservation enregistrée pour Ada ; GET reste réservé à une URL consultable.
### Exercice 2
La variante doit conserver la structure du problème et produire un résultat recalculé.
### Exercice 3
Le cas limite est accepté seulement si la copie indique l’effet exact sur la méthode.
### Exercice 4
La capacité citée doit être reliée à une étape précise du raisonnement.
