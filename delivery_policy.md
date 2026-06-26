# Delivery Policy

- Statut : prototype non publiable.

## Archive pédagogique

- Seul livrable pédagogique portable : `dist/source_clean.tar.gz`.
- L’archive principale de livraison est `dist/source_clean.tar.gz`. Toute archive contenant `.git/` est interdite comme livraison pédagogique.
- Ce fichier ne contient ni `.git/`, ni caches, ni artefacts LaTeX, ni environnements virtuels, ni rapports obsolètes.
- `audit-extracted-source` doit passer sur `source_clean.tar.gz` extrait sans dépendance à Git.

## Historique Git

- Livrable technique séparé : `dist/git_bundle.bundle`.
- Ce fichier est transmis uniquement si l'historique est nécessaire.
- Il n'est jamais inclus dans l'archive pédagogique.

## Archives interdites

- `NSI.tar` contenant `.git/` est interdit comme livraison principale.
- `nsi-enseignement.tar` contenant `.git/` est interdit comme livraison pédagogique.
- `NSI.tar.gz` ou tout export contenant `.git/` est interdit.
- Le dossier `.git/` local sert au versionnement de travail, pas à la livraison pédagogique.

## Règles de livraison

- Une livraison n'implique aucun statut `published` et ne remplace pas `release-audit`.
- Pour audit pédagogique : envoyer uniquement `dist/source_clean.tar.gz`.
- Pour historique technique : envoyer `dist/git_bundle.bundle` séparément.
- Ne jamais envoyer une archive contenant `.git/` comme livraison principale.
- Ne pas transmettre `nsi-enseignement.tar` comme livrable pédagogique si ce fichier contient `.git/`.
- Si une archive transmise doit être auditée explicitement, lancer `DELIVERED_ARCHIVE=<chemin> python scripts/check_uploaded_archive_policy.py`.
- Toute archive principale nommée `NSI.tar`, `NSI.tar.gz`, `archive.tar`, `archive.tar.gz` ou équivalent est refusée si elle contient ou peut contenir `.git/`.
