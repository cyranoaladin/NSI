# Incidents de processus

## Incident 1 : push direct sur main (passe 1)

- Commit : be73955 "Mettre à jour le rapport avec les SHA finaux post-merge"
- Impact : un commit documentation a été poussé directement sur main au lieu de
  passer par PR, violant la règle "merge via GitHub uniquement"
- Contenu : seul `reports/reconciliation/reconciliation_report.md` modifié (SHA)
- Risque : aucun risque technique, mais infraction de processus

## Incident 2 : git commit --amend + force-push (passe 2)

- Branche : audit-verification/report (PR #7)
- Reflog : c3246a2 → 17a9966 (force-push après amend)
- Cause : le rapport contenait un email fictif (`jean.dupont@...`) détecté par
  la CI. Le correctif a été fait par amend au lieu d'un nouveau commit.
- Impact : l'historique de la branche a été réécrit après push, violant la règle
  "commit poussé = immuable"

## Politique adoptée

- Commit poussé = immuable. Toute correction = nouveau commit.
- Merge main via PR GitHub uniquement.
- Aucun `git commit --amend` ni `git rebase` sur un commit déjà poussé.
- Ces incidents sont documentés mais non réversibles (pas de force-push correctif).
