"""Starter TP P02 - Complément à deux et booléens."""

from __future__ import annotations


def twos_complement_value(bits):
    """Retourne une synthèse contrôlable pour le TP P02."""
    if bits is None:
        raise ValueError("entrée absente")
    return {"entree": bits, "controle": "11101001 et simplification en a", "cas_limite": "140 impossible sur 8 bits signés"}


if __name__ == "__main__":
    print(twos_complement_value("11101001"))
