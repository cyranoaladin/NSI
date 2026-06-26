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
- `nsi-enseignement.tar`, `nsi-enseignement.tar.gz`, `nsi-enseignement.zip`, `NSI.tar`, `archive.tar`, `archive.tar.gz`, `archive.zip` et toute archive globale équivalente sont refusés comme livrable pédagogique principal.
- `NSI.tar.gz` ou tout export contenant `.git/` est interdit.
- Toute archive contenant `.venv/`, `__pycache__/`, `.pytest_cache/`, `.mypy_cache/`, `.ruff_cache/` ou un fichier `.pyc` est refusée.
- Toute archive globale contenant un sous-dossier `dist/` est refusée comme livraison pédagogique : `dist/source_clean.tar.gz` doit être transmis directement, pas inclus dans une archive du dépôt complet.
- Le dossier `.git/` local sert au versionnement de travail, pas à la livraison pédagogique.

## Règles de livraison

- Une livraison n'implique aucun statut `published` et ne remplace pas `release-audit`.
- Pour audit pédagogique : envoyer uniquement `dist/source_clean.tar.gz`.
- Pour historique technique : envoyer `dist/git_bundle.bundle` séparément.
- Ne jamais envoyer une archive contenant `.git/` comme livraison principale.
- Ne pas transmettre `nsi-enseignement.tar` comme livrable pédagogique si ce fichier contient `.git/`.
- Commande unique de création et vérification du livrable pédagogique :

```bash
make package-audit
DELIVERED_ARCHIVE=dist/source_clean.tar.gz make verify-delivery-archive
```

- Si une archive transmise doit être auditée explicitement, lancer `DELIVERED_ARCHIVE=<chemin> make verify-delivery-archive`.
- Si `DELIVERED_ARCHIVE` pointe vers autre chose que `dist/source_clean.tar.gz`, la livraison est refusée sauf exception documentée dans une politique dédiée.
