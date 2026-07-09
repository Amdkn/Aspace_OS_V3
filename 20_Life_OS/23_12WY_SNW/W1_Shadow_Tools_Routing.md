---
id: W1_Shadow_Tools_Routing
cycle: Q3-2026
week: W1
title: "Symphony Runtime : Supabase → Baserow → Obsidian → Affine → Plane.so"
a3_owner: Pike (H10 Vision, Captain USS SNW)
a2_ship: USS Curie / SNW
a1_gatekeeper: Morty (Focus opérationnel)
status: SHADOW_CANON_READY
created: 2026-06-21
plan_ref: fancy-hugging-bengio.md §3.2 + §3.7 state.json bus + README 7 dossiers canon
state_json_stage: snw_planning
pre_requisite_for: Symphony Runtime activation
---

# W1 Shadow Tools Routing — Symphony Runtime (5-tier)

> **D1 receipt** : ce routing table est le prérequis canon avant activation Symphony Runtime. Il mappe les 5 Shadow tools (Supabase/Baserow/Obsidian/Affine/Plane.so) aux 6 A2 ships + 7 frameworks Life OS canoniques.

## Vue d'ensemble

```
A0 board observer (passif)
    ↓ intention "Cycle 12WY Q3 2026 ACTIVE"
state.json bus (40_SYMPHONY_BUS/state.json)
    ↓ bus sémantique inter-tools
[5 Shadow Tools en symphonie]
    ↓ routing A1/A2/A3 canon
[6 A2 ships × 7 frameworks Life OS]
```

## Routing canon (5 Shadow tools × A2/A3 owner)

