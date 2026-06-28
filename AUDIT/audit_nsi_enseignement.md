# Audit du dépôt `nsi-enseignement` et propositions de production

*Audit conduit sur l'archive `source_clean_tar.gz` (version la plus avancée : scripts et dossiers `code/` supplémentaires, `human_review_wave_1_plan.md` présent, par rapport au `.zip`).*

---

## Partie I — État des lieux factuel

### 1. Ce que le dépôt est réellement

Le dépôt n'est pas un corpus en cours de rédaction : c'est un **système de production de corpus**, doté d'une gouvernance écrite mature (`AGENTS.md`, `SKILLS.md`, `METHODE_PRODUCTION_REELLE.md`), d'un schéma de métadonnées normalisé, d'une source de vérité programme propre, et d'une chaîne de contrôle volumineuse. Le travail de cadrage est de bonne facture. Le problème n'est pas l'intention ni l'architecture déclarée ; il est dans l'écart entre la machinerie et le contenu réellement validé.

Chiffres mesurés sur l'arborescence :

| Élément | Mesure |
| --- | --- |
| Fichiers Markdown | 475 |
| Fichiers Python | 289 (dont 157 scripts, 44 tests) |
| Scripts `check_*` (gates) | 138 |
| LOC de scripts | ~17 000 |
| LOC de tests | ~4 400 |
| Capacités officielles (YAML) | 114 |
| Capacités `covered` | **0** |
| Capacités `needs_review` / `partial` / `absent` | 11 / 4 / 99 |
| Ressources inventoriées (`manifest.csv`) | 813 |
| Ressources publiables | **0** |

### 2. Le constat central : un ratio inversé

Le dépôt comporte environ **21 500 lignes de code de vérification** (gates + tests) pour **0 capacité validée** au sens de ses propres règles. La chaîne de contrôle a grossi plus vite que le contenu qu'elle est censée garder. `METHODE_PRODUCTION_REELLE.md` a déjà diagnostiqué cette pathologie avec lucidité (« le progrès pédagogique net a été nul […] 11 scripts dont l'effet est de faire passer les contrôles sur cet état »). Le diagnostic est juste, mais la cause structurelle persiste : la méthode interdit le comportement sans supprimer ce qui le rend possible.

### 3. Le point le plus important : deux arbres de contenu désynchronisés

Il existe **deux modèles de contenu parallèles**, et la chaîne qualité n'en voit qu'un.

- **Modèle « séquences »** — `premiere/sequences/` et `terminale/sequences/`. Deux séquences pilotes seulement (`s01_representation_donnees`, `s01_structures_donnees_interfaces_implementations`). Contenu **excellent** : situation-problème concrète, formalisation, exemples corrigés vérifiés par opération inverse, prose liée et variée. C'est le standard §6 atteint.
- **Modèle « supports »** — `03_progressions/supports/premiere/P00–P14` et `terminale/T00–T19`, soit **35 unités** couvrant toute la progression, chacune avec 9 à 12 fichiers (cours, td, tp, corrigé, évaluation, barème, trace, remédiation, version aménagée) plus du code typé et des jeux de données. Environ 3,2 Mo de contenu réel.

Or :

- `coverage.md` contient **0 référence** à `supports/`.
- `manifest.csv` contient **444 lignes** référençant `supports/`.

Autrement dit : **la matrice de couverture est aveugle à l'arbre où vit l'essentiel du contenu.** Le « 0/114 covered » ne dit pas qu'il n'y a pas de contenu ; il dit que le contenu existant n'est pas câblé à l'indicateur. C'est la première chose à corriger, et elle ne demande aucune rédaction nouvelle.

### 4. Qualité réelle, par strate

Le contenu n'est pas homogène. Trois strates aux qualités distinctes :

