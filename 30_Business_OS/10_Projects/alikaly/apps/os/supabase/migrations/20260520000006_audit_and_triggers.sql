-- ============================================================================
-- Alykaly OS — Migration 006
-- Audit log + updated_at triggers
-- ============================================================================

-- ===== updated_at trigger (generic) =====
CREATE OR REPLACE FUNCTION public.set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = now();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Apply to all tables having updated_at
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
      'DROP TRIGGER IF EXISTS set_updated_at ON %I.%I; CREATE TRIGGER set_updated_at BEFORE UPDATE ON %I.%I FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();',
      t.table_schema, t.table_name, t.table_schema, t.table_name
    );
  END LOOP;
END $$;

-- ===== AUDIT LOG (append-only) =====
CREATE TABLE audit.log (
  id            BIGSERIAL PRIMARY KEY,
  org_id        TEXT NOT NULL DEFAULT 'alykaly',
  actor_id      UUID,
  actor_email   TEXT,
  table_schema  TEXT NOT NULL,
  table_name    TEXT NOT NULL,
  row_id        TEXT,
  action        TEXT NOT NULL,
  changes       JSONB,
  ip_address    INET,
  user_agent    TEXT,
  occurred_at   TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX audit_log_table_time_idx ON audit.log(table_schema, table_name, occurred_at DESC);
CREATE INDEX audit_log_actor_idx      ON audit.log(actor_id) WHERE actor_id IS NOT NULL;
CREATE INDEX audit_log_action_idx     ON audit.log(action) WHERE action IN ('DELETE','SOFT_DELETE');

COMMENT ON TABLE audit.log IS 'Append-only audit trail of sensitive mutations';

-- ===== Generic audit trigger function =====
CREATE OR REPLACE FUNCTION audit.record_change()
RETURNS TRIGGER AS $$
DECLARE
  changes_jsonb JSONB;
  actor_email_val TEXT;
BEGIN
  IF TG_OP = 'INSERT' THEN
    changes_jsonb := jsonb_build_object('after', to_jsonb(NEW));
  ELSIF TG_OP = 'UPDATE' THEN
    changes_jsonb := jsonb_build_object('before', to_jsonb(OLD), 'after', to_jsonb(NEW));
  ELSIF TG_OP = 'DELETE' THEN
    changes_jsonb := jsonb_build_object('before', to_jsonb(OLD));
  END IF;

  SELECT email INTO actor_email_val FROM identity.profiles WHERE user_id = auth.uid();

  INSERT INTO audit.log (actor_id, actor_email, table_schema, table_name, row_id, action, changes)
  VALUES (
    auth.uid(),
    actor_email_val,
    TG_TABLE_SCHEMA, TG_TABLE_NAME,
    COALESCE((NEW).id::TEXT, (OLD).id::TEXT),
    TG_OP, changes_jsonb
  );
  RETURN COALESCE(NEW, OLD);
END;
$$ LANGUAGE plpgsql SECURITY DEFINER SET search_path = audit, identity, public;

-- Apply audit trigger to sensitive tables
CREATE TRIGGER audit_cases
  AFTER INSERT OR UPDATE OR DELETE ON app.cases
  FOR EACH ROW EXECUTE FUNCTION audit.record_change();

CREATE TRIGGER audit_transactions
  AFTER INSERT OR UPDATE OR DELETE ON app.transactions
  FOR EACH ROW EXECUTE FUNCTION audit.record_change();

CREATE TRIGGER audit_documents
  AFTER INSERT OR UPDATE OR DELETE ON crm.documents
  FOR EACH ROW EXECUTE FUNCTION audit.record_change();

CREATE TRIGGER audit_profiles
  AFTER UPDATE ON identity.profiles
  FOR EACH ROW EXECUTE FUNCTION audit.record_change();
