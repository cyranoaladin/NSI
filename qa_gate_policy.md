# Politique des gates QA

## Principe

Les gates bloquants doivent rester peu nombreux, explicites et défendables. Les scripts de comptage, de longueur, de présence de sections ou de métrique documentaire restent utiles, mais ils ne doivent pas remplacer le jugement de substance.

## Classes

| Script | Classe | Rôle |
| --- | --- | --- |
| scripts/check_git_clean.py | blocking_structure | dépôt propre avant audit |
| scripts/check_audit_folder_policy.py | blocking_structure | `/AUDIT` hors corpus pédagogique |
| scripts/check_content_tree_policy.py | blocking_structure | arbre canonique `supports/` |
| scripts/check_metadata.py | blocking_structure | métadonnées minimales |
| scripts/check_links.py | blocking_structure | liens internes |
| scripts/check_no_private_data.py | blocking_privacy | données personnelles |
| scripts/check_no_placeholders_docs.py | blocking_structure | placeholders documents |
| scripts/check_no_placeholders_code.py | blocking_structure | placeholders code |
| scripts/check_no_build_artifacts_in_index.py | blocking_structure | artefacts suivis |
| scripts/check_uploaded_archive_policy.py | blocking_structure | politique archives |
| scripts/check_program_coverage.py | blocking_structure | indicateur central de couverture documentaire |
| scripts/check_substance_anchors.py | blocking_substance | garde-fou mécanique du juge de substance |
| scripts/check_status_promotion_guard.py | blocking_substance | interdit `validated_*`, `covered>0` ou `published>0` sans verdict A vérifié et confirmation relecteur |
| scripts/check_contract_substance_quality.py | blocking_substance | contrats de séquence |
| scripts/check_differentiation_distinctness.py | blocking_substance | différenciation non copiée |
| scripts/check_rendered_unit_artifacts.py | blocking_structure | rendu charté pilote |
| scripts/check_drive_enrichment_traceability_portable.py | blocking_privacy | traçabilité Drive portable |
| scripts/check_drive_action_plan_completeness.py | blocking_privacy | plan Drive restant |
| scripts/check_no_coverage_from_sheets_only.py | blocking_structure | pas de fausse couverture |
| scripts/run_python_tests.py | blocking_tests | tests Python |

## Informational Metrics

Les scripts de matrices, comptages de lignes, sections requises, profondeur approximative, ratios TP papier/exécutable et listes de séances sont des `informational_metric` sauf lorsqu'un autre gate bloquant s'appuie explicitement sur une preuve de substance.

## Gates clone-propre

Ces gates doivent fonctionner dans une archive extraite sans miroir local
`Documents_DRIVE` et peuvent donc être appelés par la CI et par
`make audit-extracted-source`.

- `scripts/check_drive_enrichment_traceability_portable.py`
- `scripts/check_drive_action_plan_completeness.py`
- `scripts/check_drive_trace_no_absolute_local_paths.py`
- `scripts/check_status_promotion_guard.py`

## Gates Drive-requis

Ces gates d'audit local déréférencent le miroir brut `Documents_DRIVE`. Ils ne
doivent pas être appelés par la CI ni par `make audit-extracted-source`. S'ils
sont exécutés avec un miroir absent ou vide alors que des ressources locales sont
déclarées intégrées, ils doivent échouer bruyamment au lieu de passer par
vacuité.

- `scripts/check_local_drive_traceability.py`
- `scripts/check_drive_integration_plan.py`
- `scripts/check_drive_enrichment_traceability.py`

## Legacy

Les anciens scripts `check_required_sections.py`, `check_document_depth.py` et `check_document_style.py` restent consultables, mais ne sont pas des preuves de validation pédagogique.
