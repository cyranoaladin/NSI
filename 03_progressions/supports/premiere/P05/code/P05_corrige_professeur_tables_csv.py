"""Asset Python TP. Statut pédagogique: needs_review."""

from __future__ import annotations

def filtrer_table(rows):
    if rows is None:
        raise ValueError("table absente")
    valides = []
    erreurs = []
    for row in rows:
        try:
            age = int(row.get("age", ""))
        except ValueError:
            erreurs.append(row)
            continue
        if age >= 16:
            valides.append(dict(row, age=age))
    return {"valides": valides, "erreurs": erreurs}
