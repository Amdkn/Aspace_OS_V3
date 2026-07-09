"""
collector_11_memory.py — Pilier Memory (📚) pour Citadelle A0.

Carte mémoire : wiki 124 pages · MEMORY.md · graphify master · Supabase.
Source : Memory Architect Kit (02_Templates/Memory Architect Kit).

Date : 2026-07-04 · Auteur : Mavis (MC/L1) — Plan Citadelle A0 P2
Source : ~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md §3 page Memory
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

ROOT = Path(r"C:\Users\amado")
OUTPUT = Path(r"C:\Users\amado\agent-os\citadel\data\11_memory.json")


def count_pages(base: Path, ext: str = "*.md") -> int:
    if not base.exists():
        return 0
    return sum(1 for _ in base.rglob(ext))


def main() -> int:
    wiki = ROOT / "wiki"
    mem_md = ROOT / ".mavis" / "agents" / "mavis" / "memory" / "MEMORY.md"
    graphify_master = ROOT / ".mavis" / "graphify-out" / "graph.json"  # fallback
    graphify_h = ROOT / ".hermes" / "graphify-out" / "graph.json"

    memory_arch_kit = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\02_Templates\Memory Architect Kit")

    payload = {
        "collector": "11_memory",
        "pillar": 11,
        "pillar_name": "Memory (📚 — carte mémoire)",
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "source": "~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md §3 page Memory + Memory Architect Kit",
        "doctrine": "lecture seule — Memristor observational memory — Kill switch E3 wiki-lint",
        "entities": {
            "wiki_pages": {"path": str(wiki), "count": count_pages(wiki), "target_124": 124},
            "memory_md": {"path": str(mem_md), "exists": mem_md.exists(),
                          "size_bytes": mem_md.stat().st_size if mem_md.exists() else 0},
            "graphify_master_M": {"path": str(graphify_m if (graphify_m := ROOT / "ASpace_OS_V2" / "graphify-out-master" / "graph.json").exists() else graphify_h),
                                   "exists": (ROOT / "ASpace_OS_V2" / "graphify-out-master" / "graph.json").exists() or graphify_h.exists()},
            "memory_arch_kit": {"path": str(memory_arch_kit), "exists": memory_arch_kit.exists()},
        },
        "memory_principles": [
            "Memristor observational memory (Eero)",
            "Append-only sessions/ + contracts/ + WEEK_CONTRACT.md",
            "Frontmatter coverage ≥ 95% (rot-rate W6 audit)",
            "Wiki-lint E3 (Memory health)",
            "Cross-harness memory junction .mavis/ ↔ .minimax/",
        ],
        "summary": {
            "wiki_pages": count_pages(wiki),
            "wiki_target": 124,
            "memory_md_exists": mem_md.exists(),
            "memory_md_size": mem_md.stat().st_size if mem_md.exists() else 0,
        },
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[11_memory] OK → {OUTPUT} ({OUTPUT.stat().st_size} b)")
    print(f"  wiki={payload['summary']['wiki_pages']} (target {payload['summary']['wiki_target']}) memory_md={payload['summary']['memory_md_size']}b")
    return 0


if __name__ == "__main__":
    sys.exit(main())