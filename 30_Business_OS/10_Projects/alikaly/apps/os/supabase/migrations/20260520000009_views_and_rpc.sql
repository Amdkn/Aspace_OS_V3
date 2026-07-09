-- ============================================================================
-- Alykaly OS — Migration 009
-- Views + RPC functions for dashboard aggregates
-- ============================================================================

-- ===== Dashboard KPIs =====
CREATE OR REPLACE FUNCTION app.dashboard_kpis()
RETURNS TABLE (
  treasury_mtd     NUMERIC,
  pipeline_value   NUMERIC,
  conversion_rate  NUMERIC,
  avg_delay_weeks  NUMERIC
)
LANGUAGE sql STABLE SECURITY DEFINER SET search_path = app, identity, public AS $$
  WITH mtd AS (
    SELECT COALESCE(SUM(CASE WHEN tx_type='inflow' THEN amount ELSE -amount END), 0)::NUMERIC AS net
    FROM app.transactions
    WHERE date_trunc('month', tx_date) = date_trunc('month', current_date)
      AND status = 'completed'
      AND deleted_at IS NULL
      AND org_id = identity.current_user_org()
  ),
  pipeline AS (
    SELECT COALESCE(SUM(amount), 0)::NUMERIC AS val
    FROM app.cases
    WHERE status IN ('ready','filed','hearing')
      AND deleted_at IS NULL
      AND org_id = identity.current_user_org()
  ),
  conv AS (
    SELECT
      COALESCE(
        (COUNT(*) FILTER (WHERE status = 'won'))::NUMERIC
        / NULLIF((COUNT(*) FILTER (WHERE status IN ('won','lost'))), 0),
        0
      )::NUMERIC AS rate
    FROM app.cases
    WHERE deleted_at IS NULL
      AND org_id = identity.current_user_org()
  ),
  delay AS (
    SELECT COALESCE(
      AVG(EXTRACT(EPOCH FROM (updated_at - created_at))/86400/7),
      0
    )::NUMERIC AS weeks
    FROM app.cases
    WHERE status IN ('won','lost')
      AND deleted_at IS NULL
      AND org_id = identity.current_user_org()
  )
  SELECT mtd.net, pipeline.val, conv.rate, delay.weeks FROM mtd, pipeline, conv, delay;
$$;

GRANT EXECUTE ON FUNCTION app.dashboard_kpis() TO authenticated;

-- ===== Pipeline weekly growth (6 last weeks) =====
CREATE OR REPLACE FUNCTION app.dashboard_pipeline_weekly()
RETURNS TABLE (week_label TEXT, value NUMERIC)
LANGUAGE sql STABLE SECURITY DEFINER SET search_path = app, identity, public AS $$
  WITH weeks AS (
    SELECT generate_series(
      date_trunc('week', current_date) - INTERVAL '5 weeks',
      date_trunc('week', current_date),
      INTERVAL '1 week'
    ) AS week_start
  ),
  ranked AS (
    SELECT
      w.week_start,
      row_number() OVER (ORDER BY w.week_start) AS rn,
      COALESCE(SUM(c.amount), 0)::NUMERIC AS sum_amount
    FROM weeks w
    LEFT JOIN app.cases c
      ON date_trunc('week', c.created_at) = w.week_start
     AND c.deleted_at IS NULL
     AND c.org_id = identity.current_user_org()
    GROUP BY w.week_start
  )
  SELECT 'W' || rn::TEXT AS week_label, sum_amount AS value FROM ranked ORDER BY rn;
$$;

GRANT EXECUTE ON FUNCTION app.dashboard_pipeline_weekly() TO authenticated;

-- ===== Sales pipeline kanban view (Sales Sanctum) =====
CREATE OR REPLACE VIEW crm.sales_kanban AS
SELECT
  s.id,
  s.case_id,
  c.case_number AS cases,
  c.defendant   AS name,
  s.stage,
  s.envelope_id,
  s.views_count,
  s.last_event_at,
  s.org_id
FROM crm.sales_pipeline_items s
JOIN app.cases c ON c.id = s.case_id
WHERE c.deleted_at IS NULL;

GRANT SELECT ON crm.sales_kanban TO authenticated;

-- ===== Court kanban view (Legal) =====
CREATE OR REPLACE VIEW crm.court_kanban AS
SELECT
  f.id,
  f.case_id,
  c.case_number AS cases,
  c.defendant   AS name,
  f.stage,
  f.filed_at,
  f.hearing_at,
  f.filed_amount AS amount,
  f.delay_days,
  f.org_id
FROM crm.court_filings f
JOIN app.cases c ON c.id = f.case_id
WHERE c.deleted_at IS NULL;

GRANT SELECT ON crm.court_kanban TO authenticated;

-- ===== Ledger view (Finance) with case_number resolved =====
CREATE OR REPLACE VIEW app.ledger_view AS
SELECT
  t.id,
  t.tx_date AS date,
  c.case_number AS case_id_label,
  t.case_id,
  t.tx_type AS type,
  t.amount,
  t.status,
  t.description AS desc,
  t.org_id,
  t.created_at
FROM app.transactions t
JOIN app.cases c ON c.id = t.case_id
WHERE t.deleted_at IS NULL;

GRANT SELECT ON app.ledger_view TO authenticated;
