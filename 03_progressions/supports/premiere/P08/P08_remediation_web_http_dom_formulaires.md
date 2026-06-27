---
title: "P08 - Remédiation - HTML, CSS, DOM, HTTP GET/POST"
level: "premiere"
sequence_id: "P08"
document_type: "remediation"
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

# P08 - Remédiation - HTML, CSS, DOM, HTTP GET/POST

## Erreur fréquente 1
Oublier la donnée stable. Activité corrective : surligner dans `<form method="post" action="/reservation"><input name="nom"><button>Envoyer</button></form>` les valeurs qui pilotent la méthode.

## Erreur fréquente 2
Appliquer une étape dans le mauvais ordre. Activité corrective : remettre ces étapes dans l’ordre : séparer structure HTML, style CSS et comportement DOM, identifier méthode GET pour lecture et POST pour envoi, modifier textContent sans injecter de HTML non contrôlé.

## Erreur fréquente 3
Donner une conclusion non vérifiable. Activité corrective : retrouver le résultat `le formulaire POST transporte nom=Ada ; le DOM affiche Réservation enregistrée pour Ada ; GET reste réservé à une URL consultable` à partir de la donnée.

## Différenciation
- Socle : refaire l’exemple de référence.
- Standard : traiter une valeur modifiée.
- Approfondissement : créer un cas limite et le corriger.
