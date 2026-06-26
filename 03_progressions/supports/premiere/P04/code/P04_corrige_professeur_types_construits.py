"""Asset Python TP. Statut pédagogique: needs_review."""

from __future__ import annotations

def resume_mesures(mesures):
    if mesures is None:
        raise ValueError("mesures absentes")
    if not mesures:
        return {"nombre": 0, "minimum": None, "maximum": None, "moyenne": None}
    return {"nombre": len(mesures), "minimum": min(mesures), "maximum": max(mesures), "moyenne": sum(mesures) / len(mesures)}
