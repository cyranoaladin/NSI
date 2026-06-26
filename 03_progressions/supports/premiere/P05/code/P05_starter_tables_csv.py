"""Starter TP P05 - Tables CSV et requêtes simples."""

from __future__ import annotations


def filtrer_table(rows):
    """Retourne une synthèse contrôlable pour le TP P05."""
    if rows is None:
        raise ValueError("entrée absente")
    return {"entree": rows, "controle": "liste de dictionnaires filtrée puis moyenne calculée", "cas_limite": "champ vide, séparateur inattendu ou nombre invalide"}


if __name__ == "__main__":
    print(filtrer_table([{"nom":"Ada", "age":"17"}]))
