#!/usr/bin/env python3
"""
extract_anchors.py — Extract discriminative anchors (5-grams) from pricing source.

D2 research FIRST doctrine : extract discriminative substrings from
pricing transcripts/docs before grepping CC sessions.

Usage:
    python extract_anchors.py --source transcript.txt --output anchors.json
    python extract_anchors.py --source transcript.txt --keywords "tizi teachizi 4000" --output anchors.json

D1 verify receipts: anchors are 5-grams with score = distinctiveness.
"""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path


def extract_5grams(text: str, min_score: float = 2.0):
    """Extract 5-grams with TF-IDF style scoring."""
    # Normalize whitespace
    text = re.sub(r"\s+", " ", text.lower().strip())
    words = text.split()

    # Generate 5-grams
    ngrams = []
    for i in range(len(words) - 4):
        gram = " ".join(words[i:i+5])
        ngrams.append(gram)

    # Score = frequency * (length factor)
    counter = Counter(ngrams)

    # Filter: keep only ngrams with score >= min_score
    scored = []
    for gram, freq in counter.most_common():
        # Score: frequency * (1 if contains number, else 0.5)
        has_number = bool(re.search(r"\d", gram))
        score = freq * (1.5 if has_number else 1.0)
        if score >= min_score:
            scored.append({
                "ngram": gram,
                "frequency": freq,
                "score": score,
                "has_number": has_number,
            })

    return scored


def extract_pricing_anchors(text: str):
    """Extract pricing-specific anchors (numbers + currency + period)."""
    pricing_patterns = [
        # $XXX/month or $XXX/mois
        r"\$\s?(\d+[,\.]?\d*)\s*(?:/mois|par mois|monthly|/mo|/m)",
        # $XXX/year or $XXX/an
        r"\$\s?(\d+[,\.]?\d*)\s*(?:/an|par an|annual|/y|/year)",
        # €XXX/month or €XXX/mois
        r"€\s?(\d+[,\.]?\d*)\s*(?:/mois|par mois|monthly|/mo|/m)",
        # €XXX/year
        r"€\s?(\d+[,\.]?\d*)\s*(?:/an|par an|annual|/y|/year)",
        # XXX€ direct
        r"(\d+)\s*€",
        # $XXX direct
        r"\$\s?(\d+[,\.]?\d*)",
    ]

    anchors = []
    for pat in pricing_patterns:
        matches = re.finditer(pat, text)
        for m in matches:
            anchors.append({
                "match": m.group(0),
                "context": text[max(0, m.start()-50):m.end()+50].strip(),
                "type": "pricing_amount",
            })

    return anchors


def extract_keywords_anchors(text: str, keywords: list):
    """Extract anchors around user-provided keywords."""
    text_lower = text.lower()
    anchors = []
    for kw in keywords:
        kw_lower = kw.lower()
        # Find all occurrences
        start = 0
        while True:
            idx = text_lower.find(kw_lower, start)
            if idx == -1:
                break
            # Extract 100-char context
            ctx_start = max(0, idx - 50)
            ctx_end = min(len(text), idx + len(kw_lower) + 100)
            context = text[ctx_start:ctx_end].strip()
            anchors.append({
                "keyword": kw,
                "context": context,
                "position": idx,
                "type": "user_keyword",
            })
            start = idx + 1

    return anchors


def main():
    parser = argparse.ArgumentParser(description="Extract discriminative anchors from pricing source")
    parser.add_argument("--source", required=True, help="Path to source text file (transcript, doc, etc.)")
    parser.add_argument("--keywords", default="", help="Comma-separated keywords to anchor on")
    parser.add_argument("--min-score", type=float, default=2.0, help="Minimum 5-gram score")
    parser.add_argument("--output", required=True, help="Output JSON file")
    args = parser.parse_args()

    # Read source
    source_path = Path(args.source)
    if not source_path.exists():
        print(f"ERROR: source not found: {args.source}", file=sys.stderr)
        sys.exit(1)

    text = source_path.read_text(encoding="utf-8", errors="ignore")

    # Extract anchors
    ngrams_5 = extract_5grams(text, args.min_score)
    pricing = extract_pricing_anchors(text)
    keywords_anchors = []
    if args.keywords:
        keywords = [k.strip() for k in args.keywords.split(",")]
        keywords_anchors = extract_keywords_anchors(text, keywords)

    output = {
        "source_file": str(source_path.absolute()),
        "text_length": len(text),
        "ngrams_5_count": len(ngrams_5),
        "pricing_anchors_count": len(pricing),
        "keywords_anchors_count": len(keywords_anchors),
        "ngrams_5": ngrams_5[:50],  # Top 50
        "pricing_anchors": pricing[:50],  # Top 50
        "keywords_anchors": keywords_anchors[:30],  # Top 30
    }

    # Write output
    output_path = Path(args.output)
    output_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")

    # D1 receipt
    print(f"[D1] Anchors extracted:")
    print(f"  Source: {source_path.absolute()}")
    print(f"  Length: {len(text):,} chars")
    print(f"  5-grams (score >= {args.min_score}): {len(ngrams_5)}")
    print(f"  Pricing anchors: {len(pricing)}")
    print(f"  Keyword anchors: {len(keywords_anchors)}")
    print(f"  Output: {output_path.absolute()}")


if __name__ == "__main__":
    main()
