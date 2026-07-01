# RAG v2 Cutover UI — Rapport

## Statut : V2_CUTOVER_DONE

## Compatibilite pre-bascule (section 1)

- **Embedder parite** : v2 vectors = 768d, query = nomic-embed-text 768d (PROUVE)
- **private_data** : v2 = False (bool). UI n'applique aucun filtre private_data (grep vide)
- **capacity_ids** : CSV dans Chroma, adapt_metadata cote NSI
- **Ancres Unicode** : UI (app_v2.py) utilise l'API ingestor, pas de re-slugging
- **Distance** : cosine (v2 et query identiques)

## Point de bascule (section 2)

Le fichier `/tmp/nsi_judge/.env.rag` controle la collection cible :
```
RAG_COLLECTION=nsi_corpus_v2   ← APRES
```
(avant : `RAG_COLLECTION=nsi_corpus`)

La bascule est un `sed -i` sur cette ligne. Pas de restart conteneur
necessaire (le smoke lit .env.rag a chaque invocation).

L'UI Streamlit (app_v2.py) utilise l'API `/search` avec `collection`
explicite — pas de collection hardcodee a changer.

## Rollback TESTE (section 3) — 3 transitions prouvees

```
TRANSITION 1: RAG_COLLECTION=nsi_corpus_v2 → smoke v2 VERT
  level=premiere pd=False(bool) anchor=p05---tp---tables-cs

TRANSITION 2: RAG_COLLECTION=nsi_corpus (rollback) → legacy confirme
  HITS=5, anchor=True section_anchor=False

TRANSITION 3: RAG_COLLECTION=nsi_corpus_v2 (re-switch) → smoke v2 VERT
  level=terminale caps=T-STRUCT-04A anchor=t05---td---arbres-binaire
```

Rollback = 1 commande sed, < 1 seconde. nsi_corpus (legacy) intact (4716 chunks).

## Bascule executee (section 4)

`/tmp/nsi_judge/.env.rag` pointe desormais sur `nsi_corpus_v2`.
Health-check : `/health` = `{"status":"healthy"}`. Aucune fenetre
d'indisponibilite (pas de restart conteneur).

## Smoke STRICT post-bascule (section 5)

```
RAG_SMOKE_STRICT=1 → RAG_SMOKE_TEST_OK collection=nsi_corpus_v2 hits=5
```

Fail-closed confirme :
```
RAG_SMOKE_STRICT=1, .env.rag absent → EXIT=1 (FAILED)
```

## Collections INCHANGEES (section 8)

| Collection | Avant | Apres |
|---|---|---|
| nsi_corpus | 4716 | 4716 (rollback source) |
| nsi_corpus_v2 | 5992 | 5992 |
| rag_education | 7181 | 7181 |
| rag_francais_premiere | 5948 | 5948 |
| rag_math_correction | 67 | 67 |

Korrigo container IDs identiques. Aucun secret affiche.

## Suppression legacy DIFFEREE (section 9)

nsi_corpus (4716 chunks) conserve comme source de rollback.
Suppression apres soak post-cutover (14 jours minimum) + smoke v2 stable.

## Invariants depot

```
covered : 0
absent : 22
published : 0
validated_* : 0
FINAL_STATUS = NON_RELEASE_READY
```

Le cutover est infra, pas une release contenu.
