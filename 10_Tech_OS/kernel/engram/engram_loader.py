#!/usr/bin/env python3
"""
A'Space OS V3 — Engram Phrase Book Loader
Résolution déterministe O(1) via memory-mapped file (mmap) sur SSD NVMe.
Zéro token LLM consommé pour le Lore et les règles structurelles.
"""

import json
import mmap
from pathlib import Path
from typing import Any, Optional

DEFAULT_PHRASEBOOK = Path(__file__).parent / "phrase_book_aspace.json"

class EngramPhraseBook:
    def __init__(self, path: Path = DEFAULT_PHRASEBOOK):
        self.path = Path(path)
        self._data: dict[str, Any] = {}
        self._load_mmap()

    def _load_mmap(self) -> None:
        if not self.path.exists():
            raise FileNotFoundError(f"[Engram] Fichier introuvable : {self.path}")
        
        with open(self.path, "r", encoding="utf-8") as f:
            with mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_READ) as mm:
                content = mm.read().decode("utf-8")
                self._data = json.loads(content)

    def resolve(self, tokens: list[str]) -> Optional[dict[str, Any]]:
        """Résout une séquence de tokens contre la lookup table sans appel modèle."""
        normalized = " ".join(t.lower().strip() for t in tokens)
        for key, payload in self._data.get("entries", {}).items():
            pattern = " ".join(payload.get("ngram", []))
            if pattern and pattern in normalized:
                return {
                    "matched_key": key,
                    "dimension": payload.get("dimension"),
                    "resolution_type": payload.get("resolution_type"),
                    "payload": payload
                }
        return None

if __name__ == "__main__":
    resolver = EngramPhraseBook()
    query = ["Besoin", "de", "valider", "la", "definition", "of", "done", "du", "build"]
    match = resolver.resolve(query)
    print(f"[*] Test Résolution Engram : {json.dumps(match, indent=2, ensure_ascii=False)}")
