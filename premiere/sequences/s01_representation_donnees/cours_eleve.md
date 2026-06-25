---
title: "S01 - Représenter des données : bits, textes et types construits"
level: "premiere"
sequence_id: "s01_representation_donnees"
document_type: "cours"
status: "needs_review"
version: "0.2.0"
authors: ["NSI"]
source: "BO spécial n°1 du 22 janvier 2019"
theme: "Représentation des données"
notion: "bits, bases, complément à deux, booléens, texte, listes, tuples, dictionnaires"
duration: "5 séances"
difficulty: "standard"
private_data: false
official_program:
  level: "premiere"
  rubrique: "Représentation des données : types et valeurs de base ; types construits"
  content: "Bases 2/10/16, entiers relatifs, booléens, texte, p-uplets, tableaux, dictionnaires"
  capacities:
    - id: "P-DATA-BASE-01"
      label: "Passer de la représentation d'une base dans une autre."
      evidence:
        - section: "Bases 2, 10 et 16"
          file: "premiere/sequences/s01_representation_donnees/cours_eleve.md"
          anchor: "#bases-2-10-et-16"
          type: "cours"
    - id: "P-DATA-BASE-02"
      label: "Evaluer un codage binaire d'entier relatif et utiliser le complément à deux."
      evidence:
        - section: "Entiers relatifs et complément à deux"
          file: "premiere/sequences/s01_representation_donnees/cours_eleve.md"
          anchor: "#entiers-relatifs-et-complément-à-deux"
          type: "cours"
    - id: "P-DATA-BASE-04"
      label: "Dresser la table d'une expression booléenne."
      evidence:
        - section: "Booléens et tables de vérité"
          file: "premiere/sequences/s01_representation_donnees/cours_eleve.md"
          anchor: "#booléens-et-tables-de-vérité"
          type: "cours"
    - id: "P-DATA-BASE-05"
      label: "Identifier l'intérêt des systèmes d'encodage de texte."
      evidence:
        - section: "Texte, ASCII et Unicode"
          file: "premiere/sequences/s01_representation_donnees/cours_eleve.md"
          anchor: "#texte-ascii-et-unicode"
          type: "cours"
    - id: "P-DATA-CONSTR-01"
      label: "Ecrire une fonction renvoyant un p-uplet de valeurs."
      evidence:
        - section: "Tuples et p-uplets"
          file: "premiere/sequences/s01_representation_donnees/cours_eleve.md"
          anchor: "#tuples-et-p-uplets"
          type: "cours"
    - id: "P-DATA-CONSTR-02"
      label: "Lire, modifier, construire et itérer sur des tableaux."
      evidence:
        - section: "Listes et tableaux Python"
          file: "premiere/sequences/s01_representation_donnees/cours_eleve.md"
          anchor: "#listes-et-tableaux-python"
          type: "cours"
    - id: "P-DATA-CONSTR-03"
      label: "Construire et parcourir un dictionnaire."
      evidence:
        - section: "Dictionnaires"
          file: "premiere/sequences/s01_representation_donnees/cours_eleve.md"
          anchor: "#dictionnaires"
          type: "cours"
    - id: "P-LANG-04"
      label: "Utiliser des jeux de tests."
      evidence:
        - section: "Tests et cas limites"
          file: "premiere/sequences/s01_representation_donnees/cours_eleve.md"
          anchor: "#tests-et-cas-limites"
          type: "cours"
prerequisites:
  - "Utiliser Python pour affecter une variable et appeler une fonction."
  - "Lire une expression arithmétique simple."
learning_objectives:
  - "Comprendre pourquoi toute donnée manipulée par une machine est codée."
  - "Passer entre bases 2, 10 et 16 pour des entiers positifs."
  - "Interpréter un entier relatif codé en complément à deux."
  - "Choisir entre liste, tuple et dictionnaire selon le problème."
assessment:
  formative: true
  summative: false
last_review:
  pedagogy: ""
  science: ""
  technical: ""
---

# S01 - Représenter des données : bits, textes et types construits

## Situation-problème

