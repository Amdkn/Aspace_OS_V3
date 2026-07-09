-- =============================================================================
-- LIFE OS BOOTSTRAP V1.0 — Schema canon unifié 16 tables
-- Source de vérité : REALITY_MAP.md (ligne 190) + schema_migration.sql (V1.0)
-- Date           : 2026-06-17
-- Project ref    : hjweyhpmrxqsxfbibsnc.supabase.co
-- D1 receipts    :
--   - REALITY_MAP.md l.190 : UNIFIED schema = {id, title, metrics, type, updated_at, created_at}
--   - schema_migration.sql l.14-15 : 16 noms canon = 8 LD + 6 FW + 2 SYS
--   - Grep "CREATE TABLE" clone     : 0 base DDL found → D6 root cause no base DDL in repo
-- =============================================================================

-- Extensions ----------------------------------------------------------------
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Trigger function : auto-update updated_at -------------------------------
CREATE OR REPLACE FUNCTION public.tg_set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- =============================================================================
-- COUCHE 2 — Domaines de vie (LD01-LD08) — 8 tables
-- =============================================================================

-- LD01 — Business (Book / Biz)
CREATE TABLE IF NOT EXISTS public.ld01_business (
  id         uuid        PRIMARY KEY DEFAULT gen_random_uuid(),
  title      text        NOT NULL    DEFAULT '',
  metrics    jsonb                   DEFAULT '{}'::jsonb,
  type       text,
  created_at timestamptz             DEFAULT NOW(),
  updated_at timestamptz             DEFAULT NOW()
);
CREATE TRIGGER ld01_business_set_updated_at BEFORE UPDATE ON public.ld01_business
  FOR EACH ROW EXECUTE FUNCTION public.tg_set_updated_at();

-- LD02 — Finance (Saru / Balance)
CREATE TABLE IF NOT EXISTS public.ld02_finance (
  id         uuid        PRIMARY KEY DEFAULT gen_random_uuid(),
  title      text        NOT NULL    DEFAULT '',
  metrics    jsonb                   DEFAULT '{}'::jsonb,
  type       text,
  created_at timestamptz             DEFAULT NOW(),
  updated_at timestamptz             DEFAULT NOW()
);
CREATE TRIGGER ld02_finance_set_updated_at BEFORE UPDATE ON public.ld02_finance
  FOR EACH ROW EXECUTE FUNCTION public.tg_set_updated_at();

-- LD03 — Health (Culber / Hospital)
CREATE TABLE IF NOT EXISTS public.ld03_health (
  id         uuid        PRIMARY KEY DEFAULT gen_random_uuid(),
  title      text        NOT NULL    DEFAULT '',
  metrics    jsonb                   DEFAULT '{}'::jsonb,
  type       text,
  created_at timestamptz             DEFAULT NOW(),
  updated_at timestamptz             DEFAULT NOW()
);
CREATE TRIGGER ld03_health_set_updated_at BEFORE UPDATE ON public.ld03_health
  FOR EACH ROW EXECUTE FUNCTION public.tg_set_updated_at();

-- LD04 — Cognition (Tilly / Mind)
CREATE TABLE IF NOT EXISTS public.ld04_cognition (
  id         uuid        PRIMARY KEY DEFAULT gen_random_uuid(),
  title      text        NOT NULL    DEFAULT '',
  metrics    jsonb                   DEFAULT '{}'::jsonb,
  type       text,
  created_at timestamptz             DEFAULT NOW(),
  updated_at timestamptz             DEFAULT NOW()
);
CREATE TRIGGER ld04_cognition_set_updated_at BEFORE UPDATE ON public.ld04_cognition
  FOR EACH ROW EXECUTE FUNCTION public.tg_set_updated_at();

-- LD05 — Environment (Stamets / Network)
CREATE TABLE IF NOT EXISTS public.ld05_environment (
  id         uuid        PRIMARY KEY DEFAULT gen_random_uuid(),
  title      text        NOT NULL    DEFAULT '',
  metrics    jsonb                   DEFAULT '{}'::jsonb,
  type       text,
  created_at timestamptz             DEFAULT NOW(),
  updated_at timestamptz             DEFAULT NOW()
);
CREATE TRIGGER ld05_environment_set_updated_at BEFORE UPDATE ON public.ld05_environment
  FOR EACH ROW EXECUTE FUNCTION public.tg_set_updated_at();

