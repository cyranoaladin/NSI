# RAG v2 Cutover — Registre final

## CUTOVER CHROMA v2 (prouve, chaque ligne = commande rejouable)

### v2 = 5992 chunks, nomic-embed-text 768d, PII=0

```bash
# Comptes (endpoint Chroma REST v2)
python3 -c "..." # → nsi_corpus_v2: 5992
# Dimension (GET embeddings)
POST /collections/{v2_id}/get {limit:1, include:["embeddings"]} → DIM=768
# PII : ingestion PII_skipped=0 + check_no_private_data: PASS
```

### Metadonnees canoniques (hit reel)

```
POST /search {q:"CSV", collection:"nsi_corpus_v2", k:1}
→ collection='nsi_corpus_v2', source_type='nsi_corpus',
  private_data=False (bool), capacity_ids='P-TABLE-01,P-TABLE-02',
  section_anchor='p05---tp---tables-csv' (Unicode)
```

### Config canonique unique (par construction)

`rag_core.resolve_env_file(ROOT)` importe par smoke ET juge.
Test `test_env_file_resolution.py` : 3 scenarii (defaut/override/roots).
Guard AST anti-inline : `test_no_inline_env_resolution.py` (11 cas).

### Smoke strict + juge run-time sur v2

```
RAG_SMOKE_STRICT=1 → RAG_SMOKE_TEST_OK collection=nsi_corpus_v2 hits=5
search_rag(env, ...) → collection=nsi_corpus_v2, anchor=a-savoir
RAG_COLLECTION=rag_education → REFUS (exit 1)
```

### Isolation

nsi_corpus=4716 (legacy intact), Korrigo IDs identiques, tierces inchangees.

## DURCISSEMENT — TOUS ITEMS CLOS

### ITEM 1 — Config env unifiee + guard AST anti-inline : CLOS

PRs #40-45. resolve_env_file partage, bootstrap sys.path, detecteur AST
(11 cas adverse incl. AugAssign), regle d'arret.

### ITEM 2 — Barrieres juge fail-closed : CLOS

PRs #46-49. Barriere A (allowlist collection {nsi_corpus, nsi_corpus_v2}).
Barriere B (is_internal_hit, source_type=nsi_corpus, isinstance(metadata,dict)).
search_rag : is_internal_hit AVANT doc_type_filter. 14 tests barrieres
(predicats + e2e monkeypatch + metadata malforme). Preuve adverse par copie.

### ITEM 3 — Policy checker AST + matrice adverse : CLOS

PRs #50-52. Checker AST (plus de regex). 19 cas adverse : litteral collection
(tout quote), defaut RAG_COLLECTION (absent/faux/multiple), Barriere A
(is_internal_collection + allowlist + AnnAssign avec valeur), Barriere B
(is_internal_hit + isinstance(metadata,dict) + appel reel scope-borne).
Regle d'arret documentee.

### ITEM 4 — Test enum source_type : CLOS

Guard : `rag_core.extract_metadata` leve `ValueError` si `source_type`
n'est pas dans `{nsi_corpus, golden_example, excluded}` (lignes 118-120).
```bash
grep -n 'VALID_SOURCE_TYPES\|ValueError.*source_type' scripts/rag_core.py
→ 118: VALID_SOURCE_TYPES = {"nsi_corpus", "golden_example", "excluded"}
  119: if source_type not in VALID_SOURCE_TYPES:
  120: raise ValueError(...)
```
Tests : `test_source_type_enum_rejects_invalid` (bogus → ValueError) +
`test_source_type_enum_accepts_all_valid` (3 valeurs acceptees).

### ITEM 5 — adapt_metadata : CLOS (utilitaire conserve)

Decision : `adapt_metadata` n'est sur AUCUN chemin de production (le juge
lit les capacites du frontmatter, pas des hits RAG).
```bash
grep -rn 'adapt_metadata' scripts/ | grep -v 'def adapt_metadata'
→ (vide) — aucun appel en production
```
Conserve comme utilitaire documente avec 2 tests existants
(`test_adapt_metadata_roundtrip` + `test_adapt_metadata_empty`).
Utile pour de futurs consommateurs qui voudraient CSV → liste.

## AUDIT FE-01 — CLOS, REJOUABLE

PRs #53-56. 14 blocs de preuve, chacun rejouable ligne a ligne.
Conclusion nuancee : le brief agrege (1) une transition pgvector inscrite
dans ce depot (rag_connection.md, rag_state_of_truth.md) mais non deployee,
et (2) une chaine e5-large/LOT 22-24/22 518 chunks du depot cyranoaladin/RAG.

Options A (Chroma v2 existant) / B (deployer pgvector, roadmap inscrite) /
C (reaiguiller FE-01 vers RAG) presentees. Decision = lead humain.

## INVARIANTS

```
covered : 0, absent : 22, published : 0, validated_* : 0
FINAL_STATUS = NON_RELEASE_READY
```
