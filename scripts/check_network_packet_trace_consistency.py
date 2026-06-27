#!/usr/bin/env python3
"""Check network packet and routing examples for concrete consistency."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re

from _qa_common import ROOT


TARGETS = [
    ROOT / "03_progressions" / "supports" / "premiere" / "P10",
    ROOT / "03_progressions" / "supports" / "terminale" / "T12",
    ROOT / "03_progressions" / "supports" / "terminale" / "T13",
    ROOT / "03_progressions" / "fiches_cours" / "premiere" / "P10",
    ROOT / "03_progressions" / "fiches_cours" / "terminale" / "T12",
    ROOT / "03_progressions" / "fiches_cours" / "terminale" / "T13",
]


@dataclass
class NetworkTraceResult:
    errors: list[str] = field(default_factory=list)
    files_checked: int = 0


def network_block_errors(text: str) -> list[str]:
    errors: list[str] = []
    lowered = text.lower()
    if re.search(r"ttl\s*=\s*1", lowered) and re.search(r"transmettre|routeur suivant|prochain routeur", lowered):
        if not re.search(r"ttl\s*=\s*0|drop|rejeter|détruit|detruit|icmp|expir", lowered):
            errors.append("TTL=1 transmis sans décrément à 0 ni rejet explicite")
    if "mac" in lowered and "ip" in lowered and re.search(r"mac\s*(?:=|est)\s*\d+\.\d+\.\d+\.\d+", lowered):
        errors.append("adresse MAC confondue avec une adresse IP")
    if "https" in lowered and re.search(r"\b80\b", lowered) and "443" not in lowered:
        errors.append("HTTPS associé au port 80 sans correction vers 443")
    if re.search(r"destination\s+locale", lowered) and re.search(r"passerelle", lowered):
        if not re.search(r"sinon|si.*pas locale|préfixe|masque", lowered):
            errors.append("destination locale et passerelle mélangées sans décision par préfixe")
    if "route choisie" in lowered and "préfixe" in lowered and not re.search(r"/\d{1,2}|masque", lowered):
        errors.append("route par préfixe annoncée sans préfixe vérifiable")
    return errors


def network_block_is_consistent(text: str) -> bool:
    return not network_block_errors(text)


def candidate_files(root: Path = ROOT) -> list[Path]:
    files: list[Path] = []
    for base in TARGETS:
        if base.exists():
            files.extend(sorted(base.glob("*.md")))
    return files


def analyze_network_packet_trace_consistency(root: Path = ROOT) -> NetworkTraceResult:
    result = NetworkTraceResult()
    for path in candidate_files(root):
        result.files_checked += 1
        text = path.read_text(encoding="utf-8", errors="replace")
        for error in network_block_errors(text):
            result.errors.append(f"{path.relative_to(root).as_posix()}: {error}")
    return result


def main() -> int:
    result = analyze_network_packet_trace_consistency()
    if result.errors:
        print("check_network_packet_trace_consistency: KO")
        for error in result.errors[:160]:
            print(f"- {error}")
        return 1
    print(f"check_network_packet_trace_consistency: PASS ({result.files_checked} fichiers)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