-- LD06 — Relationships (Burnham / DEAL)
CREATE TABLE IF NOT EXISTS public.ld06_relationships (
  id         uuid        PRIMARY KEY DEFAULT gen_random_uuid(),
  title      text        NOT NULL    DEFAULT '',
  metrics    jsonb                   DEFAULT '{}'::jsonb,
  type       text,
  created_at timestamptz             DEFAULT NOW(),
  updated_at timestamptz             DEFAULT NOW()
);
CREATE TRIGGER ld06_relationships_set_updated_at BEFORE UPDATE ON public.ld06_relationships
  FOR EACH ROW EXECUTE FUNCTION public.tg_set_updated_at();

-- LD07 — Emotions (Reno / Maintenance)
CREATE TABLE IF NOT EXISTS public.ld07_emotions (
  id         uuid        PRIMARY KEY DEFAULT gen_random_uuid(),
  title      text        NOT NULL    DEFAULT '',
  metrics    jsonb                   DEFAULT '{}'::jsonb,
  type       text,
  created_at timestamptz             DEFAULT NOW(),
  updated_at timestamptz             DEFAULT NOW()
);
CREATE TRIGGER ld07_emotions_set_updated_at BEFORE UPDATE ON public.ld07_emotions
  FOR EACH ROW EXECUTE FUNCTION public.tg_set_updated_at();

-- LD08 — Purpose (Georgiou / Moat)
CREATE TABLE IF NOT EXISTS public.ld08_purpose (
  id         uuid        PRIMARY KEY DEFAULT gen_random_uuid(),
  title      text        NOT NULL    DEFAULT '',
  metrics    jsonb                   DEFAULT '{}'::jsonb,
  type       text,
  created_at timestamptz             DEFAULT NOW(),
  updated_at timestamptz             DEFAULT NOW()
);
CREATE TRIGGER ld08_purpose_set_updated_at BEFORE UPDATE ON public.ld08_purpose
  FOR EACH ROW EXECUTE FUNCTION public.tg_set_updated_at();

-- =============================================================================
-- COUCHE 3 — Frameworks (FW — transversaux) — 6 tables
-- =============================================================================

-- FW PARA (FolderRoot) — Projects/Areas/Resources/Archives
CREATE TABLE IF NOT EXISTS public.fw_para (
  id         uuid        PRIMARY KEY DEFAULT gen_random_uuid(),
  title      text        NOT NULL    DEFAULT '',
  metrics    jsonb                   DEFAULT '{}'::jsonb,
  type       text,
  created_at timestamptz             DEFAULT NOW(),
  updated_at timestamptz             DEFAULT NOW()
);
CREATE TRIGGER fw_para_set_updated_at BEFORE UPDATE ON public.fw_para
  FOR EACH ROW EXECUTE FUNCTION public.tg_set_updated_at();

-- FW Ikigai (Target) — Purpose/Mission/Passion/Vocation/Profession
CREATE TABLE IF NOT EXISTS public.fw_ikigai (
  id         uuid        PRIMARY KEY DEFAULT gen_random_uuid(),
  title      text        NOT NULL    DEFAULT '',
  metrics    jsonb                   DEFAULT '{}'::jsonb,
  type       text,
  created_at timestamptz             DEFAULT NOW(),
  updated_at timestamptz             DEFAULT NOW()
);
CREATE TRIGGER fw_ikigai_set_updated_at BEFORE UPDATE ON public.fw_ikigai
  FOR EACH ROW EXECUTE FUNCTION public.tg_set_updated_at();

-- FW Life Wheel (Compass) — 8 secteurs LD01-LD08 score
CREATE TABLE IF NOT EXISTS public.fw_life_wheel (
  id         uuid        PRIMARY KEY DEFAULT gen_random_uuid(),
  title      text        NOT NULL    DEFAULT '',
  metrics    jsonb                   DEFAULT '{}'::jsonb,
  type       text,
  created_at timestamptz             DEFAULT NOW(),
  updated_at timestamptz             DEFAULT NOW()
);
CREATE TRIGGER fw_life_wheel_set_updated_at BEFORE UPDATE ON public.fw_life_wheel
  FOR EACH ROW EXECUTE FUNCTION public.tg_set_updated_at();

