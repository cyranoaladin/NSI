# QA Report

## Résumé

- Statut global : NON PUBLIABLE
- Ressources inventoriées : 448
- Ressources needs_review : 448
- Ressources publiables : 0
- Source generated : 448
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

## Fiches de cours

- Les fiches de cours sont des ressources d’aide et de révision. Elles ne prouvent aucune couverture publiable.
- Une capacité ne peut être covered que si existent et sont relus : cours ou fiche, séance, TD ou TP, corrigé, évaluation, barème, remédiation, revue pédagogique humaine et revue scientifique humaine.
- Fiches attendues : 35 séquences avec au moins une fiche.
- Fiches créées : 44
- Séquences sans fiche : 0
- Capacités sans fiche : 0
- Fiches théoriques : 0
- Fiches liées : 16
- Fiches opérationnelles : 28
- Liens vers supports existants : 81
- Liens vers supports inscrits au registre : 32
- Statut : needs_review
- Effet couverture : aucun ; les fiches ne rendent aucune capacité covered.

## Fiches liées non opérationnelles

| Fiche | Support absent | Registre associé | Date cible | Impact pédagogique | Action suivante |
|---|---|---|---|---|---|
| `P10_fiche_cours_reseaux_protocoles_paquets.md` | `P10_TD_reseaux_protocoles_paquets.md` | `missing_documents_register_v2.md` | 2027-06-30 | td absent : la fiche P10 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `P10_fiche_cours_reseaux_protocoles_paquets.md` | `P10_evaluation_reseaux_protocoles_paquets.md` | `missing_documents_register_v2.md` | 2027-06-30 | evaluation absent : la fiche P10 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `P11_fiche_cours_parcours_recherche_extremum_moyenne.md` | `P11_TD_parcours_recherche_extremum_moyenne.md` | `missing_documents_register_v2.md` | 2027-06-30 | td absent : la fiche P11 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `P11_fiche_cours_parcours_recherche_extremum_moyenne.md` | `P11_evaluation_parcours_recherche_extremum_moyenne.md` | `missing_documents_register_v2.md` | 2027-06-30 | evaluation absent : la fiche P11 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `P12_fiche_cours_tris_invariants_complexite.md` | `P12_TD_tris_invariants_complexite.md` | `missing_documents_register_v2.md` | 2027-06-30 | td absent : la fiche P12 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `P12_fiche_cours_tris_invariants_complexite.md` | `P12_evaluation_tris_invariants_complexite.md` | `missing_documents_register_v2.md` | 2027-06-30 | evaluation absent : la fiche P12 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `P13_fiche_cours_dichotomie_glouton_knn.md` | `P13_TD_dichotomie_glouton_knn.md` | `missing_documents_register_v2.md` | 2027-06-30 | td absent : la fiche P13 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `P13_fiche_cours_dichotomie_glouton_knn.md` | `P13_evaluation_dichotomie_glouton_knn.md` | `missing_documents_register_v2.md` | 2027-06-30 | evaluation absent : la fiche P13 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `P14_fiche_cours_synthese_projet_oral.md` | `P14_TD_synthese_projet_oral.md` | `missing_documents_register_v2.md` | 2027-06-30 | td absent : la fiche P14 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `P14_fiche_cours_synthese_projet_oral.md` | `P14_evaluation_synthese_projet_oral.md` | `missing_documents_register_v2.md` | 2027-06-30 | evaluation absent : la fiche P14 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `T10_fiche_cours_sql_insert_update_delete.md` | `T10_TD_sql_insert_update_delete.md` | `missing_documents_register_v2.md` | 2027-06-30 | td absent : la fiche T10 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `T10_fiche_cours_sql_insert_update_delete.md` | `T10_evaluation_sql_insert_update_delete.md` | `missing_documents_register_v2.md` | 2027-06-30 | evaluation absent : la fiche T10 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `T10_fiche_cours_sql_select_where_join.md` | `T10_TD_sql_select_where_join.md` | `missing_documents_register_v2.md` | 2027-06-30 | td absent : la fiche T10 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `T10_fiche_cours_sql_select_where_join.md` | `T10_evaluation_sql_select_where_join.md` | `missing_documents_register_v2.md` | 2027-06-30 | evaluation absent : la fiche T10 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `T11_fiche_cours_processus_ordonnancement_interblocage.md` | `T11_TD_processus_ordonnancement_interblocage.md` | `missing_documents_register_v2.md` | 2027-06-30 | td absent : la fiche T11 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `T11_fiche_cours_processus_ordonnancement_interblocage.md` | `T11_evaluation_processus_ordonnancement_interblocage.md` | `missing_documents_register_v2.md` | 2027-06-30 | evaluation absent : la fiche T11 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `T12_fiche_cours_routage_rip_ospf.md` | `T12_TD_routage_rip_ospf.md` | `missing_documents_register_v2.md` | 2027-06-30 | td absent : la fiche T12 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `T12_fiche_cours_routage_rip_ospf.md` | `T12_evaluation_routage_rip_ospf.md` | `missing_documents_register_v2.md` | 2027-06-30 | evaluation absent : la fiche T12 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `T13_fiche_cours_chiffrement_https.md` | `T13_TD_chiffrement_https.md` | `missing_documents_register_v2.md` | 2027-06-30 | td absent : la fiche T13 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `T13_fiche_cours_chiffrement_https.md` | `T13_evaluation_chiffrement_https.md` | `missing_documents_register_v2.md` | 2027-06-30 | evaluation absent : la fiche T13 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `T14_fiche_cours_modularite_api_paradigmes_bugs.md` | `T14_TD_modularite_api_paradigmes_bugs.md` | `missing_documents_register_v2.md` | 2027-06-30 | td absent : la fiche T14 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `T14_fiche_cours_modularite_api_paradigmes_bugs.md` | `T14_evaluation_modularite_api_paradigmes_bugs.md` | `missing_documents_register_v2.md` | 2027-06-30 | evaluation absent : la fiche T14 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `T15_fiche_cours_calculabilite_arret.md` | `T15_TD_calculabilite_arret.md` | `missing_documents_register_v2.md` | 2027-06-30 | td absent : la fiche T15 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `T15_fiche_cours_calculabilite_arret.md` | `T15_evaluation_calculabilite_arret.md` | `missing_documents_register_v2.md` | 2027-06-30 | evaluation absent : la fiche T15 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `T16_fiche_cours_diviser_pour_regner_tri_fusion.md` | `T16_TD_diviser_pour_regner_tri_fusion.md` | `missing_documents_register_v2.md` | 2027-06-30 | td absent : la fiche T16 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `T16_fiche_cours_diviser_pour_regner_tri_fusion.md` | `T16_evaluation_diviser_pour_regner_tri_fusion.md` | `missing_documents_register_v2.md` | 2027-06-30 | evaluation absent : la fiche T16 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `T17_fiche_cours_programmation_dynamique.md` | `T17_TD_programmation_dynamique.md` | `missing_documents_register_v2.md` | 2027-06-30 | td absent : la fiche T17 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `T17_fiche_cours_programmation_dynamique.md` | `T17_evaluation_programmation_dynamique.md` | `missing_documents_register_v2.md` | 2027-06-30 | evaluation absent : la fiche T17 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `T18_fiche_cours_boyer_moore.md` | `T18_TD_boyer_moore.md` | `missing_documents_register_v2.md` | 2027-06-30 | td absent : la fiche T18 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `T18_fiche_cours_boyer_moore.md` | `T18_evaluation_boyer_moore.md` | `missing_documents_register_v2.md` | 2027-06-30 | evaluation absent : la fiche T18 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `T19_fiche_cours_bac_pratique_grand_oral_projet.md` | `T19_TD_bac_pratique_grand_oral_projet.md` | `missing_documents_register_v2.md` | 2027-06-30 | td absent : la fiche T19 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |
| `T19_fiche_cours_bac_pratique_grand_oral_projet.md` | `T19_evaluation_bac_pratique_grand_oral_projet.md` | `missing_documents_register_v2.md` | 2027-06-30 | evaluation absent : la fiche T19 reste liée mais non opérationnelle pour la mise en activité ou l’évaluation. | créer |

