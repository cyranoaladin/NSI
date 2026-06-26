# Pedagogical Blockers Report

- Statut global : NON PUBLIABLE.
- Décision : ne pas générer de nouvelles séquences.

## Bloquants explicitement suivis

- Séances encore génériques : le retour a identifié une répétition massive de gabarits ; `check_session_specificity.py` interdit les formulations génériques et les déroulés trop répétés.
- Semaines incohérentes : le retour a identifié des semaines impossibles ; `check_session_week_calendar_consistency.py` impose semaines scolaires 1 à 38, semaines civiles et cohérence avec les mois.
- Absence d’évaluation en Première : corrigée dans les séances et contrôlée par `check_evaluation_distribution.py`, mais la qualité des évaluations reste à relire.
- `qa_report.md` obsolète : `generate_qa_report.py` et `check_qa_report_freshness.py` pilotent désormais les chiffres à partir du manifest et de la couverture.
- Bug `source=drive` : `scripts/ingest_drive_export.py` ne doit plus être classé comme Drive ; `check_manifest_source_integrity.py` contrôle cette règle.
- Archive globale contenant `.git/` : politique documentée dans `delivery_policy.md`; seule `dist/source_clean.tar.gz` est livrable comme archive pédagogique.
- Documents professeurs encore `needs_review` : ils sont plus structurés mais non relus pédagogiquement et scientifiquement.
- Ressources Drive non intégrées localement : `release-audit` reste bloquant.

## Séquences trop denses

- Première S01 reste trop large : représentations de base, booléens, texte, types construits et tests. La progression la découpe en P01 à P07.
- Terminale S01 reste trop dense : interfaces, POO, piles/files/dictionnaires, graphes et BFS. La progression la découpe en T01 à T08.

## Capacités absentes

La couverture atomique contient encore des capacités `absent`; aucune capacité n'est `covered`.

## Risques de surcharge cognitive

- Ramadan impose de maintenir février et début mars sur activités guidées, remédiation ou pratiques courtes.
- Juin ne doit pas lancer de chapitre lourd ; les séances de juin sont synthèse, oral, pratique ou projet.

## Points à traiter avant publication

- Intégration locale et audit vie privée des ressources Drive.
- Relecture scientifique des définitions et exemples.
- Alignement exact entre chaque TD/TP/évaluation et son corrigé professeur.
- Exports élève sans corrigé et sans contenu professeur.
