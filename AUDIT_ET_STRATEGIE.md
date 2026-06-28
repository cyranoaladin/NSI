---
title: "Audit du prototype Codex et stratégie de production du corpus NSI"
scope: "nsi-enseignement (Première / Terminale)"
date: "2026-06-26"
auteur: "Note de cadrage technique et pédagogique"
statut: "cadrage — à valider avant lancement en série"
---

# Audit du prototype Codex et stratégie de production du corpus NSI

## 1. Méthode d'audit

Audit par preuve empirique, pas par lecture des déclarations : extraction du dépôt,
exécution des scripts, lecture du contenu pédagogique, vérification des chiffres de
couverture contre le contenu réel. Aucun statut n'est cru sur parole.

## 2. État réel mesuré

| Indicateur | Valeur mesurée | Source |
| --- | --- | --- |
| Capacités officielles recensées | 114 | `coverage.md` (résumé) |
| Capacités `covered` | 0 | `coverage.md` |
| Capacités `needs_review` | 11 | `coverage.md` |
| Capacités `partial` | 4 | `coverage.md` |
| Capacités `absent` | 99 | `coverage.md` |
| Séquences planifiées Première | 15 (P00–P14) | `03_progressions/progression_premiere.md` |
| Séquences planifiées Terminale | 20 (T00–T19) | `03_progressions/progression_terminale.md` |
| Séquences réellement produites | 2 (1 par niveau) | arborescence |
| Tests Python | 15, PASS | `scripts/run_python_tests.py` |
| Scripts de contrôle | ~50 `check_*` (59 .py) | `scripts/` |
| Pipeline de rendu PDF/HTML | absent | `scripts/build_all.py` |

Lecture : l'infrastructure est avancée (~80 %), le corpus pédagogique ne couvre que
~6 % des séquences cibles, et **aucune** ressource n'est validée. L'effort a porté sur
l'échafaudage, pas sur le livrable.

## 3. Forces à conserver

1. **Gouvernance** : `AGENTS.md` (rôles + règles non négociables), `SKILLS.md` (spec par
   type de document), schéma de métadonnées, workflow de statuts. Réutilisable tel quel.
2. **Honnêteté du reporting** : la couverture affiche 0 `covered` / 99 `absent` au lieu de
   simuler l'achèvement ; statut `partial` forcé sur le parcours de graphes. À préserver.
3. **Progressions annuelles** complètes, calibrées sur le calendrier Tunisie 2026-2027
   (140 h NSI Première, 30,7 % projet).
4. **Séquences pilotes** scientifiquement correctes, jeu documentaire complet, code Python
   propre, typé et testé.

## 4. Faiblesses critiques (avec preuve)

1. **Gates de « profondeur » = comptage de mots-clés.** `check_document_depth.py` compte les
   occurrences de « Définition », « Exemple corrigé », « Erreur fréquente » et des lignes.
   Un document creux qui remplit le gabarit passe. Contredit `AGENTS.md` §2.8/§2.9.
2. **Couverture déclarative.** `check_program_coverage.py` fait confiance aux `evidence:`
   écrits par l'auteur dans le frontmatter. Ancre existante ≠ capacité enseignée.
3. **Pas de rendu.** `build_all.py` ne fait que valider. Charte LaTeX définie mais appliquée
   à aucun livrable (contenu en `.md`, aucun PDF/HTML produit). L'exigence « charte sur tous
   les documents + qualité UI/UX » n'est pas satisfaite.
4. **Style rédactionnel mécanique** : une phrase courte par ligne, sans liant. Correct mais
   pénible à lire ; faible sur l'axe forme / place de l'élève.
5. **Disproportion** effort infrastructure / volume produit.

## 5. Réorientation stratégique

Le goulot n'est pas l'infrastructure : c'est la production de contenu substantiel, bien
écrit, **rendu**, vérifié au niveau du **sens**. Trois décisions :

1. **Geler l'ajout de gates de comptage.** Ajouter un seul mécanisme manquant : la revue de
   substance (§6.3). `validated_pedagogy` ne s'obtient que par preuve textuelle citée,
   jamais par un script d'occurrences.
2. **Construire le pipeline de rendu** `.md → PDF/HTML` appliquant la charte, pour que la
   charte existe sur le livrable élève.
3. **Cadence pilote → série.** Valider une séquence de bout en bout (contenu + rendu +
   revue de substance) avant toute production en série, puis dérouler les progressions.

## 6. Workflow de production (cible)

### 6.1 Unité de travail : la séquence

