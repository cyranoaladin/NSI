---
title: "P08 - TP - HTML, CSS et DOM"
level: "premiere"
sequence_id: "P08"
document_type: "tp"
status: "needs_review"
version: "0.2.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Interactions sur le Web"
notion: "HTML, CSS, DOM et événement"
objectifs:
  - "identifier balise, attribut id et classe CSS"
  - "sélectionner un élément du DOM"
  - "associer un événement clic"
  - "contrôler que seul t2 change de classe"
private_data: false
official_program:
  capacities:
    - "P-IHM-01A"
    - "P-IHM-01B"
    - "P-IHM-02"
    - "P-IHM-03A"
---

# P08 - TP - HTML, CSS et DOM

## Objectif technique
Une page locale affiche une liste de tâches ; un bouton doit ajouter la classe CSS termine à l’élément choisi sans modifier le texte des autres éléments.

## Consigne technique détaillée
- identifier balise, attribut id et classe CSS.
- sélectionner un élément du DOM.
- associer un événement clic.
- contrôler que seul t2 change de classe.

## Starter code
```python
def verifier_html_css_dom(donnee):
    """À compléter : renvoyer une structure vérifiable, pas un texte hardcodé."""
    raise NotImplementedError("à compléter par l’élève")
```

## Tests attendus
- Test nominal : donnée de référence acceptée et résultat exact.
- Test limite : donnée vide ou minimale traitée selon la convention.
- Test invalide : donnée incohérente refusée avec exception ou message explicite.

## Exemple d’exécution
- Entrée : `<ul><li id="t1">Réviser</li><li id="t2">Tester</li></ul>`.
- Sortie attendue : structure contrôlable par assertions, pas phrase libre.

## Livrable vérifiable
- Un fichier `P08_solution_html_css_dom.py` avec au moins trois tests personnels.
- Une capture texte des tests exécutés.

## Cas limite
- Cas à discuter : modifier tous les li avec un sélecteur trop large.

## Corrigé professeur séparé
- Le corrigé professeur doit être conservé séparément et ne pas être cité comme document élève.

## Critères de réussite
- Le code ne retourne pas une constante unique.
- Les tests distinguent cas nominal, cas limite et entrée invalide.
- La justification relie le résultat à une capacité officielle.
