# Audit infrastructure RAG — verite terrain (2026-07-02)

## Statut : BLOCKED_PREFLIGHT — decision du lead requise

## Ambiguite de perimetre (tranchee par preuve)

Le brief FE-01 ordonne de raccorder l'UI au "moteur v2 pgvector 16 892
chunks e5-large 1024d". **Ces termes n'appartiennent PAS a ce depot.**

### Preuves

```
grep -rn 'pgvector|e5.large|resolve_collection_v2|16892|LOT.24' cyranoaladin/NSI
→ AUCUNE occurrence dans le code source ou la documentation originale
  (seules occurrences : l'audit ecrit a la passe precedente)
```

Le vocabulaire du brief (pgvector, e5-large 1024d, LOT 24, resolve_collection_v2,
collections rag_nexus_nsi_*) appartient au depot **cyranoaladin/RAG** :
- ADR-0013 : convergence dual-engine → e5-large 1024d + pgvector (decide)
- LOT 22 : 22 518 chunks ingeres dans pgvector (rag_nexus_nsi_premiere
  7 143 + rag_nexus_nsi_terminale 15 375)
- LOT 25 : cadrage re-ingestion heading-aware

**Conclusion** : le brief FE-01 vise le projet RAG (cyranoaladin/RAG),
pas ce depot (cyranoaladin/NSI). Le raccordement UI → pgvector v2 est
un chantier du depot RAG, pas du depot NSI.

## Etat reel du serveur (chaque ligne adossee a une commande)

### Backend actif = Chroma (pas pgvector)

```
docker exec compose-ingestor-1 env | grep CHROMA
→ CHROMA_HOST=chroma
  CHROMA_PORT=8000

docker exec compose-ingestor-1 env | grep EMBED
→ EMBED_MODEL=nomic-embed-text   (PAS e5-large)

grep "import database|from database|RagDatabase" /app/api.py
→ (vide) — database.py present mais NON IMPORTE par api.py
```

### pgvector : aucune table RAG

```
docker exec infra-postgres-1 psql -U postgres -c "\dt" | grep rag
→ NO_RAG_TABLES

docker exec nexus-postgres-db psql -U postgres -c "\dt" | grep rag
→ NO_RAG_TABLES
```

### Collections Chroma reelles

```
curl .../collections → nsi_corpus: 4716, nsi_corpus_v2: 5992,
  rag_education: 7181, rag_francais_premiere: 5948, rag_math_correction: 67
```

### UI app_v2.py → Chroma

```
docker inspect compose-ui-1 --format "{{.Config.Cmd}}"
→ [streamlit run app_v2.py ...]

docker exec compose-ui-1 env | grep INGEST_API
→ INGEST_API_BASE=http://ingestor:8001   (Chroma backend)
```

### Depot RAG non clone sur le serveur

```
ls /root/RAG /opt/RAG 2>/dev/null → NO_RAG_REPO_ON_SERVER
```

L'image compose-ingestor est buildee, pas un checkout live.

## Options et decision requise (lead/humain)

### Option A — Raccorder l'UI au Chroma v2 EXISTANT

Cible : nsi_corpus_v2 (5992 chunks, nomic 768d, schema canonique).
Deja valide par smoke + juge + barrieres ITEM 1-3.

- Cout : faible (config UI, pas d'infra)
- Risque : faible (meme stack Chroma)
- Limite : ce n'est PAS le "moteur v2" du brief (pas pgvector, pas e5-large,
  pas 22 518 chunks, pas de rerank). Pas de F-01 (citabilite source_label/doc_id
  au sens du LOT 22).
- Isolation : nsi_corpus (legacy) intact, Korrigo inchange

### Option B — Deployer l'infra pgvector v2 (gros perimetre)

Cible : deployer la chaine RAG v2 du depot cyranoaladin/RAG sur le serveur
(pgvector, e5-large, ingestor v2, collections rag_nexus_nsi_*).

- Cout : eleve (tables pgvector, re-ingestion 22 518 chunks, cablage api.py,
  deploiement moteur, UI). Projet infra multi-semaines.
- Risque : eleve (volume partage, Korrigo colocalise, migration embedding)
- C'est le scope du brief FE-01, mais ce n'est pas un chantier de CE depot.

### Option C — Re-aiguiller FE-01 vers cyranoaladin/RAG

Le brief FE-01 parle le vocabulaire du depot RAG. Le raccordement UI → pgvector
v2 devrait etre execute dans le contexte de CE projet, avec ses outils, ses
tests, et sa CI. Sur le depot NSI, le travail de durcissement (ITEM 1-3) est
FAIT et le Chroma v2 est pret.

- Cout : nul sur ce depot ; le travail est dans le depot RAG.
- Risque : clarifier la gouvernance entre les deux depots.
- Sur CE depot : rien a faire au-dela du Chroma v2 deja en place.

## Invariants (ce depot, inchanges)

```
covered : 0
absent : 22
published : 0
validated_* : 0
FINAL_STATUS = NON_RELEASE_READY
```

Aucune ecriture effectuee. Aucun secret affiche. Korrigo inchange.
