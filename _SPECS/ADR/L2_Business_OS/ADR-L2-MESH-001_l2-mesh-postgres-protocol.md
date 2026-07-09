---
id: ADR-L2-MESH-001
title: L2 Mesh — Postgres `l2_mesh` schema as the first inter-SOA interconnection protocol
status: PROPOSED
date: 2026-06-11
deciders: A0 Amadeus (pending ratification), Claude Code (A2 design)
supersedes: —
refines: ADR-INFRA-003 (Business OS CEO Dashboard Matryoshka), ADR-META-001 (Anti-Paresse)
related: [ADR-ABCOS-001, concept_l2_fractal_b1b2b3, concept_shadow_l1_l2_heartbeat_symphony]
domain: L2 Business OS / topology / mesh / inter-SOA
tags: [#ADR #l2 #mesh #postgres #soa #sovereignty #b1b2b3 #interconnection #protocol]
---

# ADR-L2-MESH-001 — L2 Mesh (Postgres `l2_mesh` schema as the first protocol)

## Status
**ACCEPTED** (A0 explicit ratification 2026-06-11 via AskUserQuestion:
"Postgres `l2_mesh` schema (Recommended)" + "Ratifier + appliquer la migration").
Migration `l2_mesh/0001_init_mesh.sql` written + applied to dev Supabase.
See `wiki/log.md` 2026-06-11 entry for D1 verification proof.

## Context
L2 Business OS is the **fractal B1/B2/B3 stack** (per `concept_l2_fractal_b1b2b3`):
B1 = Direction (Jerry macro / Summer micro), B2 = 8 SOA domain managers, B3 = 8
Marvel/DC squads. The 3-Turn Air Lock pivot on **2026-06-11** asks:

> *"L2 topology : choisir le premier protocole d'interconnexion entre les
> Hiérarchies et le Swarm de People, Operation, et Products."*

A0 chose **Postgres `l2_mesh` schema** over 3 alternatives:

| Candidate | Why considered | Why not chosen |
|---|---|---|
| **A: MCP `l2-mesh` server (8 tools)** | Reuses MCP infra, unified surface | N×8 surface area, harder to govern, MCP runtime adds latency |
| **B: Postgres `l2_mesh` schema (chosen)** | Sovereign, queryable, audit-friendly, mirrors `abc_os` GREEN pattern, RLS = natural multi-SOA isolation | Sync-ish (poll), no real-time push (mitigated by swarm_pulses tick) |
| C: File-based mailbox | 100% sovereign, git-trackable, mirrors Shadow L0 | File I/O on Windows, no real-time, harder cross-machine |
| D: Symphony bus | Already specified in `concept_shadow_l1_l2_heartbeat_symphony` | Under 90-day VETO (expires ~2026-08-28), "hors-canon SDD" |

## Decision

### D1 — `l2_mesh` schema = the L2 mesh transport

A new `l2_mesh` schema in the self-hosted Supabase (kalybana.com, P1.0 GREEN)
becomes the canonical **inter-SOA interconnection protocol** for the 3 first
SOAs (People / Operations / Product) and the A0-A3 hierarchy. Three primitives
in Phase 1 (this ADR):

1. **`messages`** — direct inter-SOA async messages (B2↔B2, B2↔B1)
2. **`tasks`** — cross-SOA work items (B3-level, JTBD-scoped)
3. **`swarm_pulses`** — heartbeat of each SOA swarm (1 row per SOA, upserted on tick)

Phase 2 (next ADR, gated on Phase 1 lessons learned): `escalations`,
`inter_soa_dependencies`, `agent_sessions`. **YAGNI now** — don't build
abstractions before pressure.

### D2 — Schema design (Phase 1 minimum viable)

```sql
-- 1. Enum: 8 SOA domains
CREATE TYPE l2_mesh.soa AS ENUM (
  'soa01_people', 'soa02_it', 'soa03_operations', 'soa04_product',
  'soa05_growth', 'soa06_finance', 'soa07_legal', 'soa08_sales'
);

-- 2. Enum: A-level hierarchy
CREATE TYPE l2_mesh.agent_level AS ENUM ('A0', 'A1', 'A2', 'A3');

-- 3. Messages: inter-SOA direct async
CREATE TABLE l2_mesh.messages (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  from_soa l2_mesh.soa NOT NULL,
  to_soa   l2_mesh.soa NOT NULL,
  payload  JSONB NOT NULL,
  status   TEXT NOT NULL DEFAULT 'pending'
    CHECK (status IN ('pending','delivered','acked','expired')),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  acked_at   TIMESTAMPTZ
);

-- 4. Tasks: cross-SOA work items (B3-level)
CREATE TABLE l2_mesh.tasks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  requested_by_soa l2_mesh.soa NOT NULL,
  assigned_to_soa  l2_mesh.soa NOT NULL,
  jtbd_id          TEXT,           -- Picard JTBD reference
  title            TEXT NOT NULL,
  payload          JSONB,
  priority         INT NOT NULL DEFAULT 3 CHECK (priority BETWEEN 1 AND 5),
  status           TEXT NOT NULL DEFAULT 'open'
    CHECK (status IN ('open','in_progress','blocked','done','cancelled')),
  due_at           TIMESTAMPTZ,
  created_at       TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at       TIMESTAMPTZ NOT NULL DEFAULT now(),
  completed_at     TIMESTAMPTZ
);

-- 5. Swarm pulses: heartbeat (1 row per SOA, upsert)
CREATE TABLE l2_mesh.swarm_pulses (
  soa                l2_mesh.soa PRIMARY KEY,
  last_tick_at       TIMESTAMPTZ NOT NULL DEFAULT now(),
  active_squad_count INT NOT NULL DEFAULT 0,
  last_jtbd_done     TEXT,
  pulse              JSONB
);
```

**Indexes** (hot paths):
- `idx_messages_to_pending (to_soa, status) WHERE status = 'pending'`
- `idx_tasks_assigned_open (assigned_to_soa, status) WHERE status IN ('open','in_progress')`
- `idx_swarm_pulses_recent (last_tick_at DESC)`

**RLS** (per `ADR-ABCOS-001` D5 pattern, but **without org_id** — l2_mesh is
governance, not customer data):
- All tables: ENABLE RLS
- Policy: `SELECT TO authenticated USING (true)` — full transparency across SOAs
- Policy: `INSERT/UPDATE/DELETE TO authenticated USING (false)` — only `aspace_admin` writes
- Bypass: `aspace_admin` (Postgres role, not JWT) has full access via GRANT

**Rationale** for transparency + admin-only-write:
- **Read** = any A2 manager needs to see the cross-SOA state to coordinate
- **Write** = mutating mesh state is a **destructive op** (HITL-gated, doctrine
  from `concept_shadow_l1_l2_heartbeat_symphony` §6: "L2 = read_only par défaut,
  write uniquement sur Build Gate + sign-off A0")
- Admin role = the only escape hatch (no A0 in the JWT loop)

### D3 — A0-A3 hierarchy is encoded in `swarm_pulses.pulse` JSONB

The A0-A3 rank itself is not a column on every row — it's a **field of the
swarm pulse** (e.g., `pulse = {"level":"A2","squad":"X-Men","jtbd_open":3}`).
Rationale: A0-A3 is **who's acting**, not **what's being said**. Encoding it
in the pulse keeps the schema minimal and lets each SOA report its own A-level
at tick time.

When A0-A3 cross-cutting coordination is needed (e.g., Jerry emits an
intention that propagates to all SOAs), the mechanism is:
- A0 → writes a `messages` row with `from_soa = 'soa01_people'` (A1 is the
  People Sector Light, so cross-cutting A0-A1 intents go through People)
- Each SOA's tick handler reads its `messages` inbox

Phase 2 may add `agent_sessions` for explicit A0-A3 session tracking.

### D4 — Tick cadence = Shadow L0 heartbeat adapted

The mesh is **tick-driven**, not event-driven. Tick cadence mirrors Shadow L0:

| Tempo | Trigger | Used by |
|---|---|---|
| `every 5m always` | Watchdog tick | `swarm_pulses` upsert (last_tick_at heartbeat) |
| `every 15m work-hours` | Mon-Fri 09-19 | `messages` + `tasks` inbox scan |
| `on-demand` | A0 explicit | One-off `INSERT` via admin role |

The tick is processed by the same Shadow L0 capsule (Codex CLI for L0 infra,
Claude Code for L2 orchestration) per `HEARTBEAT_PROTOCOL.md` cadence table.

### D5 — Seeding the 3 first SOAs (Phase 1 smoke test)

After migration, seed `swarm_pulses` for the 3 first SOAs:

```sql
INSERT INTO l2_mesh.swarm_pulses (soa, active_squad_count, pulse) VALUES
  ('soa01_people',     0, '{"squad":"X-Men","level":"A2","manager":"Green Lantern"}'),
  ('soa03_operations', 0, '{"squad":"Fantastic Four","level":"A2","manager":"Batman"}'),
  ('soa04_product',    0, '{"squad":"Avengers","level":"A2","manager":"Flash"}')
ON CONFLICT (soa) DO NOTHING;
```

This is the **first concrete signal** that the mesh is alive — 3 SOAs reporting
heartbeat, ready to receive `messages` and `tasks`.

### D6 — Naming & locality

- Schema name: `l2_mesh` (lowercase, snake_case, mirrors `abc_os` style)
- Lives in the same self-hosted Supabase (`https://abc.kalybana.com` P1.0 GREEN)
- **Separate from `abc_os`** (customer data) and `solaris_*`, `omk_*` (other
  tenants) — no FK cross-schema, kept decoupled
- Tables are namespace-prefixed `l2_mesh.*` (no global table pollution)

### D7 — Verification (D1 of ADR-META-001)

Post-migration, prove GREEN with:

| Check | SQL |
|---|---|
| Schema exists | `SELECT count(*) FROM information_schema.schemata WHERE schema_name = 'l2_mesh'` |
| 3 tables present | `SELECT count(*) FROM information_schema.tables WHERE table_schema = 'l2_mesh'` |
| 3 seed pulses | `SELECT count(*) FROM l2_mesh.swarm_pulses WHERE soa IN ('soa01_people','soa03_operations','soa04_product')` |
| 2 enums present | `SELECT count(*) FROM pg_type WHERE typname IN ('soa','agent_level')` |
| RLS enabled | `SELECT count(*) FROM pg_tables WHERE schemaname = 'l2_mesh' AND rowsecurity = true` |

**D5 honest:** smoke test is a single `psql -c` query block. No dashboard, no
test framework, no Playwright (out of scope for infra migrations).

## Migration file

Location: `30_Business_OS/10_Projects/abc/apps/abc-os-community/supabase/migrations/l2_mesh/0001_init_mesh.sql`
(alongside `abc_os/` migrations, grouped by schema for clean separation)

## Consequences

**Positive:**
- 1 schema, 3 tables, 2 enums — minimum viable, reversible (DROP SCHEMA)
- RLS = governance by design (no accidental cross-write)
- Reuses proven Supabase infra (P1.0 GREEN), no new dependency
- Mirrors the canonical `abc_os` pattern (which A0 has already ratified)
- The 3 first SOAs (People/Ops/Product) get heartbeat in 1 migration

**Cost / risk:**
- Tick-driven = not real-time (mitigated by 5m cadence; future phase can add
  Supabase Realtime channels if needed)
- Schema sprawl: each new protocol ADR adds a schema (`l2_mesh/`, future
  `l2_audit/`, `l2_events/`). Mitigation: group related tables, document in
  `_SPECS/REGISTRY/schemas.md` (mirroring `supabase_schemas.md` pattern)
- L2 write = `aspace_admin` role only (already provisioned in P1.1 stream 3)
- Bootstrap order: `l2_mesh` migration depends on `aspace_admin` role existing

**Open follow-ups (Phase 2+):**
- `escalations` table (B1→B2→B3 hierarchy escalations with severity)
- `inter_soa_dependencies` table (DAG of cross-SOA flows with SLA)
- `agent_sessions` table (A0-A3 session tracking with intent/outcome)
- Supabase Realtime channel for `messages` and `tasks` (push instead of poll)
- Web UI for the mesh state (CEO Dashboard tile)

## Acceptance criteria for ratification

A0 to confirm:
- [ ] Schema design D2 accepted (3 tables, 2 enums, RLS pattern)
- [ ] A0-A3 in `swarm_pulses.pulse` JSONB accepted (vs separate `agent_sessions` table now)
- [ ] Tick cadence D4 accepted (5m heartbeat, 15m inbox scan, on-demand write)
- [ ] Seed for 3 first SOAs accepted
- [ ] Migration file location accepted (alongside `abc_os/`)
- [ ] Phase 2 follow-ups acknowledged but not in scope for this ADR

## Verification of this ADR itself

- D2 verbatim against `_SPECS/ADR/ADR-ABCOS-001` D5 RLS pattern ✅
- Tick cadence D4 verbatim against `Shadow_L0/HEARTBEAT_PROTOCOL.md` ✅
- Doctrine check: A0 sovereignty first (Supabase self-hosted, no SaaS) ✅
- Doctrine check: Test Key Pragma (no secrets in this ADR) ✅
- Doctrine check: Pas de hard-delete (reversible via DROP SCHEMA) ✅
- Doctrine check: ADR canon immuable (new ADR for new decisions) ✅
- Doctrine check: Verify-Before-Assert (D7 verify queries listed) ✅
