---
name: sym_supabase_drain
description: Drain `40_SYMPHONY_BUS/pending_upserts.ndjson` sidecar into Supabase `public.symphony_state` via `mcp__supabase__execute_sql`. Idempotent upsert via session_id ON CONFLICT. Trigger : every 5 minutes or manual `/sym-drain-now`. Use when state_writer.py appended a line to the sidecar and it hasn't yet reached Supabase.
domain: L2 Observability slot — meta-état Symphony
kernel: L1/L0 bus sémantique
source: U1 ship 2026-07-03 + canon sister `symphony-supabase.spec.md` + R3 swarm brief
created: 2026-07-03
doctrine_anchors: ADR-META-001 D1/D5/D7, ADR-LOOP-003 (sidecar = signals), ADR-AAAS-PRICING-001 (cost discipline)
sister: `wiki/hand_offs/u1_symphony_supabase_sink_shipped_2026-07-03.md`
related: `/canon-batch-spawn` (batch sister), `/swarm-orchestrator` (consumer pattern), `/Multi-Backend-Router` (route to MCP-vs-CLI)
---

# 🔌 sym_supabase_drain

> **Mission** : drainer le sidecar `40_SYMPHONY_BUS/pending_upserts.ndjson` dans la table `public.symphony_state` (Life OS Supabase, project `hjweyhpmrxqsxfbibsnc`) via `mcp__supabase__execute_sql`. Idempotent : `INSERT ... ON CONFLICT (session_id) DO UPDATE`. Best-effort, ne raise jamais.

## Triggers

| Trigger | Action |
|---|---|
| Trigger 1 — cron-like | toutes les 5 min (cron heartbeat gated A0 ; ne s'auto-installe PAS sans GO A0 per Posture C) |
| Trigger 2 — manuel | `/sym-drain-now` slash command (à créer, pas un scope de ce skill) |
| Trigger 3 — wakeful | avant chaque W13 scorecard (Chapel) |
| Trigger 4 — assertion | si `pending_upserts.ndjson` > 1000 lignes → drain synchrone |

## Étapes (toujours best-effort)

1. **Read sidecar** : ouvre `C:/Users/amado/ASpace_OS_V2/00_Amadeus/40_SYMPHONY_BUS/pending_upserts.ndjson`. Si absent → exit silencieux.
2. **Parse NDJSON** : chaque ligne est un dict JSON (state-bus.v1). Erreur parse → log + skip la ligne.
3. **Validate** : `session_id` (text non-vide), `cycle`, `week`, `agent_id` obligatoires. Skip lignes invalides.
4. **Build SQL** : `INSERT INTO public.symphony_state (...) VALUES (...) ON CONFLICT (session_id) DO UPDATE SET ... RETURNING session_id`.
5. **Invoke** : `mcp__supabase__execute_sql(project_id="hjweyhpmrxqsxfbibsnc", query=sql)`.
6. **Rotate** : si retour success → mv sidecar vers `pending_upserts.processed-YYYYMMDD-HHMMSS.ndjson` + append log à `wiki/log.md`.
7. **D5 receipt** : log ligne `**{date}** : sym_supabase_drain drain OK — {N} rows, {M} skipped. Sidecar rotated to {path}.`

## Anti-patterns

- ❌ Utiliser `requests.post` sur `/rest/v1/symphony_state` — 401 confirmé (D6 #NEW 2026-07-03).
- ❌ Lire/Afficher le contenu de `pending_upserts.ndjson` (données A0-private).
- ❌ Drainer > 100 lignes sans batcher via B1 (risk: MCP timeout).
- ❌ Hard-delete le sidecar — toujours `_YYYYMMDD-HHMMSS.ndjson` rotation (D4 append-only).

## Cross-refs

- `state_writer.py::_sync_to_supabase()` — producer
- `sym_base.spec.md` (Twin canon)
- `symphony-supabase.spec.md` (L2 adapter spec)
- `supabase-specifics.md` (L2 adapter standard)
- `wiki/hand_offs/u1_symphony_supabase_sink_shipped_2026-07-03.md` (U1 D5 receipts)
