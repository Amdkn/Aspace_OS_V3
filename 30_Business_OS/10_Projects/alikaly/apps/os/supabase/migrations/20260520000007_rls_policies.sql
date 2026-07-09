-- ============================================================================
-- Alykaly OS — Migration 007
-- Row Level Security policies
-- ============================================================================

-- ===== Enable RLS on all business tables =====
ALTER TABLE identity.profiles          ENABLE ROW LEVEL SECURITY;
ALTER TABLE app.cases                  ENABLE ROW LEVEL SECURITY;
ALTER TABLE app.clients                ENABLE ROW LEVEL SECURITY;
ALTER TABLE app.transactions           ENABLE ROW LEVEL SECURITY;
ALTER TABLE app.knowledge_docs         ENABLE ROW LEVEL SECURITY;
ALTER TABLE app.intake_submissions     ENABLE ROW LEVEL SECURITY;
ALTER TABLE crm.sales_pipeline_items   ENABLE ROW LEVEL SECURITY;
ALTER TABLE crm.court_filings          ENABLE ROW LEVEL SECURITY;
ALTER TABLE crm.documents              ENABLE ROW LEVEL SECURITY;
ALTER TABLE crm.cohorts                ENABLE ROW LEVEL SECURITY;
ALTER TABLE crm.feed_events            ENABLE ROW LEVEL SECURITY;
ALTER TABLE ops.agents                 ENABLE ROW LEVEL SECURITY;
ALTER TABLE ops.agent_events           ENABLE ROW LEVEL SECURITY;
ALTER TABLE ops.system_metrics         ENABLE ROW LEVEL SECURITY;
ALTER TABLE ops.wind_direction_alerts  ENABLE ROW LEVEL SECURITY;
ALTER TABLE audit.log                  ENABLE ROW LEVEL SECURITY;

-- ===== PROFILES =====
CREATE POLICY profiles_select_self_or_admin ON identity.profiles
  FOR SELECT TO authenticated USING (
    user_id = auth.uid()
    OR (identity.current_user_role() = 'admin' AND org_id = identity.current_user_org())
  );

CREATE POLICY profiles_update_self ON identity.profiles
  FOR UPDATE TO authenticated USING (user_id = auth.uid())
  WITH CHECK (user_id = auth.uid());

CREATE POLICY profiles_update_admin ON identity.profiles
  FOR UPDATE TO authenticated USING (
    identity.current_user_role() = 'admin'
    AND org_id = identity.current_user_org()
  );

-- ===== CASES =====
CREATE POLICY cases_select_org_clearance ON app.cases
  FOR SELECT TO authenticated USING (
    org_id = identity.current_user_org()
    AND identity.clearance_at_least(clearance_required)
    AND deleted_at IS NULL
  );

CREATE POLICY cases_insert_operator ON app.cases
  FOR INSERT TO authenticated WITH CHECK (
    identity.current_user_role() IN ('admin','operator')
    AND org_id = identity.current_user_org()
  );

CREATE POLICY cases_update_assigned ON app.cases
  FOR UPDATE TO authenticated USING (
    org_id = identity.current_user_org()
    AND (
      identity.current_user_role() = 'admin'
      OR assigned_to = auth.uid()
    )
  );

CREATE POLICY cases_delete_admin ON app.cases
  FOR DELETE TO authenticated USING (identity.current_user_role() = 'admin');

-- ===== CLIENTS =====
CREATE POLICY clients_select_org_clearance ON app.clients
  FOR SELECT TO authenticated USING (
    org_id = identity.current_user_org()
    AND identity.clearance_at_least(clearance_required)
    AND deleted_at IS NULL
  );

CREATE POLICY clients_insert_operator ON app.clients
  FOR INSERT TO authenticated WITH CHECK (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator')
  );

CREATE POLICY clients_update_operator ON app.clients
  FOR UPDATE TO authenticated USING (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator')
  );

CREATE POLICY clients_delete_admin ON app.clients
  FOR DELETE TO authenticated USING (identity.current_user_role() = 'admin');

-- ===== TRANSACTIONS =====
CREATE POLICY tx_select_org ON app.transactions
  FOR SELECT TO authenticated USING (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator','viewer')
    AND deleted_at IS NULL
  );

CREATE POLICY tx_insert_operator ON app.transactions
  FOR INSERT TO authenticated WITH CHECK (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator')
  );

