#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Phase 2 fallback: oEmbed metadata fetcher.
When youtube-transcript-api is rate-limited, fall back to oEmbed for title/author verification.
Doctrine: D6 honest (transcript blocked) + D1 verify (oEmbed HTTP 200) + D3 (title is signal but not ground truth).
"""
import json
import os
import sys
import time
import requests

OUT_DIR = "C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/youtube_ingest_2026-06-15_Saru_LD02_watch_history"


def fetch_oembed(video_id):
    url = f'https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json'
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            return r.json(), 'ok'
        return None, f'status-{r.status_code}'
    except Exception as e:
        return None, f'error: {str(e)[:80]}'


def main(video_ids):
    results = {}
    for i, vid in enumerate(video_ids):
        meta, status = fetch_oembed(vid)
        if meta:
            results[vid] = {
                'title': meta.get('title', ''),
                'author': meta.get('author_name', ''),
                'status': 'ok',
            }
            print(f"[{i+1}/{len(video_ids)}] {vid} -> {meta.get('author_name','?')[:30]:30s} | {meta.get('title','')[:80]}")
        else:
            results[vid] = {'status': status, 'title': '', 'author': ''}
            print(f"[{i+1}/{len(video_ids)}] {vid} -> SKIPPED ({status})")
        time.sleep(0.3)

    out_path = os.path.join(OUT_DIR, "oembed_metadata.json")
    existing = {}
    if os.path.exists(out_path):
        with open(out_path, 'r', encoding='utf-8') as f:
            existing = json.load(f)
    existing.update(results)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    print(f"\nWrote {out_path} (total {len(existing)} entries)")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        # Read fetch_list.json
        path = os.path.join(OUT_DIR, "fetch_list.json")
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                fl = json.load(f)
            vids = [e['video_id'] for e in fl]
            main(vids)
        else:
            print("Usage: fetch_oembed.py <vid1> <vid2> ...")
