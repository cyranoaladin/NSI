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
## Déroulé opérationnel détaillé
1. créer un formulaire GET avec champ `q`.
2. observer l’URL produite après soumission GET.
3. créer un formulaire POST fictif vers `/contact`.
4. distinguer paramètres visibles et corps de requête.
5. encoder correctement espace et accent dans une valeur.
6. rédiger une trace comparant GET et POST.

## Tests vérifiables attendus
- Test 1 : GET `/recherche?q=nsi` affiche le paramètre dans l’URL.
- Test 2 : GET avec `q=site web` encode l’espace en `+` ou `%20`.
- Test 3 : POST ne met pas le message complet dans l’URL.
- Test 4 : un champ obligatoire vide bloque la soumission côté navigateur.
- Test 5 : la méthode est lisible dans le HTML.
- Test 6 : la trace cite au moins deux en-têtes ou champs utiles.

## Cas limites à documenter
- Cas limite : champ vide.
- Cas limite : caractère accentué.
- Cas limite : mot avec espace.
- Cas limite : message long.
- Cas limite : donnée sensible.
- Cas limite : rafraîchissement de page.

## Plan de correction professeur
- Vérifier que le programme se lance dans un répertoire temporaire propre.
- Lire les fonctions avant les tests pour repérer un retour constant ou hardcodé.
- Exécuter les tests nominaux puis les tests limites.
- Ajouter un test invalide avant toute correction manuelle.
- Comparer la sortie obtenue avec le résultat attendu écrit dans ce TP.
- Refuser une solution qui supprime le cas limite au lieu de le traiter.
- Noter séparément exactitude, robustesse, lisibilité et justification.

## Grille de vérification élève
- [ ] le fichier demandé existe avec le bon nom.
- [ ] le starter n’a pas été remplacé par une constante.
- [ ] chaque fonction possède une docstring ou un commentaire de contrat.
- [ ] les tests nominaux passent.
- [ ] les tests limites passent.
- [ ] les entrées invalides sont refusées explicitement.
- [ ] le livrable ne dépend pas d’un chemin absolu local.
- [ ] la réponse cite la capacité travaillée.

## Différenciation opérationnelle
- Socle : compléter les fonctions dans l’ordre des tests fournis.
- Standard : ajouter deux tests personnels avant de demander la validation.
- Approfondissement : proposer une variante de donnée et expliquer pourquoi les tests restent pertinents.
- Aide autorisée : rappel de syntaxe, sans fournir le corps complet de la fonction.
- Aide interdite : donner directement le résultat attendu comme unique retour de fonction.

## Livrable final contrôlable
- Livrable : `formulaires.html` avec deux formulaires et un tableau comparatif GET/POST..
- Le professeur peut vérifier le livrable sans accès au Drive distant.
- Toute source locale éventuellement utilisée doit être tracée dans `support_source_trace.yml`.
