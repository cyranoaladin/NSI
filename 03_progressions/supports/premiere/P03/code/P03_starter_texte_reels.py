"""Starter TP P03 - Texte Unicode et nombres réels."""

from __future__ import annotations


def inspect_text(text):
    """Retourne une synthèse contrôlable pour le TP P03."""
    if text is None:
        raise ValueError("entrée absente")
    return {"entree": text, "controle": "2 caractères, 3 octets, somme flottante non exactement égale à 0.3", "cas_limite": "caractère hors ASCII ou comparaison directe de flottants"}


if __name__ == "__main__":
    print(inspect_text("Aé"))
