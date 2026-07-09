-- ============================================================================
-- Alykaly OS — Seed data (dev + smoke tests)
-- Run automatically by `supabase db reset`
-- ============================================================================

-- ===== Agents (matches People.tsx Roster) =====
INSERT INTO ops.agents (slug, display_name, kind, description, endpoint) VALUES
  ('jerry-n8n',      'Jerry',         'synthetic', 'Orchestrateur N8N (Airtable, DocuSign, Supabase)', 'https://n8n.kalybana.com/webhook/jerry'),
  ('docusign-bot',   'DocuSign Bot',  'webhook',   'Réception callbacks DocuSign',                     NULL),
  ('case-sourcer',   'Case Sourcer',  'cron',      'Scan PACER quotidien pour nouveaux cases',         NULL),
  ('audit-keeper',   'Audit Keeper',  'cron',      'Distillation logs heartbeat L2 + rotation',        NULL)
ON CONFLICT (org_id, slug) DO NOTHING;

-- ===== Knowledge docs (call script + FAQ) =====
INSERT INTO app.knowledge_docs (category, title, body_md, tags, clearance_required) VALUES
  ('call-script', 'Bana — Audit Cold Call FR',
    E'Bonjour [Nom], c''est [Votre Prénom] du service d''audit de Alykaly. ' ||
    E'Je vous contacte concernant le Case #[NUMERO] dans lequel vous êtes mentionné comme [RÔLE].\n\n' ||
    E'Nous avons identifié un potentiel surplus de [MONTANT] qui pourrait vous revenir. ' ||
    E'L''audit est gratuit et sans engagement. Avez-vous 2 minutes pour en discuter ?',
    ARRAY['cold-call','bana','french'],
    'level_0_public'
  ),
  ('faq', 'Qu''est-ce qu''un Surplus Fund ?',
    E'Un surplus fund est le montant restant après la vente forcée d''un bien immobilier ' ||
    E'aux enchères judiciaires, lorsque le prix de vente dépasse les dettes garanties. ' ||
    E'Ces fonds reviennent légalement aux anciens propriétaires ou héritiers.',
    ARRAY['faq','surplus','definition'],
    'level_0_public'
  ),
  ('procedure', 'Process DocuSign cession',
    E'1. Préparer envelope avec Affidavit of Heirship + Power of Attorney\n' ||
    E'2. Envoyer via DocuSign API (webhook callback configuré)\n' ||
    E'3. Suivre signature dans Sales Sanctum kanban\n' ||
    E'4. Une fois signed → Legal kanban (court filing)',
    ARRAY['procedure','docusign','legal'],
    'level_1_internal'
  )
ON CONFLICT DO NOTHING;

-- ===== Sample cohort (Growth) =====
INSERT INTO crm.cohorts (name, source, acquisition_cost, lifetime_value, started_at) VALUES
  ('Bana Landing — Q1 2026',  'organic-landing', 0,    8500.00, '2026-01-01'),
  ('Facebook Ads — Spring',   'facebook-ads',    340,  12200.00, '2026-03-15')
ON CONFLICT DO NOTHING;

-- ===== Sample cases (Docket — dev only) =====
-- Note: assigned_to NULL for now (will be filled after first user signup)
INSERT INTO app.cases (case_number, defendant, amount, priority, status, confidence_score, court_jurisdiction, sourced_from) VALUES
  ('A 2403702', 'Estate of Robert Chase', 29531.00, 'genealogie', 'new',      0, 'TX-Harris',   'PACER'),
  ('B 1984221', 'Apex Industrial LLC',    14200.50, 'b2b',        'ready',    5, 'TX-Dallas',   'PACER'),
  ('C 8829103', 'Sarah Jenkins',           8450.00, 'expulsion',  'tracking', 2, 'TX-Travis',   'manual'),
  ('A 2401198', 'Michael T. Vance',       41200.00, 'genealogie', 'ready',    4, 'TX-Bexar',    'partner-acme'),
  ('D 3302911', 'Horizon Realty Trust',  112000.00, 'b2b',        'new',      0, 'TX-Tarrant',  'PACER')
