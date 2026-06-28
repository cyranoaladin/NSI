"""Slugification d'ancres Markdown, compatible avec le rendu GitHub/Pandoc
utilisé par le dépôt nsi-enseignement.

Règles validées (11/11) contre les ancres réelles citées dans les frontmatters
des séquences pilotes :
  - minuscule ;
  - le balisage inline `code` est retiré (le backtick disparaît) ;
  - tout caractère qui n'est ni lettre unicode, ni chiffre, ni espace, ni
    tiret, ni underscore est supprimé (les accents sont CONSERVÉS) ;
  - les espaces deviennent des tirets ;
  - les tirets consécutifs NE sont PAS fusionnés
    (« Réponse attendue — TD » -> « réponse-attendue--td »).

GitHub désambiguïse les titres identiques en suffixant -1, -2, ... aux
occurrences suivantes. `build_slug_table` reproduit ce comportement.
"""

from __future__ import annotations

import unicodedata


def github_slug(title: str) -> str:
    """Renvoie le slug d'un titre seul (sans gestion des doublons)."""
    s = unicodedata.normalize("NFC", title).strip().lower()
    s = s.replace("`", "")
    kept = [ch for ch in s if ch.isalnum() or ch in (" ", "-", "_")]
    return "".join(kept).replace(" ", "-")


def build_slug_table(titles: list[str]) -> dict[str, str]:
    """Associe chaque titre à son slug effectif, doublons désambiguïsés.

    Renvoie un dict {titre_original: slug_effectif}. L'ordre de `titles` doit
    être l'ordre d'apparition dans le document.
    """
    counts: dict[str, int] = {}
    table: dict[str, str] = {}
    for title in titles:
        base = github_slug(title)
        n = counts.get(base, 0)
        slug = base if n == 0 else f"{base}-{n}"
        counts[base] = n + 1
        table[title] = slug
    return table


if __name__ == "__main__":
    refs = {
        "Bases 2, 10 et 16": "bases-2-10-et-16",
        "Entiers relatifs et complément à deux": "entiers-relatifs-et-complément-à-deux",
        "Booléens et tables de vérité": "booléens-et-tables-de-vérité",
        "Texte, ASCII et Unicode": "texte-ascii-et-unicode",
        "Réponse attendue — TD": "réponse-attendue--td",
    }
    ok = sum(github_slug(h) == v for h, v in refs.items())
    print(f"auto-test slug: {ok}/{len(refs)}")
