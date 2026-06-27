---
title: "P08 - Trace écrite - HTML, CSS, DOM, HTTP GET/POST"
level: "premiere"
sequence_id: "P08"
document_type: "trace"
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

# P08 - Trace écrite - HTML, CSS, DOM, HTTP GET/POST

## À retenir
- Situation : Une page de réservation affiche un formulaire et met à jour une zone DOM après validation.
- Donnée de référence : `<form method="post" action="/reservation"><input name="nom"><button>Envoyer</button></form>`.
- Résultat de référence : le formulaire POST transporte nom=Ada ; le DOM affiche Réservation enregistrée pour Ada ; GET reste réservé à une URL consultable.

## Méthode courte
- séparer structure HTML, style CSS et comportement DOM.
- identifier méthode GET pour lecture et POST pour envoi.
- modifier textContent sans injecter de HTML non contrôlé.

## Exemple minimal corrigé
Entrée : `<form method="post" action="/reservation"><input name="nom"><button>Envoyer</button></form>`.
Sortie attendue : le formulaire POST transporte nom=Ada ; le DOM affiche Réservation enregistrée pour Ada ; GET reste réservé à une URL consultable.

## Point de vigilance
Le résultat doit être calculable à partir de la donnée, sans phrase de validation vague.

## Lien séance
- Séance P08-S1 : découverte et exemple.
- Séance P08-S2 : exercices et correction.
