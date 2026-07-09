---
title: Alykaly OS — Stratégie de Structuration Supabase
project: Alikaly Bana Holding OS / alykaly-os-V2
author: Claude Code CLI on MiniMax (Architecte Souverain)
date: 2026-05-20
status: DRAFT_FOR_A0_VALIDATION
domain: L1 Life OS / 24_PARA_Enterprise / Project Picard
related:
  - ./picard_audit.md
  - ./README.md
  - ../../../../00_Amadeus/30_MEMORY_CORE/Shadow_L2/01_mcp-shadow-l2-config-20260516.md
inputs:
  - hosting_plan: Hostinger Business Web Hosting ($18.99/mo, kalybana.com, 5 Node.js apps, 50GB SSD)
  - tenancy: hybride (single-tenant immédiat, slot org_id réservé)
  - pii_level: standard + redaction (LEVEL 5 CLEARANCE)
tags: [#Supabase, #Alykaly, #Picard, #Hostinger, #Architecture, #Strategy, #PostgresRLS]
---

# Alykaly OS — Stratégie Supabase + Déploiement Hostinger Business

## 0. Executive Summary

Le dashboard `alykaly-os-V2` (Next.js 15 App Router) est aujourd'hui 100% mockée : `src/lib/store.ts` + `src/lib/actions.ts` retournent des constantes hardcodées. Cette spec définit la **bascule vers Supabase comme source de vérité unique** (Postgres + Auth + Storage + Edge Functions + Realtime) et le **déploiement sur Hostinger Business** via Node.js Application (Phusion Passenger derrière LiteSpeed).

### Décisions structurantes

| Décision | Valeur retenue | Rationale |
|---|---|---|
| Backend | **Supabase self-hosted** (`supabase.kalybana.com` déjà ADR'd) ou Supabase Cloud | Self-hosted = souveraineté A'Space. Cloud = vélocité. Choix A0 §13. |
| Hosting frontend | **Hostinger Business — Node.js Application** | Plan confirmé : 5 Node.js apps inclus, 50GB SSD, daily backups, RAM ~2GB. |
| Next.js mode | **`output: 'standalone'` (inchangé)** | `node server.js` derrière Passenger. Server Actions + App Router intacts. |
| Tenancy | **Hybride** : pas de table `organizations`, mais colonne `org_id TEXT NOT NULL DEFAULT 'alykaly'` sur tables business | Migration multi-tenant future = ajouter table + foreign key, pas refonte schema. |
| PII | **Standard + RLS-driven redaction** | `clearance_required` enum sur lignes sensibles. Pas de pgsodium custom (overhead non justifié). |
| Migrations | **`supabase/migrations/*.sql` versionnés Git** | Branches Supabase pour preview/staging. |
| Realtime | **Channels Postgres CDC** pour Dashboard (Wind Direction, Pipeline, Ledger live) | Évite polling, réduit RAM Node.js. |

### Phases (estimation 12-16h dev)

| # | Phase | Durée | Bloque sur |
|---|---|---|---|
| P0 | Bootstrap projet Supabase + env vars | 30min | A0 décide cloud vs self-hosted |
| P1 | Schema core (cases, clients, profiles, auth) + RLS | 2-3h | P0 |
| P2 | Schema secondaire (transactions, documents, kanbans) + RLS | 2-3h | P1 |
| P3 | Edge Functions (sob-engine, docusign-webhook, intake-handler) | 2-3h | P1 |
| P4 | Refactor code Next.js (`actions.ts` mocks → Supabase JS) | 3-4h | P1 + P2 |
| P5 | Hostinger Node.js App deploy + DNS + smoke tests | 1-2h | P4 |
| P6 | Realtime channels + cron edge functions (audit-rotate) | 1h | P5 |

---

## 1. Cartographie du domaine (extrait du code source)

Inventaire des entités dérivées de `src/components/*` et `src/lib/*` (audit `picard_audit.md` complété par lecture exhaustive 2026-05-20).

### 1.1 Business core — Surplus Funds Recovery

| Component | Entité Postgres | Volumetrie estimée |
|---|---|---|
| `Docket.tsx` | `cases` (court cases sourcées) | 100-500 actives, 5k-20k historiques/an |
| `Clients.tsx` | `clients` (Estate of X, LLCs) | 1:N avec cases |
| `Legal.tsx` (Kanban) | `court_filings` (workflow tribunal) | 1:1 avec case actif |
| `SalesSanctum.tsx` (Kanban) | `sales_pipeline_items` (DocuSign workflow) | 1:N avec case |
| `Finance.tsx` (Ledger) | `transactions` (inflow/outflow) | 1:N avec case |
| `bana/IntakeForm.tsx` (landing publique) | `intake_submissions` | 50-200/mois |

### 1.2 Operational

| Component | Entité | Source |
|---|---|---|
| `People.tsx` | `agents` + `agent_events` | Jerry (n8n), DocuSign, Supabase ops |
| `Growth.tsx` | `cohorts` + `feed_events` | Marketing campaigns |
| `Dashboard.tsx` (Wind Direction) | `wind_direction_alerts` (vue dérivée) | Agrégation triggers |
| `SystemRoots.tsx` | `system_metrics` | Edge function status |

### 1.3 Content / CMS

| Component | Entité |
|---|---|
| `Knowledge.tsx` | `knowledge_docs` (scripts d'appel, FAQ catégorisée) |
| `Settings.tsx` | `user_settings` (préférences user-scoped) |

### 1.4 Auth / Identity

| Entité | Source Supabase |
|---|---|
| `auth.users` | natif Supabase Auth |
| `profiles` | extension custom, 1:1 sur `auth.users` |
| `profile_roles` | rôle enum + clearance level |
| `audit_log` | append-only, tous events |

### 1.5 API existante / à migrer

- `src/app/api/engine/status/route.ts` → reste route Next.js, **appelle Supabase Edge Function `sob-engine-simulate`** au lieu de mock.

---

## 2. Architecture cible — diagramme texte

```
┌──────────────────────────────────────────────────────────────┐
│                    HOSTINGER BUSINESS                        │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  kalybana.com (LiteSpeed)                            │   │
│  │  ├── alykaly.kalybana.com (subdomain)                │   │
│  │  │   └── Node.js App #1 (Passenger)                  │   │
│  │  │       node server.js (Next.js standalone)         │   │
│  │  │       :4444 → reverse proxied :443                │   │
│  │  └── bana.kalybana.com (subdomain) — OPTIONAL split  │   │
│  │      └── Node.js App #2 ou same app /bana route     │   │
│  └──────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────┘
                           │
                           │ HTTPS (Supabase JS SDK + REST + Realtime WS)
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                  SUPABASE (self-hosted ou Cloud)             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Postgres 15+ (RLS-protected)                        │   │
│  │  ├── app.*            (cases, clients, transactions) │   │
│  │  ├── crm.*            (sales_pipeline, court_filings)│   │
│  │  ├── identity.*       (profiles, roles)              │   │
│  │  ├── ops.*            (agents, events, metrics)      │   │
│  │  └── audit.*          (append-only log)              │   │
│  ├──────────────────────────────────────────────────────┤   │
│  │  GoTrue Auth                                          │   │
│  │  ├── email/password                                   │   │
│  │  ├── magic link (admin onboarding)                    │   │
│  │  └── JWT custom claims (role, clearance, org_id)      │   │
│  ├──────────────────────────────────────────────────────┤   │
│  │  Storage S3-compatible                                │   │
│  │  ├── documents-private  (DocuSign PDFs, court docs)   │   │
│  │  ├── intake-attachments (Bana form uploads)          │   │
│  │  └── marketing-public   (logos, hero images)          │   │
│  ├──────────────────────────────────────────────────────┤   │
│  │  Edge Functions (Deno)                                │   │
│  │  ├── sob-engine-simulate   (replaces /api/engine/...) │   │
│  │  ├── docusign-webhook       (callback receiver)       │   │
│  │  ├── intake-handler         (Bana form → cases)       │   │
│  │  ├── case-confidence-recalc (scheduled)               │   │
│  │  └── audit-rotate           (daily cleanup)           │   │
│  └──────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────┘
                           │
                           │ (optional outbound)
                           ▼
                  n8n (orchestration) — VPS séparé
```

---

## 3. Schema Postgres — DDL complète

### 3.1 Conventions

- **Schemas** : `app` (business), `crm` (pipelines), `identity`, `ops`, `audit`, `public` (vues + helpers)
- **PK** : `id UUID DEFAULT gen_random_uuid() PRIMARY KEY`
- **Timestamps** : `created_at TIMESTAMPTZ NOT NULL DEFAULT now()` + `updated_at` via trigger
- **Soft-delete** : `deleted_at TIMESTAMPTZ` nullable + index partiel `WHERE deleted_at IS NULL`
- **Multi-tenant slot** : `org_id TEXT NOT NULL DEFAULT 'alykaly'` sur toutes tables business
- **Money** : `NUMERIC(14,2)` (jamais `FLOAT`/`REAL`)
- **FK** : `ON DELETE RESTRICT` par défaut, `CASCADE` uniquement sur tables enfant strictes
- **Enums** : `CREATE TYPE` Postgres natif (versionné via migrations)

### 3.2 Migration `001_init_schemas_and_enums.sql`

```sql
-- ===== Schemas =====
CREATE SCHEMA IF NOT EXISTS app;
CREATE SCHEMA IF NOT EXISTS crm;
CREATE SCHEMA IF NOT EXISTS identity;
CREATE SCHEMA IF NOT EXISTS ops;
CREATE SCHEMA IF NOT EXISTS audit;

-- ===== Extensions =====
CREATE EXTENSION IF NOT EXISTS "pgcrypto";    -- gen_random_uuid
CREATE EXTENSION IF NOT EXISTS "pg_trgm";     -- fuzzy search defendants/clients

-- ===== Enums =====
CREATE TYPE app.case_priority AS ENUM ('genealogie', 'b2b', 'expulsion', 'other');
CREATE TYPE app.case_status   AS ENUM ('new', 'tracking', 'ready', 'filed', 'hearing', 'won', 'lost', 'archived');
CREATE TYPE app.tx_type       AS ENUM ('inflow', 'outflow');
CREATE TYPE app.tx_status     AS ENUM ('pending', 'completed', 'failed', 'reversed');
CREATE TYPE app.client_module AS ENUM ('cession', 'buyout', 'audit_only');

CREATE TYPE identity.user_role        AS ENUM ('admin', 'operator', 'agent', 'viewer', 'client');
CREATE TYPE identity.clearance_level  AS ENUM ('level_0_public', 'level_1_internal', 'level_3_restricted', 'level_5_sovereign');

CREATE TYPE crm.sales_stage   AS ENUM ('audit', 'sent', 'opened', 'signed', 'lost');
CREATE TYPE crm.court_stage   AS ENUM ('ready', 'filed', 'hearing', 'signed', 'closed');

CREATE TYPE ops.agent_kind    AS ENUM ('synthetic', 'human', 'webhook', 'cron');
CREATE TYPE ops.event_severity AS ENUM ('debug', 'info', 'warning', 'critical');
```

### 3.3 Migration `002_identity.sql`

```sql
-- One profile per Supabase auth.users
CREATE TABLE identity.profiles (
  user_id           UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  org_id            TEXT NOT NULL DEFAULT 'alykaly',
  display_name      TEXT NOT NULL,
  email             TEXT NOT NULL,
  role              identity.user_role NOT NULL DEFAULT 'viewer',
  clearance         identity.clearance_level NOT NULL DEFAULT 'level_1_internal',
  avatar_url        TEXT,
  preferences       JSONB NOT NULL DEFAULT '{}'::JSONB,
  last_seen_at      TIMESTAMPTZ,
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at        TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX profiles_org_role_idx ON identity.profiles(org_id, role);
CREATE INDEX profiles_clearance_idx ON identity.profiles(clearance);

-- Trigger: auto-create profile when auth.users insertion
CREATE OR REPLACE FUNCTION identity.handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO identity.profiles (user_id, display_name, email)
  VALUES (
    NEW.id,
    COALESCE(NEW.raw_user_meta_data->>'display_name', split_part(NEW.email, '@', 1)),
    NEW.email
  )
  ON CONFLICT (user_id) DO NOTHING;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE FUNCTION identity.handle_new_user();

-- Helper: current user role + clearance (used by RLS policies)
CREATE OR REPLACE FUNCTION identity.current_user_clearance()
RETURNS identity.clearance_level
LANGUAGE sql STABLE SECURITY DEFINER AS $$
  SELECT clearance FROM identity.profiles WHERE user_id = auth.uid();
$$;

CREATE OR REPLACE FUNCTION identity.current_user_role()
RETURNS identity.user_role
LANGUAGE sql STABLE SECURITY DEFINER AS $$
  SELECT role FROM identity.profiles WHERE user_id = auth.uid();
$$;

CREATE OR REPLACE FUNCTION identity.current_user_org()
RETURNS TEXT
LANGUAGE sql STABLE SECURITY DEFINER AS $$
  SELECT org_id FROM identity.profiles WHERE user_id = auth.uid();
$$;
```

### 3.4 Migration `003_business_core.sql`

```sql
-- ===== CLIENTS (entity facing whom we recover) =====
CREATE TABLE app.clients (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id            TEXT NOT NULL DEFAULT 'alykaly',
  name              TEXT NOT NULL,
  module            app.client_module NOT NULL,
  contact_email     TEXT,
  contact_phone     TEXT,
  notes             TEXT,
  status            TEXT,
  clearance_required identity.clearance_level NOT NULL DEFAULT 'level_1_internal',
  metadata          JSONB NOT NULL DEFAULT '{}'::JSONB,
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  deleted_at        TIMESTAMPTZ
);

CREATE INDEX clients_org_idx ON app.clients(org_id) WHERE deleted_at IS NULL;
CREATE INDEX clients_name_trgm_idx ON app.clients USING gin(name gin_trgm_ops);

-- ===== CASES (court cases sourcées au tribunal) =====
CREATE TABLE app.cases (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id            TEXT NOT NULL DEFAULT 'alykaly',
  case_number       TEXT NOT NULL,                   -- ex: 'A 2403702'
  defendant         TEXT NOT NULL,                   -- ex: 'Estate of Robert Chase'
  client_id         UUID REFERENCES app.clients(id) ON DELETE SET NULL,
  amount            NUMERIC(14,2) NOT NULL DEFAULT 0,
  priority          app.case_priority NOT NULL DEFAULT 'other',
  status            app.case_status NOT NULL DEFAULT 'new',
  confidence_score  INT NOT NULL DEFAULT 0 CHECK (confidence_score BETWEEN 0 AND 5),
  court_jurisdiction TEXT,                            -- ex: 'TX-Harris'
  sourced_from      TEXT,                             -- ex: 'PACER', 'manual', 'partner-X'
  assigned_to       UUID REFERENCES identity.profiles(user_id),
  clearance_required identity.clearance_level NOT NULL DEFAULT 'level_1_internal',
  metadata          JSONB NOT NULL DEFAULT '{}'::JSONB,
  version           INT NOT NULL DEFAULT 1,
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  deleted_at        TIMESTAMPTZ,
  UNIQUE (org_id, case_number)
);

CREATE INDEX cases_org_status_idx       ON app.cases(org_id, status) WHERE deleted_at IS NULL;
CREATE INDEX cases_priority_idx         ON app.cases(priority);
CREATE INDEX cases_assigned_idx         ON app.cases(assigned_to) WHERE deleted_at IS NULL;
CREATE INDEX cases_defendant_trgm_idx   ON app.cases USING gin(defendant gin_trgm_ops);
CREATE INDEX cases_amount_idx           ON app.cases(amount DESC) WHERE deleted_at IS NULL;

-- ===== TRANSACTIONS (ledger Finance) =====
CREATE TABLE app.transactions (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id            TEXT NOT NULL DEFAULT 'alykaly',
  case_id           UUID NOT NULL REFERENCES app.cases(id) ON DELETE RESTRICT,
  tx_type           app.tx_type NOT NULL,
  amount            NUMERIC(14,2) NOT NULL,
  tx_date           DATE NOT NULL,
  status            app.tx_status NOT NULL DEFAULT 'pending',
  description       TEXT,
  external_ref      TEXT,                             -- ex: Stripe charge id, ACH ref
  created_by        UUID REFERENCES identity.profiles(user_id),
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  deleted_at        TIMESTAMPTZ
);

CREATE INDEX transactions_case_idx   ON app.transactions(case_id);
CREATE INDEX transactions_date_idx   ON app.transactions(tx_date DESC);
CREATE INDEX transactions_status_idx ON app.transactions(status);
```

### 3.5 Migration `004_crm_pipelines.sql`

```sql
-- ===== SALES SANCTUM kanban (DocuSign workflow) =====
CREATE TABLE crm.sales_pipeline_items (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id            TEXT NOT NULL DEFAULT 'alykaly',
  case_id           UUID NOT NULL REFERENCES app.cases(id) ON DELETE CASCADE,
  stage             crm.sales_stage NOT NULL DEFAULT 'audit',
  envelope_id       TEXT,                              -- DocuSign envelope ID
  views_count       INT NOT NULL DEFAULT 0,
  last_event_at     TIMESTAMPTZ,
  metadata          JSONB NOT NULL DEFAULT '{}'::JSONB,
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (case_id)                                     -- 1 entry par case in sales
);

CREATE INDEX sales_pipeline_org_stage_idx ON crm.sales_pipeline_items(org_id, stage);

-- ===== LEGAL kanban (Court workflow) =====
CREATE TABLE crm.court_filings (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id            TEXT NOT NULL DEFAULT 'alykaly',
  case_id           UUID NOT NULL REFERENCES app.cases(id) ON DELETE CASCADE,
  stage             crm.court_stage NOT NULL DEFAULT 'ready',
  filed_at          DATE,
  hearing_at        TIMESTAMPTZ,
  filed_amount      NUMERIC(14,2),
  delay_days        INT,
  metadata          JSONB NOT NULL DEFAULT '{}'::JSONB,
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (case_id)
);

CREATE INDEX court_filings_org_stage_idx ON crm.court_filings(org_id, stage);
CREATE INDEX court_filings_hearing_idx   ON crm.court_filings(hearing_at) WHERE hearing_at IS NOT NULL;

-- ===== DOCUMENTS (Storage metadata pour DocuSign PDFs, court docs) =====
CREATE TABLE crm.documents (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id            TEXT NOT NULL DEFAULT 'alykaly',
  case_id           UUID REFERENCES app.cases(id) ON DELETE SET NULL,
  client_id         UUID REFERENCES app.clients(id) ON DELETE SET NULL,
  bucket            TEXT NOT NULL,                     -- 'documents-private' or other
  storage_path      TEXT NOT NULL,                     -- relative path inside bucket
  doc_type          TEXT NOT NULL,                     -- 'docusign_envelope','court_filing','wire_proof'
  filename          TEXT NOT NULL,
  mime_type         TEXT,
  size_bytes        BIGINT,
  checksum_sha256   TEXT,
  uploaded_by       UUID REFERENCES identity.profiles(user_id),
  clearance_required identity.clearance_level NOT NULL DEFAULT 'level_1_internal',
  metadata          JSONB NOT NULL DEFAULT '{}'::JSONB,
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  deleted_at        TIMESTAMPTZ
);

CREATE INDEX documents_case_idx   ON crm.documents(case_id) WHERE deleted_at IS NULL;
CREATE INDEX documents_client_idx ON crm.documents(client_id) WHERE deleted_at IS NULL;
```

### 3.6 Migration `005_ops_and_content.sql`

```sql
-- ===== AGENTS (People = synthetic + human) =====
CREATE TABLE ops.agents (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id            TEXT NOT NULL DEFAULT 'alykaly',
  slug              TEXT NOT NULL,                     -- 'jerry-n8n', 'docusign-bot'
  display_name      TEXT NOT NULL,
  kind              ops.agent_kind NOT NULL,
  description       TEXT,
  endpoint          TEXT,                              -- webhook URL or service ref
  is_active         BOOLEAN NOT NULL DEFAULT true,
  metadata          JSONB NOT NULL DEFAULT '{}'::JSONB,
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (org_id, slug)
);

-- ===== AGENT EVENTS (webhook calls, errors) =====
CREATE TABLE ops.agent_events (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  agent_id          UUID NOT NULL REFERENCES ops.agents(id) ON DELETE CASCADE,
  case_id           UUID REFERENCES app.cases(id) ON DELETE SET NULL,
  severity          ops.event_severity NOT NULL DEFAULT 'info',
  event_type        TEXT NOT NULL,                     -- 'webhook.received','sync.completed','error.timeout'
  message           TEXT,
  payload           JSONB,
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX agent_events_agent_idx     ON ops.agent_events(agent_id, created_at DESC);
CREATE INDEX agent_events_severity_idx  ON ops.agent_events(severity) WHERE severity IN ('warning','critical');

-- ===== SYSTEM METRICS (System Roots) =====
CREATE TABLE ops.system_metrics (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  metric_key        TEXT NOT NULL,                     -- 'sob.global_exposure','sob.ytd_yield'
  numeric_value     NUMERIC(20,4),
  text_value        TEXT,
  metadata          JSONB,
  recorded_at       TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX system_metrics_key_time_idx ON ops.system_metrics(metric_key, recorded_at DESC);

-- ===== KNOWLEDGE (scripts d'appel, FAQ) =====
CREATE TABLE app.knowledge_docs (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id            TEXT NOT NULL DEFAULT 'alykaly',
  category          TEXT NOT NULL,                     -- 'call-script','faq','procedure'
  title             TEXT NOT NULL,
  body_md           TEXT NOT NULL,
  tags              TEXT[] NOT NULL DEFAULT ARRAY[]::TEXT[],
  clearance_required identity.clearance_level NOT NULL DEFAULT 'level_0_public',
  author_id         UUID REFERENCES identity.profiles(user_id),
  version           INT NOT NULL DEFAULT 1,
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  deleted_at        TIMESTAMPTZ
);

CREATE INDEX knowledge_category_idx ON app.knowledge_docs(category) WHERE deleted_at IS NULL;
CREATE INDEX knowledge_tags_idx     ON app.knowledge_docs USING gin(tags);

-- ===== GROWTH cohorts / feed =====
CREATE TABLE crm.cohorts (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id            TEXT NOT NULL DEFAULT 'alykaly',
  name              TEXT NOT NULL,
  source            TEXT,                              -- 'facebook-ads','referral','organic'
  acquisition_cost  NUMERIC(14,2),
  lifetime_value    NUMERIC(14,2),
  started_at        DATE,
  metadata          JSONB NOT NULL DEFAULT '{}'::JSONB,
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE crm.feed_events (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id            TEXT NOT NULL DEFAULT 'alykaly',
  cohort_id         UUID REFERENCES crm.cohorts(id) ON DELETE SET NULL,
  event_kind        TEXT NOT NULL,                     -- 'lead.captured','demo.scheduled','case.signed'
  case_id           UUID REFERENCES app.cases(id) ON DELETE SET NULL,
  payload           JSONB,
  occurred_at       TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX feed_events_time_idx ON crm.feed_events(occurred_at DESC);

-- ===== INTAKE submissions (Bana landing form) =====
CREATE TABLE app.intake_submissions (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id            TEXT NOT NULL DEFAULT 'alykaly',
  source            TEXT NOT NULL DEFAULT 'bana_intake',
  payload           JSONB NOT NULL,
  defender_email    TEXT,
  defender_phone    TEXT,
  routed_case_id    UUID REFERENCES app.cases(id) ON DELETE SET NULL,
  status            TEXT NOT NULL DEFAULT 'new',       -- 'new','triaged','rejected','converted'
  processed_by      UUID REFERENCES identity.profiles(user_id),
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  processed_at      TIMESTAMPTZ
);

CREATE INDEX intake_status_idx ON app.intake_submissions(status) WHERE status = 'new';

-- ===== WIND DIRECTION alerts (Dashboard) =====
CREATE TABLE ops.wind_direction_alerts (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id            TEXT NOT NULL DEFAULT 'alykaly',
  severity          ops.event_severity NOT NULL,
  title             TEXT NOT NULL,
  description       TEXT,
  case_id           UUID REFERENCES app.cases(id) ON DELETE SET NULL,
  action_url        TEXT,                              -- link to relevant module
  acknowledged_at   TIMESTAMPTZ,
  acknowledged_by   UUID REFERENCES identity.profiles(user_id),
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX wind_unack_idx ON ops.wind_direction_alerts(created_at DESC) WHERE acknowledged_at IS NULL;
```

### 3.7 Migration `006_audit_and_triggers.sql`

```sql
-- ===== Generic updated_at trigger =====
CREATE OR REPLACE FUNCTION public.set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = now();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Apply to all tables with updated_at column
DO $$
DECLARE
  t RECORD;
BEGIN
  FOR t IN
    SELECT table_schema, table_name
    FROM information_schema.columns
    WHERE column_name = 'updated_at'
      AND table_schema IN ('app','crm','identity','ops')
  LOOP
    EXECUTE format(
      'CREATE TRIGGER set_updated_at BEFORE UPDATE ON %I.%I FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();',
      t.table_schema, t.table_name
    );
  END LOOP;
END $$;

-- ===== AUDIT LOG (append-only) =====
CREATE TABLE audit.log (
  id                BIGSERIAL PRIMARY KEY,
  org_id            TEXT NOT NULL DEFAULT 'alykaly',
  actor_id          UUID,                              -- auth.uid() at time of event
  actor_email       TEXT,
  table_schema      TEXT NOT NULL,
  table_name        TEXT NOT NULL,
  row_id            TEXT,
  action            TEXT NOT NULL,                     -- 'INSERT','UPDATE','DELETE','SOFT_DELETE'
  changes           JSONB,                             -- diff before→after
  ip_address        INET,
  user_agent        TEXT,
  occurred_at       TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX audit_log_table_time_idx ON audit.log(table_schema, table_name, occurred_at DESC);
CREATE INDEX audit_log_actor_idx      ON audit.log(actor_id) WHERE actor_id IS NOT NULL;

-- Generic audit trigger
CREATE OR REPLACE FUNCTION audit.record_change()
RETURNS TRIGGER AS $$
DECLARE
  changes_jsonb JSONB;
BEGIN
  IF TG_OP = 'INSERT' THEN
    changes_jsonb := jsonb_build_object('after', to_jsonb(NEW));
  ELSIF TG_OP = 'UPDATE' THEN
    changes_jsonb := jsonb_build_object('before', to_jsonb(OLD), 'after', to_jsonb(NEW));
  ELSIF TG_OP = 'DELETE' THEN
    changes_jsonb := jsonb_build_object('before', to_jsonb(OLD));
  END IF;

  INSERT INTO audit.log (actor_id, actor_email, table_schema, table_name, row_id, action, changes)
  VALUES (
    auth.uid(),
    (SELECT email FROM identity.profiles WHERE user_id = auth.uid()),
    TG_TABLE_SCHEMA, TG_TABLE_NAME,
    COALESCE((NEW).id::TEXT, (OLD).id::TEXT),
    TG_OP, changes_jsonb
  );
  RETURN COALESCE(NEW, OLD);
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Apply audit trigger to sensitive tables
CREATE TRIGGER audit_cases       AFTER INSERT OR UPDATE OR DELETE ON app.cases       FOR EACH ROW EXECUTE FUNCTION audit.record_change();
CREATE TRIGGER audit_transactions AFTER INSERT OR UPDATE OR DELETE ON app.transactions FOR EACH ROW EXECUTE FUNCTION audit.record_change();
CREATE TRIGGER audit_documents   AFTER INSERT OR UPDATE OR DELETE ON crm.documents   FOR EACH ROW EXECUTE FUNCTION audit.record_change();
CREATE TRIGGER audit_profiles    AFTER UPDATE                ON identity.profiles  FOR EACH ROW EXECUTE FUNCTION audit.record_change();
```

---

## 4. RLS Policies — Sécurité par rôle + clearance

### 4.1 Principes

- **Enable RLS** sur TOUTES les tables (`ENABLE ROW LEVEL SECURITY`)
- **Service role** (Edge Functions internes) bypass via `bypassrls = true`
- **`auth.uid()` IS NULL** → REFUSE par défaut (anon n'a accès qu'aux tables publiques limitées)
- **Clearance compare** via fonction helper `identity.current_user_clearance()`
- **Org isolation** : `org_id = identity.current_user_org()` partout

### 4.2 Migration `007_rls_policies.sql`

```sql
-- ===== Enable RLS on all business tables =====
ALTER TABLE app.cases               ENABLE ROW LEVEL SECURITY;
ALTER TABLE app.clients             ENABLE ROW LEVEL SECURITY;
ALTER TABLE app.transactions        ENABLE ROW LEVEL SECURITY;
ALTER TABLE app.knowledge_docs      ENABLE ROW LEVEL SECURITY;
ALTER TABLE app.intake_submissions  ENABLE ROW LEVEL SECURITY;
ALTER TABLE crm.sales_pipeline_items ENABLE ROW LEVEL SECURITY;
ALTER TABLE crm.court_filings       ENABLE ROW LEVEL SECURITY;
ALTER TABLE crm.documents           ENABLE ROW LEVEL SECURITY;
ALTER TABLE crm.cohorts             ENABLE ROW LEVEL SECURITY;
ALTER TABLE crm.feed_events         ENABLE ROW LEVEL SECURITY;
ALTER TABLE ops.agents              ENABLE ROW LEVEL SECURITY;
ALTER TABLE ops.agent_events        ENABLE ROW LEVEL SECURITY;
ALTER TABLE ops.system_metrics      ENABLE ROW LEVEL SECURITY;
ALTER TABLE ops.wind_direction_alerts ENABLE ROW LEVEL SECURITY;
ALTER TABLE identity.profiles       ENABLE ROW LEVEL SECURITY;
ALTER TABLE audit.log               ENABLE ROW LEVEL SECURITY;

-- ===== Helper: clearance comparison =====
-- (ordinal comparison; uses enum ordering)
CREATE OR REPLACE FUNCTION identity.clearance_at_least(target identity.clearance_level)
RETURNS BOOLEAN
LANGUAGE sql STABLE AS $$
  SELECT identity.current_user_clearance() >= target
$$;

-- ===== PROFILES =====
-- Read: own profile always; admin sees all in same org
CREATE POLICY profiles_select_self_or_admin ON identity.profiles
  FOR SELECT USING (
    user_id = auth.uid()
    OR (identity.current_user_role() = 'admin' AND org_id = identity.current_user_org())
  );

-- Update: own profile (limited fields); admin can update role/clearance
CREATE POLICY profiles_update_self ON identity.profiles
  FOR UPDATE USING (user_id = auth.uid())
  WITH CHECK (user_id = auth.uid());

CREATE POLICY profiles_update_admin ON identity.profiles
  FOR UPDATE USING (
    identity.current_user_role() = 'admin'
    AND org_id = identity.current_user_org()
  );

-- ===== CASES =====
-- Read: same org + clearance >= row's requirement; client role sees only own cases via client_id
CREATE POLICY cases_select_org_clearance ON app.cases
  FOR SELECT USING (
    org_id = identity.current_user_org()
    AND identity.clearance_at_least(clearance_required)
    AND deleted_at IS NULL
  );

-- Insert: operator/admin only
CREATE POLICY cases_insert_operator ON app.cases
  FOR INSERT WITH CHECK (
    identity.current_user_role() IN ('admin','operator')
    AND org_id = identity.current_user_org()
  );

-- Update: assigned operator/admin
CREATE POLICY cases_update_assigned ON app.cases
  FOR UPDATE USING (
    org_id = identity.current_user_org()
    AND (
      identity.current_user_role() = 'admin'
      OR assigned_to = auth.uid()
    )
  );

-- Delete: admin only (and soft-delete preferred via UPDATE deleted_at)
CREATE POLICY cases_delete_admin ON app.cases
  FOR DELETE USING (identity.current_user_role() = 'admin');

-- ===== CLIENTS (same pattern) =====
CREATE POLICY clients_select_org_clearance ON app.clients
  FOR SELECT USING (
    org_id = identity.current_user_org()
    AND identity.clearance_at_least(clearance_required)
    AND deleted_at IS NULL
  );

CREATE POLICY clients_modify_operator ON app.clients
  FOR ALL USING (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator')
  );

-- ===== TRANSACTIONS =====
-- Read: same org operators/admins
CREATE POLICY tx_select_org ON app.transactions
  FOR SELECT USING (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator','viewer')
    AND deleted_at IS NULL
  );

-- Insert: operator/admin
CREATE POLICY tx_insert_operator ON app.transactions
  FOR INSERT WITH CHECK (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator')
  );

-- Update: admin only (legal compliance — ledger immutable for operators)
CREATE POLICY tx_update_admin ON app.transactions
  FOR UPDATE USING (identity.current_user_role() = 'admin');

-- Delete: forbidden (use soft delete + reversal entries)

-- ===== CRM tables (sales, court, documents) =====
CREATE POLICY sales_pipeline_org ON crm.sales_pipeline_items
  FOR ALL USING (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator','agent')
  );

CREATE POLICY court_filings_org ON crm.court_filings
  FOR ALL USING (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator','agent')
  );

CREATE POLICY documents_select_org_clearance ON crm.documents
  FOR SELECT USING (
    org_id = identity.current_user_org()
    AND identity.clearance_at_least(clearance_required)
    AND deleted_at IS NULL
  );

CREATE POLICY documents_insert_operator ON crm.documents
  FOR INSERT WITH CHECK (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator','agent')
  );

-- ===== KNOWLEDGE (mostly readable) =====
CREATE POLICY knowledge_select_clearance ON app.knowledge_docs
  FOR SELECT USING (
    org_id = identity.current_user_org()
    AND identity.clearance_at_least(clearance_required)
    AND deleted_at IS NULL
  );

CREATE POLICY knowledge_modify_operator ON app.knowledge_docs
  FOR INSERT WITH CHECK (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator')
  );

CREATE POLICY knowledge_update_author ON app.knowledge_docs
  FOR UPDATE USING (
    org_id = identity.current_user_org()
    AND (author_id = auth.uid() OR identity.current_user_role() = 'admin')
  );

-- ===== INTAKE submissions =====
-- Public (anon) can INSERT only (Bana form)
CREATE POLICY intake_insert_anon ON app.intake_submissions
  FOR INSERT TO anon WITH CHECK (true);

-- Authenticated operators can read + update
CREATE POLICY intake_select_operator ON app.intake_submissions
  FOR SELECT USING (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator','agent')
  );

CREATE POLICY intake_update_operator ON app.intake_submissions
  FOR UPDATE USING (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator','agent')
  );

-- ===== Audit log (read only by admin) =====
CREATE POLICY audit_log_select_admin ON audit.log
  FOR SELECT USING (identity.current_user_role() = 'admin');

-- ===== OPS tables (system, agents) =====
CREATE POLICY agents_select_operator ON ops.agents
  FOR SELECT USING (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator','agent','viewer')
  );

CREATE POLICY agents_modify_admin ON ops.agents
  FOR ALL USING (
    identity.current_user_role() = 'admin'
    AND org_id = identity.current_user_org()
  );

CREATE POLICY agent_events_select_operator ON ops.agent_events
  FOR SELECT USING (identity.current_user_role() IN ('admin','operator'));

CREATE POLICY system_metrics_public_read ON ops.system_metrics
  FOR SELECT USING (true);    -- system status visible to all authenticated

CREATE POLICY wind_select_org ON ops.wind_direction_alerts
  FOR SELECT USING (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator','agent','viewer')
  );
```

---

## 5. Auth Flow & Session Management

### 5.1 Stack côté Next.js

```bash
npm install @supabase/supabase-js @supabase/ssr
```

### 5.2 Env vars (Hostinger + local)

```
# .env.local (dev) / Hostinger env (prod)
NEXT_PUBLIC_SUPABASE_URL=https://supabase.kalybana.com
NEXT_PUBLIC_SUPABASE_ANON_KEY=<ANON_KEY>
SUPABASE_SERVICE_ROLE_KEY=<SERVICE_KEY — server only>
SUPABASE_JWT_SECRET=<JWT_SECRET — pour edge functions custom>

# n8n webhook (déjà présent)
N8N_WEBHOOK_URL=https://n8n.kalybana.com/webhook/bana-intake

# DocuSign callback
DOCUSIGN_WEBHOOK_SECRET=<HMAC secret>
```

### 5.3 Clients Supabase (à créer)

**`src/lib/supabase/server.ts`** (Server Components + Server Actions) :

```ts
import { createServerClient } from '@supabase/ssr'
import { cookies } from 'next/headers'

export async function createSupabaseServerClient() {
  const cookieStore = await cookies()
  return createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        getAll: () => cookieStore.getAll(),
        setAll: (toSet) => {
          try { toSet.forEach(({ name, value, options }) => cookieStore.set(name, value, options)) }
          catch { /* called from Server Component — read-only OK */ }
        },
      },
    }
  )
}
```

**`src/lib/supabase/client.ts`** (Client Components) :

```ts
import { createBrowserClient } from '@supabase/ssr'

export function createSupabaseBrowserClient() {
  return createBrowserClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
  )
}
```

**`src/lib/supabase/admin.ts`** (Server-side service role, RLS bypass) :

```ts
import { createClient } from '@supabase/supabase-js'

export function createSupabaseAdminClient() {
  return createClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.SUPABASE_SERVICE_ROLE_KEY!,
    { auth: { persistSession: false } }
  )
}
```

### 5.4 Middleware auth gate

**`src/middleware.ts`** :

```ts
import { createServerClient } from '@supabase/ssr'
import { NextResponse, type NextRequest } from 'next/server'

const PUBLIC_PATHS = ['/bana', '/api/intake', '/auth/callback']

export async function middleware(req: NextRequest) {
  const isPublic = PUBLIC_PATHS.some(p => req.nextUrl.pathname.startsWith(p))
  if (isPublic) return NextResponse.next()

  const res = NextResponse.next()
  const supabase = createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        getAll: () => req.cookies.getAll(),
        setAll: (toSet) => toSet.forEach(({ name, value, options }) => res.cookies.set(name, value, options)),
      },
    }
  )

  const { data: { user } } = await supabase.auth.getUser()
  if (!user) {
    const url = req.nextUrl.clone()
    url.pathname = '/auth/login'
    url.searchParams.set('redirect', req.nextUrl.pathname)
    return NextResponse.redirect(url)
  }
  return res
}

export const config = {
  matcher: ['/((?!_next/static|_next/image|favicon.ico).*)'],
}
```

---

## 6. Storage Buckets (3 buckets minimum)

### 6.1 Définition

```sql
-- Migration 008_storage.sql (à coller dans Studio ou via supabase storage CLI)

-- Bucket privé pour documents sensibles (DocuSign, court)
INSERT INTO storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
VALUES (
  'documents-private',
  'documents-private',
  false,
  52428800,                          -- 50 MB max per file
  ARRAY['application/pdf','image/png','image/jpeg','application/zip']
);

-- Bucket Bana intake uploads (utilisateurs anonymes peuvent POST)
INSERT INTO storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
VALUES ('intake-attachments', 'intake-attachments', false, 20971520,
  ARRAY['application/pdf','image/png','image/jpeg']);

-- Bucket public (marketing assets)
INSERT INTO storage.buckets (id, name, public, file_size_limit)
VALUES ('marketing-public', 'marketing-public', true, 10485760);
```

### 6.2 Policies storage

```sql
-- documents-private : SELECT only if RLS row in crm.documents allows
CREATE POLICY "documents_private_select"
ON storage.objects FOR SELECT TO authenticated
USING (
  bucket_id = 'documents-private'
  AND EXISTS (
    SELECT 1 FROM crm.documents d
    WHERE d.storage_path = storage.objects.name
      AND d.bucket = 'documents-private'
      -- inherits RLS from crm.documents above
  )
);

-- documents-private : INSERT by operators only
CREATE POLICY "documents_private_insert"
ON storage.objects FOR INSERT TO authenticated
WITH CHECK (
  bucket_id = 'documents-private'
  AND identity.current_user_role() IN ('admin','operator','agent')
);

-- intake-attachments : INSERT by anon (Bana form)
CREATE POLICY "intake_attachments_anon_insert"
ON storage.objects FOR INSERT TO anon
WITH CHECK (
  bucket_id = 'intake-attachments'
  AND octet_length(name) < 200
);

-- intake-attachments : SELECT by operators
CREATE POLICY "intake_attachments_operator_select"
ON storage.objects FOR SELECT TO authenticated
USING (
  bucket_id = 'intake-attachments'
  AND identity.current_user_role() IN ('admin','operator','agent')
);
```

---

## 7. Edge Functions (Deno serverless)

### 7.1 `sob-engine-simulate` — remplace `/api/engine/status`

**`supabase/functions/sob-engine-simulate/index.ts`** :

```ts
import { serve } from 'https://deno.land/std@0.208.0/http/server.ts'
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'

serve(async (req) => {
  const supabase = createClient(
    Deno.env.get('SUPABASE_URL')!,
    Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
  )

  // Agrégation live des cases actifs pour exposure
  const { data: activeCases } = await supabase
    .schema('app').from('cases')
    .select('amount')
    .in('status', ['ready','filed','hearing'])
    .is('deleted_at', null)

  const exposure = (activeCases ?? []).reduce((s, c) => s + Number(c.amount ?? 0), 0)
  const lastMetric = await supabase.schema('ops')
    .from('system_metrics')
    .select('numeric_value')
    .eq('metric_key', 'sob.ytd_yield')
    .order('recorded_at', { ascending: false })
    .limit(1)
    .single()

  return new Response(JSON.stringify({
    status: 'ONLINE',
    latency: '24ms',
    node: 'LX-990',
    engine_version: 'V4.82',
    last_scan: new Date().toISOString(),
    global_exposure: exposure,
    ytd_yield: lastMetric.data?.numeric_value ?? null,
  }), { headers: { 'Content-Type': 'application/json' } })
})
```

### 7.2 `docusign-webhook` — réception callbacks

**`supabase/functions/docusign-webhook/index.ts`** : valide HMAC `DOCUSIGN_WEBHOOK_SECRET`, update `crm.sales_pipeline_items.stage` selon event (`envelope-sent`,`envelope-opened`,`envelope-signed`,`recipient-completed`), append à `ops.agent_events`.

### 7.3 `intake-handler` — Bana form

Reçoit le POST depuis IntakeForm.tsx, valide payload, écrit dans `app.intake_submissions`, déclenche éventuellement webhook n8n, retourne `{ success, message }`.

### 7.4 `case-confidence-recalc` — cron quotidien

Recalcule `confidence_score` selon signaux (DocuSign opened, court filing stage, age, etc.). Trigger via Supabase Cron (`pg_cron` extension).

### 7.5 `audit-rotate` — cleanup hebdo

Archive `audit.log` lignes > 90 jours vers Storage `audit-archive/YYYY-MM.jsonl.gz`, supprime de la table chaude.

---

## 8. Realtime channels

### 8.1 Tables exposées Realtime (CDC)

Dans Supabase Studio → Database → Replication → activer `realtime` pour :

- `app.cases` (Dashboard Wind Direction + Docket live)
- `app.transactions` (Finance ledger live)
- `crm.sales_pipeline_items` (Sales Sanctum kanban)
- `crm.court_filings` (Legal kanban)
- `ops.wind_direction_alerts` (alerts pop-up)
- `crm.feed_events` (Growth feed)

### 8.2 Pattern client Next.js

```ts
useEffect(() => {
  const supabase = createSupabaseBrowserClient()
  const channel = supabase
    .channel('dashboard:cases')
    .on('postgres_changes',
      { event: '*', schema: 'app', table: 'cases' },
      (payload) => refreshCasesQuery(payload))
    .subscribe()
  return () => { supabase.removeChannel(channel) }
}, [])
```

---

## 9. Refactor code Next.js — Mocks → Supabase JS

### 9.1 Avant (`src/lib/actions.ts`)

```ts
"use server";
import { MOCK_ASSETS, Asset } from "./store";

export async function getAssets(): Promise<Asset[]> {
  await new Promise((r) => setTimeout(r, 500));
  return MOCK_ASSETS;
}
```

### 9.2 Après

```ts
"use server";
import { createSupabaseServerClient } from "./supabase/server";

export type Case = {
  id: string
  case_number: string
  defendant: string
  amount: number
  priority: 'genealogie'|'b2b'|'expulsion'|'other'
  status: string
  confidence_score: number
}

export async function getActiveCases(): Promise<Case[]> {
  const supabase = await createSupabaseServerClient()
  const { data, error } = await supabase
    .schema('app').from('cases')
    .select('id, case_number, defendant, amount, priority, status, confidence_score')
    .is('deleted_at', null)
    .order('amount', { ascending: false })
    .limit(50)

  if (error) {
    console.error('[getActiveCases]', error)
    return []
  }
  return data as Case[]
}

export async function submitIntake(formData: FormData) {
  const supabase = await createSupabaseServerClient()
  const payload = Object.fromEntries(formData.entries())

  const { data, error } = await supabase
    .schema('app').from('intake_submissions')
    .insert({
      source: 'bana_intake',
      payload,
      defender_email: payload.email as string | null,
      defender_phone: payload.phone as string | null,
    })
    .select('id')
    .single()

  if (error) {
    return { success: false, message: error.message }
  }

  // Optional: forward to n8n
  const webhookUrl = process.env.N8N_WEBHOOK_URL
  if (webhookUrl) {
    fetch(webhookUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ source: 'BANA_INTAKE_ACTION', submission_id: data?.id, payload }),
    }).catch(e => console.error('Webhook failed:', e))
  }

  return { success: true, message: 'Audit Request Secured', id: data?.id }
}
```

### 9.3 Tableau de remplacement composant par composant

| Composant | Données mockées actuelles | Source Supabase (après refactor) |
|---|---|---|
| `Dashboard.tsx` `pipelineData` | hardcoded W1-W6 | RPC `app.dashboard_pipeline_weekly()` (vue agrégée) |
| `Dashboard.tsx` `alerts` | hardcoded | `select * from ops.wind_direction_alerts where acknowledged_at is null order by created_at desc limit 5` |
| `Dashboard.tsx` StatCards | hardcoded | RPC `app.dashboard_kpis()` retournant tresorerie/pipeline/conversion |
| `Finance.tsx` `ledgerData` | hardcoded 5 rows | `app.transactions` select ordered by tx_date desc |
| `Docket.tsx` `mockLeads` | hardcoded 5 cases | `app.cases` select where status in ('new','tracking','ready') |
| `Clients.tsx` `mockClients` | hardcoded 3 | `app.clients` select where deleted_at is null |
| `Legal.tsx` `kanbanData` | hardcoded 4 stages | `crm.court_filings` group by stage |
| `SalesSanctum.tsx` `kanbanData` | hardcoded 4 stages | `crm.sales_pipeline_items` group by stage |
| `People.tsx` Roster | hardcoded agents | `ops.agents` where is_active = true |
| `Knowledge.tsx` mockDoc + categories | hardcoded | `app.knowledge_docs` |
| `Growth.tsx` cohorts + feed | hardcoded | `crm.cohorts` + `crm.feed_events` |
| `bana/IntakeForm.tsx` | submitIntake mock | submitIntake → `app.intake_submissions` |

---

## 10. Vues + RPC Functions (helpers)

```sql
-- Migration 009_views_and_rpc.sql

-- Dashboard KPIs (single row)
CREATE OR REPLACE FUNCTION app.dashboard_kpis()
RETURNS TABLE (
  treasury_mtd       NUMERIC,
  pipeline_value     NUMERIC,
  conversion_rate    NUMERIC,
  avg_delay_weeks    NUMERIC
) LANGUAGE sql STABLE SECURITY DEFINER AS $$
  WITH mtd AS (
    SELECT COALESCE(SUM(CASE WHEN tx_type='inflow' THEN amount ELSE -amount END), 0) AS net
    FROM app.transactions
    WHERE date_trunc('month', tx_date) = date_trunc('month', current_date)
      AND status = 'completed'
      AND deleted_at IS NULL
  ),
  pipeline AS (
    SELECT COALESCE(SUM(amount), 0) AS val
    FROM app.cases
    WHERE status IN ('ready','filed','hearing')
      AND deleted_at IS NULL
  ),
  conv AS (
    SELECT
      (COUNT(*) FILTER (WHERE status = 'won'))::NUMERIC
      / NULLIF((COUNT(*) FILTER (WHERE status IN ('won','lost'))), 0) AS rate
    FROM app.cases
    WHERE deleted_at IS NULL
  ),
  delay AS (
    SELECT AVG(EXTRACT(EPOCH FROM (updated_at - created_at))/86400/7)::NUMERIC AS weeks
    FROM app.cases
    WHERE status IN ('won','lost') AND deleted_at IS NULL
  )
  SELECT mtd.net, pipeline.val, conv.rate, delay.weeks FROM mtd, pipeline, conv, delay;
$$;

-- Pipeline weekly growth (6 last weeks)
CREATE OR REPLACE FUNCTION app.dashboard_pipeline_weekly()
RETURNS TABLE (week_label TEXT, value NUMERIC)
LANGUAGE sql STABLE SECURITY DEFINER AS $$
  WITH weeks AS (
    SELECT generate_series(
      date_trunc('week', current_date) - INTERVAL '5 weeks',
      date_trunc('week', current_date),
      INTERVAL '1 week'
    ) AS week_start
  )
  SELECT
    'W' || (row_number() OVER (ORDER BY week_start))::TEXT AS week_label,
    COALESCE(SUM(c.amount), 0) AS value
  FROM weeks w
  LEFT JOIN app.cases c
    ON date_trunc('week', c.created_at) = w.week_start
   AND c.deleted_at IS NULL
  GROUP BY w.week_start
  ORDER BY w.week_start;
$$;
```

---

## 11. Déploiement Hostinger Business (Node.js Application)

### 11.1 Pré-requis Hostinger Business

- ✅ Plan Business actif (`kalybana.com`, 5 Node.js apps)
- ✅ Sous-domaine prêt : `alykaly.kalybana.com` (créer dans hPanel)
- ✅ Repo Git (privé) avec le projet `alykaly-os-V2`
- ✅ SSL Let's Encrypt auto via hPanel
- ✅ Node.js version 22 (alignée Dockerfile actuel)

### 11.2 Étapes hPanel

1. **hPanel → Websites → Add Website → Subdomain** : `alykaly.kalybana.com`
2. **Advanced → Node.js** :
   - Application root : `/home/u<XXX>/domains/kalybana.com/public_html/alykaly`
   - Application URL : `https://alykaly.kalybana.com`
   - Application startup file : `server.js`
   - Node version : 22
   - Environment vars : ajouter les 5 vars de §5.2
3. **Git Deploy** :
   - Clone repo dans application root
   - `npm ci`
   - `npm run build` → génère `.next/standalone/server.js`
   - Copier `.next/standalone/*` à la racine de l'app (Hostinger lance directement le startup file)
   - Copier `public/` et `.next/static/` aux endroits attendus par standalone
4. **Restart Application** dans hPanel
5. **Health check** : `curl https://alykaly.kalybana.com/api/engine/status`

### 11.3 Build artefact layout attendu

Next.js standalone produit cette arbo :

```
.next/standalone/
├── server.js              ← Application startup file Hostinger
├── package.json
├── node_modules/          ← only required deps (lean)
└── .next/
    └── server/
```

Avec, à côté :
```
public/                    ← copier manuellement (n'est pas dans standalone)
.next/static/              ← copier manuellement
```

**Script `deploy/hostinger.sh`** (à créer) :

```bash
#!/usr/bin/env bash
set -euo pipefail
APP_ROOT=$1  # /home/uXXX/domains/kalybana.com/public_html/alykaly

npm ci
npm run build

rsync -a --delete .next/standalone/ "$APP_ROOT/"
mkdir -p "$APP_ROOT/.next/static" "$APP_ROOT/public"
rsync -a .next/static/ "$APP_ROOT/.next/static/"
rsync -a public/ "$APP_ROOT/public/"

echo "[OK] Deployed to $APP_ROOT — restart Node.js app in hPanel"
```

### 11.4 CI/CD GitHub Actions (optionnel)

`.github/workflows/deploy.yml` : SSH vers Hostinger, pull, build, restart via API hPanel. À spécifier dans une itération suivante (Phase 5+).

### 11.5 DNS

- `alykaly.kalybana.com` → A record vers IP Hostinger Business (auto si subdomain créé via hPanel)
- Si Supabase self-hosted sur kalybana.com : sous-domaine séparé `supabase.kalybana.com` déjà existant per ADR.

---

## 12. Observability & Backups

### 12.1 Backups Supabase

- **Daily** auto (Supabase Cloud : inclus ; self-hosted : `pg_dump` cron via Hostinger Business backups quotidiens)
- **WAL archiving** vers Storage bucket dédié si auto-host
- **Restore drill** : 1×/trimestre, doc dans `_SPECS/ADR/`

### 12.2 Monitoring

- **Supabase Studio Logs** : Edge Functions + Postgres slow queries
- **Hostinger logs** : Application Manager → Logs (Node.js stdout/stderr)
- **`get_advisors` MCP** : Claude Code peut exécuter advisor checks
- **Wind Direction** : table `ops.wind_direction_alerts` agrège les anomalies cross-stack et les expose au Dashboard

### 12.3 Audit log review

Mission heartbeat Shadow_L2 dédiée : scan `audit.log` last 24h, alerte si action sensible (DELETE on `app.cases`, UPDATE `identity.profiles.role`, etc.).

---

## 13. Décisions ouvertes (A0 doit trancher)

| ID | Décision | Options | Recommandation |
|---|---|---|---|
| D-01 | Supabase cloud vs self-hosted | (a) Cloud (vélocité) — (b) `supabase.kalybana.com` self-host | **b** (souveraineté A'Space, ADR existant) |
| D-02 | Single vs split Hostinger apps | (a) une app `alykaly.kalybana.com` pour tout — (b) `app.` (dashboard) + `bana.` (landing) séparés | **b** (deploy indépendant, sécurité, perf cache différente) |
| D-03 | n8n hosting | (a) Hostinger Business VPS séparé — (b) Hetzner/autre VPS — (c) n8n.io cloud | A0 décide selon coût |
| D-04 | DocuSign sandbox vs prod dès P3 | (a) sandbox d'abord — (b) prod direct | **a** (test fixtures pour edge function) |
| D-05 | Realtime activé dès P1 ou P6 | (a) P1 (early test) — (b) P6 (après stabilisation schema) | **b** (évite churn migrations CDC) |

---

## 14. Acceptance Criteria

- [ ] **AC-01** — Schema déployé : 15 tables, 6 schemas, 30+ RLS policies, audit triggers actifs.
- [ ] **AC-02** — Test RLS : un user role=viewer ne peut pas INSERT/UPDATE/DELETE sur `app.cases`.
- [ ] **AC-03** — Test clearance : user clearance=level_1 ne voit pas les rows `clearance_required=level_5_sovereign`.
- [ ] **AC-04** — Bana intake form anon POST réussit, INSERT visible dans `app.intake_submissions`.
- [ ] **AC-05** — Edge function `sob-engine-simulate` retourne JSON avec `global_exposure` calculé depuis DB live.
- [ ] **AC-06** — Refactor `actions.ts` : `getActiveCases()` retourne données réelles depuis `app.cases`.
- [ ] **AC-07** — Realtime : modification d'un row `app.cases` provoque update Dashboard sans refresh.
- [ ] **AC-08** — Deploy Hostinger : `https://alykaly.kalybana.com` répond 200, login + dashboard accessible.
- [ ] **AC-09** — Audit log : DELETE sur `app.cases` génère 1 row dans `audit.log` avec actor_id correct.
- [ ] **AC-10** — Backup restore drill : `pg_dump` → restore sur DB test passe sans erreur.

---

## 15. Annexes

### 15.1 Sample seed data (`supabase/seed.sql`)

```sql
-- Insert seed agents (matches People.tsx Roster)
INSERT INTO ops.agents (slug, display_name, kind, description, endpoint) VALUES
  ('jerry-n8n', 'Jerry', 'synthetic', 'Orchestrateur N8N (Airtable, DocuSign, Supabase)', 'https://n8n.kalybana.com/webhook/jerry'),
  ('docusign-bot', 'DocuSign Bot', 'webhook', 'Réception callbacks DocuSign', null),
  ('case-sourcer', 'Case Sourcer', 'cron', 'Scan PACER quotidien', null)
ON CONFLICT (org_id, slug) DO NOTHING;

-- Insert default knowledge categories
INSERT INTO app.knowledge_docs (category, title, body_md) VALUES
  ('call-script', 'Bana — Audit Cold Call FR', 'Bonjour [Nom], c''est [Prénom] du service d''audit Alykaly...'),
  ('faq', 'Qu''est-ce qu''un Surplus Fund ?', 'Un surplus fund est le montant restant après...'),
  ('procedure', 'Process DocuSign cession', '1. Préparer envelope...');
```

### 15.2 Commande Supabase CLI

```bash
# Init projet local
npx supabase init

# Lier au projet distant
npx supabase link --project-ref <ref> --password <db-password>

# Generate types TypeScript depuis DB
npx supabase gen types typescript --linked > src/lib/supabase/database.types.ts

# Lancer migrations
npx supabase db push

# Lancer edge function dev local
npx supabase functions serve sob-engine-simulate --env-file .env.local

# Deploy edge function
npx supabase functions deploy sob-engine-simulate
```

### 15.3 Coût estimé mensuel

| Composant | Coût |
|---|---|
| Hostinger Business plan (déjà payé) | inclus |
| Supabase self-hosted `supabase.kalybana.com` | inclus dans VPS existant |
| Supabase Cloud (alternative D-01a) | $25/mo Pro plan |
| DocuSign API | $40+/mo selon volume |
| n8n auto-host | inclus VPS Hostinger |
| **Total marginal** | **~$0-65/mo selon D-01/D-03** |

### 15.4 Risques résiduels & mitigations

| Risque | Mitigation |
|---|---|
| Hostinger Node.js app ne supporte pas streaming SSE/WebSocket → Realtime KO côté browser via WS direct | Supabase Realtime WS = client direct au Supabase, pas via Hostinger → OK |
| Cold start Hostinger après inactivity | Cron interne `/api/engine/status` toutes les 10 min pour keep warm |
| `pg_cron` non dispo sur Supabase self-hosted | Utiliser GitHub Actions schedule pour cron Edge functions |
| Migrations breaking en prod | Branches Supabase Cloud (uniquement) OU dump-test-restore en pre-prod |
| Audit log ballonne (>10M rows) | `audit-rotate` edge function archive vers Storage trimestriellement |

---

## 16. Prochaine étape immédiate

> A0 valide cette stratégie → je passe à **P0 (Bootstrap)** :
> 1. Confirme D-01 (cloud vs self-host) et D-02 (single vs split app)
> 2. Je crée les fichiers `supabase/migrations/001_*.sql` à `009_*.sql` (DDL prêt à exécuter)
> 3. Je peux exécuter directement via `mcp__plugin_supabase_supabase__apply_migration` si tu pointes vers ton projet
> 4. Je scaffolde `src/lib/supabase/*.ts` (client/server/admin)
> 5. Je commence le refactor `actions.ts` (Phase P4 démarre en parallèle dès que P1 est posé)

**Status :** DRAFT_FOR_A0_VALIDATION — pending Turn 3 (per AGENTS.md 3-Turn BMad Protocol)
