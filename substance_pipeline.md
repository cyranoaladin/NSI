# Pipeline de substance

## Doctrine

Le pipeline de substance distingue strictement deux rôles.

## System A - autorité

`scripts/check_substance_anchors.py` et `substance_verdict.schema.json` forment
le système d'autorité. System A vérifie mécaniquement les fichiers, ancres,
citations et cohérences déclarées.

System A ne promeut jamais un verdict. Il peut seulement accepter un verdict
déjà correctement soutenu ou le dégrader.

## System B - proposeur

`scripts/substance_judge.py` est un proposeur outillé par RAG/LLM. Il produit des
propositions au format de System A, puis elles doivent passer par le veto de
System A.

System B ne peut jamais écrire `validated_pedagogy` comme verdict final. Ses
propositions sont limitées à `needs_content` ou `needs_review`, avec preuves
citées, ancres et chemins vérifiables.

## Relecture humaine

Une promotion ultérieure exige à la fois:

- un verdict conforme au schéma System A;
- une vérification mécanique par System A;
- une confirmation relecteur conforme à `reviewer_confirmation.schema.json`.

Sans cette confirmation, `validated_* = 0`, `covered = 0` et `published = 0`.