- **Code** — solide. Typage `from __future__ import annotations`, gestion d'erreurs explicite (`ValueError`/`KeyError`), cas limites traités, style idiomatique. Exemple : `P05_corrige_professeur_tables_csv.py` sépare proprement chargement, filtrage, conversion (valides/erreurs), tri à clé composite.
- **Contenu spécifique à la notion** — bon. Les `contracts/*.yml` sont d'excellentes spécifications : `notions_exigibles`, `exemples_obligatoires`, `cas_limites`, `erreurs_frequentes`, `interdits_pedagogiques`, `must_include`/`must_not`. Le scénario `pays_monde.csv` de P05 est concret et vérifiable.
- **Échafaudage pédagogique générique des supports** — **creux et templaté**. La ligne d'objectif « Objectif O1 - Identifier précisément la représentation ou la structure en jeu » apparaît à l'identique dans **108 fichiers**. Le motif « Définition D1 : *X* est utilisé dans *Y* avec une donnée, une règle et un contrôle » est un gabarit à trous : il n'enseigne rien (« table est utilisé dans Traitement de tables avec une donnée, une règle et un contrôle ») et il est **grammaticalement faux** (« est utilisé » sur des noms féminins : table, pile, classe, fonction — 48 occurrences). C'est exactement le « gabarit dupliqué » que la méthode interdit, conservé dans les zones génériques pendant que les zones spécifiques, elles, sont travaillées.

### 5. La différenciation est étiquetée, pas réelle

La `version_amenagee` de P05 reprend **mot pour mot** les mêmes « Objectif O1–O4 » que le cours standard. Le risque anticipé par §5 de la méthode (« trois étiquettes sur le même exercice ») est matérialisé : la différenciation socle/standard/approfondissement est structurellement présente mais pédagogiquement indistincte dans la strate supports.

### 6. La seule porte pédagogique réelle n'a pas été passée à l'échelle

La « porte de substance » (§5 de `METHODE_PRODUCTION_REELLE.md`) — fiche citée par capacité, avec preuve cours / entraînement / correction et verdict — est le **seul contrôle pédagogiquement signifiant** du dépôt. Elle est manuelle, et elle n'a été appliquée qu'aux pilotes (`revue_substance.md` existe pour P-s01). Les 138 gates `check_*` mesurent des proxys (lignes, occurrences de mots-clés, présence de fichiers) ; aucun ne mesure si un élève apprend. Le dépôt confond, à grande échelle, validation technique et validation pédagogique — ce que `AGENTS.md` interdit en toutes lettres (règle 2.8).

---

## Partie II — Diagnostic : trois causes racines

1. **Désynchronisation structurelle.** Deux arbres de contenu, un seul vu par la couverture. Tant que `supports/` et `sequences/` coexistent sans relation explicite, tout indicateur sera faux et tout agent hésitera sur l'endroit où écrire.

2. **Inflation de gates de comptage.** 138 contrôles dont la méthode dit elle-même qu'ils devraient être « indicatifs, non bloquants ». Ils créent l'illusion de rigueur et incitent à produire ce qui les satisfait (fichiers, mots-clés) plutôt que ce qui enseigne. C'est le moteur du « gaming ».

3. **Absence de juge de substance automatisable.** Le seul contrôle qui compte est manuel et ne scale pas. Sans un juge de substance reproductible, on ne peut ni valider 114 capacités, ni détecter le boilerplate, ni mesurer la différenciation réelle.

---

## Partie III — Architecture cible et workflows agentiques

### Proposition 0 — Unifier en une source de vérité unique (préalable, sans rédaction)

Décider d'un seul arbre canonique. Recommandation : **promouvoir le modèle « supports » par unité (P00–T19) comme canon**, car il couvre déjà toute la progression, et **rétrograder `sequences/` au rang de gabarit de référence** (les deux pilotes deviennent les *golden examples* du standard §6).

Action immédiate, purement mécanique :
- Étendre `check_program_coverage.py` pour indexer `03_progressions/supports/**` via les `contracts/*.yml` (qui portent déjà `capacites_officielles`). La couverture passera mécaniquement de 0 à la réalité (probablement 60–80 % en `partial`/`needs_review`), sans écrire une ligne de cours.
- Geler `premiere/sequences/` et `terminale/sequences/` comme `reference/` (gabarits), pour qu'aucun agent n'y écrive plus de contenu de production.

