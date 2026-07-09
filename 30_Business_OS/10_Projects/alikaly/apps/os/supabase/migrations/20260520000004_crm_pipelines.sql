-- ============================================================================
-- Alykaly OS — Migration 004
-- CRM : sales_pipeline_items, court_filings, documents
-- ============================================================================

-- ===== SALES SANCTUM (DocuSign workflow) =====
CREATE TABLE crm.sales_pipeline_items (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id          TEXT NOT NULL DEFAULT 'alykaly',
  case_id         UUID NOT NULL REFERENCES app.cases(id) ON DELETE CASCADE,
  stage           crm.sales_stage NOT NULL DEFAULT 'audit',
  envelope_id     TEXT,
  views_count     INT NOT NULL DEFAULT 0,
  last_event_at   TIMESTAMPTZ,
  metadata        JSONB NOT NULL DEFAULT '{}'::JSONB,
  created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (case_id)
);

CREATE INDEX sales_pipeline_org_stage_idx ON crm.sales_pipeline_items(org_id, stage);
CREATE INDEX sales_pipeline_envelope_idx  ON crm.sales_pipeline_items(envelope_id) WHERE envelope_id IS NOT NULL;

COMMENT ON TABLE crm.sales_pipeline_items IS 'DocuSign envelope tracking per case (audit→sent→opened→signed)';

-- ===== LEGAL kanban (Court workflow) =====
CREATE TABLE crm.court_filings (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id        TEXT NOT NULL DEFAULT 'alykaly',
  case_id       UUID NOT NULL REFERENCES app.cases(id) ON DELETE CASCADE,
  stage         crm.court_stage NOT NULL DEFAULT 'ready',
  filed_at      DATE,
  hearing_at    TIMESTAMPTZ,
  filed_amount  NUMERIC(14,2),
  delay_days    INT,
  metadata      JSONB NOT NULL DEFAULT '{}'::JSONB,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (case_id)
);

CREATE INDEX court_filings_org_stage_idx ON crm.court_filings(org_id, stage);
CREATE INDEX court_filings_hearing_idx   ON crm.court_filings(hearing_at) WHERE hearing_at IS NOT NULL;

COMMENT ON TABLE crm.court_filings IS 'Legal Kanban (ready→filed→hearing→signed→closed)';

-- ===== DOCUMENTS (Storage metadata) =====
CREATE TABLE crm.documents (
  id                 UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id             TEXT NOT NULL DEFAULT 'alykaly',
  case_id            UUID REFERENCES app.cases(id) ON DELETE SET NULL,
  client_id          UUID REFERENCES app.clients(id) ON DELETE SET NULL,
  bucket             TEXT NOT NULL,
  storage_path       TEXT NOT NULL,
  doc_type           TEXT NOT NULL,
  filename           TEXT NOT NULL,
  mime_type          TEXT,
  size_bytes         BIGINT,
  checksum_sha256    TEXT,
  uploaded_by        UUID REFERENCES identity.profiles(user_id) ON DELETE SET NULL,
  clearance_required identity.clearance_level NOT NULL DEFAULT 'level_1_internal',
  metadata           JSONB NOT NULL DEFAULT '{}'::JSONB,
  created_at         TIMESTAMPTZ NOT NULL DEFAULT now(),
  deleted_at         TIMESTAMPTZ,
  UNIQUE (bucket, storage_path)
);

CREATE INDEX documents_case_idx     ON crm.documents(case_id) WHERE deleted_at IS NULL;
CREATE INDEX documents_client_idx   ON crm.documents(client_id) WHERE deleted_at IS NULL;
CREATE INDEX documents_doc_type_idx ON crm.documents(doc_type);

COMMENT ON TABLE crm.documents IS 'Metadata for files stored in Supabase Storage buckets';
