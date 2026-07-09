#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Phase 2 transcript fetcher v2 — direct YouTube page scraping.
youtube-transcript-api gets IP-blocked; we use requests to grab the watch page,
extract captionTracks JSON, then fetch the timedtext XML.
Doctrine: D1 verify, D3 nuance, D6 root cause (IP block workaround).
"""
import json
import os
import sys
import re
import time
import requests
import urllib.parse
import xml.etree.ElementTree as ET

OUT_DIR = "C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/youtube_ingest_2026-06-15_Saru_LD02_watch_history"
TRANSCRIPT_DIR = os.path.join(OUT_DIR, "transcripts")
os.makedirs(TRANSCRIPT_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}


def _absolutize_url(url: str) -> str:
    """YouTube sometimes returns relative /api/timedtext URLs; make them absolute."""
    if url.startswith('/api/'):
        return 'https://www.youtube.com' + url
    return url


def get_caption_url(video_id, prefer_langs=('fr', 'en')):
    """Fetch the YouTube watch page and extract captionTracks baseUrl.
    Returns list of (lang_code, base_url, name) tuples, ordered by preference.
    """
    url = f'https://www.youtube.com/watch?v={video_id}'
    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
    except Exception as e:
        return [], f'request-error: {str(e)[:80]}'
    if r.status_code != 200:
        return [], f'status-{r.status_code}'
    if 'unusual traffic' in r.text.lower() or 'ip was blocked' in r.text.lower():
        return [], 'ip-blocked'
    # Find captionTracks
    m = re.search(r'"captionTracks":\s*\[(.+?)\](?=,"audioTracks|"translationLanguages|"defaultAudioTrack)', r.text, re.DOTALL)
    if not m:
        return [], 'no-caption-tracks'
    blob = m.group(1)
    # Each track: {"baseUrl":"...","name":{...},"vssId":"...","languageCode":"...","kind":...}
    # Match flexible: baseUrl then any chars (incl. nested {}) up to languageCode
    tracks = re.findall(
        r'"baseUrl":"([^"]+)".{0,3000}?"languageCode":"([^"]+)"',
        blob,
        re.DOTALL
    )
    if not tracks:
        return [], 'no-tracks-parsed'
    return [(lang, _absolutize_url(urllib.parse.unquote(url)), lang) for url, lang in tracks], 'ok'


def fetch_caption(base_url: str):
    """Fetch caption XML and convert to plain text. Retry on 429."""
    for attempt in range(3):
        try:
            r = requests.get(base_url, headers=HEADERS, timeout=20)
        except Exception as e:
            if attempt == 2:
                return None, f'request-error: {str(e)[:80]}'
            time.sleep(2 ** attempt)
            continue
        if r.status_code == 200:
            try:
                root = ET.fromstring(r.content)
            except ET.ParseError:
                return None, 'xml-parse-error'
            texts = []
            for elem in root.iter('text'):
                if elem.text:
                    texts.append(elem.text)
            return ' '.join(texts), 'ok'
        elif r.status_code == 429:
            time.sleep(5 + 5 * attempt)  # back off
            continue
        else:
            return None, f'status-{r.status_code}'
    return None, 'rate-limited-after-retries'


def fetch_transcript_v2(video_id, prefer_langs=('fr', 'en')):
    """Returns (text, status)."""
    tracks, status = get_caption_url(video_id, prefer_langs)
    if not tracks:
        return None, status
    # Sort tracks by language preference
    def lang_priority(t):
        lang = t[2]
        if lang in prefer_langs:
            return prefer_langs.index(lang)
        return 100
    tracks_sorted = sorted(tracks, key=lang_priority)
    # Try each
    for lang, url, name in tracks_sorted:
        text, st = fetch_caption(url)
        if text and len(text) > 50:
            return text, f'ok-{lang}'
    return None, 'all-tracks-failed'


# LD02 classification heuristic (reuse from v1)
LD02_STRONG_TERMS = [
    'business model', 'pricing', 'revenue', 'mrr', 'arr', 'churn', 'ltv', 'cac',
    'cash flow', 'runway', 'salary', 'payroll', 'invest', 'investment', 'stock',
    'share', 'bourse', 'dividend', 'saas', 'margin', 'profit', 'loss',
    'budget', 'expense', 'opex', 'capex', 'burn rate', 'burn',
    'fundrai', 'valuation', 'ipo', 'exit', 'acquisition', 'acquired',
    'freelance', 'indie hacker', 'solopreneur', 'side hustle', 'passive income',
    'patrimoine', 'épargne', 'économies', 'retraite', 'pension', 'liberte',
    'liberté', 'fire', 'financial independence', 'retraite anticipée', 'frugal',
    'inflation', 'taux d\'intérêt', 'taux d\'interet', 'crédit immobilier',
    'hypothèque', 'emprunt', 'prêt bancaire', 'loan', 'dette', 'debt',
    'subscription', 'abonnement', 'churn', 'tarif', 'prix', 'sales', 'vente',
    'closing', 'contrat', 'facturation', 'billing', 'invoice', 'facture',
    'paiement', 'payment', 'tva', 'impôt', 'impot', 'fiscal', 'tax',
    'urssaf', 'auto-entrepreneur', 'sasu', 'eurl', 'sarl', 'micro-entreprise',
    'bankrupt', 'faillite', 'liquidation', 'argent', 'pauvre', 'pauvreté',
    'million', 'millionaire', 'billion', 'wealth', 'richesse', 'fortune',
    'travail', 'emploi', 'job', 'salarié', 'salarie', 'cdi', 'cdd', 'cout',
    'coût', 'revenu', 'revenus', 'banque', 'banquier', 'bourse', 'indie',
    'solopreneur', 'liberté', 'autonomie', 'flat tax', 'micro', 'fiscalité'
]


def classify_ld02(transcript_text):
    if not transcript_text or len(transcript_text) < 100:
        return ('EMPTY', 0, [])
    text = transcript_text.lower()
    strong_hits = []
    for term in LD02_STRONG_TERMS:
        if term in text:
            strong_hits.append(term)
    if len(strong_hits) >= 3:
        return ('STRONG', len(strong_hits), strong_hits[:10])
    elif len(strong_hits) >= 1:
        return ('TANGENT', len(strong_hits), strong_hits[:5])
    else:
        return ('NON-LD02', 0, [])


def main(video_ids=None):
    if video_ids is None:
        if len(sys.argv) > 1:
            video_ids = sys.argv[1:]
        else:
            print("Usage: fetch_transcripts_v2.py <vid1> <vid2> ...")
            return

    results = []
    for i, vid in enumerate(video_ids):
        print(f"[{i+1}/{len(video_ids)}] {vid} ...", end=' ', flush=True)
        text, status = fetch_transcript_v2(vid)
        if text:
            tpath = os.path.join(TRANSCRIPT_DIR, f"{vid}.txt")
            with open(tpath, 'w', encoding='utf-8') as f:
                f.write(text)
            label, score, hits = classify_ld02(text)
            print(f"OK {len(text)} chars -> {label} (score={score}) [{status}]")
            results.append({
                'video_id': vid, 'status': status, 'label': label,
                'score': score, 'hits': hits, 'chars': len(text),
                'transcript_path': tpath
            })
        else:
            print(f"SKIPPED ({status})")
            results.append({
                'video_id': vid, 'status': status, 'label': 'SKIPPED',
                'score': 0, 'hits': [], 'chars': 0, 'transcript_path': None
            })
        time.sleep(0.3)

    out_path = os.path.join(OUT_DIR, "transcript_results_v2.json")
    existing = []
    if os.path.exists(out_path):
        with open(out_path, 'r', encoding='utf-8') as f:
            existing = json.load(f)
    # Dedupe by video_id (latest wins)
    seen = {r['video_id']: r for r in existing}
    for r in results:
        seen[r['video_id']] = r
    final = list(seen.values())
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(final, f, ensure_ascii=False, indent=2)
    print(f"\nWrote {out_path} (total {len(final)} entries)")


if __name__ == '__main__':
    main()