Bénéfice : l'indicateur redevient vrai. On ne peut piloter que ce qu'on mesure correctement.

### Proposition 1 — Le juge de substance LLM (le cœur du dispositif)

Remplacer l'inflation de gates de comptage par **un seul gate pédagogique automatisé mais non-comptable** : un agent-juge LLM qui exécute la porte de substance §5 par capacité, et rend un verdict structuré cité.

Principe : le juge reçoit (a) l'intitulé officiel exact de la capacité depuis `programme_nsi_2019.yaml`, (b) le contrat de l'unité, (c) les extraits cours/td/tp/corrigé pertinents. Il produit la fiche §5 en sortie JSON stricte (verdict + citations + ancres), jamais un score numérique. La sortie JSON est versionnée à côté de l'unité (`P05/_substance_review.json`).

Garde-fous anti-complaisance du juge (essentiels, sinon le juge devient un nouveau tampon vert) :
- **Citation obligatoire et vérifiable** : chaque « oui » doit pointer une ancre réelle ; un script léger vérifie *a posteriori* que l'ancre existe dans le fichier (contrôle mécanique de l'existence, pas du sens).
- **Juge ≠ auteur** : l'instance qui rédige ne juge jamais sa propre production (rôles séparés, contextes séparés).
- **Échantillon adverse** : injecter périodiquement une unité volontairement creuse (le boilerplate « Définition D1 ») ; si le juge la valide, le juge est recalibré. C'est un test du test.
- **Verdict par défaut = `needs_content`**, jamais `validated_pedagogy` en l'absence de preuve.

Ce gate-là peut être bloquant, parce qu'il mesure la substance, pas un proxy. Les 138 autres redeviennent indicatifs.

### Proposition 2 — Pipeline agentique multi-rôles piloté par contrat

Le `contract.yml` est déjà la bonne abstraction. L'industrialiser comme **entrée unique d'un pipeline d'agents spécialisés**, chacun avec un périmètre fermé et un livrable vérifiable (les rôles existent déjà dans `AGENTS.md` §4 ; il s'agit de les rendre exécutables et chaînés) :

1. **Agent Cadrage** — lit le contrat + le YAML programme, écrit les métadonnées et la liste des capacités atomiques visées. Ne rédige pas.
2. **Agent Auteur** — rédige cours/trace/td/tp/fiche_methode en prose liée (§6), en consommant `exemples_obligatoires`, `cas_limites`, `erreurs_frequentes` du contrat. Reçoit les deux pilotes comme *few-shot*.
3. **Agent Code** — écrit `code/` + `tests/`, exécute les tests, refuse de livrer si rouge.
4. **Agent Évaluation** — produit évaluation/corrigé/barème/grille/qcm, chaque question rattachée à une capacité atomique.
5. **Agent Différenciation** — produit trois variantes *réellement distinctes* (cf. Proposition 5).
6. **Agent Scientifique** — vérifie définitions, algorithmes, complexités, sans approximation non signalée.
7. **Agent Juge de substance** (Proposition 1) — verdict bloquant.
8. **Agent Rendu** — PDF/HTML chartés élève + prof.

Chaque agent ne consomme que les sorties écrites de l'amont (jamais des références à des fichiers absents — interdit §3.1 de la méthode). Orchestration par `Makefile` cible `make unit U=P05` qui enchaîne les étapes et s'arrête au premier livrable manquant.

### Proposition 3 — Génération *contract-first* avec *golden examples*

La cause du boilerplate est la génération sans ancrage. La corriger par deux leviers :

