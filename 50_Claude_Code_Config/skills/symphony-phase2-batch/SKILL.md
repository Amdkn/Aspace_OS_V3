---
name: symphony-phase2-batch
description: Batch canonization + wiring for Symphony Lane A/B/C (OSS Twin Runtime of L1 Life OS). Triggers when A0 mandates "go for all Next steps Symphony" or similar Phase 2 commands. Combines 8 sub-agents in parallel (D8) to (1) re-twin 2 A1 + 6 A2 specs with canon corrections, (2) create 35 A3 twins (6 ships), (3) build 4 MCP Python servers (Affine/Baserow/Obsidian/Plane), (4) wire 6 bridge Python runtimes (A0→A1, A1→A2, A2→A3, A3→DLQ, L0→L1, L1→L2). All 4 sub-tasks parallelize independently with no cross-dependencies. ROI ~120 min/symphony-phase2 invocation. Use proactively when A0 says "Symphony Phase 2" or "wiring L1 runtime" or asks to extend Lane A/B/C coverage.
---

# Symphony Phase 2 Batch — Twin Runtime Wiring

## When to use

- A0 says "go for all Next steps Symphony (Phase 2 candidates)"
- A0 says "Symphony Lane B" / "wiring 4 MCPs" / "6 bridges"
- A0 says "create 35 A3 twins" / "re-twin A2 specs"
- A0 mandates any combination of the 4 sub-tasks (twin spec corrections, A3 twin creation, MCP building, bridge wiring)

## When NOT to use

- A0 asks for ONE specific file/twin (use the dedicated skill like `picard-audit-and-prod-workflow` or `replicate-squads` instead)
- A0 asks for Symphony analysis (read the 3 INDEX files in `00_Amadeus/05_OSS_Twin/symphony/L1/` first)
- A0 asks for Telegram plugin (separate scope, see MEMORY handoff)

## Workflow (D2 research-first, D8 parallel, D4 append-only)

### Phase 1 — D2 research (read-first, ~5 min)

Read these 5 files FIRST (in parallel):

1. `00_Amadeus/05_OSS_Twin/symphony/L1/INDEX_specs.md` — Lane A index (A1+A2+A3 structure)
2. `00_Amadeus/05_OSS_Twin/symphony/L1/INDEX_capsules.md` — Lane C capsule template
3. `00_Amadeus/05_OSS_Twin/symphony/L1/INDEX_runtime.md` — Lane B structure (routing/scripts/bridges/mcps)
4. `00_Amadeus/05_OSS_Twin/symphony/L1/lane_A_specs/02_A2_ships/*.twin.md` — current A2 twins (v1.1 expected)
5. `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/skills_queue.md` — A0 pending decisions

**D2 receipts required** : all 5 files read BEFORE any Write.

### Phase 2 — Launch 8 sub-agents in parallel (D8, ~10-15 min)

Launch these 8 sub-agents with `run_in_background: true` in a SINGLE message:

