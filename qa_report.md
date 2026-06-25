# QA Report

## Résumé

- Statut global : NON PUBLIABLE.
- Raison principale : ressources Drive absentes localement, ressources `needs_review`, aucune capacité `covered`.
- Ressources Drive référencées : 22 lignes dans `drive_inventory.csv`.
- Ressources Drive intégrées localement : 0.
- Ressources générées : 137.
- Séquences pilotes : 2, non publiées.
- Tests Python : 15 tests exécutés, `PASS`.
- `make audit` : PASS technique uniquement.
- `make release-audit` : NON PASSANT.
- Couverture programme : 0 `covered`, 11 `needs_review`, 4 `partial`, 39 `absent`.
- Décision : ne pas générer de nouvelles séquences.

## Commandes exécutées

### Audit prototype hors Git pendant édition

```bash
PYTHONDONTWRITEBYTECODE=1 python scripts/generate_index.py
PYTHONDONTWRITEBYTECODE=1 python scripts/rebuild_inventory.py
PYTHONDONTWRITEBYTECODE=1 python scripts/check_metadata.py
PYTHONDONTWRITEBYTECODE=1 python scripts/check_links.py
PYTHONDONTWRITEBYTECODE=1 python scripts/check_no_private_data.py
PYTHONDONTWRITEBYTECODE=1 python scripts/check_no_placeholders_docs.py
PYTHONDONTWRITEBYTECODE=1 python scripts/check_no_placeholders_code.py
PYTHONDONTWRITEBYTECODE=1 python scripts/check_no_build_artifacts_in_index.py
PYTHONDONTWRITEBYTECODE=1 python scripts/check_required_sections.py
PYTHONDONTWRITEBYTECODE=1 python scripts/check_document_depth.py
PYTHONDONTWRITEBYTECODE=1 python scripts/check_qcm_schema.py
PYTHONDONTWRITEBYTECODE=1 python scripts/check_document_style.py
PYTHONDONTWRITEBYTECODE=1 python scripts/check_sequence_completeness.py
PYTHONDONTWRITEBYTECODE=1 python scripts/check_course_internal_coherence.py
PYTHONDONTWRITEBYTECODE=1 python scripts/check_td_corrige_alignment.py
PYTHONDONTWRITEBYTECODE=1 python scripts/check_tp_test_alignment.py
PYTHONDONTWRITEBYTECODE=1 python scripts/check_evaluation_bareme_alignment.py
PYTHONDONTWRITEBYTECODE=1 python scripts/check_learning_objectives_assessed.py
PYTHONDONTWRITEBYTECODE=1 python scripts/check_differentiation_quality.py
PYTHONDONTWRITEBYTECODE=1 python scripts/check_scientific_claims_review.py
PYTHONDONTWRITEBYTECODE=1 python scripts/check_program_capacity_evidence_depth.py
PYTHONDONTWRITEBYTECODE=1 python scripts/check_program_coverage.py
PYTHONDONTWRITEBYTECODE=1 python scripts/check_coverage_evidence.py
PYTHONDONTWRITEBYTECODE=1 python scripts/run_python_tests.py
```

Sortie synthétique :

```text
check_metadata: PASS
check_links: PASS
check_no_private_data: PASS
check_no_placeholders_docs: PASS
check_no_placeholders_code: PASS
check_no_build_artifacts_in_index: PASS
check_required_sections: PASS
check_document_depth: PASS
check_qcm_schema: PASS
check_document_style: PASS
check_sequence_completeness: PASS
check_course_internal_coherence: PASS
check_td_corrige_alignment: PASS
check_tp_test_alignment: PASS
check_evaluation_bareme_alignment: PASS
check_learning_objectives_assessed: PASS
check_differentiation_quality: PASS
check_scientific_claims_review: PASS
check_program_capacity_evidence_depth: PASS
check_coverage_evidence: PASS
run_python_tests: tests exécutés = 15
run_python_tests: PASS
```

### Release checks exécutés individuellement

```bash
PYTHONDONTWRITEBYTECODE=1 python scripts/check_drive_mapping_release.py
```

Sortie :

```text
check_drive_mapping_release: KO
- ressources Drive référencées mais non intégrées localement: copie_de_progres_nsi_amelioree.pdf, copie_de_progres_nsi_amelioree.tex, guide_enseignant_reprise_nsi_ameliore.tex, Cours.pdf, 2_TP.pdf, eval_nsi_corrige.pdf, eval_nsi.pdf, rendus_eleves, .git, .venv, TP_SOC.tex, Séquence1_Histoire de l'informatique, Séquence4_Types construits, 1_Cours_Types_construits.pdf, 1_RdD_Entier naturel.pdf, pays_monde.csv, NotesEleves.csv, Fichier_Eleves.csv, tri_bulles_eleve.py, Séquence1_TAD_Théorie
```

```bash
PYTHONDONTWRITEBYTECODE=1 python scripts/check_no_needs_review_for_release.py
```

Sortie :

```text
check_no_needs_review_for_release: KO
- 137 ressources restent needs_review
```

```bash
PYTHONDONTWRITEBYTECODE=1 python scripts/check_no_absent_coverage_for_release.py
```

Sortie :

```text
check_no_absent_coverage_for_release: KO
- aucune capacité covered
- 43 capacités restent absent ou partial
```

## Bloquants restants

- Drive : ressources référencées mais non intégrées localement.
- Vie privée : les ressources Drive contenant `rendus_eleves`, `NotesEleves.csv`, `Fichier_Eleves.csv`, `.git` ou `.venv` doivent être exclues ou anonymisées avant ingestion.
- Statuts : 137 ressources restent `needs_review`.
- Couverture : aucune capacité n'est `covered`.
- Première : `s01_representation_donnees` est trop large et doit être découpée.
- Terminale : `s01_structures_donnees_interfaces_implementations` reste dense ; `T-ALGO-02` reste `partial`.
- YAML officiel : encore trop agrégé pour une couverture fine publiable.
- Revue humaine : aucune revue pédagogique ou scientifique finale n'est tracée.

## Séquences auditées

- Première : `premiere/sequences/s01_representation_donnees/`.
- Terminale : `terminale/sequences/s01_structures_donnees_interfaces_implementations/`.

## Décisions

- Corpus : non publié.
- Première S01 : décision de publication NON.
- Terminale S01 : décision de publication NON.
- Drive : référencé, non intégré.
- Banques : source unique conservée.
- Couverture : aucune capacité promue à `covered`.
- Génération annuelle : interdite à ce stade.

## Prochaine action unique recommandée

Importer un export Drive contrôlé dans un dossier de quarantaine, calculer les hash, exclure ou anonymiser les données élèves, puis relancer l'inventaire Drive avant toute revue pédagogique finale.
