from __future__ import annotations

import socket
import sys
import urllib.request
from pathlib import Path
from typing import Any

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))


def _blocked_network(*_args: Any, **_kwargs: Any) -> None:
    raise AssertionError("réseau réel interdit pendant les tests")


@pytest.fixture(autouse=True)
def block_real_network_and_unmocked_substance_services(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(urllib.request, "urlopen", _blocked_network)
    monkeypatch.setattr(socket, "create_connection", _blocked_network)
    if "substance_judge" in sys.modules:
        module = sys.modules["substance_judge"]
        monkeypatch.setattr(module, "search_rag", _blocked_network)
        monkeypatch.setattr(module, "call_llm", _blocked_network)
