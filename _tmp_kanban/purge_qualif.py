import sqlite3, json, datetime
c = sqlite3.connect('10_Tech_OS/kernel/uc.db', timeout=10); c.row_factory = sqlite3.Row
now = datetime.datetime.now().isoformat(timespec='seconds')
# --- Purge doublons L1 30/31/32 : status failed -> blocked (doublon), trace event
for wid, motif in [
    (30, 'doublon L1: ruban duplique (tape_id NULL), ruban canonique tape 24 -> work 34 (done)'),
    (31, 'doublon L1: soumission triple du meme intent (tape 24) ; ruban canonique -> work 34 (done)'),
    (32, 'doublon L1: soumission triple du meme intent (tape 24) ; ruban canonique -> work 34 (done)'),
]:
    c.execute("UPDATE work SET status='blocked', updated_at=? WHERE id=? AND status='failed'", (now, wid))
    if c.total_changes:
        c.execute("INSERT INTO event(work_id, harness, kind, payload) VALUES (?,?,?,?)",
                  (wid, 'doctor11_review_l1/kanban-t_0dcaef64', 'purge_doublon', json.dumps({'motif': motif}, ensure_ascii=False)))
    print(wid, c.execute("select status from work where id=?", (wid,)).fetchone()[0])
c.commit()

# --- Qualification works morts 1/8/9 : deja failed, tracer la cause racine
qual = {
    1: 'landing OMK: work pre-historique (2026-08-02), sans ruban ni prediction; echec de la premiere generation L2. Cause: ruban incomplet (pre-canon). Verdict: mort definitive, non reanimable sans ruban.',
    8: 'pc:run-simule-0001 agent Nardole bloque: simulation de blocage Nardole, echec attendu de l epreuve DLQ. Verdict: mort definitive (epreuve passee), deja requalifie partiellement par work 29.',
    9: 'pc:run-simule-0002 agent Nardole bloque: idem 8. Verdict: mort definitive (epreuve passee).',
}
for wid, motif in qual.items():
    c.execute("INSERT INTO event(work_id, harness, kind, payload) VALUES (?,?,?,?)",
              (wid, 'doctor11_review_l1/kanban-t_0dcaef64', 'qualification_mort', json.dumps({'verdict': 'mort_definitive', 'motif': motif}, ensure_ascii=False)))
    print(wid, 'event qualification insere')
c.commit()
c.close()
print('OK')
