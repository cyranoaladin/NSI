# RAG v2 Cutover — Etat de verite

## PROUVE (re-verifie par commande)

- nsi_corpus_v2 = 5992 chunks, nomic-embed-text 768d, PII=0
- Metadonnees canoniques : collection=nsi_corpus_v2, source_type=nsi_corpus (KIND),
  private_data=False (bool), capacity_ids CSV, section_anchor Unicode
- Config canonique unique : /tmp/nsi_ingest/.env.rag, lu par smoke ET juge
  (readlink prouve passes anterieures)
- Smoke strict + juge run-time interrogent v2 ; rollback vers nsi_corpus teste
- nsi_corpus legacy = 4716, intact (source de rollback)
- Korrigo inchange (IDs conteneurs identiques)
- Collections tierces inchangees (rag_education=7181, rag_francais_premiere=5948,
  rag_math_correction=67)

## ITEM 1 — CI/hash : FERME

Le gate de fraicheur (`make check-generated-freshness`) fonctionne correctement :
- Il regenere TOUS les reports (y compris manifest_tooling.csv avec hashes recalcules)
- Puis `git diff --exit-code` detecte toute divergence commitee

La divergence 275d595c→aa50d5f4 de la passe anterieure etait causee par un `sed`
de reformatage APRES regeneration (anti-pattern desormais proscrit). Le premier CI
run sur la PR #39 a ECHOUE au gate de fraicheur (run 28549249891), puis le second
run a PASSE apres commit de la regeneration correcte (run 28549741407).

Preuve de repro : mutation manuelle d'un hash → regen → le hash correct est
restaure automatiquement → si committe avec le hash mute, git diff l'aurait
detecte. Le gate n'est PAS fail-open.

## OUVERT

- ITEM 2 : Juge fail-closed sur collection non-interne (risque fonctionnel)
- ITEM 3 : Policy checker AST + matrice adverse
- ITEM 4 : Test du garde-fou enum source_type
- ITEM 5 : capacity_ids / adapt_metadata (dette)
