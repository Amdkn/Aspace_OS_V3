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
              CHECK (status IN ('pending','claimed','review','done','failed','blocked')),
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
  expires_at  TEXT    NOT NULL
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

-- ============================================================== LOIS DUREES
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
