# QA Report

## Résumé

- Statut global : NON PUBLIABLE
- Ressources inventoriées : 516
- Ressources needs_review : 516
- Ressources publiables : 0
- Source generated : 509
- Source adapted_from_drive : 6
- Source import_partiel : 1
- Source inspiration_drive : 0
- Source drive : 0
- Lignes drive_inventory.csv : 22
- Couverture covered : 0
- Couverture needs_review : 11
- Couverture partial : 4
- Couverture absent : 99
- Archive pédagogique à transmettre : dist/source_clean.tar.gz
- Archive globale contenant .git : interdite comme livraison principale
- L’archive principale de livraison est dist/source_clean.tar.gz. Toute archive contenant .git/ est interdite comme livraison pédagogique.
- make audit : PASS prototype uniquement si exécuté après génération de ce rapport
- QUALITY_GATES_PASS : qualité interne contrôlée par scripts/check_quality_gates.py.
- PACKAGE_AUDIT_PASS : paquet source propre attendu via make package-audit.
- EXTRACTED_SOURCE_AUDIT_PASS : audit source extrait attendu sans dépendance Git.
- RELEASE_AUDIT_STATUS : RELEASE_AUDIT_FAIL
- FINAL_STATUS = NON_RELEASE_READY
- Raison : Drive partiellement intégré ; publication bloquée par ressources restantes non auditées / absentes / sensibles.
- Drive est partiellement intégré.
- L’audit portable ne vérifie pas les fichiers bruts Drive.
- L’audit local vérifie les fichiers bruts Drive lorsque le miroir Documents_DRIVE est présent.
- Le dépôt reste NON_RELEASE_READY.
- Drive integrated_adapted : 6
- Drive inspiration_only : 1
- Drive rejected_sensitive : 5
- Drive missing_local_copy : 7
- Drive deferred : 3
- Drive quarantined : 0
- Décision : ne pas générer de nouvelles séquences

## Commandes de référence

```bash
make audit
make package-audit
make --no-print-directory release-audit
```

## Dernier blocage release observé

```text
Le vrai make release-audit est exécuté séparément.
python scripts/check_drive_mapping_release.py
- rendus_eleves: rejected_sensitive - Dossier de rendus élèves interdit en livraison pédagogique.
- .git: rejected_sensitive - Dossier Git Drive interdit en ressource pédagogique.
- .venv: rejected_sensitive - Environnement virtuel interdit en ressource pédagogique.
- TP_SOC.tex: missing_local_copy - Fichier TP_SOC.tex absent ; dossier SoC alternatif repéré mais non repris dans ce lot.
- Séquence1_Histoire de l'informatique: missing_local_copy - Dossier exact absent du miroir local ; pas de contenu inventé.
- NotesEleves.csv: rejected_sensitive - Nom et contenu suggèrent des notes élèves ; ressource exclue.
- Fichier_Eleves.csv: rejected_sensitive - Nom suggère fichier élèves ; ressource exclue.
- Séquence6_Arbres binaires: deferred - Dossier local trouvé ; audit différé pour éviter intégration partielle non relue.
```

## Bloquants restants

- Drive partiellement intégré : voir `reports/drive_enrichment_report.md` et `drive_inventory.csv` pour les décisions par ressource.
- Ressources Drive absentes localement : 7.
- Ressources Drive différées : 3.
- Ressources Drive rejetées sensibles : 5.
- Toutes les ressources restent en revue ou non publiables.
- Aucune capacité n'est covered.
- Documents professeurs encore en needs_review.
- Revue pédagogique et scientifique humaine absente.
- Les séances hors première tranche restent théoriques et non prêtes.

## Fiches de cours

- Les fiches de cours sont des ressources d’aide et de révision. Elles ne prouvent aucune couverture publiable.
- Une capacité ne peut être covered que si existent et sont relus : cours ou fiche, séance, TD ou TP, corrigé, évaluation, barème, remédiation, revue pédagogique humaine et revue scientifique humaine.
- Fiches attendues : 35 séquences avec au moins une fiche.
- Fiches créées : 44
- Séquences sans fiche : 0
- Capacités sans fiche : 0
- Fiches théoriques : 0
- Fiches liées : 0
- Fiches opérationnelles : 44
- Liens vers supports existants : 113
- Liens vers supports inscrits au registre : 0
- Statut : needs_review
- Effet couverture : aucun ; les fiches ne rendent aucune capacité covered.

## Fiches liées non opérationnelles

| Fiche | Support absent | Registre associé | Date cible | Impact pédagogique | Action suivante |
|---|---|---|---|---|---|
| Aucune fiche liée non opérationnelle. | - | - | - | - | - |

## Gates indicatifs encore en échec

| Fichier concerné | Erreur | Décision | Date cible de correction |
|---|---|---|---|
| Aucun échec indicatif observé pendant cette génération. | - | - | - |

Les dettes indicatives ouvertes sont aussi suivies dans `qa_debt_register.md` avec cause, risque, impact, responsable et critère de fermeture.

## Décisions

- Statut publication : NON.
- Statut covered : 0.
- Statut published : 0.
- Statut validated_* : 0.
- Archive pédagogique : dist/source_clean.tar.gz.
- Archive globale contenant .git : interdite comme livraison principale.