## Gates indicatifs encore en échec

| Fichier concerné | Erreur | Décision | Date cible de correction |
|---|---|---|---|
| `scripts/check_required_sections.py` | check_required_sections: KO; premiere/sequences/s01_representation_donnees/corrige.md: section manquante -> variante acceptable; premiere/sequences/s01_representation_donnees/cours_eleve.md: section manquante -> activité d'introduction; premiere/sequences/s01_representation_donnees/cours_eleve.md: section manquante -> exemples corrigés; premiere/sequences/s01_representation_donnees/cours_eleve.md: section manquante -> exercices intégrés; premiere/sequences/s01_representation_donnees/cours_eleve.md: section manquante -> extension; premiere/sequences/s01_representation_donnees/cours_eleve.md: section manquante -> aides progressives | Dette pédagogique connue ; reste non bloquant uniquement pour le prototype global. | 2026-07-15 |
| `scripts/check_document_depth.py` | check_document_depth: KO; premiere/sequences/s01_representation_donnees/cours_eleve.md: profondeur insuffisante (234 lignes utiles, minimum 250); premiere/sequences/s01_representation_donnees/cours_eleve.md: moins de 3 définitions formelles | Dette pédagogique connue ; reste non bloquant uniquement pour le prototype global. | 2026-07-15 |

## Décisions

- Statut publication : NON.
- Statut covered : 0.
- Statut published : 0.
- Statut validated_* : 0.
- Archive pédagogique : dist/source_clean.tar.gz.
- Archive globale contenant .git : interdite comme livraison principale.