-- FW 12 Week Year (CalendarRange) — Rocks / Scorecard / Lead-Lag
CREATE TABLE IF NOT EXISTS public.fw_12wy (
  id         uuid        PRIMARY KEY DEFAULT gen_random_uuid(),
  title      text        NOT NULL    DEFAULT '',
  metrics    jsonb                   DEFAULT '{}'::jsonb,
  type       text,
  created_at timestamptz             DEFAULT NOW(),
  updated_at timestamptz             DEFAULT NOW()
);
CREATE TRIGGER fw_12wy_set_updated_at BEFORE UPDATE ON public.fw_12wy
  FOR EACH ROW EXECUTE FUNCTION public.tg_set_updated_at();

-- FW GTD (Inbox) — Capture/Clarify/Organize/Reflect/Engage
CREATE TABLE IF NOT EXISTS public.fw_gtd (
  id         uuid        PRIMARY KEY DEFAULT gen_random_uuid(),
  title      text        NOT NULL    DEFAULT '',
  metrics    jsonb                   DEFAULT '{}'::jsonb,
  type       text,
  created_at timestamptz             DEFAULT NOW(),
  updated_at timestamptz             DEFAULT NOW()
);
CREATE TRIGGER fw_gtd_set_updated_at BEFORE UPDATE ON public.fw_gtd
  FOR EACH ROW EXECUTE FUNCTION public.tg_set_updated_at();

-- FW DEAL (Zap) — Define/Eliminate/Automate/Liberate
CREATE TABLE IF NOT EXISTS public.fw_deal (
  id         uuid        PRIMARY KEY DEFAULT gen_random_uuid(),
  title      text        NOT NULL    DEFAULT '',
  metrics    jsonb                   DEFAULT '{}'::jsonb,
  type       text,
  created_at timestamptz             DEFAULT NOW(),
  updated_at timestamptz             DEFAULT NOW()
);
CREATE TRIGGER fw_deal_set_updated_at BEFORE UPDATE ON public.fw_deal
  FOR EACH ROW EXECUTE FUNCTION public.tg_set_updated_at();

-- =============================================================================
-- COUCHE 1 — OS (Shell + Agents) — 2 tables
-- =============================================================================

-- SYS Agent Veto — Veto middleware (idb.ts : "OVERRIDE DENIED: Veto is Active")
CREATE TABLE IF NOT EXISTS public.sys_agent_veto (
  id         uuid        PRIMARY KEY DEFAULT gen_random_uuid(),
  title      text        NOT NULL    DEFAULT '',
  metrics    jsonb                   DEFAULT '{}'::jsonb,
  type       text,
  created_at timestamptz             DEFAULT NOW(),
  updated_at timestamptz             DEFAULT NOW()
);
CREATE TRIGGER sys_agent_veto_set_updated_at BEFORE UPDATE ON public.sys_agent_veto
  FOR EACH ROW EXECUTE FUNCTION public.tg_set_updated_at();

-- SYS Shell Routing — Cross-Link Router aspace://app/<name>/page/subpage
CREATE TABLE IF NOT EXISTS public.sys_shell_routing (
  id         uuid        PRIMARY KEY DEFAULT gen_random_uuid(),
  title      text        NOT NULL    DEFAULT '',
  metrics    jsonb                   DEFAULT '{}'::jsonb,
  type       text,
  created_at timestamptz             DEFAULT NOW(),
  updated_at timestamptz             DEFAULT NOW()
);
CREATE TRIGGER sys_shell_routing_set_updated_at BEFORE UPDATE ON public.sys_shell_routing
  FOR EACH ROW EXECUTE FUNCTION public.tg_set_updated_at();

