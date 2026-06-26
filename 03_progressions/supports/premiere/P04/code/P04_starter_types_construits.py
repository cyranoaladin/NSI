"""Starter TP P04 - Types construits Python."""

from __future__ import annotations


def resume_mesures(mesures):
    """Retourne une synthèse contrôlable pour le TP P04."""
    if mesures is None:
        raise ValueError("entrée absente")
    return {"entree": mesures, "controle": "tuple non modifié, liste mise à jour, dictionnaire consulté par clé", "cas_limite": "copie de liste et clé absente"}


if __name__ == "__main__":
    print(resume_mesures([12, 14, 13]))
