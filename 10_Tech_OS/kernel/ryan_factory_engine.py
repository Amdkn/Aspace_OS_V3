#!/usr/bin/env python3
import sys, os, sqlite3, json
from pathlib import Path

SSSF_ROOT = Path('C:/Users/amado/super-simple-software-factory').resolve()
SSSF_DB = SSSF_ROOT / 'adws' / 'adw_data' / 'sssf.db'

def get_health():
    exists = SSSF_DB.exists()
    if not exists:
        return {'ok': False, 'error': 'db not found'}
    conn = sqlite3.connect(str(SSSF_DB))
    c = conn.cursor()
    sessions = c.execute('SELECT count(*) FROM sessions').fetchone()[0]
    phases = c.execute('SELECT count(*) FROM phases').fetchone()[0]
    conn.close()
    return {'ok': True, 'db': str(SSSF_DB), 'sessions': sessions, 'phases': phases}

def get_sessions(limit=50):
    if not SSSF_DB.exists():
        return []
    conn = sqlite3.connect(str(SSSF_DB))
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM sessions ORDER BY started_at DESC LIMIT ?', (limit,))
    sessions = [dict(r) for r in c.fetchall()]
    c.execute('SELECT phase_id, adw_id, seq, name, kind, owner, description, status, started_at, ended_at, error FROM phases ORDER BY seq')
    phases = [dict(r) for r in c.fetchall()]
    conn.close()
    phase_map = {}
    for p in phases:
        phase_map.setdefault(p['adw_id'], []).append(p)
    for s in sessions:
        s['phases'] = phase_map.get(s['adw_id'], [])
        s['phase_count'] = len(s['phases'])
    return sessions

def get_session_detail(adw_id):
    if not SSSF_DB.exists():
        return None
    conn = sqlite3.connect(str(SSSF_DB))
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM sessions WHERE adw_id = ?', (adw_id,))
    session = c.fetchone()
    if not session:
        conn.close()
        return None
    c.execute('SELECT * FROM phases WHERE adw_id = ? ORDER BY seq', (adw_id,))
    phases = [dict(r) for r in c.fetchall()]
    c.execute('SELECT * FROM envelopes WHERE adw_id = ?', (adw_id,))
    envelopes = [dict(r) for r in c.fetchall()]
    c.execute('SELECT * FROM gate_results WHERE adw_id = ?', (adw_id,))
    gates = [dict(r) for r in c.fetchall()]
    c.execute('SELECT * FROM agent_sessions WHERE adw_id = ?', (adw_id,))
    agents = [dict(r) for r in c.fetchall()]
    conn.close()
    return {'session': dict(session), 'phases': phases, 'envelopes': envelopes, 'gates': gates, 'agents': agents, 'usage': {'read': 0, 'written': 0}}

def get_events(adw_id, limit=500):
    if not SSSF_DB.exists():
        return {'events': [], 'cursor': 0, 'has_more': False}
    conn = sqlite3.connect(str(SSSF_DB))
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT rowid, event_id, adw_id, phase_id, type, name, payload_json, tokens, started_at FROM events WHERE adw_id = ? ORDER BY rowid LIMIT ?', (adw_id, limit))
    events = [dict(r) for r in c.fetchall()]
    conn.close()
    return {'events': events, 'cursor': events[-1]['rowid'] if events else 0, 'has_more': False}

def archive_session(adw_id, archived=True):
    if not SSSF_DB.exists():
        return False
    conn = sqlite3.connect(str(SSSF_DB))
    c = conn.cursor()
    c.execute('UPDATE sessions SET archived = ? WHERE adw_id = ?', (1 if archived else 0, adw_id))
    conn.commit()
    affected = c.rowcount
    conn.close()
    return affected > 0

if __name__ == '__main__':
    action = sys.argv[1] if len(sys.argv) > 1 else 'sessions'
    if action == 'health':
        print(json.dumps(get_health()))
    elif action == 'sessions':
        print(json.dumps(get_sessions()))
    elif action == 'detail':
        adw_id = sys.argv[2] if len(sys.argv) > 2 else ''
        print(json.dumps(get_session_detail(adw_id)))
    elif action == 'events':
        adw_id = sys.argv[2] if len(sys.argv) > 2 else ''
        print(json.dumps(get_events(adw_id)))
    elif action == 'archive':
        adw_id = sys.argv[2] if len(sys.argv) > 2 else ''
        archived = sys.argv[3] != 'false' if len(sys.argv) > 3 else True
        print(json.dumps({'ok': archive_session(adw_id, archived)}))
    else:
        print(json.dumps({'ok': False, 'error': f'Unknown action: {action}'}))
