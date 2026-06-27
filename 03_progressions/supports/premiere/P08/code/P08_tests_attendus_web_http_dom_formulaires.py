"""Tests attendus TP P08. Statut pédagogique: needs_review."""
from __future__ import annotations
import importlib
import os

MODULE = importlib.import_module(os.environ.get("TP_MODULE", "P08_starter_web_http_dom_formulaires"))
HTML = "<html><head><title>Mini site NSI</title></head><body><p class='alerte'>Erreur</p><p class='ok'>Valide</p></body></html>"


def test_nominal_html_dom_get_post() -> None:
    assert MODULE.titre_page(HTML) == "Mini site NSI"
    assert MODULE.textes_classe(HTML, "alerte") == ["Erreur"]
    assert MODULE.parametres_get("https://nsi.test/recherche?q=tri&page=2") == {"q": "tri", "page": "2"}
    assert MODULE.action_formulaire("POST", {"nom": "Ada"}) == "paramètres dans le corps de la requête"


def test_limites_classe_absente_et_get_vide() -> None:
    assert MODULE.textes_classe(HTML, "absente") == []
    assert MODULE.parametres_get("https://nsi.test/recherche") == {}
    assert MODULE.action_formulaire("GET", {"q": "tri"}) == "paramètres dans l'URL"


def test_entrees_invalides() -> None:
    title_absent_refuse = False
    try:
        MODULE.titre_page("<html></html>")
    except ValueError:
        title_absent_refuse = True
    if not title_absent_refuse:
        raise AssertionError("ValueError attendue pour title absent")
    try:
        MODULE.action_formulaire("TRACE", {})
    except ValueError:
        return
    raise AssertionError("ValueError attendue pour méthode interdite")


if __name__ == "__main__":
    test_nominal_html_dom_get_post()
    test_limites_classe_absente_et_get_vide()
    test_entrees_invalides()
    print("tests attendus OK")
