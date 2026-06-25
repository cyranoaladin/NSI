# Cartographie Drive

## Etat

BLOCKER: accès Drive impossible depuis cet environnement.

Action nécessaire : fournir un export zip/tar des dossiers Drive ou monter le Drive localement.

## Conséquence

- Aucune ressource Drive n'est intégrée à ce stade.
- Les ressources générées ne sont pas considérées comme équivalentes à des ressources Drive.
- L'inventaire `drive = 0` reste un bloquant explicite, pas une anomalie masquée.

## Format attendu après fourniture des exports

Chaque ressource Drive devra renseigner :

- `drive_url`
- `drive_folder`
- `file_name`
- `mime_type`
- `local_copy`
- `sha256`
- `niveau`
- `theme`
- `sequence_possible`
- `qualite_initiale`
- `decision`
- `raison`
