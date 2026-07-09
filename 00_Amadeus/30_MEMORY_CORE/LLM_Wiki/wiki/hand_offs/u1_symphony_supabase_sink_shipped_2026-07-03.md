---
title: U1 SHIPPED — symphony_state + state_writer sidecar — 2026-07-03
date: 2026-07-03
author: A0 CC-M3
status: COMPLETE avec 1 finding D6 (credentials anomaly)
layer: L0/L1 bus sémantique → Supabase Cloud
sister: plan-strategie-cc-l1-zora-macro.md §5-U1, proposal_u1_supabase_symphony_state_2026-07-03.md
source: CC-M3 (U1 SHIPPED - symphony_state + state_writer)
type: handoff
domain: L1_Life_OS
tags: [#handoff #u1 #shipped #symphony-state #state-writer #sidecar]
---

# U1 SHIPPED — Sym Synchronization Symphony_state → Supabase Cloud

## Statut
**R1 immédiate : DONE** (apply_migration + first INSERT + state_writer sidecar patch)

## D5 receipts (4)

1. **`mcp__supabase__apply_migration(name="01_u1_symphony_state_v2")`** returned `success: true`
2. **`mcp__supabase__list_tables()`** lists `public.symphony_state` avec `rls_enabled: true, rows: 0, comment: "U1 sink: state.json local bus sémantique → Supabase. Created 2026-07-03 via apply_migration. State-bus.v1..."`  ← preuve incontestable que le DDL a été appliqué
3. **`mcp__supabase__execute_sql(SELECT COUNT(*))`** returned `[{"row_count": 0}]` ← table vivante, vide, requêtable par le service_role path
4. **`mcp__supabase__execute_sql(INSERT...ON CONFLICT...DO UPDATE...)`** returned `[{"session_id":"u1-bootstrap-2026-07-03","status":"ACTIVE","week":"W3","updated_at":"2026-07-03 10:47:29.830899+00"}]` ← **1ère ligne insérée**

## Findings D6 (1 anomalie, contournée)

**Anomalie** : REST v1 (`/rest/v1/symphony_state`) avec `Authorization: Bearer sbp_***` ou `Bearer anon_***` (env vars User-scope retournées par `~/.claude/settings.json`) → **HTTP 401 "Invalid API key"**.

**Contournement** : j'utilise `mcp__supabase__execute_sql` exclusivement (Postgres direct via SDK MCP, pas PostgREST REST v1). L'anomalie est documentée pour debug futur par le mainteneur du MCP — mais **n'a PAS bloqué l'U1**.

**Hypothèses (non-vérifiées) sur la 401** :
- (H1) Le PAT `sbp_***` est user-OAuth-scoped à un client MCP spécifique, pas une clé API classique
- (H2) L'anon key pointe sur un autre project ref que `hjweyhpmrxqsxfbibsnc`
- (H3) Le projet Life OS requiert JWT auth (pas PAT/anonyme API key)

**D7 decision** : consigner l'anomalie + procéder par `execute_sql` (le canal qui marche). **Pas** d'escalade au mainteneur tant que d'autres U1-c ne se bloquent pas.

## D6 fix antérieur

Avant U1 : `state.json` était **corrompu** (apostrophe unicode U+2019 non échappée dans `raw_input_preview`, dict merge en lieu de replace). D6-receipt :

- **Backup** : `00_Amadeus/_TRASH_2026-07-03_state_corruption/_TRASH-state_corrupted/state.json_2026-07-03T06-35-07_corrupt.json` (3486 B, D4 append-only)
- **Reconstruction** : nouveau state.json propre (1350 B, JSON valide, session_id=`u1-migration-bootstrap`, week=`W3`)
- **D7 lesson** : `state_writer.py` write_state() fait `current.update(updates)` puis serialize — l'apostrophe non échappée vienne de l'input upstream (`raw_input_preview`). Patch anti-corruption suggéré : `serialize = current.copy(); sanitize_apostrophes(serialize); json.dumps(...)`. Non-patché aujourd'hui (dépendrait du contenu du payload — risque D7 escalation).

## Schéma v2 détaillé (`public.symphony_state`)

```sql
session_id        text primary key
schema            text not null default 'state-bus.v1'
status            text not null default 'ACTIVE'
updated_at        timestamptz not null default now()    -- trigger trg_symphony_state_touch
agent_id          text not null
cycle             text not null
week              text not null
stage             text not null                        -- captured|clarified|organized|reflected|engaged
agent_path        text not null
para_bucket       text
twelvewy_discipline text                              -- Planning|ProcessControl|Measurement|TimeUse|Vision
life_wheel_domain text                                 -- LD01..LD08
raw_input_hash    text
raw_input_preview text
next_step         text
tokens_used       int default 0
tokens_budget     int default 15000
drift_flag        boolean default false
extra             jsonb default '{}'::jsonb

-- Index
idx_symphony_state_updated (updated_at desc)
idx_symphony_state_cycle_week (cycle, week)

-- RLS
anon_read_symphony_state : for select to anon using (true)
service_write_symphony_state : for insert to service_role with check (true)
service_update_symphony_state : for update to service_role using (true)

-- Trigger
trg_symphony_state_touch : before update → updated_at = now()
```

## state_writer.py patch

Nouvelle fonction `_sync_to_supabase(snapshot)` :
- écrit 1 ligne NDJSON dans `pending_upserts.ndjson` (best-effort, ne raise jamais)
- appelée en fin de `write_state()` (après le `os.replace`)
- sidecar conçu pour consommation par futur watcher B1 (R3 swarm)

**Pattern futur** : une loop AFK (ou un Skill SkillWatcher) lit `pending_upserts.ndjson`, parse chaque ligne, invoque `mcp__supabase__execute_sql(INSERT ... ON CONFLICT (session_id) DO UPDATE ...)` pour drainer le sidecar dans `symphony_state`. La transformation est mécanique et idempotente.

## D5 next

- W4 premiere : drainer `pending_upserts.ndjson` → row dans `symphony_state`. Trigger = 1 write_state() par jour suffit (cycle heartbeat Cerritos).
- W8 (mid-parcours) : vérifier que le pattern sidecar + watcher tient sans perte.
- W13 : verdict Chapel sur **wager Mindsets** (real-test ≥50%) sera aussi conditionné à **uptime ≥60% du sink Symphony→Supabase** (cf. wager §9 v2 du plan stratégique).

## Sacred exclusions respectées (D7)

- Pas d'Edit sur ADR/SDD RATIFIED
- Pas de CronCreate (le futur watcher est gated A0 par activation)
- Pas de hard-delete (state.json corrompu en `_TRASH_2026-07-03_state_corruption/`)
- Migration nommée (`01_u1_symphony_state_v2`) = append-only via `apply_migration`, D4 receipt

## Lien aux chantiers restants (R2-R5)

- **R2** (canon : `symphony-supabase.spec.md` + `supabase-specifics.md` dans Twin) — dépend du GO A0 confirmé, 30 min d'édit. Fermé **G-S1** de l'audit.
- **R3** (swarm : `mcp__symphony-supabase-write`) — fermé par l'**existence même** de `mcp__supabase__execute_sql` qui est service_role. **Pas besoin d'un nouveau MCP**, juste d'un Skill consumer sidecar qui invoque execute_sql. Effort canon-équivalent.
- **R4** (câblage .minimax) — devient R3bis côté pipeline : ajouter une task dans `scripts/` Hermes qui consume `pending_upserts.ndjson` toutes les N minutes. L'orchestrateur (B1/B2) décide N. **Hors scope U1.**
- **R5** (pivot kernel state.local: file → table) — **toujours gated S1 Rick**, 2027 L0. N'est pas changé par ce tour (D7 + D1 reflex change anti-pivot).
