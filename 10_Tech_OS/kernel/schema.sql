-- Noyau A'Space V3 — constructeur universel
-- Loi L0 : un systeme qui ne sait pas se repliquer est un document.
-- Von Neumann : ruban (tape) + constructeur + copieur + controleur.

PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;
PRAGMA busy_timeout = 5000;

-- ---------------------------------------------------------------- RUBAN (phi)
-- La description. Utilisee de deux facons : interpretee par le constructeur,
-- copiee en aveugle par le copieur. C'est cette dualite qui casse la regression.
CREATE TABLE IF NOT EXISTS tape (
  id          INTEGER PRIMARY KEY,
  path        TEXT    NOT NULL UNIQUE,
  sha256      TEXT    NOT NULL,
  created_at  TEXT    NOT NULL DEFAULT (datetime('now'))
);

-- ------------------------------------------------------------------- TRAVAIL
-- Un agent n'est pas un dossier : c'est un item qui traverse des etats.
CREATE TABLE IF NOT EXISTS work (
  id          INTEGER PRIMARY KEY,
  tape_id     INTEGER REFERENCES tape(id),
  layer       TEXT    NOT NULL CHECK (layer IN ('A0','L0','L1','L2')),
  title       TEXT    NOT NULL,
  status      TEXT    NOT NULL DEFAULT 'pending'
              CHECK (status IN ('pending','claimed','review','done','failed','blocked','waiting')),
  wake_at     TEXT,
  priority    INTEGER NOT NULL DEFAULT 0,
  parent_id   INTEGER REFERENCES work(id),   -- descendance : qui a engendre qui
  attempts    INTEGER NOT NULL DEFAULT 0,
  created_at  TEXT    NOT NULL DEFAULT (datetime('now')),
  updated_at  TEXT    NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS work_ready ON work(status, layer, priority DESC, id);

-- --------------------------------------------------------------------- BAIL
-- Un agent qui meurt rend son travail tout seul. Sans ca, une panne bloque
-- une branche pour toujours et l'operateur redevient le superviseur.
CREATE TABLE IF NOT EXISTS claim (
  work_id     INTEGER PRIMARY KEY REFERENCES work(id) ON DELETE CASCADE,
  harness     TEXT    NOT NULL,
  claimed_at  TEXT    NOT NULL DEFAULT (datetime('now')),
  expires_at  TEXT    NOT NULL,
  institutional_owner TEXT,
  runtime_id TEXT
);

-- --------------------------------------------------------------- PREDICTION
-- Ecrite AVANT l'execution, scoree apres. Une prediction posterieure a l'acte
-- n'est pas une verification, c'est une justification.
CREATE TABLE IF NOT EXISTS prediction (
  id            INTEGER PRIMARY KEY,
  work_id       INTEGER NOT NULL REFERENCES work(id) ON DELETE CASCADE,
  claim_text    TEXT    NOT NULL,
  confidence    REAL    NOT NULL CHECK (confidence > 0.0 AND confidence < 1.0),
  predicted_at  TEXT    NOT NULL DEFAULT (datetime('now')),
  outcome       INTEGER CHECK (outcome IN (0,1)),
  scored_at     TEXT
);

-- ------------------------------------------------------------------- TRACES
CREATE TABLE IF NOT EXISTS event (
  id       INTEGER PRIMARY KEY,
  work_id  INTEGER REFERENCES work(id) ON DELETE CASCADE,
  harness  TEXT,
  kind     TEXT NOT NULL,
  payload  TEXT,
  at       TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS event_work ON event(work_id, id);

-- ================================================== BRIOCHES ANTIGRAVITY (ADR-0007)
-- Ces regles sont tenues par la base, pas par la discipline de l'agent.

-- Loi de prediction : rien n'atteint 'review' ou 'done' sans prediction prealable.
CREATE TRIGGER IF NOT EXISTS loi_prediction_prealable
BEFORE UPDATE OF status ON work
WHEN NEW.status IN ('review','done')
 AND NOT EXISTS (SELECT 1 FROM prediction WHERE work_id = NEW.id)
BEGIN
  SELECT RAISE(ABORT, 'loi_prediction: aucune prediction enregistree avant execution');
END;

-- Loi de detachement : on ne detache (done) que depuis 'review'.
-- La descendance est laches parce qu'elle a prouve, pas parce qu'on l'espere.
CREATE TRIGGER IF NOT EXISTS loi_detachement
BEFORE UPDATE OF status ON work
WHEN NEW.status = 'done' AND OLD.status <> 'review'
BEGIN
  SELECT RAISE(ABORT, 'loi_detachement: done exige un passage par review');
END;

-- Horodatage automatique.
CREATE TRIGGER IF NOT EXISTS touch_work
AFTER UPDATE ON work
BEGIN
  UPDATE work SET updated_at = datetime('now') WHERE id = NEW.id;
END;

-- --------------------------------------------------------------------- VUES
CREATE VIEW IF NOT EXISTS v_ready AS
  SELECT w.* FROM work w
  WHERE w.status = 'pending'
  ORDER BY w.priority DESC, w.id;

CREATE VIEW IF NOT EXISTS v_calibration AS
  SELECT round(confidence, 1) AS bucket,
         count(*)             AS n,
         avg(outcome)         AS taux_reel
  FROM prediction WHERE outcome IS NOT NULL
  GROUP BY bucket ORDER BY bucket;

-- ================================================== BRIOCHES ANTIGRAVITY (ADR-0007)
-- Prompt-as-Code : blueprints compiles par nardole_assembler.py. SQLite local,
-- zero dependance Supabase.
CREATE TABLE IF NOT EXISTS prompt_blueprints (
  id                TEXT PRIMARY KEY,        -- UUID
  slug              TEXT NOT NULL UNIQUE,
  layer             TEXT NOT NULL CHECK (layer IN ('A0','L0','L1','L2')),
  target_role       TEXT NOT NULL,
  template_body     TEXT NOT NULL,
  max_token_ceiling INTEGER NOT NULL DEFAULT 2048,
  version           INTEGER NOT NULL DEFAULT 1,
  sha256            TEXT NOT NULL
);

-- Regles de domaine B2.
CREATE TABLE IF NOT EXISTS domain_rules_b2 (
  id         TEXT PRIMARY KEY,               -- UUID
  domain     TEXT NOT NULL,
  rule       TEXT NOT NULL,
  severity   TEXT NOT NULL DEFAULT 'soft' CHECK (severity IN ('soft','hard')),
  active     INTEGER NOT NULL DEFAULT 1,
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- WorkGraph / Intent / Goal state reconstructed from the live canonical uc.db.
-- These definitions must stay compatible with uc_workgraph.py; a clean clone must
-- not depend on untracked local migration files to initialize the Kernel.

CREATE TABLE IF NOT EXISTS intent (
  id              INTEGER PRIMARY KEY,
  intent_key      TEXT NOT NULL UNIQUE,
  title           TEXT NOT NULL,
  layer           TEXT CHECK (layer IN ('A0','L0','L1','L2')),
  status          TEXT NOT NULL DEFAULT 'draft'
                  CHECK (status IN ('draft','frozen','active','done','cancelled')),
  source_path     TEXT,
  verbatim_sha256 TEXT,
  intent_ir       TEXT,
  created_at      TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at      TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS work_intent (
  work_id   INTEGER PRIMARY KEY REFERENCES work(id) ON DELETE CASCADE,
  intent_id INTEGER NOT NULL REFERENCES intent(id) ON DELETE RESTRICT,
  relation  TEXT NOT NULL DEFAULT 'implements'
);

CREATE TABLE IF NOT EXISTS work_dependency (
  work_id       INTEGER NOT NULL REFERENCES work(id) ON DELETE CASCADE,
  depends_on_id INTEGER NOT NULL REFERENCES work(id) ON DELETE CASCADE,
  kind          TEXT NOT NULL DEFAULT 'blocks'
                CHECK (kind IN ('blocks','requires','informs')),
  created_at    TEXT NOT NULL DEFAULT (datetime('now')),
  PRIMARY KEY (work_id, depends_on_id),
  CHECK (work_id <> depends_on_id)
);

CREATE TABLE IF NOT EXISTS session_binding (
  id           INTEGER PRIMARY KEY,
  work_id      INTEGER NOT NULL REFERENCES work(id) ON DELETE CASCADE,
  session_key  TEXT NOT NULL UNIQUE,
  harness      TEXT NOT NULL,
  capability   TEXT,
  external_ref TEXT,
  status       TEXT NOT NULL DEFAULT 'active'
               CHECK (status IN ('active','idle','closed','failed')),
  started_at   TEXT NOT NULL DEFAULT (datetime('now')),
  ended_at     TEXT
);

CREATE TABLE IF NOT EXISTS harness_capability (
  id             INTEGER PRIMARY KEY,
  harness        TEXT NOT NULL,
  capability     TEXT NOT NULL CHECK (capability IN (
    'START','AUTH','MODEL_DISCOVERY','STREAM','STEER','INTERRUPT',
    'RESUME','SANDBOX','FAILURE_SIGNAL','RECOVER'
  )),
  evidence_level TEXT NOT NULL CHECK (evidence_level IN (
    'DECLARED','DOCUMENTED','SYNTHETIC','NATIVE','CANARY'
  )),
  status         TEXT NOT NULL DEFAULT 'unknown'
                 CHECK (status IN ('unknown','pass','fail','degraded')),
  evidence_ref   TEXT,
  checked_at     TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE(harness, capability)
);

CREATE TABLE IF NOT EXISTS artifact (
  id                  INTEGER PRIMARY KEY,
  work_id             INTEGER NOT NULL REFERENCES work(id) ON DELETE CASCADE,
  kind                TEXT NOT NULL,
  uri                 TEXT NOT NULL,
  sha256              TEXT,
  producer_session_id INTEGER REFERENCES session_binding(id) ON DELETE SET NULL,
  created_at          TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE(work_id, kind, uri)
);

CREATE TABLE IF NOT EXISTS gate_decision (
  id                INTEGER PRIMARY KEY,
  work_id           INTEGER NOT NULL REFERENCES work(id) ON DELETE CASCADE,
  gate              TEXT NOT NULL,
  verdict           TEXT NOT NULL CHECK (verdict IN ('pass','fail','veto','waive')),
  reason            TEXT,
  evidence_event_id INTEGER REFERENCES event(id) ON DELETE SET NULL,
  decided_by        TEXT,
  decided_at        TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS goal (
  id               INTEGER PRIMARY KEY,
  intent_id        INTEGER REFERENCES intent(id) ON DELETE SET NULL,
  goal_key         TEXT NOT NULL UNIQUE,
  title            TEXT NOT NULL,
  success_criteria TEXT NOT NULL DEFAULT '[]',
  status           TEXT NOT NULL DEFAULT 'active'
                   CHECK (status IN ('active','waiting','done','abandoned')),
  created_at       TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at       TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS goal_round (
  id             INTEGER PRIMARY KEY,
  goal_id        INTEGER NOT NULL REFERENCES goal(id) ON DELETE CASCADE,
  round_no       INTEGER NOT NULL,
  status         TEXT NOT NULL DEFAULT 'planned'
                 CHECK (status IN ('planned','active','review','closed')),
  review_verdict TEXT CHECK (review_verdict IN ('done','wait','abandon','next_round')),
  review_reason  TEXT,
  created_at     TEXT NOT NULL DEFAULT (datetime('now')),
  reviewed_at    TEXT,
  UNIQUE(goal_id, round_no)
);

CREATE TABLE IF NOT EXISTS round_work (
  round_id INTEGER NOT NULL REFERENCES goal_round(id) ON DELETE CASCADE,
  work_id  INTEGER NOT NULL REFERENCES work(id) ON DELETE CASCADE,
  PRIMARY KEY(round_id, work_id)
);

CREATE TABLE IF NOT EXISTS work_wait (
  work_id        INTEGER PRIMARY KEY REFERENCES work(id) ON DELETE CASCADE,
  condition_text TEXT NOT NULL,
  wake_at        TEXT,
  reason         TEXT,
  created_at     TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE VIEW IF NOT EXISTS v_workgraph_v1 AS
SELECT
  w.id AS work_id, w.title, w.layer, w.status, w.parent_id, w.attempts,
  wi.intent_id, i.intent_key, i.status AS intent_status,
  c.harness AS claimed_by, c.expires_at AS lease_expires_at
FROM work w
LEFT JOIN work_intent wi ON wi.work_id = w.id
LEFT JOIN intent i ON i.id = wi.intent_id
LEFT JOIN claim c ON c.work_id = w.id;

-- Personas B3.
CREATE TABLE IF NOT EXISTS marvel_personas_b3 (
  id         TEXT PRIMARY KEY,               -- UUID
  codename   TEXT NOT NULL UNIQUE,
  role       TEXT NOT NULL,
  persona    TEXT NOT NULL,
  active     INTEGER NOT NULL DEFAULT 1,
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- ================================================== WARGAME CONTINUATION PROTOCOL (#321)
-- Stores parent Wargame state for prompt-independent continuation.
CREATE TABLE IF NOT EXISTS wargame (
  github_issue INTEGER PRIMARY KEY,
  work_id INTEGER REFERENCES work(id) ON DELETE SET NULL,
  state TEXT NOT NULL DEFAULT 'OPEN' CHECK (state IN ('OPEN', 'CLOSED')),
  current_round INTEGER NOT NULL DEFAULT 1,
  hypothesis TEXT,
  falsification_conditions TEXT,
  last_verified_effect TEXT,
  next_gate TEXT,
  owner_level TEXT,
  return_to TEXT,
  stale_after TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Stores bounded executable children for Wargames.
CREATE TABLE IF NOT EXISTS wargame_child (
  id INTEGER PRIMARY KEY,
  parent_issue INTEGER NOT NULL REFERENCES wargame(github_issue) ON DELETE CASCADE,
  work_id INTEGER REFERENCES work(id) ON DELETE SET NULL,
  claim_prediction TEXT,
  institutional_owner TEXT,
  capability TEXT,
  runtime_binding TEXT,
  evidence_sink TEXT,
  deterministic_gates TEXT,
  receipt TEXT,
  return_to TEXT,
  status TEXT NOT NULL DEFAULT 'ACTIVE' CHECK (status IN ('ACTIVE', 'CLOSED')),
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);
