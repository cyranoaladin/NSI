---
title: "T18 - Fiche cours - Boyer-Moore"
level: "terminale"
sequence_id: "T18"
document_type: "fiche_cours"
status: "needs_review"
version: "0.1.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Recherche textuelle"
notion: "Boyer-Moore"
official_program:
  capacities:
    - "T-ALGO-05"
readiness: operational
private_data: false
---
# T18 - Fiche cours - Boyer-Moore

## À savoir
- Boyer-Moore se travaille dans le contexte “recherche textuelle” avec des données vérifiables.
- La fiche distingue vocabulaire, méthode, exemple corrigé et contrôle pour Boyer-Moore.
- Les capacités T-ALGO-05 sont rappelées ici sans être déclarées couvertes.
- L’élève doit pouvoir refaire un exemple de Boyer-Moore avec une valeur, une table ou un code différent.

## Méthodes
1. Capacités explicitement travaillées dans les méthodes et exercices : T-ALGO-05.
2. T-ALGO-05 : comparer un motif depuis sa droite et décaler.
3. Identifier les données d’entrée de Boyer-Moore puis écrire le résultat attendu avant de conclure.
4. Contrôler Boyer-Moore par un cas limite explicite et une vérification courte.
5. Relier la réponse à un support de séance T18 sans confondre fiche de révision et preuve de couverture.

## Exemples corrigés
### Exemple corrigé 1 - Exemple principal
Dans `BANANA`, la dernière occurrence de A est à l’indice 5.
### Exemple corrigé 2 - Contrôle ou contre-exemple
Si le mauvais caractère est absent du motif, le motif peut être décalé au-delà de ce caractère.

## Erreurs fréquentes
- Confondre le vocabulaire de Boyer-Moore avec une simple récitation : corriger par un exemple calculé ou exécuté.
- Oublier une hypothèse de recherche textuelle : corriger en l’écrivant avant la méthode.
- Conclure sans contrôle sur Boyer-Moore : corriger par un cas limite ou une vérification inverse.

## Cas limites
- Cas de départ vide ou nul pour Boyer-Moore, à traiter selon la convention du chapitre T18.
- Donnée invalide dans recherche textuelle, par exemple symbole interdit, clé absente ou requête trop large selon la fiche.
- Cas frontière de Boyer-Moore où une seule valeur change la méthode ou le résultat attendu.

## Mini-exercices
### Mini-exercice 1
T-ALGO-05 : appliquer la méthode de Boyer-Moore à un exemple court choisi dans le chapitre T18.
### Mini-exercice 2
Repérer l’erreur dans une réponse qui oublie une hypothèse de recherche textuelle.
### Mini-exercice 3
Proposer un cas limite pertinent pour Boyer-Moore et expliquer le résultat attendu.
### Mini-exercice 4
Écrire une phrase de contrôle qui vérifie la conclusion obtenue pour Boyer-Moore.

## Réponses rapides
1. La méthode attendue pour Boyer-Moore commence par les données puis applique l’opération du chapitre T18.
2. L’erreur vient de l’hypothèse manquante ; elle se corrige en testant le cas mentionné dans recherche textuelle.
3. Le cas limite doit donner un résultat explicite, par exemple 0, vide, absent ou hors plage selon Boyer-Moore.
4. Le contrôle compare le résultat avec la définition ou avec une opération inverse de Boyer-Moore.

## À retenir
- T18 : Boyer-Moore se révise avec une définition, une méthode et un exemple corrigé.
- Les capacités T-ALGO-05 restent en travail tant que TD, TP, évaluation, barème et revues humaines manquent.
- Un exemple de Boyer-Moore doit changer autre chose qu’une simple valeur pour tester la compréhension.
- Pour T18, le tableau de liens distingue les supports existants et les supports inscrits au registre.
- La fiche T18 sur Boyer-Moore reste needs_review et ne déclenche ni publication ni couverture.

## Lien avec la progression

| Élément | Fichier | Statut | Remarque |
|---|---|---|---|
| Séance | T18-S1 | réelle | séance présente dans la progression |
| TD | T18_TD_boyer_moore.md | existant | support TD créé en needs_review |
| Évaluation | T18_evaluation_boyer_moore.md | existant | support d’évaluation créé en needs_review |

## Auto-évaluation
- Je peux expliquer Boyer-Moore avec un exemple différent de ceux de la fiche T18.
- Je peux citer au moins une capacité parmi T-ALGO-05 et dire où elle est travaillée dans la fiche.
- Je peux dire quel support lié à T18 existe déjà ou reste inscrit au registre.
- Je peux identifier un cas limite de Boyer-Moore sans transformer la fiche en corrigé complet.