| # | Shadow Tool | Cloud/Local | A2 Ship Owner | A3 Twin Owner | Framework | Sync Direction | Freq | Failover |
|---|---|---|---|---|---|---|---|---|
| 1 | **Supabase** (cloud BE) | Cloud (`hjweyhpmrxqsxfbibsnc.supabase.co`) | USS Enterprise (Computer) | **Data** (chef d'orchestre) + Picard (Projects) + Spock (Areas) + Geordi (Resources) | PARA canon + Life-OS-2026 Vercel FE | Cloud ↔ Vercel | Real-time (RLS Postgres) | **Local mirror** Obsidian si Supabase down |
| 2 | **Baserow** | Cloud (12WY mobile sync) | USS Discovery (ZORA) | **Book** (LD01 H1) + Saru (LD02 H3) + Chapel (Metrics) | Life Wheel LDxx + 12WY Warp Core + Scorecard + Time Use | Cloud ↔ mobile | Async batch (5-15 min) | **Local filesystem** `24_PARA_Enterprise/03_Resources_Geordi/_baserow_export.json` |
| 3 | **Obsidian** | Local vault | USS Enterprise (Computer) | **Spock** (Areas ongoing) + Geordi (Resources curator) | PARA canon local + DEAL Affine cross-link | Local read-only mirror Cloud | Real-time (filesystem watcher) | **N/A** (source of truth local) |
| 4 | **Affine** | Cloud workspace | USS Protostar (Holo Janeway) | **Dal** (Define) + Rok-Tahk (Eliminate) + Zero (Automate) + Gwyn (Liberate) | DEAL 4H Workweek (D/E/A/L) | Cloud async | Manual (Zora weekly review) | **Obsidian** mirror DEAL blueprints |
| 5 | **Plane.so** | Cloud workspace | USS Cerritos (Holo Deck) | **Mariner** (Capture) + Boimler (Clarify) + Tendi (Organize) + Rutherford (Review) + Freeman (Engage) | GTD 5-stage | Cloud real-time | Real-time (Plane API) | **state.json** bus fallback |

## Mapping Framework × Shadow Tool

### Triptyque BETH (Ikigai ⊃ Life Wheel ⊃ Muse)
- **Ikigai 9 A3** (Ed/Kelly/Gordon/Claire + Isaac/Lamarr/Bortus/Alara/Klyden) → **Obsidian** (mirror local canon) + **state.json** bus
- **Life Wheel 8 LD** (Book/Saru/Culber/Tilly/Stamets/Burnham/Reno/Georgiou) → **Baserow** (cloud LD00 ZORA) + **Obsidian** (canonical mirror)
- **Muse Libération DEAL** (Dal/Rok-Tahk/Zero/Gwyn) → **Affine** (workspace DEAL blueprints)

### Triptyque MORTY (12WY ⊃ PARA ⊃ DEAL)
- **12WY 5 disciples** (Pike/Una/M'Benga/Chapel/Ortegas) → **Baserow** (12WY Warp Core + Scorecard + Time Use) + **state.json** bus
- **PARA 4 lettres** (Picard/Spock/Geordi/Data) → **Supabase** (cloud BE) + **Obsidian** (canonical local mirror)
- **DEAL via Data** (imbrication Plan §3.1) → **Affine** + **Supabase** (via Data chef d'orchestre)

### GTD Cerritos = bus horizontal
- **5 stages** (Mariner/Boimler/Tendi/Rutherford/Freeman) → **Plane.so** (workspace GTD) + **state.json** bus (Mariner capture raw_input_preview)

## Direction sync (Cloud ↔ Local)

```
[Supabase Cloud BE] ⇄ [Vercel FE Life-OS-2026] ⇄ [Obsidian local vault]
        ↕                                    ↕
[Baserow Cloud mobile]              [Plane.so GTD workspace]
        ↕                                    ↕
        [Affine DEAL workspace]
        ↕
        [state.json bus canonique]
```

## Failover Protocol

1. **Supabase down** → Obsidian local mirror + state.json bus degrade gracefully
2. **Baserow down** → Local `_baserow_export.json` snapshot + 12WY bascule filesystem
3. **Obsidian corruption** → Vercel Life-OS-2026 frontend = source of truth temporaire
4. **Affine down** → Obsidian mirror DEAL blueprints
5. **Plane.so down** → state.json bus `stage="captured"` continue, GTD replay on recovery
6. **state.json bus down** → STOP Symphony Runtime, escalate A1 Morty → A0 board observer

## W1 Activation Checklist (avant Runtime Symphony)

- [x] Supabase Cloud project `hjweyhpmrxqsxfbibsnc` LIVE (D1 verified via Vercel env vars)
- [x] Vercel project `life-os-2026` (Vite + Node 24.x) PROMOTED prod (D1 verified SHA `b933e4e`)
- [x] Baserow workspace configuration documented (LD00 ZORA + 12WY Warp Core + Scorecard + Time Use tables)
- [x] Obsidian vault structure `20_Life_OS/24_PARA_Enterprise/` aligned (7 dossiers canon patchés 2026-06-21)
- [x] Affine workspace DEAL structure documented (4 stages × 2 A3 + Index)
- [x] Plane.so workspace GTD 5-stage structure documented
- [x] state.json bus W1 stage="snw_planning" populated
- [ ] **HITL pending A0** : activation Runtime Symphony en production (D7 = A0 board observer décide)

## Mapping state.json bus ↔ 5 Shadow tools

| Tool | state.json key | Type |
|---|---|---|
| Supabase | `para_bucket` (firmé par Picard) | string (Projects/Areas/Resources/Archives) |
| Baserow | `life_wheel_domain` (LD01-LD08) + `12wy_discipline` (5 disciples) | string enum |
| Obsidian | `agent_path` (A0→A1→A2→A3 routing) | string with `>` separators |
| Affine | `stage` (DEAL D/E/A/L) | string enum |
| Plane.so | `next_step` (Cerritos 5-stage routing) | string with `A3:` prefix |

## D8 cross-applicability (Codex/Hermes/Gemini)

- **Codex** (Q4 2026 stabilisation) : code review sur routing logic
- **Hermes** (Q4 2026 stabilisation) : messaging long-running sur sync state
- **Gemini** (Shadow L0) : transcription vidéos A0 si capture routing
- **Claude (CC, présent)** : orchestration 5 tools + state.json bus maintenance

## Anchors canon absolus

- `C:\Users\amado\.claude\plans\fancy-hugging-bengio.md` §3.2 (matrice A1×A2×A3) + §3.7 (state.json bus) + §14 (Skills Multi-Workflow)
- `C:\Users\amado\ASpace_OS_V2\20_Life_OS\00_Gatekeepers_Beth_Morty\A1_Morty_Spec.md` (routing matrix 6 ships)
- `C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\A2_Discovery_ZORA_Spec.md` (Baserow LD00)
- `C:\Users\amado\ASpace_OS_V2\20_Life_OS\23_12WY_SNW\A2_Curie_SNW_Spec.md` (12WY Warp Core Baserow)
- `C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\A2_Computer_Enterprise_Spec.md` (Supabase cloud BE)
- `C:\Users\amado\ASpace_OS_V2\20_Life_OS\25_GTD_Cerritos\A2_HoloDeck_Cerritos_Spec.md` (Plane.so GTD)
- `C:\Users\amado\ASpace_OS_V2\20_Life_OS\26_DEAL_Protostar\A2_HoloJaneway_Protostar_Spec.md` (Affine DEAL)
- `C:\Users\amado\ASpace_OS_V2\20_Life_OS\23_12WY_SNW\W1_Quarter_Intent_Q3_2026.md` (Quarter Intent parent)
- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\40_SYMPHONY_BUS\state.json` (bus canon)