Un même badge de cantine peut contenir un identifiant, un solde, un droit d'accès et un nom court.
La machine ne conserve pas ces informations comme un humain les lit.
Elle manipule des suites de bits.
Elle doit donc choisir un codage pour chaque donnée.
Un identifiant peut être un entier positif.
Un solde peut être positif ou négatif.
Un droit d'accès peut être vrai ou faux.
Un nom court peut être un texte Unicode.
Un historique d'achats peut être une liste.
Une fiche compacte peut être un tuple.
Un accès par identifiant peut être un dictionnaire.
La question de la séquence est donc la suivante.
Comment choisir une représentation qui permet de stocker, traiter et tester correctement une donnée ?

## Objectifs

- Savoir définir un bit et expliquer son rôle.
- Convertir un entier positif entre bases 2, 10 et 16.
- Repérer l'intervalle représentable sur un nombre de bits donné.
- Encoder et décoder de petits entiers relatifs en complément à deux.
- Construire une table de vérité pour une expression booléenne.
- Expliquer la différence entre caractère, point de code et encodage.
- Choisir entre liste, tuple et dictionnaire.
- Justifier un choix de représentation par les opérations attendues.
- Vérifier une fonction avec des tests simples.

## Prérequis

- Savoir additionner et diviser des entiers.
- Savoir lire une écriture décimale positionnelle.
- Savoir exécuter une fonction Python simple.
- Savoir distinguer une valeur, une variable et une expression.
- Savoir lire une condition `if`.
- Savoir utiliser une liste Python en lecture.

## Limites de la séquence

Cette séquence pilote regroupe deux blocs liés du programme de Première.
Elle traite les types et valeurs de base.
Elle introduit aussi les types construits utilisés en Python.
Elle ne traite pas encore sérieusement l'import CSV, le tri de table ou la fusion de tables.
Ces points restent à placer dans une autre séquence.
Les nombres flottants sont seulement signalés comme angle mort de cette séquence.
L'objectif ici est de consolider les représentations indispensables avant les traitements de table.

## Activité d'introduction

On veut coder quatre informations du badge `B-17`.
Information 1 : identifiant numérique `17`.
Information 2 : variation du solde `-3`.
Information 3 : accès autorisé `oui`.
Information 4 : initiale affichée `É`.
Question 1 : lesquelles peuvent se coder directement par un entier positif ?
Question 2 : lesquelles nécessitent une convention supplémentaire ?
Question 3 : que se passe-t-il si on lit `11111101` comme un entier positif ?
Question 4 : que se passe-t-il si on lit `11111101` comme un entier relatif sur 8 bits ?
Question 5 : pourquoi le caractère `É` peut poser un problème dans certains anciens encodages ?
Conclusion attendue : une suite de bits ne suffit pas, il faut aussi connaître la convention de représentation.

## Formalisation

Une donnée informatique n'est pas seulement une valeur visible.
Une donnée informatique est une valeur associée à une représentation.
La même suite de bits peut représenter plusieurs choses selon la convention.
La convention indique comment lire, écrire et transformer la donnée.
Choisir une représentation revient à répondre à trois questions.
Question A : quelles valeurs doit-on pouvoir représenter ?
Question B : quelles opérations doit-on effectuer souvent ?
Question C : quelles erreurs faut-il éviter ?
Un bon choix de représentation simplifie les traitements.
Un mauvais choix impose des conversions inutiles ou crée des erreurs silencieuses.

## Définitions

Définition 1 : un bit est une unité d'information qui prend l'une des deux valeurs `0` ou `1`.
Définition 2 : une base de numération est un système positionnel qui utilise un nombre fixé de chiffres.
Définition 3 : le complément à deux est une convention de codage des entiers relatifs sur un nombre fixe de bits.
Définition 4 : un booléen est une valeur logique qui vaut `True` ou `False`.
Définition 5 : une table de vérité énumère toutes les valeurs possibles des variables booléennes d'une expression.
Définition 6 : un encodage de texte associe des caractères à des suites d'octets.
Définition 7 : une liste Python est une collection ordonnée et modifiable.
Définition 8 : un tuple Python est une collection ordonnée généralement utilisée comme p-uplet non modifié.
Définition 9 : un dictionnaire Python associe des clés à des valeurs.

## Bases 2, 10 et 16

