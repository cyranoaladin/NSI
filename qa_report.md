# QA Report

## Résumé

- Statut global : NON PUBLIABLE
- Ressources inventoriées : 241
- Ressources needs_review : 241
- Ressources publiables : 0
- Source generated : 241
- Source drive : 0
- Lignes drive_inventory.csv : 22
- Couverture covered : 0
- Couverture needs_review : 11
- Couverture partial : 4
- Couverture absent : 99
- Archive pédagogique à transmettre : dist/source_clean.tar.gz
- Archive globale contenant .git : interdite comme livraison principale
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
python scripts/cleanup_python_artifacts.py
cleanup_python_artifacts: removed 0 path(s)
python scripts/check_git_clean.py
check_git_clean: PASS
python scripts/check_drive_mapping_release.py
check_drive_mapping_release: KO
- ressources Drive référencées mais non intégrées localement: copie_de_progres_nsi_amelioree.pdf, copie_de_progres_nsi_amelioree.tex, guide_enseignant_reprise_nsi_ameliore.tex, Cours.pdf, 2_TP.pdf, eval_nsi_corrige.pdf, eval_nsi.pdf, rendus_eleves, .git, .venv, TP_SOC.tex, Séquence1_Histoire de l'informatique, Séquence4_Types construits, 1_Cours_Types_construits.pdf, 1_RdD_Entier naturel.pdf, pays_monde.csv, NotesEleves.csv, Fichier_Eleves.csv, tri_bulles_eleve.py, Séquence1_TAD_Théorie
make: *** [Makefile:release-audit] Error 1
```

## Bloquants restants

- Ressources Drive référencées mais non intégrées localement.
- Toutes les ressources restent en revue ou non publiables.
- Aucune capacité n'est covered.
- Documents professeurs encore en needs_review.
- Revue pédagogique et scientifique humaine absente.
- Les séances hors première tranche restent théoriques et non prêtes.

## Décisions

- Statut publication : NON.
- Statut covered : 0.
- Statut published : 0.
- Statut validated_* : 0.
- Archive pédagogique : dist/source_clean.tar.gz.
- Archive globale contenant .git : interdite comme livraison principale.
