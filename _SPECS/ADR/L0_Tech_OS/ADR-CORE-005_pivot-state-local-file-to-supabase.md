---
id: ADR-CORE-005
title: Pivot kernel — state local bus sémantique : file → Supabase table (long-horizon, anti-paperclip D6)
date: 2026-07-03
author: A0 jumeau numérique (CC-M3) — réponse A0 GO immédiat R5
status: PROPOSED
ratified: null (A0 ratify after W13 verdict)
layer: L0 — Kernel OS / Architecture pivot
preserves:
  - ADR-META-001 D1 (verify-before-assert), D6 (root-cause collection)
  - ADR-SOBER-002 Anti-paperclip (no auto-promote; pivot gated)
  - ADR-LOOP-001 §3 (verifier read-only, jamais d'auto-vérification)
  - ADR-A0-L-META-001 (4-layer identity preservation — state file/table is the meta-OS thread)
  - ADR-HERMES-001 (Nous/workspace persistence invariant)
sister:
  - u1_symphony_supabase_sink_shipped_2026-07-03.md (U1 livraison — précurseur canon)
  - wikipedia/hand_offs/audit_supabase_symp_config_2026-07-03.md (audit 3 couches)
  - 05_OSS_Twin/symphony/L2/symphony-supabase.spec.md (canon twin)
  - 05_OSS_Twin/symphony/agent-os/standards/supabase-specifics.md (standard canon twin)
  - ~/.claude/plans/plan-strategie-cc-l1-zora-macro.md §5 (U1 alignement canon)
tags: [#ADR #kernel-pivot #state #supabase #antifragility #l0-os ]
---

# ADR-CORE-005 — Pivot kernel : state local file → Supabase table

## Décision (D4 short)

L'état du bus sémantique Symphony (`40_SYMPHONY_BUS/state.json`) **reste la source de vérité locale** ; **Supabase `public.symphony_state` devient la source de vérité canonique inter-harness** (CC, Hermes, MiniMax, Shadow L1 Agent Zero). Le sidecar `pending_upserts.ndjson` est le canal de transition (D5-receipt 2026-07-03). Le pivot n'est **PAS** une bascule, mais une **sécurisation multi-couches**.

## Rationale (Pourquoi maintenant)

1. **D6 #NEW 2026-07-03** : `state.json` local **corrompu** (apostrophe unicode U+2019 non échappée + dict merge in lieu de replace). Backup forcé en `_TRASH_2026-07-03_state_corruption/`. Sans pivot, l'incident se reproduit à chaque input contenant `'`/`'`/`"` non échappés.
2. **D6 #NEW 2026-07-03 — 401 anomaly** : REST v1 curl avec anon/sbp env vars échoue. Le pivot impose **un seul** chemin write D5-receipté (`mcp__supabase__execute_sql`) — supprime la divergence de comportement entre canaux.
3. **D7 — coût d'escalation A0** : le pivot n'est PAS un papier-clipper (auto-promote) — il est **gated A0 explicitement** à la décision A0 `GO R5 immédiat` (reçu 2026-07-03).
4. **Antifragility** : un OS qui dépend d'un seul fichier plat (`state.json`) est fragile. Le pivot tables la rend **stronger under stress** (per ADR-SOBER-002 Anti-fragilité Rick — les pivots kernel sont la spécialité S1, mais R5 est **catalogue-spécifie** ; l'activation effective du pivot kernel complet reste S1 Rick en 2027 L0).
5. **Multi-harness convergence** : CC, Hermes, MiniMax, et Shadow L1 Agent Zero partagent la même vue Symphony state. Le pivot force un **single source of truth** cross-harness, avec sidecar local best-effort comme buffer.

## Conséquences (What changes)

### A. Architecture

```
Local (CC runtime):
  state.json — read-cache hot, single source for CURRENT session
  pending_upserts.ndjson — append-only sidecar, best-effort drain
  state.writer — productrice (Merge canon) + sink best-effort

Supabase Cloud (canonical store):
  public.symphony_state — UPSERT idempotent per session_id
  = source of truth for cross-harness reads

Drain pipeline (D5-receipt 2026-07-03):
  sym_supabase_drain skill — MCP-execute_sql service_role path
  R4 yamls emit on lifecycle hooks
  Sidecar rotated to {name}.processed-{YYYYMMDD-HHMMSS}.ndjson
```

### B. Failure mode recovery (D4)

1. JSON local corrompu (apostrophe non échappée) → sidecar drain continue, **état canonique intact côté Supabase** ; restauration locale triviale par copie depuis Supabase.
2. 401 sur REST v1 → fallback obligatoire vers `mcp__supabase__execute_sql` (l'unique canal D5-receipté).
3. Drain sidecar accumule > 1000 lignes → trigger synchrone + split en chunks (D7 anti-fire-supabase).

### C. Rejeté (alternatives considered)

- **Hibernate state.json entirely** : rejette car perd la capacité read-cache offline (CC runs in container with intermittent Supabase connectivity).
- **Keep state.json only (no pivot)** : rejette car l'incident D6 corruption + 401 démontre la fragilité single-source.
- **Force immediate full pivot file→table before W13** : rejette car D7 — c'est exactement le type de réflexe D1-réflexe-change-on-OS qu'on a gravé dans ADR-META-001. Le pivot se fait en **deux temps** : (1) état PROPOSED maintenant (ce document), (2) ratify A0 après verdict W13.

## Anti-patterns

- ❌ Switch hard du runtime : aucune bascule. Les deux sources coexistent.
- ❌ Auto-promote state.json → Supabase lors d'un incident (paperclip).
- ❌ Drain plus fréquent que 5min sans GO A0 (Posture C).
- ❌ Hard-delete state.json ou sidecar (D4 append-only respecté).
- ❌ Écrire dans Supabase sans passer par sidecar-drain (le seul chemin D5-receipté).

## Stop-conditions

1. Si **W8 mid-parcours** (T2 GTM entrée) montre que le sidecar drain cause des blocages → STOP, suspendre drain, audit patterns.
2. Si la W13 verdict Chapel (scorecard) sur wager Mindsets real-test ≥50% **échoue** → suspendre le pivot et re-évaluer (le pivot n'est pas un instrument de mesure, c'est un instrument de persistance).
3. Si la single-source pivot créé une dépendance critique non-vue (D6 surfacing feature) → rollback via sidecar-fallback (state.json redevient source de vérité temporaire).

## Vérification post-pivot (D5 receipts)

À chaque W (W3, W6, W8, W10, W12) :
- count(state.json LOC) ≤ 200 (D4 lecture rapide)
- count(symphony_state rows) ≥ count(drain_events)
- drain_latency_ms p95 ≤ 5000 (5min budget)
- sidecar_row_count = 0 entre W (sinon alert)

## Cross-refs

- `state_writer.py::_sync_to_supabase` (productrice sidecar)
- `sym_supabase_drain` skill (R3 swarm canonique)
- `symphony-supabase.spec.md` (canon twin)
- `supabase-specifics.md` (canon twin standard)
- `wiki/hand_offs/u1_symphony_supabase_sink_shipped_2026-07-03.md` (U1 livraison)
- `plan-strategie-cc-l1-zora-macro.md` §5-U1 (alignement canon stratégique)

## Sacred exclusions respectées

- Pas de modification state.json runtime (le pivot n'altère pas le producteur local, seulement le sidecar consumer).
- Pas de CronCreate (drain gated A0).
- Pas de hard-delete (sidecar rotated, jamais rm).
- ADR créé en **PROPOSED** (non RATIFIED) — A0 ratify après W13 verdict (D7 delay).
