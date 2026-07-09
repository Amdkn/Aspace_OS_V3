#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Phase 2 transcript fetcher for Saru LD02 classifier.
Fetches transcripts for a prioritized list of video_ids and classifies each as
LD02_STRONG / LD02_TANGENT / NON-LD02 based on simple text heuristics.
Doctrine: D1 verify (each transcript fetched), D3 nuance, D6 honest on rate-limit.
"""
import json
import os
import sys
import re
import time
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled, NoTranscriptFound, VideoUnavailable,
    CouldNotRetrieveTranscript
)

OUT_DIR = "C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/youtube_ingest_2026-06-15_Saru_LD02_watch_history"
TRANSCRIPT_DIR = os.path.join(OUT_DIR, "transcripts")
os.makedirs(TRANSCRIPT_DIR, exist_ok=True)


def fetch_transcript(video_id, languages=('fr', 'en')):
    """Fetch transcript for a video_id, return text or None."""
    try:
        # Try API
        api = YouTubeTranscriptApi()
        transcript_list = api.list(video_id)
        # Pick the first available in desired languages
        transcript = None
        for lang in languages:
            try:
                transcript = transcript_list.find_manually_created_transcript([lang])
                break
            except Exception:
                pass
        if not transcript:
            for lang in languages:
                try:
                    transcript = transcript_list.find_generated_transcript([lang])
                    break
                except Exception:
                    pass
        if not transcript:
            # Last resort: any available
            for t in transcript_list:
                transcript = t
                break
        if not transcript:
            return None, "no-transcript-available"
        fetched = transcript.fetch()
        text = ' '.join([s.text for s in fetched])
        return text, "ok"
    except TranscriptsDisabled:
        return None, "transcripts-disabled"
    except NoTranscriptFound:
        return None, "no-transcript-found"
    except VideoUnavailable:
        return None, "video-unavailable"
    except CouldNotRetrieveTranscript as e:
        if 'TooManyRequests' in str(type(e)) or '429' in str(e):
            return None, "rate-limited"
        return None, f"could-not-retrieve: {str(e)[:80]}"
    except Exception as e:
        return None, f"error: {str(e)[:80]}"


# LD02 classification heuristic on transcript text
LD02_STRONG_TERMS = [
    'business model', 'pricing', 'revenue', 'mrr', 'arr', 'churn', 'ltv', 'cac',
    'cash flow', 'runway', 'salary', 'payroll', 'invest', 'investment', 'stock',
    'share', 'bourse', 'dividend', 'saas', 'pricing', 'margin', 'profit', 'loss',
    'budget', 'expense', 'cost', 'cost of', 'opex', 'capex', 'burn rate', 'burn',
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
    'bankrupt', 'faillite', 'liquidation', 'argent', 'money', 'pauvre', 'pauvreté',
    'million', 'millionaire', 'billion', 'wealth', 'richesse', 'fortune',
    'travail', 'travailleur', 'emploi', 'job', 'salarié', 'salarie', 'cdi', 'cdd'
]
LD02_TANGENT_TERMS = [
    'ai', 'ia ', 'intelligence artificielle', 'tech', 'startup', 'founder', 'fondateur',
    'product', 'marketing', 'growth', 'sales', 'career', 'carrière', 'carriere',
    'productivity', 'productivité', 'outil', 'tool', 'notion', 'chatgpt', 'claude',
    'openai', 'anthropic', 'gemini', 'gpt', 'llm', 'agent', 'automation',
    'codec', 'développeur', 'developer', 'engineer', 'ingénieur', 'ingenieur',
    'code', 'coding', 'programming', 'programmation'
]


def classify_ld02(transcript_text):
    """Return (label, score, hits) where label in {STRONG, TANGENT, NON-LD02, EMPTY}."""
    if not transcript_text or len(transcript_text) < 100:
        return ('EMPTY', 0, [])
    text = transcript_text.lower()
    strong_hits = []
    for term in LD02_STRONG_TERMS:
        if term in text:
            strong_hits.append(term)
    tangent_hits = []
    for term in LD02_TANGENT_TERMS:
        if term in text:
            tangent_hits.append(term)
    if len(strong_hits) >= 3:
        return ('STRONG', len(strong_hits), strong_hits[:10])
    elif len(strong_hits) >= 1 and len(strong_hits) >= len(tangent_hits):
        return ('TANGENT', len(strong_hits), strong_hits[:5])
    else:
        return ('NON-LD02', len(strong_hits), strong_hits[:3])


def main(video_ids=None):
    if video_ids is None:
        # Read from stdin or file
        if len(sys.argv) > 1:
            video_ids = sys.argv[1:]
        else:
            print("Usage: fetch_transcripts.py <vid1> <vid2> ...")
            return

    results = []
    for i, vid in enumerate(video_ids):
        print(f"[{i+1}/{len(video_ids)}] {vid} ...", end=' ', flush=True)
        text, status = fetch_transcript(vid)
        if text:
            # Save raw transcript
            tpath = os.path.join(TRANSCRIPT_DIR, f"{vid}.txt")
            with open(tpath, 'w', encoding='utf-8') as f:
                f.write(text)
            label, score, hits = classify_ld02(text)
            print(f"OK {len(text)} chars -> {label} (score={score})")
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
        time.sleep(0.5)  # Be polite

    # Save results
    out_path = os.path.join(OUT_DIR, "transcript_results.json")
    # Append to existing
    existing = []
    if os.path.exists(out_path):
        with open(out_path, 'r', encoding='utf-8') as f:
            existing = json.load(f)
    existing.extend(results)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    print(f"\nWrote {out_path} (total {len(existing)} entries)")


if __name__ == '__main__':
    main()