CREATE POLICY tx_update_admin ON app.transactions
  FOR UPDATE TO authenticated USING (identity.current_user_role() = 'admin');

-- No DELETE policy — soft-delete enforced

-- ===== CRM: sales_pipeline =====
CREATE POLICY sales_pipeline_org ON crm.sales_pipeline_items
  FOR ALL TO authenticated USING (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator','agent')
  );

-- ===== CRM: court_filings =====
CREATE POLICY court_filings_org ON crm.court_filings
  FOR ALL TO authenticated USING (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator','agent')
  );

-- ===== CRM: documents =====
CREATE POLICY documents_select_org_clearance ON crm.documents
  FOR SELECT TO authenticated USING (
    org_id = identity.current_user_org()
    AND identity.clearance_at_least(clearance_required)
    AND deleted_at IS NULL
  );

CREATE POLICY documents_insert_operator ON crm.documents
  FOR INSERT TO authenticated WITH CHECK (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator','agent')
  );

CREATE POLICY documents_update_owner_admin ON crm.documents
  FOR UPDATE TO authenticated USING (
    org_id = identity.current_user_org()
    AND (uploaded_by = auth.uid() OR identity.current_user_role() = 'admin')
  );

-- ===== CRM: cohorts + feed_events =====
CREATE POLICY cohorts_select_org ON crm.cohorts
  FOR SELECT TO authenticated USING (
    org_id = identity.current_user_org()
  );

CREATE POLICY cohorts_modify_operator ON crm.cohorts
  FOR ALL TO authenticated USING (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator')
  );

CREATE POLICY feed_select_org ON crm.feed_events
  FOR SELECT TO authenticated USING (
    org_id = identity.current_user_org()
  );

CREATE POLICY feed_insert_operator ON crm.feed_events
  FOR INSERT TO authenticated WITH CHECK (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator','agent')
  );

-- ===== KNOWLEDGE =====
CREATE POLICY knowledge_select_clearance ON app.knowledge_docs
  FOR SELECT TO authenticated USING (
    org_id = identity.current_user_org()
    AND identity.clearance_at_least(clearance_required)
    AND deleted_at IS NULL
  );

CREATE POLICY knowledge_insert_operator ON app.knowledge_docs
  FOR INSERT TO authenticated WITH CHECK (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator')
  );

CREATE POLICY knowledge_update_author ON app.knowledge_docs
  FOR UPDATE TO authenticated USING (
    org_id = identity.current_user_org()
    AND (author_id = auth.uid() OR identity.current_user_role() = 'admin')
  );

-- ===== INTAKE submissions =====
CREATE POLICY intake_insert_anon ON app.intake_submissions
  FOR INSERT TO anon WITH CHECK (true);

CREATE POLICY intake_select_operator ON app.intake_submissions
  FOR SELECT TO authenticated USING (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator','agent')
  );

CREATE POLICY intake_update_operator ON app.intake_submissions
  FOR UPDATE TO authenticated USING (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator','agent')
  );

-- ===== AUDIT log (admin read-only) =====
CREATE POLICY audit_log_select_admin ON audit.log
  FOR SELECT TO authenticated USING (identity.current_user_role() = 'admin');

-- ===== OPS: agents =====
CREATE POLICY agents_select_operator ON ops.agents
  FOR SELECT TO authenticated USING (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator','agent','viewer')
  );

CREATE POLICY agents_modify_admin ON ops.agents
  FOR ALL TO authenticated USING (
    identity.current_user_role() = 'admin'
    AND org_id = identity.current_user_org()
  );

-- ===== OPS: agent_events =====
CREATE POLICY agent_events_select_operator ON ops.agent_events
  FOR SELECT TO authenticated USING (
    identity.current_user_role() IN ('admin','operator')
  );

-- ===== OPS: system_metrics (public read for authenticated) =====
CREATE POLICY system_metrics_authenticated_read ON ops.system_metrics
  FOR SELECT TO authenticated USING (true);

-- ===== OPS: wind_direction_alerts =====
CREATE POLICY wind_select_org ON ops.wind_direction_alerts
  FOR SELECT TO authenticated USING (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator','agent','viewer')
  );

CREATE POLICY wind_ack_operator ON ops.wind_direction_alerts
  FOR UPDATE TO authenticated USING (
    org_id = identity.current_user_org()
    AND identity.current_user_role() IN ('admin','operator','agent')
  );
