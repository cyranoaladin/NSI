# NSI-enseignement

## 1) Philosophie pédagogique

Corpus pédagogique versionné pour la spécialité NSI (Première/Terminale), structuré par séquences annuelles et reposant sur :

- conformité officielle BO 2019 (1re/Terminale),
- séparation claire des rôles (élèves/professeur/corrigé),
- répétabilité (scripts de compilation, tests et contrôles),
- production d’artefacts exploitables sans mélange de données privées.

## 2) Organisation du dépôt

- `00_programmes_officiels/` : sources institutionnelles et références du programme.
- `01_charte_graphique_et_pedagogique/` : charte visuelle + schéma de métadonnées.
- `02_modeles_documents/` : modèles réutilisables (cours, TD, TP, évaluation, corrigé, guide prof, qcm, séquence).
- `03_progressions/` : progressions annuelles proposées.
- `premiere/`, `terminale/` : corpus par niveau (séquences + banques réutilisables).
- `scripts/` : scripts de build, contrôle qualité, tests.

## 2.1) Sources locales Drive

Les ressources Drive déjà extraites sont disponibles hors dépôt dans
`/home/alaeddine/Documents/NSI/Documents_DRIVE`. Les passes d’inventaire et de rédaction
doivent chercher d’abord dans ce dossier local, puis noter le chemin consulté dans les
métadonnées ou les registres. Cette source locale ne change pas les statuts : une ressource
adaptée depuis `Documents_DRIVE` reste `needs_review` tant qu’elle n’a pas été auditée.

## 3) Progressions annuelles

- Première : `03_progressions/progression_premiere.md`
- Terminale : `03_progressions/progression_terminale.md`

## 4) Compilation / production des livrables

1. Vérifier l’arborescence.
2. Mettre à jour le `manifest.csv` si de nouvelles ressources sont ajoutées.
3. Lancer :

```bash
cd nsi-enseignement
python scripts/build_all.py
python scripts/check_metadata.py
python scripts/check_links.py
python scripts/check_program_coverage.py
python scripts/generate_index.py
```

4. Vérifier les sorties :
- `01_build_reports/build_index.md`
- `01_build_reports/build_report.md`
- `coverage.md`
- `INDEX.md`

## 5) Ajouter une séquence

1. Créer un dossier dans `premiere/sequences/` ou `terminale/sequences/`.
2. Créer les fichiers obligatoires :
   - `cours_eleve.md`
   - `trace_ecrite.md`
   - `td.md`
   - `tp.md`
   - `fiche_methode.md`
   - `aides_progressives.md`
   - `corrige.md`
   - `guide_professeur.md`
   - `evaluation.md`
   - `qcm.json`
   - `projet_associe.md`
   - dossier `python/` avec au moins un module
   - dossier `tests/` avec tests unitaires
3. Ajouter les répertoires miroir dans `banques/` (facultatif selon stratégie locale).
4. Ajouter une ligne dans `manifest.csv`.

## 6) Produire versions élève/professeur/corrigé

- `cours_eleve.md` = version élève.
- `guide_professeur.md` = version enseignant.
- `corrige.md` = corrigé.

Les documents QCM/corrigé/tests restent dans les fichiers dédiés.

## 7) Vérifier la conformité programme

- Exécuter `check_program_coverage.py` (associant `manifest.csv` et `00_programmes_officiels/programme_nsi_2019.yaml`).
- Compléter les rubriques `sequence_possible`, `notion`, `source`, `objectifs`.

## 8) Publier les ressources

- Ne publier que les ressources:
  - sans données personnelles,
  - avec métadonnées complètes,
  - ayant des tests exécutables,
  - présentes dans l’inventaire et la couverture.

## 9) Commandes de vérification complètes

```bash
cd nsi-enseignement
python scripts/build_all.py
python scripts/check_links.py
python scripts/check_metadata.py
python scripts/check_program_coverage.py
python scripts/run_python_tests.py
python scripts/generate_index.py
```

Le dépôt est orienté vers une revue continue : chaque ajout doit être répercuté dans `manifest.csv`, `coverage.md` et `inventory_report.md`.
