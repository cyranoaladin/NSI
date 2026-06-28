from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_no_committed_secrets as secrets


def test_detects_public_ip_but_allows_placeholders_and_private_ips(tmp_path: Path) -> None:
    public_file = tmp_path / "public.txt"
    placeholder_file = tmp_path / "placeholder.txt"
    private_file = tmp_path / "private.txt"
    local_env = tmp_path / ".env.rag"
    public_ip = "88.99." + "254.59"
    public_file.write_text(f"ssh root@{public_ip}\n", encoding="utf-8")
    placeholder_file.write_text("ssh <user>@<host>\n", encoding="utf-8")
    private_file.write_text("service http://127.0.0.1:8000\n", encoding="utf-8")
    local_env.write_text(f"RAG_SSH_HOST={public_ip}\n", encoding="utf-8")

    errors = secrets.scan_paths([public_file, placeholder_file, private_file, local_env], tmp_path)

    assert errors == [f"{public_file.name}: adresse IP publique en clair -> {public_ip}"]


def test_detects_token_like_assignments_without_flagging_examples(tmp_path: Path) -> None:
    secret_file = tmp_path / "secret.env.example"
    safe_file = tmp_path / "safe.env.example"
    constant_file = tmp_path / "constants.py"
    secret_file.write_text("RAG_API_KEY=abc1234567890secret\n", encoding="utf-8")
    safe_file.write_text("RAG_API_KEY=<token Bearer pour l'API>\n", encoding="utf-8")
    constant_file.write_text('CONCRETE_TOKENS = {"trace", "table"}\n', encoding="utf-8")

    errors = secrets.scan_paths([secret_file, safe_file, constant_file], tmp_path)

    assert errors == [f"{secret_file.name}: secret potentiel dans RAG_API_KEY"]
