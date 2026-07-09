---
title: U1 Proposal — table symphony_state dans Life OS Supabase (datasource upstream)
date: 2026-07-03
author: A0 CC-M3
status: PROPOSAL v2 — 3 corrections C1/C2/C3 intégrées, attend review A0 puis GO apply_migration
target_project: hjweyhpmrxqsxfbibsnc (Life OS, us-east-2, ACTIVE_HEALTHY)
source_format: 40_SYMPHONY_BUS/state.json (schema state-bus.v1)
sister: plan-strategie-cc-l1-zora-macro.md §5 (U1) + §6-G8 (dashboard 0% data)
source: CC-M3 (proposal U1 symphony_state table)
type: proposal
domain: L1_Life_OS
tags: [#proposal #u1 #supabase #symphony-state #datasource-upstream]
---

# U1 — Proposition : créer table `symphony_state` + sink dans state_writer.py

## Pourquoi maintenant

`state.json` local vit dans `00_Amadeus/40_SYMPHONY_BUS/` mais **n'alimente pas** le Web Desktop Life-OS-2026 sur Vercel (cf. plan stratégique §6-G8 : 19 tables Life OS existent, **toutes à 0 rows**). Sans uplink, le dashboard reste vide et l'observabilité A0 reste illusoire.

## D1 receipts

- Supabase project `Life OS` (`hjweyhpmrxqsxfbibsnc`) ACTIVE_HEALTHY, us-east-2, PG 17
- 19 tables UNIFIES en place, toutes à 0 rows
- `state.json` (12-handoff canon) contient 17 colonnes (champ plat) + `extra` JSONB
- `state_writer.py` lock atomique + tempfile + rename (D6-receipt 2026-06-21)

## Schéma v2 (D1-read + 3 corrections intégrées : C1/C2/C3)

```sql
-- Idempotent: sûr de rejouer la migration
create table if not exists public.symphony_state (
  session_id        text primary key,                       -- C1: la session EST l'identité (natural key)
  schema            text not null default 'state-bus.v1',
  status            text not null default 'ACTIVE',        -- INIT | ACTIVE | DONE | BLOCKED
  updated_at        timestamptz not null default now(),    -- timestamp canonique bus sémantique
  agent_id          text not null,                         -- ex 'A3:Boimler'
  cycle             text not null,                         -- ex 'Q3-2026'
  week              text not null,                         -- ex 'W1'
  stage             text not null,                         -- captured | clarified | organized | reflected | engaged
  agent_path        text not null,                         -- 'A1:Beth > A2:Cerritos > A3:Boimler'
  para_bucket       text,                                  -- '01_Projects/life-os-2026'
  twelvewy_discipline text,                                -- Planning | ProcessControl | Measurement | TimeUse | Vision
  life_wheel_domain text,                                  -- LD01..LD08
  raw_input_hash    text,                                  -- sha256:abc123
  raw_input_preview text,                                  -- 1ère phrase trimmée
  next_step         text,                                  -- 'A3:Boimler'
  tokens_used       int default 0,
  tokens_budget     int default 15000,
  drift_flag        boolean default false,
  extra             jsonb default '{}'::jsonb
);

-- C2: uploaded_at supprimé — updated_at fait foi.

-- C3: RLS strict — anon SELECT, service_role INSERT/UPDATE
alter table public.symphony_state enable row level security;
create policy "anon_read_symphony_state"  on public.symphony_state for select to anon          using (true);
create policy "service_write_symphony_state" on public.symphony_state for insert to service_role with check (true);
create policy "service_update_symphony_state" on public.symphony_state for update to service_role using (true);

create index if not exists idx_symphony_state_updated on public.symphony_state(updated_at desc);
create index if not exists idx_symphony_state_cycle_week on public.symphony_state(cycle, week);

-- Trigger updated_at auto (idempotent création)
create or replace function trg_symphony_state_touch() returns trigger language plpgsql as $$
begin new.updated_at = now(); return new; end $$;
drop trigger if exists trg_symphony_state_touch on public.symphony_state;
create trigger trg_symphony_state_touch before update on public.symphony_state
  for each row execute function trg_symphony_state_touch();
```

**Notes D3 (nuance)** :
- C1 = `session_id` est l'identité logique : upsert idempotent direct
- C2 = `updated_at` est la seule timestamp nécessaire ; `extra` JSONB peut porter `uploaded_at` côté payload si besoin
- C3 = anon peut lire, écrivait restreint à `service_role` (clé)
- Pas de FK vers `user_profiles` : Symphony state est A0-private, pas user-facing

## Modification state_writer.py (1 fonction à ajouter)

```python
# En bas de state_writer.py : _sync_to_supabase() appelé après chaque write_state()
def _sync_to_supabase(snapshot: dict) -> None:
    """Push state → Supabase REST v1 (idempotent upsert via session_id)."""
    import os, json, urllib.request
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_SERVICE_KEY")
    if not (url and key):
        return  # graceful no-op si pas configuré
    payload = {k: v for k, v in snapshot.items() if k not in ("$schema",)}
    req = urllib.request.Request(
        f"{url}/rest/v1/symphony_state?on_conflict=session_id",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "apikey": key,
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "Prefer": "resolution=merge-duplicates",
        },
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=2).read()
    except Exception as e:
        print(f"[symphony_bus] Supabase sync skipped: {e}", file=sys.stderr)
```

**D1 missing** : SUPABASE_URL + SUPABASE_SERVICE_KEY en variables d'env Windows scope User (Test Key Pragma). Sera demandé à A0 au moment de l'activation.

## Rollout phases

| Phase | Action | Pré-req | GO requis |
|-------|--------|---------|-----------|
| U1-a | `apply_migration` avec le schéma ci-dessus | aucune | ✅ reçu |
| U1-b | Edit state_writer.py : ajouter `_sync_to_supabase()` + appel en fin de `write_state()` | U1-a passé | ✅ reçu |
| U1-c | Tu colles les 2 env vars (SUPABASE_URL, SUPABASE_SERVICE_KEY) en chat → je teste un curl upsert | U1-b | en attente |
| U1-d | 1er uplink manuel sur state.json courant (W1 du 03-07) → row dans symphony_state | U1-c | en attente |

## Sacred exclusions respectées (D7)

- Pas d'Edit ADR RATIFIED
- Pas de CronCreate
- Pas de hard-delete
- Migration : nommage `01_u1_symphony_state.sql` (D4 append-only via apply_migration)

## Alternative à A0

Si tu préfères **d'abord valider le schéma SQL en review**, je m'arrête ici sans apply_migration et tu reviens avec GO. Si tu veux **exécution immédiate**, réponds "GO U1-a+b" et j'applique la migration + je patche state_writer.py.
