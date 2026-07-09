-- ============================================================================
-- Alykaly OS — Migration 003
-- Business core : clients, cases, transactions
-- ============================================================================

-- ===== CLIENTS =====
CREATE TABLE app.clients (
  id                 UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id             TEXT NOT NULL DEFAULT 'alykaly',
  name               TEXT NOT NULL,
  module             app.client_module NOT NULL,
  contact_email      TEXT,
  contact_phone      TEXT,
  notes              TEXT,
  status             TEXT,
  clearance_required identity.clearance_level NOT NULL DEFAULT 'level_1_internal',
  metadata           JSONB NOT NULL DEFAULT '{}'::JSONB,
  created_at         TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at         TIMESTAMPTZ NOT NULL DEFAULT now(),
  deleted_at         TIMESTAMPTZ
);

CREATE INDEX clients_org_idx        ON app.clients(org_id) WHERE deleted_at IS NULL;
CREATE INDEX clients_name_trgm_idx  ON app.clients USING gin(name gin_trgm_ops);
CREATE INDEX clients_module_idx     ON app.clients(module) WHERE deleted_at IS NULL;

COMMENT ON TABLE app.clients IS 'Entities we recover surplus funds for (Estate of X, LLCs, individuals)';

-- ===== CASES =====
CREATE TABLE app.cases (
  id                 UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id             TEXT NOT NULL DEFAULT 'alykaly',
  case_number        TEXT NOT NULL,
  defendant          TEXT NOT NULL,
  client_id          UUID REFERENCES app.clients(id) ON DELETE SET NULL,
  amount             NUMERIC(14,2) NOT NULL DEFAULT 0,
  priority           app.case_priority NOT NULL DEFAULT 'other',
  status             app.case_status NOT NULL DEFAULT 'new',
  confidence_score   INT NOT NULL DEFAULT 0 CHECK (confidence_score BETWEEN 0 AND 5),
  court_jurisdiction TEXT,
  sourced_from       TEXT,
  assigned_to        UUID REFERENCES identity.profiles(user_id) ON DELETE SET NULL,
  clearance_required identity.clearance_level NOT NULL DEFAULT 'level_1_internal',
  metadata           JSONB NOT NULL DEFAULT '{}'::JSONB,
  version            INT NOT NULL DEFAULT 1,
  created_at         TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at         TIMESTAMPTZ NOT NULL DEFAULT now(),
  deleted_at         TIMESTAMPTZ,
  UNIQUE (org_id, case_number)
);

CREATE INDEX cases_org_status_idx     ON app.cases(org_id, status) WHERE deleted_at IS NULL;
CREATE INDEX cases_priority_idx       ON app.cases(priority);
CREATE INDEX cases_assigned_idx       ON app.cases(assigned_to) WHERE deleted_at IS NULL;
CREATE INDEX cases_defendant_trgm_idx ON app.cases USING gin(defendant gin_trgm_ops);
CREATE INDEX cases_amount_idx         ON app.cases(amount DESC) WHERE deleted_at IS NULL;
CREATE INDEX cases_client_idx         ON app.cases(client_id) WHERE deleted_at IS NULL;

COMMENT ON TABLE app.cases IS 'Court cases sourced for surplus funds recovery';

-- ===== TRANSACTIONS =====
CREATE TABLE app.transactions (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id            TEXT NOT NULL DEFAULT 'alykaly',
  case_id           UUID NOT NULL REFERENCES app.cases(id) ON DELETE RESTRICT,
  tx_type           app.tx_type NOT NULL,
  amount            NUMERIC(14,2) NOT NULL,
  tx_date           DATE NOT NULL,
  status            app.tx_status NOT NULL DEFAULT 'pending',
  description       TEXT,
  external_ref      TEXT,
  created_by        UUID REFERENCES identity.profiles(user_id) ON DELETE SET NULL,
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  deleted_at        TIMESTAMPTZ
);

CREATE INDEX transactions_case_idx       ON app.transactions(case_id);
CREATE INDEX transactions_date_idx       ON app.transactions(tx_date DESC);
CREATE INDEX transactions_status_idx     ON app.transactions(status);
CREATE INDEX transactions_type_status_idx ON app.transactions(tx_type, status) WHERE deleted_at IS NULL;

COMMENT ON TABLE app.transactions IS 'Financial ledger (inflows/outflows) linked to cases';
