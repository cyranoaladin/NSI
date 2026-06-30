# Dette mypy --strict résiduelle

## Configuration

- `pyproject.toml` : `[tool.mypy]` strict=true, explicit_package_bases=true, mypy_path="."
- Convention d'empaquetage : `python -m scripts.<module>` (Makefile, check_quality_gates.py, tests)
- Tous les `sys.path.insert` + `# noqa: E402` rendus inutiles ont été retirés
- `scripts/__init__.py` et `scrapping_NSI/__init__.py` présents

## Résultat (post-vérification)

`mypy --strict scripts/ scrapping_NSI/` : **90 erreurs dans 23 fichiers** (sur 208 vérifiés).

Progression : 557 → 112 (passe réconciliation) → 90 (passe vérification, -22).

Corrections passe vérification :
- **union-attr (9→0)** : vrais bugs latents (Response|None, Match|None) corrigés
- **no-untyped-def (7→0)** : annotations retour manquantes ajoutées
- **no-untyped-call (4→0)** : appels sans types résolus
- **unused-ignore (1→0)** : directive type: ignore inutile retirée

## Ventilation résiduelle

| Catégorie | Nombre | Justification irréductibilité |
|-----------|--------|-------------------------------|
| arg-type | 31 | yaml.safe_load() retourne Any ; dict[str, object] propagé |
| var-annotated | 16 | Variables initialisées par YAML/CSV sans type explicite |
| attr-defined | 13 | .get() sur object au lieu de dict (YAML source) |
| return-value | 6 | Types retour dict incompatibles (object vs str) |
| misc | 6 | Generator types, class patterns |
| assignment | 6 | Assignation dict[str, object] vs dict[str, str] |
| type-arg | 5 | Arguments génériques Counter/dict sous-typés |
| str | 3 | Argument str vs Path attendu |
| operator | 3 | Opérateurs sur types non annotés |
| index | 2 | Index string sur object |
| comparison-overlap | 1 | Comparaison types disjoints |
| call-overload | 1 | Surcharge range() non compatible |

## Cause racine commune

90% des erreurs restantes tracent à `yaml.safe_load()` qui retourne `Any`.
Les dictionnaires intermédiaires sont typés `dict[str, object]` par mypy strict,
rendant chaque `.get()` ou accès `["key"]` une erreur potentielle de type.
Corriger nécessite ~23 fichiers avec TypedDict ou casts explicites — travail
mécanique sans valeur fonctionnelle. Aucune de ces erreurs ne masque un bug
d'exécution (les objets sont en réalité des dicts bien formés à l'exécution).

## Mécanisme de garde : cliquet (ratchet)

Le test `tests/test_mypy_strict_debt.py::test_mypy_ratchet` épingle le jeu
exact des 90 erreurs dans `tests/mypy_baseline.txt` (fichier:ligne:message).

- Nouvelle erreur absente du baseline → **test ROUGE** (régression bloquée)
- Erreur fixée encore dans baseline → **test ROUGE** (forcer la mise à jour)
- Baseline == réel → **test VERT**

Prouvé : ajout d'une erreur fictive → test rouge ; retrait → test vert.
