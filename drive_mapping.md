# Cartographie Drive

## État

Les ressources Drive sont traitées depuis le miroir local `Documents_DRIVE`, résolu par `NSI_DOCUMENTS_DRIVE_ROOT` ou par le dossier `../Documents_DRIVE` voisin du dépôt.

Cette passe ne publie aucune ressource. Elle classe chaque ligne de `drive_inventory.csv` et trace les reprises effectives dans `support_source_trace.yml`.

## Synthèse de décision

- `integrated_adapted` : ressource locale adaptée dans un support existant, sans copie brute et avec hash.
- `inspiration_only` : ressource locale consultée comme inspiration, sans reprise dans un support.
- `rejected_sensitive` : ressource exclue pour donnée personnelle probable ou artefact technique.
- `missing_local_copy` : copie locale absente ; contenu non inventé.
- `deferred` : copie locale trouvée mais audit pédagogique/RGPD différé.
- `quarantined` : ressource à isoler avant toute reprise.

## Ressources effectivement adaptées

- `1_RdD_Entier naturel.pdf` → enrichissement de `premiere/sequences/s01_representation_donnees/cours_eleve.md`.
- `pays_monde.csv` → extrait non personnel et supports P05 tables CSV.
- `types_construits_python-v2.pdf` → fiche P04 tuples/types construits.
- `Séquence1_TAD_Théorie` → fiche T01 interface/TAD.
- `Séquence17_Boyer-Moore` → fiche T18 Boyer-Moore.

## Ressources refusées

- `rendus_eleves`
- `.git`
- `.venv`
- `NotesEleves.csv`
- `Fichier_Eleves.csv`

## Statut de release

`check_drive_mapping.py` accepte l’état prototype car les ressources sont classées et tracées.

`check_drive_mapping_release.py` reste bloquant tant que des ressources sont `missing_local_copy`, `deferred`, `quarantined` ou `rejected_sensitive`, et tant que les revues humaines et décisions de publication manquent.

FINAL_STATUS = NON_RELEASE_READY.
