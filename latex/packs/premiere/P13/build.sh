#!/usr/bin/env bash
# Compile tous les .tex du pack en PDF (pdflatex, halt-on-error), puis nettoie.
# nsi-preamble.sty provient de la source unique 02_modeles_documents/.
set -uo pipefail
shopt -s nullglob

# Remonter vers la racine du dépôt pour trouver 02_modeles_documents/
PACK_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$PACK_DIR/../../../.." && pwd)"
export TEXINPUTS="${REPO_ROOT}/02_modeles_documents:${TEXINPUTS:-}"

fail=0
for tex in *.tex; do
  printf '→ %-32s ' "$tex"
  if pdflatex -interaction=nonstopmode -halt-on-error "$tex" >/dev/null 2>&1; then
    echo "✓ ${tex%.tex}.pdf"
  else
    echo "✗ ÉCHEC — relancer : pdflatex $tex"
    fail=1
  fi
done
rm -f ./*.aux ./*.log ./*.out ./*.toc
exit $fail