- **Le contrat comme prompt structuré.** Un contrat riche (P05 l'est déjà) donne assez de matière spécifique pour interdire le générique. Auditer d'abord les 35 contrats et combler les pauvres avant toute rédaction : un bon contrat vaut dix gates.
- **Les pilotes comme référence de style.** Injecter `s01` Première/Terminale comme exemples positifs, et un extrait de boilerplate (« Définition D1 : … est utilisé dans … ») comme **exemple négatif explicite**. L'agent apprend la frontière par contraste, pas par règle abstraite.

Test d'acceptation de l'auteur (mécanisable) : un document est rejeté si l'un de ses paragraphes a une **similarité > seuil** avec le même paragraphe d'une autre unité (détection de duplication inter-unités par n-grammes ou embeddings). C'est le contrôle qui aurait attrapé les 108 « Objectif O1 » identiques.

### Proposition 4 — Dégonfler la dette de gates

Passer de 138 gates `check_*` à un noyau d'une quinzaine, en trois familles seulement :

- **Bloquants de structure** (existence des fichiers obligatoires, métadonnées complètes, liens internes valides, absence de données privées, tests Python verts) — déterministes, rapides.
- **Bloquant de substance** (le juge §5, Proposition 1) — le seul gate pédagogique bloquant.
- **Indicateurs non bloquants** (volumétrie, occurrences de mots-clés, profondeur d'évidence) — rapportés dans un tableau de bord, jamais en `KO`.

Archiver les autres dans `scripts/_legacy/` avec une note. La méthode l'exige déjà (§10 : « Les gates de comptage : repassés en indicatif, non bloquant »). Il reste à l'exécuter.

### Proposition 5 — Différenciation réellement distincte, vérifiée

Définir trois profils opérationnels et les imposer au contrat :
- **socle** : même capacité, données réduites, étapes pré-découpées, un cas au lieu de plusieurs ;
- **standard** : le cas nominal complet ;
- **approfondissement** : extension hors-piste contrôlée (preuve d'invariant, complexité, variante d'implémentation).

Contrôle d'acceptation : les trois variantes doivent différer sur la **consigne et le jeu de données**, pas seulement sur l'en-tête. Mécanisable par comparaison de similarité entre `version_amenagee`, cours standard et extension : au-delà d'un seuil, rejet. C'est ce qui aurait attrapé la `version_amenagee` de P05 (objectifs recopiés).

### Proposition 6 — Rendu charté automatisé, livrable prouvé

La charte doit apparaître **sur le livrable**, pas seulement dans un `.tex` (méthode §4.8). Pipeline `md → PDF/HTML` charté (Pandoc + template LaTeX/CSS porteur de la charte du dépôt), avec deux variantes systématiques : **élève** (sans corrigé) et **prof** (avec corrigé, barème, grille). Le gate de rendu vérifie que les deux PDF existent et portent l'en-tête charté (présence d'un marqueur dans le PDF), bouclant la définition de « séquence rendue » du §2.

---

## Partie IV — Idées « out of the box »

### A. Le RAG pédagogique comme oracle de cohérence inter-séquences

Le projet RAG (e5 multilingue, pgvector) peut servir d'**oracle de cohérence transversale** sur ce corpus. Indexer tout le corpus produit, puis interroger : « la notion de *complément à deux* est-elle définie de façon cohérente entre P01, P05 et les évaluations ? », « un prérequis cité en T09 est-il bien enseigné en amont ? ». Le RAG détecte les **incohérences de définition, les prérequis non couverts et les redites** mieux qu'un script de mots-clés. C'est un contrôle de cohérence sémantique, pas lexical — exactement ce qui manque entre les 35 unités.

### B. Property-based testing pédagogique

Traiter chaque capacité comme une **propriété vérifiable** plutôt qu'une case à cocher. Pour les capacités algorithmiques (tris, dichotomie, kNN, glouton), le `code/` de l'unité doit passer des tests *property-based* (Hypothesis) : un tri produit une permutation triée pour toute entrée aléatoire ; une dichotomie trouve l'élément ssil est présent. La capacité n'est `validated_technical` que si la propriété tient sur des centaines d'entrées générées, pas sur trois exemples choisis. Cela transforme « le corrigé semble correct » en « le corrigé est correct sous test ».

### C. L'élève simulé adverse (test final §6)

Le test ultime de la méthode est : « l'élève doit pouvoir apprendre, s'entraîner et se corriger seul avec le document ». Le mécaniser par un **agent-élève** qui ne reçoit *que* le cours élève (sans corrigé) et doit résoudre le TD/TP. S'il échoue là où un élève de niveau standard devrait réussir, le document a un trou : prérequis implicite, étape manquante, exemple insuffisant. Le rapport d'échec de l'élève simulé est un signal de qualité pédagogique impossible à « gamer » avec des mots-clés.

### D. Banque de questions paramétrée plutôt que QCM figés

Remplacer les `qcm.json` statiques par des **générateurs** (`qcm_gen.py`) qui produisent des familles de questions paramétrées (convertir *n* en base *b*, dresser la table de *expr booléenne*) avec corrigé calculé. Avantages : sujets uniques par élève (anti-triche, cohérent avec ton travail sur `eval_maths_term`), réutilisation entre années, et vérifiabilité automatique du corrigé (le générateur connaît la réponse). Chaque générateur est rattaché à une capacité atomique.

### E. Le graphe de traçabilité capacité → preuve

Matérialiser la couverture non comme un tableau plat mais comme un **graphe** : capacité officielle → preuve cours → preuve entraînement → preuve correction → question d'évaluation. Un nœud sans arête entrante de chaque type est `partial` par construction, sans jugement humain. Ce graphe se génère depuis les `evidence` déjà présents dans les frontmatters (le pilote P-s01 a déjà la structure `official_program.capacities[].evidence[]`). Rendu en `INDEX.md` cliquable, il devient l'outil de pilotage qui dit, d'un coup d'œil, où sont les trous réels.

### F. La CI comme examinateur de bac blanc

Boucler le système sur lui-même : une cible `make bac-blanc` qui assemble, depuis les banques validées, un sujet type bac (écrit + pratique), le fait résoudre par l'agent-élève, et vérifie que le barème généré et le corrigé sont cohérents et résolubles dans le temps imparti. Un corpus qui produit un sujet d'examen cohérent et faisable est, par construction, un corpus qui couvre le programme — c'est la preuve d'intégration la plus forte possible, et elle rejoint directement ton workflow de correction BAC NSI.

---

## Partie V — Plan d'exécution séquencé

L'ordre importe : d'abord rendre les indicateurs vrais, ensuite produire, jamais l'inverse.

1. **Réconciliation (0 rédaction).** Étendre la couverture à `supports/` via les contrats ; geler `sequences/` en `reference/`. Résultat : couverture réelle affichée.
2. **Dégonflage des gates.** Réduire à ~15 gates, reclasser le comptage en indicatif, archiver le reste.
3. **Juge de substance.** Implémenter l'agent §5 + vérification mécanique des ancres + test adverse. Le faire tourner sur les 2 pilotes pour calibrer, puis sur les 35 unités. Résultat : première carte honnête des `validated` / `needs_content`.
4. **Audit des 35 contrats.** Enrichir les contrats pauvres. Détecter et purger le boilerplate inter-unités (similarité > seuil, dont les 48 définitions fautives).
5. **Reprise unité par unité, dans l'ordre de la progression.** Pour chaque unité : agent Auteur (few-shot pilotes) → Code (property-based) → Évaluation → Différenciation distincte → Scientifique → Juge → Rendu charté. Une unité terminée au sens §7 avant la suivante.
6. **Cohérence transversale.** Brancher le RAG-oracle (idée A) et le graphe de traçabilité (idée E) une fois 5–6 unités validées, pour vérifier la cohérence inter-séquences au fil de l'eau.
7. **Preuve d'intégration.** Une fois la couverture substantielle, `make bac-blanc` (idée F) comme test de bout en bout.

Le rapport d'avancement, conformément à la méthode, ne donne que deux nombres : **capacités `validated_pedagogy` avec preuve citée** et **unités rendues (PDF élève + prof chartés)**. Aucun décompte de gates verts.

---

## Synthèse en une phrase

Le dépôt a un excellent contenu sous-évalué (35 unités invisibles à la couverture), un cadrage de qualité, et une chaîne de contrôle hypertrophiée qui mesure des proxys ; le levier décisif n'est pas de produire davantage mais de **réconcilier les deux arbres, remplacer 138 gates de comptage par un seul juge de substance automatisé mais non-comptable, et industrialiser la génération contract-first ancrée sur les deux pilotes comme références de style.**