ON CONFLICT (org_id, case_number) DO NOTHING;

-- ===== Sample transactions =====
INSERT INTO app.transactions (case_id, tx_type, amount, tx_date, status, description)
SELECT
  (SELECT id FROM app.cases WHERE case_number = 'A 2403702'),
  'inflow', 8450.00, '2026-05-18', 'completed', 'Commission cession'
WHERE EXISTS (SELECT 1 FROM app.cases WHERE case_number = 'A 2403702')
ON CONFLICT DO NOTHING;

INSERT INTO app.transactions (case_id, tx_type, amount, tx_date, status, description)
SELECT
  (SELECT id FROM app.cases WHERE case_number = 'B 1984221'),
  'outflow', 1500.00, '2026-05-16', 'completed', 'Avocat Probate'
WHERE EXISTS (SELECT 1 FROM app.cases WHERE case_number = 'B 1984221')
ON CONFLICT DO NOTHING;

-- ===== Sample sales pipeline (Sales Sanctum) =====
INSERT INTO crm.sales_pipeline_items (case_id, stage, views_count)
SELECT id, 'audit'::crm.sales_stage, 0 FROM app.cases WHERE case_number = 'A 2403702'
ON CONFLICT (case_id) DO NOTHING;

INSERT INTO crm.sales_pipeline_items (case_id, stage, views_count)
SELECT id, 'sent'::crm.sales_stage, 0 FROM app.cases WHERE case_number = 'B 1984221'
ON CONFLICT (case_id) DO NOTHING;

INSERT INTO crm.sales_pipeline_items (case_id, stage, views_count)
SELECT id, 'opened'::crm.sales_stage, 3 FROM app.cases WHERE case_number = 'C 8829103'
ON CONFLICT (case_id) DO NOTHING;

INSERT INTO crm.sales_pipeline_items (case_id, stage, views_count)
SELECT id, 'signed'::crm.sales_stage, 5 FROM app.cases WHERE case_number = 'A 2401198'
ON CONFLICT (case_id) DO NOTHING;

-- ===== Sample court filings (Legal) =====
INSERT INTO crm.court_filings (case_id, stage, delay_days)
SELECT id, 'ready'::crm.court_stage, 2 FROM app.cases WHERE case_number = 'A 2401198'
ON CONFLICT (case_id) DO NOTHING;

INSERT INTO crm.court_filings (case_id, stage, filed_at)
SELECT id, 'filed'::crm.court_stage, '2026-05-12'::DATE FROM app.cases WHERE case_number = 'B 1984221'
ON CONFLICT (case_id) DO NOTHING;

INSERT INTO crm.court_filings (case_id, stage, hearing_at)
SELECT id, 'hearing'::crm.court_stage, '2026-05-24T10:00:00Z'::TIMESTAMPTZ FROM app.cases WHERE case_number = 'C 8829103'
ON CONFLICT (case_id) DO NOTHING;

-- ===== Sample wind_direction alerts =====
INSERT INTO ops.wind_direction_alerts (severity, title, description, case_id) VALUES
  ('critical', 'Motion to Disburse rejetée',  'Besoin de Probate pour Case #A 2403702',
    (SELECT id FROM app.cases WHERE case_number = 'A 2403702')),
  ('warning',  'Acompte de 10% à virer',      'Délai restant : 10 jours ouvrables',
    (SELECT id FROM app.cases WHERE case_number = 'D 3302911')),
  ('info',     'Signature DocuSign',          'Affidavit of Heirship signé par J. Doe',
    (SELECT id FROM app.cases WHERE case_number = 'A 2401198'))
ON CONFLICT DO NOTHING;

-- ===== Sample system_metrics =====
INSERT INTO ops.system_metrics (metric_key, numeric_value) VALUES
  ('sob.ytd_yield',        14.2),
  ('sob.global_exposure',  248192004.00),
  ('engine.latency_ms',    24)
ON CONFLICT DO NOTHING;
