"""Asset Python TP. Statut pédagogique: needs_review."""

from __future__ import annotations

def resume_mesures(mesures):
    if mesures is None:
        raise ValueError("mesures absentes")
    return {"nombre": len(mesures)}

if __name__ == "__main__":
    print(resume_mesures([12, 14, 13]))