En base 10, les chiffres disponibles sont `0` à `9`.
En base 2, les chiffres disponibles sont `0` et `1`.
En base 16, les chiffres disponibles sont `0` à `9`, puis `A` à `F`.
Dans une écriture positionnelle, la position donne le poids.
`1011₂` signifie `1*2^3 + 0*2^2 + 1*2^1 + 1*2^0`.
Donc `1011₂ = 8 + 0 + 2 + 1 = 11₁₀`.
`2A₁₆` signifie `2*16^1 + 10*16^0`.
Donc `2A₁₆ = 32 + 10 = 42₁₀`.
La base 16 est utile car un chiffre hexadécimal correspond à 4 bits.
`1111₂ = F₁₆`.
`1010₂ = A₁₆`.
Un octet contient 8 bits.
Un octet se lit donc souvent avec 2 chiffres hexadécimaux.
`11111111₂ = FF₁₆ = 255₁₀`.

### Exemple corrigé 1

Convertir `45₁₀` en base 2.
On divise successivement par 2.
`45 = 2*22 + 1`.
`22 = 2*11 + 0`.
`11 = 2*5 + 1`.
`5 = 2*2 + 1`.
`2 = 2*1 + 0`.
`1 = 2*0 + 1`.
On lit les restes de bas en haut.
Résultat : `45₁₀ = 101101₂`.
Vérification : `32 + 8 + 4 + 1 = 45`.

### Contre-exemple 1

Dire que `101` vaut toujours cent-un est faux.
En base 10, `101` vaut cent-un.
En base 2, `101₂` vaut cinq.
En base 16, `101₁₆` vaut deux-cent-cinquante-sept.
Il faut toujours préciser la base quand il y a ambiguïté.

### Exercice intégré 1

Convertir `31₁₀` en base 2.
Convertir `11110₂` en base 10.
Convertir `2F₁₆` en base 10.
Comparer `1111₂` et `F₁₆`.

## Entiers positifs

Un entier positif sur `n` bits peut représenter les valeurs de `0` à `2^n - 1`.
Sur 4 bits, l'intervalle est `0` à `15`.
Sur 8 bits, l'intervalle est `0` à `255`.
Sur 16 bits, l'intervalle est `0` à `65535`.
Le nombre de bits impose une limite.
Si un compteur sur 8 bits dépasse 255, la représentation n'est plus suffisante.
Python masque en partie cette limite pour ses entiers, car il utilise une taille variable.
Mais les fichiers, réseaux, images et machines utilisent souvent des tailles fixées.

### Exemple corrigé 2

Combien de bits faut-il pour écrire `100₁₀` en binaire ?
On cherche la puissance de 2 qui dépasse 100.
`2^6 = 64`.
`2^7 = 128`.
Il faut donc 7 bits pour représenter 100 sans signe.
En effet `100₁₀ = 1100100₂`.

### Erreur fréquente 1

Confondre nombre de chiffres décimaux et nombre de bits.
`100` a trois chiffres décimaux.
Mais sa représentation binaire utilise sept bits.
Le nombre de symboles dépend de la base.

## Entiers relatifs et complément à deux

Pour représenter des entiers négatifs, il faut une convention.
La convention étudiée ici est le complément à deux.
Sur `n` bits, elle permet de représenter de `-2^(n-1)` à `2^(n-1)-1`.
Sur 8 bits, l'intervalle est `-128` à `127`.
Le bit de gauche est appelé bit de poids fort.
Dans cette convention, si le bit de poids fort vaut `0`, le nombre est positif ou nul.
Si le bit de poids fort vaut `1`, le nombre est négatif.
Pour coder `-x` sur `n` bits, on peut calculer `2^n - x`.
Pour décoder une valeur binaire dont le bit de gauche vaut `1`, on soustrait `2^n`.

### Exemple corrigé 3

Coder `-5` en complément à deux sur 8 bits.
On calcule `2^8 - 5 = 256 - 5 = 251`.
On écrit `251` en binaire sur 8 bits.
`251₁₀ = 11111011₂`.
Donc `-5` se code `11111011` sur 8 bits.
Décodage inverse : `11111011₂ = 251`.
Comme le bit de gauche vaut `1`, on lit `251 - 256 = -5`.

### Contre-exemple 2

Lire `11111011` comme entier positif donne `251`.
Lire `11111011` comme complément à deux sur 8 bits donne `-5`.
La suite de bits n'a donc pas un sens unique.
La convention est indispensable.

### Exercice intégré 2

Sur 8 bits, coder `7`, `-1`, `-8`.
Sur 8 bits, décoder `00001111`, `11111111`, `11111000`.
Donner l'intervalle représentable sur 4 bits.
Expliquer pourquoi `140` ne se code pas comme entier relatif sur 8 bits.

