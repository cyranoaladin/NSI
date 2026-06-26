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
python scripts/check_git_clean.py
check_git_clean: PASS
python scripts/check_drive_mapping_release.py
check_drive_mapping_release: KO
- ressources Drive référencées mais non intégrées localement: copie_de_progres_nsi_amelioree.pdf, copie_de_progres_nsi_amelioree.tex, guide_enseignant_reprise_nsi_ameliore.tex, Cours.pdf, 2_TP.pdf, eval_nsi_corrige.pdf, eval_nsi.pdf, rendus_eleves, .git, .venv, TP_SOC.tex, Séquence1_Histoire de l'informatique, Séquence4_Types construits, 1_Cours_Types_construits.pdf, 1_RdD_Entier naturel.pdf, pays_monde.csv, NotesEleves.csv, Fichier_Eleves.csv, tri_bulles_eleve.py, Séquence1_TAD_Théorie
make: *** [Makefile:56: release-audit] Error 1
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
