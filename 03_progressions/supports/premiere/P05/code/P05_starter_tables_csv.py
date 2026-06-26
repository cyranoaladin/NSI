"""Starter TP P05. Statut pédagogique: needs_review."""

from __future__ import annotations


def filtrer_par_continent(rows, continent):
    if rows is None:
        raise ValueError("table absente")
    if not continent:
        raise ValueError("continent absent")
    return []


def populations_valides(rows):
    if rows is None:
        raise ValueError("table absente")
    return [], []


def trier_par_continent_population(rows):
    if rows is None:
        raise ValueError("table absente")
    return []


if __name__ == "__main__":
    exemple = [
        {"PAYS": "Allemagne", "CAPITALE": "Berlin", "CONTINENT": "Europe", "POPULATION": "82801531"},
        {"PAYS": "Brésil", "CAPITALE": "Brasilia", "CONTINENT": "Amérique du Sud", "POPULATION": "204259812"},
    ]
    print(filtrer_par_continent(exemple, "Europe"))
