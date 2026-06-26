"""Corrigé professeur TP P05. Statut pédagogique: needs_review."""

from __future__ import annotations


def filtrer_par_continent(rows, continent):
    if rows is None:
        raise ValueError("table absente")
    if not continent:
        raise ValueError("continent absent")
    return [row for row in rows if row.get("CONTINENT") == continent]


def populations_valides(rows):
    if rows is None:
        raise ValueError("table absente")
    valides = []
    erreurs = []
    for row in rows:
        try:
            population = int(row.get("POPULATION", ""))
        except ValueError:
            erreurs.append(row)
            continue
        valides.append(dict(row, POPULATION=population))
    return valides, erreurs


def trier_par_continent_population(rows):
    valides, _ = populations_valides(rows)
    return sorted(valides, key=lambda row: (row["CONTINENT"], -row["POPULATION"], row["PAYS"]))
