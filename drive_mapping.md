# Cartographie Drive

## État

Les liens Drive fournis sont accessibles via le connecteur Google Drive.

Cette passe référence des dossiers et ressources de premier niveau ou des échantillons représentatifs.

Aucune ressource Drive n'est copiée localement dans le corpus.

Aucune ressource Drive n'est déclarée publiable.

## Statut de release

NON PASSANT pour publication.

Raison : les ressources Drive sont référencées mais non intégrées, non anonymisées et non relues.

`check_drive_mapping.py` accepte cet état pour un prototype.

`check_drive_mapping_release.py` échoue tant que `local_copy` reste `NA_REMOTE_NOT_DOWNLOADED`.

## Points sensibles détectés

- Dossiers `rendus_eleves`.
- Dossiers `.git`.
- Dossiers `.venv`.
- Fichiers `NotesEleves.csv`.
- Fichiers `Fichier_Eleves.csv`.
- Corrigés mélangés avec sujets.
- Dossiers `Groupes`.

## Décisions initiales

- `reuse` : aucune ressource à ce stade.
- `refactor` : ressources pédagogiques potentielles à analyser.
- `archive` : ressources utiles mais non publiables telles quelles.
- `reject` : données élèves, artefacts techniques ou dossiers sensibles.

## Limite

Le listing n'est pas récursif.

La prochaine action Drive doit être un export contrôlé, anonymisé et hashé, ou une ingestion récursive dédiée avec séparation des données élèves.
