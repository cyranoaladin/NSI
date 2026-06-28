# Extension de `check_program_coverage.py` — indexation de `supports/`

## Ce que ça change

Le script de couverture ne voyait que les 2 séquences pilotes
(`iter_declared_evidence` → `TARGET_SEQUENCES`). L'arbre
`03_progressions/supports/` (35 unités, 324 documents) lui était invisible.
L'extension ajoute une seconde source de preuves et fusionne les deux.

Résultat mesuré sur le dépôt, sans rédiger une ligne de contenu :

| statut | avant (pilotes seuls) | après (avec supports) |
| --- | --- | --- |
| covered | 0 | 0 |
| needs_review | 11 | 95 |
| partial | 4 | 2 |
| absent | **99** | **17** |

`covered` reste à 0 : aucune validation n'est inventée. Les documents supports
sont `needs_review`, donc les capacités qu'ils couvrent remontent en
`needs_review` — l'indicateur devient vrai, c'est tout. La validation reste le
travail du juge de substance.

## Fichiers

- `scripts/_supports_evidence.py` — **nouveau module additif**. N'modifie pas
  `_qa_common.py` (importé par ~137 scripts) : il réutilise ses primitives et
  expose `iter_support_evidence()`. Mappe le `document_type` de chaque doc
  support vers un type de preuve (cours, trace, td, tp, evaluation, corrige…).
- `scripts/check_program_coverage.py` — **version étendue**. Fusionne
  `iter_declared_evidence()` + `iter_support_evidence()`. Réversible via
  `--no-supports` (reproduit exactement l'ancien 0/11/4/99). Nouveau drapeau
  `--print-summary`.
- `check_program_coverage.diff` — diff lisible par rapport à l'original.
- `coverage.AFTER.md` — couverture régénérée (image honnête).
- `coverage_sources.md` — **nouveau rapport de provenance** : pour chaque
  capacité, d'où vient la preuve (`pilote`, `P05`, `T06`…). Outil de pilotage
  des trous réels.

## Installation

Déposer les deux fichiers `scripts/` dans le dépôt (le module à côté de
`_qa_common.py`), puis :

```bash
python scripts/check_program_coverage.py --print-summary          # avec supports
python scripts/check_program_coverage.py --no-supports            # ancien comportement
```

Aucune dépendance nouvelle (PyYAML déjà requis par `_qa_common`).

## Finding important : trous de contenu vs trous d'étiquetage

Les 17 capacités restées `absent` ne sont pas toutes des manques de contenu.
Plusieurs sont des **trous d'étiquetage** : le contenu existe dans une unité
mais l'identifiant atomique n'est pas déclaré dans son frontmatter. Vérifié :

- `P-DATA-CONSTR-02B` (tableau par compréhension) : enseigné dans le cours et le
  TD du pilote Première, mais l'unité n'est pas taguée avec cet id.
- `T-ALGO-01A/B/C/D` (taille, hauteur, parcours infixe/préfixe/suffixe/largeur)
  et `T-STRUCT-04B` (mesures d'arbres) : étiquetés dans **0** document, alors que
  l'unité `T06` (arbres binaires de recherche) possède cours + TP + tests sur
  les arbres et mentionne les parcours. `T06` n'est tagué qu'avec `T-ALGO-01E/01F`.

Conséquence pratique : une **passe d'étiquetage** (ajouter les ids atomiques
manquants aux frontmatters quand le contenu existe réellement) résorbera une
partie des 17 sans rédaction, et isolera les vrais manques de contenu à écrire.

Prochaine brique utile : un petit auditeur d'étiquetage qui, pour chaque
capacité `absent`, cherche dans le corpus les mots-clés de l'intitulé officiel
et signale « contenu probable non étiqueté » vs « contenu réellement absent ».
