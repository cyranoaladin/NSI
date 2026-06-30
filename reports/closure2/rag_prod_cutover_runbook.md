# Runbook de cutover production RAG

## Statut : PLAN SEULEMENT — exécution interdite

## Prérequis

- Accès SSH au serveur (88.99.254.59, host korrigo)
- .env.rag avec RAG_API_KEY valide
- Timeout /search résolu (actuellement le endpoint time out)
- Pipeline d'ingestion validé en local (Phase B3)
- Approbation du chef de projet

## Étape 1 : Backup

```bash
ssh korrigo "docker exec chroma tar cf /backup/chroma_$(date +%Y%m%d).tar /chroma/chroma"
```

Jamais de drop de collection. Le backup est le prérequis absolu.

## Étape 2 : Collection STAGING

Créer une collection staging `nsi_corpus_staging` :
```bash
python -m scripts.rag_ingest --collection nsi_corpus_staging --dry-run
python -m scripts.rag_ingest --collection nsi_corpus_staging
```

Vérifier le schéma canonique sur les hits staging.
Vérifier le filtrage level/theme/capacity_ids.

## Étape 3 : Validation staging

```bash
RAG_COLLECTION=nsi_corpus_staging python -m scripts.rag_smoke_test
```

Critère : RAG_SMOKE_TEST_OK, métadonnées canoniques sur tous les hits.

## Étape 4 : Reindex complet

```bash
python -m scripts.rag_ingest --collection nsi_corpus --reindex
```

## Étape 5 : Cutover UI

Mettre à jour la collection par défaut dans rag-ui.nexusreussite.academy
de nsi_corpus (legacy) vers nsi_corpus (reindexé schéma canonique).

## Étape 6 : Vérification post-cutover

```bash
make rag-smoke-required   # doit PASSER
python -m scripts.rag_diagnose_search_timeout  # aucun timeout
```

## Rollback

Si échec à toute étape :
1. Restaurer le backup : `docker exec chroma tar xf /backup/chroma_YYYYMMDD.tar -C /`
2. Redémarrer : `docker restart chroma ingestor`
3. Vérifier : `curl -sS $RAG_API_BASE_URL/../health`

## Fenêtre d'impact

Pendant la réindexation (~5 min) : /search retourne 0 résultats.
Aucun impact utilisateur final (RAG non exposé publiquement).

## make rag-smoke-required

Reste en échec tant que le cutover n'est pas exécuté. Prod inchangée.
