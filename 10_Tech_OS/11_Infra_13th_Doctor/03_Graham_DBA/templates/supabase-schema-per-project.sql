-- ============================================================================
-- Supabase Self-Host - Schema-Per-Project Multi-Tenancy Pattern
-- ============================================================================
-- Date    : 2026-05-27 (v2 refactor - DO-block dynamic SQL only)
-- Auteur  : A0 Amadeus + A2 Claude Code
-- Niveau  : L0 Tech OS / Graham DBA squad
-- Ancre   : ADR-INFRA-001 (PM2 VPS prod), ADR-MESH-L2-001 (Notion=What, Airtable=HowMuch)
-- Cible   : 1 instance Supabase = 1 Postgres = N schemas (1 par projet/tenant)
-- ============================================================================
--
-- USAGE
--   docker exec -i supabase-db psql -U postgres -d postgres \
--        -v project_slug=acme_solaris -f /tmp/schema-per-project.sql
--
-- IMPORTANT - project_slug MUST be a valid PostgreSQL identifier:
--   - lowercase
--   - alphanumeric + underscores only (NO dashes - use underscores)
--   - <= 50 chars
-- ============================================================================

\set ON_ERROR_STOP on

-- psql client variable -> server GUC bridge (DO blocks cant see :'var' directly)
SET aspace.project_slug = :'project_slug';

DO $bootstrap$
DECLARE
  v_slug   text := current_setting('aspace.project_slug');
  v_schema text := 'tenant_'  || v_slug;
  v_role   text := 'role_'    || v_slug;
  v_anon   text := 'anon_'    || v_slug;
  v_pwd    text := md5(random()::text || clock_timestamp()::text);
BEGIN
  -- ====== 1. Schema =========================================================
  EXECUTE format('CREATE SCHEMA IF NOT EXISTS %I', v_schema);
  EXECUTE format('COMMENT ON SCHEMA %I IS %L',
                 v_schema,
                 'Tenant schema for project: ' || v_slug
                 || ' - Created ' || now()::date::text);

  -- ====== 2. Role login dedie ==============================================
  IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = v_role) THEN
    EXECUTE format('CREATE ROLE %I LOGIN PASSWORD %L NOINHERIT', v_role, v_pwd);
    RAISE NOTICE 'Role % created with random password (rotate via ALTER ROLE)', v_role;
  ELSE
    RAISE NOTICE 'Role % already exists - skipped', v_role;
  END IF;

  EXECUTE format('GRANT USAGE, CREATE ON SCHEMA %I TO %I', v_schema, v_role);
  EXECUTE format(
    'ALTER DEFAULT PRIVILEGES IN SCHEMA %I '
    'GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO %I', v_schema, v_role);
  EXECUTE format(
    'ALTER DEFAULT PRIVILEGES IN SCHEMA %I '
    'GRANT USAGE, SELECT ON SEQUENCES TO %I', v_schema, v_role);
  EXECUTE format(
    'ALTER DEFAULT PRIVILEGES IN SCHEMA %I '
    'GRANT EXECUTE ON FUNCTIONS TO %I', v_schema, v_role);
  EXECUTE format(
    'ALTER ROLE %I SET search_path = %I, public, extensions',
    v_role, v_schema);

  -- ====== 3. Role anon (lecture publique limitee) ==========================
  IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = v_anon) THEN
    EXECUTE format('CREATE ROLE %I NOLOGIN', v_anon);
  END IF;
  EXECUTE format('GRANT USAGE ON SCHEMA %I TO %I', v_schema, v_anon);
  EXECUTE format(
    'ALTER DEFAULT PRIVILEGES IN SCHEMA %I GRANT SELECT ON TABLES TO %I',
    v_schema, v_anon);

  -- ====== 4. Tables de base du mesh L2 =====================================
  EXECUTE format($t$
    CREATE TABLE IF NOT EXISTS %I.sops (
      sop_id            text PRIMARY KEY,
      notion_page_id    text UNIQUE NOT NULL,
      title             text NOT NULL,
      domain            text NOT NULL CHECK (domain IN
        ('Growth','Sales','Product','Ops','IT','Finance','People','Legal')),
      status            text NOT NULL CHECK (status IN
        ('Draft','Active','Deprecated','Under_Audit')),
      owner_vp          text,
      executor_b3       text[],
      trigger           text,
      build_gate        text,
      template_version  text,
      loom_url          text,
      context_pack_url  text,
      number            numeric,
      last_audited      date,
      synced_at         timestamptz NOT NULL DEFAULT now(),
      notion_updated_at timestamptz
    )
  $t$, v_schema);

  EXECUTE format(
    'CREATE INDEX IF NOT EXISTS sops_domain_status_idx ON %I.sops (domain, status)',
    v_schema);
  EXECUTE format(
    'CREATE INDEX IF NOT EXISTS sops_status_active_idx ON %I.sops (status) '
    'WHERE status = ''Active''', v_schema);

  EXECUTE format($t$
    CREATE TABLE IF NOT EXISTS %I.squads (
      squad_id       text PRIMARY KEY,
      notion_page_id text UNIQUE NOT NULL,
      name           text NOT NULL,
      domain         text NOT NULL,
      members        jsonb,
      lore           text,
      stack          text[],
      synced_at      timestamptz NOT NULL DEFAULT now()
    )
  $t$, v_schema);

  EXECUTE format($t$
    CREATE TABLE IF NOT EXISTS %I.symphony_log (
      id           bigserial PRIMARY KEY,
      worker       text NOT NULL,
      level        text NOT NULL CHECK (level IN ('INFO','WARN','PANIC','DLQ')),
      message      text NOT NULL,
      payload      jsonb,
      created_at   timestamptz NOT NULL DEFAULT now()
    )
  $t$, v_schema);

  EXECUTE format(
    'CREATE INDEX IF NOT EXISTS symphony_log_created_at_idx '
    'ON %I.symphony_log (created_at DESC)', v_schema);
  EXECUTE format(
    'CREATE INDEX IF NOT EXISTS symphony_log_level_idx '
    'ON %I.symphony_log (level) WHERE level IN (''PANIC'',''DLQ'')',
    v_schema);

  -- ====== 5. Audit log =====================================================
  EXECUTE format($t$
    INSERT INTO %I.symphony_log (worker, level, message, payload)
    VALUES ('schema-provisioner', 'INFO',
            'Schema provisioned',
            jsonb_build_object(
              'schema',  %L,
              'role',    %L,
              'anon',    %L,
              'at',      now()::text
            ))
  $t$, v_schema, v_schema, v_role, v_anon);

  RAISE NOTICE 'OK - Schema: % | Role: % | Anon: %', v_schema, v_role, v_anon;
END $bootstrap$;

-- ============================================================================
-- RLS template (a appliquer table par table apres provisioning) :
--
--   ALTER TABLE tenant_<slug>.<table> ENABLE ROW LEVEL SECURITY;
--   CREATE POLICY tenant_isolation ON tenant_<slug>.<table>
--     USING (tenant_id = current_setting('app.current_tenant', true));
-- ============================================================================