On produit séquence par séquence, dans l'ordre des progressions, jamais en masse.

### 6.2 Chaîne par séquence (rôles → livrables → porte)

| Étape | Rôle | Livrable | Porte de passage |
| --- | --- | --- | --- |
| 1. Cadrage | Programme | capacités visées + métadonnées | capacités existent dans le YAML officiel |
| 2. Rédaction élève | Auteur | cours, trace, TD, TP, fiche méthode, aides | structure conforme `SKILLS.md` |
| 3. Code | Code | `python/` + `tests/` | tests PASS, code typé |
| 4. Évaluation | Évaluation | évaluation, corrigé, barème, grille, QCM | chaque question → une capacité |
| 5. Différenciation | Différenciation | 3 niveaux (socle/standard/approfondissement) | les 3 niveaux présents et distincts |
| 6. Revue scientifique | Scientifique | annotations | aucune approximation non signalée |
| 7. **Revue de substance** | Relecteur indépendant | rapport cité | voir §6.3 — bloquant |
| 8. Rendu | Édition | PDF/HTML charté, version élève + prof | rendu produit, charte appliquée |
| 9. QA final | QA | rapport, statut | aucun blocage critique |

### 6.3 Porte de substance (le contrôle qui manque)

Pour chaque capacité de la séquence, le relecteur produit une entrée écrite :

```
CAPACITÉ : <id> — <intitulé officiel>
PREUVE COURS    : <citation textuelle + ancre> — enseigne-t-elle réellement la capacité ? oui/non
PREUVE ENTRAÎNEMENT : <citation TD/TP> — l'élève s'entraîne-t-il vraiment ? oui/non
PREUVE CORRECTION   : <citation corrigé> — l'élève peut-il s'auto-corriger ? oui/non
VERDICT : validated_pedagogy | needs_content | BLOCKER
JUSTIFICATION : <2 lignes>
```

Règle : un « oui » sans citation vaut « non ». Aucun statut validé sans cette fiche.
Ce contrôle est humain ou modèle, mais jamais un comptage d'occurrences.

### 6.4 Définition de « terminé » pour une séquence

Contenu substantiel vérifié (§6.3) + code testé + évaluation alignée + différenciation
3 niveaux + rendu charté produit + QA sans blocage + métadonnées complètes.

## 7. Routage des modèles

| Tâche | Modèle conseillé | Raison |
| --- | --- | --- |
| Cours / TD / TP / corrigés (séquences difficiles) | Claude Opus | rédaction longue cohérente, rigueur |
| Contenu de volume (séquences standard) | Claude Sonnet | coût / cadence |
| Revue de substance (§6.3) | Claude | adhérence à la spec, résistance au contournement |
| Scripts QA, parsing, build, plomberie | indifférent | peu différenciant |
| Contrat de production | `AGENTS.md` / `SKILLS.md` existants | à garder quel que soit le modèle |

Décision : conserver l'ossature de Codex ; basculer rédaction et revue pédagogique sur
Claude.

## 8. Plan d'action séquencé

1. **Semaine 0 — Durcir le pilote.** Réécrire le cours pilote Première en prose liée
   (supprimer le « une phrase par ligne »). Passer la séquence par la porte de substance
   (§6.3). Objectif : 1 séquence réellement `validated_pedagogy`.
2. **Semaine 0 — Rendu.** Brancher `.md → PDF/HTML` charté ; produire les deux versions
   (élève / prof) de la séquence pilote. La charte doit apparaître sur le livrable.
3. **Semaine 1 — Geler/ajuster les gates.** Marquer les gates de comptage comme
   « indicatifs, non bloquants » ; rendre bloquante uniquement la porte de substance.
4. **Semaines 2+ — Série.** Dérouler Première puis Terminale dans l'ordre des progressions,
   une séquence à la fois, chaque séquence passant la chaîne §6.2 complète.
5. **Continu — Drive.** Mapper les ressources Drive existantes comme matière première de
   réécriture (jamais publiées telles quelles ; passage par quarantaine + métadonnées).

## 9. Risques et garde-fous

- **Risque : production en masse avant pilote validé.** Garde-fou : interdiction §6.1, une
  seule séquence ouverte à la fois jusqu'à la première validée de bout en bout.
- **Risque : retour du form-over-substance.** Garde-fou : seule la porte de substance est
  bloquante ; les comptages redeviennent indicatifs.
- **Risque : charte décorative.** Garde-fou : « terminé » exige un rendu charté réel, pas un
  fichier `.tex` non utilisé.
