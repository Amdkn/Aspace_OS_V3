-- ============================================================================
-- Alykaly OS — Migration 005
-- Ops + Content : agents, agent_events, system_metrics, knowledge, cohorts, feed, intake, wind_direction
-- ============================================================================

-- ===== AGENTS (People = synthetic + human) =====
CREATE TABLE ops.agents (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id       TEXT NOT NULL DEFAULT 'alykaly',
  slug         TEXT NOT NULL,
  display_name TEXT NOT NULL,
  kind         ops.agent_kind NOT NULL,
  description  TEXT,
  endpoint     TEXT,
  is_active    BOOLEAN NOT NULL DEFAULT true,
  metadata     JSONB NOT NULL DEFAULT '{}'::JSONB,
  created_at   TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at   TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (org_id, slug)
);

CREATE INDEX agents_kind_active_idx ON ops.agents(kind, is_active);

COMMENT ON TABLE ops.agents IS 'Roster of synthetic + human + webhook + cron agents in the workforce';

-- ===== AGENT EVENTS =====
CREATE TABLE ops.agent_events (
  id         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  agent_id   UUID NOT NULL REFERENCES ops.agents(id) ON DELETE CASCADE,
  case_id    UUID REFERENCES app.cases(id) ON DELETE SET NULL,
  severity   ops.event_severity NOT NULL DEFAULT 'info',
  event_type TEXT NOT NULL,
  message    TEXT,
  payload    JSONB,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX agent_events_agent_idx    ON ops.agent_events(agent_id, created_at DESC);
CREATE INDEX agent_events_severity_idx ON ops.agent_events(severity) WHERE severity IN ('warning','critical');
CREATE INDEX agent_events_type_idx     ON ops.agent_events(event_type, created_at DESC);

-- ===== SYSTEM METRICS =====
CREATE TABLE ops.system_metrics (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  metric_key    TEXT NOT NULL,
  numeric_value NUMERIC(20,4),
  text_value    TEXT,
  metadata      JSONB,
  recorded_at   TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX system_metrics_key_time_idx ON ops.system_metrics(metric_key, recorded_at DESC);

COMMENT ON TABLE ops.system_metrics IS 'Time-series metrics for System Roots dashboard';

-- ===== WIND DIRECTION alerts =====
CREATE TABLE ops.wind_direction_alerts (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id          TEXT NOT NULL DEFAULT 'alykaly',
  severity        ops.event_severity NOT NULL,
  title           TEXT NOT NULL,
  description     TEXT,
  case_id         UUID REFERENCES app.cases(id) ON DELETE SET NULL,
  action_url      TEXT,
  acknowledged_at TIMESTAMPTZ,
  acknowledged_by UUID REFERENCES identity.profiles(user_id) ON DELETE SET NULL,
  created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX wind_unack_idx     ON ops.wind_direction_alerts(created_at DESC) WHERE acknowledged_at IS NULL;
CREATE INDEX wind_severity_idx  ON ops.wind_direction_alerts(severity) WHERE acknowledged_at IS NULL;

COMMENT ON TABLE ops.wind_direction_alerts IS 'Dashboard signals requiring attention';

-- ===== KNOWLEDGE (scripts d''appel, FAQ) =====
CREATE TABLE app.knowledge_docs (
  id                 UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id             TEXT NOT NULL DEFAULT 'alykaly',
  category           TEXT NOT NULL,
  title              TEXT NOT NULL,
  body_md            TEXT NOT NULL,
  tags               TEXT[] NOT NULL DEFAULT ARRAY[]::TEXT[],
  clearance_required identity.clearance_level NOT NULL DEFAULT 'level_0_public',
  author_id          UUID REFERENCES identity.profiles(user_id) ON DELETE SET NULL,
  version            INT NOT NULL DEFAULT 1,
  created_at         TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at         TIMESTAMPTZ NOT NULL DEFAULT now(),
  deleted_at         TIMESTAMPTZ
);

CREATE INDEX knowledge_category_idx ON app.knowledge_docs(category) WHERE deleted_at IS NULL;
CREATE INDEX knowledge_tags_idx     ON app.knowledge_docs USING gin(tags);
CREATE INDEX knowledge_title_trgm_idx ON app.knowledge_docs USING gin(title gin_trgm_ops);

COMMENT ON TABLE app.knowledge_docs IS 'Call scripts, FAQ, procedures (Knowledge module)';

-- ===== GROWTH : cohorts =====
CREATE TABLE crm.cohorts (
  id               UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id           TEXT NOT NULL DEFAULT 'alykaly',
  name             TEXT NOT NULL,
  source           TEXT,
  acquisition_cost NUMERIC(14,2),
  lifetime_value   NUMERIC(14,2),
  started_at       DATE,
  metadata         JSONB NOT NULL DEFAULT '{}'::JSONB,
  created_at       TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX cohorts_source_idx ON crm.cohorts(source);

-- ===== GROWTH : feed_events =====
CREATE TABLE crm.feed_events (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id      TEXT NOT NULL DEFAULT 'alykaly',
  cohort_id   UUID REFERENCES crm.cohorts(id) ON DELETE SET NULL,
  event_kind  TEXT NOT NULL,
  case_id     UUID REFERENCES app.cases(id) ON DELETE SET NULL,
  payload     JSONB,
  occurred_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX feed_events_time_idx       ON crm.feed_events(occurred_at DESC);
CREATE INDEX feed_events_cohort_idx     ON crm.feed_events(cohort_id, occurred_at DESC);
CREATE INDEX feed_events_event_kind_idx ON crm.feed_events(event_kind);

-- ===== INTAKE (Bana landing form) =====
CREATE TABLE app.intake_submissions (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id          TEXT NOT NULL DEFAULT 'alykaly',
  source          TEXT NOT NULL DEFAULT 'bana_intake',
  payload         JSONB NOT NULL,
  defender_email  TEXT,
  defender_phone  TEXT,
  routed_case_id  UUID REFERENCES app.cases(id) ON DELETE SET NULL,
  status          TEXT NOT NULL DEFAULT 'new',
  processed_by    UUID REFERENCES identity.profiles(user_id) ON DELETE SET NULL,
  created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
  processed_at    TIMESTAMPTZ
);

CREATE INDEX intake_status_idx       ON app.intake_submissions(status) WHERE status = 'new';
CREATE INDEX intake_created_idx      ON app.intake_submissions(created_at DESC);

COMMENT ON TABLE app.intake_submissions IS 'Public lead capture from Bana landing page';