## Booléens et tables de vérité

Un booléen vaut seulement `True` ou `False`.
En Python, les opérateurs principaux sont `and`, `or`, `not`.
Une expression booléenne combine des booléens.
Une table de vérité liste tous les cas possibles.
Avec une variable booléenne, il y a 2 lignes.
Avec deux variables booléennes, il y a 4 lignes.
Avec trois variables booléennes, il y a 8 lignes.
L'opérateur `and` vaut vrai seulement si les deux entrées sont vraies.
L'opérateur `or` vaut vrai si au moins une entrée est vraie.
L'opérateur `not` inverse la valeur.
L'opérateur xor vaut vrai si une seule des deux entrées est vraie.

### Exemple corrigé 4

Expression : `a and not b`.
Cas 1 : `a=False`, `b=False`, alors `not b=True`, résultat `False`.
Cas 2 : `a=False`, `b=True`, alors `not b=False`, résultat `False`.
Cas 3 : `a=True`, `b=False`, alors `not b=True`, résultat `True`.
Cas 4 : `a=True`, `b=True`, alors `not b=False`, résultat `False`.
La table de vérité permet de ne pas raisonner au hasard.

### Erreur fréquente 2

Croire que `or` signifie toujours "l'un ou l'autre mais pas les deux".
En Python, `or` est inclusif.
`True or True` vaut `True`.
Le "ou exclusif" doit être formulé autrement.

### Exercice intégré 3

Dresser la table de vérité de `not a or b`.
Dresser la table de vérité de `(a and b) or (a and not b)`.
Simplifier l'expression précédente si possible.

## Texte, ASCII et Unicode

Un texte informatique est une suite de caractères.
Un caractère n'est pas directement un octet.
Il faut un système d'encodage.
ASCII est un ancien encodage limité à 128 codes principaux.
ASCII code correctement les lettres anglaises non accentuées.
ASCII ne suffit pas pour représenter tous les caractères utilisés dans le monde.
Unicode attribue un point de code à un très grand nombre de caractères.
UTF-8 est un encodage courant d'Unicode en octets.
La lettre `A` a le point de code 65.
La lettre `é` a le point de code 233.
Certains caractères prennent plusieurs octets en UTF-8.
Un fichier texte mal interprété peut afficher des caractères incorrects.
Le problème ne vient pas du texte visible mais de l'encodage utilisé pour lire les octets.

### Exemple corrigé 5

En Python, `ord("A")` retourne `65`.
En Python, `chr(65)` retourne `"A"`.
`"A".encode("utf-8")` donne un octet.
`"é".encode("utf-8")` donne deux octets.
Donc le nombre de caractères n'est pas toujours le nombre d'octets.
Cette différence compte dans les fichiers et les réseaux.

### Contre-exemple 3

Dire qu'un caractère vaut toujours un octet est faux.
Cette affirmation peut être vraie dans des cas ASCII simples.
Elle échoue pour de nombreux caractères Unicode.
Elle échoue aussi quand l'encodage du fichier est mal choisi.

## Listes et tableaux Python

Une liste Python représente une collection ordonnée.
Les éléments sont repérés par des index.
Le premier index est `0`.
Une liste peut être modifiée.
`notes[0]` lit le premier élément.
`notes[1] = 14` modifie le deuxième élément.
Une liste est utile quand l'ordre compte.
Une liste est utile quand on parcourt tous les éléments.
Une liste est utile quand on ajoute ou modifie des valeurs.
Une compréhension de liste construit une liste à partir d'une règle.
Exemple : `[x*x for x in range(5)]` construit `[0, 1, 4, 9, 16]`.
Une matrice peut être représentée par une liste de listes.
Exemple : `m[1][2]` lit ligne 1, colonne 2.

### Exemple corrigé 6

On dispose de `valeurs = [4, 7, 9]`.
Le nombre `4` est à l'index `0`.
Le nombre `7` est à l'index `1`.
Le nombre `9` est à l'index `2`.
La somme se calcule par parcours.
Code possible : `total = sum(valeurs)`.
Compréhension possible : `[v + 1 for v in valeurs]`.
Résultat : `[5, 8, 10]`.

### Erreur fréquente 3

