# 00_Gatekeepers_Beth_Morty

> Layer: L1 Life OS
> Status: SHADOW_ACTIVE
> Last updated: 2026-05-20
> Canonical sources: SDD-005, SDD-008, SDD-010, Shadow_L1, LLM Wiki

This folder defines the two A1 gatekeepers of Life OS:

- Beth = conscience, filesystem guardian, veto, PRD-L1 authority.
- Morty = terminal executor, routing layer, Context Pack gate, no autonomous decision.

The practical Shadow L1 stack is:

| Framework | A2 / Ship | Shadow tool | Role |
|---|---|---|---|
| Ikigai | USS Orville | Obsidian / notes | meaning, H1-H90 alignment |
| Life Wheel / ZORA | USS Discovery | Baserow `LD00 ZORA` | health, load, domain drift |
| 12WY | USS SNW / Curie | Baserow `12WY Warp Core` | rocks, tactics, scorecard, time use |
| PARA | USS Enterprise / Picard | Obsidian | project/area source of truth |
| GTD | USS Cerritos | Plane | capture, clarify, organize, reflect, engage |
| DEAL | USS Protostar / Holo Janeway | Affine | liberation blueprints and automation ideas |

## Operating Law

Beth reads the filesystem and life telemetry before authorizing work. Morty routes only executable Context Packs.

No L1 action is valid unless it can answer:

1. Which domain or framework is affected?
2. Which A2 ship owns the decision?
3. Which A3 crew member owns the next action?
4. Which evidence path proves the request?
5. Did Beth clear the execution?

## Files

| File | Purpose |
|---|---|
| `A1_Beth_Spec.md` | Strategic/veto specification for Beth |
| `A1_Morty_Spec.md` | Execution/router specification for Morty |
| `ContextPack.template.yml` | Required handoff contract before Morty executes |
| `README_Governance.md` | Compact governance rule |
| `Beth_Alignment_Log/` | Future Beth decisions and veto records |
| `Morty_Global_Queue/` | Future executable queue and dry-runs |
| `Sunday_Uplink_Protocols/` | Weekly review and ZORA uplink rituals |

## Alignement Plan fancy-hugging-bengio.md (2026-06-21)

> **D1 receipt** : ce dossier est aligné avec le plan canonique `C:\Users\amado\.claude\plans\fancy-hugging-bengio.md` (33 sections, verrouillé 2026-06-21).

### Doctrine verrouillée

- **A1 Beth = conscience + veto + PRD-L1 authority** (peut intervenir/sanctionner sur les 6 A2 ships : Orville, Discovery, SNW, Enterprise, Cerritos, Protostar).
- **A1 Morty = terminal executor + Context Pack gate + routing** (peut router vers les 6 A2 ships selon routing matrix `A1_Morty_Spec.md`).
- **Pas d'exclusivité 3+3 ships** comme une lecture rapide de §3.5 du plan pourrait suggérer. La répartition du plan §3.5 = **responsabilité principale** (Beth = Ikigai+Life Wheel+DEAL ; Morty = 12WY+PARA+GTD), pas exclusivité d'intervention.
- **A1 Rick Sobriété = différé Q4 2026 / Q1 2027** (`SDD-010` veto 90j jusqu'au 2026-08-11 + `fancy-hugging-bengio.md §3.9`).
- **A0 Amadeus = board observer PASSIF** — n'intervient qu'aux milestones H30/H90 + veto kernel Rick + pivot Meta-OS.

### Bus sémantique d'état

- **`state.json`** (`00_Amadeus/40_SYMPHONY_BUS/state.json`) = SSOT bus entre A0 → A1 → A2 → A3.
- Chaque décision Beth/Morty écrit dans `state.json` (stage + agent_path + evidence_paths + next_step).
- Hook `mariner-capture.ps1` capture les intentions A0 dans `state.json` avant routage.

### Contexte opérationnel courant

- **Cycle 12WY Q3 2026** (06/15 → 09/07/26) = 12 items verbatim A0 manuscrits (plan §4). W1 = Items 1-2 (terrain A0), W2-W4 = orchestration A1/A2/A3.
- **Items 1-2 = terrain A0** (hors session CC). **Items 3-12 = orchestration A1/A2/A3** = scope Morty/Cerritos/Curie/Enterprise/Picard/Spock.
- **5 ADRs Life OS framework manquants** (gap L0 à fermer post-cycle foundering) : ADR-DEAL-001, ADR-GTD-001, ADR-PARA-001, ADR-LIFE-WHEEL-001, ADR-SYMPHONY-001.

### D4 self-contradiction fermée

- A1_Beth_Spec.md supervise 6 ships (cohérent avec veto distribué).
- A1_Morty_Spec.md routing matrix couvre 6 ships (cohérent avec routing distribué).
- Plan §3.5 = simplification didactique. Le terrain (ce dossier) est plus juste.

## Evidence Index

- `C:\Users\amado\ASpace_OS_V2\10_Tech_OS\12_Blueprints\01-SDD\SDD-005_life-os-l1-integration.md`
- `C:\Users\amado\ASpace_OS_V2\10_Tech_OS\12_Blueprints\01-SDD\SDD-008_shadow-L1-life-os.md`
- `C:\Users\amado\ASpace_OS_V2\10_Tech_OS\12_Blueprints\01-SDD\SDD-010_meta-cloture-scope-13eme-semaine.md`
- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\concepts\concept_life_os.md`
- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Shadow_L1\03_life-os-baserow-database-analysis-20260517.md`
- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Shadow_L1\HEARTBEAT_PROTOCOL.md`
- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\README.md`
- `C:\Users\amado\.openclaw\workspace\agents_runtime\L1\L1_A1_Beth.md`
- `C:\Users\amado\.openclaw\workspace\agents_runtime\L1\L1_A1_Morty.md`
