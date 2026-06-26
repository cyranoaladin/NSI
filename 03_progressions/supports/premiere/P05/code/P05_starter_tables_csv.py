"""Asset Python TP. Statut pédagogique: needs_review."""

from __future__ import annotations

def filtrer_table(rows):
    if rows is None:
        raise ValueError("table absente")
    return []

if __name__ == "__main__":
    print(filtrer_table([{"nom":"Ada","age":"17"},{"nom":"Tim","age":"14"}]))
