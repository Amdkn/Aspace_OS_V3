---
title: Mindsets Canon — Discipline Porting Layer (L1+L2 isomorphic) + Hooks + Fable baselines
date: 2026-06-25
author: A0 jumeau numérique (Opus 4.8, meta layer)
tags: [mindsets, dispatch-doctrine, fable, m3-discipline, hooks, isomorphy, sobriety, anti-paperclip]
status: canon
---

# Handoff — Mindsets Canon Session (2026-06-25)

## Why (the unlock)

MiniMax-M3 is the runtime workhorse (~99% of work, $50/7B-token plan) but **lazy by
default**: measured this session, it skips the reason→observe→re-evaluate loop ~half
the time. That IS the "L1 agents too lazy" symptom A0 named. The fix is **explicit
instruction**, not a better model. This session forged that instruction layer:
disposition (Mindsets) + mechanism (Dispatch Doctrines), isomorphic L1=L2, all
grounded in measured M3-vs-Fable discipline gaps. **Posture C (artifact-first): zero
cron activated, capability gated behind A0 HITL.**

## What was built — `.claude/mindsets/` (23 files, D1 verified)

**L1 Life OS — disposition (per A1 gatekeeper):**
- `Beth_Mindset.md` (gate ALIGN / Ikigai-Life Wheel)
- `Morty_Mindset.md` (gate FOCUS / 12WY Definition-of-Done)
- `Rick_Mindset.md` (gate SOBER / anti-fragility, L0 kernel, ~1×/an)

