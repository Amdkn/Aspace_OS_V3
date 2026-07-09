#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Phase 2 LD02 classifier for YouTube watch history.
Takes parsed_watch_history.json, applies finance keyword filter on title+channel,
groups by month in REVERSE-chronological order (A0 law: 6→5→4→3→2→1→pre-2026),
outputs candidates.json with finance_density stats.
Doctrine: D1 verify, D3 nuance, D6 root cause, D11 Fable metric.
"""
import json
import os
import re
from collections import defaultdict, Counter
from datetime import datetime

OUT_DIR = "C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/youtube_ingest_2026-06-15_Saru_LD02_watch_history"
INPUT_JSON = os.path.join(OUT_DIR, "parsed_watch_history.json")

# Finance seed list (FR + EN) - per A0 brief
FINANCE_KEYWORDS = [
    'finance', 'budget', 'argent', 'money', 'revenu', 'income', 'mrr', 'saas',
    'pricing', 'coût', 'cout', 'cost', 'runway', 'trésorerie', 'tresorerie', 'cash',
    'investir', 'invest', 'bourse', 'stock', 'crypto', 'bitcoin', 'nft', 'business',
    'entrepreneur', 'indie', 'solopreneur', 'sob', 'autonomie', 'independence',
    'fire', 'frugal', 'épargne', 'epargne', 'savings', 'side hustle', 'dividend',
    'roi', 'marge', 'margin', 'profit', 'vente', 'sales', 'facturation', 'billing',
    'subscription', 'abonnement', 'banquier', 'banque', 'banq', 'prêt', 'pret', 'loan',
    'debt', 'dette', 'crédit', 'credit', 'hypothèque', 'hypotheque', 'inflation',
    'taux', 'interest', 'patrimoine', 'wealth', 'richesse', 'million', 'millionaire',
    'pauvre', 'pauvreté', 'pauvrete', 'broke', 'revenus', 'flat tax', 'impôt', 'impot',
    'fiscal', 'tax', 'tva', 'urssaf', 'auto-entrepreneur', 'auto entrepreneur', 'micro',
    'liberté', 'liberte', 'liberty', 'retraite', 'pension', 'rente', 'rendement',
    'investissement', 'wallet', 'portefeuille', 'boursier', 'boursière', 'capital',
    'levée', 'levee', 'fundraising', 'levée de fonds', 'pitch', 'valorisation', 'valuation',
    'startup', 'pme', 'tpe', 'indie hacker', 'indie-hacker', 'solopreneu', 'freelance',
    'indépendant', 'independant', 'tarif', 'tarifs', 'price', 'revenue', 'kpi financier'
]

# Word boundary regex builder
def build_kw_regex(kws):
    # Sort by length desc to match longer first
    kws_sorted = sorted(set(kws), key=lambda x: -len(x))
    escaped = [re.escape(k) for k in kws_sorted]
    # Use \b boundaries; some keywords contain accents/hyphens
    return re.compile(r'(?<![a-zA-Z0-9])(' + '|'.join(escaped) + r')', re.IGNORECASE)


KW_RE = build_kw_regex(FINANCE_KEYWORDS)


def is_finance_hit(title, channel):
    """Check if title or channel matches any finance keyword."""
    text = f"{title} {channel}"
    m = KW_RE.search(text)
    if m:
        return m.group(0)
    return None


def main():
    print("Loading parsed_watch_history.json...")
    with open(INPUT_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)
    videos = data['videos']
    print(f"Total videos: {len(videos)}")

    # Group by month
    by_month = defaultdict(list)
    for v in videos:
        month = v['last_watched_month']  # 'YYYY-MM'
        by_month[month].append(v)

    # Define month ordering per A0 law: 6→5→4→3→2→1→pre-2026
    # All months in 2026, then 2025 descending, then older
    def month_sort_key(m):
        # Parse 'YYYY-MM' to a sortable key, but we want 2026 first DESC, then 2025 DESC, then pre
        y, mo = m.split('-')
        y, mo = int(y), int(mo)
        if y == 2026:
            # 2026 should come first, ordered DESC by month
            return (0, y, -mo)
        elif y == 2025:
            # 2025 next
            return (1, y, -mo)
        else:
            # Pre-2026 last
            return (2, y, -mo)

    months_ordered = sorted(by_month.keys(), key=month_sort_key)
    print(f"Months ordered: {months_ordered}")

    # Per-month classifier
    results = {
        'months': {},
        'all_candidates': [],
        'overall': {
            'total_videos': len(videos),
            'total_finance_hits': 0,
            'top_finance_channels': Counter(),
            'top_finance_keywords': Counter(),
        }
    }

    for month in months_ordered:
        vids = by_month[month]
        candidates = []
        for v in vids:
            hit = is_finance_hit(v['title'], v['channel'])
            if hit:
                candidates.append({
                    'video_id': v['video_id'],
                    'title': v['title'],
                    'channel': v['channel'],
                    'channel_id': v['channel_id'],
                    'last_watched_iso': v['last_watched_iso'],
                    'watch_count': v['watch_count'],
                    'keyword_matched': hit,
                })
                results['overall']['total_finance_hits'] += 1
                results['overall']['top_finance_channels'][v['channel']] += 1
                results['overall']['top_finance_keywords'][hit.lower()] += 1
        # Sort candidates by last_watched DESC
        candidates.sort(key=lambda x: x['last_watched_iso'], reverse=True)

        # Calculate density
        density = (len(candidates) / len(vids) * 100) if vids else 0

        results['months'][month] = {
            'total_videos': len(vids),
            'finance_hits': len(candidates),
            'finance_density_pct': round(density, 2),
            'candidates': candidates,
        }
        results['all_candidates'].extend(candidates)
        print(f"  {month}: {len(vids)} total, {len(candidates)} finance hits ({density:.1f}%)")

    # Convert Counters to dicts
    results['overall']['top_finance_channels'] = dict(results['overall']['top_finance_channels'].most_common(30))
    results['overall']['top_finance_keywords'] = dict(results['overall']['top_finance_keywords'].most_common(30))

    # Save candidates.json
    out_path = os.path.join(OUT_DIR, "ld02_candidates.json")
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nWrote {out_path}")

    # Summary
    print(f"\n=== D11 FABLE METRIC ===")
    print(f"Total finance hits: {results['overall']['total_finance_hits']} / {len(videos)} = "
          f"{results['overall']['total_finance_hits']/len(videos)*100:.2f}%")
    print(f"Top 10 finance channels:")
    for ch, c in list(results['overall']['top_finance_channels'].items())[:10]:
        print(f"  {c:5d}  {ch}")
    print(f"Top 10 finance keywords matched:")
    for kw, c in list(results['overall']['top_finance_keywords'].items())[:10]:
        print(f"  {c:5d}  {kw}")


if __name__ == '__main__':
    main()
