-- ============================================================================
-- Alykaly OS — Migration 001
-- Bootstrap : schemas, extensions, enums
-- ============================================================================

-- ===== Schemas =====
CREATE SCHEMA IF NOT EXISTS app;
CREATE SCHEMA IF NOT EXISTS crm;
CREATE SCHEMA IF NOT EXISTS identity;
CREATE SCHEMA IF NOT EXISTS ops;
CREATE SCHEMA IF NOT EXISTS audit;

COMMENT ON SCHEMA app      IS 'Business core entities (cases, clients, transactions, knowledge)';
COMMENT ON SCHEMA crm      IS 'Pipelines & relationship management (sales, court, documents, growth)';
COMMENT ON SCHEMA identity IS 'Users, roles, clearance levels';
COMMENT ON SCHEMA ops      IS 'Operational telemetry (agents, events, metrics, alerts)';
COMMENT ON SCHEMA audit    IS 'Append-only audit log of mutations on sensitive tables';

-- Grant usage so PostgREST exposes them (Supabase pattern)
GRANT USAGE ON SCHEMA app      TO authenticated, anon, service_role;
GRANT USAGE ON SCHEMA crm      TO authenticated, anon, service_role;
GRANT USAGE ON SCHEMA identity TO authenticated, anon, service_role;
GRANT USAGE ON SCHEMA ops      TO authenticated, anon, service_role;
GRANT USAGE ON SCHEMA audit    TO authenticated, service_role;

-- ===== Extensions =====
CREATE EXTENSION IF NOT EXISTS "pgcrypto";    -- gen_random_uuid
CREATE EXTENSION IF NOT EXISTS "pg_trgm";     -- fuzzy search defendants/clients

-- ===== Enums : business =====
CREATE TYPE app.case_priority AS ENUM ('genealogie', 'b2b', 'expulsion', 'other');
CREATE TYPE app.case_status   AS ENUM ('new', 'tracking', 'ready', 'filed', 'hearing', 'won', 'lost', 'archived');
CREATE TYPE app.tx_type       AS ENUM ('inflow', 'outflow');
CREATE TYPE app.tx_status     AS ENUM ('pending', 'completed', 'failed', 'reversed');
CREATE TYPE app.client_module AS ENUM ('cession', 'buyout', 'audit_only');

-- ===== Enums : identity =====
CREATE TYPE identity.user_role       AS ENUM ('admin', 'operator', 'agent', 'viewer', 'client');
CREATE TYPE identity.clearance_level AS ENUM ('level_0_public', 'level_1_internal', 'level_3_restricted', 'level_5_sovereign');

-- ===== Enums : crm =====
CREATE TYPE crm.sales_stage   AS ENUM ('audit', 'sent', 'opened', 'signed', 'lost');
CREATE TYPE crm.court_stage   AS ENUM ('ready', 'filed', 'hearing', 'signed', 'closed');

-- ===== Enums : ops =====
CREATE TYPE ops.agent_kind     AS ENUM ('synthetic', 'human', 'webhook', 'cron');
CREATE TYPE ops.event_severity AS ENUM ('debug', 'info', 'warning', 'critical');
