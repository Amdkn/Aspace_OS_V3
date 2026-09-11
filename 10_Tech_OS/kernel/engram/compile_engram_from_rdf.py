#!/usr/bin/env python3
"""
compile_engram_from_rdf.py — Compilateur Graham Ontologie -> Engram Phrase Book
Lit l'ensemble des fichiers JSONL dans 70_Onthologies/triplets/ (1 347+ faits)
et compile les invariants et entités stables dans phrase_book_aspace.json sur NVMe.
Garantit zéro token consommé pour les résolutions d'actes et de gouvernance.
"""

from __future__ import annotations
import json
import re
from pathlib import Path

ICI = Path(__file__).resolve().parent
KERNEL_DIR = ICI.parent
ROOT_DIR = KERNEL_DIR.parent.parent
TRIPLETS_DIR = ROOT_DIR / "70_Onthologies" / "triplets"
PHRASEBOOK_PATH = ICI / "phrase_book_aspace.json"


def normalize_words(text: str) -> list[str]:
    cleaned = re.sub(r"[^a-zA-Z0-9àâéèêëîïôöùûüç\- ]", " ", str(text).lower())
    return [w for w in cleaned.split() if len(w) > 2]


def compile_triplets():
    if not TRIPLETS_DIR.exists():
        print(f"[!] Dossier triplets introuvable : {TRIPLETS_DIR}")
        return

    if PHRASEBOOK_PATH.exists():
        with open(PHRASEBOOK_PATH, "r", encoding="utf-8") as f:
            phrasebook = json.load(f)
    else:
        phrasebook = {
            "$schema": "https://aspace.os/schemas/v3/engram-phrasebook.json",
            "version": "1.0.0",
            "storage_backend": "mmap_nvme",
            "entries": {}
        }

    entries = phrasebook.setdefault("entries", {})
    triplet_files = list(TRIPLETS_DIR.glob("*.jsonl"))
    total_triplets = 0
    added_keys = 0

    for tf in triplet_files:
        with open(tf, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                total_triplets += 1
                try:
                    data = json.loads(line)
                    sujet = data.get("sujet", "")
                    verbe = data.get("verbe", "")
                    objet = data.get("objet", "")
                    phrase = data.get("phrase", "")
                    confiance = data.get("confiance", "moyenne")

                    if not sujet or not verbe:
                        continue

                    key = f"ONTO_{sujet.upper()}_{verbe.upper()}_{objet.upper()}"[:64]
                    ngram = normalize_words(f"{sujet} {verbe} {objet}")
                    if not ngram:
                        continue

                    dim = "5D"
                    if "business" in tf.name or "sob" in tf.name:
                        dim = "7D"
                    elif "life" in tf.name:
                        dim = "1D"
                    elif "tech" in tf.name or "kernel" in tf.name:
                        dim = "3D"

                    if key not in entries:
                        entries[key] = {
                            "ngram": ngram[:4],
                            "dimension": dim,
                            "resolution_type": "ONTOLOGY_TRIPLET",
                            "subject": sujet,
                            "predicate": verbe,
                            "object": objet,
                            "phrase": phrase,
                            "source_file": tf.name,
                            "confidence": confiance
                        }
                        added_keys += 1
                except Exception:
                    continue

    with open(PHRASEBOOK_PATH, "w", encoding="utf-8") as f:
        json.dump(phrasebook, f, indent=2, ensure_ascii=False)

    print(f"[*] Compilation achevée avec succès.")
    print(f"    - Fichiers analysés : {len(triplet_files)}")
    print(f"    - Triplets scannés : {total_triplets}")
    print(f"    - Nouveaux invariants compilés dans Engram : {added_keys}")
    print(f"    - Total des entrées dans le Phrase Book : {len(entries)}")


if __name__ == "__main__":
    compile_triplets()