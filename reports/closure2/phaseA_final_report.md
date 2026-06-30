# Phase A — Rapport final (passe 11, derniere)

## Statut : CLOSED_CLEAN (enforcement qualifie)

## Gate archive fail-closed + positif (passe 11)

test_no_stale_archive_guard durci :
- **Fail-closed** : echoue si la cible package-audit est absente du Makefile.
- **Positif** : verifie que build_source_archive est invoque ET qu'aucun token
  de guard (`test -f`, `[ -f`, `[ -e`, `if `, `||`, `&&`) n'apparait sur la ligne.

4 cas prouves :
- VERT : aucun guard present (2 passed)
- ROUGE : `[ -f dist/... ] ||` reintroduit (1 failed)
- ROUGE : `if [ -f ... ]` reintroduit (1 failed)
- ROUGE : cible package-audit supprimee (1 failed)

## Standard fail-closed (passe 11)

Inscrit dans AGENTS.md section 8. Regle : tout gate echoue si son evidence
est absente. Audit des gates recents :
- check_makefile_audit_policy : fail-closed (errors si cible absente)
- test_mypy_ratchet : fail-closed (assert sentinel stdout)
- test_no_stale_archive_guard : fail-closed (assert body non vide)

## Decision assumee : double-build (passe 9)

deliver-pedagogical-archive et package-audit reconstruisent chacun l'archive.
Choix delibere correctness > vitesse (surcout ~1s). Jamais de reutilisation
d'un dist/ perime.

## Enforcement qualifie

La CI DETECTE les fichiers perimes (freshness gate rouge prouve en run
28457692935) et les regressions. La CI ne BLOQUE PAS les merges tant que
la protection de branche main n'est pas activee.

Critere de fermeture :
```bash
gh api repos/cyranoaladin/NSI/branches/main/protection \
  --jq '(.required_pull_request_reviews != null) and
         ((.required_status_checks.contexts // []) | index("quality") != null)'
```
Doit renvoyer `true`.

## Sentinel STALE_CONTENT_FOR_ROUGE_TEST

`git grep` sur origin/main : present UNIQUEMENT comme citation dans
phaseA_closure_report.md (description du test), pas comme donnee stale.
PR #20 : CLOSED, non mergee (mergedAt=null).

## Doublon P08

duplicates_report.md : deux regenerations consecutives identiques (diff vide).
Le doublon reste un item de CONTENU au registre (qa_debt_register.md), non
modifiable sans revue pedagogique humaine.

## Definition de DONE Phase A

| Critere | Etat |
|---|---|
| Freshness rouge-en-CI | FAIT (run 28457692935) |
| Regression archive refermee | FAIT (guard supprime, passe 9) |
| Gate anti-regression FAIL-CLOSED+POSITIF | FAIT (4 cas prouves, passe 11) |
| Standard fail-closed inscrit | FAIT (AGENTS.md section 8) |
| Sentinel absent de main | FAIT (citation seulement) |
| Doublon P08 deterministe | FAIT (2 regens identiques) |
| Double-build documente | FAIT (decision assumee) |
| Critere protection durci | FAIT (commande jq exacte) |
| Enforcement qualifie | FAIT |
| Protection branche | ACTION HUMAINE REQUISE |

## Invariants

```
covered : 0
absent : 22
published : 0
validated_* : 0
FINAL_STATUS = NON_RELEASE_READY
```

## Dette residuelle

| Item | Nature | Action |
|---|---|---|
| Protection branche main OFF | Processus | Proprietaire active require PR + status check quality |
| Doublon P08 | Contenu pedagogique | Revue humaine |
| Backlog Drive (3+7+5) | Contenu | Lots Drive ulterieurs |
| 22 capacites absentes | Contenu | Production pedagogique |
| Cutover RAG prod | Infra | Runbook pret |
| Nits P2/P3 reviewers residuels | Cosmetique | qa_debt_register, sans nouvelle passe tooling |

Aucune dette technique de tooling.

## Lot 4 contenu : non

STOP DEFINITIF du tooling Phase A.
