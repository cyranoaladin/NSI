# Juge de substance NSI — prototype

Transforme la **porte de substance §5** de `METHODE_PRODUCTION_REELLE.md` en gate
reproductible : un agent-juge LLM rend un verdict cité par capacité, et un
vérificateur mécanique constate que les preuves citées existent vraiment. C'est
le **seul gate pédagogique bloquant** destiné à remplacer une large part des
138 gates de comptage du dépôt.

Principe directeur : le juge dit la vérité sur ce que l'unité enseigne ; le
vérificateur n'a aucun avis pédagogique mais un **droit de veto** sur les preuves
invérifiables. Il ne promeut jamais un verdict, il peut seulement le dégrader.

## Contenu

| Fichier | Rôle |
| --- | --- |
| `schema/substance_verdict.schema.json` | Schéma JSON strict de la sortie du juge (3 preuves par capacité, verdict ∈ {validated_pedagogy, needs_content, BLOCKER}). |
| `prompts/substance_judge.system.md` | Prompt système du juge, avec garde-fous anti-complaisance et anti-gabarit. |
| `prompts/substance_judge.user_template.md` | Gabarit du message utilisateur (table des ancres + texte intégral). |
| `run_substance_judge.py` | Orchestrateur : assemble le prompt depuis une unité, appelle le juge, écrit le verdict. `--dry-run` fonctionne hors-ligne. |
| `check_substance_anchors.py` | Vérificateur d'ancres et de citations. Le veto mécanique. |
| `slug.py` | Slugifieur d'ancres style GitHub, validé 11/11 contre les ancres réelles du dépôt. |
| `examples/*.verdict.json` | Un verdict valide et un verdict empoisonné, pour tester les deux chemins. |

## Ce que le vérificateur contrôle

1. conformité au schéma JSON (si `jsonschema` est installé) ;
2. concordance de `official_label` avec `programme_nsi_2019.yaml` ;
3. existence du fichier de chaque preuve `present` ;
4. existence réelle de l'`anchor` (slug recalculé depuis les titres, sous-sections incluses) ;
5. présence **littérale** de la `quote` dans la section (exacte / normalisée / approximative ≥ 85 % / absente) ;
6. cohérence : `validated_pedagogy` exige 3 preuves vérifiées **et** `teaches=true` **et** aucun `scientific_flag` ;
7. signal si `judge_model == author_model` (séparation des rôles).

Tout `validated_pedagogy` non soutenu est **dégradé** en `needs_content`, motif rapporté.

## Démo (sur le dépôt extrait)

```bash
pip install jsonschema            # facultatif mais recommandé
REPO=/chemin/vers/nsi-enseignement

# chemin valide : 3 citations réelles -> validated_pedagogy, code retour 0
python check_substance_anchors.py examples/s01_premiere.valid.verdict.json --repo-root "$REPO"

# chemin empoisonné : ancre fausse + citations hallucinées + label faux
# -> dégradé en needs_content, code retour 1
python check_substance_anchors.py examples/s01_premiere.poisoned.verdict.json --repo-root "$REPO"
```

## Boucle complète

```bash
# 1. assembler le prompt et juger (brancher call_judge sur l'API au préalable)
python run_substance_judge.py --unit P05 --level premiere --repo-root "$REPO" \
    --out P05/_substance_review.json

# 2. veto mécanique (bloquant en CI)
python check_substance_anchors.py P05/_substance_review.json --repo-root "$REPO"
```

Pour inspecter le prompt sans appeler de modèle : ajouter `--dry-run`.

## Intégration Makefile (proposition)

```makefile
REPO ?= .
JUDGE := python substance_judge/check_substance_anchors.py

# gate bloquant : vérifie tous les verdicts produits
substance-gate:
	@status=0; \
	for v in $$(find $(REPO) -name '_substance_review.json'); do \
	  $(JUDGE) $$v --repo-root $(REPO) || status=1; \
	done; \
	exit $$status

# juger une unité : make judge U=P05 LVL=premiere
judge:
	python substance_judge/run_substance_judge.py --unit $(U) --level $(LVL) \
	  --repo-root $(REPO) --out $(REPO)/$(U)/_substance_review.json
	$(JUDGE) $(REPO)/$(U)/_substance_review.json --repo-root $(REPO)
```

## Garde-fous contre la complaisance du juge

Le juge reste un modèle ; il peut être trop indulgent. Trois protections, dont
deux déjà mécanisées ici :

- **citation vérifiée** : une preuve dont la citation est introuvable est
  invalidée quoi qu'en dise le juge (mécanisé) ;
- **séparation juge/auteur** : le verdict porte `judge_model` et `author_model` ;
  l'égalité est signalée (mécanisé) ;
- **test adverse** : faire juger périodiquement une unité volontairement creuse
  (p. ex. le gabarit « Définition D1 : X est utilisé dans Y… ») ; si le juge la
  valide, recalibrer le prompt. Le verdict empoisonné fourni sert d'amorce à ce
  test (à automatiser dans la CI).

## Notes d'implémentation

- Slug GitHub : minuscule, accents conservés, ponctuation supprimée, tirets
  multiples non fusionnés (« Réponse attendue — TD » → `#réponse-attendue--td`),
  doublons suffixés `-1`, `-2`. Validé contre les ancres réelles des pilotes.
- Une section englobe ses sous-sections : citer `#exercices` couvre une preuve
  située dans `### Exercice 1`.
- Aucune dépendance externe pour le vérificateur hormis `jsonschema`
  (facultatif). Le parsing du YAML programme est tolérant et sans PyYAML.
```