Commencer les index à `1` en Python.
Dans une liste de longueur 3, les index valides sont `0`, `1`, `2`.
L'index `3` provoque une erreur.
Cette erreur est un cas limite classique à tester.

## Tuples et p-uplets

Un tuple Python est une collection ordonnée.
On l'utilise souvent pour regrouper un petit nombre de valeurs liées.
Un point du plan peut être représenté par `(x, y)`.
Une couleur RGB peut être représentée par `(rouge, vert, bleu)`.
Un tuple sert bien quand le nombre de champs est fixe.
Un tuple sert bien quand l'ordre des champs est connu.
Un tuple est moins lisible si les champs sont nombreux ou ambigus.

### Exemple corrigé 7

Fonction attendue : renvoyer les coordonnées du milieu de deux points.
Un point est représenté par un tuple `(x, y)`.
La fonction peut renvoyer un tuple.
Code : `return ((x1 + x2) / 2, (y1 + y2) / 2)`.
Le résultat contient deux valeurs liées.
Le tuple évite de créer deux variables séparées à retourner.

### Contre-exemple 4

Représenter une fiche élève longue par un tuple comme `(id, nom, groupe, option, date, mail)` est fragile.
Le lecteur doit mémoriser la position de chaque champ.
Un dictionnaire est plus lisible si l'accès par nom de champ est important.

## Dictionnaires

Un dictionnaire associe des clés à des valeurs.
Chaque clé permet d'accéder directement à une valeur.
Exemple : `stock["stylo"] = 18`.
La clé `"stylo"` est associée à la valeur `18`.
Un dictionnaire est utile quand l'accès par nom ou identifiant est fréquent.
Un dictionnaire est utile pour compter des occurrences.
Un dictionnaire est utile pour représenter un enregistrement avec champs nommés.
Les méthodes `keys`, `values` et `items` aident à parcourir.
`keys()` donne les clés.
`values()` donne les valeurs.
`items()` donne les couples clé-valeur.

### Exemple corrigé 8

On veut compter des votes : `["A", "B", "A", "C", "A"]`.
On crée un dictionnaire vide.
Pour chaque vote, on augmente le compteur de la clé correspondante.
Après parcours, on obtient `{"A": 3, "B": 1, "C": 1}`.
La clé est le choix.
La valeur est l'effectif.
La représentation est adaptée car on accède souvent par choix.

### Contre-exemple 5

Utiliser une liste de couples pour chercher souvent par identifiant peut être inefficace.
Avec `[("A", 3), ("B", 1), ("C", 1)]`, trouver `"C"` impose un parcours.
Avec `{"A": 3, "B": 1, "C": 1}`, l'accès par clé est direct dans l'usage courant.
Le choix dépend donc des opérations attendues.

## Choisir une représentation

Si l'ordre est important et les éléments sont modifiables, une liste convient souvent.
Si les valeurs forment un petit groupe fixe, un tuple convient souvent.
Si l'accès se fait par clé, un dictionnaire convient souvent.
Si la valeur doit être stockée en peu de mémoire, le nombre de bits compte.
Si la valeur peut être négative, la convention de signe compte.
Si la valeur est un texte, l'encodage compte.
Si la valeur est logique, une table de vérité clarifie les cas.
Le choix doit toujours être justifié par un traitement.

## Tests et cas limites

Un test vérifie un comportement attendu sur un exemple choisi.
Un cas limite est une valeur qui risque de révéler une erreur.
Pour les bases, tester `0` est indispensable.
Pour les bases, tester la plus grande base autorisée évite un oubli.
Pour le complément à deux, tester `-1` est indispensable.
Pour le complément à deux, tester les bornes de l'intervalle est indispensable.
Pour le texte, tester un caractère accentué est utile.
Pour les listes, tester une liste vide est utile.
Pour les dictionnaires, tester une clé absente est utile.
Un jeu de tests ne prouve pas tout.
Mais un bon jeu de tests réduit les erreurs évidentes.
Le fichier Python associé à ce cours est `python/representation_tools.py`.
Les tests associés sont dans `tests/test_representation_tools.py`.

## Aides progressives

