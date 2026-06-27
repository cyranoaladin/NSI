# Index des pré-jugements de substance

Ces verdicts sont des pré-jugements outillés. Ils vérifient des ancres et citations, mais ne remplacent pas une revue humaine.

## Périmètre pilote

| Unité | Verdict |
| --- | --- |
| P05 | `03_progressions/supports/premiere/P05/_substance_review.json` |
| P06 | `03_progressions/supports/premiere/P06/_substance_review.json` |
| T06 | `03_progressions/supports/terminale/T06/_substance_review.json` |
| T07 | `03_progressions/supports/terminale/T07/_substance_review.json` |
| T08 | `03_progressions/supports/terminale/T08/_substance_review.json` |
| T10 | `03_progressions/supports/terminale/T10/_substance_review.json` |
| T17 | `03_progressions/supports/terminale/T17/_substance_review.json` |
| T18 | `03_progressions/supports/terminale/T18/_substance_review.json` |

## Garde-fou adverse

Le fichier `substance_reviews/_adversarial/poisoned.verdict.json` doit être refusé par `scripts/check_substance_anchors.py`.

## Statut

Aucun verdict ne promeut une ressource. Les statuts restent `needs_review`, `covered = 0`, `validated_* = 0`, `published = 0`.