-- =============================================================================
-- Indexes — fast filtered queries (type + created_at DESC)
-- =============================================================================
CREATE INDEX IF NOT EXISTS idx_ld01_business_type     ON public.ld01_business(type);
CREATE INDEX IF NOT EXISTS idx_ld01_business_created  ON public.ld01_business(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_ld02_finance_type      ON public.ld02_finance(type);
CREATE INDEX IF NOT EXISTS idx_ld02_finance_created   ON public.ld02_finance(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_ld03_health_type       ON public.ld03_health(type);
CREATE INDEX IF NOT EXISTS idx_ld03_health_created    ON public.ld03_health(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_ld04_cognition_type    ON public.ld04_cognition(type);
CREATE INDEX IF NOT EXISTS idx_ld04_cognition_created ON public.ld04_cognition(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_ld05_environment_type  ON public.ld05_environment(type);
CREATE INDEX IF NOT EXISTS idx_ld05_environment_created ON public.ld05_environment(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_ld06_relationships_type    ON public.ld06_relationships(type);
CREATE INDEX IF NOT EXISTS idx_ld06_relationships_created ON public.ld06_relationships(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_ld07_emotions_type     ON public.ld07_emotions(type);
CREATE INDEX IF NOT EXISTS idx_ld07_emotions_created  ON public.ld07_emotions(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_ld08_purpose_type      ON public.ld08_purpose(type);
CREATE INDEX IF NOT EXISTS idx_ld08_purpose_created   ON public.ld08_purpose(created_at DESC);

CREATE INDEX IF NOT EXISTS idx_fw_para_type           ON public.fw_para(type);
CREATE INDEX IF NOT EXISTS idx_fw_para_created        ON public.fw_para(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_fw_ikigai_type         ON public.fw_ikigai(type);
CREATE INDEX IF NOT EXISTS idx_fw_ikigai_created      ON public.fw_ikigai(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_fw_life_wheel_type     ON public.fw_life_wheel(type);
CREATE INDEX IF NOT EXISTS idx_fw_life_wheel_created  ON public.fw_life_wheel(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_fw_12wy_type           ON public.fw_12wy(type);
CREATE INDEX IF NOT EXISTS idx_fw_12wy_created        ON public.fw_12wy(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_fw_gtd_type            ON public.fw_gtd(type);
CREATE INDEX IF NOT EXISTS idx_fw_gtd_created         ON public.fw_gtd(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_fw_deal_type           ON public.fw_deal(type);
CREATE INDEX IF NOT EXISTS idx_fw_deal_created        ON public.fw_deal(created_at DESC);

CREATE INDEX IF NOT EXISTS idx_sys_agent_veto_type    ON public.sys_agent_veto(type);
CREATE INDEX IF NOT EXISTS idx_sys_agent_veto_created ON public.sys_agent_veto(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_sys_shell_routing_type    ON public.sys_shell_routing(type);
CREATE INDEX IF NOT EXISTS idx_sys_shell_routing_created ON public.sys_shell_routing(created_at DESC);

-- =============================================================================
-- Verification — assert 16 tables created
-- =============================================================================
DO $$
DECLARE
  table_count int;
BEGIN
  SELECT COUNT(*) INTO table_count
  FROM information_schema.tables
  WHERE table_schema = 'public'
    AND table_name IN (
      'ld01_business', 'ld02_finance', 'ld03_health', 'ld04_cognition',
      'ld05_environment', 'ld06_relationships', 'ld07_emotions', 'ld08_purpose',
      'fw_para', 'fw_ikigai', 'fw_life_wheel', 'fw_12wy', 'fw_gtd', 'fw_deal',
      'sys_agent_veto', 'sys_shell_routing'
    );
  RAISE NOTICE '✅ Life OS V1.0 bootstrap : % tables créées (attendu : 16)', table_count;
  IF table_count != 16 THEN
    RAISE EXCEPTION '❌ Attendu 16 tables, trouvé %', table_count;
  END IF;
END $$;

-- =============================================================================
-- Post-bootstrap manual steps (HUMAN / A0) :
-- 1. Run this SQL in Supabase SQL Editor (hjweyhpmrxqsxfbibsnc).
-- 2. Then run schema_migration.sql (adds user_id + RLS + user_profiles + handle_new_user trigger).
-- 3. Then run memory_migration.sql AFTER first signup (assigns user_id = admiral to all rows).
-- 4. Verify with : SELECT count(*) FROM information_schema.tables WHERE table_schema='public';
-- =============================================================================
