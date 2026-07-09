-- ============================================================================
-- Alykaly OS — Migration 010
-- Realtime activation (Postgres CDC to Supabase Realtime)
-- ============================================================================

-- Drop tables from default publication first (no-op if not present)
DO $$
BEGIN
  IF EXISTS (SELECT 1 FROM pg_publication WHERE pubname = 'supabase_realtime') THEN
    -- already exists, just alter
    NULL;
  ELSE
    EXECUTE 'CREATE PUBLICATION supabase_realtime';
  END IF;
END $$;

-- Add tables we want exposed via Realtime
ALTER PUBLICATION supabase_realtime ADD TABLE
  app.cases,
  app.transactions,
  crm.sales_pipeline_items,
  crm.court_filings,
  crm.feed_events,
  ops.wind_direction_alerts;

-- Replica identity FULL on tables where UPDATE/DELETE rows matter for Realtime payloads
ALTER TABLE app.cases                 REPLICA IDENTITY FULL;
ALTER TABLE app.transactions          REPLICA IDENTITY FULL;
ALTER TABLE crm.sales_pipeline_items  REPLICA IDENTITY FULL;
ALTER TABLE crm.court_filings         REPLICA IDENTITY FULL;
ALTER TABLE ops.wind_direction_alerts REPLICA IDENTITY FULL;

COMMENT ON PUBLICATION supabase_realtime IS 'Tables exposed via Supabase Realtime (CDC)';
