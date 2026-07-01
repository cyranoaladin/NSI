# RAG v2 Cutover — Etat de verite

## PROUVE (chaque ligne adossee a une commande)

### v2 = 5992 chunks

```
curl ... /collections/{v2_id}/count → 5992
```

### v2 dim = 768 (nomic-embed-text)

```
POST /collections/{v2_id}/get {limit:1, include:["embeddings"]}
→ V2_VECTOR_DIM=768
```

### v2 PII = 0

Ingestion avec `rag_core.file_has_pii()` actif, sortie `PII_skipped=0`.
Re-scan : tous les fichiers source passent `check_no_private_data: PASS`.

### Metadonnees canoniques (hit reel)

```
POST /search {q:"CSV", collection:"nsi_corpus_v2", k:1}
→ collection='nsi_corpus_v2'
  source_type='nsi_corpus'
  private_data=False (bool)
  capacity_ids='P-TABLE-01,P-TABLE-02' (str CSV)
  section_anchor='p05---tp---tables-csv' (Unicode)
```

### Config canonique unique (par construction, pas par coincidence)

Smoke et juge importent TOUS DEUX `rag_core.resolve_env_file(ROOT)` :
`Path(os.getenv("RAG_ENV_FILE", str(ROOT / ".env.rag")))`.

Il est IMPOSSIBLE qu'ils divergent : meme fonction, meme ROOT, meme override.

Verification reproductible depuis N'IMPORTE quel ROOT :
```
# Sans override : les deux pointent ROOT/.env.rag
RAG_ENV_FILE unset → resolve_env_file(ROOT) = ROOT/.env.rag

# Avec override : les deux suivent l'override
RAG_ENV_FILE=/custom/path → resolve_env_file(ROOT) = /custom/path
```

Test : `test_env_file_resolution.py` prouve l'egalite sous 3 scenarii
(defaut, override, roots differents).

### Smoke strict + juge run-time interrogent v2

```
RAG_SMOKE_STRICT=1 python3 -m scripts.rag_smoke_test
→ RAG_SMOKE_TEST_OK collection=nsi_corpus_v2 hits=5

search_rag(env, "algorithme de tri", k=2)
→ hits collection=nsi_corpus_v2, source_type=nsi_corpus, anchor=a-savoir
```

Rollback vers nsi_corpus teste (4 logs colles dans les passes anterieures).

### nsi_corpus legacy = 4716

```
curl ... /collections/{nsi_corpus_id}/count → 4716
```

### Korrigo inchange

```
docker inspect --format "{{.Id}}" docker-nginx-1 docker-backend-1 docker-db-1
→ 9a407675aece... 1b6b631318be... 54202b9d02f8...
```

IDs identiques a la reference initiale.

### Collections tierces inchangees

```
rag_education: 7181
rag_francais_premiere: 5948
rag_math_correction: 67
```

## ITEM 1 — CI/hash : FERME

Gate de fraicheur (`make check-generated-freshness`) fonctionne correctement.

**Repro dans le bon sens** (fichier modifie + manifeste stale → gate ECHOUE) :
```
echo "# repro-test-comment" >> scripts/check_rag_collection_policy.py
git commit scripts/check_rag_collection_policy.py  # manifeste inchange
make check-generated-freshness
→ -aa50d5f4... (manifeste committe)
  +130d0c15... (hash recalcule du fichier modifie)
  make: *** [Makefile:23 : check-generated-freshness] Erreur 1
```

Le premier CI run de PR#39 a ECHOUE (run 28549249891, conclusion=failure)
puis le second a PASSE apres commit de la regeneration (run 28549741407).
La divergence 275d595c etait causee par un sed post-regen (proscrit).

## OUVERT

- ITEM 2 : Juge fail-closed sur collection non-interne (risque fonctionnel)
- ITEM 3 : Policy checker AST + matrice adverse
- ITEM 4 : Test du garde-fou enum source_type
- ITEM 5 : capacity_ids / adapt_metadata (dette)
