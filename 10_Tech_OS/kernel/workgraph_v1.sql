-- Fichier complet
CREATE TABLE IF NOT EXISTS work_dependency (
  work_id INTEGER,
  depends_on_id INTEGER,
  kind TEXT
);
CREATE TABLE IF NOT EXISTS session_binding (
  work_id INTEGER,
  status TEXT,
  ended_at TEXT,
  harness TEXT,
  session_key TEXT,
  capability TEXT,
  external_ref TEXT
);
CREATE VIEW IF NOT EXISTS v_workgraph_v1 AS SELECT * FROM work;
