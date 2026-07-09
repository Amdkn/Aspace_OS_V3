#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Phase 1 parser for A0's YouTube watch history.
Reads watch-history.html (51 MB, ~42k entries) and produces:
  - parsed_watch_history.json (one entry per unique video_id, sorted DESC)
  - per_month_stats.json
  - top_channels.json
Doctrine: D1 verify-before-assert, D4 append-only, D6 root cause.
"""
import os
import re
import json
from datetime import datetime
from collections import Counter, defaultdict

INPUT = "YouTube et YouTube\xa0Music/historique/watch-history.html"
BASE = "C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/takeout-20260611T084246Z-3-001/Takeout"
OUT_DIR = "C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/youtube_ingest_2026-06-15_Saru_LD02_watch_history"

# Pattern for each content-cell that contains the watch info
# Format: <div class="content-cell ...mdl-typography--body-1">Vous avez regardé
#   <a href="...watch?v=VIDEO_ID">TITLE</a><br>
#   <a href="...channel/CHAN_ID">CHANNEL</a><br>
#   TIMESTAMP<br>
# </div>
CELL_RE = re.compile(
    r'<div class="content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1">\s*'
    r'Vous avez regard[^<]*<a href="https://www\.youtube\.com/watch\?v=([A-Za-z0-9_-]{11})">((?:(?!</a>).)*)</a><br>\s*'
    r'<a href="https://www\.youtube\.com/channel/([A-Za-z0-9_-]+)">((?:(?!</a>).)*)</a><br>\s*'
    r'((?:(?!<br>).)*)<br>\s*'
    r'</div>',
    re.DOTALL
)

# HTML entity decode for the most common ones
def decode_entities(s):
    return (s.replace('&#39;', "'")
             .replace('&quot;', '"')
             .replace('&amp;', '&')
             .replace('&lt;', '<')
             .replace('&gt;', '>')
             .replace('&nbsp;', ' ')
             .replace('&eacute;', 'é')
             .replace('&egrave;', 'è')
             .replace('&agrave;', 'à')
             .replace('&ecirc;', 'ê')
             .replace('&icirc;', 'î')
             .replace('&ocirc;', 'ô')
             .replace('&ucirc;', 'û')
             .replace('&ccedil;', 'ç')
             .replace('&Eacute;', 'É'))

# FR month names (full + abbreviated)
FR_MONTHS = {
    'janvier': 1, 'janv': 1, 'jan.': 1,
    'février': 2, 'févr': 2, 'fév.': 2, 'fevrier': 2, 'fevr': 2,
    'mars': 3, 'mar.': 3,
    'avril': 4, 'avr': 4, 'avr.': 4,
    'mai': 5,
    'juin': 6,
    'juillet': 7, 'juil': 7, 'juil.': 7,
    'août': 8, 'aout': 8,
    'septembre': 9, 'sept': 9, 'sept.': 9, 'sep': 9, 'sep.': 9,
    'octobre': 10, 'oct': 10, 'oct.': 10,
    'novembre': 11, 'nov': 11, 'nov.': 11,
    'décembre': 12, 'déc': 12, 'déc.': 12, 'decembre': 12, 'dec': 12
}

def parse_ts(ts_raw):
    """Parse '11 juin 2026, 03:53:15 EDT' or '30 avr. 2026, 20:25:45 EDT' to datetime."""
    ts = ts_raw.strip().replace('\xa0', ' ').replace('  ', ' ')
    # Remove trailing timezone
    m = re.match(r'(\d{1,2})\s+(\S+?)\.?\s+(\d{4}),?\s+(\d{1,2}):(\d{2}):(\d{2})\s*(\S*)', ts)
    if not m:
        return None
    d, mon_name, y, h, mn, s, _tz = m.groups()
    mon_name_norm = mon_name.lower().rstrip('.').strip()
    mon = FR_MONTHS.get(mon_name_norm, 0)
    if not mon:
        return None
    try:
        return datetime(int(y), mon, int(d), int(h), int(mn), int(s))
    except ValueError:
        return None


def main():
    in_path = os.path.join(BASE, INPUT)
    print(f"Reading {in_path} ({os.path.getsize(in_path)} bytes)...")
    with open(in_path, 'r', encoding='utf-8') as f:
        data = f.read()
    print(f"Loaded {len(data)} chars. Running regex...")

    # Dedupe by video_id, keep LATEST watch timestamp
    videos = {}  # video_id -> {title, channel, channel_id, last_watched, watch_count}
    parse_errors = 0
    for m in CELL_RE.finditer(data):
        vid, title, chan_id, chan, ts_raw = m.groups()
        ts = parse_ts(ts_raw)
        if not ts:
            parse_errors += 1
            continue
        vid = vid.strip()
        title = decode_entities(title).strip()
        chan = decode_entities(chan).strip()
        chan_id = chan_id.strip()
        if vid in videos:
            videos[vid]['watch_count'] += 1
            if ts > videos[vid]['last_watched']:
                videos[vid]['last_watched'] = ts
                videos[vid]['title'] = title
                videos[vid]['channel'] = chan
                videos[vid]['channel_id'] = chan_id
        else:
            videos[vid] = {
                'video_id': vid,
                'title': title,
                'channel': chan,
                'channel_id': chan_id,
                'last_watched': ts,
                'watch_count': 1,
            }

    print(f"Parsed {len(videos)} unique videos, {parse_errors} parse errors.")

    # Sort by last_watched DESC
    sorted_vids = sorted(videos.values(), key=lambda x: x['last_watched'], reverse=True)

    # Convert datetimes to ISO strings for JSON
    out_list = []
    for v in sorted_vids:
        out_list.append({
            'video_id': v['video_id'],
            'title': v['title'],
            'channel': v['channel'],
            'channel_id': v['channel_id'],
            'last_watched_iso': v['last_watched'].isoformat(),
            'last_watched_month': v['last_watched'].strftime('%Y-%m'),
            'watch_count': v['watch_count'],
        })

    # Stats
    month_counter = Counter()
    channel_counter = Counter()
    first_watch = None
    last_watch = None
    for v in sorted_vids:
        month_counter[v['last_watched'].strftime('%Y-%m')] += 1
        channel_counter[v['channel']] += 1
        if not first_watch or v['last_watched'] < first_watch:
            first_watch = v['last_watched']
        if not last_watch or v['last_watched'] > last_watch:
            last_watch = v['last_watched']

    # Write parsed_watch_history.json
    out_json = os.path.join(OUT_DIR, "parsed_watch_history.json")
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump({
            'total_unique': len(out_list),
            'total_watch_events': sum(v['watch_count'] for v in out_list),
            'first_watch': first_watch.isoformat() if first_watch else None,
            'last_watch': last_watch.isoformat() if last_watch else None,
            'parse_errors': parse_errors,
            'videos': out_list,
        }, f, ensure_ascii=False, indent=2)
    print(f"Wrote {out_json}")

    # Month stats
    per_month = sorted(month_counter.items(), reverse=True)
    stats = {
        'total_unique_videos': len(out_list),
        'first_watch': first_watch.isoformat() if first_watch else None,
        'last_watch': last_watch.isoformat() if last_watch else None,
        'per_month': per_month,
        'top_20_channels': channel_counter.most_common(20),
    }
    stats_path = os.path.join(OUT_DIR, "per_month_stats.json")
    with open(stats_path, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    print(f"Wrote {stats_path}")

    # Print summary
    print(f"\n=== D1 RECEIPT ===")
    print(f"Total unique videos: {len(out_list)}")
    print(f"First watch: {first_watch}")
    print(f"Last watch: {last_watch}")
    print(f"\nPer month (top 12):")
    for m, c in per_month[:12]:
        print(f"  {m}: {c}")
    print(f"\nTop 10 channels:")
    for ch, c in channel_counter.most_common(10):
        print(f"  {c:5d}  {ch}")


if __name__ == '__main__':
    main()
