# Registre de dette QA

## Dettes indicatives encore ouvertes

| Fichier concerné | Gate concerné | Cause | Risque | Impact | Décision | Date cible | Responsable | Critère de fermeture |
|---|---|---|---|---|---|---|---|---|
| Aucune dette indicative ouverte sur S01 après enrichissement Drive. | - | - | - | - | Continuer à exécuter les gates, sans promotion de statut. | - | équipe NSI | `python scripts/check_required_sections.py` et `python scripts/check_document_depth.py` restent PASS. |

## Dettes fermées

| Fichier concerné | Gate concerné | Cause initiale | Action réalisée | Date de fermeture | Critère vérifié |
|---|---|---|---|---|---|
| `premiere/sequences/s01_representation_donnees/cours_eleve.md` | `scripts/check_required_sections.py` | Titres attendus absents : activité d'introduction, exemples corrigés, exercices intégrés, extension, aides progressives. | Sections ajoutées et adaptées depuis la ressource Drive `1_RdD_Entier naturel.pdf`, sans copie brute. | 2026-06-26 | `python scripts/check_required_sections.py` PASS. |
| `premiere/sequences/s01_representation_donnees/corrige.md` | `scripts/check_required_sections.py` | Libellé singulier `variante acceptable` absent. | Section renommée et critère explicite ajouté. | 2026-06-26 | `python scripts/check_required_sections.py` PASS. |
| `premiere/sequences/s01_representation_donnees/cours_eleve.md` | `scripts/check_document_depth.py` | Profondeur utile et définitions formelles insuffisantes. | Activité d'introduction, définitions formelles, repères d'exemples, extension et aides progressives ajoutés. | 2026-06-26 | `python scripts/check_document_depth.py` PASS. |

## Dettes release Drive

| Dette | Cause | Risque | Impact | Décision | Date cible | Responsable | Critère de fermeture |
|---|---|---|---|---|---|---|---|
| Drive partiellement intégré | 7 copies locales absentes, 3 ressources différées et 5 ressources sensibles rejetées restent classées dans `drive_inventory.csv`. | Publication fondée sur sources incomplètes ou non auditées. | `make release-audit` doit rester en échec. | Maintenir `FINAL_STATUS = NON_RELEASE_READY`; poursuivre les lots d'audit Drive ressource par ressource. | 2026-07-15 | équipe NSI | `scripts/check_drive_mapping_release.py` passe sans `missing_local_copy`, `deferred` ni `rejected_sensitive` bloquant. |
| Portabilité Drive | `source_clean.tar.gz` ne contient pas le miroir brut `Documents_DRIVE`. | Audit extrait non reproductible si un contrôle local déréférence les fichiers Drive. | L'audit extrait doit utiliser le contrôle portable. | Séparer `check_drive_enrichment_traceability.py` local et `check_drive_enrichment_traceability_portable.py` portable. | 2026-06-26 | équipe NSI | `timeout 180 make audit-extracted-source` passe sans miroir Drive. |
