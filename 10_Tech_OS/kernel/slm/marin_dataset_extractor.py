#!/usr/bin/env python3
"""
marin_dataset_extractor.py — Extraction et compilation de dataset d'alignement pour MiniMind.
Extrait les concepts certifiés OKF v0.2 et les triplets RDF de 70_Onthologies/ pour générer
des paires d'instruction tuning déterministes.
"""
from __future__ import annotations
import json
import re
from pathlib import Path
from typing import Any, Dict, List

KERNEL_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = KERNEL_DIR.parent.parent
OKF_CONCEPTS_DIR = ROOT_DIR / "40_Memory_Wiki_OKF" / "concepts"
RDF_TRIPLETS_DIR = ROOT_DIR / "70_Onthologies" / "triplets"


def extract_okf_concepts() -> List[Dict[str, str]]:
    dataset = []
    if not OKF_CONCEPTS_DIR.exists():
        return dataset

    for file_path in OKF_CONCEPTS_DIR.glob("*.md"):
        try:
            content = file_path.read_text(encoding="utf-8", errors="replace")
            # Extraction frontmatter
            title = file_path.stem
            description = ""
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    fm = parts[1]
                    for line in fm.splitlines():
                        if line.startswith("title:"):
                            title = line.split(":", 1)[1].strip().strip("\"'")
                        elif line.startswith("description:"):
                            description = line.split(":", 1)[1].strip().strip("\"'")

            dataset.append({
                "instruction": f"Explique le concept canonique d'A'Space OS V3 : {title}",
                "input": description,
                "output": content[:1200]
            })
        except Exception:
            continue
    return dataset


def extract_rdf_triplets() -> List[Dict[str, str]]:
    dataset = []
    if not RDF_TRIPLETS_DIR.exists():
        return dataset

    for file_path in RDF_TRIPLETS_DIR.glob("*.jsonl"):
        try:
            with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        data = json.loads(line)
                        s = data.get("subject") or data.get("s")
                        p = data.get("predicate") or data.get("p")
                        o = data.get("object") or data.get("o")
                        if s and p and o:
                            dataset.append({
                                "instruction": f"Quelle est la relation ontologique entre {s} et {o} ?",
                                "input": f"Sujet: {s}, Prédicat: {p}",
                                "output": f"Dans l'ontologie d'A'Space OS V3, {s} {p} {o}."
                            })
                    except json.JSONDecodeError:
                        continue
        except Exception:
            continue
    return dataset


def compile_marin_dataset(output_path: Path | None = None) -> Path:
    if output_path is None:
        output_path = KERNEL_DIR / "slm" / "marin_alignment_dataset.jsonl"

    dataset = extract_okf_concepts() + extract_rdf_triplets()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        for entry in dataset:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    return output_path


if __name__ == "__main__":
    out_file = compile_marin_dataset()
    print(f"Dataset Marin compile avec succes : {out_file}")
