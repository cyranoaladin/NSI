# QA Report

## Résumé

- Statut global : NON PUBLIABLE
- Ressources inventoriées : 170
- Ressources needs_review : 170
- Ressources publiables : 0
- Source generated : 170
- Source drive : 0
- Lignes drive_inventory.csv : 22
- Couverture covered : 0
- Couverture needs_review : 11
- Couverture partial : 4
- Couverture absent : 99
- make audit : PASS prototype uniquement si exécuté après génération de ce rapport
- make release-audit : KO attendu
- Décision : ne pas générer de nouvelles séquences

## Commandes de référence

```bash
make audit
make package-audit
make release-audit
```

## Dernier release-audit observé

```text
?? scripts/check_manifest_source_integrity.py
?? scripts/check_qa_report_freshness.py
?? scripts/check_session_specificity.py
?? scripts/check_session_week_calendar_consistency.py
?? scripts/check_teacher_corrections_alignment.py
?? scripts/check_uploaded_archive_policy.py
?? scripts/generate_qa_report.py
make: *** [Makefile:55: release-audit] Error 1
```

## Bloquants restants

- Ressources Drive référencées mais non intégrées localement.
- Toutes les ressources restent en revue ou non publiables.
- Aucune capacité n'est covered.
- Documents professeurs encore en needs_review.
- Revue pédagogique et scientifique humaine absente.

## Décisions

- Statut publication : NON.
- Statut covered : 0.
- Statut published : 0.
- Statut validated_* : 0.