**L1 — mechanism (dispatch to A3):**
- `Beth_Dispatch_Doctrine.md` — Orville 9 (4 pillars + 5 horizons) · Discovery 8 (Life Wheel) · Protostar 4 (DEAL, delegated to Morty's Data/Archives)
- `Morty_Dispatch_Doctrine.md` — Curie/SNW 5 · Computer/Enterprise 4 PARA (Data carries DEAL upkeep) · Cerritos 5 GTD (80% focus). Russian doll **12WY ⊃ PARA ⊃ DEAL**

**L2 Business OS — isomorphic mirror (A1↔B1, A2↔B2, A3↔B3):**
- `B1_Manifesto.md` — shared isomorphy lock + **Sobriety gate: NO A1→B1 cron without A0 HITL** (anti-paperclip trigger #5, ADR-SOBER-002). HITL channel = **Terminal** (Telegram deferred).
- `Jerry_Mindset.md` (gate SYSTEMIZE / E-Myth) · `Summers_Mindset.md` (gate SHIP / variant+ICP)
- `Jerry_Dispatch_Doctrine.md` — 8 Business Domains → 53 B3
- `Summers_Dispatch_Doctrine.md` — 3 AaaS Captains (product axis) × 8 domains matrix
- 8× `B2_*_Dispatch_Doctrine.md` — GreenLantern/Batman/Flash/Superman/JohnJones/Cyborg/WonderWoman/Aquaman, each B2→its B3 squad with per-B3 triggers

**Shared evidence + dormant artifacts:**
- `_DISCIPLINE_BASELINES.md` — single source of truth, 2 baselines côte à côte, **Fable ★ = mimetic priority**
- `Telegram_HITL_Mindset.md` + `Telegram_HITL_Dispatch.md` (Minimax) — DORMANT (deferred, Terminal chosen)
- `DesktopCommander_Mindset.md` + `DesktopCommander_Dispatch.md` (Minimax) — config `true` pending CC restart

The 5 gates, isomorphic skeleton, different step-1 veto:
**ALIGN** (Beth) · **FOCUS** (Morty) · **SOBER** (Rick) · **SYSTEMIZE** (Jerry) · **SHIP** (Summers).
Dispatch law gravée partout: *gatekeeper decides+routes, never executes; manager dispatches; sub-agent executes & reports up.*

## Canonical counts (D1)
A1=3 · A2=6 · A3=35 (9+8+4+5+4+5) · B1=2(+Rick sobriété transverse) · B2=8 · B3=53. Total 107 agents.
Concurrency: Beth 9+8=17 > 16 → stagger ; Morty 5+4+5=14 ≤ 16 → one pass ; Jerry full sweep 53 > 16 → pipeline + shard (53×~19 ≈ 1007 > 1000 lifetime).

## Measured discipline — M3 vs both baselines (Fable ★ = mimetic priority)

| Habit | M3 | Opus 4.8 | Fable-5 ★ | gap vs Fable |
|---|---|---|---|---|
| reasons before first action | 53% | 74% | 88% | **−35 (top)** |
| re-evaluates after a result | 50% | 67% | 87% | **−37 (top)** |
| turns containing reasoning | 51% | 68% | 82% | −31 |
| runs real test after editing | 33% | 50% | 63% | −31 |
| reads file before editing | 91% | 100% | 58% | +33 (M3 wins — hold) |
| runs a check after editing | 80% | 100% | 63% | +17 (M3 wins — hold) |
| tool error rate | 5.9% | 3.7% | 5.2% | ≈ |

Samples: M3 14148 beats/363 sessions · Opus 116/2 (thin) · Fable 913/25 (PUBLIC armand0e dataset).
**Mimetic rule:** close toward Fable on the reasoning loop; do NOT regress M3's strong hygiene to match Fable's weaker numbers.

## Hooks wired this session (3, settings.json, active next CC restart for SessionStart; Stop confirmed live)
- `posttooluse-test-after-edit.ps1` — PostToolUse Write|Edit|MultiEdit, code-files only, 120s timeout, log-only → `.claude/logs/test-after-edit.log`. Mechanizes M3's 33% real-test gap. Distinct from Rick-vetoed hard-block Hook 1.
- `sessionstart-log-digest.ps1` — SessionStart smart-read: tail+noise-filter canon log (last 12 curated) + turn-journal (last 8). Never cat.
- `stop-log-append.ps1` — Stop, 1 compact line/turn → `.claude/logs/turn-journal.md` (isolated from canon; canon stays curated).

## Fable kit fix (D6 — Windows portability)
The kit's `analyze_discipline.py` used `subprocess grep` whose `"` quoting breaks on Windows → 0 sessions. Fix: additive `analyze_discipline_win.py` (pure-Python os.walk monkeypatch, original untouched). New adapter `analyze_vs_fable_dataset.py` compares M3 vs the public Fable-5 dataset (both native CC JSONL → no conversion). Sample 24.5 MB at `.claude/logs/_fable_dl/` (huggingface_hub, re-downloadable). Both scripts in the Fable Mindset kit `scripts/`.

## A0 decisions locked
- **F-2 (HITL channel):** Terminal now; Telegram deferred (plugin ✗ Failed, premortem + 2 dormant files exist, 4 gates pending). Recorded in `B1_Manifesto.md §Sobriety`.
- **F-3 (L2 Russian-doll):** does NOT map mechanically — no native DEAL analogue at L2. No file created.
- **Baselines:** keep both côte à côte, **Fable = mimetic priority**, canonical `_DISCIPLINE_BASELINES.md`.
- **Desktop Commander:** config fixed to `true` (line 209) by Minimax with A0 GO; pending CC restart (D6 #4 static registry).

## Pending (A0 actions)
- CC restart → activates SessionStart digest hook + Desktop Commander + (deferred) reloads registry.
- Per-cron GO (HITL) before ANY L1/L2 cron activation. Solaris H10 weekly = natural first candidate when A0 decides.

## Anti-pattern avoided (D8 cross-agent)
The Desktop Commander breakage (2026-06-16) was "guess without verify" (assumed a `.mcp.json` duplicate that didn't exist). This session every claim is a file-line receipt (settings.json:209, the 2 stale "to create" refs, the binary). Trust = verifiable receipts, not promises.
