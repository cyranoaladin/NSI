---
title: "P08 - TP - HTTP, GET, POST et formulaires"
level: "premiere"
sequence_id: "P08"
document_type: "tp"
status: "needs_review"
version: "0.2.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Interactions sur le Web"
notion: "requêtes HTTP et formulaires"
objectifs:
  - "repérer méthode, URL, paramètres et corps"
  - "justifier GET pour une recherche partageable"
  - "justifier POST pour une donnée sensible"
  - "identifier le risque de mot de passe dans l’URL"
private_data: false
official_program:
  capacities:
    - "P-IHM-03A"
    - "P-IHM-03B"
    - "P-IHM-03C"
    - "P-IHM-04A"
    - "P-IHM-04B"
    - "P-IHM-04C"
---

# P08 - TP - HTTP, GET, POST et formulaires

## Objectif technique
Un formulaire de recherche envoie un mot-clé public en GET, tandis qu’un formulaire de connexion doit envoyer les identifiants en POST.

## Consigne technique détaillée
- repérer méthode, URL, paramètres et corps.
- justifier GET pour une recherche partageable.
- justifier POST pour une donnée sensible.
- identifier le risque de mot de passe dans l’URL.

## Starter code
```python
def verifier_http_get_post_formulaires(donnee):
    """À compléter : renvoyer une structure vérifiable, pas un texte hardcodé."""
    raise NotImplementedError("à compléter par l’élève")
```

## Tests attendus
- Test nominal : donnée de référence acceptée et résultat exact.
- Test limite : donnée vide ou minimale traitée selon la convention.
- Test invalide : donnée incohérente refusée avec exception ou message explicite.

## Exemple d’exécution
- Entrée : `GET /search?q=nsi puis POST /login avec champs utilisateur et mot_de_passe`.
- Sortie attendue : structure contrôlable par assertions, pas phrase libre.

## Livrable vérifiable
- Un fichier `P08_solution_http_get_post_formulaires.py` avec au moins trois tests personnels.
- Une capture texte des tests exécutés.

## Cas limite
- Cas à discuter : confondre code de statut et méthode HTTP.

## Corrigé professeur séparé
- Le corrigé professeur doit être conservé séparément et ne pas être cité comme document élève.

## Critères de réussite
- Le code ne retourne pas une constante unique.
- Les tests distinguent cas nominal, cas limite et entrée invalide.
- La justification relie le résultat à une capacité officielle.
