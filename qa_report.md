# QA Report

## Résumé

- Statut global : NON PUBLIABLE
- Ressources inventoriées : 500
- Ressources needs_review : 500
- Ressources publiables : 0
- Source generated : 500
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
- Décision : ne pas générer de nouvelles séquences

## Commandes de référence

```bash
make audit
make package-audit
make --no-print-directory release-audit
```

## Dernier blocage release observé

```text
Snapshot des bloqueurs release hors check_git_clean.
Le vrai make release-audit est exécuté séparément.
python scripts/check_drive_mapping_release.py
check_drive_mapping_release: KO
- ressources Drive référencées mais non intégrées localement: copie_de_progres_nsi_amelioree.pdf, copie_de_progres_nsi_amelioree.tex, guide_enseignant_reprise_nsi_ameliore.tex, Cours.pdf, 2_TP.pdf, eval_nsi_corrige.pdf, eval_nsi.pdf, rendus_eleves, .git, .venv, TP_SOC.tex, Séquence1_Histoire de l'informatique, Séquence4_Types construits, 1_Cours_Types_construits.pdf, 1_RdD_Entier naturel.pdf, pays_monde.csv, NotesEleves.csv, Fichier_Eleves.csv, tri_bulles_eleve.py, Séquence1_TAD_Théorie
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
| `scripts/check_required_sections.py` | check_required_sections: KO; premiere/sequences/s01_representation_donnees/corrige.md: section manquante -> variante acceptable; premiere/sequences/s01_representation_donnees/cours_eleve.md: section manquante -> activité d'introduction; premiere/sequences/s01_representation_donnees/cours_eleve.md: section manquante -> exemples corrigés; premiere/sequences/s01_representation_donnees/cours_eleve.md: section manquante -> exercices intégrés; premiere/sequences/s01_representation_donnees/cours_eleve.md: section manquante -> extension; premiere/sequences/s01_representation_donnees/cours_eleve.md: section manquante -> aides progressives | Dette pédagogique connue ; reste non bloquant uniquement pour le prototype global. | 2026-07-15 |
| `scripts/check_document_depth.py` | check_document_depth: KO; premiere/sequences/s01_representation_donnees/cours_eleve.md: profondeur insuffisante (234 lignes utiles, minimum 250); premiere/sequences/s01_representation_donnees/cours_eleve.md: moins de 3 définitions formelles | Dette pédagogique connue ; reste non bloquant uniquement pour le prototype global. | 2026-07-15 |

Les dettes indicatives ouvertes sont aussi suivies dans `qa_debt_register.md` avec cause, risque, impact, responsable et critère de fermeture.

## Décisions

- Statut publication : NON.
- Statut covered : 0.
- Statut published : 0.
- Statut validated_* : 0.
- Archive pédagogique : dist/source_clean.tar.gz.
- Archive globale contenant .git : interdite comme livraison principale.
