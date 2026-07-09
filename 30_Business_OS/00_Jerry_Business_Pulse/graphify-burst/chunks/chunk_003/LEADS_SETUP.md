# D09 — Lead Capture Setup

The landing CTAs ("submit your url") now POST to `/api/leads` and persist a lead. This resolves audit debt **D09**.

## How it works
- **Endpoint**: `src/app/api/leads/route.ts` (POST, Node runtime). Validates URL + email, honeypot anti-spam, captures UTM/referrer.
- **Core**: `src/lib/leads.ts` — `parseLead()` (validation) + `captureLead()` (persistence).
- **Form**: `src/components/sections/LeadForm.tsx` (rendered in `FinalCTA`, id `#vault-form`; Hero + Topbar CTAs point there).

## Storage
1. **Supabase (canonical, prod)** — used when env vars are set:
   ```
   SUPABASE_URL=https://<project>.supabase.co
   SUPABASE_SERVICE_ROLE_KEY=<server-side key>   # or SUPABASE_ANON_KEY (RLS-insert policy required)
   ```
   Inserts into a `leads` table via REST (`/rest/v1/leads`). **Never commit these** (`.env*` is gitignored).
2. **Dev fallback** — when env absent AND `NODE_ENV !== production`: appends to `.data/leads.jsonl` (gitignored).
   In production with no Supabase env, the endpoint returns **503 `storage_unavailable`** (honest, no silent loss).

## Supabase table (run once)
```sql
create table if not exists public.leads (
  id uuid primary key default gen_random_uuid(),
  url text not null,
  email text not null,
  archetype text,
  note text,
  utm jsonb,
  referrer text,
  ua text,
  source text not null default 'landing',
  captured_at timestamptz not null default now()
);
-- If inserting with the anon key, add an INSERT RLS policy. With the service-role key, RLS is bypassed.
```

## Test (dev)
```bash
npm run dev
curl -s -X POST localhost:3000/api/leads -H "Content-Type: application/json" \
  -d '{"url":"acme-studio.com","email":"you@acme-studio.com","archetype":"forges"}'
# → {"ok":true}   (and a line in .data/leads.jsonl)
curl -s -X POST localhost:3000/api/leads -H "Content-Type: application/json" -d '{"url":"x","email":"nope"}'
# → 422 {"ok":false,"error":"validation","fields":["url","email"]}
```

## Cross-domain (flagship)
- **Growth** : this is the lead-capture path the VOC packet required (source-of-truth + tracking). Unblocks acquisition.
- **IT** : runtime owner — provision the Supabase `leads` table + env (the canonical store; Symphony can later read it as a tracker).
- **Legal** : the form collects email + URL → add consent/privacy note per RGPD (L6) before scaling diffusion.
