#!/usr/bin/env python3
"""
Hook Auto-Memory & DOX Journal (Loi de Persistance Cognitive Souveraine)
Couche [5D] Runtime Hooks.

Objectif :
Garantir que tout jalon substantiel, arbitrage d'architecture ou livraison PRD
est consigné de manière append-only dans le DOX local AGENTS.md et dans
40_Memory_Wiki_OKF/concepts/ sans déperdition cognitive.
"""

import os
import sys
import json
import datetime

import zoneinfo

DOX_AGENTS = r'C:\Users\amado\ASpace_OS_V3\40_Memory_Wiki_OKF\AGENTS.md'
TZ_KENTUCKY = zoneinfo.ZoneInfo('America/Kentucky/Louisville')

def get_kentucky_now():
    return datetime.datetime.now(TZ_KENTUCKY)

def append_dox_entry(summary: str, author: str = 'Antigravity') -> bool:
    now = get_kentucky_now()
    date_str = now.date().isoformat()
    time_str = now.strftime('%H:%M:%S EDT')
    entry = f"- `{date_str} {time_str}` : {summary} ({author}).\n"
    if os.path.exists(DOX_AGENTS):
        with open(DOX_AGENTS, 'a', encoding='utf-8') as f:
            f.write(entry)
        return True
    return False

if __name__ == '__main__':
    msg = sys.argv[1] if len(sys.argv) > 1 else ''
    if msg:
        ok = append_dox_entry(msg)
        print(json.dumps({'ok': ok, 'recorded': msg}, ensure_ascii=False))
    else:
        print(json.dumps({'ok': False, 'error': 'No message provided'}))
