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
| scripts/check_status_promotion_guard.py | blocking_substance | interdit toute promotion sans verdict A et confirmation humaine |
| scripts/check_contract_substance_quality.py | blocking_substance | contrats de séquence |
| scripts/check_differentiation_distinctness.py | blocking_substance | différenciation non copiée |
| scripts/check_rendered_unit_artifacts.py | blocking_structure | rendu charté pilote |
| scripts/check_drive_enrichment_traceability_portable.py | blocking_privacy | traçabilité Drive portable |
| scripts/check_drive_action_plan_completeness.py | blocking_privacy | plan Drive restant |
| scripts/check_no_coverage_from_sheets_only.py | blocking_structure | pas de fausse couverture |
| scripts/run_python_tests.py | blocking_tests | tests Python |

## Informational Metrics

Les scripts de matrices, comptages de lignes, sections requises, profondeur approximative, ratios TP papier/exécutable et listes de séances sont des `informational_metric` sauf lorsqu'un autre gate bloquant s'appuie explicitement sur une preuve de substance.

## Frontière clone-propre / Drive local

### Gates clone-propre

Les gates de clone-propre doivent fonctionner dans une archive source ou un checkout CI sans miroir Drive local. Ils ne déréférencent pas `Documents_DRIVE` et s'appuient uniquement sur les traces publiables suivies dans Git. Sont notamment classés clone-propre : `scripts/check_drive_enrichment_traceability_portable.py`, `scripts/check_drive_action_plan_completeness.py`, `scripts/check_status_promotion_guard.py`, `scripts/check_substance_anchors.py` et l'agrégateur `scripts/check_quality_gates.py`.

### Gates Drive-requis

Les gates Drive-requis exigent explicitement un miroir `Documents_DRIVE` réel, non vide, adjacent au dépôt ou désigné par `NSI_DOCUMENTS_DRIVE_ROOT`. Ils doivent échouer bruyamment si ce dossier est absent ou vide afin d'éviter un passage au vert par vacuité. Sont classés Drive local : `scripts/check_drive_enrichment_traceability.py`, `scripts/check_local_drive_traceability.py`, `scripts/drive_local_inventory.py` et `scripts/drive_resource_triage.py`.

## Legacy

Les anciens scripts `check_required_sections.py`, `check_document_depth.py` et `check_document_style.py` restent consultables, mais ne sont pas des preuves de validation pédagogique.
