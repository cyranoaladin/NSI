# QA Report

## Résumé

- Statut global : prototype technique non publiable, toutes les ressources restent en `needs_review`.
- Ressources Drive intégrées : 0.
- Ressources générées : 98.
- Séquences pilotes : 2 séquences refondues, Première `s01_representation_donnees` et Terminale `s01_structures_donnees_interfaces_implementations`.
- Tests Python : 8 tests exécutés, retour `PASS`.
- Quality gates : `PASS` technique au dernier audit, sans valeur de validation pédagogique ou scientifique.
- Couverture programme : 39 capacités `absent`, 4 `partial`, 11 `needs_review`, 0 `covered`.

## Commandes exécutées

### Nettoyage physique des artefacts

```bash
find . -type d -name "__pycache__" -prune -exec rm -rf {} +
find . -type f \( -name "*.pyc" -o -name "*.pyo" -o -name "*.aux" -o -name "*.log" -o -name "*.toc" -o -name "*.out" -o -name "*.synctex.gz" -o -name "*.fdb_latexmk" -o -name "*.fls" -o -name ".DS_Store" \) -delete
rm -rf .pytest_cache .mypy_cache .ruff_cache .venv
```

Sortie : aucune erreur affichée.

### Régénération index, inventaire et couverture

```bash
python scripts/generate_index.py && python scripts/rebuild_inventory.py && python scripts/check_program_coverage.py
```

Sortie :

```text
generate_index: done -> /home/alaeddine/Documents/NSI/nsi-enseignement/INDEX.md
rebuild_inventory: manifest= /home/alaeddine/Documents/NSI/nsi-enseignement/manifest.csv
rebuild_inventory: inventory= /home/alaeddine/Documents/NSI/nsi-enseignement/inventory_report.md
rebuild_inventory: duplicates= /home/alaeddine/Documents/NSI/nsi-enseignement/duplicates_report.md
check_program_coverage: generated coverage.md and programme matrices
```

### Audit final

```bash
make audit
```

Sortie :

```text
python scripts/rebuild_inventory.py
rebuild_inventory: manifest= /home/alaeddine/Documents/NSI/nsi-enseignement/manifest.csv
rebuild_inventory: inventory= /home/alaeddine/Documents/NSI/nsi-enseignement/inventory_report.md
rebuild_inventory: duplicates= /home/alaeddine/Documents/NSI/nsi-enseignement/duplicates_report.md
python scripts/check_metadata.py
check_metadata: PASS
python scripts/check_links.py
check_links: PASS
python scripts/check_no_private_data.py
check_no_private_data: PASS
python scripts/check_no_placeholders_docs.py
check_no_placeholders_docs: PASS
python scripts/check_no_placeholders_code.py
check_no_placeholders_code: PASS
python scripts/check_no_build_artifacts_in_index.py
check_no_build_artifacts_in_index: PASS
python scripts/check_required_sections.py
check_required_sections: PASS
python scripts/check_document_depth.py
check_document_depth: PASS
python scripts/check_qcm_schema.py
check_qcm_schema: PASS
python scripts/check_sequence_completeness.py
check_sequence_completeness: PASS
python scripts/check_program_coverage.py
check_program_coverage: generated coverage.md and programme matrices
python scripts/check_coverage_evidence.py
check_coverage_evidence: PASS
python scripts/run_python_tests.py
run_python_tests: tests exécutés = 8
run_python_tests: PASS
python scripts/check_quality_gates.py
check_metadata: PASS
check_links: PASS
check_no_private_data: PASS
check_no_placeholders_docs: PASS
check_no_placeholders_code: PASS
check_no_build_artifacts_in_index: PASS
check_required_sections: PASS
check_document_depth: PASS
check_qcm_schema: PASS
check_python_quality: PASS
check_sequence_completeness: PASS
check_pedagogical_alignment: PASS
check_bank_strategy: PASS
check_drive_mapping: PASS
check_coverage_evidence: PASS
run_python_tests: tests exécutés = 8
run_python_tests: PASS
== scripts/check_metadata.py ==
== scripts/check_links.py ==
== scripts/check_no_private_data.py ==
== scripts/check_no_placeholders_docs.py ==
== scripts/check_no_placeholders_code.py ==
== scripts/check_no_build_artifacts_in_index.py ==
== scripts/check_required_sections.py ==
== scripts/check_document_depth.py ==
== scripts/check_qcm_schema.py ==
== scripts/check_python_quality.py ==
== scripts/check_sequence_completeness.py ==
== scripts/check_pedagogical_alignment.py ==
== scripts/check_bank_strategy.py ==
== scripts/check_drive_mapping.py ==
== scripts/check_coverage_evidence.py ==
== scripts/run_python_tests.py ==
check_quality_gates: PASS
```

### Compteurs d'inventaire et couverture

```bash
python - <<'PY'
import csv
from collections import Counter
from pathlib import Path
with open('manifest.csv', encoding='utf-8', newline='') as f:
    rows=list(csv.DictReader(f))
print('manifest_rows', len(rows))
for key in ['source','statut','type','niveau','publishable','audience','copie_dans_banques']:
    print(key, dict(Counter(r.get(key,'') for r in rows)))
counts=Counter()
for line in Path('coverage.md').read_text(encoding='utf-8').splitlines():
    if not line.startswith('| ') or line.startswith('| ---') or line.startswith('| niveau'):
        continue
    cells=[c.strip() for c in line.strip('|').split('|')]
    if len(cells)==10:
        counts[cells[8]]+=1
print('coverage_status', dict(counts))
PY
```

Sortie :

```text
manifest_rows 98
source {'generated': 98}
statut {'needs_review': 98}
type {'document': 27, 'script': 25, 'banque': 14, 'sequence': 32}
niveau {'interne': 52, 'premiere': 23, 'terminale': 23}
publishable {'non': 98}
audience {'mixte': 74, 'corrige': 3, 'professeur': 3, 'eleve': 18}
copie_dans_banques {'non': 98}
coverage_status {'absent': 39, 'needs_review': 11, 'partial': 4}
```

## Bloquants restants

- `drive = 0` : accès Drive impossible dans l'environnement local courant.
- Les fichiers `drive_sources.yml`, `drive_inventory.csv` et `drive_mapping.md` exposent ce blocker explicitement.
- Toutes les ressources sont `needs_review`.
- Aucune ressource n'est `published`.
- Aucune capacité n'est `covered` car les statuts pédagogiques et scientifiques restent non finalisés.
- Le programme YAML doit encore être relu par un enseignant NSI avant usage comme référentiel de décision.
- Les deux séquences pilotes doivent être relues en profondeur avant diffusion élève.
- Les ressources Drive doivent être fournies sous forme d'export zip/tar ou montées localement.

## Séquences auditées

- Première : `premiere/sequences/s01_representation_donnees/`.
- Terminale : `terminale/sequences/s01_structures_donnees_interfaces_implementations/`.

## Décisions

- Corpus : non validé pour publication.
- Séquence Première : non validée pour publication.
- Séquence Terminale : non validée pour publication.
- Couverture programme : non fiable pour publication tant que Drive reste absent et que les statuts restent `needs_review`.
- Banques : stratégie source unique appliquée, sans copie manuelle.

## Prochaine action unique recommandée

Fournir un export zip/tar des dossiers Drive ou monter le Drive localement, puis relancer l'inventaire Drive avant toute nouvelle production de séquence.