Aide niveau 1 : écrire d'abord la valeur en base 10 avant toute conversion.
Aide niveau 2 : poser les puissances de la base sous chaque chiffre.
Aide niveau 3 : vérifier le résultat en effectuant la conversion inverse.
Aide niveau 1 : pour le complément à deux, noter le nombre de bits.
Aide niveau 2 : calculer l'intervalle représentable.
Aide niveau 3 : si le bit de gauche vaut `1`, soustraire `2^n`.
Aide niveau 1 : pour choisir une structure Python, identifier l'opération principale.
Aide niveau 2 : si l'opération principale est "accéder par clé", essayer un dictionnaire.
Aide niveau 3 : si l'opération principale est "parcourir dans l'ordre", essayer une liste ou un tuple.

## Différenciation

Parcours socle : convertir bases 2, 10, 16 sur de petits entiers.
Parcours socle : lire une table de vérité déjà préparée.
Parcours socle : distinguer liste, tuple et dictionnaire sur des exemples.
Parcours standard : construire les conversions et justifier les choix.
Parcours standard : coder et décoder de petits relatifs sur 8 bits.
Parcours standard : écrire une fonction Python testée.
Parcours expert : discuter le coût d'une recherche dans une liste ou un dictionnaire.
Parcours expert : comparer nombre de caractères et nombre d'octets en UTF-8.
Parcours expert : produire des tests de bornes pour le complément à deux.

## Erreurs fréquentes

Erreur fréquente 1 : oublier de préciser la base d'une écriture.
Erreur fréquente 2 : lire un complément à deux comme un entier positif.
Erreur fréquente 3 : confondre caractère et octet.
Erreur fréquente 4 : utiliser une liste quand une clé de dictionnaire est nécessaire.
Erreur fréquente 5 : oublier que les index Python commencent à zéro.
Erreur fréquente 6 : croire qu'un test réussi prouve toutes les situations.

## À retenir

Une suite de bits n'a de sens que par une convention.
Les bases 2, 10 et 16 sont des écritures différentes d'une même valeur.
Le complément à deux code des entiers relatifs sur un nombre fixé de bits.
Une table de vérité rend explicite une expression booléenne.
Unicode sert à représenter des textes variés.
Une liste est ordonnée et modifiable.
Un tuple regroupe des valeurs liées.
Un dictionnaire associe une clé à une valeur.
Le choix d'une représentation dépend des traitements attendus.
Les tests doivent couvrir des cas ordinaires et des cas limites.

## Auto-évaluation

- Je sais convertir `37₁₀` en base 2.
- Je sais convertir `2A₁₆` en base 10.
- Je sais donner l'intervalle des entiers relatifs sur 8 bits.
- Je sais décoder `11111110` en complément à deux sur 8 bits.
- Je sais dresser une table de vérité à deux variables.
- Je sais expliquer pourquoi `é` n'est pas un caractère ASCII simple.
- Je sais choisir entre liste, tuple et dictionnaire.
- Je sais proposer au moins deux cas limites pour tester une fonction.

## Extension

Approfondissement 1 : mesurer avec Python la taille en octets de plusieurs chaînes Unicode.
Approfondissement 2 : écrire une fonction qui vérifie si une chaîne est une écriture binaire.
Approfondissement 3 : écrire une fonction qui calcule l'intervalle représentable en complément à deux.
Approfondissement 4 : comparer deux représentations d'un carnet de contacts, liste de tuples ou dictionnaire.
Approfondissement 5 : expliquer pourquoi les nombres flottants devront être étudiés séparément.

## Exemples corrigés

Cette section récapitule les exemples corrigés de la séquence.

Exemple corrigé récapitulatif 1 : convertir `1101_2` donne `13_10` car `8 + 4 + 1 = 13`.

Exemple corrigé récapitulatif 2 : `0x2A` donne `42_10` car `2 x 16 + 10 = 42`.

Exemple corrigé récapitulatif 3 : sur 8 bits, `11111111` vaut `-1` en complément à deux.

Exemple corrigé récapitulatif 4 : `A` a pour code Unicode `U+0041`.

Exemple corrigé récapitulatif 5 : un dictionnaire convient pour retrouver une valeur par clé stable.

## Exercices intégrés

Cette section rassemble les exercices intégrés à refaire après le cours.

Exercice intégré récapitulatif 1 : convertir `101101_2` en base 10 puis en base 16.

Exercice intégré récapitulatif 2 : coder `-12` en complément à deux sur 8 bits.

Exercice intégré récapitulatif 3 : choisir entre liste, tuple et dictionnaire pour stocker des mesures horodatées.
