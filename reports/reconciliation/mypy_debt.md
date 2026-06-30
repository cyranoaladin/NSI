# Dette mypy --strict residuelle

## Configuration

- `pyproject.toml` : `[tool.mypy]` strict=true, explicit_package_bases=true, mypy_path="."
- Convention d'empaquetage : `python -m scripts.<module>` (Makefile, check_quality_gates.py, tests)
- Tous les `sys.path.insert` + `# noqa: E402` rendus inutiles ont été retirés
- `scripts/__init__.py` et `scrapping_NSI/__init__.py` présents

## Résultat

`mypy --strict scripts/ scrapping_NSI/` : **112 erreurs dans 29 fichiers** (sur 208 fichiers vérifiés).

Aucune erreur `import-not-found` ne subsiste (557 → 0 après conversion).

## Ventilation par catégorie

| Catégorie | Nombre | Nature |
|-----------|--------|--------|
| arg-type | 31 | Typage dict[str, object] vs types attendus |
| var-annotated | 17 | Variables sans annotation de type explicite |
| attr-defined | 13 | Accès à .get() sur object au lieu de dict |
| union-attr | 9 | Accès conditionnel sur unions Optional |
| no-untyped-def | 7 | Fonctions sans annotation retour |
| return-value | 6 | Type retour incompatible |
| misc | 6 | Divers (generator types, etc.) |
| assignment | 6 | Assignation incompatible |
| type-arg | 5 | Arguments de types génériques |
| no-untyped-call | 4 | Appels à fonctions non typées |
| operator | 3 | Opérateurs sur types incompatibles |
| index | 2 | Index sur types incompatibles |
| unused-ignore | 1 | Directive noqa inutile |
| comparison-overlap | 1 | Comparaison sur types disjoints |
| call-overload | 1 | Surcharge non compatible |

## Fichiers principaux concernés

- `scripts/check_session_*.py` (4 fichiers, ~40 erreurs) : typage dict[str, object] hérité de _session_checks
- `scripts/generate_qa_report.py` (~15 erreurs) : dict course_sheet_stats retourne object
- `scripts/rebuild_inventory.py` (~10 erreurs) : typage frontmatter dict
- `scripts/_qa_common.py` (~5 erreurs) : YAML loader retourne Any
- `scripts/substance_judge.py` (~8 erreurs) : typage JSON verdict
- `scripts/generate_index.py` (2 erreurs) : fonction sans annotation
- `scrapping_NSI/scraper_nsi_v2.py` (2 erreurs) : imports bare netpolicy/provenance dans test exclus

## Cause racine

Les erreurs résiduelles proviennent principalement du typage dynamique YAML/JSON :
`yaml.safe_load()` retourne `Any`, propagé comme `object` dans les dictionnaires
intermédiaires. Corriger nécessiterait d'ajouter des TypedDict ou des casts explicites
dans ~29 fichiers, travail estimé à 2-3h sans valeur fonctionnelle immédiate.

## Couverture par test xfail

Le test `tests/test_mypy_strict_debt.py::test_mypy_strict_known_debt` vérifie que
mypy --strict produit exactement 112 erreurs (± tolérance). Si le nombre baisse,
le test force la mise à jour du seuil. Si le nombre monte, le test échoue.
