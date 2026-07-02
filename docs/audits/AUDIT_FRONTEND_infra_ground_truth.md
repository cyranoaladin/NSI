# Audit infrastructure RAG — verite terrain (corrige 2026-07-02)

## Statut : BLOCKED_PREFLIGHT — decision du lead requise

## Ambiguite de perimetre (tranchee par preuve corrigee)

Le brief FE-01 ordonne de raccorder l'UI au "moteur v2 pgvector 16 892
chunks e5-large 1024d, resolve_collection_v2, LOT 24". Certains de ces
termes existent dans ce depot, d'autres non.

### Preuves par terme (commandes correctes, par terme separe)

**pgvector** — PRESENT dans le depot originel :
```
rg -n pgvector *.md reports/ docs/
→ rag_connection.md:17: trajectoire Nexus : rag-pedago -> pgvector -> retrieval HMAC
  reports/closure2/rag_state_of_truth.md:50: Transition vers pgvector documentee mais non deployee
```
pgvector est une TRANSITION documentee dans ce depot, pas un vocabulaire etranger.
Elle n'a jamais ete deployee (database.py present dans le conteneur, NON cable).

**e5-large** — ABSENT du depot originel :
```
rg -n 'e5[-_.]?large' *.md scripts/ reports/ docs/
→ (vide hors AUDIT_FRONTEND_*.md, texte de l'audit precedent)
```

**resolve_collection_v2** — ABSENT du depot originel :
```
rg -n resolve_collection_v2 scripts/ *.md reports/ docs/
→ (vide hors AUDIT_FRONTEND_*.md)
```

**16 892 / 22 518** — ABSENTS du depot originel :
```
rg -n '16.?892|22.?518' *.md scripts/ reports/ docs/
→ (vide hors AUDIT_FRONTEND_*.md)
```
Le "16 892" du brief ne correspond a AUCUN compte reel verifie :
ni Chroma (4716 / 5992) ni pgvector LOT 22 (22 518). Chiffre non source.

**LOT 24 / rag_nexus_nsi** — ABSENTS du depot originel :
```
rg -n 'LOT[ ._-]?24' *.md scripts/ reports/ docs/
rg -n rag_nexus_nsi *.md scripts/ reports/ docs/
→ (vide hors AUDIT_FRONTEND_*.md)
```
Present dans cyranoaladin/RAG (ADR-0013, LOT 22 = 22 518 chunks pgvector).

### Conclusion nuancee

Le brief FE-01 agrege DEUX realites :
1. **pgvector** : transition documentee dans CE depot (rag_connection.md,
   rag_state_of_truth.md) mais JAMAIS deployee sur le serveur.
2. **e5-large 1024d / LOT 22-24 / 22 518 chunks / resolve_collection_v2 /
   rag_nexus_nsi_*** : chaine qui vit dans cyranoaladin/RAG, absente de ce depot.

L'ambiguite n'est pas "mauvais depot" simple : c'est un brief qui agrege
une roadmap non executee de CE depot et une chaine operationnelle d'un AUTRE.

## Etat reel du serveur (chaque ligne = commande collee)

### Backend actif = Chroma (pas pgvector)

```
docker exec compose-ingestor-1 env | grep CHROMA
→ CHROMA_HOST=chroma, CHROMA_PORT=8000

docker exec compose-ingestor-1 env | grep EMBED
→ EMBED_MODEL=nomic-embed-text   (PAS e5-large)

docker exec compose-ingestor-1 grep "import database" /app/api.py
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
nsi_corpus: 4716
nsi_corpus_v2: 5992
rag_education: 7181
rag_francais_premiere: 5948
rag_math_correction: 67
```

### UI app_v2.py → Chroma

```
docker inspect compose-ui-1 --format "{{.Config.Cmd}}"
→ [streamlit run app_v2.py ...]

INGEST_API_BASE=http://ingestor:8001 (Chroma backend)
```

## Options et decision requise (lead/humain)

### Option A — Raccorder l'UI au Chroma v2 EXISTANT

Cible : nsi_corpus_v2 (5992 chunks, nomic 768d, schema canonique).
Valide par smoke + juge + barrieres ITEM 1-3.

- Cout : faible (config UI)
- Risque : faible (meme stack Chroma)
- Limite : ne fournit PAS e5-large/rerank/22 518 chunks. Pas de F-01
  (citabilite source_label/doc_id au sens du LOT 22).

### Option B — Deployer l'infra pgvector (transition inscrite ici)

Ce n'est PAS "hors sujet" : la transition pgvector est documentee
dans rag_connection.md et rag_state_of_truth.md de CE depot. La deployer
serait la CONCRETISATION d'une roadmap existante.

- Cout : eleve (tables, migration, cablage api.py, modele d'embedding).
  La chaine e5-large/rerank/22 518 chunks vient du depot RAG et
  necessiterait un pont entre les deux projets.
- Risque : eleve (volume partage, Korrigo colocalise)

### Option C — Reaiguiller FE-01 vers cyranoaladin/RAG

La partie e5-large/LOT 22-24/22 518 chunks vit dans le depot RAG.
Le raccordement UI → cette chaine devrait etre pilote depuis CE projet.
Sur CE depot, le Chroma v2 est pret (option A).

- La partie pgvector a un pied dans ce depot (roadmap documentee).
- La partie e5-large/LOT est entierement dans l'autre.

## Invariants (ce depot, inchanges)

```
covered : 0
absent : 22
published : 0
validated_* : 0
FINAL_STATUS = NON_RELEASE_READY
```

Aucune ecriture effectuee. Aucun secret affiche. Korrigo inchange.
