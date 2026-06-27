"""Corrigé professeur TP P08 Web, DOM et HTTP. Statut pédagogique: needs_review."""
from __future__ import annotations
import re
from urllib.parse import parse_qs, urlparse


def titre_page(html: str) -> str:
    match = re.search(r"<title>(.*?)</title>", html, re.I | re.S)
    if not match:
        raise ValueError("titre absent")
    return " ".join(match.group(1).split())


def textes_classe(html: str, classe: str) -> list[str]:
    pattern = rf"<(?P<tag>\w+)[^>]*class=['\"][^'\"]*\b{re.escape(classe)}\b[^'\"]*['\"][^>]*>(?P<text>.*?)</(?P=tag)>"
    return [
        " ".join(re.sub(r"<[^>]+>", "", text).split())
        for _tag, text in re.findall(pattern, html, re.I | re.S)
    ]


def parametres_get(url: str) -> dict[str, str]:
    parsed = urlparse(url)
    return {cle: valeurs[0] for cle, valeurs in parse_qs(parsed.query, keep_blank_values=True).items()}


def action_formulaire(method: str, champs: dict[str, str]) -> str:
    methode = method.upper()
    if methode not in {"GET", "POST"}:
        raise ValueError("méthode HTTP non prise en charge")
    if methode == "GET":
        return "paramètres dans l'URL"
    return "paramètres dans le corps de la requête"
