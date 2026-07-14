---
title: "P08 - corrige - HTML, CSS, DOM, HTTP et formulaires"
level: "premiere"
sequence_id: "P08"
document_type: "corrige"
status: "needs_review"
version: "0.7.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "HTML, CSS, DOM, HTTP et formulaires"
notion: "HTML, CSS, DOM, HTTP et formulaires"
private_data: false
official_program:
  capacities:
    - "P-IHM-01A"
    - "P-IHM-01B"
    - "P-IHM-02"
    - "P-IHM-03A"
    - "P-IHM-03B"
    - "P-IHM-03C"
    - "P-IHM-04A"
    - "P-IHM-04B"
    - "P-IHM-04C"
---

# P08 - Corrigé - HTML, CSS, DOM, HTTP et formulaires

## Corrigé du TD HTML/CSS/DOM

Les huit exercices ci-dessous correspondent exclusivement au TD `P08_TD_html_css_dom.md`.
Ils ne corrigent ni les formulaires HTTP ni les requêtes GET/POST.

### Exercice 1

- Résultat : `main`, `h1`, `p` et `button` sont des balises ; `class="intro"` et `id="inscrire"` sont des attributs ; les intitulés du club et du bouton sont du texte.
- Justification : `h1`, `p` et `button` sont enfants de `main`. L'identifiant `inscrire` désigne le bouton ; la classe `intro` n'est pas un identifiant.

### Exercice 2

- Résultat : les deux paragraphes sont ciblés par `p` et `.important` ; seul le premier est ciblé par `#alerte`, donc il devient rouge et gras.
- Justification : `#alerte` recherche l'attribut `id="alerte"`, alors que `.important` recherche une classe réutilisable.

### Exercice 3

- Résultat : `const etat = document.getElementById("etat");` sélectionne le paragraphe, puis `etat.textContent = "Inscription confirmée";` modifie son contenu.
- Justification : sélectionner le nœud ne change rien à la page ; l'affectation à `textContent` réalise la modification. Si la sélection renvoie `null`, l'identifiant est absent ou mal orthographié.

### Exercice 4

- Résultat : `document.querySelector("#resultats")` sélectionne la section et `document.querySelector(".score")` le premier score. Pour sélectionner l'équipe B, on ajoute `id="equipe-b"` puis on utilise `document.querySelector("#equipe-b")`.
- Justification : `p` et `.score` sont trop larges pour distinguer l'équipe B ; `querySelector` renvoie le premier élément correspondant, pas une collection.

### Exercice 5

- Résultat : au chargement, les constantes sont créées et `addEventListener("click", saluer)` installe l'écouteur. Au clic, le gestionnaire `saluer` est appelé et `message.textContent` devient `"Bonjour !"`.
- Justification : `click` est l'événement, tandis que `saluer` est la fonction qui le traite. Sans clic, le texte reste vide.

### Exercice 6

- Résultat : `document.getElementById("totale")` doit devenir `document.getElementById("total")`. Après le clic, `total.textContent = "1";` affiche `1`.
- Justification : l'identifiant erroné produit `null`. Un script placé avant l'élément peut aussi produire `null` ; il faut alors déplacer le script ou attendre `DOMContentLoaded`.

### Activité 7 — HTML, CSS et JavaScript

- Résultat : ajouter `<h2 id="titre">Ateliers</h2>` relève du HTML, `#titre { color: blue; }` du CSS et l'écouteur qui affecte `message.textContent` du JavaScript.
- Justification : HTML construit les nœuds, CSS règle leur présentation et JavaScript modifie le comportement ou le DOM. Une règle CSS ne crée pas de nœud et ne traite pas le clic.

### Activité 8 — Raisonnements faux

- Résultat : les quatre affirmations sont fausses. Un `id` et une `class` n'ont pas le même rôle ; `document.querySelector("#titre")` renvoie le premier élément correspondant ; un gestionnaire attend l'événement ; `element.textContent = "Bonjour"` modifie le texte, contrairement à un sélecteur CSS.
- Justification : `querySelectorAll(".important")` est l'API adaptée lorsqu'il faut obtenir tous les éléments correspondant à une classe.

## Corrigé du TD HTTP/formulaires

Le corrigé complet et autonome du TD `P08_TD_http_get_post_formulaires.md` est
`P08_corrige_http_get_post_formulaires.md`. Les réponses HTTP ne sont pas
dupliquées dans cette section afin de ne pas les confondre avec le TD HTML/CSS/DOM.

### Exercice 7

- Réponse attendue : erreur 1 — `name` manquant, le champ nom n'est pas transmis ; correction : `<label for=nom>Nom</label><input id=nom name=nom>`. Erreur 2 — `method` absent, GET par défaut ; ajouter `method="post"` si POST souhaité.
- Méthode : identifier chaque erreur HTML et son impact sur la requête.
- Cas limite : champ nom vide après correction, le paramètre est transmis avec une valeur vide.

### Exercice 8

- Réponse attendue : F1 — POST masque de l'URL mais ne chiffre pas, seul HTTPS chiffre ; F2 — HTTPS ne transforme pas GET en POST, il chiffre via TLS ; F3 — un champ sans `name` n'est pas transmis ; F4 — la validation côté serveur est indispensable, le JavaScript peut être contourné.
- Méthode : identifier la confusion précise et reformuler avec le vocabulaire technique.
- Cas limite : paramètre jour absent si le champ n'a pas d'attribut `name`.

## Corrigé du TP

- TP HTML/CSS/DOM : les fonctions `titre_page`, `textes_classe` et `valeur_champ` sont vérifiées par les assets Python P08.
- TP HTTP/formulaires : les capacités client-serveur et de requêtes sont corrigées dans le support HTTP dédié.

## Corrigés des deux évaluations

Les deux sujets ne partagent plus un corrigé générique :

- HTML, CSS et DOM : `P08_corrige_html_css_dom.md` ;
- HTTP, formulaires et confidentialité : `P08_corrige_http_get_post_formulaires.md`.

Cette séparation est disciplinaire : le premier corrigé suit l'arbre HTML, les sélecteurs et les états du gestionnaire d'événement ; le second suit les paramètres HTTP, l'ordre client-serveur, les lieux de stockage et les critères de confidentialité.
