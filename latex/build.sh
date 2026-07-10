#!/usr/bin/env bash
# Compile tous les .tex du dossier en PDF (pdflatex, halt-on-error), puis nettoie.
set -uo pipefail
shopt -s nullglob
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