| Sub-agent | Mission | Output count | Source of truth |
|---|---|---|---|
| A1+A2 re-twin (1 sub-agent) | Re-twin 2 A1 + 6 A2 files to v1.1 with canon corrections (Computer ≠ Picard, Holo Deck ≠ Freeman, ZORA ≠ Sia, Holo Janeway with space) | 8 files | `20_Life_OS/00_Gatekeepers_Beth_Morty/A1_*.md` + `20_Life_OS/2X_*/A2_*_Spec.md` |
| A3 twins Orville (1 sub-agent) | Create 9 A3 twins for USS Orville crew | 9 files | `20_Life_OS/21_Ikigai_Orville/` + Claude Code agents `~/.claude/agents/a3-orville-*.md` |
| A3 twins Discovery (1 sub-agent) | Create 8 A3 twins (LD01-LD08) with STOP authority on LD03/LD04 + scarcity_mode on LD02 | 8 files | `20_Life_OS/22_Wheel_Discovery/` + Claude Code agents |
| A3 twins SNW (1 sub-agent) | Create 5 A3 twins (Pike/Una/M'Benga/Chapel/Ortegas) | 5 files | `20_Life_OS/23_12WY_SNW/` + Claude Code agents |
| A3 twins Enterprise (1 sub-agent) | Create 4 A3 twins (Picard/Spock/Geordi/Data) — Picard must say "NOT the A2" | 4 files | `20_Life_OS/24_PARA_Enterprise/` + Claude Code agents |
| A3 twins Cerritos (1 sub-agent) | Create 5 A3 twins — Freeman must say "NOT the A2" | 5 files | `20_Life_OS/25_GTD_Cerritos/` + Claude Code agents |
| A3 twins Protostar (1 sub-agent) | Create 4 A3 twins — Holo Janeway (with space) | 4 files | `20_Life_OS/26_DEAL_Protostar/` + Claude Code agents |
| MCPs (1 sub-agent) | Build 4 Python MCP servers (Affine/Baserow/Obsidian/Plane) using `mcp.server` low-level API | 4 files (~30 KB) | `01_routing/symphony-*.spec.md` |
| Bridges (1 sub-agent) | Build 6 Python bridge wirings (A0→A1, A1→A2, A2→A3, A3→DLQ, L0→L1, L1→L2) | 6 files (~44 KB) | `03_bridges/*.bridge.md` |

**Total** : 8 sub-agents → 8 missions → 49 files (8 A1+A2 + 35 A3 + 4 MCPs + 6 bridges — wait, that's 53 files; recheck per A0 mandate).

### Phase 3 — D1 verify independently (~2 min)

After sub-agents complete, **NEVER trust their claims**. Run these independent checks:

```bash
# 1. File count
cd "C:/Users/amado/ASpace_OS_V2/00_Amadeus/05_OSS_Twin/symphony/L1/"
find lane_A_specs/03_A3_crews/ -name "*.twin.md" -not -path "*_TRASH*" | wc -l   # expect 35
ls lane_B_runtime/04_mcps/ | wc -l                                               # expect 4
ls lane_B_runtime/03_bridges/*.bridge.py | wc -l                                # expect 6

# 2. Syntax check (UTF-8 mode mandatory, Windows console codec pitfall)
"C:/Python314/python.exe" -X utf8 -c "
import ast
files = ['lane_B_runtime/04_mcps/mcp-affine.py', 'lane_B_runtime/04_mcps/mcp-baserow.py',
         'lane_B_runtime/04_mcps/mcp-obsidian.py', 'lane_B_runtime/04_mcps/mcp-plane.py',
         'lane_B_runtime/03_bridges/A0_to_A1.bridge.py', 'lane_B_runtime/03_bridges/A1_to_A2.bridge.py',
         'lane_B_runtime/03_bridges/A2_to_A3.bridge.py', 'lane_B_runtime/03_bridges/A3_DLQ.bridge.py',
         'lane_B_runtime/03_bridges/L0_to_L1.bridge.py', 'lane_B_runtime/03_bridges/L1_to_L2.bridge.py']
ok = sum(1 for f in files if ast.parse(open(f, encoding='utf-8').read()) is None)
print(f'{ok}/10 syntactically valid')
"

# 3. Anti-pattern grep (CRITICAL — D4 no-self-contradiction)
grep -rE "Picard is the A2|Freeman is the A2|Sia is the A2|Ship Captain.*Compiler" lane_A_specs/03_A3_crews/*/[a-z]*.twin.md
# Expect: 0 hits (matches in v0 legacy or comments OK)
```

### Phase 4 — D4 archive legacy v0 twins (~1 min)

If `03_A3_crews/<ship>/` already has PascalCase `A3_*.twin.md` from a prior scaffold (2026-06-07):

```bash
cd "C:/Users/amado/ASpace_OS_V2/00_Amadeus/05_OSS_Twin/symphony/L1/lane_A_specs/03_A3_crews/"
mkdir -p _TRASH_2026-06-15_legacy_v0/
for ship in orville discovery snw enterprise cerritos protostar; do
  for f in "$ship"/A3_*.twin.md; do
    [ -f "$f" ] && mv "$f" "_TRASH_2026-06-15_legacy_v0/$(basename "$f")"
  done
done
```

**D4 no-hard-delete** : never `rm`; always archive to `_TRASH_<date>/`.

### Phase 5 — Write-back canonique + report (~3 min)

1. Append `**YYYY-MM-DD** : Symphony Phase 2 batch — ...` to `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md`
2. Update `INDEX_specs.md` (A1+A2 v1.1 ACTIVE) + `INDEX_capsules.md` (A3 ACTIVE) + `INDEX_runtime.md` (MCPs+bridges ACTIVE)
3. Append 5-line INDEX-ONLY section to `~/.claude/projects/c--Users-amado/memory/MEMORY.md`
4. Report to A0 with : file count, KB totals, anti-pattern grep clean, Doctrine anchored

## D1 Anti-Patterns to Guard (CRITICAL)

These 5 anti-patterns MUST be 0 in v1 twins. Sub-agents that produce ANY of these must be re-run.

| Anti-pattern | Correct |
|---|---|
| `Picard is the A2` | Picard = A3 Projects, LCARS Computer = A2 Enterprise |
| `Freeman is the A2` | Freeman = A3 Engage, Holo Deck = A2 Cerritos |
| `Sia is the A2` (Discovery) | ZORA = A2 Discovery, Sia = A2 Orville (not real A2) |
| `Ship Captain` as A2 role | A2 = ship intelligence (Computer/AI), not captain |
| `HoloJaneway` hyphen | Holo Janeway with space (per `A2_HoloJaneway_Protostar_Spec.md` L.25) |

## Sub-Agent Prompt Template

Each sub-agent prompt should include:
- File path to read (D2 research-first)
- Ship name + A2 name canon
- 35 A3 names reference table (from `~/.claude/agents/a3-*.md`)
- Format template (~1.5-2 KB per file)
- D1 receipts expected (syntax valid, anti-pattern grep, file count)
- D4 append-only constraint (no canon modification)

## ROI

First observed run (2026-06-15) : ~120 min for 8 sub-agents + D1 verify + write-back. Subsequent runs : ~15-30 min if all 5 source files already read in current session (cache hit).

## Doctrine Anchoring

- **D1 verify-before-assert** : D1 verify INDEPENDENTLY after sub-agents (never trust claims)
- **D2 research-first** : 5 INDEX files read before any Write
- **D4 append-only** : 35 v0 archived to `_TRASH_<date>/`, never `rm`
- **D6 root cause** : 5 anti-patterns identified (D4 no-self-contradiction cascade)
- **D7 cost-of-escalation A0** : 8 sub-agents in parallel = 1 A0 turn (not 35)
- **D8 cross-agent** : Python MCP servers, env var auth, JSON logging = portable Codex/Gemini/Hermes
- **Test Key Pragma** : no hardcoded API keys in code, env var User scope only
