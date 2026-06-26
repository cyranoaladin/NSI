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
## Déroulé opérationnel détaillé
1. créer une page `index.html` avec titre, liste et bouton.
2. lier `style.css` sans style inline.
3. lier `main.js` en fin de page.
4. sélectionner la liste par `querySelector`.
5. ajouter un élément `li` au clic sur le bouton.
6. afficher un compteur DOM cohérent après chaque ajout.

## Tests vérifiables attendus
- Test 1 : le document contient un seul `h1` avec texte non vide.
- Test 2 : le bouton a un identifiant stable `ajouter`.
- Test 3 : la liste initiale contient deux éléments.
- Test 4 : un clic ajoute exactement un élément.
- Test 5 : trois clics donnent cinq éléments au total.
- Test 6 : aucun document professeur n’est requis pour lancer la page.

## Cas limites à documenter
- Cas limite : liste vide.
- Cas limite : texte d’élément vide.
- Cas limite : sélecteur introuvable.
- Cas limite : double clic rapide.
- Cas limite : CSS non chargé.
- Cas limite : JavaScript désactivé.

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
- Livrable : dossier avec `index.html`, `style.css`, `main.js` et capture console sans erreur..
- Le professeur peut vérifier le livrable sans accès au Drive distant.
- Toute source locale éventuellement utilisée doit être tracée dans `support_source_trace.yml`.
