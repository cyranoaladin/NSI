# QA Report

## Résumé

- Statut global : NON PUBLIABLE
- Ressources inventoriées : 180
- Ressources needs_review : 180
- Ressources publiables : 0
- Source generated : 180
- Source drive : 0
- Lignes drive_inventory.csv : 22
- Couverture covered : 0
- Couverture needs_review : 11
- Couverture partial : 4
- Couverture absent : 99
- make audit : PASS prototype uniquement si exécuté après génération de ce rapport
- make --no-print-directory release-audit : KO attendu
- Décision : ne pas générer de nouvelles séquences

## Commandes de référence

```bash
make audit
make package-audit
make --no-print-directory release-audit
```

## Dernier release-audit observé

```text
?? carnet_de_bord.md
?? missing_documents_register.md
?? scripts/check_document_naming_conventions.py
?? scripts/check_python_cache_stability.py
?? scripts/check_qcm_contract_consistency.py
?? scripts/check_session_referenced_files_exist.py
?? scripts/check_validated_documents_quality_gates.py
make: *** [Makefile:82: release-audit] Error 1
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
